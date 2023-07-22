# ADCS

AD CS is a Microsoft server role solution for public key infrastructure (PKI) that provides myriad services within an AD environment.
AD CS can provide certificate-based user authentication – which can be an extremely useful tool for managing an AD environment – but it can also be an extremely useful tool for compromising one. 

### Enumeration

```certipy``` enumerates vulnerabilities in certificate templates

```certipy find -u 'username@authority.htb' -p 'password' -dc-ip 10.10.11.222```

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

for example, the template 'CorpVPN' is vulnerable ESC1, where an enrolle from the 512 permission group can supply a subject for client authentication.

### Exploitation
attackers can then use a tool such as ```Rubeus``` to request an authentication token from Kerberos (available to any user). The attackers then use Kerberos authentication to request a certificate using the vulnerable template and specify the request is on behalf of any domain admin they choose.

if the regkey ```HKLM:\SYSTEM\CurrentControlSet\Services\Kdc\StrongCertificateBindingEnforcement``` is set to 2, attackers will have to supply the szOID_NTDS_CA_SECURITY_EXT value when making a certificate request.

```If (Test-Path "HKLM:\SYSTEM\CurrentControlSet\Services\Kdc\StrongCertificateBindingEnforcement") {(Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\Kdc").StrongCertificateBindingEnforcement}```
