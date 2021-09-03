# Microsoft breaks Windows 11 Start Menu, Taskbar with Teams promo
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-breaks-windows-11-start-menu-taskbar-with-teams-promo/)
+ Date: September 3, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft breaks Windows 11 Start Menu, Taskbar with Teams promo](https://www.bleepstatic.com/content/hl-images/2021/09/01/Windows_11_headpic.jpg)


Microsoft accidentally broke the Start menu and taskbar on systems of Windows Insiders after pushing a Teams promo to the desktops of users running Windows 11 preview builds.


While the company didn't explain the reason behind Dev and Beta Channel Insiders experiencing Start menu and taskbar unresponsive and having issues accessing other OS areas, including Settings, developer [Daniel Aleksandersen discovered](https://www.ctrl.blog/entry/windows11-empty-taskbar.html) that a buggy promo deployment caused the problem.


"The problem wasn’t caused by an update delivered through Windows Update," Aleksandersen explained."Instead, it was caused by a small file [..] [that] contained an advertisement for Microsoft Teams."


"The promo intended to promote the upcoming operating system’s integration with Microsoft Teams Instead, it caused Explorer (the Windows desktop shell) to stop responding and left users without a working Start menu and taskbar."



![Windows 11 Teams promo](https://www.bleepstatic.com/images/news/u/1109292/2021/windows11-connect-with-teams-panel.png)*Windows 11 Teams promo (Daniel Aleksandersen)*
Windows Insiders impacted by this issue reported that they couldn't use their computers because Explorer and the Taskbar are gone, and the Windows desktop shell is not accessible even after reinstalling the system.


After being flooded with reports, Microsoft [acknowledged the issue](https://twitter.com/windowsinsider/status/1433615378362503177) and pinned it on a "server-side deployment" problem.


"Recently, Windows Insiders in both the Dev and Beta Channels began reporting that Start and Taskbar were unresponsive and Settings and other areas of the OS wouldn’t load," [Microsoft said](https://blogs.windows.com/windows-insider/2021/09/02/announcing-windows-11-insider-preview-build-22000-176/).


"We quickly discovered an issue with a server-side deployment that went out to Insiders and canceled that deployment."


Windows Insiders whose computers' were impacted by the buggy Teams promo need to go through the following steps to get their PCs back into a working state:


* **Step 1:** Use CTRL-ALT-DEL and choose to open Task Manager.
* **Step 2**: Choose “More details” at the bottom of Task Manager to expand Task Manager.
* **Step 3**: Go to “File” and choose “Run new task.”
* **Step 4:** Type “cmd” in the “Open” field.
* **Step 5:** Paste the following (everything in bold):  
**reg delete HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\IrisService /f && shutdown -r -t 0**
* **Step 6**: Hit enter, and then your PC should reboot. After rebooting, everything should be back to normal.


*Update:* When asked for more details about this issue, a Microsoft spokesperson told BleepingComputer that "Microsoft has nothing to share on this topic besides the update published in this Windows Insider Blog: [Announcing Windows 11 Insider Preview Build 22449 | Windows Insider Blog](https://blogs.windows.com/windows-insider/2021/09/02/announcing-windows-11-insider-preview-build-22449/) and [tweet](https://twitter.com/windowsinsider/status/1433615378362503177?s=20) from the Windows Insider Twitter."




#### Tags:
[[Windows]] [[Microsoft]] [[Teams]] [[Bleeping Computer]]
