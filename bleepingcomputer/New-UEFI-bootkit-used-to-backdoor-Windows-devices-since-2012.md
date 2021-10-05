# New UEFI bootkit used to backdoor Windows devices since 2012
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-uefi-bootkit-used-to-backdoor-windows-devices-since-2012/)
+ Date: October 5, 2021
+ Author: Sergiu Gatlan


## Article:
![New UEFI bootkit used to backdoor Windows devices since 2012](https://www.bleepstatic.com/content/hl-images/2021/10/05/Windows-keyboard.jpg)


*Image: [Jeff Hardi](https://unsplash.com/@jeffhardi)*


A newly discovered and previously undocumented UEFI (Unified Extensible Firmware Interface) bootkit has been used by attackers to backdoor Windows systems by hijacking the Windows Boot Manager since 2012.


Bootkits are malicious code planted in the firmware (sometimes targeting UEFI) invisible to security software that runs within the operating system since the malware is designed to load before everything else, in the initial stage of the booting sequence.


They provide threat actors with persistence and control over an operating systems' boot process, making it possible to sabotage OS defenses bypassing the Secure Boot mechanism if the system boot security mode is not properly configured. Enabling 'thorough boot' or 'full boot' mode would block such malware as the NSA [explains](https://media.defense.gov/2020/Sep/15/2002497594/-1/-1/0/CTR-UEFI-SECURE-BOOT-CUSTOMIZATION-20200915.PDF/CTR-UEFI-SECURE-BOOT-CUSTOMIZATION-20200915.PDF)).


Persistence on the EFI System Partition
---------------------------------------


The bootkit, dubbed ESPecter by ESET researchers who found it, achieves persistence on the EFI System Partition (ESP) of compromised devices by loading its own unsigned driver to bypass Windows Driver Signature Enforcement.


"ESPecter was encountered on a compromised machine along with a user-mode client component with keylogging and document-stealing functionalities, which is why we believe ESPecter is mainly used for espionage," ESET security researchers Martin Smolár and Anton Cherepanov [said](https://www.welivesecurity.com/2021/10/05/uefi-threats-moving-esp-introducing-especter-bootkit/).


"Interestingly, we traced the roots of this threat back to at least 2012, previously operating as a bootkit for systems with legacy BIOSes."


The malicious driver deployed on compromised Windows computers is used to load two payloads (WinSys.dll and Client.dll) that can also download and execute additional malware.


WinSys.dll is an update agent, the component used to reach out to the command-and-control (C2) server for further commands or more malicious payloads.


As the researchers found, WinSys.dll can exfiltrate system info, launch other malware downloaded from the C2 server, restart the PC using ExitProcess (only on Windows Vista), and get new configuration info and save it to the registry.


Client.dll, the second payload, acts as a backdoor with automatic data exfiltration capabilities, including keylogging, document stealing, and screen monitoring via screenshots.


ESET also found ESPecter versions that target Legacy Boot modes and achieving persistence by altering the MBR code found in the first physical sector of the system disk drive.



![Normal Windows UEFI boot vs boot flow modified by ESPecte](https://www.bleepstatic.com/images/news/u/1109292/2021/Normal_Windows_UEFI_boot_vs_boot_flow_modified_by_ESPecte.png)*Normal Windows UEFI boot vs. boot flow modified by ESPecter (ESET)*
Secure Boot doesn't really help
-------------------------------


Patching the Windows Boot Manager (bootmgfw.efi) requires for Secure Boot (which helps check if the PC boots using trusted firmware) to be disabled.


As the researchers discovered, attackers have deployed the bootkit in the wild, which means they've found a method to toggle off Secure Boot on targeted devices.


Even though right not there's no hint of how the ESPecter operators achieved this, there are a few possible scenarios:


* The attacker has physical access to the device (historically known as an "evil maid" attack) and manually disables Secure Boot in the BIOS setup menu (it is common for the firmware configuration menu to still be labeled and referred to as the "BIOS setup menu," even on UEFI systems).
* Secure Boot was already disabled on the compromised machine (e.g., a user might dual-boot Windows and other OSes that do not support Secure Boot).
* Exploiting an unknown UEFI firmware vulnerability that allows disabling Secure Boot.
* Exploiting a known UEFI firmware vulnerability (e.g., [CVE-2014-2961](http://web.nvd.nist.gov/vuln/detail/CVE-2014-2961), [CVE-2014-8274](http://web.nvd.nist.gov/vuln/detail/CVE-2014-8274), or [CVE-2015-0949](http://web.nvd.nist.gov/vuln/detail/CVE-2015-0949)) in the case of an outdated firmware version or a no-longer-supported product.


Publicly documented attacks using bootkits in the wild are extremely rare — the [FinSpy bootkit](https://www.bleepingcomputer.com/news/security/finfisher-malware-hijacks-windows-boot-manager-with-uefi-bootkit/) used to load spyware, [Lojax](https://www.bleepingcomputer.com/news/security/apt28-uses-lojax-first-uefi-rootkit-seen-in-the-wild/) deployed by the Russian-backed APT28 hacker group, [MosaicRegressor](https://www.bleepingcomputer.com/news/security/mosaicregressor-second-ever-uefi-rootkit-found-in-the-wild/) used by Chinese-speaking hackers, and the [TrickBoot module](https://www.bleepingcomputer.com/news/security/trickbots-new-trickboot-module-infects-your-uefi-firmware/) used by the TrickBot gang.


"ESPecter shows that threat actors are relying not only on UEFI firmware implants when it comes to pre-OS persistence and, despite the existing security mechanisms like UEFI Secure Boot, invest their time into creating malware that would be easily blocked by such mechanisms, if enabled and configured correctly."


To secure your systems against attacks using bootkits like ESPecter, you are advised to ensure that:


* You always use the latest firmware version.
* Your system is properly configured, and Secure Boot is enabled.
* You apply proper [Privileged Account Management](https://attack.mitre.org/mitigations/M1026) to help prevent adversaries from accessing privileged accounts necessary for bootkit installation.


Further technical details on the ESPecter bootkit and indicators of compromise can be found in [ESET's report](https://www.welivesecurity.com/2021/10/05/uefi-threats-moving-esp-introducing-especter-bootkit/). 




#### Tags:
[[Windows]] [[UEFI]] [[bootkit]] [[ESPecter]] [[malware]] [[ESET]] [[Bleeping Computer]]
