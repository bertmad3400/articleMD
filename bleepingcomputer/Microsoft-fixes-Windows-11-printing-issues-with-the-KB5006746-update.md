# Microsoft fixes Windows 11 printing issues with the KB5006746 update
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-11-printing-issues-with-the-kb5006746-update/)
+ Date: October 22, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft fixes Windows 11 printing issues with the KB5006746 update](https://www.bleepstatic.com/content/hl-images/2021/06/30/windows-11-square-header.jpg)


Microsoft has fixed multiple known issues impacting printing on Windows 11 with the release of the optional KB5006746 cumulative update preview on Thursday.


This update was released for customers who want to test fixes and performance improvements coming on November 9th, as part of next month's Patch Tuesday.


To install [KB5006746](https://support.microsoft.com/en-us/topic/october-21-2021-kb5006746-os-build-22000-282-preview-03190705-0960-4ba4-9ee8-af40bef057d3), you have to go to **Settings** > **Windows Update**and click the 'Check for updates' button. Since this is an optional update, Windows will only install it after you click on the 'Download now' button.


Windows 11 users can also manually download and deploy the cumulative update preview from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5006746).



![KB5006746 in Windows Update](https://www.bleepstatic.com/images/news/u/1109292/2021/KB5006746_optional_CU.png)*KB5006746 in Windows Update (BleepingComputer)*
Multiple printing issues fixed
------------------------------


Microsoft confirmed that KB5006746 fixes Windows 11 known issues [causing printer installation fails](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-new-windows-11-printer-installation-issues/) and [prompts for admin credentials before every attempt to print](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-11-bug-may-only-allow-admins-to-print/) on systems commonly found in enterprise environments.


On systems where KB5006746 is not yet deployed, printing install attempts may not complete over the network on devices that access printers via print server using HTTP connections.


Installing printers on Windows devices not yet updated could also fail via the Internet Printing Protocol (IPP) in orgs sharing an IPP printer using printer connections.


Redmond also addressed a third known issue leading to custom printing properties not correctly provided to print server clients. Even though not causing printing operations to fail, it would only allow customers to print with default settings.


Impacted customers running earlier Windows versions (including Windows 10) can fix these printing issues by installing the [September Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5005565-and-kb5005566-cumulative-updates-released/) and [October Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/windows-10-updates-kb5006670-and-kb5006667-released/) cumulative updates.


Also addresses gaming performance issues
----------------------------------------


Since Windows 11 was released in early October, customers have also complained of [noticeable performance issues impacting systems with AMD Ryzen CPUs](https://www.bleepingcomputer.com/news/microsoft/amd-warns-of-up-to-15-percent-windows-11-performance-decrease/).


AMD explained in a [support article](http://web.archive.org/web/20211006195809/https://www.amd.com/en/support/kb/faq/pa-400) that the performance hit was caused by "L3 cache latency may increase for some applications" and "UEFI CPPC2 ("preferred core") may not preferentially schedule threads on a processor's fastest core."


Microsoft fixed the AMD performance problems in the KB5006746 optional update, saying that it "addresses an L3 caching issue that might affect performance in some applications on devices that have AMD Ryzen processors after upgrading to Windows 11 (original release)."


With this update, Microsoft has also fixed another issue causing Bluetooth mice and keyboards to be slower than expected, adversely affecting shooters and eSports games.


Last but not least, Microsoft fixed an issue that prevented Windows 11 users from using the Xbox Game Bar recording features.


The complete list of known issues acknowledged and fixed by Microsoft since Windows 11 was released includes:


* [Up to 15% performance hit on AMD CPUs](https://www.bleepingcomputer.com/news/microsoft/amd-warns-of-up-to-15-percent-windows-11-performance-decrease/) (fixed)
* [Compatibility issue apps creating registry keys using some non-ASCII characters](https://www.bleepingcomputer.com/news/microsoft/windows-11-incompatible-with-apps-using-non-ascii-registry-keys/) (fixed)
* [Compatibility issue with Oracle VirtualBox](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-11-issues-with-virtualbox-intel-killer/) (fixed)
* [Printer installation issues](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-new-windows-11-printer-installation-issues/) (fixed)
* [Custom printing properties not correctly provided to print clients](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-new-windows-11-printer-installation-issues/) (fixed)
* [Slower Internet speeds with Intel 'Killer' and Dell 'SmartByte' apps](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-11-issues-with-virtualbox-intel-killer/) (fixed)
* [Smartcard authentication fails when trying to connect using Remote](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-10-auth-issue-impacting-remote-desktop/) Desktop (fixed)
* The Windows 10 taskbar not upgraded to the new one designed for Windows 11
* The Windows 11 Start Menu does not open
* Incorrect "This PC can’t run Windows 11" error
* Windows 11 File Explorer is using too much memory




#### Tags:
[[Windows]] [[Microsoft]] [[(fixed)]] [[KB5006746]] [[AMD]] [[update,]] [[Bleeping Computer]]
