# ADCS

if the regkey ```HKLM:\SYSTEM\CurrentControlSet\Services\Kdc\StrongCertificateBindingEnforcement``` is set to 2, attackers will have to supply the szOID_NTDS_CA_SECURITY_EXT value when making a certificate request.
```If (Test-Path "HKLM:\SYSTEM\CurrentControlSet\Services\Kdc\StrongCertificateBindingEnforcement") {(Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\Kdc").StrongCertificateBindingEnforcement}```
