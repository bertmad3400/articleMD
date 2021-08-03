# ‘DeadRinger’ Targeted Exchange Servers Long Before Discovery
### Cyberespionage campaigns linked to China attacked telecoms via ProxyLogon bugs, stealing call records and maintaining persistence, as far back as 2017.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168300)
+ Date: August 3, 2021  10:55 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/03104933/telecoms-e1628002187766.jpeg)
Threat actors linked to China exploited the notorious Microsoft Exchange [ProxyLogon](https://threatpost.com/attackers-target-proxylogon-cryptojacker/165418/) vulnerabilities long before they were publicly disclosed, in attacks against telecommunications companies aimed at stealing sensitive customer data and maintaining network persistence, researchers have found.


Researchers from Cybereason have been tracking multiple cyberespionage campaigns – collectively dubbed “DeadRinger” – since 2017, [reporting initially](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers) on findings that a Chinese threat group dubbed SoftCell was targeting billing servers to steal call records from telecoms in Africa, the Middle East, Europe and Asia in 2019.


A [report released Tuesday](https://www.cybereason.com/blog/deadringer-exposing-chinese-threat-actors-targeting-major-telcos) builds upon this research, identifying two new threat groups – Naikon APT and Group-3390 – that also appear to be working for China’s regime to compromise billing servers to steal telco call records as well as maintain persistent access to their networks through other core components, according to the report.



The report also discloses that SoftCell targeted a set of Microsoft Exchange vulnerabilities collectively known as ProxyLogon “long before they became publicly known,” researchers wrote. These vulnerabilities [spurred a frenzy of attacks](https://threatpost.com/microsoft-exchange-cyberattacks-one-click-fix/164817/) earlier this year before Microsoft mitigations and patches began to [take effect](https://threatpost.com/microsoft-exchange-servers-proxylogon-patching/165001/).


Indeed, threat actors used similar tactics to those exposed recently in [the Hafnium zero-day attacks](https://threatpost.com/hades-ransomware-connections-hafnium/165069/) – which were recently blamed on China and [condemned](https://www.nytimes.com/2021/07/19/us/politics/microsoft-hacking-china-biden.html) by the White House – that exploited ProxyLogon vulnerabilities in Microsoft Exchange Servers to gain access to the targeted networks, according to the report.


Overall, the attacks show an aggressive assault by China on the security of critical infrastructure that – similarly to the [SolarWinds](https://threatpost.com/solarwinds-hack-linked-turla-apt/162918/) and [Kaseya](https://threatpost.com/kaseya-patches-zero-days-revil-attacks/167670/) attacks – compromise third-party service providers to ultimately attack their customers while undermining those trust relationships and causing other collateral damage, Cybereason CEO and co-founder Lior Div said.


“These state-sponsored espionage operations not only negatively impact the telecoms’ customers and business partners, they also have the potential to threaten the national security of countries in the region and those who have a vested interest in the region’s stability,” he said in a press statement.


**Related Yet Separate Attacks**
--------------------------------


Specifically, researchers have identified three clusters of attacks that show a common agenda but use different tactics as a means to accomplish it. Overall, the attackers are “highly adaptive” and have been successful at obscuring their activity to maintain persistence on victims’ networks, with some having managed to evade detection since 2017, researchers said.


Dubbed Cluster A, the SoftCell attacks on telecoms in multiple regions – including Southeast Asia – started in 2018 and continued through the first quarter of this year. These attackers leverage Microsoft Exchange vulnerabilities to install the ChinaChopper Webshell and gain a foothold using the PcShare backdoor. Attackers then use various tools to perform reconnaissance, move laterally on the network, and steal credentials and data.


Naikon APT, a cyber espionage group attributed to the [Chinese People’s Liberation Army’s](https://en.wikipedia.org/wiki/People%27s_Liberation_Army) (PLA) Chengdu Military Region Second Technical Reconnaissance Bureau (Military Unit Cover Designator 78020 [[PDF](https://cdn2.hubspot.net/hubfs/454298/Project_CAMERASHY_ThreatConnect_Copyright_2015.pdf)]), is behind the Cluster B attacks, researchers said. These attacks have been targeting telcom companies in Southeast Asia since late last year and continued through the first quarter of 2021.


Researchers still don’t know how Naikon APT initially compromises its targeted networks, but have observed the group using the Nebulae backdoor and other tools to perform similar activities to SoftCell once attackers gain a foothold.


The Cluster C attacks are actually a “mini-cluster” that began in 2017, continued through Q1 2021 and are related to SoftCell activity, researchers said. However, they also might be the work of Chinese APT Group-3390, given the use of a “unique OWA (Outlook Web Access) backdoor” deployed across multiple Microsoft Exchange and IIS servers in the attacks.


“The backdoor was used to harvest credentials of users logging into Microsoft OWA services, granting the attackers the ability to access the environment stealthily,” researchers wrote.


Researchers’ analysis of the backdoor “shows significant code similarities with a previously documented backdoor observed being used in the operation dubbed Iron Tiger,” which was attributed to Group-3390, they added.


Overall, overlaps throughout the three clusters “are evidence of a likely connection between the threat actors” indicating that “each group was tasked with parallel objectives in monitoring the communications of specific high-value targets” by central command “aligned with Chinese state interests,” researchers concluded.


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[Microsoft]] [[SoftCell]] [[said.]] [[ProxyLogon]] [[Naikon]] [[networks,]] [[Overall,]] [[ThreatPost]]
