# BotenaGo botnet source code has been leaked to GitHub.
### The BotenaGo botnet source code has been leaked to GitHub.  In a Wednesday report, AT&T Alien Labs – which first discovered the difficult-to-detect malware in November 2021 – said it expects that the ready availability of the source code to malware authors puts millions of routers and internet-of-things (IoT) devices at risk.  Uploading of the

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178059
+ Date: 2022-01-27T17:19:49+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2020/11/13123912/iot-botnet.jpg)

The BotenaGo botnet source code has been leaked to GitHub.


In a Wednesday [report](https://cybersecurity.att.com/blogs/labs-research/botenago-strike-again-malware-source-code-uploaded-to-github), AT&T Alien Labs – which first [discovered](https://threatpost.com/routers-iot-open-source-malware/176270/) the difficult-to-detect malware in November 2021 – said it expects that the ready availability of the source code to malware authors puts millions of routers and internet-of-things (IoT) devices at risk.


Uploading of the source code to GitHub “can potentially lead to a significant rise of new malware variants as malware authors will be able to use the source code and adapt it to their objectives,” Alien Labs security researcher Ofer Caspi wrote. “Alien Labs expects to see new campaigns based on BotenaGo variants targeting routers and IoT devices globally.”


Caspi said that as of yesterday, AV vendor detection for BotenaGo and its variants was still bumping along near the bottom when it comes to detecting the malware, with the BotenaGo samples discovered back in November still slipping past most AV software to infect systems with one of the most popular botnets: [Mirai](https://threatpost.com/mirai-variant-sonicwall-d-link-iot/164811/). The screen capture from [VirusTotal](https://www.virustotal.com/gui/file/fef2b32e34ac1b64281c5083e7fc6e055c885820a38fa5eed1f563e38e04c6db) below shows how few AV programs – three out of 60 – are detecting the malware’s new variants.


Scrawny Code, Brawny Malware
----------------------------


Alien Labs only recently discovered that the BotenaGo source code had been uploaded to the wildly popular GitHub software development platform a month prior to when researchers discovered the malware to begin with: Specifically, it was uploaded on Oct. 16, 2021.


The leak means that any malicious actor can use, modify and upgrade the malware, Caspi said, “or even simply compile it as is and use the source code as an exploit kit, with the potential to leverage all BotenaGo’s exploits to attack vulnerable devices.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Researchers also found additional hacking tools, from several sources, collected in the same repository.


Alien Labs called the malware source code “simple yet efficient,” able to carry out malware attacks with a grand total of a mere 2,891 lines of code (including empty lines and comments). In its November writeup, Alien Labs noted that BotenaGo, written in Google’s open-source Golang programming language, could exploit 33 vulnerabilities,


The malware is light, easy to use and powerful. BotenaGo’s 2,891 lines of code are all that’s needed for a malware attack, including, but not limited to, installing a reverse shell and telnet loader used to create a backdoor to receive commands from its command-and-control (C2) operator.


Caspi explained that BotenaGo has automatic setup of its 33 exploits, presenting an attacker a “ready state” to attack a vulnerable target and infect it with an appropriate payload based on target type or operating system.


The source code leaked to GitHub and depicted below features a “supported” list of vendors and software used by BotenaGo to target its exploits at a slew of routers and IoT devices.


New C2 Server
-------------


Besides the fact that BotenaGo is still going undetected by the majority of AV products, Alien Labs’ also recently found that one variant is configured to use a new C2 server, as shown below.


Caspi said that it’s also worth noting that “the IP address for one of BotenaGo’s payload storage servers is included in the list of indicators of compromise (IOC) for detecting exploitation of the Apache Log4Shell flaw in the [Log4j](https://threatpost.com/microsoft-rampant-log4j-exploits-testing/177358/) logging library.


Following in Mirai’s Footsteps
------------------------------


With the recent release of BotenaGo’s source code, the risk to routers and IoT devices is going to spike, Caspi predicted. History tells the tale: the Mirai botnet rocketed to prominence after its source code had similarly been uploaded to a hacking community forum in 2016 and later [uploaded to GitHub](https://techcrunch.com/2016/10/10/hackers-release-source-code-for-a-powerful-ddos-app-called-mirai/) along with details about its infrastructure, configuration and how to build it.


“Today, BotenaGo variants serve as a standalone exploit kit and as a spreading tool for other malware,” he said. “Now with its source code available to any malicious hacker, new malicious activity can be added easily to the malware. Alien Labs sees the potential for a significant increase in these malware variants, giving rise to potentially new malware families that could put millions of routers and IoT devices at risk of attack.”


How to Make BotenaGo Go-Go-Go Away
----------------------------------


Alien Labs researchers recommend three steps to keep this malware off devices:


1. Maintain minimal exposure to the Internet on Linux servers and IoT devices and use a properly configured firewall.
2. Install security and firmware upgrades from vendors, as soon as possible.
3. Check your system for unnecessary open ports and suspicious processes.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=Rocke]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Epic]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=route]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Malware]] [[Botenago]] [[Caspi]] [[Github]] [[Iot]] [[Mirai]] [[ThreatPost]]

