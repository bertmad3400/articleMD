# Conti ransomware uses Log4j bug to hack VMware vCenter servers
### Conti ransomware operation is using the critical Log4Shell exploit to gain rapid access to internal VMware vCenter Server instances and encrypt virtual machines.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/conti-ransomware-uses-log4j-bug-to-hack-vmware-vcenter-servers/
+ Date: 2021-12-17T10:00:00-05:00
+ Author: Ionut Ilascu


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j_logo.jpg)

![Conti ransomware uses Log4j bug to hack VMware vCenter servers](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j_logo.jpg)


Conti ransomware operation is using the critical Log4Shell exploit to gain rapid access to internal VMware vCenter Server instances and encrypt virtual machines.


The gang did not waste much time adopting the new attack vector and is the first "top-tier" operation known to weaponize the Log4j vulnerability.


### Vulnerable vCenter in the crosshair


A proof-of-concept (PoC) [exploit for CVE-2021-44228](https://www.bleepingcomputer.com/news/security/new-zero-day-exploit-for-log4j-java-library-is-an-enterprise-nightmare/) — otherwise known as Log4Shell — emerged in the public space on December 9.


A day later, mass scanning of the internet started, with multiple actors looking for vulnerable systems. Among the [first to leverage the bug](https://www.bleepingcomputer.com/news/security/hackers-start-pushing-malware-in-worldwide-log4shell-attacks/) were cryptocurrency miners, botnets, and a new ransomware strain called [Khonsari](https://www.bleepingcomputer.com/news/security/new-ransomware-now-being-deployed-in-log4shell-attacks/).


By December 15, the list of threat actors using Log4Shell expanded to state-backed hackers and initial access brokers that typically sell network access to ransomware gangs.


Conti, one of the largest and most prolific ransomware gangs today with tens of active full-time members, appears to have taken interest in Log4Shell early on, seeing it as a possible attack avenue on Sunday, December 12.


The gang started looking for new victims the next day their goal being lateral movement to VMware vCenter networks, cybercrime and adversarial disruption company Advanced Intelligence ([AdvIntel](https://www.advintel.io/)) shared with BleepingComputer.


Dozens of vendors have been affected by Log4Shell and rushed to patch their products or provide workarounds and mitigations for customers. [VMware is one of them](https://www.bleepingcomputer.com/news/security/log4j-list-of-vulnerable-products-and-vendor-advisories/#:~:text=Cloud%20App%20Security.-,VMware,-%3A), listing 40 vulnerable products.


While the company provided mitigations or fixes, a patch for vCenter versions impacted has yet to become available.


vCenter servers are not normally exposed to the public internet, there are scenarios where an attacker could exploit the issue:



“A malicious actor with network access to an impacted VMware product may exploit this issue to gain full control of the target system and/or perform a denial of service attack” - [VMware](https://www.vmware.com/security/advisories/VMSA-2021-0028.html)



AdvIntel says that Conti ransomware gang members showed interest in leveraging Log4Shell for their operations using the public exploit.


### Log4Shell to move laterally


In a report shared with BleepingComputer, the company notes that “this is the first time this vulnerability entered the radar of a major ransomware group.”



“The current exploitation led to multiple use cases through which the Conti group tested the possibilities of utilizing the Log4J exploit” - [AdvIntel](https://www.advintel.io/post/ransomware-advisory-log4shell-exploitation-for-initial-access-lateral-movement)



While most defenders are focused on blocking Log4Shell attacks on Internet-exposed devices, the Conti ransomware operation shows how the vulnerability can be used to target internal devices that may not receive as much attention.



![Conti ransomware's use of Log4Shell exploit to access vCenter servers](https://www.bleepstatic.com/images/news/u/1100723/Ransomware/Conti/lateral-movement-to-vcenter.jpg)source: AdvIntel
The researchers confirmed that Conti ransomware affiliates had already compromised the target networks and exploited vulnerable Log4j machines to gain access to vCenter servers.


This means that Conti ransomware members relied on a different initial access vector (RDP, VPN, email phishing) to compromise a network and are currently using Log4Shell to move laterally on the network.



![Initial access vectors used by Conti ransomware](https://www.bleepstatic.com/images/news/u/1100723/Ransomware/Conti/ContiInitialAccess.jpg)source: AdvIntel
Conti is a Russian-speaking group that has been in the ransomware game for a long time, being the successor of the infamous Ryuk.


The gang is responsible for hundreds of attacks, its data leak site alone listing more than 600 victim companies that did not pay a ransom. To these are added other businesses that paid the actor to have their data decrypted.


Cybersecurity company [Group-IB estimates](https://www.group-ib.com/resources/threat-research/2021-reports.html?utm_source=blog_post&utm_campaign=htct-reports-2021-en&utm_medium=organic&utm_content=corporansom) that about 30% of the ransomware victims choose to pay to restore their files using the attacker’s decryption tool.


Recently, the Australian Cyber Security Centre (ACSC) published an [alert about Conti ransomware](https://www.bleepingcomputer.com/news/security/australian-govt-raises-alarm-over-conti-ransomware-attacks/) targeting multiple organizations in the country. One of the victims was electricity provider CS Energy.


Frontier Software, a payroll software provider used by the Australian government, was also [hit by Conti](https://www.bleepingcomputer.com/news/security/data-breach-impacts-80-000-south-australian-govt-employees/), the breach leading to exposing the data of tens of thousands of government employees.


More recently, [BleepingComputer learned](https://www.bleepingcomputer.com/news/security/mcmenamins-breweries-hit-by-a-conti-ransomware-attack/) that the gang hit McMenamins, a brewery and hotel chain in Oregon (Portland) and Washington, U.S.


Conti ransomware has been operating under this name since June 2020. According to info from AdvIntel, the group has extorted more than $150 million from its victims over the past six months.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Expand]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Ryuk]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=Washington, D.C.]] [[victim.country.name=Navassa Island]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Australia]] [[victim.continent.name=Oceania]] [[victim.country.name=Australia]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Ransomware]] [[Conti]] [[Log4shell]] [[Vcenter]] [[Vmware]] [[Advintel]] [[Bleepingcomputer]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-44228]]

