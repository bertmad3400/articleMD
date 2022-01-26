# German govt warns of APT27 hackers backdooring business networks
### The BfV German domestic intelligence services (short for Bun­des­amt für Ver­fas­sungs­schutz) warn of ongoing attacks coordinated by the APT27 Chinese-backed hacking group.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/german-govt-warns-of-apt27-hackers-backdooring-business-networks/
+ Date: 2022-01-26T08:00:00-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/11/08/China_hacker.jpg)

![China APT27 hackers](https://www.bleepstatic.com/content/hl-images/2021/11/08/China_hacker.jpg)


The BfV German domestic intelligence services (short for Bun­des­amt für Ver­fas­sungs­schutz) warn of ongoing attacks coordinated by the APT27 Chinese-backed hacking group.


This active campaign is targeting German commercial organizations, with the attackers using the HyperBro remote access trojans (RAT) to backdoor their networks.


[HyperBro](https://malpedia.caad.fkie.fraunhofer.de/details/win.hyperbro) helps the threat actors maintain persistence on the victims' networks by acting as an in-memory backdoor with remote administration capabilities.


The agency said the threat group's goal is to steal sensitive information and may also attempt to target their victims' customers in supply chain attacks.


"The Federal Office for the Protection of the Constitution (BfV) has information about an ongoing cyber espionage campaign by the cyber attack group APT27 using the malware variant HYPERBRO against German commercial companies," the BfV [said](https://www.verfassungsschutz.de/SharedDocs/kurzmeldungen/DE/2022/2022-01-26-cyberbrief.html).


"It cannot be ruled out that the actors, in addition to stealing business secrets and intellectual property, also try to infiltrate the networks of (corporate) customers or service providers (supply chain attack)."


The BfV also published [indicators of compromise (IOCs) and YARA rules](https://www.verfassungsschutz.de/SharedDocs/publikationen/DE/cyberabwehr/2022-01-bfv-cyber-brief.pdf) to help targeted German organizations to check for HyperBro infections and connections to APT27 command-and-control (C2) servers.



![HyperBro infection chain](https://www.bleepstatic.com/images/news/u/1109292/2022/HyperBro_infection_chain.jpg)*HyperBro infection chain (BfV)*
Breaching networks via Zoho and Exchange servers
------------------------------------------------


[APT27](https://attack.mitre.org/groups/G0027/) (also tracked as TG-3390, Emissary Panda, BRONZE UNION, Iron Tiger, and LuckyMouse) is a Chinese-sponsored threat group active since at least 2010 and known for its focus on information theft and cyberespionage campaigns.


The German intelligence agency says APT27 has been exploiting flaws in Zoho AdSelf Service Plus software, an enterprise password management solution for Active Directory and cloud apps, since March 2021.


This aligns with previous reports of Zoho ManageEngine installations being the target of multiple campaigns in 2021, coordinated by nation-state hackers using tactics and tooling similar to those employed by APT27.


They first used an [ADSelfService zero-day exploi](https://www.bleepingcomputer.com/news/security/fbi-and-cisa-warn-of-state-hackers-exploiting-critical-zoho-bug/)t until mid-September, then switched to an [n-day AdSelfService exploit](https://www.bleepingcomputer.com/news/security/state-hackers-breach-defense-energy-healthcare-orgs-worldwide/), and started exploiting [a ServiceDesk bug beginning with October 25](https://www.bleepingcomputer.com/news/security/hackers-use-in-house-zoho-servicedesk-exploit-to-drop-webshells/).



![Zoho ManageEngine campaigns](https://www.bleepstatic.com/images/news/u/1109292/2021/Zoho%20ManageEngine%20exploitation.png)*Zoho ManageEngine campaigns (Unit 42)*
In these attacks, they successfully [compromised at least nine organizations from critical sectors worldwide](https://www.bleepingcomputer.com/news/security/state-hackers-breach-defense-energy-healthcare-orgs-worldwide/), including defense, healthcare, energy, technology, and education, according to Palo Alto Networks researchers.


In light of these campaigns, the FBI and CISA issued joint advisories ([1](https://us-cert.cisa.gov/ncas/alerts/aa21-259a), [2](https://us-cert.cisa.gov/ncas/alerts/aa21-336a)) warning of APT actors exploiting ManageEngine flaws to drop web shells on the networks of breached critical infrastructure orgs.


APT27 and other Chinese-backed hacking groups were also [linked to attacks exploiting critical ProxyLogon bugs](https://www.bleepingcomputer.com/news/security/state-hackers-rush-to-exploit-unpatched-microsoft-exchange-servers/) in early March 2021 that allowed them to take over and steal data from unpatched Microsoft Exchange servers worldwide.


US and allies (the European Union, the United Kingdom, and NATO) [officially blamed China in June](https://www.bleepingcomputer.com/news/security/us-and-allies-officially-accuse-china-of-microsoft-exchange-attacks/) for last year's widespread Microsoft Exchange hacking campaign.





## Tags:

#### Threatactor:
[[threatactor.name=Putter Panda]] [[threatactor.name=Threat Group-3390]] [[threatactor.name=Threat Group-3390]] [[threatactor.name=Threat Group-3390]] [[threatactor.name=Threat Group-3390]] [[threatactor.name=Threat Group-3390]] [[threatactor.name=Threat Group-3390]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Emissary]] [[action.malware.name=HyperBro]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Healthcare]]

#### Location:
[[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=United Kingdom]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Apt27]] [[Hyperbro]] [[Zoho]] [[Bfv]] [[Manageengine]] [[Bleeping Computer]]

