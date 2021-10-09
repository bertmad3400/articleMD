# Windows 11: Microsoft is investigating these eight problems
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-11-microsoft-is-investigating-these-eight-problems/)
+ Date: October 9, 2021
+ Author: Lawrence Abrams


## Article:
![WIndows 11 bugs](https://www.bleepstatic.com/content/hl-images/2021/09/01/windows-11-glow-glass.jpg)


Windows 11 is officially released, and users are running into various issues and problems preventing them from upgrading or using the new operating system correctly. Below we have collected eight known issues affecting Windows 11 and when they are expected to be fixed.


As with any major feature update or new version of Windows, there are bound to be incompatibilities with software and hardware that cause crashes or other instability.


To protect against these poor upgrade experiences, Microsoft will place safeguard holds on devices with known incompatibilities that prevent users from upgrading to Windows 11.


Below we have listed the known safeguard holds, common problems, and known issues that users are running into with Windows 11.


Windows 11 uses the Windows 10 taskbar
--------------------------------------


After upgrading to Windows 11, some users report that they [still have the Windows 10 taskbar](https://www.bleepingcomputer.com/news/microsoft/windows-11-bug-reverts-users-back-to-the-windows-10-tas) rather than the revamped one designed for the new operating system.



![Windows 10 taskbar in Windows 11](https://www.bleepstatic.com/images/news/Microsoft/windows-11/w/windows-10-taskbar-bug/windows-11-windows-10-hybrid.jpg)**Windows 10 taskbar in Windows 11**
For some people, this is disappointing as they prefer the new updated, while others are happy as the new Windows 11 taskbar is missing some features from the Windows 10 taskbar.


These missing features are the ability to move the taskbar to the top and sides of the screen, the right-click context menu has been removed, and you can no longer ungroup program windows.


While Microsoft has not publicly acknowledged this bug, they are looking into it.


For now, users have provided various methods that you can use to try and restore the Windows 11 taskbar.


**Method 1:**Remove the latest Windows 11 Update, reboot, and install all available updates again. As Windows 11 is brand new, most people will not have any updates installed and can skip to the next method.


**Method 2:** Open PowerShell prompt as an Administrator and run the following command:


This PowerShell command was used to resolve Start Menu problems in Windows 10 and should apply to Windows 11.


**Method 3:**As a last resort, you can create a new user profile, and the Windows 11 taskbar should be restored. However, this method will require you to copy all your data and possibly reinstall apps in the new profile.


The Windows 11 Start Menu does not open
---------------------------------------


People are reporting that the Start Menu no longer works after upgrading to Windows 11. When they attempt to use it, it simply won't open or will freeze.


Like the taskbar issue above, Microsoft has not publicly acknowledged this bug or provided a fix, but are looking into it.


Windows 11 users have been able to fix it using one of the same methods above.


Up to 15% performance hit on AMD CPUs
-------------------------------------


AMD has announced that users can [experience up to a 5% CPU performance hit](https://www.bleepingcomputer.com/news/microsoft/amd-warns-of-up-to-15-percent-windows-11-performance-decrease/) when using certain applications, with some games seeing as high as a 15% hit.


These performance issues are caused by increased L3 cache latency and Windows 11 not preferentially scheduling threat on the processor's fasted core.


You can find more detailed information on the performance issues in the table below.


AMD has said they are working on a fix with Microsoft and hope to have it available this month.


Incorrect "This PC can’t run Windows 11" error
----------------------------------------------


Some users see a message stating, "This PC doesn't currently meet all the system requirements for Windows 11" on the Windows Update page even if their hardware is compatible.


What's frustrating is that when the users run PC Health Check, they are told that their hardware is compatible and would work fine with Windows 11.


Ultimately, there is no current way to bypass this error without using a [Windows 11 hardware requirements bypass script](https://www.bleepingcomputer.com/news/microsoft/new-windows-11-install-script-bypasses-tpm-system-requirements/) designed to allow incompatible hardware to install the new operating system.



![This PC doesn’t currently meet all the system requirements message](https://www.bleepstatic.com/images/news/Microsoft/windows-11/k/known-issues-release/incorrect-not-compatible-errors.jpg)**This PC doesn’t currently meet all the system requirements message**  
*Source: WindowsLatest*
WindowsLatest said they [spoke to Microsoft](http://www.windowslatest.com/2021/10/07/microsoft-confirms-false-this-pc-cant-run-windows-11-error/), who confirmed they were aware of the issue and working on a fix.


“We are aware of the issue, and we’re currently working for a fix,” a Microsoft’s support agent told WindowsLatest.


Windows 11 File Explorer is using too much memory
-------------------------------------------------


Since the release of Windows 11 preview builds, File Explorer has been experiencing a memory leak causing the application to use too much system memory.


For some people, the leak has caused file explorer to [use 1GB of memory](https://www.reddit.com/r/Windows11/comments/ov3y55/windows_explorer_memory_leak_important_please/) after opening a couple of folders. What makes matters worse is that when File Explorer is closed, the memory is not released and remains unusable by the system until Windows 11 is restarted.


Microsoft has fixed the memory leak issues in the Windows 11 builds 22454 preview builds in the Insider 'Dev' channel, but it is unknown when the fix will make it into the release channel.


"We've included changes with Build 22454 to mitigate a couple of issues that were causing leaks when using File Explorer," Microsoft shared in a Feedback Hub report about the memory leak.


Windows 11 compatibility issue with Oracle VirtualBox
-----------------------------------------------------


If Oracle VirtualBox is installed on a Windows 11 device that has Hyper-V enabled, a compatibility issue may cause virtual machines (VMs) not to start.


"Microsoft and Oracle have found a compatibility issue between VirtualBox and Windows 11, when Hyper-V or Windows Hypervisor is installed. You might be unable to start Virtual machines (VMs) and you might receive an error," Microsoft said in a list of known Windows 11 issues.


To prevent these issues, Microsoft has placed a compatibility hold that will not let users upgrade to Windows 11 unless Hyper-V, Windows Hypervisor, or VirtualBox is uninstalled from the device.


Oracle is working on a solution to this issue and hopes to have a new compatible version available this month. However, those who attempt to install Windows 11 before this fix is available may see the following error:



> 
> "VirtualBox. Your PC requires the latest version of this app. Click Learn More for more information on how to update this app.”
> 
> 
> 


Microsoft also advises users not to perform a forced upgrade via bootable media or the Installation Assistant to bypass this compatibility hold.


Data loss with Intel 'Killer' and Dell 'SmartByte' apps
-------------------------------------------------------


Microsoft has discovered [compatibility issues with the Intel "Killer"](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-11-issues-with-virtualbox-intel-killer/) and Dell "SmartByte" network optimization applications.


Both Intel Killer and Dell SmartByte are applications that claim to optimize and speed up the Internet by prioritizing network connections based upon the type of activity.


Microsoft has discovered that these applications have compatibility issues with Windows 11 that cause User Datagram Protocol (UDP) packets to be dropped when communicating with remote devices.


"Compatibility issues have been found between some Intel “Killer” and “SmartByte” networking software and Windows 11. Devices with the affected software might drop User Datagram Protocol (UDP) packets under certain conditions," explains Microsoft in a list of known issues affecting Windows 11.


"This creates performance and other problems for protocols based on UDP. For example, some websites might load slower than others in affected devices, with videos streaming slower in certain resolutions. VPN solutions based on UDP might also be slower."


Microsoft states that they are working on a fix and plan on releasing it as part of next week's Patch Tuesday on October 12th.


Cốc Cốc browser issues
----------------------


Microsoft has discovered a compatibility issue with the Cốc Cốc browser that prevents the browser from opening and may cause other problems and errors.


To protect against upgrade issues, Microsoft has placed a safeguard hold that prevents users with this browser from upgrading to Windows 11.


Microsoft states that they are investigating the issues and will provide further information when it becomes available.




#### Tags:
[[Windows]] [[Microsoft]] [[taskbar]] [[VirtualBox]] [[Cốc]] [[AMD]] [["This]] [[Bleeping Computer]]
