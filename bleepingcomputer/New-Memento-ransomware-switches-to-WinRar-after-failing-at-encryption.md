# New Memento ransomware switches to WinRar after failing at encryption
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-memento-ransomware-switches-to-winrar-after-failing-at-encryption/)
+ Date: November 18, 2021
+ Author: Bill Toulas


## Article:
![lockpad](https://www.bleepstatic.com/content/hl-images/2021/10/11/padlock.jpg?rand=1550384843)


A new ransomware group called Memento takes the unusual approach of locking files inside password-protected archives after their encryption method kept being detected by security software.


Last month, the group became active when they began exploiting a VMware vCenter Server web client flaw for the initial access to victims' networks.


The vCenter vulnerability is tracked as '[CVE-2021-21971](https://nvd.nist.gov/vuln/detail/CVE-2021-21972)' and is an unauthenticated, remote code execution bug with a 9.8 (critical) severity rating.


This flaw allows anyone with remote access to TCP/IP port 443 on an exposed vCenter server to execute commands on the underlying OS with admin privileges.


A patch for this flaw came out in February, but as indicated by Memento's operation, numerous organizations have not patched their installs.


This vulnerability has been under exploitation by Memento since April, while in May, a different actor was spotted exploiting it to install XMR miners via PowerShell commands.


Exploiting vCenter to deploy ransomware
---------------------------------------


Memento launched their ransomware operation last month when they began vCenter to extract administrative credentials from the target server, establish persistence through scheduled tasks, and then use RDP over SSH to spread laterally within the network.


After the reconnaissance stage, the actors used WinRAR to create an archive of the stolen files and exfiltrate it.



![Memento attack flow](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/memento-flow.png)**Memento attack flow**  
*Source: Sophos*
Finally, they used Jetico’s BCWipe data wiping utility to delete any traces left behind and then used a Python-based ransomware strain for the AES encryption.


However, Memento's original attempts at encrypted files as the systems had anti-ransomware protection, causing the encryption step to be detected and stopped before any damage was done.


A workaround
------------


To overcome the detection of commodity ransomware by security software, Memento came up with an interesting tactic - skip encryption altogether and move files into password-protected archives.


To do this, the group now moves files into WinRAR archives, sets a srong password for access protection, encrypts that key, and finally deletes the original files.


"Instead of encrypting files, the “crypt” code now put the files in unencrypted form into archive files, using the copy of WinRAR, saving each file in its own archive with a .vaultz file extension," [explains](https://news.sophos.com/en-us/2021/11/18/new-ransomware-actor-uses-password-protected-archives-to-bypass-encryption-protection/) Sophos analyst Sean Gallagher.


"Passwords were generated for each file as it was archived. Then the passwords themselves were encrypted."


The ransom note that is dropped demands the victim pay 15.95 BTC ($940,000) for complete recovery or 0.099 BTC ($5,850) per file.



![The Memento ransom note](https://www.bleepstatic.com/images/news/u/1220909/ransomware/ransom%20note(1).png)The Memento ransom note  

Source: Sophos
In the cases that Sophos investigated, these extortion attempts haven't led to a ransom payment, as victims used their backups to restore the files.


However, Memento is a new group that has just found an atypical approach that works, so they'll likely try it against other organizations.


As such, if you're using VMware vCenter Server and/or Cloud Foundation, make sure to update your tools to the latest available version to resolve known vulnerabilities.




#### Tags:
[[vCenter]] [[ransomware]] [[Sophos]] [[Bleeping Computer]]
