import argparse
from ldap3 import Server, Connection, ALL, DEREF_ALWAYS, ALL_ATTRIBUTES

def connect(server, user, password):
    server = Server(server, get_info=ALL)
    conn = Connection(server, user, password, auto_bind=True)
    return conn

def search(conn, query, attributes):
    conn.search(query, '(objectclass=*)', attributes=attributes, dereference_aliases=DEREF_ALWAYS)

def get_all_objects(conn, realm):
    base_dn = 'dc=' + realm.replace('.', ',dc=')
    search(conn, base_dn, ALL_ATTRIBUTES)

def get_all_users(conn, realm):
    base_dn = 'dc=' + realm.replace('.', ',dc=')
    conn.search(base_dn, '(objectclass=user)', attributes=ALL_ATTRIBUTES, dereference_aliases=DEREF_ALWAYS)

def get_all_OUs_and_users(conn, realm):
    base_dn = 'dc=' + realm.replace('.', ',dc=')
    conn.search(base_dn, '(objectclass=organizationalUnit)', attributes=['ou'], dereference_aliases=DEREF_ALWAYS)
    for entry in conn.entries:
        print(entry)
        search(conn, str(entry.entry_dn), ALL_ATTRIBUTES)

def print_entries(entries):
    for entry in entries:
        print("CN: " + str(entry.entry_dn))
        print(entry.entry_attributes_as_dict)
        print("-------------------------------")

def main():
    parser = argparse.ArgumentParser(
    description='''Perform LDAP queries.

    Example:
    python ldapsearch.py support.htb --user 'support\ldap' --password 'nvEaEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz' --realm support.htb --query all_users''',
    epilog='''Additional Example:
    python ldapsearch.py --server ldap.example.com --realm example.com --query all_objects'''
)
    parser.add_argument('server', help='LDAP server address')
    parser.add_argument('--user', help='Username for LDAP server', default=None)
    parser.add_argument('--password', help='Password for LDAP server', default=None)
    parser.add_argument('--realm', help='Realm for LDAP server', required=True)
    parser.add_argument('--query', help='Query to run. Options are: all_objects, all_users, all_OUs_and_users', default='all_objects')

    args = parser.parse_args()

    conn = connect(args.server, args.user, args.password)

    if args.query == 'all_objects':
        get_all_objects(conn, args.realm)
    elif args.query == 'all_users':
        get_all_users(conn, args.realm)
    elif args.query == 'all_OUs_and_users':
        get_all_OUs_and_users(conn, args.realm)

    print_entries(conn.entries)

if __name__ == "__main__":
    main()

