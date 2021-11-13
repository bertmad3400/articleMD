# New Windows 11 build fixes widespread printer issues, system freezes
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/new-windows-11-build-fixes-widespread-printer-issues-system-freezes/)
+ Date: November 13, 2021
+ Author: Sergiu Gatlan


## Article:
![New Windows 11 build fixes widespread printer issues, system freezes](https://www.bleepstatic.com/content/hl-images/2021/10/21/windows-11-gradient-header.jpg)


Microsoft has fixed a long list of issues impacting Windows 11 in a newly released build for Windows Insiders in the Beta and Release Preview Channels.


Among the significant bugs addressed in Windows 11 Build 22000.346 (KB5007262), Redmond has addressed known issues preventing USB Print devices with support for Internet Printing Protocol (IPP) Over USB from completing the installation and leading to some USB Print installers reporting that they don't printer after they were plugged in.


Another printing issue fixed in today's Windows 11 preview build caused 0x000006e4 (RPC\_S\_CANNOT\_SUPPORT), 0x0000007c (ERROR\_INVALID\_LEVEL), and 0x00000709 (ERROR\_INVALID\_PRINTER\_NAME) error codes when connecting to remote printers shared on Windows print servers.


This fix is expected to roll out to all impacted Windows 10 and Windows 11 customers during the December 2021 Patch Tuesday.


The originating update for this known issue is [the mandatory KB5006670 cumulative update](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-kb5006674-kb5006670-updates-break-printing/) released during the [October 2021 Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/microsoft-october-2021-patch-tuesday-fixes-4-zero-days-71-flaws/) with security updates for two Windows Print Spooler vulnerabilities ([CVE-2021-36970](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36970) and [CVE-2021-41332](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41332)).


Since the October Patch Tuesday updates have been released, Windows 10 admins and users have been reporting widespread network printing issues in a [22-page forum topic](https://www.bleepingcomputer.com/forums/t/759880/kb5006670-network-printer-problems-again-this-month/) at BleepingComputer.


Prior to today's update, on Thursday, BleepingComputer also [shared a fix for the 0x0000007c printing error](https://www.bleepingcomputer.com/news/microsoft/how-to-fix-the-windows-0x0000007c-network-printing-error/) allowing users to work around the printing issue.


Microsoft privately distributed the same fix using ADMX installers that added new Windows Registry values, which disabled the problematic changes from October.


Last month, Redmond fixed two other Windows 11 known issues [causing printer installation fails](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-new-windows-11-printer-installation-issues/) and [prompts for admin credentials before every attempt to print](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-11-bug-may-only-allow-admins-to-print/) in enterprise environments.


More fixes for system and app freezes
-------------------------------------


In today's Windows 11 beta build, Microsoft also addressed multiple issues reported by Windows Insiders that would lead to system and application freezes.


The Windows Insider Program Team also removed a mechanism used by some web browsers and apps to intercept microsoft-edge: links before being opened using Microsoft Chromium-based Edge browser.


Last but not least, Microsoft said it improved Defender for Endpoint's ability to detect and block ransomware and advanced attacks, although there are no details on what exactly was enhanced.


The list of freeze fixes in this release includes:


* We fixed an issue that causes devices that have certain processors to stop responding when waking from hibernation.
* We fixed an issue in the Hyper-V virtual machine bus (VMBus) that causes the Windows Subsystem for Linux (WSL) VM to occasionally time out when attaching disks. This issue also prevents the utility from starting.
* We fixed an issue that causes the system to stop working after you enable Hyper-V.
* We fixed an issue that prevents your device from starting up, and it becomes unresponsive because of licensing API calls.
* We fixed an issue that causes certain apps to stop responding to input. This issue occurs on devices that have a touchpad.


You can find the complete list of improvements in Windows 11 Build 22000.346 (KB5007262) [here](https://blogs.windows.com/windows-insider/2021/11/12/releasing-windows-11-build-22000-346-to-beta-and-release-preview-channels/).


Microsoft is rolling out the Windows 11 upgrade to "an expanded set of eligible devices" in a phased rollout to provide users with a smoother upgrade experience. According to Redmond's estimates, Windows 11 will be offered as an upgrade to all eligible Windows 10 devices until the summer of 2022.


"If you are using Windows 10, you can determine if your device is eligible for the upgrade using the [PC Health Check app](https://www.microsoft.com/windows/windows-11#pchealthcheck) or checking [Windows 11 specs, features, and computer requirements](https://www.microsoft.com/windows/windows-11-specifications)," Microsoft explains.




#### Tags:
[[Windows]] [[Microsoft]] [[Redmond]] [[USB]] [[Bleeping Computer]]
