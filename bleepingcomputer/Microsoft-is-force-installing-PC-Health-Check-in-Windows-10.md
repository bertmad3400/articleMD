# Microsoft is force installing PC Health Check in Windows 10
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-is-force-installing-pc-health-check-in-windows-10/)
+ Date: October 26, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 10](https://www.bleepstatic.com/content/hl-images/2020/10/13/Windows-10-headpic.jpg)


Microsoft has begun force installing the PC Health Check application on Windows 10 devices using a new KB5005463 update.


PC Health Check is a new diagnostics tool created by Microsoft and released in conjunction with Windows 11 that provides various troubleshooting and maintenance features.


However, its primary use has been to analyze a device's hardware to check if it's compatible with Windows 11.



![PC Health Check application](https://www.bleepstatic.com/images/news/Microsoft/Windows-10/update/KB5005463-pc-health-check/pc-health-check-app.jpg)**PC Health Check application**
This Friday, Microsoft began rolling out the new KB5005463 update to force-install the PC Health Check application on Windows 10 devices.



![Windows 10 KB5005463 update automatically installing](https://www.bleepstatic.com/images/news/Microsoft/Windows-10/update/KB5005463-pc-health-check/KB5005463-update.jpg)**Windows 10 KB5005463 update automatically installing**
Microsoft says that users who do not want PC Health Check on their system can simply uninstall it using the Settings app.


However, readers have told BleepingComputer that they have had to uninstall the application numerous times as the applications keep being reinstalled on the next check for updates.


To make matters worse, when attempting to uninstall KB5005463, Windows 10 states that the update is not installed, when that is clearly untrue, as shown in the image below.



![Unable to uninstall the KB5005463 update](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Unable to uninstall the KB5005463 update**
BleepingComputer has found a way to block the update from installing PC Health Check on your computer for those who do not want the application installed.


How to prevent PC Health Check from installing
----------------------------------------------


When you uninstall the PC Health Check application, it creates a "PreviousUninstall" value under the 'HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\PCHC' key and sets its value to '**1**', as shown below.



Windows Registry Editor Version 5.00


[HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\PCHC]  

"PreviousUninstall"=dword:00000001



If this value exists, the next time you perform a 'Check for updates' in Windows Update, the KB5005463 update and PC Health Check will not install again.


It is unclear why this key is not being created for some users or being ignored and causing the application to reinstall.


It is also possible to use the following Registry key to prevent the installation of PC Health Check, but it is not clear if this will cause unexpected behavior.



Windows Registry Editor Version 5.00


[HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\PCHealthCheck]  

"installed"=dword:00000001



There is no good reason not to install the utility as it does not run automatically and can be closed as needed.


However, if you do not wish to have the application installed, you can use one of the above methods to prevent its installation.


BleepingComputer has reached out to Microsoft to learn why PC Health Check is being reinstalled for some users and will update this article when we hear back.




#### Tags:
[[Windows]] [[Microsoft]] [[KB5005463]] [[uninstall]] [[However,]] [[BleepingComputer]] [[Bleeping Computer]]
