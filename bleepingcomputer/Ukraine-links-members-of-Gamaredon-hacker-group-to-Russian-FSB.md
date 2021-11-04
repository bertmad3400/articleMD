# Ukraine links members of Gamaredon hacker group to Russian FSB
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/ukraine-links-members-of-gamaredon-hacker-group-to-russian-fsb/)
+ Date: November 4, 2021
+ Author: Bill Toulas


## Article:
![Hidden attackers](https://www.bleepstatic.com/content/hl-images/2020/12/03/Stalker.jpg)


SSU and the Ukrainian secret service say they have identified five members of the Gamaredon hacking group, a Russian state-sponsored operation known for targeting Ukraine since 2014.


This Gamaredon hacking group, tracked as Armageddon by the SSU, is allegedly operated under the FSB (Russian Federal Security Service) and is believed to be responsible for over 5,000 attacks in Ukraine since the operation began.


Over the last seven years, Ukraine says the actors targeted over 1,500 government, public and private entities in the country, aiming to collect intelligence, disrupt operations, and take control over critical infrastructure facilities.


The five men accused of taking part in these attacks were identified by SSU investigators who claim to have unequivocal evidence of their involvement, coming from communication interceptions.



The investigators underline that they managed to identify the hackers despite using their own custom malware, anonymization tools, and were generally very diligent in hiding their digital trace.


The names of the five individuals the SSU claims are part of the Gamaredon operation are Sklianko Oleksandr Mykolaiovych, Chernykh Mykola Serhiovych, Starchenko Anton Oleksandrovych, Miroshnychenko Oleksandr Valeriovych, and Sushchenko Oleh Oleksandrovych.



![Identities of the five identified Armageddon members](https://www.bleepstatic.com/images/news/u/1220909/police/agents.jpg)**Identities of the five identified Armageddon members**  
*Source:* SSU
All five were reportedly operating under the guidance of the 18th Center of Information Security of the FSB in Moscow.


Moreover, all of them are officers of the Crimean FSB who sided with Russia during the peninsula's occupation in 2014. 


As such, the Ukrainian authorities are also accusing them of treason, espionage, unauthorized inference in the work of electronic computers, and distribution and use of malware.


Although the five men haven’t been arrested, the SSU sees their exposure as an effective neutralization measure.


Entire toolset and tactics exposed
----------------------------------


The SSU has published [a technical activity report](https://ssu.gov.ua/uploads/files/DKIB/%D0%A2%D0%B5%D1%85%D0%BD%D1%96%D1%87%D0%BD%D0%B8%D0%B9%20%D0%B7%D0%B2%D1%96%D1%82%20%D0%B4%D1%96%D1%8F%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%96%20%D0%90%D1%80%D0%BC%D0%B0%D0%B3%D0%B5%D0%B4%D0%BE%D0%BD.pdf) on Gamaredon, where they lay down several key points around the group’s toolset and tactics.


The report says the group is known to [use Outlook macros](https://www.bleepingcomputer.com/news/security/gamaredon-hackers-use-outlook-macros-to-spread-malware-to-contacts/) and the deployment of [EvilGnome backdoor](https://www.bleepingcomputer.com/news/security/new-evilgnome-backdoor-spies-on-linux-users-steals-their-files/) to compromise systems.


Other details include highly targeted vulnerabilities such as the WinRAR CVE-2018-20250 vulnerability, which existed for [almost two decades](https://www.bleepingcomputer.com/news/security/19-year-old-winrar-rce-vulnerability-gets-micropatch-which-keeps-ace-support/), and CVE-2017-0199, a remote code execution flaw on MS Office.


Moreover, it is mentioned that the actors used removable media to plant malware on offline systems and then moved laterally in isolated networks, using this tactic from 2014 until 2021.


Finally, a novel malware tool named “Pteranodon” is detailed in the report, which is a modular remote administration tool (RAT) with powerful anti-analysis and info-collection features.



![Pteranodon exfiltrating data to the C2](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/c2%20exfiltration.jpg)**Pteranodon exfiltrating data to the C2**  
*Source: SSU*
According to SSU, Pteranodon was derived from “Pterodo,” a widely available malware circulating Russian hacking forums since 2016.


The group continued to create new powerful DLL modules for Pteranodon, so it has evolved significantly over the past five years.


The release of these technical details will empower analysts to assign attribution on past attacks and momentarily reduce Russian state actors' operational effectiveness.




#### Tags:
[[Gamaredon]] [[FSB]] [[malware]] [[Bleeping Computer]]
