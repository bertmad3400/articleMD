# MoleRats APT Flaunts New Trojan in Latest Cyberespionage Campaign
### Researchers from Proofpoint have spotted a new Middle East-targeted phishing campaign that delivers a novel malware dubbed NimbleMamba.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178305
+ Date: 2022-02-09T14:03:18+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/24162819/MoleRAT-scaled-e1643059797213.jpeg)

Known Palestinian threat actor MoleRats is likely behind a recent malicious email campaign targeting Middle Eastern governments, foreign-policy think tanks and a state-affiliated airline with a new intelligence-gathering trojan dubbed NimbleMamba, researchers said.


Researchers from Proofpoint said they have observed a spear-phishing campaign using multiple vectors since November that they believe is the work of TA402, more [commonly known as](https://threatpost.com/molerats-apt-espionage-facebook-dropbox/162162/) MoleRats and linked to the Palestinian Territories, according to a [report](https://www.proofpoint.com/us/blog/threat-insight/ugg-boots-4-sale-tale-palestinian-aligned-espionage) posted online Tuesday.


The campaign uses various phishing lures and includes tactics not only to avoid being detected but also to ensure that its core malware payload only attacks specific targets, Proofpoint researchers wrote in the report. Some of the attacks observed by the team also delivered a secondary payload, a trojan dubbed BrittleBush, they said.


NimbleMamba, delivered as an obfuscated .NET executable using third-party obfuscators, is an intelligence-gathering trojan researchers believe is a replacement for previous malware used by TA402, LastConn.


“NimbleMamba has the traditional capabilities of an intelligence-gathering trojan and is likely designed to be the initial access,” researchers wrote. “Functionalities include capturing screenshots and obtaining process information from the computer. Additionally, it can detect user interaction, such as looking for mouse movement.”


MoleRats is part of the Gaza Cybergang, an Arabic speaking, politically motivated collective of interrelated threat groups actively targeting the Middle East and North Africa. It’s known for attacks using spyware and other malware aimed at gathering intelligence.


Researchers from Zscaler have already observed MoleRats targeting prominent Palestinians, as well as activists and journalists in Turkey, with spyware [in a previously identified attack](https://threatpost.com/molerats-apt-spy-bankers-politicians-journalists/177907/) in January. That campaign used malicious files doctored up to look like legitimate content related to the Israeli-Palestine conflict.


**Variations of an Espionage Campaign**
---------------------------------------


Proofpoint outlined three types of emails using different tactics and URLs aimed at tricking victims into clicking on malicious links to download the ultimate payloads.


One, which they observed in November, shows MoleRats pretending to be the Quora website while using an actor-controlled Gmail account with an actor-controlled domain, they said.


The attack vector demonstrated a hallmark of the campaign, which is to use geofencing to target specific countries with the malicious payload rather than delivering it to everyone who clicks on the email’s malicious link. The email appears to advertise Ugg boots for sale.


“The malicious URL, such as https[:]//www[.]uggboots4sale[.]com/news15112021.php, in the phishing email was geofenced to the targeted countries,” researchers wrote. ” If the target’s IP address fits into the targeted region, the user would be redirected to the .RAR file download containing the latest TA402 implant, NimbleMamba. If outside the target area, the user would be redirected to a legitimate news site.”


The second variation, called “Dropbox URL,” was observed in December using “multiple phishing pretenses, including clickbait medical lures and ones allegedly sharing confidential geopolitical information,” researchers wrote.


This variation also used a Gmail account controlled by TA402 to send the email, but shifted to Dropbox URLs to deliver the malicious .RAR files containing NimbleMamba. It also abandoned the use of geofencing, they said.


Moreover, in this variation, researchers noticed that the threat actor also was using the cloud-based file-sharing service Dropbox for malware command and control (C2), which prompted them to notify Dropbox of the malicious activity so they could put an end to it, they said. MoleRats was seen using Dropbox for C2 in its previously identified attacks in January.


The third email used by attackers, observed in December and January, used socially engineered content specifically to lure targets. However, in this variation, MoleRats “slightly adjusted their attack chain by inserting an additional actor-controlled WordPress URL,” researchers wrote.


The WordPress site impersonates a news aggregator of the legitimate news site used in the first campaign variation, and likely redirects to the download site of the malicious .RAR files containing NimbleMamba if someone in the targeted region clicks on the link, researchers said.


“If the source IP address does not align with the target region, the URL will redirect the recipient to a benign website, typically an Arabic-language news website,” they added.


**NimbleMamba in Depth**
------------------------


The most frequently delivered payload of the campaign, NimbleMamba, has some similarities between TA402’s previously used deliverable, LastConn, but also some notable differences, researchers observed.


Both executables are written in C#, have base64 encoding within the C2 framework and use the Dropbox API for C2 communication. However,  there appears to be little code overlap between the two, they said.


NimbleMamba’s use of guardrails to ensure that all infected victims are within TA402’s target region also is unique, as is its use of the Dropbox API for both C2 as well as exfiltration, researchers wrote in the post.


“The malware also contains multiple capabilities designed to complicate both automated and manual analysis,” they wrote. “Based on this, Proofpoint assesses NimbleMamba is actively being developed, is well-maintained, and designed for use in highly targeted intelligence collection campaigns.”


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=Molerats]] [[threatactor.name=Molerats]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Healthcare]]

#### Location:
[[victim.continent.name=Africa]] [[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Israel]] [[victim.continent.name=Asia]] [[victim.country.name=Palestine]] [[victim.continent.name=Asia]] [[victim.country.name=Turkey]] [[victim.continent.name=Asia]] [[victim.country.name=Turkey]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Nimblemamba]] [[Molerats]] [[Ta402]] [[Dropbox]] [[Malware]] [[Proofpoint]] [[C2]] [[Intelligence-gathering]] [[Phishing]] [[Actor-controlled]] [[ThreatPost]]

