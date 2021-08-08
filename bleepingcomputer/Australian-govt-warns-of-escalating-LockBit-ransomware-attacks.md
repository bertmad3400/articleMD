# Australian govt warns of escalating LockBit ransomware attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/australian-govt-warns-of-escalating-lockbit-ransomware-attacks/)
+ Date: August 8, 2021
+ Author: Sergiu Gatlan


## Article:
![Australian govt warns of escalating LockBit ransomware attacks](https://www.bleepstatic.com/content/hl-images/2021/07/27/Lockbit-1.jpg)


The Australian Cyber Security Centre (ACSC) warns of an increase of LockBit 2.0 ransomware attacks against Australian organizations starting July 2021.


"ACSC has observed an increase in reporting of LockBit 2.0 ransomware incidents in Australia," Australia's cybersecurity agency said in a [security alert issued on Thursday](https://www.cyber.gov.au/acsc/view-all-content/alerts/lockbit-20-ransomware-incidents-australia).



According to the agency, LockBit victims also report threats of having data stolen during the attacks leaked online, a known and popular tactic among ransomware gangs to coerce their targets into paying the ransoms.


Increasing number of attacks since July
---------------------------------------


"The majority of victims known to the ACSC have been reported after July 2021, indicating a sharp and significant increase in domestic victims in comparison to other tracked ransomware variants," the ACSC [added](https://www.cyber.gov.au/acsc/view-all-content/advisories/2021-006-acsc-ransomware-profile-lockbit-20).


"The ACSC has observed LockBit affiliates successfully deploying ransomware on corporate systems in a variety of sectors including professional services, construction, manufacturing, retail and food."


The agency also published a [ransomware profile](https://www.cyber.gov.au/sites/default/files/2021-08/2021-006%20ACSC%20Ransomware%20Profile%20-%20Lockbit%202.0.pdf) with additional information on the LockBit group, including initial access indicators, targeted sectors, and mitigation measures.


It added that these threat actors are opportunistic and could target organizations from any industry sector. Therefore, not being included in the list of already targeted sectors does not necessarily indicate LockBit's target won't switch to other industries.


The ACSC provides [mitigations focused on LockBit TTPs](https://www.cyber.gov.au/sites/default/files/2021-08/2021-006%20ACSC%20Ransomware%20Profile%20-%20Lockbit%202.0.pdf) (Tactics, Techniques, and Procedures), which include:


* enabling multifactor authentication (MFA) on all accounts to block the use of stolen credentials
* encrypting sensitive data at rest to block exfiltration of sensitive information
* segmenting corporate networks and restricting admin privileges to block lateral movement and privilege escalation attempts
* maintaining daily backups to reduce a successful attack's impact
* patching internet facing Fortinet device against [CVE-2018-13379](https://www.bleepingcomputer.com/news/security/hacker-posts-exploits-for-over-49-000-vulnerable-fortinet-vpns/), a security bug heavily exploited by LockBit to breach networks


Organizations affected by these escalating ransomware attacks or who need assistance are advised to reach out using ACSC's *1300 CYBER1* hotline.


From LockBit to LockBit 2.0
---------------------------


The [LockBit ransomware](https://www.bleepingcomputer.com/tag/Lockbit/) gang started operating in September 2019 as a ransomware-as-a-service (RaaS), recruiting threat actors to breach networks and encrypt devices.


Since its launch, LockBit has been very active, with gang representatives promoting the RaaS and providing support on various Russian-language hacking forums.


LockBit announced [the LockBit 2.0 RaaS](https://twitter.com/Intel_by_KELA/status/1406905385580118017?s=20) in June 2021 on their data leak site after ransomware topics were banned on cybercrime forums [[1](https://www.bleepingcomputer.com/news/security/ransomware-ads-now-also-banned-on-exploit-cybercrime-forum/), [2](https://www.bleepingcomputer.com/news/security/popular-russian-hacking-forum-xss-bans-all-ransomware-topics/)].


While the alert issued by the Australian cybersecurity agency would imply that LockBit has hit never before seen levels of activity, the ransomware gang is just ramping up their engines again following a slowdown in attacks since January 2021, as shown by the number of ID Ransomware submissions.



![ID Ransomware LockBit submissions](https://www.bleepstatic.com/images/news/u/1109292/2021/ID%20Ransomware%20LockBit%20submissions.png)*LockBit submissions (ID Ransomware)*
This relaunch came together with redesigned Tor sites and advanced features, including the [automatic encryption of devices across Windows domains](https://www.bleepingcomputer.com/news/security/lockbit-ransomware-now-encrypts-windows-domains-using-group-policies/) using Active Directory group policies.


With LockBit 2.0, the gang is also [attempting to remove the middlemen](https://www.bleepingcomputer.com/news/security/lockbit-ransomware-recruiting-insiders-to-breach-corporate-networks/) by recruiting insiders who would provide them with access to corporate networks via Remote Desktop Protocol (RDP) and Virtual Private Network (VPN).


In related news, the ACSC and the FBI also warned in May of ongoing and [escalating Avaddon ransomware attacks](https://www.bleepingcomputer.com/news/security/us-and-australia-warn-of-escalating-avaddon-ransomware-attacks/) targeting organizations from an extensive array of sectors worldwide.


One month later, [the Avaddon ransomware gang shut down operations](https://www.bleepingcomputer.com/news/security/avaddon-ransomware-shuts-down-and-releases-decryption-keys/) and released decryption keys for their victims to BleepingComputer.




#### Tags:
[[LockBit]] [[ransomware]] [[ACSC]] [[Bleeping Computer]]
