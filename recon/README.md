# Enumeration
```─$ enum4linux $(getent hosts support.htb)```
```
 ===================================( Session Check on 10.10.11.174 )===================================


[+] Server 10.10.11.174 allows sessions using username '', password ''


 ================================( Getting domain SID for 10.10.11.174 )================================

Domain Name: SUPPORT
Domain Sid: S-1-5-21-1677581083-3380853377-188903654
```
# SMB Shares
```smbclient -N -L \\\\10.10.11.174 # NULL session```
