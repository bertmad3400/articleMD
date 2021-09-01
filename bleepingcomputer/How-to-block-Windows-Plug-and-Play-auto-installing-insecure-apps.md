# How to block Windows Plug-and-Play auto-installing insecure apps
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/how-to-block-windows-plug-and-play-auto-installing-insecure-apps/)
+ Date: September 1, 2021
+ Author: Lawrence Abrams


## Article:
![Comptuer device connectors](https://www.bleepstatic.com/content/hl-images/2021/09/01/usb-plug-and-play.jpg)


A trick has been discovered that prevents your device from being taken over by vulnerable Windows applications when devices are plugged into your computer.


Last month, researchers detailed how simply plugging in a device in Windows may also install a vendor's application that allows regular users to quickly gain SYSTEM privileges, the highest user privilege level in Windows.


For example, when users [plugged in a Razer USB mouse](https://www.bleepingcomputer.com/news/security/razer-bug-lets-you-become-a-windows-10-admin-by-plugging-in-a-mouse/), Windows would automatically install its driver and the Razer Synapse software.


However, since Windows started the software's installation using a process with SYSTEM privileges, the Razer Synapse software also ran with SYSTEM privileges.



![RazerInstaller.exe running with SYSTEM privileges](https://www.bleepstatic.com/images/news/security/vulnerabilities/r/razer/razer-lpe-driver/razer-process-properties.jpg)**RazerInstaller.exe running with SYSTEM privileges**
During the Razer Synapse installation, you could specify a different folder to install the program, which would open a 'Choose a Folder' dialog.


However, when this dialog is open, it is possible to open a PowerShell console, which would also open with the SYSTEM privileges of the Razer Synapse installer.


For those not familiar with SYSTEM privileges, they are the highest user rights available in Windows and allow you to perform any command in the operating system. 


Using these bugs, users with little privileges on a Windows device could easily take complete control over it by simply plugging in a $20 USB mouse.


This vulnerability was discovered in apps known as "co-installers" and, since the first one was spotted, other researchers [found more devices](https://twitter.com/_MG_/status/1431426497286328325) that may allow local privilege elevation, including [SteelSeries devices](https://www.bleepingcomputer.com/news/security/steelseries-bug-gives-windows-10-admin-rights-by-plugging-in-a-device/).


Blocking Windows driver co-installer applications
-------------------------------------------------


When hardware developers submit drivers to Microsoft for distribution through Windows, they can configure device-specific [co-installers](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/co-installer-functionality) that will be executed after Windows Plug-and-Play installs the driver.


These co-installers can be used to configure device-specific Registry keys, download and install other applications, or perform other necessary functions for the device to work correctly.


Through the co-installer feature, Razer, Synapse, and other hardware manufacturers can install their configuration utilities when their USB devices are plugged into a computer.


As [first discovered](https://twitter.com/wdormann/status/1432703702079508480?s=12) by [Will Dormann](https://twitter.com/wdormann), a vulnerability analyst for CERT/CC, it is possible to configure a Windows Registry value that blocks co-installers from being installed during the Plug-and-Play feature.


To do this, open the Registry Editor and navigate to the **HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Device Installer** Registry key. Under that key, add a DWORD-32 value named **DisableCoInstallers** and set it to **1**, as shown below.



![The DisableCoInstallers Registry value](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/c/coinstallers/block-coinstallers/disable-coinstallers-registry.jpg)**The DisableCoInstallers Registry value**

Windows Registry Editor Version 5.00


[HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Device Installer]  

"DisableCoInstallers"=dword:00000001



Once enabled, Windows will block co-installers from being installed when you plug an associated USB device into your computer.


It is important to note that making this change will block a device's configuration software from automatically being installed. Instead, you will need to download and install it from the vendor's site manually.


However, the inconvenience is worth the added security received by blocking the installation of potentially exploitable applications during the Windows Plug-and-Play process.




#### Tags:
[[Windows]] [[USB]] [[co-installers]] [[computer.]] [[privileges,]] [[However,]] [[Plug-and-Play]] [[Bleeping Computer]]
