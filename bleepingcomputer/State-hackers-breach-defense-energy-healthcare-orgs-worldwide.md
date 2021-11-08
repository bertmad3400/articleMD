# State hackers breach defense, energy, healthcare orgs worldwide
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/state-hackers-breach-defense-energy-healthcare-orgs-worldwide/)
+ Date: November 8, 2021
+ Author: Sergiu Gatlan


## Article:
![State hackers breach defense, energy, healthcare orgs worldwide](https://www.bleepstatic.com/content/hl-images/2021/11/08/China_hacker.jpg)


Cybersecurity firm Palo Alto Networks warned over the weekend of an ongoing hacking campaign that has already resulted in the compromise of at least nine organizations worldwide from critical sectors, including defense, healthcare, energy, technology, and education.


To breach the orgs networks, the threat actors behind this cyberespionage campaign exploited a critical vulnerability ([CVE-2021-40539](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-40539)) in Zoho's enterprise password management solution known as ManageEngine ADSelfService Plus which allows remotely executing code on unpatched systems without authentication.


The attacks observed by Palo Alto Networks researchers started on September 17 with scans for vulnerable servers, nine days after the US Cybersecurity and Infrastructure Security Agency (CISA) [warned it detected exploits used in the wild](https://www.bleepingcomputer.com/news/security/zoho-patches-actively-exploited-critical-adselfservice-plus-bug/) and one day after a [joint advisory was published](https://us-cert.cisa.gov/ncas/alerts/aa21-259a) by CISA, the FBI, and the United States Coast Guard Cyber Command (CGCYBER).


Exploitation attempts began on September 22 after five days of harvesting info on potential targets who hadn't yet patched their systems.


"While we lack insight into the totality of organizations that were exploited during this campaign, we believe that, globally, at least nine entities across the technology, defense, healthcare, energy and education industries were compromised," [the researchers said](https://unit42.paloaltonetworks.com/manageengine-godzilla-nglite-kdcsponge/).


"Through global telemetry, we believe that the actor targeted at least 370 Zoho ManageEngine servers in the United States alone. Given the scale, we assess that these scans were largely indiscriminate in nature as targets ranged from education to Department of Defense entities."


Following the joint advisory, the researchers observed another series of unrelated attacks that failed to compromise their targets, hinting at other state-backed or financially-motivated hacking groups likely joining in to exploit companies using Zoho servers.


Targets on credentials, persistence
-----------------------------------


After successfully getting a foothold on their victims' systems using CVE-2021-40539 exploits, the threat actors first deployed a malware dropper that delivered Godzilla web shells on compromised servers to gain and maintain access to the victims' networks, as well as malware, including an open-source backdoor known as NGLite.


They also used KdcSponge, malware known as credential stealer, which hooks into Windows LSASS API functions to capture credentials (i.e., domain names, usernames, and passwords) that later get sent to attacker-controlled servers.


"After gaining access to the initial server, the actors focused their efforts on gathering and exfiltrating sensitive information from local domain controllers, such as the Active Directory database file (ntds.dit) and the SYSTEM hive from the registry," the researchers found.


"Ultimately, the actor was interested in stealing credentials, maintaining access and gathering sensitive files from victim networks for exfiltration."


Attacks linked to Chinese APT27 state hackers
---------------------------------------------


Even though the researchers are working on attributing these attacks to a specific hacking group, they suspect that this is the work of a Chinese-sponsored threat group known as [APT27](https://attack.mitre.org/groups/G0027/) (also tracked as TG-3390, Emissary Panda, BRONZE UNION, Iron Tiger, and LuckyMouse).


The partial attribution is based on malicious tools and tactics used in this campaign that match APT27's previous activity as a hacking group active since at least 2010 and targeting the same range of industry sectors (e.g., defense, technology, energy, aerospace, government, and manufacturing) in cyber espionage campaigns.


Palo Alto Networks' report also includes analysis from US Government partners, including NSA's Cybersecurity Collaboration Center, a component designed to prevent and block foreign cyber threats to National Security Systems (NSS), the Department of Defense, and the Defense Industrial Base (DIB) with the help of private industry partners.


In early March, [APT27 was also linked to attacks](https://www.bleepingcomputer.com/news/security/state-hackers-rush-to-exploit-unpatched-microsoft-exchange-servers/) exploiting critical bugs (dubbed ProxyLogon) to achieve remote code execution without authentication on unpatched on-premises Microsoft Exchange servers worldwide.


US and allies, including the European Union, the United Kingdom, and NATO, [officially blamed China in June](https://www.bleepingcomputer.com/news/security/us-and-allies-officially-accuse-china-of-microsoft-exchange-attacks/) for this year's widespread Microsoft Exchange hacking campaign.




#### Tags:
[[APT27]] [[Cybersecurity]] [[Palo]] [[defense,]] [[technology,]] [[Zoho]] [[Bleeping Computer]]
