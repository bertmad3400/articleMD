# RedCurl corporate espionage hackers resume attacks with updated tools
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/redcurl-corporate-espionage-hackers-resume-attacks-with-updated-tools/)
+ Date: November 18, 2021
+ Author: Ionut Ilascu


## Article:
![RedCurl corporate espionage hackers resume attacks with updated tools](https://www.bleepstatic.com/content/hl-images/2021/11/18/RedCurl.jpg)


A crew of highly-skilled hackers specialized in corporate espionage has resumed activity, one of their victims this year being a large wholesale company in Russia.


Tracked as RedCurl, the group attacked the Russian business twice this year, each time using carefully constructed spear-phishing emails with initial-stage malware.


### Increasing the victim count


Active since 2018, [RedCurl](https://www.bleepingcomputer.com/news/security/stealthy-redcurl-hackers-steal-corporate-documents/) is responsible for at least 30 attacks against businesses in Russia (18 of them), Ukraine, Canada, Norway, the UK, and Germany, the latest four of them occurring this year.


![RedCurl victim geography](https://www.bleepstatic.com/images/news/u/1100723/2021/RedCurlVicCount.jpg)


The hackers are proficient at staying undetected for long periods, between two and six months, before stealing corporate data (staff records, documents about legal entities, court records, internal files, email history).


### Hitting the same company twice


Researchers at cybersecurity company [Group-IB noticed](https://www.group-ib.ru/resources/threat-research/red-curl-2.html) a seven-month gap in RedCurl’s activity, which the hackers used to add significant improvements to their set of custom tools and attack methods.


Among the hacker’s latest victims is one of Russia’s largest wholesale companies, which supplies chain stores and other wholesalers with home, office, and leisure goods.


For reasons that remain unknown, RedCurl attacked this company twice, gaining initial access via emails impersonating the company’s human resources department announcing bonuses and the government services portal.


![RedCurl spear-phishing emails to a large wholesale company in Russia](https://www.bleepstatic.com/images/news/u/1100723/2021/RedCurlEmails.jpg)


In both cases, the goal was to deploy on the employee’s computer a malware downloader (RedCurl.InitialDropper) hidden in an attached document that could launch the next stage of the attack.


During the investigation, Group-IB found that the RedCurl extended the attack chain to five stages, from the previously observed three or four steps.


![Typical RedCurl kill chain](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)


The hackers were careful not to raise any suspicion when the recipient opened the malicious document that launched the initial dropper, so they included a well-crafted decoy file with content related to the organization.


The dropper would fetch the RedCurl.Downloader tool, which collected info about the infected machine and delivered it to a command and control server (C2), and also initiated the next stage of the attack.


### Updated toolset


Group-IB discovered that the hackers now used RedCurl.Extractor, a modified version of the RedCurl.Dropper they found in previous attacks from this threat actor.


The purpose of this tool was only to prepare the final step of the attack, which involved achieving persistence on the system.


The researchers note that RedCurl has shifted from the typical use of batch and PowerShell scripts to executable files and that antivirus software failed to detect the initial infection or the attacker moving laterally on the victim network.


However, the improvements to RedCurl’s toolset appear to have been rushed, as Group-IB discovered a logical error in one of the commands. One explanation is that the group had little time to start the attack and could not properly test their tools.


Group-IB has published a [report](https://www.group-ib.ru/resources/threat-research/red-curl-2.html) today with indicators of compromise and technical information on RedCurl’s updated set of tools and their functionality:


* RedCurl.InitialDropper: LNK file used in the initial infection stage, downloads batch or PowerShell scripts from the C2 that get malware for the next step
* RedCurl.Downloader (new tool): intermediary stage downloader that collects data about the infected system, downloads and deploys malware for the next stage
* RedCurl.Extractor: DLL file equivalent to RedCurl.Dropper, extracts the legitimate 7-Zip utility, downloads and installs the next stage malware
* RedCurl.FSABIN: binary equivalent of the old RedCurl.FirstStageAgent, gets commands from hacker-controlled HTTP servers
* RedCurl.CHABIN1: a fork of FSABIN
* RedCurl.CHABIN2: similar to CHABIN1, determines the proxy server settings to connect the infected system to servers controlled by the hackers


Despite not being as active as in other years, RedCurl maintains its sophistication and remains an advanced threat actor capable to stay undetected for months.


Group-IB says that of the four attacks identified this year, two were against the same target. However, they expect more victims to appear since RedCurl’s updated tools have been detected in the wild with increased frequency.




#### Tags:
[[Group-IB]] [[RedCurl]] [[RedCurl’s]] [[malware]] [[Bleeping Computer]]
