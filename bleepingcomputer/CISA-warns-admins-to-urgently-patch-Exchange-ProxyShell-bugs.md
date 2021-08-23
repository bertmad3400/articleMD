# CISA warns admins to urgently patch Exchange ProxyShell bugs
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/cisa-warns-admins-to-urgently-patch-exchange-proxyshell-bugs/)
+ Date: August 23, 2021
+ Author: Sergiu Gatlan


## Article:
![CISA warns admins to urgently patch Exchange ProxyShell bugs](https://www.bleepstatic.com/content/hl-images/2021/08/23/Mircosoft-Exchange_headpic.jpg)


The US Cybersecurity and Infrastructure Security Agency (CISA) issued its first alert tagged as "urgent," warning admins to patch on-premises Microsoft Exchange servers against actively exploited ProxyShell vulnerabilities.


"Malicious cyber actors are actively exploiting the following ProxyShell vulnerabilities: CVE-2021-34473, CVE-2021-34523, and CVE-2021-31207," CISA [warned](https://us-cert.cisa.gov/ncas/current-activity/2021/08/21/urgent-protect-against-active-exploitation-proxyshell) over the weekend.


"CISA strongly urges organizations to identify vulnerable systems on their networks and immediately apply [Microsoft's Security Update from May 2021](https://us-cert.cisa.gov/ncas/current-activity/2021/05/11/microsoft-releases-may-2021-security-updates)—which remediates all three ProxyShell vulnerabilities—to protect against these attacks."


These three security flaws (patched in April and May) were discovered by Devcore security researcher [Orange Tsai](https://twitter.com/orange_8361), who used them to compromise a Microsoft Exchange server in April's [Pwn2Own 2021 hacking contest](https://www.bleepingcomputer.com/news/security/researchers-earn-1-2-million-for-exploits-demoed-at-pwn2own-2021/):


* [CVE-2021-34473](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34473) - Pre-auth path confusion leads to ACL Bypass *(Patched in April by [KB5001779](https://support.microsoft.com/en-us/topic/description-of-the-security-update-for-microsoft-exchange-server-2019-2016-and-2013-april-13-2021-kb5001779-8e08f3b3-fc7b-466c-bbb7-5d5aa16ef064))*
* [CVE-2021-34523](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34523) - Elevation of privilege on Exchange PowerShell backend *(Patched in April by [KB5001779](https://support.microsoft.com/en-us/topic/description-of-the-security-update-for-microsoft-exchange-server-2019-2016-and-2013-april-13-2021-kb5001779-8e08f3b3-fc7b-466c-bbb7-5d5aa16ef064))*
* [CVE-2021-31207](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-31207) - Post-auth Arbitrary-File-Write leads to RCE *(Patched in May by [KB5003435](https://support.microsoft.com/en-us/topic/description-of-the-security-update-for-microsoft-exchange-server-2019-2016-and-2013-may-11-2021-kb5003435-028bd051-b2f1-4310-8f35-c41c9ce5a2f1)**)*


Actively exploited by multiple threat actors
--------------------------------------------


This warning comes after [similar](https://www.bleepingcomputer.com/news/security/dhs-orders-agencies-to-urgently-patch-or-disconnect-exchange-servers/) [ones](https://www.bleepingcomputer.com/news/security/cisa-gives-federal-agencies-5-days-to-find-hacked-exchange-servers/) [alerting](https://www.bleepingcomputer.com/news/security/cisa-gives-federal-agencies-until-friday-to-patch-exchange-servers/) organizations to defend their networks from the wave of attacks that hit [tens of thousands of organizations worldwide](https://www.bleepingcomputer.com/news/security/us-and-allies-officially-accuse-china-of-microsoft-exchange-attacks/) in March, with exploits targeting four zero-day Microsoft Exchange bugs known as [ProxyLogon](https://www.bleepingcomputer.com/tag/proxylogon/).


Even though Microsoft fully patched the ProxyShell bugs in May 2021, they didn't assign CVE IDs for the three security vulnerabilities until July, thus preventing some organizations who had unpatched servers from discovering that they had vulnerable systems on their networks.


After additional technical details were recently disclosed, both security researchers and threat actors could [reproduce a working ProxyShell exploit](https://peterjson.medium.com/reproducing-the-proxyshell-pwn2own-exploit-49743a4ea9a1).


Then, just as it happened in March, attackers began [scanning for](https://www.bleepingcomputer.com/news/microsoft/microsoft-exchange-servers-scanned-for-proxyshell-vulnerability-patch-now/) and [hacking Microsoft Exchange servers using the ProxyShell vulnerabilities](https://www.bleepingcomputer.com/news/microsoft/microsoft-exchange-servers-are-getting-hacked-via-proxyshell-exploits/).


After breaching unpatched Exchange servers, threat actors drop web shells that allow them to upload and execute malicious tools.


While, in the beginning, the payloads were harmless, attackers have begun [deploying LockFile ransomware](https://www.bleepingcomputer.com/news/security/microsoft-exchange-servers-being-hacked-by-new-lockfile-ransomware/) payloads delivered across Windows domains compromised using [Windows PetitPotam exploits](https://www.bleepingcomputer.com/news/microsoft/new-petitpotam-attack-allows-take-over-of-windows-domains/).


So far, US-based security firm Huntress Labs [said](https://twitter.com/KyleHanslovan/status/1428804893423382532) it found over 140 web shells deployed by attackers on more than 1,900 compromised Microsoft Exchange servers until Friday.


Shodan is also tracking tracking ten of thousands of Exchange servers vulnerable to attacks using ProxyShell exploits, most of them located in the US and in Germany.




> 
> More than 18% of Exchange servers remain unpatched for the ProxyShell vulnerability. Nearly 40% are vulnerable to CVE-2021-31206: <https://t.co/7yetz9GoJw> [pic.twitter.com/0r2AOQsibB](https://t.co/0r2AOQsibB)
> 
> 
> — Shodan (@shodanhq) [August 11, 2021](https://twitter.com/shodanhq/status/1425508828246953989?ref_src=twsrc%5Etfw)


"New surge in Microsoft Exchange server exploitation underway," NSA Cybersecurity Director Rob Joyce also [warned](https://twitter.com/NSA_CSDirector/status/1429035182049333249) over the weekend. "You Must ensure you are patched and monitoring if you are hosting an instance."


The NSA has [also reminded defenders](https://twitter.com/NSACyber/status/1429073988957970441?s=20) this weekend that the [guidance published in March](https://twitter.com/NSACyber/status/1367887884917817351) on hunting for web shells is still applicable to these ongoing attacks.


Detailed information on how to identify Microsoft Exchange servers that need patching against ProxyShell and how to detect exploitation attempts can be found in [the blog post published by security researcher Kevin Beaumont](https://doublepulsar.com/multiple-threat-actors-including-a-ransomware-gang-exploiting-exchange-proxyshell-vulnerabilities-c457b1655e9c).




#### Tags:
[[Microsoft]] [[ProxyShell]] [[(Patched]] [[Bleeping Computer]]
