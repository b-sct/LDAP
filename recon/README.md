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
Enumeration
```smbclient -N -L \\\\10.10.11.174 # NULL session```
```        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share
        support-tools   Disk      support staff tools
        SYSVOL          Disk      Logon server share
```
```smbclient -N \\\\10.10.11.174\\support-tools```
```smbclient -L \\\\10.10.11.174 -U 'support\guest'```
