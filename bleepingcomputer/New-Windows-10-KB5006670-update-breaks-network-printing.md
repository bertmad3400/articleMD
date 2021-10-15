# New Windows 10 KB5006670 update breaks network printing
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/new-windows-10-kb5006670-update-breaks-network-printing/)
+ Date: October 15, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 10 bug](https://www.bleepstatic.com/content/hl-images/2021/01/13/windows-10-glass-broken.jpg)


Windows 10 users and administrators report widescale network printing issues after installing the KB5006670 cumulative update and other updates released this week.


On Tuesday, Microsoft released Windows updates to fix bugs and security vulnerabilities as part of the [October 2021 Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/microsoft-october-2021-patch-tuesday-fixes-4-zero-days-71-flaws/).


These updates include [KB5006674](https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5006674-update-released-with-compatibility-fixes/) for Windows 11, [KB5006670](https://www.bleepingcomputer.com/news/microsoft/windows-10-updates-kb5006670-and-kb5006667-released/) for Windows 10 2004, 20H1, and 21H1, KB5006667 for Windows 10 1909, and KB5006714 for Windows 8.


Since installing the KB5006670 update, users are reporting that they cannot print to network print servers, with some users receiving **0x00000709**or '**Element not found**' errors when attempting to print.


In an [eight-page forum topic](https://www.bleepingcomputer.com/forums/t/759880/kb5006670-network-printer-problems-again-this-month/) at BleepingComputer, Windows administrators recounted their frustration with the printing bugs and came to the same conclusion — uninstalling this week's updates resolves the problem.


Since July, Microsoft has been releasing a constant stream of security updates to fix the [PrintNightmare](https://www.bleepingcomputer.com/tag/printnightmare/) vulnerabilities in the Windows Print Spooler.


As threat actors, [including ransomware gangs](https://www.bleepingcomputer.com/news/security/ransomware-gang-uses-printnightmare-to-breach-windows-servers/), actively exploit these vulnerabilities, Microsoft has changed its Point and Print printing feature drastically. Unfortunately, while these changes fix the vulnerabilities, they also lead to problems printing to network print servers.


This week, Microsoft released further security updates for Windows printing vulnerabilities tracked as [CVE-2021-41332](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41332) and [CVE-2021-36970](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36970), likely causing the new network printing issues.


While most of the reported problems are related to Windows 10's KB5006670 update, this is likely because it is the most widely used version of Windows at this time.


The same security fixes were also released for Windows 10 1909 and Windows 11 and will likely cause similar issues on those Windows versions.


How to fix KB5006670 network printing issues
--------------------------------------------


When the September cumulative updates caused printing issues, it was possible to fix them by allowing non-Admins to install printer drivers or [disabling the 'RpcAuthnLevelPrivacyEnabled' Registry value](https://www.bleepingcomputer.com/news/microsoft/how-to-fix-the-windows-0x0000011b-network-printing-error/).


However, this Registry key is no longer working for the problems caused by the October updates, and users are required to fix it using other methods.


The [BleepingComputer forum topic](https://www.bleepingcomputer.com/forums/t/759880/kb5006670-network-printer-problems-again-this-month/) includes numerous suggestions from Windows admins on how to resolve the networking printing issues caused by the Windows 10 KB5006670 update. Unfortunately, as these suggestions either remove security updates or don't always work, they are not ideal for resolving the issues.


What makes these printing issues so frustrating is Microsoft's lack of clear guidance and the numerous changes that happen each month to the Windows printing feature.


As these changes all resolve different vulnerable aspects of the Windows Print Spooler, they create a mess of individual fixes that Windows admins need to figure out whether they will fix their printing problems.


BleepingComputer has reached out to Microsoft for official guidance on resolving all of these issues but has not heard back at this time.


### Method 1: Uninstall the KB5006670 update


The most common suggestion is to simply uninstall the KB5006670 update, which can be done using the following command in an elevated command prompt:


However, uninstalling the update will remove the [security fixes for 74 vulnerabilities](https://www.bleepingcomputer.com/news/microsoft/microsoft-october-2021-patch-tuesday-fixes-4-zero-days-71-flaws/), including one actively exploited, making this a dangerous method.


### Method 2: Replace C:\Windows\System32\Win32spl.dll


Others have found that replacing[the Win32spl.dll DLL file](https://www.bleepingcomputer.com/forums/t/759880/kb5006670-network-printer-problems-again-this-month/?p=5262826) with the version from the September 2021 updates will fix the network printing problem.



> 
> "KB5006670 replaces C:\Windows\System32\Win32spl.dll with version 10.0.19041.1288 which halts printing
> 
> 
> We replace this dll with version 10.0.19041.1237 that was installed September's Cumulative update
> 
> 
> The attached batch script will copy your "good" dll file to each computer this runs on from a server location and rename the "bad" dll. I run it as a startup script for ease"
> 
> 
> 


As this DLL was likely changed as part of a security update, this too will cause your computer to become less protected from possible future vulnerability exploits.


### Method 3: Recreating printer queues on print servers


Some users have also reported that removing and reinstalling their printers on the print server resolved their problem.


When you remove the printer and install it again as an admin, the queues will be rebuilt, potentially allowing printing to work again.


However, workstations may need to be reconfigured to use the new printer queue, which may be a very time-consuming task for some organizations.


### Method 4: Enable CopyFiles feature again


Finally, some HP printer drivers require the [CopyFiles feature](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-remaining-windows-printnightmare-vulnerabilities/), which Microsoft disabled in September by default.


For users who still need this feature, Microsoft introduced a hidden Group Policy that allows you to enable it again.


To enable the CopyFiles feature, create a Windows Registry value under the **HKLM\Software\Policies\Microsoft\Windows NT\Printers** key named **CopyFilesPolicy**. When set to '1', CopyFiles will be enabled again.




#### Tags:
[[Windows]] [[KB5006670]] [[Microsoft]] [[update,]] [[CopyFiles]] [[problem.]] [[vulnerabilities,]] [[However,]] [[again.]] [[feature,]] [[Bleeping Computer]]
