# Meet ESPecter: a new UEFI bootkit for cyber spying
### The bootkit is able to load unsigned drivers to hijack the ESP.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/meet-especter-a-new-uefi-bootkit-for-cyber-spying/)
+ Date: October 6, 2021
+ Author: Charlie Osborne


## Article:
Unknown

A new bootkit for conducting covert cyberespionage that is able to compromise system partitions has been discovered. 


Researchers from ESET say [the new malware](https://www.welivesecurity.com/2021/10/05/uefi-threats-moving-esp-introducing-especter-bootkit/), dubbed ESPecter, was only found recently but the origin of the bootkit has been traced back to 2012 -- suggesting that the software is stealthy enough to have avoided detection by cybersecurity teams for the best part of a decade. 

"We traced the roots of this threat back to at least 2012; it was previously operating as a bootkit for systems with legacy BIOSes," commented ESET researcher Anton Cherepanov. "Despite ESPecter's long existence, its operations and upgrade to UEFI went unnoticed and have not been documented until now." 

The only radical change in the malware since 2012 is a shift from legacy BIOS and Master Boot Record (MBR) infiltration to modern UEFI. UEFI is a critical component in the pre-OS stage of a machine starting up and has a hand in loading an operating system.  

The malware takes root in the EFI System Partition (ESP) and persists through a patch applied to the Windows Boot Manager, however, this is yet to be fully analyzed.  

The patch allows ESPecter to bypass Windows Driver Signature Enforcement (DSE) protocols to load its own unsigned drivers on a target machine and inject other components to create a connection to the operator's command-and-control (C2) server.  

ESET found an ESPecter sample on a PC together with keylogging and document-stealing functionality modules, an indicator that the malware is likely used for surveillance purposes.  






Once executed on a target machine, ESPecter is able to deploy a backdoor containing commands for cyber spying, and alongside key logs and documents, the malicious code also takes screenshots on a regular basis and hides this content in a hidden directory.  

However, the Secure Boot feature has to be disabled for a successful ESPecter attack.  

"It's worth mentioning that the first Windows version supporting Secure Boot was Windows 8, meaning that all previous versions are vulnerable to this persistence method," the team says. 

The researchers have not found concrete evidence for attribution, but there are clues in the malware's components -- specifically debug messages -- which suggests that the threat actors are Chinese-speaking.  

It is also not known how ESPecter is distributed; however, there are a number of potential scenarios: an attacker has physical access to a target machine, Secure Boot has already been disabled, or the exploit of either a zero-day UEFI bug or a known, but unpatched, security flaw in legacy software.  

"Even though Secure Boot stands in the way of executing untrusted UEFI binaries from the ESP, over the last few years we have been witness to various UEFI firmware vulnerabilities affecting thousands of devices that allow disabling or bypassing Secure Boot," ESET says. "This shows that securing UEFI firmware is a challenging task and that the way various vendors apply security policies and use UEFI services is not always ideal." 

###  Previous and related coverage

* [Chinese hacker group spotted using a UEFI bootkit in the wild](https://www.zdnet.com/article/chinese-hacker-group-spotted-using-a-uefi-bootkit-in-the-wild/)  

* [FinSpy surveillance malware is now spreading through UEFI bootkits](https://www.zdnet.com/article/finspy-surveillance-malware-is-now-spreading-through-uefi-bootkits/)  

* [New Moriya rootkit stealthily backdoors Windows systems](https://www.zdnet.com/article/new-moriya-rootkit-stealthily-backdoors-windows-systems/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[UEFI]] [[ESPecter]] [[malware]] [[Windows]] [[bootkit]] [[ESET]] [[ZDNet]]
