# How to fix the Windows 0x0000007c network printing error
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/how-to-fix-the-windows-0x0000007c-network-printing-error/)
+ Date: November 11, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 10 bug](https://www.bleepstatic.com/content/hl-images/2021/04/16/broken-windows-header.jpg)


A Windows security update released in October caused widespread Windows 10 and Windows 11 issues where users experience 0x0000007c errors when adding or printing to network printers. This article describes a fix you can use for the 0x0000007c printing errors.


Microsoft has been releasing a constant stream of Print Spooler security updates after Windows Print Spooler vulnerabilities known as '[PrintNightmare](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-remaining-windows-printnightmare-vulnerabilities/)' were disclosed starting in June.


However, these security fixes have led to massive problems for Windows network printing, causing organizations large and small to no longer print properly.


During the [October 2021 Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/microsoft-october-2021-patch-tuesday-fixes-4-zero-days-71-flaws/), Microsoft released the mandatory [KB5006670](https://www.bleepingcomputer.com/news/microsoft/windows-10-updates-kb5006670-and-kb5006667-released/) cumulative update with security updates for two vulnerabilities ([CVE-2021-36970](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36970) and [CVE-2021-41332](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41332)) in the Windows Print Spooler.


Once again, these fixes caused a wide range of network printing problems, where Windows users started receiving **0x00000709**and **0x0000007c**errors when attempting to print.


"Windows cannot connect to the printer. Operation failed with error 0x0000007c," reads one of the errors, as shown below.



![Windows 0x0000007c error when adding a new printer](https://www.bleepstatic.com/images/news/Microsoft/Windows-10/p/0x0000007c-printing-errors/0000007c-error.jpg)**Windows 0x0000007c error when adding a new printer**  
*Source: [Microsoft Forums](https://docs.microsoft.com/en-us/answers/questions/617683/error-0x0000007c-connecting-to-to-a-shared-printer.html)*
Since the October 2021 updates, Windows admins have been helping each other resolve their printing problems in a [22-page forum topic on BleepingComputer](https://www.bleepingcomputer.com/forums/t/759880/kb5006670-network-printer-problems-again-this-month/).


Unfortunately, to resolve most of these errors, users have resorted to [replacing the win32spl.dll file](https://www.bleepingcomputer.com/forums/t/759880/kb5006670-network-printer-problems-again-this-month/page-2#entry5262826) with an older version before October would resolve the issues. However, doing so will likely leave the computer vulnerable to any vulnerabilities fixed in the October updates.


How to fix Windows 0x0000007c printing errors
---------------------------------------------


This week, Microsoft started to [share a fix for the 0x0000007c printing errors](https://www.bleepingcomputer.com/forums/t/759880/kb5006670-network-printer-problems-again-this-month/page-19#entry5278335) in support calls with desperate Windows admins.


Microsoft is now privately distributing the fixes using ADMX installers. However, these packages are just manually using [Known Issue Rollback](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/known-issue-rollback-helping-you-keep-windows-devices-protected/ba-p/2176831) (KIR) fixes that add a new Windows Registry value to disable problematic changes from October.


KIR fixes are usually installed via Windows Update to revert problematic code changes, including security updates, that lead to bugs for many Windows users.


Below are the registry changes added by these fixes that you need to add to resolve the 0x0000007c network printing errors.


These registry values should be added to the Windows client, not the print server, and are different for each version of Windows, as shown below. It is also required to reboot the device after adding the Registry value for the change to take effect.


Below are the registry values for Windows 10 2004+, Windows 1909, and Windows 10 1809. We have also provided premade Registry files that can add the new value for you.


Registry value to add for **Windows 10 2004, 20H2, 21H1 and 21H2** (or use [this reg file](https://download.bleepingcomputer.com/reg/print-0000007c-2004.reg)):


Windows Registry Editor Version 5.00  

   

[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Policies\Microsoft\FeatureManagement\Overrides]  

"713073804"=dword:00000000


Registry value to add for **Windows 10 1909** (or use [this reg file](https://download.bleepingcomputer.com/reg/print-0000007c-1909.reg)):


Windows Registry Editor Version 5.00  

   

[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Policies\Microsoft\FeatureManagement\Overrides]  

"1921033356"=dword:00000000


  

Registry value to add for **Windows 10 1809** and **Windows Server 2019** (or use [this reg file](https://download.bleepingcomputer.com/reg/print-0000007c-1809.reg)):


Windows Registry Editor Version 5.00  

   

[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Policies\Microsoft\FeatureManagement\Overrides]  

"3598754956"=dword:00000000


These fixes are expected to roll out to everyone during the December 2021 Patch Tuesday. However, it is unclear if enabling them now will reduce the protection provided by security updates released in October.


If you can't wait until December for your printer issues to be fixed, you can use the above Registry values to fix the errors now.


Unfortunately, this fix does not resolve the 0x00000709 printing errors that continue to plague Windows users when printing to network printers.




#### Tags:
[[Windows]] [[0x0000007c]] [[Microsoft]] [[However,]] [[(or]] [[file):]] [[[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Policies\Microsoft\FeatureManagement\Overrides]]] [[Bleeping Computer]]
