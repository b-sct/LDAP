# LDAP

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
