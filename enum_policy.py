import ldap3

server = ldap3.Server('sauna.htb',
                      port=389,
                      use_ssl=False,
                      get_info=ldap3.ALL)

connection = ldap3.Connection(server)
connection.bind()

# Get domain name (first naming context) and print intro
domain = (server.info).naming_contexts[0]
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
            print('Lockout Threshold: {}'.format(attr['lockoutThreshold'][0].decode()))
            print('Lockout Duration: {}'.format(attr['lockoutDuration'][0].decode()))
            print('Minimum Password Length: {}'.format(attr['minPwdLength'][0].decode()))
            print('Maximum Password Age: {}'.format(attr['maxPwdAge'][0].decode()))
        except:
            raise('Policy does not include 1 of the following')
