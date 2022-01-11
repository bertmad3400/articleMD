# Microsoft January 2022 Patch Tuesday fixes 6 zero-days, 97 flaws
### Today is Microsoft's January 2022 Patch Tuesday, and with it comes fixes for six zero-day vulnerabilities and a total of 97 flaws.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-january-2022-patch-tuesday-fixes-6-zero-days-97-flaws/
+ Date: 2022-01-11T13:31:10-05:00
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
Today is Microsoft's January 2022 Patch Tuesday, and with it comes fixes for six zero-day vulnerabilities and a total of 97 flaws.


Microsoft has fixed 97 vulnerabilities (not including 29 Microsoft Edge vulnerabilities ) with today's update, with nine classified as Critical and 88 as Important.


The number of each type of vulnerability is listed below:


* 41 Elevation of Privilege Vulnerabilities
* 9 Security Feature Bypass Vulnerabilities
* 29 Remote Code Execution Vulnerabilities
* 6 Information Disclosure Vulnerabilities
* 9 Denial of Service Vulnerabilities
* 3 Spoofing Vulnerabilities

Six zero-days fixed, none actively exploited
--------------------------------------------


This month's Patch Tuesday includes fixes for six publicly disclosed zero-day vulnerabilities. The good news is that none of them have been actively exploited in attacks.


Microsoft classifies a vulnerability as a zero-day if it is publicly disclosed or actively exploited with no official fix available.


The publicly disclosed vulnerabilities fixes as part of the December 2021 Patch Tuesday are:


* [CVE-2021-22947](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-22947) - Open Source Curl Remote Code Execution Vulnerability
* [CVE-2021-36976](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36976) - Libarchive Remote Code Execution Vulnerability
* [CVE-2022-21919](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21919) - Windows User Profile Service Elevation of Privilege Vulnerability
* [CVE-2022-21836](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21836) - Windows Certificate Spoofing Vulnerability
* [CVE-2022-21839](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21839) - Windows Event Tracing Discretionary Access Control List Denial of Service Vulnerability
* [CVE-2022-21874](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21874) - Windows Security Center API Remote Code Execution Vulnerability

Both the Curl and Libarchive vulnerabilities had already been fixed by their maintainers but the fixes were not added to Windows until today.


However, as many of these have public proof-of-concept exploits available, they will likely be exploited by threat actors soon.


Recent updates from other companies
-----------------------------------


Other vendors who released updates in January 2022 include:


* **Adobe's** [January updates](https://helpx.adobe.com/security/security-bulletin.html) are released today.
* **Android's** December security updates were [released](https://source.android.com/security/bulletin/2022-01-01) last week.
* **Cisco** [released security updates](https://tools.cisco.com/security/center/publicationListing.x) for numerous products this month, including Cisco Prime Infrastructure and Cisco Common Services Platform Collector.
* **SAP** released its [January 2022 security updates](https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=596902035).
* **VMWare** [released fixes](https://www.vmware.com/security/advisories/VMSA-2022-0001.html) for a code execution vulnerability in VMWare Workstation, Fusion, and ESXi.

The January 2022 Patch Tuesday Security Updates
-----------------------------------------------


Below is the complete list of resolved vulnerabilities and released advisories in the January 2022 Patch Tuesday updates. To access the full description of each vulnerability and the systems that it affects, you can view the [full report here](https://www.bleepingcomputer.com/microsoft-patch-tuesday-reports/Jan-2022.html).





| Tag | CVE ID | CVE Title | Severity |
| --- | --- | --- | --- |
| .NET Framework | [CVE-2022-21911](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21911) | .NET Framework Denial of Service Vulnerability | Important |
| Microsoft Dynamics | [CVE-2022-21932](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21932) | Microsoft Dynamics 365 Customer Engagement Cross-Site Scripting Vulnerability | Important |
| Microsoft Dynamics | [CVE-2022-21891](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21891) | Microsoft Dynamics 365 (on-premises) Spoofing Vulnerability | Important |
| Microsoft Edge (Chromium-based) | [CVE-2022-0105](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0105) | Chromium: CVE-2022-0105 Use after free in PDF | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0102](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0102) | Chromium: CVE-2022-0102 Type Confusion in V8 | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0104](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0104) | Chromium: CVE-2022-0104 Heap buffer overflow in ANGLE | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0101](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0101) | Chromium: CVE-2022-0101 Heap buffer overflow in Bookmarks | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0103](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0103) | Chromium: CVE-2022-0103 Use after free in SwiftShader | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0109](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0109) | Chromium: CVE-2022-0109 Inappropriate implementation in Autofill | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0110](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0110) | Chromium: CVE-2022-0110 Incorrect security UI in Autofill | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0108](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0108) | Chromium: CVE-2022-0108 Inappropriate implementation in Navigation | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0106](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0106) | Chromium: CVE-2022-0106 Use after free in Autofill | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0107](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0107) | Chromium: CVE-2022-0107 Use after free in File Manager API | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-21954](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21954) | Microsoft Edge (Chromium-based) Elevation of Privilege Vulnerability | Important |
| Microsoft Edge (Chromium-based) | [CVE-2022-21970](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21970) | Microsoft Edge (Chromium-based) Elevation of Privilege Vulnerability | Important |
| Microsoft Edge (Chromium-based) | [CVE-2022-21931](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21931) | Microsoft Edge (Chromium-based) Remote Code Execution Vulnerability | Important |
| Microsoft Edge (Chromium-based) | [CVE-2022-21929](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21929) | Microsoft Edge (Chromium-based) Remote Code Execution Vulnerability | Moderate |
| Microsoft Edge (Chromium-based) | [CVE-2022-21930](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21930) | Microsoft Edge (Chromium-based) Remote Code Execution Vulnerability | Important |
| Microsoft Edge (Chromium-based) | [CVE-2022-0099](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0099) | Chromium: CVE-2022-0099 Use after free in Sign-in | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0100](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0100) | Chromium: CVE-2022-0100 Heap buffer overflow in Media streams API | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0098](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0098) | Chromium: CVE-2022-0098 Use after free in Screen Capture | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0096](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0096) | Chromium: CVE-2022-0096 Use after free in Storage | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0097](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0097) | Chromium: CVE-2022-0097 Inappropriate implementation in DevTools | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0116](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0116) | Chromium: CVE-2022-0116 Inappropriate implementation in Compositing | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0117](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0117) | Chromium: CVE-2022-0117 Policy bypass in Service Workers | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0115](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0115) | Chromium: CVE-2022-0115 Uninitialized Use in File API | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0113](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0113) | Chromium: CVE-2022-0113 Inappropriate implementation in Blink | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0114](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0114) | Chromium: CVE-2022-0114 Out of bounds memory access in Web Serial | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0118](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0118) | Chromium: CVE-2022-0118 Inappropriate implementation in WebShare | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0111](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0111) | Chromium: CVE-2022-0111 Inappropriate implementation in Navigation | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0112](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0112) | Chromium: CVE-2022-0112 Incorrect security UI in Browser UI | Unknown |
| Microsoft Edge (Chromium-based) | [CVE-2022-0120](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-0120) | Chromium: CVE-2022-0120 Inappropriate implementation in Passwords | Unknown |
| Microsoft Exchange Server | [CVE-2022-21969](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21969) | Microsoft Exchange Server Remote Code Execution Vulnerability | Important |
| Microsoft Exchange Server | [CVE-2022-21846](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21846) | Microsoft Exchange Server Remote Code Execution Vulnerability | Critical |
| Microsoft Exchange Server | [CVE-2022-21855](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21855) | Microsoft Exchange Server Remote Code Execution Vulnerability | Important |
| Microsoft Graphics Component | [CVE-2022-21904](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21904) | Windows GDI Information Disclosure Vulnerability | Important |
| Microsoft Graphics Component | [CVE-2022-21903](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21903) | Windows GDI Elevation of Privilege Vulnerability | Important |
| Microsoft Graphics Component | [CVE-2022-21915](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21915) | Windows GDI+ Information Disclosure Vulnerability | Important |
| Microsoft Graphics Component | [CVE-2022-21880](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21880) | Windows GDI+ Information Disclosure Vulnerability | Important |
| Microsoft Office | [CVE-2022-21840](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21840) | Microsoft Office Remote Code Execution Vulnerability | Critical |
| Microsoft Office Excel | [CVE-2022-21841](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21841) | Microsoft Excel Remote Code Execution Vulnerability | Important |
| Microsoft Office SharePoint | [CVE-2022-21837](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21837) | Microsoft SharePoint Server Remote Code Execution Vulnerability | Important |
| Microsoft Office Word | [CVE-2022-21842](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21842) | Microsoft Word Remote Code Execution Vulnerability | Important |
| Microsoft Windows Codecs Library | [CVE-2022-21917](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21917) | HEVC Video Extensions Remote Code Execution Vulnerability | Critical |
| Open Source Software | [CVE-2021-22947](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-22947) | Open Source Curl Remote Code Execution Vulnerability | Critical |
| Role: Windows Hyper-V | [CVE-2022-21901](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21901) | Windows Hyper-V Elevation of Privilege Vulnerability | Important |
| Role: Windows Hyper-V | [CVE-2022-21900](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21900) | Windows Hyper-V Security Feature Bypass Vulnerability | Important |
| Role: Windows Hyper-V | [CVE-2022-21905](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21905) | Windows Hyper-V Security Feature Bypass Vulnerability | Important |
| Role: Windows Hyper-V | [CVE-2022-21847](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21847) | Windows Hyper-V Denial of Service Vulnerability | Important |
| Tablet Windows User Interface | [CVE-2022-21870](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21870) | Tablet Windows User Interface Application Core Elevation of Privilege Vulnerability | Important |
| Windows Account Control | [CVE-2022-21859](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21859) | Windows Accounts Control Elevation of Privilege Vulnerability | Important |
| Windows Active Directory | [CVE-2022-21857](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21857) | Active Directory Domain Services Elevation of Privilege Vulnerability | Critical |
| Windows AppContracts API Server | [CVE-2022-21860](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21860) | Windows AppContracts API Server Elevation of Privilege Vulnerability | Important |
| Windows Application Model | [CVE-2022-21862](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21862) | Windows Application Model Core API Elevation of Privilege Vulnerability | Important |
| Windows BackupKey Remote Protocol | [CVE-2022-21925](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21925) | Windows BackupKey Remote Protocol Security Feature Bypass Vulnerability | Important |
| Windows Bind Filter Driver | [CVE-2022-21858](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21858) | Windows Bind Filter Driver Elevation of Privilege Vulnerability | Important |
| Windows Certificates | [CVE-2022-21836](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21836) | Windows Certificate Spoofing Vulnerability | Important |
| Windows Cleanup Manager | [CVE-2022-21838](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21838) | Windows Cleanup Manager Elevation of Privilege Vulnerability | Important |
| Windows Clipboard User Service | [CVE-2022-21869](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21869) | Clipboard User Service Elevation of Privilege Vulnerability | Important |
| Windows Cluster Port Driver | [CVE-2022-21910](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21910) | Microsoft Cluster Port Driver Elevation of Privilege Vulnerability | Important |
| Windows Common Log File System Driver | [CVE-2022-21897](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21897) | Windows Common Log File System Driver Elevation of Privilege Vulnerability | Important |
| Windows Common Log File System Driver | [CVE-2022-21916](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21916) | Windows Common Log File System Driver Elevation of Privilege Vulnerability | Important |
| Windows Connected Devices Platform Service | [CVE-2022-21865](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21865) | Connected Devices Platform Service Elevation of Privilege Vulnerability | Important |
| Windows Cryptographic Services | [CVE-2022-21835](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21835) | Microsoft Cryptographic Services Elevation of Privilege Vulnerability | Important |
| Windows Defender | [CVE-2022-21921](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21921) | Windows Defender Credential Guard Security Feature Bypass Vulnerability | Important |
| Windows Defender | [CVE-2022-21906](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21906) | Windows Defender Application Control Security Feature Bypass Vulnerability | Important |
| Windows Devices Human Interface | [CVE-2022-21868](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21868) | Windows Devices Human Interface Elevation of Privilege Vulnerability | Important |
| Windows Diagnostic Hub | [CVE-2022-21871](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21871) | Microsoft Diagnostics Hub Standard Collector Runtime Elevation of Privilege Vulnerability | Important |
| Windows DirectX | [CVE-2022-21898](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21898) | DirectX Graphics Kernel Remote Code Execution Vulnerability | Critical |
| Windows DirectX | [CVE-2022-21918](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21918) | DirectX Graphics Kernel File Denial of Service Vulnerability | Important |
| Windows DirectX | [CVE-2022-21912](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21912) | DirectX Graphics Kernel Remote Code Execution Vulnerability | Critical |
| Windows DWM Core Library | [CVE-2022-21852](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21852) | Windows DWM Core Library Elevation of Privilege Vulnerability | Important |
| Windows DWM Core Library | [CVE-2022-21902](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21902) | Windows DWM Core Library Elevation of Privilege Vulnerability | Important |
| Windows DWM Core Library | [CVE-2022-21896](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21896) | Windows DWM Core Library Elevation of Privilege Vulnerability | Important |
| Windows Event Tracing | [CVE-2022-21872](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21872) | Windows Event Tracing Elevation of Privilege Vulnerability | Important |
| Windows Event Tracing | [CVE-2022-21839](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21839) | Windows Event Tracing Discretionary Access Control List Denial of Service Vulnerability | Important |
| Windows Geolocation Service | [CVE-2022-21878](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21878) | Windows Geolocation Service Remote Code Execution Vulnerability | Important |
| Windows HTTP Protocol Stack | [CVE-2022-21907](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21907) | HTTP Protocol Stack Remote Code Execution Vulnerability | Critical |
| Windows IKE Extension | [CVE-2022-21843](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21843) | Windows IKE Extension Denial of Service Vulnerability | Important |
| Windows IKE Extension | [CVE-2022-21890](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21890) | Windows IKE Extension Denial of Service Vulnerability | Important |
| Windows IKE Extension | [CVE-2022-21883](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21883) | Windows IKE Extension Denial of Service Vulnerability | Important |
| Windows IKE Extension | [CVE-2022-21889](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21889) | Windows IKE Extension Denial of Service Vulnerability | Important |
| Windows IKE Extension | [CVE-2022-21848](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21848) | Windows IKE Extension Denial of Service Vulnerability | Important |
| Windows IKE Extension | [CVE-2022-21849](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21849) | Windows IKE Extension Remote Code Execution Vulnerability | Important |
| Windows Installer | [CVE-2022-21908](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21908) | Windows Installer Elevation of Privilege Vulnerability | Important |
| Windows Kerberos | [CVE-2022-21920](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21920) | Windows Kerberos Elevation of Privilege Vulnerability | Important |
| Windows Kernel | [CVE-2022-21881](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21881) | Windows Kernel Elevation of Privilege Vulnerability | Important |
| Windows Kernel | [CVE-2022-21879](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21879) | Windows Kernel Elevation of Privilege Vulnerability | Important |
| Windows Libarchive | [CVE-2021-36976](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-36976) | Libarchive Remote Code Execution Vulnerability | Important |
| Windows Local Security Authority | [CVE-2022-21913](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21913) | Local Security Authority (Domain Policy) Remote Protocol Security Feature Bypass | Important |
| Windows Local Security Authority Subsystem Service | [CVE-2022-21884](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21884) | Local Security Authority Subsystem Service Elevation of Privilege Vulnerability | Important |
| Windows Modern Execution Server | [CVE-2022-21888](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21888) | Windows Modern Execution Server Remote Code Execution Vulnerability | Important |
| Windows Push Notifications | [CVE-2022-21867](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21867) | Windows Push Notifications Apps Elevation Of Privilege Vulnerability | Important |
| Windows RDP | [CVE-2022-21851](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21851) | Remote Desktop Client Remote Code Execution Vulnerability | Important |
| Windows RDP | [CVE-2022-21850](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21850) | Remote Desktop Client Remote Code Execution Vulnerability | Important |
| Windows RDP | [CVE-2022-21893](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21893) | Remote Desktop Protocol Remote Code Execution Vulnerability | Important |
| Windows Remote Access Connection Manager | [CVE-2022-21914](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21914) | Windows Remote Access Connection Manager Elevation of Privilege Vulnerability | Important |
| Windows Remote Access Connection Manager | [CVE-2022-21885](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21885) | Windows Remote Access Connection Manager Elevation of Privilege Vulnerability | Important |
| Windows Remote Desktop | [CVE-2022-21964](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21964) | Remote Desktop Licensing Diagnoser Information Disclosure Vulnerability | Important |
| Windows Remote Procedure Call Runtime | [CVE-2022-21922](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21922) | Remote Procedure Call Runtime Remote Code Execution Vulnerability | Important |
| Windows Resilient File System (ReFS) | [CVE-2022-21961](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21961) | Windows Resilient File System (ReFS) Remote Code Execution Vulnerability | Important |
| Windows Resilient File System (ReFS) | [CVE-2022-21959](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21959) | Windows Resilient File System (ReFS) Remote Code Execution Vulnerability | Important |
| Windows Resilient File System (ReFS) | [CVE-2022-21958](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21958) | Windows Resilient File System (ReFS) Remote Code Execution Vulnerability | Important |
| Windows Resilient File System (ReFS) | [CVE-2022-21960](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21960) | Windows Resilient File System (ReFS) Remote Code Execution Vulnerability | Important |
| Windows Resilient File System (ReFS) | [CVE-2022-21963](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21963) | Windows Resilient File System (ReFS) Remote Code Execution Vulnerability | Important |
| Windows Resilient File System (ReFS) | [CVE-2022-21892](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21892) | Windows Resilient File System (ReFS) Remote Code Execution Vulnerability | Important |
| Windows Resilient File System (ReFS) | [CVE-2022-21962](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21962) | Windows Resilient File System (ReFS) Remote Code Execution Vulnerability | Important |
| Windows Resilient File System (ReFS) | [CVE-2022-21928](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21928) | Windows Resilient File System (ReFS) Remote Code Execution Vulnerability | Important |
| Windows Secure Boot | [CVE-2022-21894](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21894) | Secure Boot Security Feature Bypass Vulnerability | Important |
| Windows Security Center | [CVE-2022-21874](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21874) | Windows Security Center API Remote Code Execution Vulnerability | Important |
| Windows StateRepository API | [CVE-2022-21863](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21863) | Windows StateRepository API Server file Elevation of Privilege Vulnerability | Important |
| Windows Storage | [CVE-2022-21875](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21875) | Windows Storage Elevation of Privilege Vulnerability | Important |
| Windows Storage Spaces Controller | [CVE-2022-21877](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21877) | Storage Spaces Controller Information Disclosure Vulnerability | Important |
| Windows System Launcher | [CVE-2022-21866](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21866) | Windows System Launcher Elevation of Privilege Vulnerability | Important |
| Windows Task Flow Data Engine | [CVE-2022-21861](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21861) | Task Flow Data Engine Elevation of Privilege Vulnerability | Important |
| Windows Tile Data Repository | [CVE-2022-21873](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21873) | Tile Data Repository Elevation of Privilege Vulnerability | Important |
| Windows UEFI | [CVE-2022-21899](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21899) | Windows Extensible Firmware Interface Security Feature Bypass Vulnerability | Important |
| Windows UI Immersive Server | [CVE-2022-21864](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21864) | Windows UI Immersive Server API Elevation of Privilege Vulnerability | Important |
| Windows User Profile Service | [CVE-2022-21895](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21895) | Windows User Profile Service Elevation of Privilege Vulnerability | Important |
| Windows User Profile Service | [CVE-2022-21919](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21919) | Windows User Profile Service Elevation of Privilege Vulnerability | Important |
| Windows User-mode Driver Framework | [CVE-2022-21834](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21834) | Windows User-mode Driver Framework Reflector Driver Elevation of Privilege Vulnerability | Important |
| Windows Virtual Machine IDE Drive | [CVE-2022-21833](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21833) | Virtual Machine IDE Drive Elevation of Privilege Vulnerability | Critical |
| Windows Win32K | [CVE-2022-21882](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21882) | Win32k Elevation of Privilege Vulnerability | Important |
| Windows Win32K | [CVE-2022-21876](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21876) | Win32k Information Disclosure Vulnerability | Important |
| Windows Win32K | [CVE-2022-21887](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21887) | Win32k Elevation of Privilege Vulnerability | Important |
| Windows Workstation Service Remote Protocol | [CVE-2022-21924](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21924) | Workstation Service Remote Protocol Security Feature Bypass Vulnerability | Important |





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Information]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[(chromium-based)]] [[(refs)]] [[Api]] [[Hyper-v]] [[Directx]] [[Dwm]] [[Libarchive]] [[Zero-day]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-22947]] [[CVE-2021-36976]] [[CVE-2022-21919]] [[CVE-2022-21836]] [[CVE-2022-21839]] [[CVE-2022-21874]] [[CVE-2022-21911]] [[CVE-2022-21932]] [[CVE-2022-21891]] [[CVE-2022-0105]] [[CVE-2022-0102]] [[CVE-2022-0104]] [[CVE-2022-0101]] [[CVE-2022-0103]] [[CVE-2022-0109]] [[CVE-2022-0110]] [[CVE-2022-0108]] [[CVE-2022-0106]] [[CVE-2022-0107]] [[CVE-2022-21954]] [[CVE-2022-21970]] [[CVE-2022-21931]] [[CVE-2022-21929]] [[CVE-2022-21930]] [[CVE-2022-0099]] [[CVE-2022-0100]] [[CVE-2022-0098]] [[CVE-2022-0096]] [[CVE-2022-0097]] [[CVE-2022-0116]] [[CVE-2022-0117]] [[CVE-2022-0115]] [[CVE-2022-0113]] [[CVE-2022-0114]] [[CVE-2022-0118]] [[CVE-2022-0111]] [[CVE-2022-0112]] [[CVE-2022-0120]] [[CVE-2022-21969]] [[CVE-2022-21846]] [[CVE-2022-21855]] [[CVE-2022-21904]] [[CVE-2022-21903]] [[CVE-2022-21915]] [[CVE-2022-21880]] [[CVE-2022-21840]] [[CVE-2022-21841]] [[CVE-2022-21837]] [[CVE-2022-21842]] [[CVE-2022-21917]] [[CVE-2022-21901]] [[CVE-2022-21900]] [[CVE-2022-21905]] [[CVE-2022-21847]] [[CVE-2022-21870]] [[CVE-2022-21859]] [[CVE-2022-21857]] [[CVE-2022-21860]] [[CVE-2022-21862]] [[CVE-2022-21925]] [[CVE-2022-21858]] [[CVE-2022-21838]] [[CVE-2022-21869]] [[CVE-2022-21910]] [[CVE-2022-21897]] [[CVE-2022-21916]] [[CVE-2022-21865]] [[CVE-2022-21835]] [[CVE-2022-21921]] [[CVE-2022-21906]] [[CVE-2022-21868]] [[CVE-2022-21871]] [[CVE-2022-21898]] [[CVE-2022-21918]] [[CVE-2022-21912]] [[CVE-2022-21852]] [[CVE-2022-21902]] [[CVE-2022-21896]] [[CVE-2022-21872]] [[CVE-2022-21878]] [[CVE-2022-21907]] [[CVE-2022-21843]] [[CVE-2022-21890]] [[CVE-2022-21883]] [[CVE-2022-21889]] [[CVE-2022-21848]] [[CVE-2022-21849]] [[CVE-2022-21908]] [[CVE-2022-21920]] [[CVE-2022-21881]] [[CVE-2022-21879]] [[CVE-2022-21913]] [[CVE-2022-21884]] [[CVE-2022-21888]] [[CVE-2022-21867]] [[CVE-2022-21851]] [[CVE-2022-21850]] [[CVE-2022-21893]] [[CVE-2022-21914]] [[CVE-2022-21885]] [[CVE-2022-21964]] [[CVE-2022-21922]] [[CVE-2022-21961]] [[CVE-2022-21959]] [[CVE-2022-21958]] [[CVE-2022-21960]] [[CVE-2022-21963]] [[CVE-2022-21892]] [[CVE-2022-21962]] [[CVE-2022-21928]] [[CVE-2022-21894]] [[CVE-2022-21863]] [[CVE-2022-21875]] [[CVE-2022-21877]] [[CVE-2022-21866]] [[CVE-2022-21861]] [[CVE-2022-21873]] [[CVE-2022-21899]] [[CVE-2022-21864]] [[CVE-2022-21895]] [[CVE-2022-21834]] [[CVE-2022-21833]] [[CVE-2022-21882]] [[CVE-2022-21876]] [[CVE-2022-21887]] [[CVE-2022-21924]]

