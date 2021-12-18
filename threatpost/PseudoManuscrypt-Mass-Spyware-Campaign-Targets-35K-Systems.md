# ‘PseudoManuscrypt’ Mass Spyware Campaign Targets 35K Systems
### It’s similar to Lazarus’s Manuscrypt malware, but the new spyware is splattering itself onto government organizations and ICS in a non-Lazarus-like, untargeted wave of attacks.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177097
+ Date: 2021-12-16T18:36:40+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2020/03/20163020/keylogger.jpg)

Researchers have tracked new spyware – dubbed “PseudoManuscrypt” because it’s similar to “Manuscrypt” malware from the Lazarus advanced persistent threat (APT) group – that’s attempted to scribble itself across more than 35,000 targeted computers in 195 countries.


Kaspersky researchers said in a Thursday [report](https://securelist.com/pseudomanuscrypt-a-mass-scale-spyware-attack-campaign/105286/) that from Jan. 20 to Nov. 10, the actors behind the vast campaign were targeting government organizations and industrial control systems (ICS) across a range of industries, including engineering, building automation, energy, manufacturing, construction, utilities and water management. At least 7.2 percent of all attacked computers are part of ICS, researchers said.


[Manuscrypt](https://threatpost.com/lazarus-targets-defense-threatneedle-malware/164321/), aka NukeSped, is a family of malware tools that have been used in espionage campaigns in the past. One such was a February spear-phishing campaign linked to [Lazarus](https://threatpost.com/lazarus-engineers-malicious-docs/167647/) – a prolific North Korean APT – that used the Manuscrypt malware family’s ‘ThreatNeedle’ tool cluster to [attack defense companies.](https://threatpost.com/lazarus-targets-defense-threatneedle-malware/164321/)


Fake Pirated Installers
-----------------------


The operators behind PseudoManuscrypt are using fake pirated software installer archives to initially download the spyware onto targets’ systems.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The fake installers are for for “ICS-specific software, such as an [application](https://www.win-tech.com/html/modbus1.htm) designed to create a MODBUS Master Device to receive data from a PLC [programmable logic controller], as well as more general-purpose software, which is nevertheless used on OT networks, such as a key generator for a SolarWinds [tool](https://www.solarwinds.com/engineers-toolset) for network engineers and systems administrators,” researchers said.


They suspect that the threat actors are getting the fake installers off a malware-as-a-service (MaaS) platform that’s offering them up to operators of multiple malicious campaigns, not just this widely dispersed PseudoManuscrypt campaign.


However, Kaspersky also shared a screen capture – shown below –of the listings for fake installers they found via a Google search.


Kaspersky outlined two variants of the module, both of which are outfitted with advanced spyware capabilities. One version rode in via the infamous [Glupteba](https://threatpost.com/google-glupteba-botnet-lawsuit/176826/) botnet: a hard-to-scrub-off, 1 million-strong botnet of compromised Windows and internet of things (IoT) devices that Google’s Threat Analysis Group (TAG) disrupted earlier this month.


The tie-in with Glupteba is a clue that PseudoManuscrypt’s could have originated on a MaaS platform, researchers said, given that the botnet’s main installer “is also distributed via the pirated software installer distribution platform.”


Shanghaing Systems with Full Spyware Capabilities
-------------------------------------------------


Both of the module variants have brawny spyware capabilities, researchers said. PseudoManuscrypt’s main module has a full tool kit for spying every which way, including, among many other things, the ability to:


* Steal VPN connection data
* Log keystrokes
* Grab screenshots and take screen videos
* Use a system’s microphone to eavesdrop and record sound
* Filch clipboard data
* Steal OS event log data – which also makes it possible to steal Remote Desktop Protocol [(RDP) authentication data](https://threatpost.com/remote-desktop-protocol-secure/167719/).


In other words, it can completely take over infected systems, researchers said: “Essentially, the functionality of PseudoManuscrypt provides the attackers with virtually full control of the infected system.”


Is This an APT On a Bender?
---------------------------


For an APT, this one’s weirdly promiscuous, what with those 35,000 attacks on systems across the globe: a spread that doesn’t indicate that it’s targeted. “Such a large number of attacked systems is not characteristic of the Lazarus group or APT attacks as a whole,” researchers noted.


The PseudoManuscrypt campaign attacks what they called “a significant number of industrial and government organizations, including enterprises in the military-industrial complex and research laboratories.”


Similarities to Manuscrypt
--------------------------


Kasperskiy’s ICS-CERT team first detected the PseudoManuscrypt series of attacks in June, when the malware triggered antivirus detection designed to spot Lazarus activity. The full picture didn’t point to Lazarus, however, given the atypical, untargeted splatter of tens of thousands of attacks.


However, Kaspersky subsequently found similarities between the new PseudoManuscrypt and Lazarus’s Manuscrypt malware


The PseudoManuscrypt malware loads its payload from the system registry and decrypts it, researchers explained, with the payload using a registry location that’s unique to each infected system.


“Both malicious programs load a payload from the system registry and decrypt it; in both cases, a special value in the CLSID format is used to determine the payload’s location in the registry,” they said. “The executable files of both malicious programs have virtually identical export tables.”


The two malwares also use similar executable file naming formats.


Another commonality between the two malwares is that some of the organizations attacked by PseudoManuscrypt have business and production ties with victims of the Lazarus ThreatNeedle campaign, Kaspersky noted.


With regards to the geographic reach of the PseudoManuscrypt campaign, nearly a third – 29.4 percent – of the targeted, non-ICS computers are located in Russia (10.1 percent), India (10 percent) and Brazil (9.3 percent), Kaspersky found, which is a distribution that’s similar to that for ICS computers.


“The number of attacked systems is large and we see no clear focus on specific industrial organizations,” they concluded. “However, the fact that a large number of ICS computers across the globe (many hundreds according to our telemetry alone – and in reality very likely to be much more) have been attacked in this campaign certainly makes it a threat that merits the very closest attention of specialists responsible for the security and safety of shop-floor systems and their continuous operation.”


Who’s Behind PseudoManuscrypt?
------------------------------


Researchers listed these clues as to the adversary’s origin or its ties:


1. Some malware samples contain comments in Chinese in executable file metadata.
2. Data is sent to the attackers’ server using a library that has previously been used only in malware of the Chinese group APT41.
3. When connecting to the command-and-control server, the malware specifies Chinese as the preferred language.
4. The malicious file contains code for connecting to Baidu, a popular Chinese cloud storage for files.
5. The time of day at which new versions of the PseudoManuscrypt loader were uploaded by the developer falls within the 11 am to 7 pm interval in the GMT+8 time zone, in which several East Asian and Asia-Pacific countries are located.


Execution Flow
--------------


In a detailed drilldown on its [ICS-CERT website](https://ics-cert.kaspersky.com/reports/2021/12/16/pseudomanuscrypt-a-mass-scale-spyware-attack-campaign/), Kaspersky researchers said that the execution flow for PseudoManuscrypt installation has numerous possible variants, with malware installers downloading and executing loads of other malicious programs, including spyware, backdoors, cryptocurrency miners and adware.


As well, at each stage, they saw a slew of different droppers installed and modules downloaded, with different modules designed to steal data and each module having its own command-and-control (C2) server.


Below is the execution flow for one of the two variants spotted by Kaspersky: the one that uses the Glupteba botnet’s infrastructure and malware installers.


Researchers pointed to yet another variant of the PseudoManuscrypt installer that’s been described by [BitDefender](https://www.bitdefender.com/files/News/CaseStudies/study/400/Bitdefender-PR-Whitepaper-MosaicLoader-creat5540-en-EN.pdf) that was downloaded using the link hxxps://jom[.]diregame[.]live/userf/2201/google-game.exe on May 17, 2021.


“It is worth noting that at different times the link could be used to download malware from different families,” Kaspersky said.


A Bit of a Head-Scratcher
-------------------------


The fact that industrial entities are tempting targets both for financially motivated adversaries and cyberespionage isn’t news, Kaspersky said in summing up its report. “Industrial organizations are some of the most coveted targets for cybercriminals both for financial gain and intelligence gathering,” according to the writeup, which pointed to 2021 having seen “significant interest in industrial organizations from well-known APT groups like Lazarus and APT41.”


[APT 41](https://threatpost.com/apt41-operatives-indicted-hacking/159324/) – aka Barium, [Winnti](https://threatpost.com/black-hat-linux-spyware-stack-chinese-apts/158092/), Wicked Panda or Wicked Spider – is a China-linked threat group known for nation-state-backed cyber-espionage activity as well as financial cybercrime.


But Kaspersky said that it can’t say for sure whether the PseudoManuscrypt campaign is “pursuing criminal mercenary goals or goals correlating with some governments’ interests.” Nevertheless, “the fact that attacked systems include computers of high-profile organizations in different countries makes us assess the threat level as high,” researchers said.


They added, “The large number of engineering computers attacked, including systems used for 3D and physical modeling, the development and use of digital twins raises the issue of industrial espionage as one of the possible objectives of the campaign.”


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=APT41]] [[threatactor.name=APT41]] [[threatactor.name=Lazarus Group]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Construction]] [[victim.industry.name=Manufacturing]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.continent.name=Asia]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Oman]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Brazil]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Pseudomanuscrypt]] [[Malware]] [[Kaspersky]] [[Spyware]] [[Manuscrypt]] [[Botnet]] [[Ics]] [[Glupteba]] [[“the]] [[Percent)]] [[ThreatPost]]
#### urls
hxxps://jom.diregame.live/userf/2201/google-game.exe

