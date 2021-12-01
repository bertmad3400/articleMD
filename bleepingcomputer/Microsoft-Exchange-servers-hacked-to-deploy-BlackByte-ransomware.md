# Microsoft Exchange servers hacked to deploy BlackByte ransomware
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/microsoft-exchange-servers-hacked-to-deploy-blackbyte-ransomware/)
+ Date: December 1, 2021
+ Author: Bill Toulas


## Article:
![exchange_ransomware](https://www.bleepstatic.com/content/hl-images/2021/09/03/exchange-header.jpg?rand=345982338)


The BlackByte ransomware gang is now breaching corporate networks by exploiting Microsoft Exchange servers using the ProxyShell vulnerabilities.


ProxyShell is the name for a set of three Microsoft Exchange vulnerabilities that allow unauthenticated, remote code execution on the server when chained together.


These vulnerabilities are listed below and were fixed by security updates released in April and May 2021:


* [CVE-2021-34473](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34473) - Pre-auth Path Confusion leads to ACL Bypass *(Patched in April by [KB5001779](https://support.microsoft.com/en-us/topic/description-of-the-security-update-for-microsoft-exchange-server-2019-2016-and-2013-april-13-2021-kb5001779-8e08f3b3-fc7b-466c-bbb7-5d5aa16ef064)**)*
* [CVE-2021-34523](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34523) - Elevation of Privilege on Exchange PowerShell Backend *(Patched in April by [KB5001779](https://support.microsoft.com/en-us/topic/description-of-the-security-update-for-microsoft-exchange-server-2019-2016-and-2013-april-13-2021-kb5001779-8e08f3b3-fc7b-466c-bbb7-5d5aa16ef064))*
* [CVE-2021-31207](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-31207) - Post-auth Arbitrary-File-Write leads to RCE *(Patched in May by [KB5003435](https://support.microsoft.com/en-us/topic/description-of-the-security-update-for-microsoft-exchange-server-2019-2016-and-2013-may-11-2021-kb5003435-028bd051-b2f1-4310-8f35-c41c9ce5a2f1)**)*


Since researchers disclosed the vulnerabilities, [threat actors have begun to exploit them](https://www.bleepingcomputer.com/news/security/the-microsoft-exchange-hacks-how-they-started-and-where-we-are/) to breach servers and install web shells, coin miners, and ransomware.


BlackByte begins exploiting ProxyShell
--------------------------------------


In a detailed [report by Red Canary](https://redcanary.com/blog/blackbyte-ransomware/), researchers analyzed a BlackByte ransomware attack where they saw them exploiting the ProxyShell vulnerabilities to install web shells on a compromised Microsoft Exchange server.


Web Shells are small scripts uploaded to web servers that allow a threat actor to gain persistence to a device and remotely execute commands or upload additional files to the server.



![Example webshell](https://www.bleepstatic.com/images/news/security/webshell-example.jpg)**Example webshell**  
*Source: BleepingComputer*
The planted web shell is then utilized to drop a Cobalt Strike beacon on the server, injected into the Windows Update Agent process.


The widely abused penetration testing tool is then used for dumping credentials for a service account on the compromised system.


Finally, after taking over the account, the adversaries install the AnyDesk remote access tool and then proceed to the lateral movement stage.


BlackByte is still a severe threat
----------------------------------


When conducting ransomware attacks, threat actors commonly use third-party tools to gain elevated privileges or deploy the ransomware on a network.


However, the actual BlackByte ransomware executable plays a central role as it handles both privilege escalation and the ability to worm, or perform lateral movement, within the compromised environment.


The malware sets three registry values, one for local privilege elevation, one for enabling network connection sharing between all privilege levels, and one to allow long path values for file paths, names, and namespaces.


Before encryption, the malware deletes the "Raccine Rules Updater" scheduled task to prevent last-minute interceptions and also wipes shadow copies directly through WMI objects using an obfuscated PowerShell command.


Finally, stolen files are exfiltrated using WinRAR to archive files and anonymous file-sharing platforms such as "file.io" or "anonymfiles.com."


Although Trustwave [released a decryptor](https://www.bleepingcomputer.com/news/security/blackbyte-ransomware-decryptor-released-to-recover-files-for-free/) for BlackByte ransomware in October 2021, it is unlikely that the operators are still using the same encryption tactics that allowed victims to restore their files for free.


As such, you may or may not be able to restore your files using that decryptor, depending on what key was used in the particular attack.


Red Canary has seen multiple "fresh" variants of BlackByte in the wild, so there's clearly an effort from the malware authors to evade detection, analysis, and decryption.


From ProxyShell to ransomware
-----------------------------


Exploiting ProxyShell vulnerabilities to drop ransomware is not new, and in fact, we saw something similar at the start of November by actors who [deployed the Babuk strain](https://www.bleepingcomputer.com/news/security/microsoft-exchange-proxyshell-exploits-used-to-deploy-babuk-ransomware/).


The ProxyShell set has been under active exploitation from multiple actors [since at least March 2021](https://www.bleepingcomputer.com/news/security/state-hackers-rush-to-exploit-unpatched-microsoft-exchange-servers/), so the time to apply the security updates is well overdue.


If that’s impossible for any reason, admins are advised to monitor their exposed systems for precursor activity such as the deletion of shadow copies, suspicious registry modification, and PowerShell execution that bypasses restriction policies.




#### Tags:
[[ransomware]] [[BlackByte]] [[ProxyShell]] [[Microsoft]] [[(Patched]] [[PowerShell]] [[malware]] [[Bleeping Computer]]
