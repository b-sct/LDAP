# User Enumeration
```Get-ADUser -Filter * | Select-Object -ExpandProperty SAMAccountName```
# Security Group Enumeration
```Get-ADGroupMember -Identity "Domain Admins" | Select-Object -ExpandProperty SamAccountName```

# Objects
### Machine Accounts
```
net computer \\pc02 /add
Set-ADAccountPassword -Identity pc02$ -Reset -NewPassword (ConvertTo-SecureString -AsPlainText "password" -Force)
```
