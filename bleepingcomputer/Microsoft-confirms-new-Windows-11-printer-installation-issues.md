# Microsoft confirms new Windows 11 printer installation issues
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-new-windows-11-printer-installation-issues/)
+ Date: October 14, 2021
+ Author: Sergiu Gatlan


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/10/05/Windows11_laptop.jpg)


Microsoft has confirmed new Windows 11 known issues which cause printers installation fails on systems commonly found in enterprise environments.


As Redmond explains, printer installation might fail when attempted over the network on devices that access printers via print server [using HTTP connections](https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2#1719msgdesc).


Installing printers [might also not complete successfully](https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2#1722msgdesc) via the Internet Printing Protocol (IPP) in organizations sharing an IPP printer using printer connections.


Given that this known issue impacts only the automatic download and installation processes, Microsoft says that administrators can still install printer drivers on the client by copying packaged drivers from a known good package location as a workaround.


The issues impact both client and server platforms, including:


* Client: Windows 10, version 21H1; Windows 10, version 20H2; Windows 10, version 2004; Windows 10, version 1909; Windows 10, version 1809; Windows 10, version 1607; Windows 10 Enterprise 2015 LTSB; Windows 8.1; Windows 7 SP1; Windows 11, version 21H2
* Server: Windows Server 2022; Windows Server, version 20H2; Windows Server, version 2004; Windows Server, version 1909; Windows Server, version 1809; Windows Server 2016; Windows Server 2012; Windows Server 2008 SP2


The company is investigating both issues and working on a fix for Windows 11 customers that will be released in a future update.


Affected customers running previous Windows versions (including Windows 10 and Windows Server 2022) can fix the issues by installing the [October Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/windows-10-updates-kb5006670-and-kb5006667-released/) cumulative updates.


Microsoft confirmed [a third known issue](https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2#1725msgdesc) leading to custom printing properties not correctly provided to print server clients. Although not causing printing operations to fail, it would only allow printing with default settings.


"This issue results from an improper building of the data file which contains the printer properties. Clients which receive this data file will not be able to use the file content and will instead proceed with default printing settings. Servers which use default print settings and have no custom settings to provide to clients are unaffected," Redmond explained.


Previously acknowledged Windows 11 issues
-----------------------------------------


After [Windows 11 was released worldwide last week](https://www.bleepingcomputer.com/news/microsoft/windows-11-is-released-what-you-need-to-know-and-new-features/), Microsoft has also acknowledged other known issues impacting the new Windows version, including:


* [Windows 11 compatibility issue apps creating registry keys using some non-ASCII characters](https://www.bleepingcomputer.com/news/microsoft/windows-11-incompatible-with-apps-using-non-ascii-registry-keys/)
* [Windows 11 compatibility issue with Oracle VirtualBox](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-11-issues-with-virtualbox-intel-killer/)
* [Slower Internet speeds with Intel 'Killer' and Dell 'SmartByte' apps](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-11-issues-with-virtualbox-intel-killer/) (now [fixed](https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5006674-update-released-with-compatibility-fixes/))
* The Windows 10 taskbar not upgraded to the new one designed for Windows 11
* The Windows 11 Start Menu does not open
* Up to 15% performance hit on AMD CPUs
* Incorrect "This PC can’t run Windows 11" error
* Windows 11 File Explorer is using too much memory




#### Tags:
[[Windows]] [[Microsoft]] [[Server,]] [[Bleeping Computer]]
