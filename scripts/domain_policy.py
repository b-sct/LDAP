import sys
import ldap3

if len(sys.argv) < 4:
    print("Usage: python domain_policy.py <server> <username> <password> [-ssl]")
    print("Example: python domain_policy.py support.htb 'support\support' 'Ironside47pleasure40Watchful'")
    sys.exit(1)

server_name = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
use_ssl = False

if "-ssl" in sys.argv:
    use_ssl = True

port = 636 if use_ssl else 389

server = ldap3.Server(server_name, port=port, use_ssl=use_ssl, get_info=ldap3.ALL)

connection = ldap3.Connection(server, username, password)
connection.bind()

# Get domain name (first naming context) and print intro
domain = server.info.naming_contexts[0]
intro = 'Domain name: {}'.format(domain)
print('#' * (len(intro) + 4))
print('# {} #'.format(intro))
print('#' * (len(intro) + 4) + '\n')

# Search all objects in the tree
connection.search(search_base=domain,
                  search_scope='SUBTREE',
                  search_filter="(&(objectClass=*))",
                  attributes='*')

for entry in connection.entries:
    if entry.entry_raw_attributes.keys():
        attr = entry.entry_raw_attributes
        # The policy might be open to be read by anon
        try:
            if 'lockoutThreshold' in attr.keys():  # found entry containing lockout settings
                print('-------------------------------')
                print(attr['objectGUID'])
                print(attr['objectSid'])
                print(attr['objectClass'])
                print(attr['objectCategory'])
                print(attr['gPlink'])  # could be a link to the gpo that holds these settings
            print('lockoutThreshold: {}'.format(attr['lockoutThreshold']))
            print('lockoutDuration: {}'.format(attr['lockoutDuration']))
            print('minPwdAge: {}'.format(attr['minPwdAge']))
            print('maxPwdAge: {}'.format(attr['maxPwdAge']))
            print('minPwdLength: {}'.format(attr['minPwdLength']))
            print('modifiedCount: {}'.format(attr['modifiedCount']))
            print('pwdProperties: {}'.format(attr['pwdProperties']))
            print('--------------------------------')
        except:
            pass
