# Microsoft: Windows 11 bug may only allow admins to print
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-11-bug-may-only-allow-admins-to-print/)
+ Date: October 18, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft: Windows 11 bug may only allow admins to print](https://www.bleepstatic.com/content/hl-images/2021/09/01/Windows_11_headpic.jpg)


Microsoft is working on a fix for a known issue impacting Windows 11 customers and causing a prompt for admin credentials before every attempt to print.


According to Microsoft, this problem impacts Windows environments where the print clients and print servers are in different time zones.


"You might receive a prompt for administrative credentials every time you attempt to print in environments in which the print server and print client are in different times zones," the company [explains](https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2#1728msgdesc).


Affected platforms include both client and server Windows versions:


* Client: Windows 11, version 21H2; Windows 10, version 21H1; Windows 10, version 20H2; Windows 10, version 2004; Windows 10, version 1909; Windows 10, version 1809; Windows 10 Enterprise LTSC 2019; Windows 10 Enterprise LTSC 2016; Windows 10, version 1607; Windows 10 Enterprise 2015 LTSB; Windows 8.1; Windows 7 SP1
* Server: Windows Server 2022; Windows Server, version 20H2; Windows Server, version 2004; Windows Server, version 1909; Windows Server, version 1809; Windows Server 2019; Windows Server 2016; Windows Server 2012 R2; Windows Server 2012; Windows Server 2008 R2 SP1; Windows Server 2008 SP2


While Redmond has already fixed the problem for previously released Windows versions in September and October updates, a solution to address this issue is unavailable for Windows 11 customers for the moment.


Affected customers running previous Windows versions (including Windows 10) can fix the issues by installing the [September Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5005565-and-kb5005566-cumulative-updates-released/) and [October Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/windows-10-updates-kb5006670-and-kb5006667-released/) cumulative updates.


Microsoft says an update that will fix this on Windows 11 is likely to be released in late October.


Luckily, the known issue should not impact home users since affected systems are more commonly found in enterprise environments.


Other Windows 11 printing issues
--------------------------------


Microsoft also [confirmed other Windows 11 known issues](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-new-windows-11-printer-installation-issues/) which caused printers installation to fail on systems in enterprise environments last week.


As Redmond explained, printer installation processes may fail when attempted over the network on devices that access printers via print servers [using HTTP connections](https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2#1719msgdesc).


Installing printers [might also not complete successfully](https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2#1722msgdesc) via the Internet Printing Protocol (IPP) in organizations sharing IPP printers using printer connections.


Last week, Microsoft confirmed a third known issue leading to custom printing properties not being correctly provided to print clients.


Even though not causing printing operations to fail, customers using impacted devices would only print with default settings.


The complete list of acknowledged known issues impacting Windows 11 includes:


* [Compatibility issue apps creating registry keys using some non-ASCII characters](https://www.bleepingcomputer.com/news/microsoft/windows-11-incompatible-with-apps-using-non-ascii-registry-keys/)
* [Compatibility issue with Oracle VirtualBox](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-11-issues-with-virtualbox-intel-killer/)
* [Printer installation issues](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-new-windows-11-printer-installation-issues/)
* [Custom printing properties not correctly provided to print clients](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-new-windows-11-printer-installation-issues/)
* [Slower Internet speeds with Intel 'Killer' and Dell 'SmartByte' apps](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-11-issues-with-virtualbox-intel-killer/) (now [fixed](https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5006674-update-released-with-compatibility-fixes/))
* The Windows 10 taskbar not upgraded to the new one designed for Windows 11
* The Windows 11 Start Menu does not open
* Up to 15% performance hit on AMD CPUs
* Incorrect "This PC can’t run Windows 11" error
* Windows 11 File Explorer is using too much memory




#### Tags:
[[Windows]] [[Microsoft]] [[Server,]] [[Bleeping Computer]]
