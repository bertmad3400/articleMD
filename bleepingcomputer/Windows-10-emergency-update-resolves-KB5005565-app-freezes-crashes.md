# Windows 10 emergency update resolves KB5005565 app freezes, crashes
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-10-emergency-update-resolves-kb5005565-app-freezes-crashes/)
+ Date: September 25, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 10](https://www.bleepstatic.com/content/hl-images/2021/01/25/Windows-10.jpg)


Microsoft has released an emergency fix for freezing and crashing app issues caused by September's KB5005565  and KB5005101 cumulative updates.


With the release of the Windows 10 KB5005101 preview update and the KB5005565 cumulative update, Microsoft states that users may have experienced app freezes, app crashes, and the inability to launch an application.


These issues only affected users utilizing the Microsoft Exploit Protection Export Address Filtering (EAF) feature, which is used to detect dangerous operations used by malicious code or exploit modules.


"After installing [KB5005101](https://support.microsoft.com/help/5005101) or a later update on devices using Microsoft Exploit Protection Export Address Filtering (EAF), you might have issues with some applications," explained Microsoft.


"You might be experiencing this issue if apps fail to open, fail to open files, or you might receive a white window when attempting to login."


Microsoft has rolled out a fix using the [Known Issue Rollback (KIR) feature](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-10-known-issue-rollback-auto-fixes-update-bugs/), distributed to Windows 10 devices using Windows Update.


"This issue is resolved using [Known Issue Rollback (KIR)](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/known-issue-rollback-helping-you-keep-windows-devices-protected/ba-p/2176831). Please note that it might take up to 24 hours for the resolution to propagate automatically to consumer devices and non-managed business devices. Restarting your Windows device might help the resolution apply to your device faster."


For enterprise users or those who wish to receive the update sooner, you can also install various group policies or add Registry keys to install the fix.


Microsoft has released the following group policies, which users can install to apply the fix. It is critical that users only install the group policy associated with a device's version of Windows.


* [Windows Server 2022](https://download.microsoft.com/download/7/f/1/7f194890-eea9-4cad-b19f-25ab67e41bbe/Windows%20Server%202022%20Known%20Issue%20Rollback%20091821%2001.msi)
* [Windows 10, version 2004, Windows 10, version 20H2 and Windows 10, version 21H1](https://download.microsoft.com/download/7/f/1/7f194890-eea9-4cad-b19f-25ab67e41bbe/Windows%2010%20(2004%20,%2020H2%20and%2021H1)%20Known%20Issue%20Rollback%20091721%2001.msi)
* [Windows 10, version 1909](https://download.microsoft.com/download/7/f/1/7f194890-eea9-4cad-b19f-25ab67e41bbe/Windows%2010%20(1903%20&%201909)%20Known%20Issue%20Rollback%20091721%2001.msi)
* [Windows 10, version 1809, Windows Server 2019](https://download.microsoft.com/download/7/f/1/7f194890-eea9-4cad-b19f-25ab67e41bbe/Windows%2010%20(1809)%20&%20Windows%20Server%202019%20Known%20Issue%20Rollback%20091821%2001.msi)


Windows users can also install the fix immediately by running one of the following commands from a Windows 10 elevated command prompt. Like the registry policies, only run the command associated with your version of Windows.


Resolved using the Known Issue Rollback feature
-----------------------------------------------


When Microsoft releases new updates to fix known bugs, the new code may cause further issues in Windows 10.


If Windows telemetry and diagnostics indicate that a large audience of Windows 10 users are affected by a new issue, Microsoft can release a Known Issue Rollback (KIR) fix to disable the new code causing the issues, as illustrated below.



![Illustration of how Known Issue Rollout fixes are delivered](https://www.bleepstatic.com/images/news/u/1109292/2021/Known-Issue-Rollback.png)**Illustration of how Known Issue Rollout fixes are delivered**
In the past, Microsoft has used Known Issue Rollout fixes to [resolve printing issues](https://www.bleepingcomputer.com/news/microsoft/microsoft-pushes-emergency-fix-for-windows-10-kb5004945-printing-issues/) and [performance issues while gaming](https://www.bleepingcomputer.com/news/microsoft/microsoft-pushes-emergency-fix-for-windows-10-kb5001330-gaming-issues/). 


While these fixes are distributed via Windows Update, they are not delivered as an actual update. Instead, they are deployed by creating Windows Registry entries that disable changes made in previous updates.


Microsoft says that Known Issue Rollout fixes are usually installed within 24 hours and that restarting the computer may speed up this process.




#### Tags:
[[Windows]] [[Microsoft]] [[KB5005101]] [[Bleeping Computer]]
