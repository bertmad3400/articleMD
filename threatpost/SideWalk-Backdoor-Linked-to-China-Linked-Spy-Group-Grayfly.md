# SideWalk Backdoor Linked to China-Linked Spy Group ‘Grayfly’
### Grayfly campaigns have launched the novel malware against businesses in Taiwan, Vietnam, the US and Mexico and are targeting Exchange and MySQL servers. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169310)
+ Date: September 9, 2021  10:30 am
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/09100748/House-Fly-4-e1631196481176.jpeg)
The novel backdoor technique called [SideWalk](https://threatpost.com/sparklinggoblin-apt/168928/), seen in campaigns targeting US media and retailers late last month, has been tied to an adversary that’s been around for quite a while: namely, China-linked Grayfly espionage group.


ESET researchers, who named and discovered the new “SparklingGoblin” advanced persistent threat (APT) actor behind SideWalk, [reported](https://www.welivesecurity.com/2021/08/24/sidewalk-may-be-as-dangerous-as-crosswalk/) at the time that the group is an offshoot of another APT – Winnti Group – first identified in 2013 by Kaspersky.


ESET also said that the SideWalk backdoor is similar to one used by [Winnti](https://threatpost.com/black-hat-linux-spyware-stack-chinese-apts/158092/) (aka APT41, Barium, Wicked Panda or Wicked Spider, an APT [known for](https://threatpost.com/apt41-operatives-indicted-hacking/159324/) nation state-backed cyberespionage and financial cybercrime) called CrossWalk (Backdoor.Motnug). Both CrossWalk and SideWalk are modular backdoors used to exfiltrate system information and can run shellcode sent by the command-and-control (C2) server.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


According to a [report](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/grayfly-china-sidewalk-malware) published by Symantec on Thursday, the SideWalk malware has been deployed in recent Grayfly campaigns against organizations in Taiwan, Vietnam, the US and Mexico. Symantec’s Threat Hunter Team has observed recent campaigns that have involved exploits targeting Exchange and MySQL servers.


Besides attacking organizations in the IT, media and finance sectors, the group also has zeroed in on the telecoms sector, according to the report.


Indicted but Undeterred
-----------------------


The US [indicted](https://www.justice.gov/opa/pr/seven-international-cyber-defendants-including-apt41-actors-charged-connection-computer) several members of APT41 in September 2020, all of them Chinese residents and nationals. A Federal grand jury charged them with pulling off dozens of crimes, including allegedly facilitating ” the theft of source code, software code-signing certificates, customer-account data and valuable business information,” which in turn “facilitated other criminal schemes, including ransomware and cryptojacking.”


As the Department of Justice (DOJ) said at the time, one of the defendants – Jiang Lizhi – allegedly bragged about having a “working relationship” with the Chinese Ministry of State Security: a relationship that would give him and his alleged co-conspirators a degree of state protection.


According to Symantec researchers, the SideWalk campaign suggests that the [arrests and the publicity](https://threatpost.com/apt41-operatives-indicted-hacking/159324/) can’t have made much of a dent in the group’s activity.


**Pesky Grayfly**
-----------------


You might know Grayfly better by its also-known-as’s, which include GREF and Wicked Panda. Symantec said that even though the Grayfly APT is sometimes labeled APT41, its researchers consider Grayfly to be a distinct arm of APT41 that’s devoted to espionage. This is similar to how Symantec separately tracks other sub-groups of APT41, such as Blackfly, the APT’s cybercrime arm.


Grayfly, a targeted attack group, has been around since at least March 2017, using the CrossWalk/Backdoor.Motnug (aka TOMMYGUN) backdoor. The group has also wielded a custom loader called Trojan.Chattak, Cobalt Strike (aka Trojan.Agentemis, the legitimate, commercially available tool used by network penetration testers and, increasingly, [by crooks](https://threatpost.com/cobalt-strike-cybercrooks/167368/)) and ancillary tools in its attacks.


Researchers have seen Grayfly targeting a number of countries in Asia, Europe, and North America across a variety of industries, including food, financial, healthcare, hospitality, manufacturing and telecommunications. Recently, it’s continued to torment telecoms, but it’s also been going after the media, finance and IT service providers.


Grayfly’s typical modus operandi is to target publicly facing web servers to install web shells for initial intrusion before spreading further within the network, Symantec said. After it has penetrated a network, Grayfly then might install its custom backdoors onto more systems. That gives the operators remote access to the network and proxy connections that enable them to access hard-to-reach segments of a target’s network, according to the writeup.


**Walking the Slippery SideWalk**
---------------------------------


Symantec researchers observed that in the recent SideWalk campaign, Grayfly looked to be particularly interested in attacking exposed Microsoft Exchange or MySQL servers, suggesting that “the initial vector may be the exploit of multiple vulnerabilities against public-facing servers.”


In fact, the Cybersecurity & Infrastructure Security Agency (CISA) recently put out an urgent [alert](https://us-cert.cisa.gov/ncas/current-activity/2021/08/21/urgent-protect-against-active-exploitation-proxyshell) about a [surge in ProxyShell attacks](https://threatpost.com/proxyshell-attacks-unpatched-exchange-servers/168879/), as attackers launched 140 web shells against 1,900 unpatched Microsoft Exchange servers. Security researchers at Huntress reported seeing [ProxyShell vulnerabilities](https://www.huntress.com/blog/rapid-response-microsoft-exchange-servers-still-vulnerable-to-proxyshell-exploit) being actively exploited throughout the month of August to install backdoor access once the [ProxyShell exploit code](https://peterjson.medium.com/reproducing-the-proxyshell-pwn2own-exploit-49743a4ea9a1) was published on Aug. 6: A few weeks later, the surge hit.


In at least one of the SideWalk attacks that Symantec researchers observed, the suspicious Exchange activity was followed by PowerShell commands used to install an unidentified web shell. That may sound familiar, given that one of the vulnerabilities Huntress described last month was CVE-2021-34523: a bug that enables malicious actors to execute arbitrary code post-authentication on Microsoft Exchange servers due to a flaw in the PowerShell service not properly validating access tokens.


The Grayfly attackers executed the malicious SideWalk backdoor after the web shell was installed. Then, they deployed a tailor-made version of the open-source, credential-dumping tool Mimikatz that Symantec said has been used in earlier Grayfly attacks. Symantec’s report does a deep dive on the technical details, including indicators of compromise.


Expect more to come, researchers said, since this fly isn’t likely to buzz off: “Grayfly is a capable actor, likely to continue to pose a risk to organizations in Asia and Europe across a variety of industries, including telecommunications, finance, and media. It’s likely this group will continue to develop and improve its custom tools to enhance evasion tactics along with using commodity tools such as publicly available exploits and web shells to assist in their attacks.”


**It’s time to evolve threat hunting into a pursuit of adversaries.** [**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **Threatpost and Cybersixgill for** [**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **and get a guided tour of the dark web and learn how to track threat actors before their next attack.** [**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **for the LIVE discussion on September 22 at 2 PM EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[Symantec]] [[(aka]] [[APT41,]] [[network,]] [[Microsoft]] [[ProxyShell]] [[ThreatPost]]
