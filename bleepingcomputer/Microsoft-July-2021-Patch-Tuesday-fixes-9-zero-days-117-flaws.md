# Microsoft July 2021 Patch Tuesday fixes 9 zero-days, 117 flaws
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-july-2021-patch-tuesday-fixes-9-zero-days-117-flaws/)
+ Date: July 13, 2021
+ Author: Lawrence Abrams


## Article:

![Patch Tuesday](https://www.bleepstatic.com/images/stock-photos/operating-systems/windows-10/patch-tuesday-large.jpg)



Today is Microsoft's July 2021 Patch Tuesday, and with it comes fixes for nine zero-day vulnerabilities and a total of 117 flaws, so Windows admins will be pulling their hair out as they scramble to get devices patched and secured.


Microsoft has fixed 117 vulnerabilities with today's update, with 13 classified as Critical, 1 Moderate, and 103 as Important.



Of the 117 vulnerabilities, 44 are remote code execution, 32 are for elevation of privilege, 14 are information disclosure, 12 are Denial of Service, 8 are security feature bypass, and seven are spoofing vulnerabilities.


For information about the non-security Windows updates, you can read about today's [Windows 10 KB5004237 & KB5004245 cumulative updates](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5004237-and-kb5004245-cumulative-updates-released/).




Nine zero-days fixed, with four actively exploited
--------------------------------------------------


July's Patch Tuesday includes nine zero-day vulnerabilities, with four actively exploited in the wild.


Microsoft classifies a zero-day vulnerability as publicly disclosed or actively exploited with no official security updates or released.


The five publicly disclosed, but not exploited, zero-day vulnerabilities are:


* CVE-2021-34492 - Windows Certificate Spoofing Vulnerability
* CVE-2021-34523 - Microsoft Exchange Server Elevation of Privilege Vulnerability
* CVE-2021-34473 - Microsoft Exchange Server Remote Code Execution Vulnerability
* CVE-2021-33779 - Windows ADFS Security Feature Bypass Vulnerability
* CVE-2021-33781 - Active Directory Security Feature Bypass Vulnerability


There was one publicly disclosed and actively exploited vulnerability known as PrintNightmare.


* CVE-2021-34527 - Windows Print Spooler Remote Code Execution Vulnerability


Finally, there are three actively exploited Windows vulnerabilities that were not publicly disclosed.


* CVE-2021-33771 - Windows Kernel Elevation of Privilege Vulnerability
* CVE-2021-34448 - Scripting Engine Memory Corruption Vulnerability
* CVE-2021-31979 - Windows Kernel Elevation of Privilege Vulnerability


The print nightmare
-------------------


Last month, a proof-of-concept exploit was released by accident for the zero-day [PrintNightmare vulnerability](https://www.bleepingcomputer.com/news/security/public-windows-printnightmare-0-day-exploit-allows-domain-takeover/) that allows remote code execution and local privilege escalation.


Due to the severity of the attacks, Microsoft [released an out-of-band KB5004945 security update](https://www.bleepingcomputer.com/news/security/microsoft-pushes-emergency-update-for-windows-printnightmare-zero-day/) that was supposed to fix the [PrintNightmare vulnerability](https://www.bleepingcomputer.com/news/security/public-windows-printnightmare-0-day-exploit-allows-domain-takeover/) tracked as [CVE-2021-34527](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527).


Microsoft's OOB patch only resolves the vulnerability if the Point and Print policy is disabled. The patch can be bypassed for those devices that still have this registry setting enabled to achieve remote code execution and local privilege escalation.


However, Microsoft states that the patches are working as intended and that Windows admins should install the patches immediately as the vulnerabilities are being actively exploited.


"Our investigation has shown that the OOB security update is working as designed and is effective against the known printer spooling exploits and other public reports collectively being referred to as PrintNightmare," the Microsoft Security Response Center explains.


"All reports we have investigated have relied on the changing of default registry setting related to Point and Print to an insecure configuration."


Security research and Mimikatz creator feels that the patch still needs improvement to protect against the bypasses he and others have found




> 
> Clarified Guidance for CVE-2021-34527 [#printnightmare](https://twitter.com/hashtag/printnightmare?src=hash&ref_src=twsrc%5Etfw)  
>   
> 
> So I presume all is OK, and:  
> 
> - you will not change UNC path detection  
> 
> - RestrictDriverInstallationToAdministrators & driver no explaination?  
>   
> 
> It's not, and you know it  
>   
> 
> > <https://t.co/ONmlFjuhn0> [pic.twitter.com/aqMDS8gdJa](https://t.co/aqMDS8gdJa)
> 
> 
> —  Benjamin Delpy (@gentilkiwi) [July 9, 2021](https://twitter.com/gentilkiwi/status/1413420341658066944?ref_src=twsrc%5Etfw)


Recent updates from other companies
-----------------------------------


Other vendors who released updates in July include:


* **Adobe**[released security updates](https://helpx.adobe.com/security/security-bulletin.html) for five products.
* **Android's** July security updates were [released](https://source.android.com/security/bulletin/2021-07-01) last week.
* **Cisco** [released security updates](https://tools.cisco.com/security/center/publicationListing.x) for numerous products this month.
* **SAP** [released](https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=580617506) its July 2021 security updates.
* VMware released [security updates](https://www.vmware.com/security/advisories.html) for ESXi and ThinApp.


The July 2021 Patch Tuesday Security Updates
--------------------------------------------


Below is the full list of resolved vulnerabilities and released advisories in the July 2021 Patch Tuesday updates. To access the full description of each vulnerability and the systems that it affects, you can view the [full report here](https://www.bleepingcomputer.com/microsoft-patch-tuesday-reports/July-2021.html).





| Tag | CVE ID | CVE Title | Severity |
| --- | --- | --- | --- |
| Active Directory Federation Services | [CVE-2021-33779](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33779) | Windows ADFS Security Feature Bypass Vulnerability | Important |
| Common Internet File System | [CVE-2021-34476](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34476) | Bowser.sys Denial of Service Vulnerability | Important |
| Dynamics Business Central Control | [CVE-2021-34474](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34474) | Dynamics Business Central Remote Code Execution Vulnerability | Critical |
| Microsoft Bing | [CVE-2021-33753](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33753) | Microsoft Bing Search Spoofing Vulnerability | Important |
| Microsoft Exchange Server | [CVE-2021-31206](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-31206) | Microsoft Exchange Server Remote Code Execution Vulnerability | Important |
| Microsoft Exchange Server | [CVE-2021-34473](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34473) | Microsoft Exchange Server Remote Code Execution Vulnerability | Critical |
| Microsoft Exchange Server | [CVE-2021-33766](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33766) | Microsoft Exchange Information Disclosure Vulnerability | Important |
| Microsoft Exchange Server | [CVE-2021-34523](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34523) | Microsoft Exchange Server Elevation of Privilege Vulnerability | Important |
| Microsoft Exchange Server | [CVE-2021-31196](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-31196) | Microsoft Exchange Server Remote Code Execution Vulnerability | Important |
| Microsoft Exchange Server | [CVE-2021-33768](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33768) | Microsoft Exchange Server Elevation of Privilege Vulnerability | Important |
| Microsoft Exchange Server | [CVE-2021-34470](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34470) | Microsoft Exchange Server Elevation of Privilege Vulnerability | Important |
| Microsoft Graphics Component | [CVE-2021-34440](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34440) | GDI+ Information Disclosure Vulnerability | Important |
| Microsoft Graphics Component | [CVE-2021-34489](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34489) | DirectWrite Remote Code Execution Vulnerability | Important |
| Microsoft Graphics Component | [CVE-2021-34496](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34496) | Windows GDI Information Disclosure Vulnerability | Important |
| Microsoft Graphics Component | [CVE-2021-34498](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34498) | Windows GDI Elevation of Privilege Vulnerability | Important |
| Microsoft Graphics Component | [CVE-2021-34438](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34438) | Windows Font Driver Host Remote Code Execution Vulnerability | Important |
| Microsoft Office | [CVE-2021-34469](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34469) | Microsoft Office Security Feature Bypass Vulnerability | Important |
| Microsoft Office | [CVE-2021-34451](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34451) | Microsoft Office Online Server Spoofing Vulnerability | Important |
| Microsoft Office | [CVE-2021-34452](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34452) | Microsoft Word Remote Code Execution Vulnerability | Important |
| Microsoft Office Excel | [CVE-2021-34501](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34501) | Microsoft Excel Remote Code Execution Vulnerability | Important |
| Microsoft Office Excel | [CVE-2021-34518](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34518) | Microsoft Excel Remote Code Execution Vulnerability | Important |
| Microsoft Office SharePoint | [CVE-2021-34468](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34468) | Microsoft SharePoint Server Remote Code Execution Vulnerability | Important |
| Microsoft Office SharePoint | [CVE-2021-34519](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34519) | Microsoft SharePoint Server Information Disclosure Vulnerability | Moderate |
| Microsoft Office SharePoint | [CVE-2021-34520](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34520) | Microsoft SharePoint Server Remote Code Execution Vulnerability | Important |
| Microsoft Office SharePoint | [CVE-2021-34517](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34517) | Microsoft SharePoint Server Spoofing Vulnerability | Important |
| Microsoft Office SharePoint | [CVE-2021-34467](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34467) | Microsoft SharePoint Server Remote Code Execution Vulnerability | Important |
| Microsoft Scripting Engine | [CVE-2021-34448](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34448) | Scripting Engine Memory Corruption Vulnerability | Critical |
| Microsoft Windows Codecs Library | [CVE-2021-33778](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33778) | HEVC Video Extensions Remote Code Execution Vulnerability | Important |
| Microsoft Windows Codecs Library | [CVE-2021-31947](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-31947) | HEVC Video Extensions Remote Code Execution Vulnerability | Important |
| Microsoft Windows Codecs Library | [CVE-2021-33740](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33740) | Windows Media Remote Code Execution Vulnerability | Critical |
| Microsoft Windows Codecs Library | [CVE-2021-33760](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33760) | Media Foundation Information Disclosure Vulnerability | Important |
| Microsoft Windows Codecs Library | [CVE-2021-33775](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33775) | HEVC Video Extensions Remote Code Execution Vulnerability | Important |
| Microsoft Windows Codecs Library | [CVE-2021-33776](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33776) | HEVC Video Extensions Remote Code Execution Vulnerability | Important |
| Microsoft Windows Codecs Library | [CVE-2021-33777](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33777) | HEVC Video Extensions Remote Code Execution Vulnerability | Important |
| Microsoft Windows Codecs Library | [CVE-2021-34521](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34521) | Raw Image Extension Remote Code Execution Vulnerability | Important |
| Microsoft Windows DNS | [CVE-2021-34499](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34499) | Windows DNS Server Denial of Service Vulnerability | Important |
| Microsoft Windows DNS | [CVE-2021-33746](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33746) | Windows DNS Server Remote Code Execution Vulnerability | Important |
| Microsoft Windows DNS | [CVE-2021-33754](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33754) | Windows DNS Server Remote Code Execution Vulnerability | Important |
| Microsoft Windows Media Foundation | [CVE-2021-34441](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34441) | Microsoft Windows Media Foundation Remote Code Execution Vulnerability | Important |
| Microsoft Windows Media Foundation | [CVE-2021-34439](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34439) | Microsoft Windows Media Foundation Remote Code Execution Vulnerability | Critical |
| Microsoft Windows Media Foundation | [CVE-2021-34503](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34503) | Microsoft Windows Media Foundation Remote Code Execution Vulnerability | Critical |
| OpenEnclave | [CVE-2021-33767](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33767) | Open Enclave SDK Elevation of Privilege Vulnerability | Important |
| Power BI | [CVE-2021-31984](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-31984) | Power BI Remote Code Execution Vulnerability | Important |
| Role: DNS Server | [CVE-2021-33749](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33749) | Windows DNS Snap-in Remote Code Execution Vulnerability | Important |
| Role: DNS Server | [CVE-2021-33745](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33745) | Windows DNS Server Denial of Service Vulnerability | Important |
| Role: DNS Server | [CVE-2021-34442](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34442) | Windows DNS Server Denial of Service Vulnerability | Important |
| Role: DNS Server | [CVE-2021-34444](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34444) | Windows DNS Server Denial of Service Vulnerability | Important |
| Role: DNS Server | [CVE-2021-34525](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34525) | Windows DNS Server Remote Code Execution Vulnerability | Important |
| Role: DNS Server | [CVE-2021-33780](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33780) | Windows DNS Server Remote Code Execution Vulnerability | Important |
| Role: DNS Server | [CVE-2021-34494](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34494) | Windows DNS Server Remote Code Execution Vulnerability | Critical |
| Role: DNS Server | [CVE-2021-33750](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33750) | Windows DNS Snap-in Remote Code Execution Vulnerability | Important |
| Role: DNS Server | [CVE-2021-33752](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33752) | Windows DNS Snap-in Remote Code Execution Vulnerability | Important |
| Role: DNS Server | [CVE-2021-33756](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33756) | Windows DNS Snap-in Remote Code Execution Vulnerability | Important |
| Role: Hyper-V | [CVE-2021-33758](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33758) | Windows Hyper-V Denial of Service Vulnerability | Important |
| Role: Hyper-V | [CVE-2021-33755](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33755) | Windows Hyper-V Denial of Service Vulnerability | Important |
| Role: Hyper-V | [CVE-2021-34450](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34450) | Windows Hyper-V Remote Code Execution Vulnerability | Critical |
| Visual Studio Code | [CVE-2021-34529](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34529) | Visual Studio Code Remote Code Execution Vulnerability | Important |
| Visual Studio Code | [CVE-2021-34528](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34528) | Visual Studio Code Remote Code Execution Vulnerability | Important |
| Visual Studio Code | [CVE-2021-34479](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34479) | Microsoft Visual Studio Spoofing Vulnerability | Important |
| Visual Studio Code - .NET Runtime | [CVE-2021-34477](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34477) | Visual Studio Code .NET Runtime Elevation of Privilege Vulnerability | Important |
| Windows Active Directory | [CVE-2021-33781](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33781) | Active Directory Security Feature Bypass Vulnerability | Important |
| Windows Address Book | [CVE-2021-34504](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34504) | Windows Address Book Remote Code Execution Vulnerability | Important |
| Windows AF\_UNIX Socket Provider | [CVE-2021-33785](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33785) | Windows AF\_UNIX Socket Provider Denial of Service Vulnerability | Important |
| Windows AppContainer | [CVE-2021-34459](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34459) | Windows AppContainer Elevation Of Privilege Vulnerability | Important |
| Windows AppX Deployment Extensions | [CVE-2021-34462](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34462) | Windows AppX Deployment Extensions Elevation of Privilege Vulnerability | Important |
| Windows Authenticode | [CVE-2021-33782](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33782) | Windows Authenticode Spoofing Vulnerability | Important |
| Windows Cloud Files Mini Filter Driver | [CVE-2021-33784](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33784) | Windows Cloud Files Mini Filter Driver Elevation of Privilege Vulnerability | Important |
| Windows Console Driver | [CVE-2021-34488](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34488) | Windows Console Driver Elevation of Privilege Vulnerability | Important |
| Windows Defender | [CVE-2021-34522](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34522) | Microsoft Defender Remote Code Execution Vulnerability | Critical |
| Windows Defender | [CVE-2021-34464](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34464) | Microsoft Defender Remote Code Execution Vulnerability | Critical |
| Windows Desktop Bridge | [CVE-2021-33759](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33759) | Windows Desktop Bridge Elevation of Privilege Vulnerability | Important |
| Windows Event Tracing | [CVE-2021-33774](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33774) | Windows Event Tracing Elevation of Privilege Vulnerability | Important |
| Windows File History Service | [CVE-2021-34455](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34455) | Windows File History Service Elevation of Privilege Vulnerability | Important |
| Windows Hello | [CVE-2021-34466](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34466) | Windows Hello Security Feature Bypass Vulnerability | Important |
| Windows HTML Platform | [CVE-2021-34446](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34446) | Windows HTML Platforms Security Feature Bypass Vulnerability | Important |
| Windows Installer | [CVE-2021-33765](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33765) | Windows Installer Spoofing Vulnerability | Important |
| Windows Installer | [CVE-2021-34511](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34511) | Windows Installer Elevation of Privilege Vulnerability | Important |
| Windows Installer | [CVE-2021-31961](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-31961) | Windows InstallService Elevation of Privilege Vulnerability | Important |
| Windows Kernel | [CVE-2021-34461](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34461) | Windows Container Isolation FS Filter Driver Elevation of Privilege Vulnerability | Important |
| Windows Kernel | [CVE-2021-34508](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34508) | Windows Kernel Remote Code Execution Vulnerability | Important |
| Windows Kernel | [CVE-2021-34458](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34458) | Windows Kernel Remote Code Execution Vulnerability | Critical |
| Windows Kernel | [CVE-2021-33771](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33771) | Windows Kernel Elevation of Privilege Vulnerability | Important |
| Windows Kernel | [CVE-2021-31979](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-31979) | Windows Kernel Elevation of Privilege Vulnerability | Important |
| Windows Kernel | [CVE-2021-34514](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34514) | Windows Kernel Elevation of Privilege Vulnerability | Important |
| Windows Kernel | [CVE-2021-34500](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34500) | Windows Kernel Memory Information Disclosure Vulnerability | Important |
| Windows Key Distribution Center | [CVE-2021-33764](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33764) | Windows Key Distribution Center Information Disclosure Vulnerability | Important |
| Windows Local Security Authority Subsystem Service | [CVE-2021-33788](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33788) | Windows LSA Denial of Service Vulnerability | Important |
| Windows Local Security Authority Subsystem Service | [CVE-2021-33786](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33786) | Windows LSA Security Feature Bypass Vulnerability | Important |
| Windows MSHTML Platform | [CVE-2021-34497](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34497) | Windows MSHTML Platform Remote Code Execution Vulnerability | Critical |
| Windows MSHTML Platform | [CVE-2021-34447](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34447) | Windows MSHTML Platform Remote Code Execution Vulnerability | Important |
| Windows Partition Management Driver | [CVE-2021-34493](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34493) | Windows Partition Management Driver Elevation of Privilege Vulnerability | Important |
| Windows PFX Encryption | [CVE-2021-34492](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34492) | Windows Certificate Spoofing Vulnerability | Important |
| Windows Print Spooler Components | [CVE-2021-34527](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34527) | Windows Print Spooler Remote Code Execution Vulnerability | Critical |
| Windows Projected File System | [CVE-2021-33743](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33743) | Windows Projected File System Elevation of Privilege Vulnerability | Important |
| Windows Remote Access Connection Manager | [CVE-2021-34457](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34457) | Windows Remote Access Connection Manager Information Disclosure Vulnerability | Important |
| Windows Remote Access Connection Manager | [CVE-2021-33761](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33761) | Windows Remote Access Connection Manager Elevation of Privilege Vulnerability | Important |
| Windows Remote Access Connection Manager | [CVE-2021-33773](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33773) | Windows Remote Access Connection Manager Elevation of Privilege Vulnerability | Important |
| Windows Remote Access Connection Manager | [CVE-2021-33763](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33763) | Windows Remote Access Connection Manager Information Disclosure Vulnerability | Important |
| Windows Remote Access Connection Manager | [CVE-2021-34445](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34445) | Windows Remote Access Connection Manager Elevation of Privilege Vulnerability | Important |
| Windows Remote Access Connection Manager | [CVE-2021-34456](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34456) | Windows Remote Access Connection Manager Elevation of Privilege Vulnerability | Important |
| Windows Remote Assistance | [CVE-2021-34507](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34507) | Windows Remote Assistance Information Disclosure Vulnerability | Important |
| Windows Secure Kernel Mode | [CVE-2021-33744](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33744) | Windows Secure Kernel Mode Security Feature Bypass Vulnerability | Important |
| Windows Security Account Manager | [CVE-2021-33757](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33757) | Windows Security Account Manager Remote Protocol Security Feature Bypass Vulnerability | Important |
| Windows Shell | [CVE-2021-34454](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34454) | Windows Remote Access Connection Manager Information Disclosure Vulnerability | Important |
| Windows SMB | [CVE-2021-33783](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33783) | Windows SMB Information Disclosure Vulnerability | Important |
| Windows Storage Spaces Controller | [CVE-2021-33751](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33751) | Storage Spaces Controller Elevation of Privilege Vulnerability | Important |
| Windows Storage Spaces Controller | [CVE-2021-34460](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34460) | Storage Spaces Controller Elevation of Privilege Vulnerability | Important |
| Windows Storage Spaces Controller | [CVE-2021-34509](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34509) | Storage Spaces Controller Information Disclosure Vulnerability | Important |
| Windows Storage Spaces Controller | [CVE-2021-34510](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34510) | Storage Spaces Controller Elevation of Privilege Vulnerability | Important |
| Windows Storage Spaces Controller | [CVE-2021-34512](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34512) | Storage Spaces Controller Elevation of Privilege Vulnerability | Important |
| Windows Storage Spaces Controller | [CVE-2021-34513](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34513) | Storage Spaces Controller Elevation of Privilege Vulnerability | Important |
| Windows TCP/IP | [CVE-2021-31183](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-31183) | Windows TCP/IP Driver Denial of Service Vulnerability | Important |
| Windows TCP/IP | [CVE-2021-33772](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-33772) | Windows TCP/IP Driver Denial of Service Vulnerability | Important |
| Windows TCP/IP | [CVE-2021-34490](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34490) | Windows TCP/IP Driver Denial of Service Vulnerability | Important |
| Windows Win32K | [CVE-2021-34449](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34449) | Win32k Elevation of Privilege Vulnerability | Important |
| Windows Win32K | [CVE-2021-34516](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34516) | Win32k Elevation of Privilege Vulnerability | Important |
| Windows Win32K | [CVE-2021-34491](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-34491) | Win32k Information Disclosure Vulnerability | Important |




#### Tags:
[[Windows]] [[Microsoft]] [[DNS]] [[-]] [[SharePoint]] [[Hyper-V]] [[TCP]] [[IP]] [[zero-day]] [[HEVC]] [[Bleeping Computer]]
