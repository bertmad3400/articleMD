# Microsoft Exchange servers being hacked by new LockFile ransomware
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/microsoft-exchange-servers-being-hacked-by-new-lockfile-ransomware/)
+ Date: August 21, 2021
+ Author: Lawrence Abrams


## Article:
![Exchange Ransomware](https://www.bleepstatic.com/content/hl-images/2021/03/11/ransomware-exchange-header.jpg)


A new ransomware gang known as LockFile encrypts Windows domains after hacking into Microsoft Exchange servers using the recently disclosed ProxyShell vulnerabilities.


ProxyShell is the name of an attack consisting of three chained Microsoft Exchange vulnerabilities that result in unauthenticated, remote code execution.



The three vulnerabilities were discovered by Devcore Principal Security Researcher [Orange Tsai](https://twitter.com/orange_8361), who chained them together to take over a Microsoft Exchange server in April's [Pwn2Own 2021 hacking contest](https://www.bleepingcomputer.com/news/security/researchers-earn-1-2-million-for-exploits-demoed-at-pwn2own-2021/).


* [CVE-2021-34473](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34473) - Pre-auth Path Confusion leads to ACL Bypass *(Patched in April by [KB5001779](https://support.microsoft.com/en-us/topic/description-of-the-security-update-for-microsoft-exchange-server-2019-2016-and-2013-april-13-2021-kb5001779-8e08f3b3-fc7b-466c-bbb7-5d5aa16ef064)**)*
* [CVE-2021-34523](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34523) - Elevation of Privilege on Exchange PowerShell Backend *(Patched in April by [KB5001779](https://support.microsoft.com/en-us/topic/description-of-the-security-update-for-microsoft-exchange-server-2019-2016-and-2013-april-13-2021-kb5001779-8e08f3b3-fc7b-466c-bbb7-5d5aa16ef064))*
* [CVE-2021-31207](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-31207) - Post-auth Arbitrary-File-Write leads to RCE *(Patched in May by [KB5003435](https://support.microsoft.com/en-us/topic/description-of-the-security-update-for-microsoft-exchange-server-2019-2016-and-2013-may-11-2021-kb5003435-028bd051-b2f1-4310-8f35-c41c9ce5a2f1)**)*


While Microsoft fully patched these vulnerabilities in May 2021, more technical details were recently disclosed, allowing security researchers and threat actors to [reproduce the exploit](https://peterjson.medium.com/reproducing-the-proxyshell-pwn2own-exploit-49743a4ea9a1).


As reported last week by BleepingComputer, this has led to threat actors actively scanning for and [hacking Microsoft Exchange servers using the ProxyShell vulnerabilities](https://www.bleepingcomputer.com/news/microsoft/microsoft-exchange-servers-are-getting-hacked-via-proxyshell-exploits/).


After exploiting an Exchange server, the threat actors dropped web shells that could be used to upload other programs and execute them.


At the time, NCC Group's vulnerability researcher [Rich Warren](https://twitter.com/buffaloverflow) told BleepingComputer that the web shells were being used to install a .NET backdoor that was downloading a harmless payload at the time.


Since then, security researcher [Kevin Beaumont](https://twitter.com/GossiTheDog) [reports](https://doublepulsar.com/multiple-threat-actors-including-a-ransomware-gang-exploiting-exchange-proxyshell-vulnerabilities-c457b1655e9c) that a new ransomware operation known as LockFile uses the Microsoft Exchange ProxyShell and the [Windows PetitPotam vulnerabilities](https://www.bleepingcomputer.com/news/microsoft/new-petitpotam-attack-allows-take-over-of-windows-domains/) to take over Windows domains and encrypt devices.


When breaching a network, the threat actors will first access the on-premise Microsoft Exchange server using the ProxyShell vulnerabilities. Once they gain a foothold, Symantec says the [LockFile gang uses the PetitPotam vulnerability](https://www.bleepingcomputer.com/news/security/lockfile-ransomware-uses-petitpotam-attack-to-hijack-windows-domains/) to take over a domain controller, and thus the Windows domain.


From there, it is trivial to deploy the ransomware through the entire network.


What we know about the LockFile ransomware
------------------------------------------


At this time, there is not much known about the new LockFile ransomware operation.


When first seen in July, the ransom note was named '**LOCKFILE-README.hta**' but did not have any particular branding, as shown below.



![Old LockFile ransom notes](https://www.bleepstatic.com/images/news/ransomware/l/lockfile/microsoft-exchange-attacks/older-lockfile-note.jpg)**Old LockFile ransom notes**
Starting last week, BleepingComputer began receiving reports of a ransomware gang using branded ransom notes indicating that they were called 'LockFile,' as shown below


These ransom notes use a naming format of **'[victim\_name]-LOCKFILE-README.hta**' and prompted the victim to contact them via Tox or email to negotiate the ransom. The current email address used by the operation is *contact@contipauper.com*, which appears to be a reference to the Conti ransomware operation.


![LockFile](https://www.bleepstatic.com/images/news/u/1100723/Ransomware/LockFile/LockFileRansomNote.png)


While the color schemes of the ransom notes are similar, the communication methods and wording make it unclear if they are the same operation.


Of particular interest is that the color scheme and layout of the ransom notes is very similar to the LockBit ransomware, but there does not appear to be any relation.


When encrypting files, the ransomware will append the **.lockfile** extension to the encrypted file's names.


Yesterday afternoon, when BleepingComputer and ransomware expert [Michael Gillespie](https://twitter.com/demonslay335) analyzed the July version of LockFile, we found it to be a noisy ransomware, taking up many system resources and causing temporary freezes of the computer.


Patch now!
----------


As the LockFile operation uses both the Microsoft Exchange ProxyShell vulnerabilities and the Windows PetitPotam NTLM Relay vulnerability, it is imperative that Windows administrators install the latest updates.


For the ProxyShell vulnerabilities, you can install the [latest Microsoft Exchange cumulative updates](https://docs.microsoft.com/en-us/exchange/new-features/build-numbers-and-release-dates?view=exchserver-2019) to patch the vulnerabilities.


The Windows PetitPotam attack gets a bit complicated as Microsoft's security update is incomplete and does not patch all the vulnerability vectors.


To patch the PetitPotam attack, you can use an [unofficial patch from 0patch](https://www.bleepingcomputer.com/news/security/new-unofficial-windows-patch-fixes-more-petitpotam-attack-vectors/) to block this NTLM relay attack vector or [apply NETSH RPC filters](https://www.bleepingcomputer.com/news/microsoft/windows-petitpotam-attacks-can-be-blocked-using-new-method/) that block access to vulnerable functions in the MS-EFSRPC API.


Beaumont says you can perform the following Azure Sentinel queries to check if your Microsoft Exchange server has been scanned for the ProxyShell vulnerability.


All organizations are strongly advised to apply the patches as soon as possible and create offline backups of their Exchange servers.




#### Tags:
[[Microsoft]] [[ransomware]] [[ProxyShell]] [[LockFile]] [[Windows]] [[PetitPotam]] [[vulnerabilities.]] [[(Patched]] [[BleepingComputer]] [[operation.]] [[Bleeping Computer]]
