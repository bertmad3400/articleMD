# SeriousSAM bug impacts all Windows 10 versions released in the past 2.5 years
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/serioussam-bug-impacts-all-windows-10-versions-released-in-the-past-2-5-years/)
+ Date: July 21, 2021
+ Author: Catalin Cimpanu


## Article:
![SeriousSAM bug impacts all Windows 10 versions released in the past 2.5 years](https://therecord.media/wp-content/uploads/2021/06/Windows-logo-1-e1626378197804.jpg)

A security researcher has discovered a major vulnerability in the Windows 10 operating system that can allow threat actors to gain access to elevated privileges and user accounts passwords.


Discovered by [Jonas Lyk](https://twitter.com/jonasLyk/status/1417205166172950531) over the weekend, the vulnerability resides in how Windows 10 grants access to some OS configuration files.


In particular, the vulnerability, nicknamed **SeriousSAM**, refers to how Windows 10 controls who can access folders like SAM, SECURITY, and SYSTEM.


**C:\Windows\System32\config\sam  
C:\Windows\System32\config\security  
C:\Windows\System32\config\system**


These are important Windows folders because they fold information such as hashed passwords for all Windows user accounts, security-related settings, data about encryption keys, and other core OS configuration details.


A threat actor who can read files from these locations can extract crucial information that can allow them to gain access to user passwords and system settings that can be abused for malicious purposes.


Because of the sensitive data they store, only Windows admin accounts are allowed to interact with these configuration files.


### Bug discovered by accident while testing Windows 11


However, while testing the upcoming Windows 11 release, Lyk discovered that while Windows was restricting low-privileged users from accessing those sensitive configuration files, copies of these files were also being saved in backup files created by [Shadow Volume Copy](https://en.wikipedia.org/wiki/Shadow_Copy), a Windows feature that creates snapshots of computer files during filesystem operations.


While in older Windows OS versions, access to these files was restricted in the Shadow Volume Copy feature, Lyk and other researchers[[1](https://doublepulsar.com/hivenightmare-aka-serioussam-anybody-can-read-the-registry-in-windows-10-7a871c465fa5), [2](https://www.kb.cert.org/vuls/id/506989), [3](https://www.blumira.com/sam-database-vulnerability/)] discovered that **since Windows 10 v1809**, released in November 2018, Microsoft has been failing to block access to these configuration files in Shadow Volume Copy backups.


This meant that malware or threat actors who gained a foothold on Windows 10 systems could abuse the SeriousSAM vulnerability to gain full control over Windows versions released over the past 2.5 years.


Threat actors gaining access to the [Security Account Manager](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-sam) (SAM) configuration file is considered the biggest issue, as this could allow them to steal hashed passwords, cracked the hashes offline, and hijack accounts.


However, the other configuration files stored in the SYSTEM and SECURITY folders can also yield similarly dangerous data, such as [DPAPI encryption keys](https://en.wikipedia.org/wiki/Data_Protection_API) and [Machine Account](https://adsecurity.org/?p=280) details (data used in joining computers to Active Directories).


 
### No patch available


In a security advisory published today, Microsoft formally acknowledged the issue, which the company is currently tracking as [CVE-2021-36934](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36934).


No workarounds, mitigations, or security patches are currently available, but a Microsoft spokesperson told *The Record* the issue is currently in the process of being investigated in order to prepare a future patch.


Right now, there’s nothing much that Windows 10 users can do to protect themselves.


Tips on how to log and monitor access to SAM data have also been shared in a [Reddit thread](https://old.reddit.com/r/cybersecurity/comments/oo6a8f/sam_database_vulnerability_what_we_know_so_far/), information that could be used by system administrators and security vendors to track possible SeriousSAM exploitation attempts.


Security researcher Kevin Beaumont has also published [proof-of-conce](https://github.com/GossiTheDog/HiveNightmare)[p](https://github.com/GossiTheDog/HiveNightmare)[t code](https://github.com/GossiTheDog/HiveNightmare) to allow sysadmins to test which of their systems are vulnerable to SeriousSAM attacks.





#### Tags:
[[Windows]] [[SeriousSAM]] [[Lyk]] [[System32]] [[config]] [[Microsoft]] [[The Record]]
