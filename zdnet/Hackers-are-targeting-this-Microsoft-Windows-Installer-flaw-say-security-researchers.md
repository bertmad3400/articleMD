# Hackers are targeting this Microsoft Windows Installer flaw, say security researchers
### Flaw can be exploited to give an attacker administrator rights on a compromised system, despite efforts to fix the problem.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/hackers-are-targeting-this-microsoft-windows-installer-flaw-say-security-researchers/)
+ Date: November 26, 2021
+ Author: Liam Tung


## Article:
Unknown

Hackers have already created malware in a bid to exploit an elevation of privilege vulnerability in Microsoft's Windows Installer.

Microsoft released a patch for [CVE-2021-41379](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41379), an elevation of privilege flaw in the [Windows Installer component](https://docs.microsoft.com/en-us/windows/win32/msi/windows-installer-portal) for enterprise application deployment. It had an "important" rating and a severity score of just 5.5 out of 10. 


It wasn't actively being exploited at the time, but it is now, according to Cisco's Talos malware researchers. And Cisco reports that the bug can be exploited even on systems with the November patch to give an attacker administrator-level privileges. 

**SEE:** [**Windows 11 FAQ: Our upgrade guide and everything else you need to know**](https://www.zdnet.com/article/windows-11-faq-heres-everything-you-need-to-know/)

This, however, contradicts [Microsoft's assessment that](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41379) an attacker would only be able to delete targeted files on a system and would not gain privileges to view or modify file contents.

"This vulnerability allows an attacker with a limited user account to elevate their privileges to become an administrator," [explains Jaeson Schultz at Cisco Talos](https://blog.talosintelligence.com/2021/11/attackers-exploiting-zero-day.html). 

"This vulnerability affects every version of Microsoft Windows, including fully patched Windows 11 and Server 2022. Talos has already detected malware samples in the wild that are attempting to take advantage of this vulnerability."






Abdelhamid Naceri, the researcher who reported CVE-2021-41379 to Microsoft, tested patched systems and on November 22 [published proof-of-concept exploit code on GitHub](https://github.com/klinix5/InstallerFileTakeOver), which shows that it works despite Microsoft's fixes. It also works on Server versions of affected Windows, including Windows Server 2022. 

"The code Naceri released leverages the discretionary access control list (DACL) for Microsoft Edge Elevation Service to replace any executable file on the system with an MSI file, allowing an attacker to run code as an administrator," writes Cisco's Shultz.

**SEE:** [**Dark web crooks are now teaching courses on how to build botnets**](https://www.zdnet.com/article/college-for-cyber-criminals-dark-web-crooks-are-teaching-courses-on-how-to-build-botnets/#link=%7B%22role%22:%22standard%22,%22href%22:%22https://www.zdnet.com/article/college-for-cyber-criminals-dark-web-crooks-are-teaching-courses-on-how-to-build-botnets/%22,%22target%22:%22_blank%22,%22absolute%22:%22%22,%22linkText%22:%22Dark%20web%20crooks%20are%20now%20teaching%20courses%20on%20how%20to%20build%20botnets%22%7D)

He adds that this "functional proof-of-concept exploit code will certainly drive additional abuse of this vulnerability." 

Naceri says there is no workaround for this bug other than another patch from Microsoft. 

"Due to the complexity of this vulnerability, any attempt to patch the binary directly will break Windows Installer. So you'd better wait and see how/if Microsoft will screw the patch up again," Naceri said. Microsoft is yet to acknowledge Naceri's new proof of concept and has not yet said whether it will issue a patch for it. 





#### Tags:
[[Microsoft]] [[Windows]] [[Naceri]] [[malware]] [[ZDNet]]
