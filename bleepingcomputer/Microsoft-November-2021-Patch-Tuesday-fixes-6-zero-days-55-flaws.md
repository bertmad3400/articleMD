# Microsoft November 2021 Patch Tuesday fixes 6 zero-days, 55 flaws
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2021-patch-tuesday-fixes-6-zero-days-55-flaws/)
+ Date: November 9, 2021
+ Author: Lawrence Abrams


## Article:
![Patch Tuesday](https://www.bleepstatic.com/images/stock-photos/operating-systems/windows-10/patch-tuesday-large.jpg)


Today is Microsoft's November 2021 Patch Tuesday, and with it comes fixes for six zero-day vulnerabilities and a total of 55 flaws. The actively exploited vulnerabilities are for Microsoft Exchange and Excel, with the Exchange zero-day used as part of the Tianfu hacking contest.


Microsoft has fixed 55 vulnerabilities with today's update, with six classified as Critical and 49 as Important. The number of each type of vulnerability is listed below:


* 20 Elevation of Privilege vulnerabilities
* 2 Security Feature Bypass vulnerabilities
* 15 Remote Code Execution vulnerabilities
* 10 Information Disclosure vulnerabilities
* 3 Denial of Service vulnerabilities
* 4 Spoofing vulnerabilities


For information about the non-security Windows updates, you can read about today's [Windows 10 KB5007186 & KB5007189 cumulative updates](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5007186-and-kb5007189-updates-released/) and the [Windows 11 KB5007215 cumulative update](https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5007215-update-released-with-application-fixes/).


Six zero-days fixed, with two actively exploited
------------------------------------------------


November's Patch Tuesday includes fixes for six zero-day vulnerabilities, two actively exploited against Microsoft Exchange and Microsoft Excel.


Microsoft classifies a vulnerability as a zero-day if it is publicly disclosed or actively exploited with no official fix available.


The actively exploited vulnerabilities fixed this month are:


* [CVE-2021-42292](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-42292) - Microsoft Excel Security Feature Bypass Vulnerability
* [CVE-2021-42321](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-42321) - Microsoft Exchange Server Remote Code Execution Vulnerability


The Microsoft Exchange [CVE-2021-42321](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-42321) vulnerability is an authenticated remote code execution bug used as part of the Tianfu Cup hacking contest last month.


However, the Microsoft Excel CVE-2021-42292 was discovered by the Microsoft Threat Intelligence Center and has been actively used in malicious attacks.


The security updates for Microsoft Office for Mac have not been released as of yet.


Microsoft also fixed four other publicly disclosed vulnerabilities that are not known to be exploited in attacks.


* [CVE-2021-38631](http://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-38631) - Windows Remote Desktop Protocol (RDP) Information Disclosure Vulnerability
* [CVE-2021-41371](http://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-41371) - Windows Remote Desktop Protocol (RDP) Information Disclosure Vulnerability
* [CVE-2021-43208](http://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-43208) - 3D Viewer Remote Code Execution Vulnerability
* [CVE-2021-43209](http://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-43209) - 3D Viewer Remote Code Execution Vulnerability


Recent updates from other companies
-----------------------------------


Other vendors who released updates in November include:


* **Adobe's** November [security updates](https://helpx.adobe.com/security/security-bulletin.html) were released for various applications.
* **Android's** November security updates were [released](https://source.android.com/security/bulletin/2021-11-01) last week.
* **Cisco** [released security updates](https://tools.cisco.com/security/center/publicationListing.x) for numerous products this month, including a [hard-coded password and SSH key vulnerability](https://www.bleepingcomputer.com/news/security/cisco-fixes-hard-coded-credentials-and-default-ssh-key-issues/).
* **SAP** [released](https://wiki.scn.sap.com/wiki/x/IAIjIw) its November 2021 security updates.


The November 2021 Patch Tuesday Security Updates
------------------------------------------------


Below is the complete list of resolved vulnerabilities and released advisories in the November 2021 Patch Tuesday updates. To access the full description of each vulnerability and the systems that it affects, you can view the [full report here](https://www.bleepingcomputer.com/microsoft-patch-tuesday-reports/November-2021.html).





| Tag | CVE ID | CVE Title | Severity |
| --- | --- | --- | --- |
| 3D Viewer | [CVE-2021-43209](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-43209) | 3D Viewer Remote Code Execution Vulnerability | Important |
| 3D Viewer | [CVE-2021-43208](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-43208) | 3D Viewer Remote Code Execution Vulnerability | Important |
| Azure | [CVE-2021-41373](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41373) | FSLogix Information Disclosure Vulnerability | Important |
| Azure RTOS | [CVE-2021-42303](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42303) | Azure RTOS Elevation of Privilege Vulnerability | Important |
| Azure RTOS | [CVE-2021-42302](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42302) | Azure RTOS Elevation of Privilege Vulnerability | Important |
| Azure RTOS | [CVE-2021-42301](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42301) | Azure RTOS Information Disclosure Vulnerability | Important |
| Azure RTOS | [CVE-2021-42323](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42323) | Azure RTOS Information Disclosure Vulnerability | Important |
| Azure RTOS | [CVE-2021-26444](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26444) | Azure RTOS Information Disclosure Vulnerability | Important |
| Azure RTOS | [CVE-2021-42304](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42304) | Azure RTOS Elevation of Privilege Vulnerability | Important |
| Azure Sphere | [CVE-2021-41374](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41374) | Azure Sphere Information Disclosure Vulnerability | Important |
| Azure Sphere | [CVE-2021-41376](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41376) | Azure Sphere Information Disclosure Vulnerability | Important |
| Azure Sphere | [CVE-2021-42300](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42300) | Azure Sphere Tampering Vulnerability | Important |
| Azure Sphere | [CVE-2021-41375](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41375) | Azure Sphere Information Disclosure Vulnerability | Important |
| Microsoft Dynamics | [CVE-2021-42316](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42316) | Microsoft Dynamics 365 (on-premises) Remote Code Execution Vulnerability | Critical |
| Microsoft Edge (Chromium-based) in IE Mode | [CVE-2021-41351](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41351) | Microsoft Edge (Chrome based) Spoofing on IE Mode | Important |
| Microsoft Exchange Server | [CVE-2021-42305](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42305) | Microsoft Exchange Server Spoofing Vulnerability | Important |
| Microsoft Exchange Server | [CVE-2021-41349](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41349) | Microsoft Exchange Server Spoofing Vulnerability | Important |
| Microsoft Exchange Server | [CVE-2021-42321](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42321) | Microsoft Exchange Server Remote Code Execution Vulnerability | Important |
| Microsoft Office Access | [CVE-2021-41368](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41368) | Microsoft Access Remote Code Execution Vulnerability | Important |
| Microsoft Office Excel | [CVE-2021-40442](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-40442) | Microsoft Excel Remote Code Execution Vulnerability | Important |
| Microsoft Office Excel | [CVE-2021-42292](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42292) | Microsoft Excel Security Feature Bypass Vulnerability | Important |
| Microsoft Office Word | [CVE-2021-42296](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42296) | Microsoft Word Remote Code Execution Vulnerability | Important |
| Microsoft Windows | [CVE-2021-41356](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41356) | Windows Denial of Service Vulnerability | Important |
| Microsoft Windows Codecs Library | [CVE-2021-42276](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42276) | Microsoft Windows Media Foundation Remote Code Execution Vulnerability | Important |
| Power BI | [CVE-2021-41372](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41372) | Power BI Report Server Spoofing Vulnerability | Important |
| Role: Windows Hyper-V | [CVE-2021-42284](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42284) | Windows Hyper-V Denial of Service Vulnerability | Important |
| Role: Windows Hyper-V | [CVE-2021-42274](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42274) | Windows Hyper-V Discrete Device Assignment (DDA) Denial of Service Vulnerability | Important |
| Visual Studio | [CVE-2021-3711](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-3711) | OpenSSL: CVE-2021-3711 SM2 Decryption Buffer Overflow | Critical |
| Visual Studio | [CVE-2021-42319](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42319) | Visual Studio Elevation of Privilege Vulnerability | Important |
| Visual Studio Code | [CVE-2021-42322](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42322) | Visual Studio Code Elevation of Privilege Vulnerability | Important |
| Windows Active Directory | [CVE-2021-42278](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42278) | Active Directory Domain Services Elevation of Privilege Vulnerability | Important |
| Windows Active Directory | [CVE-2021-42291](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42291) | Active Directory Domain Services Elevation of Privilege Vulnerability | Important |
| Windows Active Directory | [CVE-2021-42287](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42287) | Active Directory Domain Services Elevation of Privilege Vulnerability | Important |
| Windows Active Directory | [CVE-2021-42282](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42282) | Active Directory Domain Services Elevation of Privilege Vulnerability | Important |
| Windows COM | [CVE-2021-42275](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42275) | Microsoft COM for Windows Remote Code Execution Vulnerability | Important |
| Windows Core Shell | [CVE-2021-42286](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42286) | Windows Core Shell SI Host Extension Framework for Composable Shell Elevation of Privilege Vulnerability | Important |
| Windows Cred SSProvider Protocol | [CVE-2021-41366](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41366) | Credential Security Support Provider Protocol (CredSSP) Elevation of Privilege Vulnerability | Important |
| Windows Defender | [CVE-2021-42298](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42298) | Microsoft Defender Remote Code Execution Vulnerability | Critical |
| Windows Desktop Bridge | [CVE-2021-36957](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36957) | Windows Desktop Bridge Elevation of Privilege Vulnerability | Important |
| Windows Diagnostic Hub | [CVE-2021-42277](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42277) | Diagnostics Hub Standard Collector Elevation of Privilege Vulnerability | Important |
| Windows Fastfat Driver | [CVE-2021-41377](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41377) | Windows Fast FAT File System Driver Elevation of Privilege Vulnerability | Important |
| Windows Feedback Hub | [CVE-2021-42280](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42280) | Windows Feedback Hub Elevation of Privilege Vulnerability | Important |
| Windows Hello | [CVE-2021-42288](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42288) | Windows Hello Security Feature Bypass Vulnerability | Important |
| Windows Installer | [CVE-2021-41379](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41379) | Windows Installer Elevation of Privilege Vulnerability | Important |
| Windows Kernel | [CVE-2021-42285](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42285) | Windows Kernel Elevation of Privilege Vulnerability | Important |
| Windows NTFS | [CVE-2021-42283](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42283) | NTFS Elevation of Privilege Vulnerability | Important |
| Windows NTFS | [CVE-2021-41370](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41370) | NTFS Elevation of Privilege Vulnerability | Important |
| Windows NTFS | [CVE-2021-41378](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41378) | Windows NTFS Remote Code Execution Vulnerability | Important |
| Windows NTFS | [CVE-2021-41367](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41367) | NTFS Elevation of Privilege Vulnerability | Important |
| Windows RDP | [CVE-2021-38665](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38665) | Remote Desktop Protocol Client Information Disclosure Vulnerability | Important |
| Windows RDP | [CVE-2021-38631](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38631) | Windows Remote Desktop Protocol (RDP) Information Disclosure Vulnerability | Important |
| Windows RDP | [CVE-2021-38666](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-38666) | Remote Desktop Client Remote Code Execution Vulnerability | Critical |
| Windows RDP | [CVE-2021-41371](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-41371) | Windows Remote Desktop Protocol (RDP) Information Disclosure Vulnerability | Important |
| Windows Scripting | [CVE-2021-42279](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-42279) | Chakra Scripting Engine Memory Corruption Vulnerability | Critical |
| Windows Virtual Machine Bus | [CVE-2021-26443](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26443) | Microsoft Virtual Machine Bus (VMBus) Remote Code Execution Vulnerability | Critical |




#### Tags:
[[Windows]] [[Microsoft]] [[RTOS]] [[NTFS]] [[3D]] [[zero-day]] [[(RDP)]] [[Hyper-V]] [[RDP]] [[CVE-2021-42292]] [[Bleeping Computer]]
