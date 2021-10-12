# Chinese hackers use Windows zero-day to attack defense, IT firms
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/chinese-hackers-use-windows-zero-day-to-attack-defense-it-firms/)
+ Date: October 12, 2021
+ Author: Sergiu Gatlan


## Article:
![Chinese hackers use Windows zero-day to attack defense, IT firms](https://www.bleepstatic.com/content/hl-images/2021/03/01/Hacker-Light-Surveillance.jpg)


A Chinese-speaking hacking group exploited a zero-day vulnerability in the Windows Win32k kernel driver to deploy a previously unknown remote access trojan (RAT).


The malware, known as **MysterySnail**, was found by Kaspersky security researchers on multiple Microsoft Servers between late August and early September 2021.


They also found an elevation of privilege exploit targeting the Win32k driver security flaw tracked as [**CVE-2021-40449**](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-40449) and patched by Microsoft today, as part of [this month's Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/microsoft-october-2021-patch-tuesday-fixes-4-zero-days-71-flaws/).


"Besides finding the zero-day in the wild, we analyzed the malware payload used along with the zero-day exploit, and found that variants of the malware were detected in widespread espionage campaigns against IT companies, military/defense contractors, and diplomatic entities," Kaspersky researchers Boris Larin and Costin Raiu [said](https://securelist.com/mysterysnail-attacks-with-windows-zero-day/104509/).


"Code similarity and re-use of C2 infrastructure we discovered allowed us to connect these attacks with the actor known as IronHusky and Chinese-speaking APT activity dating back to 2012."


The Chinese-speaking IronHusky APT was [first spotted by Kaspersky in 2017](https://securelist.com/apt-trends-report-q3-2017/83162/) while investigating a campaign targeting Russian and Mongolian government entities, aviation companies, and research institutes with the end goal of collecting intelligence on Russian-Mongolian military negotiations.


One year later, Kaspersky researchers [observed them](https://securelist.com/apt-trends-report-q1-2018/85280/) exploiting [CVE-2017-11882](https://msrc.microsoft.com/update-guide/en-us/vulnerability/CVE-2017-11882) Microsoft Office memory corruption vulnerability to spread RATs typically used by Chinese-speaking groups, including PlugX and PoisonIvy.


Privilege escalation zero-day used to deploy RATs
-------------------------------------------------


The privilege escalation exploit used to deploy the MysterySnail RAT deployed in these attacks targets Windows client and server versions, from Windows 7 and Windows Server 2008 to the latest versions including Windows 11 and Windows Server 2022, unpatched against CVE-2021-40449.


While the zero-day exploit spotted by Kaspersky in the wild also supports targeting Windows client versions, it was only discovered on Windows Server systems.


The MysterySnail RAT is designed to collect and exfiltrate system information from compromised hosts before reaching out to its command-and-control server for further commands.


MysterySnail can perform various tasks on infected machines, ranging from spawning new processes and killing already running ones to launching interactive shells and launching a proxy server with support for up to 50 simultaneous connections.


"The malware itself is not very sophisticated and has functionality similar to many other remote shells," the two researchers added.


"But it still somehow stands out, with a relatively large number of implemented commands and extra capabilities like monitoring for inserted disk drives and the ability to act as a proxy."


Further technical details and indicators of compromise can be found in [the report published by Kaspersky today](https://securelist.com/mysterysnail-attacks-with-windows-zero-day/104509/).




#### Tags:
[[Windows]] [[Kaspersky]] [[zero-day]] [[Chinese-speaking]] [[Microsoft]] [[malware]] [[MysterySnail]] [[Bleeping Computer]]
