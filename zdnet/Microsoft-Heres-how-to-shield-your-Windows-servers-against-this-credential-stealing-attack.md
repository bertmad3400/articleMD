# Microsoft: Here's how to shield your Windows servers against this credential stealing attack
### Microsoft outlines how to mitigate the NTLM Relay Attack known as PetitPotam.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/microsoft-heres-how-to-shield-your-windows-servers-against-this-credential-stealing-attack/)
+ Date: July 26, 2021 -- 12:07 GMT (13:07 BST)
+ Author: Liam Tung


## Article:
Unknown

Microsoft has posted an advisory and detailed instructions on how to protect Windows domain controllers and other Windows servers from the NTLM Relay Attack known as PetitPotam.


The PetitPotam take on the NTLM Relay attack was discovered last week by French security researcher Gilles Lionel, as [first reported by The Record](https://therecord.media/new-petitpotam-attack-forces-windows-hosts-to-share-their-password-hashes/). The tool Lionel posted can "coerce Windows hosts to authenticate to other machines via MS-EFSRPC EfsRpcOpenFileRaw function," he explains. 

In other words, the attack can make a remote Windows server authenticate with an attacker and share Microsoft NTLM authentication credentials and certificates. 

Microsoft notes that PetitPotam "is a classic NTLM Relay Attack" that it describes [in a 2009 security security advisory](https://docs.microsoft.com/en-us/security-updates/SecurityAdvisories/2009/974926), which it says "can potentially be used in an attack on Windows domain controllers or other Windows servers."

It says customers may be vulnerable to PetitPotam if NTLM authentication is enabled on a domain and Active Directory Certificate Services (AD CS) is in use with Certificate Authority Web Enrollment or Certificate Enrollment Web Service. 

To prevent NTLM Relay Attacks that meet these conditions, Microsoft advises domain admins to ensure that services that permit NTLM authentication must "make use of protections such as [Extended Protection for Authentication (EPA)](https://docs.microsoft.com/en-us/security-updates/securityadvisories/2009/973811) or signing features such as SMB signing."

"PetitPotam takes advantage of servers where Active Directory Certificate Services (AD CS) is not configured with protections for NTLM Relay Attacks," [Microsoft notes in ADV210003](https://msrc.microsoft.com/update-guide/vulnerability/ADV210003).  






Microsoft has provided more [detailed mitigation instructions in a separate KB article, KB5005413](https://support.microsoft.com/en-gb/topic/kb5005413-mitigating-ntlm-relay-attacks-on-active-directory-certificate-services-ad-cs-3612b773-4043-4aa9-b23d-b87910cd3429). Microsoft's "preferred mitigation" is disabling NTLM authentication on a Windows domain controller. 

But it also has detailed and graphical instructions for alternative mitigations if it's not possible to disable NTLM authentication on a domain. "They are listed in order of more secure to less secure," [it notes](https://support.microsoft.com/en-gb/topic/kb5005413-mitigating-ntlm-relay-attacks-on-active-directory-certificate-services-ad-cs-3612b773-4043-4aa9-b23d-b87910cd3429).





#### Tags:
[[NTLM]] [[Microsoft]] [[Windows]] [[PetitPotam]] [[ZDNet]]
