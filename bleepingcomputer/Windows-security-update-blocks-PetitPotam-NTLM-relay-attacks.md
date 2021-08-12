# Windows security update blocks PetitPotam NTLM relay attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-security-update-blocks-petitpotam-ntlm-relay-attacks/)
+ Date: August 10, 2021
+ Author: Lawrence Abrams


## Article:
![Microsoft Windows](https://www.bleepstatic.com/content/hl-images/2021/07/09/Windows_headpic.jpg)


Microsoft has released security updates that block the PetitPotam NTLM relay attack that allows a threat actor to take over a Windows domain.


In July, security researcher GILLES Lionel, aka [Topotam](https://twitter.com/topotam77), disclosed a [new method called PetitPotam](https://www.bleepingcomputer.com/news/microsoft/new-petitpotam-attack-allows-take-over-of-windows-domains/) that forces a domain controller to authenticate against a threat actor's server using the MS-EFSRPC API functions.



Using the PetitPotam vector, a threat actor can use the Windows LSARPC interface to communicate and execute MS-EFSRPC API functions without authentication. The functions, OpenEncryptedFileRawA and OpenEncryptedFileRawW, allow the threat actor to force a domain controller to authenticate to an NTLM relay server under the attacker's control.


The NTLM relay would forward the request to a victim's Active Directory Certificate Services via HTTP to receive a Kerberos ticket-granting ticket (TGT) that allows the threat actor to assume the identity of any device on the network, including a domain controller.


This NTLM relay attack allows the threat actor to take over the domain controller, and thus the Windows domain.


In July, Microsoft released a [security advisory](http://support.microsoft.com/en-us/topic/kb5005413-mitigating-ntlm-relay-attacks-on-active-directory-certificate-services-ad-cs-3612b773-4043-4aa9-b23d-b87910cd3429) explaining how to mitigate NTLM relay attacks targeting Active Directory Certificate Services (AD CS).


However, Microsoft provided no information on blocking the PetitPotam vector until researchers discovered [how to secure it using NETSH filters](https://www.bleepingcomputer.com/news/microsoft/windows-petitpotam-attacks-can-be-blocked-using-new-method/).


Microsoft blocks the PetitPotam vector
--------------------------------------


As part of the [August 2021 Patch Tuesday updates](https://www.bleepingcomputer.com/news/microsoft/microsoft-august-2021-patch-tuesday-fixes-3-zero-days-44-flaws/), Microsoft has released a security update that blocks the PetitPotam vector ([CVE-2021-36942](http://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-36942)), so it cannot force a domain controller to authenticate against another server.:


"An unauthenticated attacker could call a method on the LSARPC interface and coerce the domain controller to authenticate against another server using NTLM," explains Microsoft in the CVE-2021-36942 advisory.


"This security update blocks the affected API calls OpenEncryptedFileRawA and OpenEncryptedFileRawW through LSARPC interface."


Microsoft warns that installing this update may affect backup software that utilizes the EFS API OpenEncryptedFileRaw(A/W) function.


"The EFS API OpenEncryptedFileRaw(A/W), often used in backup software, continues to work in all versions of Windows (local and remote), except when backing up to or from a system running Windows Server 2008 SP2. OpenEncryptedFileRaw will no longer work on Windows Server 2008 SP2," warns Microsoft.


If your backup software no longer works after installing this update on Windows 7 Service Pack 1 or Windows Server 2008 R2 Service Pack 1 and later, Microsoft suggests you contact your backup software developer to get an updated version.




#### Tags:
[[Microsoft]] [[Windows]] [[PetitPotam]] [[NTLM]] [[API]] [[LSARPC]] [[Bleeping Computer]]
