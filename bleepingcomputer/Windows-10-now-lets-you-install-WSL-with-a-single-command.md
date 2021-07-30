# Windows 10 now lets you install WSL with a single command
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-10-now-lets-you-install-wsl-with-a-single-command/)
+ Date: July 30, 2021
+ Author: Sergiu Gatlan


## Article:
![Windows 10 now lets you install WSL with a single command](https://www.bleepstatic.com/content/hl-images/2020/09/30/wsl-space-header.jpg)


Microsoft says the Windows Subsystem for Linux (WSL) can now be installed on Windows 10, version 2004 or later using a single terminal command.


"In the latest Windows Insider Preview builds, you can install everything you need to run WSL just by running wsl.exe --install," Windows Developer Platform Program Manager Craig Loewen [said](https://devblogs.microsoft.com/commandline/install-wsl-with-a-single-command-now-available-in-windows-10-version-2004-and-higher/).


"We’re excited to announce that this functionality is now officially backported to Windows 10 version 2004 and higher, which will make installing WSL on those builds much easier!"


To get access to this new feature, you have to update your computer to Windows 10 2004 or later via Windows Update or install the [KB5004296 preview cumulative update](https://www.bleepingcomputer.com/news/microsoft/windows-10-gaming-issues-fixed-in-kb5004296-how-to-download/), which also comes with fixes for fixes Windows 10 gaming issues.


How to install and use WSL
--------------------------


While previously you had to jump through several hoops such as installing multiple packages and toggling on several OS settings, now you only have to open a Command Prompt window as administrator and run the `wsl.exe --install` command.


This automatically enables WSL and installs Ubuntu as the default distro and the latest WSL Linux kernel version on the device.


After the installation process is completed and the computer is rebooted, the newly deployed Ubuntu distribution will automatically start logging in.


Once WSL is installed, you can use `wsl --update` to update the Linux kernel and `wsl --update rollback` to switch to a previous kernel version.


You can also use `wsl --status` to get an overview of your WSL configuration, including the default distro type, default distro, and the currently installed Linux kernel version.


A short WSL history
-------------------


WSL was [released in 2018](https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-tool-for-running-any-linux-os-on-windows-10/) and it is designed as a compatibility layer that makes it possible for Windows 10 users to run Linux binaries in ELF format natively on their computers, in a PowerShell or Windows 10 command prompt.


Since the initial release, Microsoft has also launched [WSL 2](https://docs.microsoft.com/en-us/windows/wsl/compare-versions), which increases file system performance, supports full system call compatibility, and uses virtualization tech to run a full Linux kernel inside a lightweight virtual machine (VM).


Even though users have been asking Microsoft to also add support for the Wayland protocol in WSL to allow GUI Linux apps to work on Windows [since at least 2016](https://github.com/microsoft/WSL/issues/938), the company only announced that it would introduce Linux GUI support last year at [BUILD 2020](https://devblogs.microsoft.com/commandline/the-windows-subsystem-for-linux-build-2020-summary/).


The new feature, dubbed [WSLg](https://github.com/microsoft/wslg) (short for Windows Subsystem for Linux GUI), was released in April and began rolling out to all Insiders in May with the rollout of Windows 10 Insider Preview Build 21364 to the Dev Channel.


As previously described, WSLg allows you to use Linux GUI applications in Windows as you would use them on a Linux desktop.


Microsoft provides [step-by-step guidance](https://github.com/microsoft/wslg#install-and-run-gui-apps) on how to install and launch Linux GUI apps on your PC. Once installed, these Linux apps can be launched from the Start menu or a Command Prompt window.




#### Tags:
[[Windows]] [[Linux]] [[WSL]] [[Microsoft]] [[GUI]] [[wsl]] [[apps]] [[Bleeping Computer]]
