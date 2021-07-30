# Microsoft shares mitigation for recent Windows Server printing issues
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-shares-mitigation-for-recent-windows-server-printing-issues/)
+ Date: July 30, 2021
+ Author: Sergiu Gatlan


## Article:
![Windows server gets temporary mitigation for recent printing issues](https://www.bleepstatic.com/content/hl-images/2021/02/03/Windows-10.jpg)


Microsoft has released temporary mitigation info for a known issue that might cause print and scan failures on multiple Windows Server versions after installing July 2021 security updates on domain controllers.


As the company [revealed last week](https://www.bleepingcomputer.com/news/microsoft/windows-10-july-security-updates-break-printing-on-some-systems/), the known issue impacts printers, scanners, and multifunction devices using smart card (PIV) auth and non-compliant with CVE-2021-33764 hardening changes.


"On July 13, 2021, Microsoft released hardening changes for CVE-2021-33764. This might cause this issue when you install updates released July 13, 2021 or later on a domain controller (DC)," Microsoft [explains](https://support.microsoft.com/en-us/topic/kb5005408-smart-card-authentication-might-cause-print-and-scan-failures-514f0bc5-ecde-4e5e-8c5a-2a776d7fb89a).


"The affected devices are smart card authenticating printers, scanners, and multifunction devices that don’t support either Diffie-Hellman (DH) for key-exchange during PKINIT Kerberos authentication or don't advertise support for des-ede3-cbc ("triple DES”) during the Kerberos AS request."


Customers who encounter this issue are advised to first check if they have the latest drivers and firmware installed on impacted devices.


If the known issue still appears on up-to-date devices, affected customers should contact the device manufacturer and ask for setting changes or updates to make the printer or scanner compliant with CVE-2021-33764 hardenings deployed via July Windows 10 security updates.


Temporary mitigation for non-compliant environments
---------------------------------------------------


If no updates are available from device manufacturers, Microsoft provides temporary mitigation for Windows Server DCs while working to get the printing or scanning devices into compliance.


"You must have your non-compliant devices updated and compliant or replaced by February 8, 2022, when the temporary mitigation will not be usable in security updates," Microsoft adds.


Affected customers are advised to take the following steps on all domain controllers to mitigate ongoing printing and scanning issues:


1. On your Domain Controllers, set the temporary mitigation registry value listed below to **1** (enable) by using the Registry Editor or the automation tools available in your environment:



```
reg add HKLM\System\CurrentControlSet\Services\Kdc /v Allow3DesFallback /t REG\_DWORD /d 1 /f
```

2. Install an update that allows the temporary mitigation available in updates released July 27, 2021 or later (below are the first updates to allow the temporary mitigation):


	* Windows Server 2019: [KB5005394](https://support.microsoft.com/help/5005394)
	
	
	* Windows Server 2016: [KB5005393](https://support.microsoft.com/help/5005393)
	
	
	* Windows Server 2012 R2: [KB5005391](https://support.microsoft.com/help/5005391)
	
	
	* Windows Server 2012: [KB5005389](https://support.microsoft.com/help/5005389)
	
	
	* Windows Server 2008 R2 SP1: [KB5005392](https://support.microsoft.com/help/5005392)
	
	
	* Windows Server 2008 SP2: [KB5005390](https://support.microsoft.com/help/5005390)
3. Restart your domain controller.




Emergency updates released for Windows 10
-----------------------------------------


Microsoft has also [released cumulative out-of-band updates](https://www.bleepingcomputer.com/news/microsoft/new-windows-10-kb5005394-emergency-update-fixes-printing-issues/) this week to address this known issue on Windows client platforms, including:


* [KB5005394 (Windows 10 1809)](https://support.microsoft.com/en-gb/topic/july-27-2021-kb5005394-os-build-17763-2091-out-of-band-58863c8f-e514-47cc-b68e-14dbb883777f)
* [KB5005393 (Windows 10 1607)](https://support.microsoft.com/en-us/topic/july-29-2021-kb5005393-os-build-14393-4532-out-of-band-97eb0e8c-3748-4570-af41-317aaa2d06ab)
* [KB5005392 (Windows 7 SP1)](https://support.microsoft.com/en-us/topic/kb5005392-noncompliant-devices-might-not-work-when-using-piv-after-installing-the-july-13-2021-update-for-windows-7-sp1-or-windows-server-2008-r2-sp1-2e410b99-3645-4321-a5a2-404027900fce)


While more cumulative should be released to address the issue on all impacted Windows client releases, Microsoft confirmed when [acknowledging this known printing issue on Friday](https://www.bleepingcomputer.com/news/microsoft/windows-10-july-security-updates-break-printing-on-some-systems/) that all affected smart card authenticating devices **should work as expected when using username and password authentication.**


Redmond has also [addressed Windows 10 printing issues](https://www.bleepingcomputer.com/news/microsoft/windows-10-printing-issues-fixed-by-july-patch-tuesday-update/) caused by changes introduced in the June 2021 cumulative update preview earlier this month.




#### Tags:
[[Windows]] [[Microsoft]] [[non-compliant]] [[(Windows]] [[Bleeping Computer]]
