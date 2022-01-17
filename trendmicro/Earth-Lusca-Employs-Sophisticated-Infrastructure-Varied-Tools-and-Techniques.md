# Earth Lusca Employs Sophisticated Infrastructure, Varied Tools and Techniques
### Our technical brief provides an in-depth look at Earth Lusca’s activities, the tools it employs in attacks, and the infrastructure it uses.

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/22/a/earth-lusca-sophisticated-infrastructure-varied-tools-and-techni.html
+ Date: 2022-01-17
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/earth-lusca-641.png)





Since mid-2021, we have been investigating a rather elusive threat actor called Earth Lusca that targets organizations globally via a campaign that uses traditional social engineering techniques such as spear phishing and watering holes. The group’s primary motivation seems to be cyberespionage: the list of its victims includes high value targets such as government and educational institutions, religious movements, pro-democracy and human rights organizations in Hong Kong, Covid-19 research organizations, and the media, among others. However, the threat actor also seems to be financially motivated, as it also took aim at gambling and cryptocurrency companies.  




Previous research into the group’s activities attributed it to other threat actors such as the Winnti group due to the use of malware such as Winnti, but despite some similarities, we consider Earth Lusca a separate threat actor (we do have evidence, however, that the group is part of the “Winnti cluster,” which is comprised of different groups with the same origin country and share aspects of their TTPs).


[The technical brief](/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf) provides an in-depth look at Earth Lusca’s activities, the tools it employs in attacks, and the infrastructure it uses.


Infrastructure and operating model
==================================


Earth Lusca’s infrastructure can essentially be grouped into two “clusters.” The first cluster is built using virtual private servers (VPS), rented from a service provider, that are used for the group’s watering hole and spear phishing operations, in addition to acting as a command-and-control (C&C) server for malware.


The second cluster is made up of compromised servers running old, open-source versions of Oracle GlassFish Server. Interestingly, this second cluster performs a different role in an Earth Lusca attack — it acts as a scanning tool that searches for vulnerabilities in public-facing servers and builds traffic tunnels within the target’s network. Like the first cluster, it also serves as a C&C server, this time for Cobalt Strike.


It’s possible that the group used portions of its infrastructure (particularly the scanning aspects) for diversion in order to trick security staff into focusing on the wrong parts of the network.






![Figure 1. An overview of Earth Lusca’s infrastructure](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/earth-lusca-1.png)
Figure 1. An overview of Earth Lusca’s infrastructure





Social Engineering and Vulnerability Exploitation techniques
============================================================


The group has three primary attack vectors, two of which involve social engineering. The social engineering techniques can be broken down into spear phishing emails and watering hole websites.


Our telemetry data shows Earth Lusca sending spear phishing emails containing malicious links to one of their targets — a media company. These links contain files that are disguised either as documents that would be of interest to the potential target, or as opinion forms allegedly coming from another media organization. The user eventually downloads an archive file containing either a malicious LNK file or an executable — eventually leading to a Cobalt Strike loader.


In addition to spear phishing emails, Earth Lusca also made use of watering hole websites — they either compromised websites of their targets or set up fake web pages copied from legitimate websites and then injected malicious JavaScript code inside them. These links to these websites are then sent to their victims (although we were not able definitively pinpoint how this was done).


In one incident, the group injected a malicious script into the compromised HR system of a target organization. This script was designed to show a social engineering message — typically a Flash update popup or a DNS error (note that Adobe discontinued Flash Player at the end of December 2020) that then instructed the visitor to download a malicious file that turned out to be a Cobalt Strike loader.






![Figure 2. Fake installation pop-up](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/earth-lusca-2.png)
Figure 2. Fake installation pop-up




The third attack vector used by Earth Lusca is the exploitation of vulnerabilities that exist in the public-facing applications — such as [Microsoft Exchange ProxyShell](https://www.trendmicro.com/en_no/research/21/k/analyzing-proxyshell-related-incidents-via-trend-micro-managed-x.html) and [Oracle GlassFish](https://www.exploit-db.com/exploits/39441) — of its targets. Once these are accomplished, Earth Lusca is free to perform its post-exploitation routines that include installation of tools such as Cobalt Strike and Acunetix (we discuss the post-exploitation routines in detail in the technical brief).


Malware used by Earth Lusca
===========================


Earth Lusca employs several malware and other hacking tools in its arsenal. A common theme we’ve seen in its attack vectors is the use of CobaltStrike loaders — and indeed, Cobalt Strike is one of the group’s preferred tools due to its wide range of post-exploitation capabilities. In this case, the Cobalt Strike shellcode that is dropped into the target system is encoded via XOR along with a corresponding key.


In addition to Cobalt Strike, Earth Lusca also uses [malware such as Doraemon](https://www.welivesecurity.com/2021/08/24/sidewalk-may-be-as-dangerous-as-crosswalk/), a backdoor named after Japanese manga that has two C&C settings: a primary one for one for IP or DNS, and a public website URL containing encrypted or clear text C&C IP addresses that is used for persistence.


The group employs well-known malware such as [ShadowPad](https://securelist.com/shadowpad-in-corporate-networks/81432/) and [Winnti](https://www.trendmicro.com/vinfo/us/security/news/cyber-attacks/winnti-group-resurfaces-with-portreuse-backdoor-now-engages-in-illicit-cryptocurrency-mining), as well as other tools such as cryptocurrency miners as part of its operations. A more comprehensive list of these malware and tools are found in the technical brief.


Security best practices can help defend against Earth Lusca attacks
===================================================================


Evidence points to Earth Lusca being a highly-skilled and dangerous threat actor mainly motivated by cyberespionage and financial gain. However, the group still primarily relies on tried-and-true techniques to entrap a target. While this has its advantages (the techniques have already proven to be effective), it also means that security best practices, such as avoiding clicking on suspicious email/website links and updating important public-facing applications, can minimize the impact — or even stop — an Earth Lusca attack.


[Read our technical brief](/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf) to learn more about Earth Lusca and its activities.








## Tags:

#### Threatactor:
[[threatactor.name=Cobalt Group]] [[threatactor.name=Winnti Group]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=ShadowPad]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Japan]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Lusca]] [[Malware]] [[Phishing]] [[Websites]] [[Winnti]] [[Public-facing]] [[C&c]] [[Emails]] [[Post-exploitation]] [[Trend Micro]]

