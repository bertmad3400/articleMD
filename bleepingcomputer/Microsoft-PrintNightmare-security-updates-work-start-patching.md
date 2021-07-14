# Microsoft: PrintNightmare security updates work, start patching!
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/microsoft-printnightmare-security-updates-work-start-patching/)
+ Date: July 9, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft: PrintNightmare security updates work, start patching!](https://www.bleepstatic.com/content/hl-images/2021/07/09/Windows-headpic.jpg)


Microsoft says the emergency security updates released at the start of the week correctly patch the PrintNightmare Print Spooler vulnerability for all supported Windows versions and urges users to start applying the updates as soon as possible.


This clarified guidance comes after security researchers [tagged the patches as incomplete](https://www.bleepingcomputer.com/news/microsoft/microsofts-incomplete-printnightmare-patch-fails-to-fix-vulnerability/) after finding that the OOB security updates could be bypassed in specific scenarios.



"Our investigation has shown that the OOB security update is working as designed and is effective against the known printer spooling exploits and other public reports collectively being referred to as PrintNightmare," the Microsoft Security Response Center explains.


"All reports we have investigated have relied on the changing of default registry setting related to Point and Print to an insecure configuration."


Clarified PrintNightmare guidance
---------------------------------


Microsoft has updated the PrintNightmare patch guidance and is now encouraging customers to update as soon as possible.


These are the correct steps required to patch this critical Windows Print Spooler RCE vulnerability as shared by Microsoft:


* In ALL cases, apply the CVE-2021-34527 security update. The update will not change existing registry settings
* After applying the security update, review the registry settings documented in the CVE-2021-34527 advisory
* If the registry keys documented do not exist, no further action is required
* If the registry keys documented exist, in order to secure your system, you must confirm that the following registry keys are set to 0 (zero) or are not present:
	+ HKEY\_LOCAL\_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Printers\PointAndPrint
	+ NoWarningNoElevationOnInstall = 0 (DWORD) or not defined (default setting)
	+ UpdatePromptSettings = 0 (DWORD) or not defined (default setting)


Additional information and further guidance are available in the [KB5005010](https://support.microsoft.com/en-us/topic/kb5005010-restricting-installation-of-new-printer-drivers-after-applying-the-july-6-2021-updates-31b91c02-05bc-4ada-a7ea-183b129578a7) support document and the [CVE-2021-34527](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527) security advisory.


How to install the PrintNightmare security updates
--------------------------------------------------


You can find detailed steps on how to install these emergency security updates in the support documents linked below:


* Windows 10, version 21H1 ([KB5004945](https://support.microsoft.com/help/5004945))
* Windows 10, version 20H2 ([KB5004945](https://support.microsoft.com/help/5004945))
* Windows 10, version 2004 ([KB5004945](https://support.microsoft.com/help/5004945))
* Windows 10, version 1909 ([KB5004946](https://support.microsoft.com/help/5004946))
* Windows 10, version 1809 and Windows Server 2019 ([KB5004947](https://support.microsoft.com/help/5004947))
* Windows 10, version 1607 and Windows Server 2016 ([KB5004948](https://support.microsoft.com/help/5004948))
* Windows 10, version 1507 ([KB5004950](https://support.microsoft.com/help/5004950))
* Windows Server 2012 (Monthly Rollup [KB5004956](https://support.microsoft.com/help/5004956) / Security only [KB5004960](https://support.microsoft.com/help/5004960))
* Windows 8.1 and Windows Server 2012 R2 (Monthly Rollup [KB5004954](https://support.microsoft.com/help/5004954) / Security only [KB5004958](https://support.microsoft.com/help/5004958))
* Windows 7 SP1 and Windows Server 2008 R2 SP1 (Monthly Rollup [KB5004953](https://support.microsoft.com/help/5004953) / Security only [KB5004951](https://support.microsoft.com/help/5004951))
* Windows Server 2008 SP2 (Monthly Rollup [KB5004955](https://support.microsoft.com/help/5004955) / Security only [KB5004959](https://support.microsoft.com/help/5004959))


If you cannot immediately install the security updates on your system(s), you can disable the Windows Print Spooler service to [mitigate the PrintNightmare vulnerability temporarily](https://www.bleepingcomputer.com/news/microsoft/how-to-mitigate-print-spooler-vulnerability-on-windows-10/).


Thursday night, Microsoft has also issued an emergency fix to address [printing issues affecting Zebra and Dymo receipt or label printers](https://www.bleepingcomputer.com/news/microsoft/microsoft-pushes-emergency-fix-for-windows-10-kb5004945-printing-issues/) due to changes introduced in the June 2021 cumulative update preview with the recently released KB5003690, KB5004760, and KB5004945 updates.


This fix is being rolled out via Microsoft's [Known Issue Rollback (KIR) feature](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-10-known-issue-rollback-auto-fixes-update-bugs/), which pushes fixes for known issues through Windows Update and should reach most impacted systems within 24 hours (restarting the computer may also speed up the process.)




#### Tags:
[[Windows]] [[Microsoft]] [[PrintNightmare]] [[KB5004945]] [[Rollup]] [[CVE-2021-34527]] [[Bleeping Computer]]
