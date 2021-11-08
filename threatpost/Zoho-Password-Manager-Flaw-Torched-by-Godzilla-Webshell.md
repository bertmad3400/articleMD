# Zoho Password Manager Flaw Torched by Godzilla Webshell
### 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176063)
+ Date: November 8, 2021  11:38 am
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/08092242/Godzilla-e1636381376959.jpeg)
A new campaign is prying apart a known security vulnerability in the Zoho ManageEngine ADSelfService Plus password manager, researchers warned over the weekend. The threat actors have managed to exploit the Zoho weakness in at least nine global entities across critical sectors so far (technology, defense, healthcare, energy and education), deploying the Godzilla webshell and exfiltrating data.


On Sunday, Palo Alto Network’s Unit 42 researchers [said](https://unit42.paloaltonetworks.com/manageengine-godzilla-nglite-kdcsponge/) that the targeted cyberespionage campaign is distinct from the ones that the FBI and [CISA warned about](https://threatpost.com/cisa-fbi-state-backed-apts-exploit-critical-zoho-bug/174768/) in September.


The bug is a critical authentication bypass flaw – CVE-2021-40539 – that allows unauthenticated remote code execution (RCE). Zoho [patched](https://threatpost.com/zoho-password-manager-zero-day-attack/169303/) the vulnerability in September, but it’s been actively exploited in the wild starting at least as early as August when it was a zero-day, opening the corporate doors to attackers who can run amok as they get free rein across users’ Active Directory (AD) and cloud accounts.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Consequences of a successful exploit can be significant: The Zoho ManageEngine ADSelfService Plus is a self-service password management and single sign-on (SSO) platform for AD and cloud apps, meaning that any cyberattacker able to take control of the platform would have multiple pivot points into both mission-critical apps (and their sensitive data) and other parts of the corporate network via AD. It is, in other words, a powerful, highly privileged application which can act as a convenient point-of-entry to areas deep inside an enterprise’s footprint, for both users and attackers alike.


CISA’s alert explained that in the earlier attacks,  state-backed, advanced persistent threats (APTs) were deploying a specific webshell and other techniques to maintain persistence in victim environments.


Nine days after the CISA alert, Unit 42 researchers saw yet another, unrelated campaign kick off starting on Sept. 17, as a different actor started scanning for unpatched servers. On Sept. 22, after five days of harvesting data on potential targets, exploitation attempts started up and likely continued into early October.


Unit 42 researchers believe that the actor more or less indiscriminately targeted unpatched servers across the spectrum, from education to the Department of Defense, with scans of at least 370 Zoho ManageEngine servers in the U.S. alone.


“While we lack insight into the totality of organizations that were exploited during this campaign, we believe that, globally, at least nine entities across the technology, defense, healthcare, energy and education industries were compromised.” they said.


Godzilla Webshell Does Some Heavy Lifting
-----------------------------------------


Unit 42 said that after threat actors exploited [CVE-2021-40539](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-40539) to gain RCE, they quickly moved laterally to deploy several pieces of malware, relying particularly on the publicly available Godzilla webshell.


The actor uploaded several Godzilla variations to compromised servers and planted some new malware tools as well, including a custom Golang-based open-source backdoor called [NGLite](https://github.com/Maka8ka/NGLite) and a new credential-stealer that Unit 42 is tracking as KdcSponge.


“The threat actors then used either the webshell or the NGLite payload to run commands and move laterally to other systems on the network, while they exfiltrated files of interest simply by downloading them from the web server,” according to the analysis. After the actors pivoted to a domain controller, they installed the new KdcSponge stealer, which is designed to harvest usernames and passwords from domain controllers as accounts attempt to authenticate to the domain via Kerberos.


Both Godzilla and NGLite are written in Chinese and are free for the taking on GitHub.


“We believe threat actors deployed these tools in combination as a form of redundancy to maintain access to high-interest networks,” Unit 42 surmised. The researchers described Godzilla as something of a multi-function pocket knife of a webshell, noting that it “parses inbound HTTP POST requests, decrypts the data with a secret key, executes decrypted content to carry out additional functionality and returns the result via a HTTP response.”


As such, attackers can refrain from inflicting targeted systems with code that’s likely to be flagged as malicious until they’re ready to dynamically execute it, researchers said.


Using NKN to Communicate Is an Eye-Opener
-----------------------------------------


“NGLite is characterized by its author as an ‘anonymous cross-platform remote control program based on blockchain technology,'” United 42 researchers Robert Falcone, Jeff White and Peter Renals explained. “It leverages New Kind of Network ([NKN](https://nkn.org/)) infrastructure for its command and control (C2) communications, which theoretically results in anonymity for its users.”


The researchers noted that using NKN – a legitimate networking service that uses blockchain technology to support a decentralized network of peers – for a C2 channel is “very uncommon.”


“We have seen only 13 samples communicating with NKN altogether – nine NGLite samples and four related to a legitimate open-source utility called [Surge](https://github.com/rule110-io/surge) that uses NKN for file sharing.”


Threat Actor Shares TTPs with Emissary Panda
--------------------------------------------


Unit 42 said the identity of the threat actor is unclear, but researchers saw [correlations in tactics and tooling](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage) between the attacker and that of Threat Group 3390, aka [Emissary Panda](https://threatpost.com/ransomware-major-gaming-companies-apt27/162735/), APT27, Bronze Union and LuckyMouse), an APT that’s been around since 2013 and which [is believed to operate from China](https://threatpost.com/bronze-union-apt-updates-remote-access-trojans-in-fresh-wave-of-attacks/142219/).


“Specifically, as documented by SecureWorks in an article on a [previous TG-3390 operation](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage), we can see that TG-3390 similarly used web exploitation and another popular Chinese webshell called [ChinaChopper](https://threatpost.com/deadringer-targeted-exchange-servers-before-discovery/168300/) for their initial footholds before leveraging legitimate stolen credentials for lateral movement and attacks on a domain controller,” Unit 42 said. “While the webshells and exploits differ, once the actors achieved access into the environment, we noted an overlap in some of their exfiltration tooling.”


In its Sept. 16 alert, CISA recommended that organizations which spot indicators of compromise related to ManageEngine ADSelfService Plus should “take action immediately.”


Also, CISA strongly recommended domain-wide password resets and double Kerberos Ticket Granting Ticket (TGT) password resets, “if any indication is found that the NTDS.dit file was compromised.”


*Image courtesy of [AlphaCoders](https://wall.alphacoders.com/big.php?i=1012166).*


***Cybersecurity for multi-cloud environments is notoriously challenging. OSquery and CloudQuery is a solid answer. Join Uptycs and Threatpost on Tues., Nov. 16 at 2 p.m. ET for “***[***An Intro to OSquery and CloudQuery***](https://bit.ly/3wf2vTP)***,” a LIVE, interactive conversation with Eric Kaiser, Uptycs’ senior security engineer, about how this open-source tool can help tame security across your organization’s entire campus.***


[***Register NOW***](https://bit.ly/3wf2vTP) ***for the LIVE event and submit questions ahead of time to Threatpost’s Becky Bracken at*** [***becky.bracken@threatpost.com***](mailto:becky.bracken@threatpost.com)***.***




#### Tags:
[[Godzilla]] [[Zoho]] [[ManageEngine]] [[webshell]] [[CISA]] [[NGLite]] [[NKN]] [[ADSelfService]] [[Sept.]] [[said.]] [[ThreatPost]]
