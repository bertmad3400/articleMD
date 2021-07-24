# Windows 10 July security updates break printing on some systems
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-10-july-security-updates-break-printing-on-some-systems/)
+ Date: July 24, 2021
+ Author: Sergiu Gatlan


## Article:
![Windows 10 July security updates break printing on some systems](https://www.bleepstatic.com/content/hl-images/2020/10/13/Windows-10-headpic.jpg)


Microsoft says customers may experience printing and scanning issues on devices using smart card (PIV) authentication after installing July 2021 Windows 10 security updates on a domain controller (DC).


"After installing updates released July 13, 2021 on domain controllers (DCs) in your environment, printers, scanners, and multifunction devices that are not compliant with section 3.2.1 of [RFC 4556 spec](https://www.ietf.org/rfc/rfc4556.txt) might fail to print when using smart card (PIV) authentication," Microsoft [explained](https://docs.microsoft.com/en-us/windows/release-health/status-windows-10-21h1#1663msgdesc).


According to Microsoft, all affected smart card authenticating devices should work as expected when using username and password authentication.


Impacted Windows versions include include:


* Client: Windows 10, version 21H1; Windows 10, version 20H2; Windows 10, version 2004; Windows 10, version 1909; Windows 10, version 1809; Windows 10 Enterprise LTSC 2019; Windows 10 Enterprise LTSC 2016; Windows 10, version 1607; Windows 10 Enterprise 2015 LTSB; Windows 8.1; Windows 7 SP1
* Server: Windows Server, version 20H2; Windows Server, version 2004; Windows Server, version 1909; Windows Server, version 1809; Windows Server 2019; Windows Server 2016; Windows Server 2012 R2; Windows Server 2012; Windows Server 2008 R2 SP1; Windows Server 2008 SP2


Issue caused by security flaw hardenings
----------------------------------------


This known issue is caused by hardening changes for [CVE-2021-33764](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-33764), and it affects smart card authenticating printers, scanners, and multifunction devices which "don't support DH or advertise support for des-ede3-cbc ("triple DES") during the Kerberos AS request."


Windows 10 users who encounter this issue are advised to first check if they have the latest drivers and firmware installed on the non-compliant and misbehaving printing or scanning devices.


If the known issue still appears even though the devices are up-to-date, affected customers should contact the device manufacturer and ask for setting changes or updates to make the printer or scanner compliant with CVE-2021-33764 hardenings deployed via July Windows 10 security updates.


Microsoft is currently working on temporary mitigation that provided with a future update to re-enable printing and scanning on impacted devices.


"This will allow time for device manufacturers to release compliant firmware and drivers for their devices," Microsoft [added](https://support.microsoft.com/en-us/topic/kb5005408-smart-card-authentication-might-cause-print-and-scan-failures-514f0bc5-ecde-4e5e-8c5a-2a776d7fb89a).


"Further, it should allow time to update settings, firmware, and drivers in your environment and make them compliant."


Other printing problems addressed this year
-------------------------------------------


Redmond [addressed Windows 10 printing issues](https://www.bleepingcomputer.com/news/microsoft/windows-10-printing-issues-fixed-by-july-patch-tuesday-update/) caused by changes introduced in the June 2021 cumulative update preview earlier this month.


Users also [encountered printing issues](https://www.bleepingcomputer.com/news/microsoft/windows-10-crashes-when-printing-due-to-microsoft-march-updates/) in March after installing the March 2021 Patch Tuesday updates, reporting that Windows 10 would [crash when printing](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-10-crash-issue-due-to-march-updates/) or [print jobs would be missing graphics elements](https://www.bleepingcomputer.com/news/microsoft/microsoft-warns-of-more-printing-issues-caused-by-march-updates/), blank pages, or other issues.


To resolve these issues, Microsoft released two out-of-band emergency updates for Windows 10 one week later: [KB5001567](https://www.bleepingcomputer.com/news/microsoft/windows-10-emergency-updates-released-to-fix-printing-crashes/) on March 15 to fix blue screen crashes when printing and [KB5001649](https://www.bleepingcomputer.com/news/microsoft/new-windows-10-emergency-updates-fix-remaining-printing-issues/) on March 18 to fix the printing issues.


One day later, the company released [yet another emergency update](https://www.bleepingcomputer.com/news/microsoft/microsoft-warns-of-more-printing-issues-caused-by-march-updates/) to fix additional printing issues besides blue screen crashes, including blank pages, document elements missing or printed as block boxes, and alignment or formatting issues.




#### Tags:
[[Windows]] [[Microsoft]] [[Bleeping Computer]]
