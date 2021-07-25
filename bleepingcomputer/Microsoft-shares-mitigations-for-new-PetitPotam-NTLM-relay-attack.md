# Microsoft shares mitigations for new PetitPotam NTLM relay attack
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/microsoft-shares-mitigations-for-new-petitpotam-ntlm-relay-attack/)
+ Date: July 24, 2021
+ Author: Ionut Ilascu


## Article:
![Microsoft shares mitigations for new PetitPotam NTML relay attack](https://www.bleepstatic.com/content/hl-images/2021/07/09/Windows_headpic.jpg)


Microsoft has released mitigations for the new PetitPotam NTLM relay attack that allows taking over a domain controller or other Windows servers.


PetitPotam is a new method that can be used to conduct an NTLM relay attack discovered by French security researcher Gilles Lionel ([Topotam](https://twitter.com/topotam77)). This method was disclosed this week along with a proof-of-concept (PoC) script.


The new attack uses the Microsoft Encrypting File System Remote Protocol ([EFSRPC](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-efsr/08796ba8-01c8-4872-9221-1000ec2eff31)) to force a device, including domain controllers, to authenticate to a remote NTLM relay controlled by a threat actor.


Once a device authenticates to a malicious NTLM server, a threat actor can steal hash and certificates that can be used to assume the identity of the device and its privileges.


### Mitigation limited to Domain Controllers


After news of the [PetitPotam NTLM relay](https://www.bleepingcomputer.com/news/microsoft/new-petitpotam-attack-allows-take-over-of-windows-domains/) attack broke yesterday, Microsoft published a security advisory with recommendations for organizations to defend against threat actors using the new technique on domain controllers.


The company says that organizations exposed to PetitPotam, or other relay attacks, have NTLM authentication enabled on the domain and are using Active Directory Certificate Services (AD CS) with Certificate Authority Web Enrollment or Certificate Enrollment Web Service.


In a [tweet](https://twitter.com/msftsecresponse/status/1419025196044865539) earlier today, Microsoft recommends disabling NTLM where it is not necessary, e.g. Domain Controllers, or to enable the [Extended Protection for Authentication](https://msrc-blog.microsoft.com/2009/12/08/extended-protection-for-authentication/) mechanism to protect credentials on Windows machines.



![Microsoft advisory on PetitPotam NTLM relay attack](https://www.bleepstatic.com/images/news/u/1100723/2021/PetitPotamMS.jpg)source: [Microsoft](https://twitter.com/msftsecresponse/status/1419025196044865539)
The company also recommends on networks with NTLM enabled that services allowing NTLM authentication to use signing features such as SMB signing that’s been available since Windows 98.



“PetitPotam takes advantage of servers where Active Directory Certificate Services (AD CS) is not configured with protections for NTLM Relay Attacks [as outlined in [KB5005413](https://support.microsoft.com/help/5005413)]” - Microsoft



However, PetitPotam is about abusing the EfsRpcOpenFileRaw function of the MS-EFSRPC API to pass on authentication requests, leaving the door open for other attacks.


Microsoft”s advisory is clear about the action to prevent NTLM relay attacks but does not address the abuse of the MS-EFSRPC API, which would need a security update to fix.


Gilles Lionel told BleepingComputer that PetitPotam allows other atacks, such as a downgrading attack to NTLMv1 that uses the Data Encryption Standard (DES) - an insecure algorithm due to its short, 56-bit key generation that makes it easy to recover a password hash.


One example, Gilles Lionel told BleepingComputer, is a downgrading attack to NTLMv1 that uses the Data Encryption Standard (DES) - an insecure algorithm due to its short, 56-bit key generation that makes it easy to recover a password hash.


An attacker can then use the account on machines where it has local admin privileges. Lionel says that Exchange and Microsoft System Center Configuration Manager ([SCCM](https://docs.microsoft.com/en-us/mem/configmgr/core/understand/what-happened-to-sccm)) servers are a common scenario.


[Benjamin Delpy](https://twitter.com/gentilkiwi) expressed criticism at the way Microsoft decided to mitigate PetitPotam, [highlighting](https://twitter.com/gentilkiwi/status/1419034669027401735) that the EFSRPC protocol is not even mentioned in the advisory.


PetitPotam affects Windows Server 2008 through 2019. Microsoft’s advisory notes that the technique has not been exploited in the wild yet but has no assessment about the exploitability level.




#### Tags:
[[NTLM]] [[Microsoft]] [[PetitPotam]] [[Windows]] [[-]] [[Bleeping Computer]]
