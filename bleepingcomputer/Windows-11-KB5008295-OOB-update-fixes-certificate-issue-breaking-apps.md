# Windows 11 KB5008295 OOB update fixes certificate issue breaking apps
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5008295-oob-update-fixes-certificate-issue-breaking-apps/)
+ Date: November 5, 2021
+ Author: Sergiu Gatlan


## Article:
![Windows 11 KB5008295 OOB update fixes certificate issue breaking apps](https://www.bleepstatic.com/content/hl-images/2021/10/21/windows-11-gradient-header.jpg)


Microsoft has released the KB5008295 out-of-band update to address Windows 11 issues while opening or using some built-in apps and features due to an expired Microsoft digital certificate.


"Devices directly connected to Windows Update and Windows Update for Business should be offered and automatically install [KB5008295](https://support.microsoft.com/help/5008295) to resolve the issues," Microsoft explained.


"If you would like to install the update before it is installed automatically, you will need to [Check for updates](https://support.microsoft.com/windows/update-windows-3c5ae7fc-9fb6-9af1-1984-b5e0412c556a). The update is available on Windows Update and [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5008295).


"In managed environments, you will need to import the package from Microsoft Update Catalog into your deployment tools."


Microsoft added that you must restart your device after applying this update to fully address the Windows 11 app issues.


The list of affected apps and features on Windows 11, version 21H2 [includes](https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2#2739msgdesc) the Snipping Tool, the Accounts page and landing page in the Settings app (S mode only), the Start menu (S mode only), the Touch Keyboard, Voice Typing, Emoji Panel, the Input Method Editor user interface (IME UI), and the "Getting started" and "Tips" dialogs.




> 
> Microsoft is releasing an Out-of-band (OOB) update (KB5008295) today to completely resolve a set of issues affecting the Snipping Tool, Touch Keyboard, some built-in apps and S Mode on Windows 11. <https://t.co/8XaFZqRH3J>
> 
> 
> — Windows Update (@WindowsUpdate) [November 5, 2021](https://twitter.com/WindowsUpdate/status/1456677227010007046?ref_src=twsrc%5Etfw)


Stream of Windows 11 problems
-----------------------------


Microsoft also said last week that [customers are seeing issues with network printing](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-kb5006674-kb5006670-updates-break-printing/) after deploying the Windows 11 [KB5006674](https://support.microsoft.com/help/5006674) and Windows 10 [KB5006670](https://support.microsoft.com/help/5006670) October Patch Tuesday updates.


Customers attempting to connect to printers shared on Windows print servers may see errors — i.e., 0x000006e4(RPC\_S\_CANNOT\_SUPPORT), 0x0000007c(ERROR\_INVALID\_LEVEL), 0x00000709(ERROR\_INVALID\_PRINTER\_NAME) — which prevent them from printing over the network.


Microsoft is still working on a solution to allow print clients to establish RPC packet privacy connections to Windows print servers via RPC over SMB.


The full list of issues Microsoft has acknowledged or fixed since Windows 11's launch includes:


* [Up to 15% performance hit on AMD CPUs](https://www.bleepingcomputer.com/news/microsoft/amd-warns-of-up-to-15-percent-windows-11-performance-decrease/) (fixed)
* [Compatibility issue apps creating registry keys using some non-ASCII characters](https://www.bleepingcomputer.com/news/microsoft/windows-11-incompatible-with-apps-using-non-ascii-registry-keys/) (fixed)
* [Compatibility issue with Oracle VirtualBox](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-11-issues-with-virtualbox-intel-killer/) (fixed)
* [Printer installation issues](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-new-windows-11-printer-installation-issues/) (fixed)
* [Custom printing properties not correctly provided to print clients](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-new-windows-11-printer-installation-issues/) (fixed)
* [Slower Internet speeds with Intel' Killer' and Dell' SmartByte' apps](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-11-issues-with-virtualbox-intel-killer/) (fixed)
* [Smartcard authentication fails when trying to connect using Remote](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-10-auth-issue-impacting-remote-desktop/)Desktop (fixed)
* [Snipping Tool and some built-in applications might not open or work as expected](https://www.bleepingcomputer.com/news/microsoft/some-windows-11-apps-are-broken-due-to-expired-certificate/) (fixed)
* [Connections to printers shared via print server encounter errors](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-kb5006674-kb5006670-updates-break-printing/)
* The Windows 10 taskbar not upgraded to the new one designed for Windows 11
* The Windows 11 Start Menu does not open
* Incorrect "This PC can't run Windows 11" error
* Windows 11 File Explorer is using too much memory




#### Tags:
[[Windows]] [[Microsoft]] [[(fixed)]] [[apps]] [[built-in]] [[Bleeping Computer]]
