# Windows 10 KB5005611 update fixes Microsoft Outlook issues
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5005611-update-fixes-microsoft-outlook-issues/)
+ Date: September 30, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 10](https://www.bleepstatic.com/content/hl-images/2021/01/25/Windows-10.jpg)


Microsoft has released the optional KB5005611 Preview cumulative update for Windows 10 2004, Windows 10 20H2, and Windows 10 21H1. This update fixes bugs in Microsoft Outlook and makes it easier to mitigate the PrintNightmare vulnerability.


This cumulative update is part of Microsoft's September 2021 monthly "C" update, allowing Windows users to test the upcoming fixes before they are automatically deployed in the forthcoming October 2021 Patch Tuesday.


Unlike Patch Tuesday cumulative updates, the "C" preview updates are optional do not include any security updates.


Windows users can install this update by going into **Settings**, clicking on **Windows Update,** and select **'Check for Updates**.'


As this is an optional update, you will be asked whether you wish to install it by clicking on the 'Download and install' link, as shown in the image below.



![Windows Update offering the optional KB5005611 update](https://www.bleepstatic.com/images/news/Microsoft/Windows-10/c/cumulative-updates/KB5005611/KB5005611.jpg)**Windows Update offering the optional KB5005611 update**
Windows 10 users can also manually download and install the KB5005611 preview update from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5005611).


Microsoft Outlook and News and Interests fixes
----------------------------------------------


In the Windows 10 KB5005611 preview update, Microsoft has introduced numerous fixes for Microsoft Outlook and News and Interests that people have been experiencing since previous updates.


For Microsoft Outlook, this update fixes a bug causing the application to stop working suddenly or for an add-in to prevent you from composing replies to emails.


For News and Interests, this update resolves blurry icons and the app displaying when you right-click on the taskbar even if you have disabled the feature.


Now easier to mitigate PrintNightmare vulnerabilities
-----------------------------------------------------


In July, Microsoft [added a new group policy](http://support.microsoft.com/en-us/topic/kb5005010-restricting-installation-of-new-printer-drivers-after-applying-the-july-6-2021-updates-31b91c02-05bc-4ada-a7ea-183b129578a7) to require drivers only to be installed by administrators. Microsoft did this to fix a remote code execution vulnerability known as [PrintNightmare](https://www.bleepingcomputer.com/tag/printnightmare/).


In August, [Microsoft enabled this setting by default](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-print-spooler-printnightmare-vulnerability/), causing numerous printing issues for enterprise users.


While this setting was added as a group policy, it could only be enabled or disabled by manually editing the Windows Registry. Microsoft did this by adding the **RestrictDriverInstallationToAdministrators** value under the **HKLM\Software\Policies\Microsoft\Windows NT\Printers\PointAndPrint**key.


Microsoft has introduced a group policy that allows you to manage this setting more easily with today's update.


Microsoft has also modified the following Group Policy settings to configure period, or dot (.) delimited IP addresses for approved print servers:


* [Package Point and Print - Approved Servers](https://gpsearch.azurewebsites.net/Default_legacy.aspx?PolicyID=2208)
* [Point and Print Restrictions](https://gpsearch.azurewebsites.net/Default_legacy.aspx?PolicyID=2212)


What's new in Windows 10 KB5005611
----------------------------------


After installing this update, Windows 10 2004 will be updated to build 19041.1266, Windows 10 20H2 will be updated to build 19042.1266, and Windows 10 21H1 will be updated to build 19043.1266.


The Windows 10 KB5005611 cumulative update preview includes thirty-eight improvements or fixes, with the highlighted ones listed below:


* Updates an issue that causes the system clock to be wrong by one hour after a daylight saving time (DST) change.  


* Updates an issue that causes applications, such as Microsoft Outlook, to suddenly stop working during normal use.


* Updates an issue with the Microsoft Outlook Add-in that prevents you from typing a reply. 


* Updates an issue that causes blurry News and interests icons when you use certain screen resolutions.


* Updates an issue that causes **News and interests** to appear when you right-click the taskbar even if you have turned off that feature on your device.


* Updates an issue that might cause distortion in the sound that Cortana and other voice assistants record. 


* Updates an issue that causes your device to stop working after you restart it.


* Updates an issue that prevents you from providing input to apps when the taskbar is not at the bottom of the screen. 




A full list of fixes can be found in the [KB5005611 support bulletin](https://support.microsoft.com/en-us/topic/september-30-2021-kb5005611-os-builds-19041-1266-19042-1266-and-19043-1266-preview-a37f5409-f320-4175-9a66-c2682fc11c07).




#### Tags:
[[Microsoft]] [[Windows]] [[KB5005611]] [[update,]] [[taskbar]] [[Bleeping Computer]]
