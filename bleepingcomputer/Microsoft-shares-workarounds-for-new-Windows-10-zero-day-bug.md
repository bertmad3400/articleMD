# Microsoft shares workarounds for new Windows 10 zero-day bug
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-shares-workarounds-for-new-windows-10-zero-day-bug/)
+ Date: July 21, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft shares workarounds for new Windows 10 zero-day bug](https://www.bleepstatic.com/content/hl-images/2021/07/09/Windows_headpic.jpg)


Microsoft has shared workarounds for a Windows 10 zero-day vulnerability that can let attackers gain admin rights on vulnerable systems and execute arbitrary code with SYSTEM privileges.


As [BleepingComputer previously reported](https://www.bleepingcomputer.com/news/microsoft/new-windows-10-vulnerability-allows-anyone-to-get-admin-privileges/), a local elevation of privilege bug in recently released Windows versions allows users with low privileges to access sensitive Registry database files.


Affects Windows 10 versions released since 2018
-----------------------------------------------


The security flaw, publicly disclosed by security researcher [Jonas Lykkegaard](https://twitter.com/jonasLyk) on Twitter and yet to receive an official patch, is now tracked by Microsoft as [**CVE-2021-36934**](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36934).


"An elevation of privilege vulnerability exists because of overly permissive Access Control Lists (ACLs) on multiple system files, including the Security Accounts Manager (SAM) database," Microsoft explains in a security advisory published on Tuesday evening.


"An attacker could then install programs; view, change, or delete data; or create new accounts with full user rights. An attacker must have the ability to execute code on a victim system to exploit this vulnerability."


As Microsoft further revealed, this zero-day vulnerability impacts Windows releases since October 2018, starting with Windows 10, version 1809. 


Lykkegaard also found that Windows 11 (Microsoft's not yet officially released OS) is also impacted.


Workarounds now available
-------------------------


The databases exposed to user access by this bug (i.e., SYSTEM, SECURITY, SAM, DEFAULT, and SOFTWARE) are stored under the C:\Windows\system32\config folder.


Mimikatz creator [Benjamin Delpy](https://twitter.com/gentilkiwi) told BleepingComputer that anyone could easily take advantage of the incorrect file permissions to steal an elevated account's NTLM hashed password and gain higher privileges via a pass-the-hash attack.


While attackers can't directly access the databases due to access violations triggered by the files always being in use by the OS, they can access them through shadow volume copies.


Microsoft recommends restricting access to the problematic folder ***AND*** deleting Volume Shadow Copy Service (VSS) shadow copies to mitigate this issue.


Users should be aware that removing shadow copies from their systems could impact system and file restore operations, such as restoring data using third-party backup apps.


These are the steps needed to block exploitation of this vulnerability temporarily:



**Restrict access to the contents of %windir%\system32\config:**


1. Open Command Prompt or Windows PowerShell as an administrator.


2. Run this command: `icacls %windir%\system32\config\*.* /inheritance:e`



**Delete Volume Shadow Copy Service (VSS) shadow copies:**


1. Delete any System Restore points and Shadow volumes that existed prior to restricting access to %windir%\system32\config.


2. Create a new System Restore point (if desired).



Microsoft is still investigating the vulnerability and is working on a patch that will most likely be released as an out-of-band security update later this week. 




#### Tags:
[[Windows]] [[Microsoft]] [[system32]] [[config]] [[windir]] [[Bleeping Computer]]
