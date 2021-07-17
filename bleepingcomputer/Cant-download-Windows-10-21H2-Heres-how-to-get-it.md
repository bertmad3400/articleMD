# Can't download Windows 10 21H2? Here's how to get it
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/cant-download-windows-10-21h2-heres-how-to-get-it/)
+ Date: July 17, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 10](https://www.bleepstatic.com/content/hl-images/2021/04/17/windows-10-sapphire.jpg)


Microsoft released the first preview build of Windows 10 21H2 this week, but it is not being offered to everyone at this time. However, for those who want to test the new build, a way has been discovered that allows anyone to upgrade to the new feature update now.


On Thursday, Microsoft released the first Windows 10 21H2 preview build. While it is not a very large release, it does have a few [new security features](https://www.bleepingcomputer.com/news/microsoft/windows-10-21h2-preview-released-with-new-security-features/) that better protect your account and Wifi connection.


However, unlike other releases of new feature updates preview builds, Microsoft is only making it available via Windows Update to Insiders who were moved to the 'Release' channel for not meeting Windows 11's hardware requirements.


This means that Windows Insiders can't just switch to the Release channel and be offered the new Windows 10 21H2 update as we could in the past.


The good news is that Windows sleuth Albacore has shared a method that allows users running Windows 10 2004, Windows 10 20H2, and Windows 10 21H1 to upgrade their device to Windows 10 21H2 quickly.


Manually installing the enablement package
------------------------------------------


The Windows 10 21H2 feature update is being rolled out to Insiders as an enablement package for Windows 10 2004, Windows 10 20H2, and Windows 10 21H1, allowing these versions to update quickly with a single reboot.


This enablement package acts as a "master switch" that enables the dormant features already present in Windows 10 2004/20H2/21H1 and upgrades the Windows version and build number.


For Windows Insiders not being offered the Windows 10 21H2 package, it is possible to upgrade to the new feature update by downloading the appropriate enablement package and manually installing it.


To manually upgrade your Windows 10 Insider device to Windows 10 21H2, please follow these steps:


1. Switch to the 'Release' channel in your Windows Insider settings.
2. Download the appropriate enablement package for your version of Windows to the Downloads folder. It will be the 64-bit version for most people, but you can confirm if you are 32-bit, 64-bit, or running ARM using [these instructions](https://www.bleepingcomputer.com/tutorials/32-bit-or-64-bit-windows/).  
  

Albacore has [shared](https://twitter.com/thebookisclosed/status/1415785915990036488) [Windows 10 21H2 enablement packages](https://drive.google.com/drive/folders/12DQyJj1BVb8GCmWJwMYKkRgoxinCP3mc) for 64-bit systems (Windows10.0-KB5003791-x64.cab), 32-bit systems (Windows10.0-KB5003791-x86.cab), and ARM systems (Windows10.0-KB5003791-arm64.cab).
3. Open a [Windows 10 Elevated Command Prompt](https://www.bleepingcomputer.com/tutorials/how-to-open-a-windows-10-elevated-command-prompt/) and type `cd %userprofile%\downloads` and press **enter**on your keyboard. You will now be in your Downloads folder.
4. Now type `DISM /online /add-package /packagepath:[name of file you downloaded]` and press **enter** on your keyboard. For example, 64-bit users would enter `DISM /online /add-package /packagepath:Windows10.0-KB5003791-x64.cab`.

![Installing the enablement package with DISM](https://www.bleepstatic.com/images/news/Microsoft/Windows-10/feature-updates/windows-10-21h2/dism-command.jpg)**Installing the enablement package with DISM**
The command will now install the enablement package on your computer, and when finished, prompt you to restart your computer.
5. After rebooting your computer, you can click on the **Start** button, and type `winver`, and press **enter**to see your new version of Windows 10, which should now say Version 21H2 Build 19044.1147, as shown below.

![Upgraded to Windows 10 Version 21H2 Build 19044.1147](https://www.bleepstatic.com/images/news/Microsoft/Windows-10/feature-updates/windows-10-21h2/windows-10-21h2.jpg)**Upgraded to Windows 10 Version 21H2 Build 19044.1147**
6. You can now close the About Windows dialog and the command prompt.


Now that you are upgraded to Windows 10 21H2, you will continue to receive new updates for the operating system as they become available.




#### Tags:
[[Windows]] [[21H2]] [[64-bit]] [[Windows10]] [[Microsoft]] [[2004]] [[20H2]] [[21H1]] [[DISM]] [[Bleeping Computer]]
