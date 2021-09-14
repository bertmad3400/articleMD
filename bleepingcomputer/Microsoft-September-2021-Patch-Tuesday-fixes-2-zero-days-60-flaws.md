# Microsoft September 2021 Patch Tuesday fixes 2 zero-days, 60 flaws
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-september-2021-patch-tuesday-fixes-2-zero-days-60-flaws/)
+ Date: September 14, 2021
+ Author: Lawrence Abrams


## Article:

![Patch Tuesday](https://www.bleepstatic.com/images/stock-photos/operating-systems/windows-10/patch-tuesday-large.jpg)



Today is Microsoft's September 2021 Patch Tuesday, and with it comes fixes for two zero-day vulnerabilities and a total of 60 flaws.


Microsoft has fixed 60 vulnerabilities (86 including Microsoft Edge) with today's update, with three classified as Critical, one as Moderate, and 56 as Important.


Of the total 86 vulnerabilities (including Microsoft Edge):


* 27 Elevation of Privilege Vulnerabilities
* 2 Security Feature Bypass Vulnerabilities
* 16 Remote Code Execution Vulnerabilities
* 11 Information Disclosure Vulnerabilities
* 1 Denial of Service Vulnerabilities
* 8 Spoofing Vulnerabilities


For information about the non-security Windows updates, you can read about today's [Windows 10 KB5005565 & KB5005566 cumulative updates](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5005565-and-kb5005566-cumulative-updates-released/).




Microsoft fixes Windows MSHTML zero-day
---------------------------------------


Microsoft has released a security update for the Windows MSHTML remote code execution vulnerability tracked as CVE-2021-40444.


Last Tuesday, Microsoft disclosed a new zero-day [Windows MSHTML remote code execution vulnerability](https://www.bleepingcomputer.com/news/security/microsoft-shares-temp-fix-for-ongoing-office-365-zero-day-attacks/) that threat actors actively used in phishing attacks.


These attacks distributed malicious Word documents that exploited the CVE-2021-40444 to download and execute a malicious DLL file that installed a Cobalt Strike beacon on the victim's computer.


This beacon allows a threat actor to gain remote access to the device to steal files and spread laterally throughout the network.


Soon after Microsoft disclosed the vulnerability, [threat actors and security researchers began sharing guides](https://www.bleepingcomputer.com/news/microsoft/windows-mshtml-zero-day-exploits-shared-on-hacking-forums/) on exploiting the vulnerability, which allowed anyone to start using it in attacks, as demonstrated below.



With the September 2021 Patch Tuesday updates, Microsoft has released a security update for this vulnerability.


As researchers discovered numerous ways to exploit the bug, including a [bypass to mitigations](https://www.bleepingcomputer.com/news/microsoft/windows-mshtml-zero-day-defenses-bypassed-as-new-info-emerges/), it is not clear if the security update fixes all of the techniques.


Two zero-days fixed, with one actively exploited
------------------------------------------------


September's Patch Tuesday includes fixes for two zero-day vulnerabilities, with the MSHTML bug actively exploited in the wild.


Microsoft classifies a vulnerability as a zero-day if publicly disclosed or actively exploited with no official security updates released.


The publicly disclosed, but not actively exploited, zero-day vulnerability is:


* [CVE-2021-36968](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-36968) - Windows DNS Elevation of Privilege Vulnerability


The only actively exploited vulnerability is the Windows MSHTML remote code execution vulnerability, as previously discussed:


* [CVE-2021-40444](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-40444) - Microsoft MSHTML Remote Code Execution Vulnerability


Recent updates from other companies
-----------------------------------


Other vendors who released updates in July include:


* **Adobe**[released security updates](https://helpx.adobe.com/security/security-bulletin.html) for two products.
* **Android's** September security updates were [released](https://source.android.com/security/bulletin/2021-09-01) last week.
* **Apple** released [security updates](https://www.bleepingcomputer.com/news/apple/apple-fixes-ios-zero-day-used-to-deploy-nso-iphone-spyware/) for iOS and macOS yesterday that fix two zero-day vulnerabilities exploited in the wild. One of the vulnerabilities was [used to install the NSO Pegasus spyware](https://www.bleepingcomputer.com/news/apple/new-zero-click-iphone-exploit-used-to-deploy-nso-spyware/) on activists's devices.
* **Cisco** [released security updates](https://tools.cisco.com/security/center/publicationListing.x) for numerous products this month.
* **SAP** [released](https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=585106405) its September 2021 security updates.


The September 2021 Patch Tuesday Security Updates
-------------------------------------------------


Below is the complete list of resolved vulnerabilities and released advisories in the September 2021 Patch Tuesday updates. To access the full description of each vulnerability and the systems that it affects, you can view the [full report here](https://www.bleepingcomputer.com/microsoft-patch-tuesday-reports/September-2021.html).





| Tag | CVE ID | CVE Title | Severity |
| --- | --- | --- | --- |
| Azure Open Management Infrastructure | [CVE-2021-38648](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38648) | Open Management Infrastructure Elevation of Privilege Vulnerability | Important |
| Azure Open Management Infrastructure | [CVE-2021-38645](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38645) | Open Management Infrastructure Elevation of Privilege Vulnerability | Important |
| Azure Open Management Infrastructure | [CVE-2021-38647](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38647) | Open Management Infrastructure Remote Code Execution Vulnerability | Critical |
| Azure Open Management Infrastructure | [CVE-2021-38649](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38649) | Open Management Infrastructure Elevation of Privilege Vulnerability | Important |
| Azure Sphere | [CVE-2021-36956](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36956) | Azure Sphere Information Disclosure Vulnerability | Important |
| Dynamics Business Central Control | [CVE-2021-40440](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40440) | Microsoft Dynamics Business Central Cross-site Scripting Vulnerability | Important |
| Microsoft Accessibility Insights for Android | [CVE-2021-40448](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40448) | Microsoft Accessibility Insights for Android Information Disclosure Vulnerability | Important |
| Microsoft Edge (Chromium-based) | [CVE-2021-30606](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30606) | Chromium: CVE-2021-30606 Use after free in Blink | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30609](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30609) | Chromium: CVE-2021-30609 Use after free in Sign-In | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30608](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30608) | Chromium: CVE-2021-30608 Use after free in Web Share | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30607](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30607) | Chromium: CVE-2021-30607 Use after free in Permissions | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-38641](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38641) | Microsoft Edge for Android Spoofing Vulnerability | Important |
| Microsoft Edge (Chromium-based) | [CVE-2021-38642](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38642) | Microsoft Edge for iOS Spoofing Vulnerability | Important |
| Microsoft Edge (Chromium-based) | [CVE-2021-38669](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38669) | Microsoft Edge (Chromium-based) Tampering Vulnerability | Important |
| Microsoft Edge (Chromium-based) | [CVE-2021-36930](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36930) | Microsoft Edge (Chromium-based) Elevation of Privilege Vulnerability | Important |
| Microsoft Edge (Chromium-based) | [CVE-2021-30632](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30632) | Chromium: CVE-2021-30632 Out of bounds write in V8 | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30610](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30610) | Chromium: CVE-2021-30610 Use after free in Extensions API | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30620](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30620) | Chromium: CVE-2021-30620 Insufficient policy enforcement in Blink | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30619](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30619) | Chromium: CVE-2021-30619 UI Spoofing in Autofill | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30618](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30618) | Chromium: CVE-2021-30618 Inappropriate implementation in DevTools | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30621](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30621) | Chromium: CVE-2021-30621 UI Spoofing in Autofill | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30624](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30624) | Chromium: CVE-2021-30624 Use after free in Autofill | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30623](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30623) | Chromium: CVE-2021-30623 Use after free in Bookmarks | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30622](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30622) | Chromium: CVE-2021-30622 Use after free in WebApp Installs | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30613](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30613) | Chromium: CVE-2021-30613 Use after free in Base internals | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30612](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30612) | Chromium: CVE-2021-30612 Use after free in WebRTC | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30611](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30611) | Chromium: CVE-2021-30611 Use after free in WebRTC | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30614](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30614) | Chromium: CVE-2021-30614 Heap buffer overflow in TabStrip | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30617](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30617) | Chromium: CVE-2021-30617 Policy bypass in Blink | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30616](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30616) | Chromium: CVE-2021-30616 Use after free in Media | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-30615](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-30615) | Chromium: CVE-2021-30615 Cross-origin data leak in Navigation | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2021-26436](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26436) | Microsoft Edge (Chromium-based) Elevation of Privilege Vulnerability | Important |
| Microsoft Edge for Android | [CVE-2021-26439](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26439) | Microsoft Edge for Android Information Disclosure Vulnerability | Moderate |
| Microsoft MPEG-2 Video Extension | [CVE-2021-38644](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38644) | Microsoft MPEG-2 Video Extension Remote Code Execution Vulnerability | Important |
| Microsoft Office | [CVE-2021-38657](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38657) | Microsoft Office Graphics Component Information Disclosure Vulnerability | Important |
| Microsoft Office | [CVE-2021-38658](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38658) | Microsoft Office Graphics Remote Code Execution Vulnerability | Important |
| Microsoft Office | [CVE-2021-38650](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38650) | Microsoft Office Spoofing Vulnerability | Important |
| Microsoft Office | [CVE-2021-38659](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38659) | Microsoft Office Remote Code Execution Vulnerability | Important |
| Microsoft Office Access | [CVE-2021-38646](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38646) | Microsoft Office Access Connectivity Engine Remote Code Execution Vulnerability | Important |
| Microsoft Office Excel | [CVE-2021-38655](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38655) | Microsoft Excel Remote Code Execution Vulnerability | Important |
| Microsoft Office Excel | [CVE-2021-38660](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38660) | Microsoft Office Graphics Remote Code Execution Vulnerability | Important |
| Microsoft Office SharePoint | [CVE-2021-38651](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38651) | Microsoft SharePoint Server Spoofing Vulnerability | Important |
| Microsoft Office SharePoint | [CVE-2021-38652](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38652) | Microsoft SharePoint Server Spoofing Vulnerability | Important |
| Microsoft Office Visio | [CVE-2021-38654](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38654) | Microsoft Office Visio Remote Code Execution Vulnerability | Important |
| Microsoft Office Visio | [CVE-2021-38653](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38653) | Microsoft Office Visio Remote Code Execution Vulnerability | Important |
| Microsoft Office Word | [CVE-2021-38656](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38656) | Microsoft Word Remote Code Execution Vulnerability | Important |
| Microsoft Windows Codecs Library | [CVE-2021-38661](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38661) | HEVC Video Extensions Remote Code Execution Vulnerability | Important |
| Microsoft Windows DNS | [CVE-2021-36968](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36968) | Windows DNS Elevation of Privilege Vulnerability | Important |
| Visual Studio | [CVE-2021-36952](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36952) | Visual Studio Remote Code Execution Vulnerability | Important |
| Visual Studio | [CVE-2021-26434](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26434) | Visual Studio Elevation of Privilege Vulnerability | Important |
| Visual Studio | [CVE-2021-26437](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26437) | Visual Studio Code Spoofing Vulnerability | Important |
| Windows Ancillary Function Driver for WinSock | [CVE-2021-38628](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38628) | Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability | Important |
| Windows Ancillary Function Driver for WinSock | [CVE-2021-38638](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38638) | Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability | Important |
| Windows Authenticode | [CVE-2021-36959](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36959) | Windows Authenticode Spoofing Vulnerability | Important |
| Windows Bind Filter Driver | [CVE-2021-36954](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36954) | Windows Bind Filter Driver Elevation of Privilege Vulnerability | Important |
| Windows BitLocker | [CVE-2021-38632](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38632) | BitLocker Security Feature Bypass Vulnerability | Important |
| Windows Common Log File System Driver | [CVE-2021-38633](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38633) | Windows Common Log File System Driver Elevation of Privilege Vulnerability | Important |
| Windows Common Log File System Driver | [CVE-2021-36963](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36963) | Windows Common Log File System Driver Elevation of Privilege Vulnerability | Important |
| Windows Common Log File System Driver | [CVE-2021-36955](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36955) | Windows Common Log File System Driver Elevation of Privilege Vulnerability | Important |
| Windows Event Tracing | [CVE-2021-36964](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36964) | Windows Event Tracing Elevation of Privilege Vulnerability | Important |
| Windows Event Tracing | [CVE-2021-38630](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38630) | Windows Event Tracing Elevation of Privilege Vulnerability | Important |
| Windows Installer | [CVE-2021-36962](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36962) | Windows Installer Information Disclosure Vulnerability | Important |
| Windows Installer | [CVE-2021-36961](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36961) | Windows Installer Denial of Service Vulnerability | Important |
| Windows Kernel | [CVE-2021-38626](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38626) | Windows Kernel Elevation of Privilege Vulnerability | Important |
| Windows Kernel | [CVE-2021-38625](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38625) | Windows Kernel Elevation of Privilege Vulnerability | Important |
| Windows Key Storage Provider | [CVE-2021-38624](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38624) | Windows Key Storage Provider Security Feature Bypass Vulnerability | Important |
| Windows MSHTML Platform | [CVE-2021-40444](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40444) | Microsoft MSHTML Remote Code Execution Vulnerability | Important |
| Windows Print Spooler Components | [CVE-2021-38667](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38667) | Windows Print Spooler Elevation of Privilege Vulnerability | Important |
| Windows Print Spooler Components | [CVE-2021-38671](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38671) | Windows Print Spooler Elevation of Privilege Vulnerability | Important |
| Windows Print Spooler Components | [CVE-2021-40447](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40447) | Windows Print Spooler Elevation of Privilege Vulnerability | Important |
| Windows Redirected Drive Buffering | [CVE-2021-36969](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36969) | Windows Redirected Drive Buffering SubSystem Driver Information Disclosure Vulnerability | Important |
| Windows Redirected Drive Buffering | [CVE-2021-38635](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38635) | Windows Redirected Drive Buffering SubSystem Driver Information Disclosure Vulnerability | Important |
| Windows Redirected Drive Buffering | [CVE-2021-36973](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36973) | Windows Redirected Drive Buffering System Elevation of Privilege Vulnerability | Important |
| Windows Redirected Drive Buffering | [CVE-2021-38636](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38636) | Windows Redirected Drive Buffering SubSystem Driver Information Disclosure Vulnerability | Important |
| Windows Scripting | [CVE-2021-26435](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26435) | Windows Scripting Engine Memory Corruption Vulnerability | Critical |
| Windows SMB | [CVE-2021-36960](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36960) | Windows SMB Information Disclosure Vulnerability | Important |
| Windows SMB | [CVE-2021-36972](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36972) | Windows SMB Information Disclosure Vulnerability | Important |
| Windows SMB | [CVE-2021-36974](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36974) | Windows SMB Elevation of Privilege Vulnerability | Important |
| Windows Storage | [CVE-2021-38637](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38637) | Windows Storage Information Disclosure Vulnerability | Important |
| Windows Subsystem for Linux | [CVE-2021-36966](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36966) | Windows Subsystem for Linux Elevation of Privilege Vulnerability | Important |
| Windows TDX.sys | [CVE-2021-38629](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38629) | Windows Ancillary Function Driver for WinSock Information Disclosure Vulnerability | Important |
| Windows Update | [CVE-2021-38634](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38634) | Microsoft Windows Update Client Elevation of Privilege Vulnerability | Important |
| Windows Win32K | [CVE-2021-38639](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38639) | Win32k Elevation of Privilege Vulnerability | Important |
| Windows Win32K | [CVE-2021-36975](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36975) | Win32k Elevation of Privilege Vulnerability | Important |
| Windows WLAN Auto Config Service | [CVE-2021-36965](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36965) | Windows WLAN AutoConfig Service Remote Code Execution Vulnerability | Critical |
| Windows WLAN Service | [CVE-2021-36967](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36967) | Windows WLAN AutoConfig Service Elevation of Privilege Vulnerability | Important |




#### Tags:
[[Microsoft]] [[Windows]] [[(Chromium-based)]] [[Chromium:]] [[MSHTML]] [[zero-day]] [[Android]] [[SMB]] [[WinSock]] [[SharePoint]] [[Bleeping Computer]]
