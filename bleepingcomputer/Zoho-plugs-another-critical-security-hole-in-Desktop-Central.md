# Zoho plugs another critical security hole in Desktop Central
### Zoho has addressed a new critical severity vulnerability found to affect the company's Desktop Central and Desktop Central MSP  unified endpoint management (UEM) solutions.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/zoho-plugs-another-critical-security-hole-in-desktop-central/
+ Date: 2022-01-17T13:04:18-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/17/Zoho.jpg)

![Zoho patches new critical authentication bypass in Desktop Central](https://www.bleepstatic.com/content/hl-images/2022/01/17/Zoho.jpg)


Zoho has addressed a new critical severity vulnerability that affects the company's Desktop Central and Desktop Central MSP unified endpoint management (UEM) solutions.


ManageEngine Desktop Central is an endpoint management platform that allows admins to deploy patches and software over the network and troubleshoot them remotely.


Zoho has fixed the security flaw tracked as [**CVE-2021-44757**](https://pitstop.manageengine.com/portal/en/community/topic/a-critical-security-patch-released-in-desktop-central-and-desktop-central-msp-for-cve-2021-44757-17-1-2022) today and is now providing mitigation with the latest released [Desktop Central](https://www.manageengine.com/products/desktop-central/cve-2021-44757.html) and [Desktop Central MSP](https://www.manageengine.com/desktop-management-msp/cve-2021-44757.html) versions (build Build: 10.1.2137.9).


"An authentication bypass vulnerability that can allow a remote user to perform unauthorized actions in the server," Zoho's ManageEngine Team [explained](https://pitstop.manageengine.com/portal/en/community/topic/a-critical-security-patch-released-in-desktop-central-and-desktop-central-msp-for-cve-2021-44757-17-1-2022) in a notification published today.


"If exploited, this vulnerability may allow an attacker to read unauthorized data or write an arbitrary zip file on the server."


The company also advised customers to follow its security hardening guidelines for [Desktop Central](https://www.manageengine.com/products/desktop-central/security-recommendations.html) and [Desktop Central MSP](https://www.manageengine.com/desktop-management-msp/security-recommendations.html).


Today, a Shodan search revealed [more than 2,800 ManageEngine Desktop Central instances](https://maps.shodan.io/#16.720385051693988/3.515625/3/satellite/http.title:%22manageengine%20desktop%20central%22) exposed to attacks over the Internet if not patched.



![Internet exposed Desktop Central servers CVE-2021-44757](https://www.bleepstatic.com/images/news/u/1109292/2022/Internet%20exposed%20Desktop%20Central%20servers%20CVE-2021-44757.jpg)*Internet-exposed Desktop Central servers (BleepingComputer)*
In early December, Zoho patched another critical vulnerability (CVE-2021-44515) that could allow threat actors to bypass authentication and execute arbitrary code on unpatched ManageEngine Desktop Central servers.


The Indian business software provider also warned at the time that it found evidence in the wild exploitation and urged customers to update as soon as possible to block incoming attacks.


In late December, the FBI's Cyber Division confirmed Zoho's ongoing exploitation alert by warning that multiple APT groups have been [exploiting the CVE-2021-44515 flaw](https://www.bleepingcomputer.com/news/security/fbi-state-hackers-exploiting-new-zoho-zero-day-since-october/) since at least late October 2021.


This is not the first time Zoho ManageEngine servers have been targeted in attacks recently. Desktop Central instances, in particular, have been hacked before and [access to compromised networks sold on hacking forums](https://www.bleepingcomputer.com/news/security/hackers-sell-access-to-your-network-via-remote-management-apps/) since at least July 2020.


Between August and October 2021, state hackers targeted Zoho ManageEngine products using tooling and tactics similar to ones observed in attacks coordinated by the APT27 Chinese-backed threat group.


Their attacks focused on and led to the breach of networks belonging to critical infrastructure organizations worldwide in three different campaigns using:


* [an ADSelfService zero-day exploi](https://www.bleepingcomputer.com/news/security/fbi-and-cisa-warn-of-state-hackers-exploiting-critical-zoho-bug/)t between early-August and mid-September,
* [an n-day AdSelfService exploit](https://www.bleepingcomputer.com/news/security/state-hackers-breach-defense-energy-healthcare-orgs-worldwide/) until late October,
* and [a ServiceDesk one starting with October 25](https://www.bleepingcomputer.com/news/security/hackers-use-in-house-zoho-servicedesk-exploit-to-drop-webshells/).

Following these series of attacks, CISA and the FBI issued joint advisories ([1](https://us-cert.cisa.gov/ncas/alerts/aa21-259a), [2](https://us-cert.cisa.gov/ncas/alerts/aa21-336a)) warning of state-backed hacking groups exploiting ManageEngine vulnerabilities to drop web shells on critical infrastructure orgs' networks from healthcare, financial services, electronics, and IT consulting industries.





## Tags:

#### Threatactor:
[[threatactor.name=Putter Panda]] [[threatactor.name=Threat Group-3390]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Healthcare]]

#### Location:
[[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Zoho]] [[Manageengine]] [[Msp]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-44757]] [[CVE-2021-44515]]

