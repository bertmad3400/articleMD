# LockFile Ransomware Uses Never-Before Seen Encryption to Avoid Detection
### Researchers from Sophos discovered the emerging threat in July, which exploits the ProxyShell vulnerabilities in Microsoft Exchange servers to attack systems.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169042)
+ Date: August 31, 2021  6:42 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/31064150/ransomware-cpu.jpg)
Researchers discovered a novel ransomware emerging on the heels of the [ProxyShell vulnerabilities](https://threatpost.com/proxyshell-attacks-unpatched-exchange-servers/168879/) discovery in Microsoft Exchange servers. The threat, dubbed LockFile, uses a unique “intermittent encryption” method as a way to evade detection as well as adopting tactics from previous ransomware gangs.


Discovered by researchers at Sophos, LockFile ransomware encrypts every 16 bytes of a file, which means some ransomware protection solutions don’t notice it because  “an encrypted document looks statistically very similar to the unencrypted original,” Mark Loman, director, engineering, for next-gen technologies at Sophos, wrote in [a report](https://news.sophos.com/en-us/2021/08/27/lockfile-ransomwares-box-of-tricks-intermittent-encryption-and-evasion/) on LockFile published last week.


“We haven’t seen intermittent encryption used before in ransomware attacks,” he wrote.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The ransomware first exploits unpatched [ProxyShell flaws](https://threatpost.com/exchange-servers-attack-proxyshell/168661/) and then uses what’s called a PetitPotam NTLM relay attack to seize control of a victim’s domain, researchers explained. In this type of attack, a threat actor uses Microsoft’s Encrypting File System Remote Protocol (MS-EFSRPC) to connect to a server, hijack the authentication session, and manipulate the results such that the server then believes the attacker has a legitimate right to access it, Sophos researchers described [in an earlier report](https://news.sophos.com/en-us/2021/08/25/how-petitpotam-hijacks-the-windows-api-and-what-you-can-do-about-it/).


LockFile also shares some attributes of previous ransomware as well as other tactics—such as forgoing the need to connect to a command-and-control center to communicate–to hide its nefarious activities, researchers found.


“Like [WastedLocker](https://news.sophos.com/en-us/2020/08/04/wastedlocker-techniques-point-to-a-familiar-heritage/) and [Maze](https://news.sophos.com/en-us/2020/05/12/maze-ransomware-1-year-counting/) ransomware, LockFile ransomware uses memory mapped input/output (I/O) to encrypt a file,” Loman wrote in the report. “This technique allows the ransomware to transparently encrypt cached documents in memory and causes the operating system to write the encrypted documents, with minimal disk I/O that detection technologies would spot.”


**Deeper Dive**
---------------


Researchers analyzed LockFile using sample of the ransomware with the SHA-256 hash  “bf315c9c064b887ee3276e1342d43637d8c0e067260946db45942f39b970d7ce” that they discovered on [VirusTotal](https://www.virustotal.com/gui/file/bf315c9c064b887ee3276e1342d43637d8c0e067260946db45942f39b970d7ce/detection). Upon opening, the sample appears to have only three functions and three sections.


The first section, named OPEN, contains no data – only zeroes, researchers said. It’s the second section, CLSE, that includes the sample’s three functions. However, rest of the data in the section is encoded code that is decoded later and placed in the “OPEN” section, which researchers examined in depth, they said.


“The entry() function is simple and calls FUN\_1400d71c0():,” researchers wrote. “The FUN\_1400d71c0() function decodes the data from the CLSE section and puts it in the OPEN section. It also resolves the necessary DLLs and functions. Then it manipulates the IMAGE\_SCN\_CNT\_UNINITIALIZED\_DATA values and jumps to the code placed in the OPEN section.”


Researchers used WinDbg and .writemem to write the OPEN section to disk to analyze the code statically in [Ghidra](https://ghidra-sre.org/), an open-source reverse-engineering tool. There they found the ransomware’s main function, the first part of which initializes a crypto library that LockFile likely uses for its encryption functions, they said.


The ransomware then uses the Windows Management Interface (WMI) command-line tool WMIC.EXE–which is part of every Windows installation—to terminate all processes with vmwp in their name, repeating the process for other critical business processes associated with virtualization software and databases, researchers wrote.


“By leveraging WMI, the ransomware itself is not directly associated with the abrupt termination of these typical business critical processes,” they explained. “Terminating these processes will ensure that any locks on associated files/databases are released, so that these objects are ready for malicious encryption.”


LockFile renames encrypted documents to lower case and adds a .lockfile file extension, and also includes an HTML Application (HTA) ransom note looks very similar to that of LockBit 2.0, researchers said.


“In its ransom note, the LockFile adversary asks victims to contact a specific e-mail address: contact[@]contipauper.com,” they said, adding that the domain name—which seems to have been created on Aug. 16–appears to be a “derogatory reference” to the [Conti Gang](https://threatpost.com/affiliate-leaks-conti-ransomware-playbook/168442/), a still-active and competing ransomware group.


**Intermittent Encryption, Explained**
--------------------------------------


The feature that most defines and differentiates LockFile from its competitors is not that it implements partial encryption per se — as [LockBit 2.0](https://threatpost.com/lockbit-bangkok-airways-breach/169019/), DarkSide and [BlackMatter](https://threatpost.com/ransomware-gangs-haron-blackmatter/168212/) ransomware all do this, according to researchers. What sets LockFile apart is the unique way it employs this type of encryption, which has not been observed by a ransomware before, Loman said.


“What sets LockFile apart is that it doesn’t encrypt the first few blocks,” he wrote. “Instead, LockFile encrypts every other 16 bytes of a document. This means that a text document, for instance, remains partially readable.”


The “intriguing advantage” to this approach is that it can elude some ransomware protection technologies that use what’s called “chi-squared (chi^2)” analysis, skewing the statistical way this analysis is done and thus confusing it.


“An unencrypted text file of 481 KB (say, a book) has a chi^2 score of 3850061,” Loman explained. “If the document was encrypted by [DarkSide](https://threatpost.com/darksides-servers-shutdown/166187/) ransomware, it would have a chi^2 score of 334 – which is a clear indication that the document has been encrypted. If the same document is encrypted by LockFile ransomware, it would still have a significantly high chi^2 score of 1789811.”


Once it has encrypted all the documents on the machine, LockFile disappears without a trace, deleting itself with a PING command, researchers said. “This means that after the ransomware attack, there is no ransomware binary for incident responders or antivirus software to find or clean up,” they wrote.




#### Tags:
[[ransomware]] [[LockFile]] [[said.]] [[wrote.]] [[explained.]] [[ransomware,]] [[Loman]] [[section,]] [[chi^2]] [[ThreatPost]]
