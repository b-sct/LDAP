# LDAP

LDAP is a hierarchical, client-server based directory service protocol. It allows clients to access, manage and update data stored in a directory service, typically for the purpose of user authentication and authorization, and for storing and retrieving information about network resources, such as users, groups, and devices.

DAP directories are organized in a tree-like structure, with each node in the tree called an "entry". Each entry is a collection of attributes, which describe the characteristics of the entry and can include information such as username, password, email address, and so on.

LDAP uses a series of operations, such as bind, search, compare, add, delete, and modify, to allow users that have been assigned correct permission to interact with the directory service.

Microsoft's implementation of LDAP on Windows servers is a directory service built into the Windows Server operating system. It is often referred to as Active Directory Domain Services (AD DS) and is used for managing and organizing information about network resources in a Windows environment, such as user accounts, groups, computers, and other devices.

In AD DS, LDAP is used as the underlying protocol for communication between clients and servers.
```
$ nmap -p- -sV sauna.htb

389/tcp open  ldap       Microsoft Windows Active Directory LDAP (Domain: MCDONALDS.LOCAL, Site: Default-First-Site-Name)
636/tcp open  ldapssl
Service Info: Host: DC-01; OS: Windows; CPE: cpe:/o:microsoft:windows
```
# Enumerating the domain

```
$ python enum_policy.py

#############################################
# Domain name: DC=MCDONALDS,DC=LOCAL #
#############################################

**Lockout Threshold: 0**
Lockout Duration: -18000000000
Minimum Password Length: 7
Maximum Password Age: -36288000000000
```

```
$ ldapsearch -h 10.10.11.168 -x -s base namingcontexts
```
