# Meet Lyceum: Iranian hackers targeting telecoms, ISPs
### The criminals climb up communication chains with the aim of reaching executives.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/meet-lyceum-iranian-hackers-targeting-telecoms-isps/)
+ Date: November 9, 2021
+ Author: Charlie Osborne


## Article:
Unknown

Researchers have provided a deep dive into the activities of Lyceum, an Iranian threat group focused on infiltrating the networks of telecoms companies and internet service providers (ISPs). 


Lyceum, also known as Hexane, Siamesekitten, or Spirlin, has been active since 2017. The advanced persistent threat (APT) group has been linked to campaigns striking Middle Eastern oil and gas companies in the past and now appears to have expanded its focus to include the technology sector.

According to a report [published on Tuesday](https://www.accenture.com/us-en/blogs/cyber-defense/Iran-based-Lyceum-campaigns) by Accenture Cyber Threat Intelligence (ACTI) and Prevailion Adversarial Counterintelligence (PACT), between July and October this year, Lyceum was spotted in attacks against ISPs and telecoms organizations across Israel, Morocco, Tunisia, and Saudi Arabia.  

In addition, the APT is responsible for a campaign against an African ministry of foreign affairs.  

The cybersecurity teams say that several of the "identified compromises" remain active at the time of publication.  

Lyceum's initial attack vectors include credential stuffing attacks and brute-force attacks. According to [Secureworks](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign), individual accounts at companies of interest are usually targeted -- and then once these accounts are breached, they are used as a springboard to launch spear phishing attacks against high-profile executives in an organization. 

The APT appears to be focused on cyberespionage. The report suggests that not only do these attackers seek out data on subscribers and connected third-party companies, but once compromised, "these industries can also be used by threat actors or their sponsors to surveil individuals of interest." 






Lyceum will attempt to deploy two different kinds of malware: Shark and Milan (known together as James). Both are backdoors; Shark, a 32-bit executable written in C# and .NET, generates a configuration file for DNS tunneling or HTTP C2 communications, whereas Milan -- a 32-bit Remote Access Trojan (RAT) retrieves data. Both are able to communicate with the groups' command-and-control (C2) servers.  

The APT maintains a C2 server network that connects to the group's backdoors, made up of over 20 domains, including six that were previously not connected with the threat actors.  

The backdoor malware families have previously been disclosed by [ClearSky](https://www.clearskysec.com/siamesekitten/) and [Kasperksy](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf) (.PDF). 

Recently, the ACTI/PACT researchers found a new backdoor similar to newer versions of Milan which sent beacons linked to potential attacks against a Tunisian telecoms company and a government agency in Africa. 

"It is unknown if the Milan backdoor beacons are coming from a customer of the Moroccan telecommunication operator or from internal systems within the operator," the researchers say. "However, since Lyceum has historically targeted telecommunication providers and the Kaspersky team identified recent targeting of telecommunication operators in Tunisia, it would follow that Lyceum is targeting other north Africa telecommunication companies."

###  Previous and related coverage

* [US indicts UK resident 'PlugwalkJoe' for cryptocurrency theft](https://www.zdnet.com/article/us-indicts-uk-resident-plugwalkjoe-for-cryptocurrency-theft/)
* [Middle East cyber-espionage is heating up with a new group joining the fold](https://www.zdnet.com/article/middle-east-cyber-espionage-is-heating-up-with-a-new-group-joining-the-fold/)
* [Cybersecurity firms provide threat intel for Clop ransomware group arrests](https://www.zdnet.com/article/cybersecurity-firms-provide-threat-intel-in-clop-ransomware-group-arrests/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[telecoms]] [[ZDNet]]
