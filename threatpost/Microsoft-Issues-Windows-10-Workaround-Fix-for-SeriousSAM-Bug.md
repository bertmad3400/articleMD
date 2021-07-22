# Microsoft Issues Windows 10 Workaround Fix for ‘SeriousSAM’ Bug
### A privilege elevation bug in Windows 10 opens all systems to attackers to access data and create new accounts on systems.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168034)
+ Date: July 22, 2021  8:57 am
+ Author: Tom Spring


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/22085143/windows-10.jpg)
A privilege escalation bug, affecting versions of Windows 10, received a workaround fix by Microsoft Wednesday to prevent attackers from accessing data and creating new accounts on compromised systems.


The bug, dubbed SeriousSAM, affects the Security Accounts Manager (SAM) database in all versions of Windows 10. The SAM component in Windows houses user account credentials and network domain information – a juicy target for attackers. A prerequisite for abuse of the bug is an adversary needs either remote or local access to the vulnerable Windows 10 system.


Tracked as CVE-2021-36934, Microsoft said the vulnerability exists because of overly permissive Access Control Lists on multiple system files, including the (SAM) database. “An attacker who successfully exploited this vulnerability could run arbitrary code with SYSTEM privileges. An attacker could then install programs; view, change, or delete data; or create new accounts with full user rights,” the [Microsoft bulletin explains](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36934).  

Simply stated, an attacker could leverage the bug to gain access to the SAM database of hashed credentials, which then could be decrypted offline and used to bypass Windows 10 user access controls.


Proof-of-Concept Available
--------------------------


The bug is rated important in severity by Microsoft. The flaw was revealed to Microsoft by researchers Jonas Lyk over the weekend and made public Monday. [Proof-of-concept code](https://github.com/GossiTheDog/HiveNightmare) was published by researcher Kevin Beaumont to help network admins identify exposure to the bug.


In a Tweet by Lyk, the researcher said the bug also impacts pre-production versions of Windows 11 (slated to be released in October, 2021). “For some reason on win11 the SAM file now is READ for users. So if you have shadowvolumes enabled you can read the sam file,” [he tweeted](https://twitter.com/jonasLyk/status/1417205166172950531).


The researcher said the bug was discovered while tinkering with Windows 11. He explains that SAM database content, while not accessible on the OS, can be accessed when part of a Windows Shadow Volume Copy (VSS) backup. VSS is a service that allows automatic or manual real-time backups of system files (preserved in their current state) tied to a particular drive letter (volume).


He later identified the same issue is present on Windows 10 systems dating back to 2018 (v1809).


**No Patch Available: Workaround Fix Recommended**
--------------------------------------------------


For this reason, Microsoft is recommending sysadmin delete the backup copies of the VSS files. The OS maker does not offer a patch for the bug, rather a simple workaround.


Microsoft explains the two step process as: “Delete any System Restore points and Shadow volumes that existed prior to restricting access to %windir%\system32\config” and “create a new System Restore point (if desired).”


It also cautions that deleting VSS shadow copies “could impact restore operations, including the ability to restore data with third-party backup applications.”


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Windows]] [[Microsoft]] [[ThreatPost]]
