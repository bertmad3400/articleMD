# Microsoft October 2021 Patch Tuesday fixes 4 zero-days, 71 flaws
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-october-2021-patch-tuesday-fixes-4-zero-days-71-flaws/)
+ Date: October 12, 2021
+ Author: Lawrence Abrams


## Article:

![Patch Tuesday](https://www.bleepstatic.com/images/stock-photos/operating-systems/windows-10/patch-tuesday-large.jpg)



Today is Microsoft's October 2021 Patch Tuesday, and with it comes fixes for four zero-day vulnerabilities and a total of 74 flaws.


Microsoft has fixed 74 vulnerabilities (81 including Microsoft Edge) with today's update, with three classified as Critical, and 70 as Important, and one as Low.


These 81 vulnerabilities (including Microsoft Edge) are classified as:


* 21 Elevation of Privilege Vulnerabilities
* 6 Security Feature Bypass Vulnerabilities
* 20 Remote Code Execution Vulnerabilities
* 13 Information Disclosure Vulnerabilities
* 5 Denial of Service Vulnerabilities
* 9 Spoofing Vulnerabilities


Four zero-days fixed, with one actively exploited
-------------------------------------------------


October's Patch Tuesday includes fixes for four zero-day vulnerabilities, with a Win32k Elevation of Privilege Vulnerability vulnerability known to have been actively exploited in attacks.


Microsoft classifies a vulnerability as a zero-day if it is publicly disclosed or actively exploited with no official fix available.


The actively exploited vulnerability was discovered by Kaspersk's [Boris Larin (oct0xor)](https://twitter.com/oct0xor) and allows malware or a threat actor to gain elevated privileges on a Windows device.


* [CVE-2021-40449](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-40449) - Win32k Elevation of Privilege Vulnerability


Kaspersky [disclosed today](https://securelist.com/mysterysnail-attacks-with-windows-zero-day/104509/) that the vulnerability was used by threat actors in "widespread espionage campaigns against IT companies, military/defense contractors, and diplomatic entities." 


As part of the attacks, the threat actors installed a remote access trojan (RAT) that was elevated with higher permissions using the zero-day Windows vulnerability. 


Kaspersky calls this cluster of malicious activity MysterSnail and is attributed to the IronHusky and Chinese-speaking APT activity.


Microsoft also fixed three other publicly disclosed vulnerabilities that are not known to be exploited in attacks.


* [CVE-2021-40469](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-40469) - Windows DNS Server Remote Code Execution Vulnerability
* [CVE-2021-41335](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-41335) - Windows Kernel Elevation of Privilege Vulnerability
* [CVE-2021-41338](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-41338) - Windows AppContainer Firewall Rules Security Feature Bypass Vulnerability


Recent updates from other companies
-----------------------------------


Other vendors who released updates in July include:


* **Adobe's** [October security updates](https://helpx.adobe.com/security/security-bulletin.html) were released for various applications.
* **Android's** October security updates were [released](https://www.bleepingcomputer.com/news/security/android-october-patch-fixes-three-critical-bugs-41-flaws-in-total/) last week.
* **Apache** [released HTTP Web Server 2.4.51](https://www.bleepingcomputer.com/news/security/apache-emergency-update-fixes-incomplete-patch-for-exploited-bug/) to fix an incompete patch for an actively exploited vulnerability.
* **Apple** released [security updates](https://support.apple.com/en-us/HT212846) for iOS and iPadOS yesterday that an actively exploited zero-day vulnerability.
* **Cisco** [released security updates](https://tools.cisco.com/security/center/publicationListing.x) for numerous products this month.
* **SAP** [released](https://wiki.scn.sap.com/wiki/x/v4D-Ig) its October 2021 security updates.
* **VMware** [released a security update](https://www.vmware.com/security/advisories/VMSA-2021-0021.html) for VMware vRealize Operations.


The October 2021 Patch Tuesday Security Updates
-----------------------------------------------


Below is the complete list of resolved vulnerabilities and released advisories in the October 2021 Patch Tuesday updates. To access the full description of each vulnerability and the systems that it affects, you can view the [full report here](https://www.bleepingcomputer.com/microsoft-patch-tuesday-reports/October-2021.html).





| Tag | CVE ID | CVE Title | Severity |
| --- | --- | --- | --- |
| .NET Core & Visual Studio | [CVE-2021-41355](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41355) | .NET Core and Visual Studio Information Disclosure Vulnerability | Important |
| Active Directory Federation Services | [CVE-2021-41361](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41361) | Active Directory Federation Server Spoofing Vulnerability | Important |
| Console Window Host | [CVE-2021-41346](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41346) | Console Window Host Security Feature Bypass Vulnerability | Important |
| HTTP.sys | [CVE-2021-26442](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26442) | Windows HTTP.sys Elevation of Privilege Vulnerability | Important |
| Microsoft DWM Core Library | [CVE-2021-41339](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41339) | Microsoft DWM Core Library Elevation of Privilege Vulnerability | Important |
| Microsoft Dynamics | [CVE-2021-40457](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40457) | Microsoft Dynamics 365 Customer Engagement Cross-Site Scripting Vulnerability | Important |
| Microsoft Dynamics | [CVE-2021-41353](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41353) | Microsoft Dynamics 365 (on-premises) Spoofing Vulnerability | Important |
| Microsoft Dynamics | [CVE-2021-41354](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41354) | Microsoft Dynamics 365 (on-premises) Cross-site Scripting Vulnerability | Important |
| Microsoft Edge (Chromium-based) | [CVE-2021-37978](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-37978) | Chromium: CVE-2021-37978 Heap buffer overflow in Blink | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-37979](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-37979) | Chromium: CVE-2021-37979 Heap buffer overflow in WebRTC | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-37980](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-37980) | Chromium: CVE-2021-37980 Inappropriate implementation in Sandbox | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-37977](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-37977) | Chromium: CVE-2021-37977 Use after free in Garbage Collection | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-37974](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-37974) | Chromium: CVE-2021-37974 Use after free in Safe Browsing | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-37975](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-37975) | Chromium: CVE-2021-37975 Use after free in V8 | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-37976](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-37976) | Chromium: CVE-2021-37976 Information leak in core | Unknown |
| Microsoft Exchange Server | [CVE-2021-26427](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26427) | Microsoft Exchange Server Remote Code Execution Vulnerability | Important |
| Microsoft Exchange Server | [CVE-2021-34453](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34453) | Microsoft Exchange Server Denial of Service Vulnerability | Important |
| Microsoft Exchange Server | [CVE-2021-41348](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41348) | Microsoft Exchange Server Elevation of Privilege Vulnerability | Important |
| Microsoft Exchange Server | [CVE-2021-41350](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41350) | Microsoft Exchange Server Spoofing Vulnerability | Important |
| Microsoft Graphics Component | [CVE-2021-41340](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41340) | Windows Graphics Component Remote Code Execution Vulnerability | Important |
| Microsoft Intune | [CVE-2021-41363](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41363) | Intune Management Extension Security Feature Bypass Vulnerability | Important |
| Microsoft Office Excel | [CVE-2021-40473](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40473) | Microsoft Excel Remote Code Execution Vulnerability | Important |
| Microsoft Office Excel | [CVE-2021-40472](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40472) | Microsoft Excel Information Disclosure Vulnerability | Important |
| Microsoft Office Excel | [CVE-2021-40471](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40471) | Microsoft Excel Remote Code Execution Vulnerability | Important |
| Microsoft Office Excel | [CVE-2021-40474](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40474) | Microsoft Excel Remote Code Execution Vulnerability | Important |
| Microsoft Office Excel | [CVE-2021-40485](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40485) | Microsoft Excel Remote Code Execution Vulnerability | Important |
| Microsoft Office Excel | [CVE-2021-40479](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40479) | Microsoft Excel Remote Code Execution Vulnerability | Important |
| Microsoft Office SharePoint | [CVE-2021-40487](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40487) | Microsoft SharePoint Server Remote Code Execution Vulnerability | Important |
| Microsoft Office SharePoint | [CVE-2021-40483](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40483) | Microsoft SharePoint Server Spoofing Vulnerability | Low |
| Microsoft Office SharePoint | [CVE-2021-40484](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40484) | Microsoft SharePoint Server Spoofing Vulnerability | Important |
| Microsoft Office SharePoint | [CVE-2021-40482](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40482) | Microsoft SharePoint Server Information Disclosure Vulnerability | Important |
| Microsoft Office SharePoint | [CVE-2021-41344](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41344) | Microsoft SharePoint Server Remote Code Execution Vulnerability | Important |
| Microsoft Office Visio | [CVE-2021-40480](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40480) | Microsoft Office Visio Remote Code Execution Vulnerability | Important |
| Microsoft Office Visio | [CVE-2021-40481](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40481) | Microsoft Office Visio Remote Code Execution Vulnerability | Important |
| Microsoft Office Word | [CVE-2021-40486](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40486) | Microsoft Word Remote Code Execution Vulnerability | Critical |
| Microsoft Windows Codecs Library | [CVE-2021-40462](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40462) | Windows Media Foundation Dolby Digital Atmos Decoders Remote Code Execution Vulnerability | Important |
| Microsoft Windows Codecs Library | [CVE-2021-41330](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41330) | Microsoft Windows Media Foundation Remote Code Execution Vulnerability | Important |
| Microsoft Windows Codecs Library | [CVE-2021-41331](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41331) | Windows Media Audio Decoder Remote Code Execution Vulnerability | Important |
| Rich Text Edit Control | [CVE-2021-40454](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40454) | Rich Text Edit Control Information Disclosure Vulnerability | Important |
| Role: DNS Server | [CVE-2021-40469](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40469) | Windows DNS Server Remote Code Execution Vulnerability | Important |
| Role: Windows Active Directory Server | [CVE-2021-41337](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41337) | Active Directory Security Feature Bypass Vulnerability | Important |
| Role: Windows AD FS Server | [CVE-2021-40456](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40456) | Windows AD FS Security Feature Bypass Vulnerability | Important |
| Role: Windows Hyper-V | [CVE-2021-40461](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40461) | Windows Hyper-V Remote Code Execution Vulnerability | Critical |
| Role: Windows Hyper-V | [CVE-2021-38672](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38672) | Windows Hyper-V Remote Code Execution Vulnerability | Critical |
| System Center | [CVE-2021-41352](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41352) | SCOM Information Disclosure Vulnerability | Important |
| Visual Studio | [CVE-2020-1971](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1971) | OpenSSL: CVE-2020-1971 EDIPARTYNAME NULL pointer de-reference | Important |
| Visual Studio | [CVE-2021-3450](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-3450) | OpenSSL: CVE-2021-3450 CA certificate check bypass with X509\_V\_FLAG\_X509\_STRICT | Important |
| Visual Studio | [CVE-2021-3449](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-3449) | OpenSSL: CVE-2021-3449 NULL pointer deref in signature\_algorithms processing | Important |
| Windows AppContainer | [CVE-2021-41338](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41338) | Windows AppContainer Firewall Rules Security Feature Bypass Vulnerability | Important |
| Windows AppContainer | [CVE-2021-40476](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40476) | Windows AppContainer Elevation Of Privilege Vulnerability | Important |
| Windows AppX Deployment Service | [CVE-2021-41347](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41347) | Windows AppX Deployment Service Elevation of Privilege Vulnerability | Important |
| Windows Bind Filter Driver | [CVE-2021-40468](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40468) | Windows Bind Filter Driver Information Disclosure Vulnerability | Important |
| Windows Cloud Files Mini Filter Driver | [CVE-2021-40475](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40475) | Windows Cloud Files Mini Filter Driver Information Disclosure Vulnerability | Important |
| Windows Common Log File System Driver | [CVE-2021-40443](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40443) | Windows Common Log File System Driver Elevation of Privilege Vulnerability | Important |
| Windows Common Log File System Driver | [CVE-2021-40467](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40467) | Windows Common Log File System Driver Elevation of Privilege Vulnerability | Important |
| Windows Common Log File System Driver | [CVE-2021-40466](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40466) | Windows Common Log File System Driver Elevation of Privilege Vulnerability | Important |
| Windows Desktop Bridge | [CVE-2021-41334](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41334) | Windows Desktop Bridge Elevation of Privilege Vulnerability | Important |
| Windows DirectX | [CVE-2021-40470](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40470) | DirectX Graphics Kernel Elevation of Privilege Vulnerability | Important |
| Windows Event Tracing | [CVE-2021-40477](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40477) | Windows Event Tracing Elevation of Privilege Vulnerability | Important |
| Windows exFAT File System | [CVE-2021-38663](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38663) | Windows exFAT File System Information Disclosure Vulnerability | Important |
| Windows Fastfat Driver | [CVE-2021-41343](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41343) | Windows Fast FAT File System Driver Information Disclosure Vulnerability | Important |
| Windows Fastfat Driver | [CVE-2021-38662](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38662) | Windows Fast FAT File System Driver Information Disclosure Vulnerability | Important |
| Windows Installer | [CVE-2021-40455](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40455) | Windows Installer Spoofing Vulnerability | Important |
| Windows Kernel | [CVE-2021-41336](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41336) | Windows Kernel Information Disclosure Vulnerability | Important |
| Windows Kernel | [CVE-2021-41335](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41335) | Windows Kernel Elevation of Privilege Vulnerability | Important |
| Windows MSHTML Platform | [CVE-2021-41342](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41342) | Windows MSHTML Platform Remote Code Execution Vulnerability | Important |
| Windows Nearby Sharing | [CVE-2021-40464](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40464) | Windows Nearby Sharing Elevation of Privilege Vulnerability | Important |
| Windows Network Address Translation (NAT) | [CVE-2021-40463](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40463) | Windows NAT Denial of Service Vulnerability | Important |
| Windows Print Spooler Components | [CVE-2021-41332](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41332) | Windows Print Spooler Information Disclosure Vulnerability | Important |
| Windows Print Spooler Components | [CVE-2021-36970](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36970) | Windows Print Spooler Spoofing Vulnerability | Important |
| Windows Remote Procedure Call Runtime | [CVE-2021-40460](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40460) | Windows Remote Procedure Call Runtime Security Feature Bypass Vulnerability | Important |
| Windows Storage Spaces Controller | [CVE-2021-40489](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40489) | Storage Spaces Controller Elevation of Privilege Vulnerability | Important |
| Windows Storage Spaces Controller | [CVE-2021-41345](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41345) | Storage Spaces Controller Elevation of Privilege Vulnerability | Important |
| Windows Storage Spaces Controller | [CVE-2021-26441](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26441) | Storage Spaces Controller Elevation of Privilege Vulnerability | Important |
| Windows Storage Spaces Controller | [CVE-2021-40478](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40478) | Storage Spaces Controller Elevation of Privilege Vulnerability | Important |
| Windows Storage Spaces Controller | [CVE-2021-40488](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40488) | Storage Spaces Controller Elevation of Privilege Vulnerability | Important |
| Windows TCP/IP | [CVE-2021-36953](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36953) | Windows TCP/IP Denial of Service Vulnerability | Important |
| Windows Text Shaping | [CVE-2021-40465](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40465) | Windows Text Shaping Remote Code Execution Vulnerability | Important |
| Windows Win32K | [CVE-2021-40449](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40449) | Win32k Elevation of Privilege Vulnerability | Important |
| Windows Win32K | [CVE-2021-41357](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41357) | Win32k Elevation of Privilege Vulnerability | Important |
| Windows Win32K | [CVE-2021-40450](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40450) | Win32k Elevation of Privilege Vulnerability | Important |




#### Tags:
[[Windows]] [[Microsoft]] [[SharePoint]] [[(Chromium-based)]] [[Chromium:]] [[zero-day]] [[Win32k]] [[AppContainer]] [[Role:]] [[Visio]] [[Bleeping Computer]]
