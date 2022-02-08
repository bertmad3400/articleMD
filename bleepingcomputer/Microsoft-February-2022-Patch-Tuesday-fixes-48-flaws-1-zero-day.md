# Microsoft February 2022 Patch Tuesday fixes 48 flaws, 1 zero-day
### Today is Microsoft's February 2022 Patch Tuesday, and with it comes fixes for one zero-day vulnerability and a total of 48 flaws.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-february-2022-patch-tuesday-fixes-48-flaws-1-zero-day/
+ Date: 2022-02-08T13:27:31-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2020/06/09/patch-tuesday-header.jpg)

![Patch Tuesday](https://www.bleepstatic.com/images/stock-photos/operating-systems/windows-10/patch-tuesday-large.jpg)


.crit {
font-weight:bold;
color:red;
}
.article\_section td {
 font-size: 14px!important;
}
Today is Microsoft's February 2022 Patch Tuesday, and with it comes fixes for one zero-day vulnerability and a total of 48 flaws.


Microsoft has fixed 48 vulnerabilities (not including 22 Microsoft Edge vulnerabilities ) with today's update, with none of them classified as Critical.


The number for each type of vulnerability is listed below:


* 16 Elevation of Privilege Vulnerabilities
* 3 Security Feature Bypass Vulnerabilities
* 16 Remote Code Execution Vulnerabilities
* 5 Information Disclosure Vulnerabilities
* 5 Denial of Service Vulnerabilities
* 3 Spoofing Vulnerabilities
* 22 Edge - Chromium Vulnerabilities

One zero-day fixed, none actively exploited
-------------------------------------------


This month's Patch Tuesday includes fixes for one publicly disclosed zero-day vulnerabilities. The good news is that there were no zero-day vulnerabilities actively exploited in attacks from this Patch Tuesday.


Microsoft classifies a vulnerability as a zero-day if it is publicly disclosed or actively exploited with no official fix available.


The publicly disclosed vulnerabilities fixes as part of the February 2022 Patch Tuesday are:


* [CVE-2022-21989](http://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21989) - Windows Kernel Elevation of Privilege Vulnerability

However, as many of these have public proof-of-concept exploits available, they will likely be exploited by threat actors soon.


Recent updates from other companies
-----------------------------------


Other vendors who released updates in February 2022 include:


* **Android's** February security updates were [released](https://source.android.com/security/bulletin/2022-02-01) yesterday.
* **Cisco** [released security updates](https://tools.cisco.com/security/center/publicationListing.x) for numerous products this month, including Cisco Small Business RV routers, Snort, and Cisco DNA Center.
* **SAP** released its [February 2022 security updates](https://wiki.scn.sap.com/wiki/display/PSR/SAP+Security+Patch+Day+-+February+2022).

The February 2022 Patch Tuesday Security Updates
------------------------------------------------


Below is the complete list of resolved vulnerabilities and released advisories in the February 2022 Patch Tuesday updates. To access the full description of each vulnerability and the systems that it affects, you can view the [full report here](https://www.bleepingcomputer.com/microsoft-patch-tuesday-reports/Feb-2022.html).





| Tag | CVE ID | CVE Title | Severity |
| --- | --- | --- | --- |
| Azure Data Explorer | [CVE-2022-23256](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-23256) | Azure Data Explorer Spoofing Vulnerability | Important |
| Kestrel Web Server | [CVE-2022-21986](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21986) | .NET Denial of Service Vulnerability | Important |
| Microsoft Dynamics | [CVE-2022-21957](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21957) | Microsoft Dynamics 365 (on-premises) Remote Code Execution Vulnerability | Important |
| Microsoft Dynamics GP | [CVE-2022-23272](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-23272) | Microsoft Dynamics GP Elevation Of Privilege Vulnerability | Important |
| Microsoft Dynamics GP | [CVE-2022-23271](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-23271) | Microsoft Dynamics GP Elevation Of Privilege Vulnerability | Important |
| Microsoft Dynamics GP | [CVE-2022-23273](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-23273) | Microsoft Dynamics GP Elevation Of Privilege Vulnerability | Important |
| Microsoft Dynamics GP | [CVE-2022-23274](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-23274) | Microsoft Dynamics GP Remote Code Execution Vulnerability | Important |
| Microsoft Dynamics GP | [CVE-2022-23269](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-23269) | Microsoft Dynamics GP Spoofing Vulnerability | Important |
| Microsoft Edge (Chromium-based) | [CVE-2022-0469](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0469) | Chromium: CVE-2022-0469 Use after free in Cast | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0467](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0467) | Chromium: CVE-2022-0467 Inappropriate implementation in Pointer Lock | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-23261](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-23261) | Microsoft Edge (Chromium-based) Tampering Vulnerability | Moderate |
| Microsoft Edge (Chromium-based) | [CVE-2022-0453](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0453) | Chromium: CVE-2022-0453 Use after free in Reader Mode | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-23262](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-23262) | Microsoft Edge (Chromium-based) Elevation of Privilege Vulnerability | Important |
| Microsoft Edge (Chromium-based) | [CVE-2022-0468](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0468) | Chromium: CVE-2022-0468 Use after free in Payments | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0452](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0452) | Chromium: CVE-2022-0452 Use after free in Safe Browsing | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-23263](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-23263) | Microsoft Edge (Chromium-based) Elevation of Privilege Vulnerability | Important |
| Microsoft Edge (Chromium-based) | [CVE-2022-0462](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0462) | Chromium: CVE-2022-0462 Inappropriate implementation in Scroll | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0461](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0461) | Chromium: CVE-2022-0461 Policy bypass in COOP | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0460](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0460) | Chromium: CVE-2022-0460 Use after free in Window Dialog | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0465](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0465) | Chromium: CVE-2022-0465 Use after free in Extensions | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0464](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0464) | Chromium: CVE-2022-0464 Use after free in Accessibility | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0463](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0463) | Chromium: CVE-2022-0463 Use after free in Accessibility | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0459](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0459) | Chromium: CVE-2022-0459 Use after free in Screen Capture | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0455](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0455) | Chromium: CVE-2022-0455 Inappropriate implementation in Full Screen Mode | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0454](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0454) | Chromium: CVE-2022-0454 Heap buffer overflow in ANGLE | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0466](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0466) | Chromium: CVE-2022-0466 Inappropriate implementation in Extensions Platform | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0458](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0458) | Chromium: CVE-2022-0458 Use after free in Thumbnail Tab Strip | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0457](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0457) | Chromium: CVE-2022-0457 Type Confusion in V8 | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0456](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0456) | Chromium: CVE-2022-0456 Use after free in Web Search | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0470](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0470) | Chromium: CVE-2022-0470 Out of bounds memory access in V8 | Unknown |
| Microsoft Office | [CVE-2022-22004](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-22004) | Microsoft Office ClickToRun Remote Code Execution Vulnerability | Important |
| Microsoft Office | [CVE-2022-22003](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-22003) | Microsoft Office Graphics Remote Code Execution Vulnerability | Important |
| Microsoft Office | [CVE-2022-23252](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-23252) | Microsoft Office Information Disclosure Vulnerability | Important |
| Microsoft Office Excel | [CVE-2022-22716](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-22716) | Microsoft Excel Information Disclosure Vulnerability | Important |
| Microsoft Office Outlook | [CVE-2022-23280](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-23280) | Microsoft Outlook for Mac Security Feature Bypass Vulnerability | Important |
| Microsoft Office SharePoint | [CVE-2022-21987](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21987) | Microsoft SharePoint Server Spoofing Vulnerability | Important |
| Microsoft Office SharePoint | [CVE-2022-21968](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21968) | Microsoft SharePoint Server Security Feature BypassVulnerability | Important |
| Microsoft Office SharePoint | [CVE-2022-22005](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-22005) | Microsoft SharePoint Server Remote Code Execution Vulnerability | Important |
| Microsoft Office Visio | [CVE-2022-21988](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21988) | Microsoft Office Visio Remote Code Execution Vulnerability | Important |
| Microsoft OneDrive | [CVE-2022-23255](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-23255) | Microsoft OneDrive for Android Security Feature Bypass Vulnerability | Important |
| Microsoft Teams | [CVE-2022-21965](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21965) | Microsoft Teams Denial of Service Vulnerability | Important |
| Microsoft Windows Codecs Library | [CVE-2022-21844](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21844) | HEVC Video Extensions Remote Code Execution Vulnerability | Important |
| Microsoft Windows Codecs Library | [CVE-2022-21927](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21927) | HEVC Video Extensions Remote Code Execution Vulnerability | Important |
| Microsoft Windows Codecs Library | [CVE-2022-21926](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21926) | HEVC Video Extensions Remote Code Execution Vulnerability | Important |
| Microsoft Windows Codecs Library | [CVE-2022-22709](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-22709) | VP9 Video Extensions Remote Code Execution Vulnerability | Important |
| Power BI | [CVE-2022-23254](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-23254) | Microsoft Power BI Elevation of Privilege Vulnerability | Important |
| Roaming Security Rights Management Services | [CVE-2022-21974](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21974) | Roaming Security Rights Management Services Remote Code Execution Vulnerability | Important |
| Role: DNS Server | [CVE-2022-21984](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21984) | Windows DNS Server Remote Code Execution Vulnerability | Important |
| Role: Windows Hyper-V | [CVE-2022-21995](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21995) | Windows Hyper-V Remote Code Execution Vulnerability | Important |
| Role: Windows Hyper-V | [CVE-2022-22712](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-22712) | Windows Hyper-V Denial of Service Vulnerability | Important |
| SQL Server | [CVE-2022-23276](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-23276) | SQL Server for Linux Containers Elevation of Privilege Vulnerability | Important |
| Visual Studio Code | [CVE-2022-21991](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21991) | Visual Studio Code Remote Development Extension Remote Code Execution Vulnerability | Important |
| Windows Common Log File System Driver | [CVE-2022-22000](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-22000) | Windows Common Log File System Driver Elevation of Privilege Vulnerability | Important |
| Windows Common Log File System Driver | [CVE-2022-22710](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-22710) | Windows Common Log File System Driver Denial of Service Vulnerability | Important |
| Windows Common Log File System Driver | [CVE-2022-21981](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21981) | Windows Common Log File System Driver Elevation of Privilege Vulnerability | Important |
| Windows Common Log File System Driver | [CVE-2022-21998](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21998) | Windows Common Log File System Driver Information Disclosure Vulnerability | Important |
| Windows DWM Core Library | [CVE-2022-21994](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21994) | Windows DWM Core Library Elevation of Privilege Vulnerability | Important |
| Windows Kernel | [CVE-2022-21989](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21989) | Windows Kernel Elevation of Privilege Vulnerability | Important |
| Windows Kernel | [CVE-2022-21992](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21992) | Windows Mobile Device Management Remote Code Execution Vulnerability | Important |
| Windows Kernel-Mode Drivers | [CVE-2022-21993](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21993) | Windows Services for NFS ONCRPC XDR Driver Information Disclosure Vulnerability | Important |
| Windows Named Pipe File System | [CVE-2022-22715](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-22715) | Named Pipe File System Elevation of Privilege Vulnerability | Important |
| Windows Print Spooler Components | [CVE-2022-22718](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-22718) | Windows Print Spooler Elevation of Privilege Vulnerability | Important |
| Windows Print Spooler Components | [CVE-2022-22717](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-22717) | Windows Print Spooler Elevation of Privilege Vulnerability | Important |
| Windows Print Spooler Components | [CVE-2022-21999](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21999) | Windows Print Spooler Elevation of Privilege Vulnerability | Important |
| Windows Print Spooler Components | [CVE-2022-21997](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21997) | Windows Print Spooler Elevation of Privilege Vulnerability | Important |
| Windows Remote Access Connection Manager | [CVE-2022-21985](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21985) | Windows Remote Access Connection Manager Information Disclosure Vulnerability | Important |
| Windows Remote Access Connection Manager | [CVE-2022-22001](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-22001) | Windows Remote Access Connection Manager Elevation of Privilege Vulnerability | Important |
| Windows Remote Procedure Call Runtime | [CVE-2022-21971](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21971) | Windows Runtime Remote Code Execution Vulnerability | Important |
| Windows User Account Profile | [CVE-2022-22002](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-22002) | Windows User Account Profile Picture Denial of Service Vulnerability | Important |
| Windows Win32K | [CVE-2022-21996](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21996) | Win32k Elevation of Privilege Vulnerability | Important |





## Tags:

#### Threatactor:
[[threatactor.name=Sidewinder]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=route]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Windows]] [[(chromium-based)]] [[Sharepoint]] [[Zero-day]] [[Hyper-v]] [[Hevc]] [[Bleeping Computer]]
#### CVE's
[[CVE-2022-21989]] [[CVE-2022-23256]] [[CVE-2022-21986]] [[CVE-2022-21957]] [[CVE-2022-23272]] [[CVE-2022-23271]] [[CVE-2022-23273]] [[CVE-2022-23274]] [[CVE-2022-23269]] [[CVE-2022-0469]] [[CVE-2022-0467]] [[CVE-2022-23261]] [[CVE-2022-0453]] [[CVE-2022-23262]] [[CVE-2022-0468]] [[CVE-2022-0452]] [[CVE-2022-23263]] [[CVE-2022-0462]] [[CVE-2022-0461]] [[CVE-2022-0460]] [[CVE-2022-0465]] [[CVE-2022-0464]] [[CVE-2022-0463]] [[CVE-2022-0459]] [[CVE-2022-0455]] [[CVE-2022-0454]] [[CVE-2022-0466]] [[CVE-2022-0458]] [[CVE-2022-0457]] [[CVE-2022-0456]] [[CVE-2022-0470]] [[CVE-2022-22004]] [[CVE-2022-22003]] [[CVE-2022-23252]] [[CVE-2022-22716]] [[CVE-2022-23280]] [[CVE-2022-21987]] [[CVE-2022-21968]] [[CVE-2022-22005]] [[CVE-2022-21988]] [[CVE-2022-23255]] [[CVE-2022-21965]] [[CVE-2022-21844]] [[CVE-2022-21927]] [[CVE-2022-21926]] [[CVE-2022-22709]] [[CVE-2022-23254]] [[CVE-2022-21974]] [[CVE-2022-21984]] [[CVE-2022-21995]] [[CVE-2022-22712]] [[CVE-2022-23276]] [[CVE-2022-21991]] [[CVE-2022-22000]] [[CVE-2022-22710]] [[CVE-2022-21981]] [[CVE-2022-21998]] [[CVE-2022-21994]] [[CVE-2022-21992]] [[CVE-2022-21993]] [[CVE-2022-22715]] [[CVE-2022-22718]] [[CVE-2022-22717]] [[CVE-2022-21999]] [[CVE-2022-21997]] [[CVE-2022-21985]] [[CVE-2022-22001]] [[CVE-2022-21971]] [[CVE-2022-22002]] [[CVE-2022-21996]]

