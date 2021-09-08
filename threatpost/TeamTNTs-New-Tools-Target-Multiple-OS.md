# TeamTNT’s New Tools Target Multiple OS
### The attackers are indiscriminately striking thousands of victims worldwide with their new “Chimaera” campaign. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169279)
+ Date: September 8, 2021  1:03 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/08095039/chimera-e1631109057905.jpg)
The TeamTNT malware pushers have a slew of new toys with which to wreak havoc – multiple shell/batch scripts, open-source tools, a cryptocurrency miner, an IRC and more – that have inflicted more than 5,000 infections globally as antivirus (AV) tools struggle to catch up with the newest malware.


Earlier today, on Wednesday, cybersecurity researchers from AT&T Alien Labs [published a report](https://cybersecurity.att.com/blogs/labs-research/teamtnt-with-new-campaign-aka-chimaera) on the group’s latest campaign, dubbed Chimaera. The threat group is carpet-bombing multiple operating systems and applications with its new kit.


According to Alien Labs, infection statistics on the command-and-control (C2) server used in Chimaera suggest that TeamTNT has been running the campaign for about 1.5 months, since July 25.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Unfortunately, all of these new tools mean that AV products, for the most part, aren’t detecting the malware yet.


“As of August 30, 2021, many malware samples still have zero antivirus detections and others have low detection rates,” according to the report.


In other words, the Chimaera campaign has largely gone unimpeded as it’s infiltrated victims’ networks, using its new, open-source tools to steal usernames and passwords from infected machines and target a range of operating systems.


Alien Labs said that the Chimaera campaign has a similar focus to older TeamTNT campaigns: Namely, “stealing cloud systems credentials, using infected systems for cryptocurrency mining, and abusing victims’ machines to search and spread to other vulnerable systems.”


Slipping In Under an Open-Source Cloak
--------------------------------------


TeamTNT typically uses open-source tools for its dirty work. For example, in January, it was using the detection-evasion tool libprocesshider to [hide its malware](https://threatpost.com/teamtnt-cloaks-malware-open-source-tool/163414/) under Linux by using the ld preloader.


In the Chimaera campaign, TeamTNT is using yet another new detection-evasion toolkit in order to help its cryptomining malware to skirt defense teams. This is a partial list of the tools it’s using:


According to Palo Alto Networks, TeamTNT [has also added](https://unit42.paloaltonetworks.com/teamtnt-operations-cloud-environments/) the open-source Kubernetes and the cloud-penetration toolset Peirates to its reconnaissance operations.


“With these techniques available, TeamTNT actors are increasingly more capable of gathering enough information in target AWS and Google Cloud environments to perform additional post-exploitation operations,” according to Palo Alto’s June report. “This could lead to more cases of lateral movement and potential privilege-escalation attacks that could ultimately allow TeamTNT actors to acquire administrative access to an organization’s entire cloud environment.”


On Wednesday, Alien Labs researchers noted that the use of open-source tools such as LaZagne helps the malware to evade detection:



> “The use of open-source tools like LaZagne allows TeamTNT to stay below the radar for a while, making it more difficult for antivirus companies to detect.” —Alien Labs
> 
> 


TeamTNT Publishes Infection Statistics
--------------------------------------


With the new campaign and the new tools came another new development: For the first time, TeamTNT has started publishing infection statistics publicly on its website. As shown in the image below, the number of victims stood at 5,104 as of the time that Alien Labs grabbed a screen capture.


Rapacious Rampaders
-------------------


Trend Micro has called TeamTNT “one of the most prolific and persistent malicious actor groups in recent memory.” As the firm described in a July [report](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/teamtnt-activities-probed?utm_source=trendmicroresearch&utm_medium=smk&utm_campaign=0721_teamtnt), the threat actor has actually been active since 2011, but it started picking up steam last year.


In April 2020, TeamTNT launched a short-lived phishing campaign that used COVID-19 terms as a lure. A month later, the threat actors targeted [vulnerable Docker containers](https://www.trendmicro.com/vinfo/us/security/news/virtualization-and-cloud/coinminer-ddos-bot-attack-docker-daemon-ports) to plant cryptocurrency miners.


TeamTNT is known for its targeting of Amazon Web Services (AWS) credentials, which the group uses to break into cloud instances so as to mine for [Monero](https://threatpost.com/monero-cybercrime-mining-malware/141116/) cryptocurrency. As of September 2020, they were achieving [full takeover of cloud instances](https://threatpost.com/teamtnt-remote-takeover-cloud-instances/159075/), using a legitimate tool called Weave Scope to establish fileless backdoors on targeted Docker and Kubernetes clusters.


TeamTNT also keeps adding new widgets to its toolkit of tactics, techniques and procedures (TTPs). For example, in October 2020, Palo Alto Network’s Unit 42 reported ([PDF](https://unit42.paloaltonetworks.com/black-t-cryptojacking-variant/)) that the group [hatched a batch of new TTPs](https://threatpost.com/blackt-cryptojacker-teamtnt/159853/), including the new Black-T cryptojacking malware, sophisticated network scanners, the targeting of competitor XMR mining tools on the network and the use of password scrapers.


Just before the end of 2020, the group launched yet another campaign, deploying TNTbotinger: an IRC (Internet Relay Chat) bot with distributed denial-of-service (DDoS) capabilities.


But as Trend Micro explained in its July report, this year, TeamTNT has zeroed in even more closely on the cloud, with campaigns encompassing different cloud-based services and software. True to form, with campaign Chimaera, the group has been targeting Windows, AWS, Docker, Kubernetes, and various Linux installations – including Alpine, which is typically used in containers – according to Alien Labs.


How to Avoid a Malware Infection
--------------------------------


As of the end of last month, Aug. 30, many malware samples have low detection rates, according to Alien Labs.


Researchers recommended that to avoid infection, security teams should take these steps:


**It’s time to evolve threat hunting into a pursuit of adversaries.** [**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **Threatpost and Cybersixgill for** [**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **and get a guided tour of the dark web and learn how to track threat actors before their next attack.** [**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **for the LIVE discussion on September 22 at 2 PM EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[TeamTNT]] [[malware]] [[open-source]] [[cloud]] [[campaign,]] [[Palo]] [[ThreatPost]]
