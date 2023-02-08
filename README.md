# LDAP

LDAP is a hierarchical, client-server based directory service protocol. It allows clients to access, manage and update data stored in a directory service, typically for the purpose of user authentication and authorization, and for storing and retrieving information about network resources, such as users, groups, and devices.

DAP directories are organized in a tree-like structure, with each node in the tree called an "entry". Each entry is a collection of attributes, which describe the characteristics of the entry and can include information such as username, password, email address, and so on.

LDAP uses a series of operations, such as bind, search, compare, add, delete, and modify, to allow users that have been assigned correct permission to interact with the directory service.
```
$ nmap -p- -sV sauna.htb

PORT    STATE SERVICE    VERSION
389/tcp open  ldap       Microsoft Windows Active Directory LDAP
636/tcp open  ldapssl
```

# Kerberoasting
```
$ python enum_policy.py
```
```
#############################################
# Domain name: DC=EGOTISTICAL-BANK,DC=LOCAL #
#############################################

Lockout Threshold: 0
Lockout Duration: -18000000000
Minimum Password Length: 7
Maximum Password Age: -36288000000000
```
