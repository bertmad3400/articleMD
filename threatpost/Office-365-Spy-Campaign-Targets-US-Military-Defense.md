# Office 365 Spy Campaign Targets US Military Defense
### An Iran-linked group is taking aim at makers of drones and satellites, Persian Gulf ports and maritime shipping companies, among others.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175425)
+ Date: October 12, 2021  1:46 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/12133312/military-scaled-e1634060011176.jpeg)
A new threat actor, dubbed DEV-0343, has been spotted attacking U.S. and Israeli defense technology companies, Persian Gulf ports of entry and global maritime transportation companies with ties to the Middle East. The threat actor’s goal is Microsoft Office 365 account takeovers.


Microsoft, which began tracking the activity in late July 2021, detailed the attacks [in an alert](https://www.microsoft.com/security/blog/2021/10/11/iran-linked-dev-0343-targeting-defense-gis-and-maritime-sectors/) released Monday, adding that the culprits appear to be bent on espionage and have ties to Iran. It stated cyberattackers are “conducting extensive password spraying” against Office 365 accounts.


Password-spraying [is the process of](https://threatpost.com/citrix-confirms-password-spraying-heist/146641/) trying a list of user names and a series of different passwords against online accounts in hopes of finding a match and gaining access to password-protected accounts. In this case, the attackers typically mount attacks on “dozens to hundreds of accounts” within each targeted organization, Microsoft said, and have been seen trying thousands of credential combinations against each account.


So far, the campaign has targeted about 250 specific organizations that use Microsoft’s cloud-based Office suite, with less than 20 of them suffering compromise, according to the company. However, “DEV-0343 continues to evolve their techniques to refine its attacks,” the computing giant warned.


The attacks for now are being carried out using an emulated Firefox or Chrome browser, and rotating IP addresses hosted on a Tor proxy network, according to the analysis. On average, each attack uses between 150 and 1,000+ unique addresses, Microsoft said, in an elaborate effort to obfuscate the operational infrastructure.


“Changing the IP address for every password attempt is becoming a more common technique among sophisticated threat groups,” according to the writeup. “Often, threat groups randomize the user agent they are using as well as IP address. This technique has been enabled by the emergence of services providing huge numbers of residential IP addresses. These services are often enabled through malicious browser plugins.”


This use of the proxy addresses makes developing indicators or compromise (IoCs) difficult, but the patterns that Microsoft has observed in the attacks include:


“The operators typically target two Exchange endpoints – Autodiscover and ActiveSync – as a feature of the enumeration/password spray tool they use,” according to Microsoft. “This allows DEV-0343 to validate active accounts and passwords, and further refine their password-spray activity.”


**Alleged Links to Iran**
-------------------------


The group’s “DEV”-based name is just Microsoft’s temporary designation standing for a cluster of developing activity. Once more is known about the attackers, Microsoft will give it a permanent name.


For now though, there’s evidence that points to the threat actors being Iranian, it said. For instance, the attacks have specifically gone after companies that make military-grade radars, drone technology, satellite systems, emergency response communication systems, geographic information systems (GIS) and spatial analytics, Microsoft said, along with the ports and transportation companies. That dovetails with Iran’s past attacks against shipping and maritime targets and overall goals, according to Microsoft.


“This activity likely supports the national interests of the Islamic Republic of Iran based on pattern-of-life analysis, extensive crossover in geographic and sectoral targeting with Iranian actors, and alignment of techniques and targets with another actor originating in Iran,” the company noted. “Microsoft assesses this targeting supports Iranian government tracking of adversary security services and maritime shipping in the Middle East to enhance their contingency plans…Gaining access to commercial satellite imagery and proprietary shipping plans and logs could help Iran compensate for its developing satellite program.”


Also, the group is most active between Sunday and Thursday between 7:30 a.m. and 8:30 p.m. local Iran time, with Microsoft observing peak password-spray activity between 7:30 a.m. and 2:30 p.m.


**How to Protect Against Office 365 Takeovers**
-----------------------------------------------


To protect against password-spraying attacks, Microsoft suggested that users first and foremost enable multifactor authentication.


Otherwise, the company said that other defensive tactics include using passwordless solutions like Microsoft Authenticator to secure accounts; reviewing Exchange Online access policies; block ActiveSync clients from bypassing Conditional Access policies; and block all incoming traffic from anonymizing services where possible.


***Check out our free***[***upcoming live and on-demand online***](https://threatpost.com/category/webinars/) ***town halls*** ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


 




#### Tags:
[[Microsoft]] [[IP]] [[said,]] [[ThreatPost]]
