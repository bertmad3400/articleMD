# New Atom Silo ransomware targets vulnerable Confluence servers
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-atom-silo-ransomware-targets-vulnerable-confluence-servers/)
+ Date: October 4, 2021
+ Author: Sergiu Gatlan


## Article:
![New Atom Silo ransomware targets vulnerable Confluence servers](https://www.bleepstatic.com/content/hl-images/2021/10/04/Target_dart.jpg)


*Image: [Silvan Arnet](https://unsplash.com/@silvanarnet)*


Atom Silo, a newly spotted ransomware group, is targeting a recently patched and actively exploited Confluence Server and Data Center vulnerability to deploy their ransomware payloads.


Atlassian Confluence is a highly popular web-based corporate team workspace that helps employees collaborate on various projects.


On August 25, Atlassian [issued security updates](http://confluence.atlassian.com/doc/confluence-security-advisory-2021-08-25-1077906215.html) to patch a Confluence remote code execution (RCE) vulnerability tracked as CVE-2021-26084 and exploited in the wild.


Successful exploitation enables unauthenticated attackers to execute commands on unpatched servers remotely.


Ransomware gangs start targeting Confluence servers
---------------------------------------------------


The discovery was made by SophosLabs researchers while investigating a recent incident. They also found that the ransomware used by this new group is almost identical to [LockFile](https://www.bleepingcomputer.com/tag/lockfile/), which is itself [very similar](https://www.bleepingcomputer.com/news/security/lockfile-ransomware-uses-petitpotam-attack-to-hijack-windows-domains/) to the one used by the [LockBit](https://www.bleepingcomputer.com/tag/LockBit/) ransomware group.


However, Atom Silo operators use "several novel techniques that made it extremely difficult to investigate, including the side-loading of malicious dynamic-link libraries tailored to disrupt endpoint protection software."


After compromising Confluence servers and installing a backdoor, the threat actors drop a second-stage stealthier backdoor using DLL side-loading to launch it on the breached system.


Ransomware payloads deployed by Atom Silo also come with a malicious kernel driver used to disrupt endpoint protection solutions and evade detection.


"The incident investigated by Sophos shows how quickly the ransomware landscape can evolve. This ultra-stealthy adversary was unknown until a few weeks ago," [said](https://news.sophos.com/en-us/2021/10/04/atom-silo-ransomware-actors-use-confluence-exploit-dll-side-load-for-stealthy-attack/) Sean Gallagher, a senior threat researcher at Sophos.


"While similar to another recently discovered ransomware group, LockFile, Atom Silo has emerged with its own bag of novel and sophisticated tactics, techniques and procedures that were full of twists and turns and challenging to spot – probably intentionally so.


"In addition, Atom Silo made significant efforts to evade detection prior to launching the ransomware, which included well-worn techniques used in new ways. Other than the backdoors themselves, the attackers used only native Windows tools and resources to move within the network until they deployed the ransomware."


Further technical details on Atom Silo's compromise and lateral movement tactics can be found in [SophosLabs' report](https://news.sophos.com/en-us/2021/10/04/atom-silo-ransomware-actors-use-confluence-exploit-dll-side-load-for-stealthy-attack/).



![Atom Silo ransom note](https://www.bleepstatic.com/images/news/u/1109292/2021/atomsilo-ransom-note.webp)*Atom Silo ransom note (SophosLabs)*
Heavily exploited Confluence vulnerability
------------------------------------------


As BleepingComputer [reported at the start of September](https://www.bleepingcomputer.com/news/security/atlassian-confluence-flaw-actively-exploited-to-install-cryptominers/), multiple threat actors began scanning for and exploiting the recently disclosed CVE-2021-26084 Confluence RCE vulnerability to install crypto miners once a PoC exploit was released six days after Atlassian's patches were issued.


BleepingComputer confirmed that the [attackers were installing crypto miners](https://www.bleepingcomputer.com/news/security/atlassian-confluence-flaw-actively-exploited-to-install-cryptominers/) (e.g., XMRig Monero cryptocurrency miners) on Windows and Linux Confluence servers.


U.S. Cyber Command (USCYBERCOM) issued a rare alert in early September to urge U.S. organizations to patch the critical Atlassian Confluence vulnerability immediately as it was already under massive exploitation.


The USCYBERCOM unit also stressed the importance of patching all vulnerable Confluence servers as soon as possible: "Please patch immediately if you haven't already— this cannot wait until after the weekend."




> 
> [#ActionRequired](https://twitter.com/hashtag/ActionRequired?src=hash&ref_src=twsrc%5Etfw) patch immediately! <https://t.co/b6eAYdFuW4>
> 
> 
> — U.S. Cyber Command (@US\_CYBERCOM) [September 3, 2021](https://twitter.com/US_CYBERCOM/status/1433810876847493134?ref_src=twsrc%5Etfw)


CISA also warned admins to apply the [Confluence security updates](https://us-cert.cisa.gov/ncas/current-activity/2021/09/03/atlassian-releases-security-updates-confluence-server-and-data) recently issued by Atlassian immediately.


As BleepingComputer cautioned at the time, although these attackers were only deploying cryptocurrency miners, they could quickly escalate to ransomware payloads and data exfiltration once the threat actors started moving laterally through corporate networks from hacked on-prem Confluence servers.


"This incident is also a good reminder how dangerous publicly disclosed security vulnerabilities in internet-facing software are when left unpatched, even for a relatively short time," Gallagher added.


"In this case, the vulnerability opened the door to two simultaneous, but unrelated attacks from ransomware and a crypto-miner."




#### Tags:
[[ransomware]] [[Atlassian]] [[BleepingComputer]] [[U.S.]] [[Bleeping Computer]]
