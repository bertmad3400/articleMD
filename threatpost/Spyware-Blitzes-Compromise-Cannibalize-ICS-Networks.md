# Spyware Blitzes Compromise, Cannibalize ICS Networks
### The brief spearphishing campaigns spread malware and use compromised networks to steal credentials that can be sold or used to commit financial fraud.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177851
+ Date: 2022-01-21T14:10:07+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/21090821/cannibal-burger.jpeg)

Attackers are targeting industrial enterprises with [spyware campaigns](https://threatpost.com/pseudomanuscrypt-mass-spyware-campaign/177097/) that hunt for corporate credentials so they can be used both for financial gain and to cannibalize compromised networks to propagate future attacks, researchers have found.


The campaigns use off-the-shelf spyware but are unique in that they limit the scope and lifetime of each sample to the bare minimum, according to researchers at Kaspersky ICS CERT who uncovered the campaigns.


Researchers dubbed the attacks “anomalous” because they veer from typical spyware attacks, Kaspersky’s Kirill Kruglov wrote [in a report](https://securelist.com/hunt-for-corporate-credentials-on-ics-networks/105545/) published this week on the SecureList blog. Attackers use spearphishing emails sent from compromised corporate mailboxes that include malicious attachments that deliver spyware, he explained.  

[![Password Management Webinar](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/12124026/specops_300x250_watch.jpg)](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)


The attackers use SMTP services of industrial enterprises not only to send spearphishing emails but also to collect data stolen by spyware as a one-way command-and-control (C2) so they can mount future attacks, Kruglov explained.


“We believe that initially stolen data is used by threat operators primarily to spread the attack inside the local network of the attacked organization (via phishing emails) and to attack other organizations in order to collect more credentials,” he wrote. “The attackers use corporate mailboxes compromised in earlier attacks as the C2 servers for new attacks.”


The malware used in the attacks typically belong to “well-known commodity spyware families,” such as AgentTesla/Origin Logger, HawkEye, Noon/Formbook, Masslogger, Snake Keylogger, Azorult and Lokibot, he noted.


However, “these attacks stand out from the mainstream due to a very limited number of targets in each attack and a very short lifetime of each malicious sample,” Kruglov wrote.


**Targeting ICS Enterprises**
-----------------------------


About 45 percent of targeted computers in the campaigns appear to be industrial control system (ICS)-related and have access to the corporate email service of their respective company, researchers said.


Kaspersky researchers have identified more than 2,000 corporate email accounts belonging to industrial companies that have been stolen and abused as next-attack C2 in the campaigns. However, they estimate that more than 7,000 have actually been stolen, sold on the internet or “abused in other ways,” Kruglov wrote.


“Amongst attacks of this kind, we’ve noticed a large set of campaigns that spread from one industrial enterprise to another via hard-to-detect phishing emails disguised as the victim organizations’ correspondence and abusing their corporate email systems to attack through the contact lists of compromised mailboxes,” he explained.


**Independent, Low-Skilled Perpetrators**
-----------------------------------------


Researchers believe the actors behind the analogous campaigns are “low-skilled individuals and small groups” operating independently, they said. Their aim is either to commit financial crimes using stolen credentials or to make money by selling access to corporate network servers and services.


Indeed, they identified more than 25 different marketplaces where threat actors are selling the data stolen in the campaigns against industrial enterprises.


“At these markets, various sellers offer thousands of RDP, SMTP, SSH, cPanel, and email accounts, as well as malware, fraud schemes, and samples of emails and webpages for social engineering,” Kruglov explained.


More dangerous threat actors like Advanced Persistent Threat (APT) and ransomware groups also can use the credentials to mount attacks, he added.


To avoid compromise by the campaigns, Kaspersky recommends implementing two-factor authentication for corporate email access and other internet-facing services such as RDP and VPN-SSL gateways.


Researchers also advise that organizations shore up endpoint security, train personnel to securely approach all incoming email, regularly check spam folders instead of just emptying them and monitor the exposure of the organization’s accounts to the web, among other protections.


*Cannibal burger photo courtesy of [Jack Lawrence](https://www.flickr.com/photos/aceofknaves/40480822634). [Licensing details](https://creativecommons.org/licenses/by-nc-sa/2.0/).*





## Tags:

#### Threatactor:
[[threatactor.name=Turla]]

#### Action:
[[action.malware.name=Agent Tesla]] [[action.malware.name=Arp]] [[action.malware.name=at]] [[action.malware.name=Azorult]] [[action.malware.name=Derusbi]] [[action.malware.name=Elise]] [[action.malware.name=Lokibot]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Tor]] [[action.malware.name=UPPERCUT]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Spyware]] [[Kruglov]] [[Kaspersky]] [[Emails]] [[ThreatPost]]

