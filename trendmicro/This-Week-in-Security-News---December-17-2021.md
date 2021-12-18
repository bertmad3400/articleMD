# This Week in Security News - December 17, 2021
### This week, read on Purple Fox’s infection chain observed by Trend Micro’s Managed XDR. Also, learn about the Log4j vulnerability that has the potential to cause ‘incalculable’ damage.

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/21/l/this-week-in-security-news-dec-17-2021.html
+ Date: 2021-12-17
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/week-in-security-news.jpg)





Welcome to our weekly roundup, where we share what you need to know about cybersecurity news and events that happened over the past few days. This week, read on Purple Fox’s infection chain observed by Trend Micro’s Managed XDR. Also, learn about the Log4j vulnerability that has the potential to cause ‘incalculable’ damage.


**Read on:**


[**A Look into Purple Fox’s Server Infrastructure**](/en_us/research/21/l/a-look-into-purple-fox-server-infrastructure.html)


In this blog, Trend Micro sheds light on the later stages of Purple Fox’s infection chain observed via Trend Micro’s Managed XDR, specifically, how it infects SQL databases by inserting a malicious SQL CLR assembly to achieve a persistent and stealthier execution. It should be noted that most files used in this attack are not stored on the disk and are either executed from memory after either being pulled from the command-and-control (C&C) server or encrypted, after which these are loaded by another process.


[**Log4j Software Bug Could Cause 'Incalculable' Damage: What You Need to Know**](https://www.cnet.com/tech/services-and-software/the-log4j-software-bug-could-put-your-favorite-sites-at-risk-what-you-need-to-know/)


The discovery of a major security flaw in widely used logging software sent much of the tech industry scrambling over the weekend to put in place patches before the vulnerability could be exploited by cybercriminals. If left unpatched, the bug in the Java-logging library Apache Log4j could be used by cyberattackers to take over computer servers, potentially putting favorite online services, as well as popular consumer devices, at risk of failure.


[**Patch Now Apache Log4j Vulnerability Called Log4Shell Actively Exploited**](/en_us/research/21/l/patch-now-apache-log4j-vulnerability-called-log4shell-being-acti.html)


A vulnerability in Apache Log4j, a widely used logging package for Java has been found. The vulnerability, which can allow an attacker to execute arbitrary code by sending crafted log messages, has been identified as CVE-2021-44228 and given the name Log4Shell. It was first reported privately to Apache on November 24 and was patched with version 2.15.0 of Log4j on December 9. It affects Apache Struts, Apache Solr, Apache Druid, Elasticsearch, Apache Dubbo, and VMware vCenter.


[**Kronos Ransomware Outage Drives Widespread Payroll Chaos**](https://threatpost.com/kronos-ransomware-outage-payroll-chaos/176984/)


Kronos, a workforce management platform, has been hit with a ransomware attack that it says will leave its cloud-based services unavailable for several weeks – and it’s suggesting that customers seek other ways to get payroll and other HR tasks accomplished. The outage has left cataclysmic issues for customers in its wake.


**[Collecting In the Dark: Tropic Trooper Targets Transportation and Government](/en_us/research/21/l/collecting-in-the-dark-tropic-trooper-targets-transportation-and-government-organizations.html)**


Earth Centaur, previously known as Tropic Trooper, is a long-running cyberespionage threat group that has been active since 2011. Trend Micro’s long-term monitoring of the group shows that the threat actors are equipped with new tools and techniques. The actors seem to be targeting organizations in the transportation industry and government agencies related to transport.


[**Ransomware Attack Hits Virginia Legislature**](https://www.cnn.com/2021/12/13/politics/ransomware-attack-virginia-legislature/index.html)


Governor Northam has been briefed on a ransomware attack on the Legislative Branch's Division of Legislative Automated Systems, and has directed relevant Executive Branch agencies to work quickly to offer any help in assessing and responding to this ongoing situation. The Division of Legislative Automated Systems (DLAS) is the IT agency for the Virginia General Assembly. The General Assembly relies on DLAS for networking infrastructure, desktop computing and printing services, according to its website.


[**New Yanluowang Ransomware Found to be Code-Signed, Terminates Database-Related Processes**](/en_us/research/21/l/yanluowang-ransomware-code-signed-terminates-database-processes.html)


In this blog, Trend Micro analyzes new samples of the Yanluowang ransomware, a recently discovered ransomware family. One interesting aspect of these samples is that the files are code-signed using a valid digital signature, which was either stolen or fraudulently signed. They also terminate various processes, including Veeam and SQL, which are related to database and backup management.


[**Ransomware Suspect Arrested Over Attacks on 'High-Profile' Organizations**](https://www.zdnet.com/article/ransomware-suspect-arrested-over-attacks-on-high-profile-organisations/)


Europol's European Cybercrime Centre has worked with the Romanian National Police and FBI on the arrest of a suspected ransomware affiliate who is alleged to have targeted high-profile organizations and companies for their sensitive data. Europol said a 41-year old man is accused of targeting organizations in ransomware attacks, encrypting files and stealing sensitive data. He's suspected of demanding a "sizeable" ransom payment in cryptocurrency, and threatening to leak the stolen data if the victim didn't give in to the extortion attempt.


[**Volatile and Adaptable: Tracking the Movements of Modern Ransomware**](/en_us/research/21/l/volatile-and-adaptable-tracking-the-movements-of-modern-ransomware.html)


In the first half of 2021, Trend Micro saw modern ransomware threats active and evolving, using double extortion techniques to victimize targets. Unlike traditional ransomware tactics, current adversaries use private data stolen from victims’ machines to add pressure and threaten to release valuable information onto public leak sites if the ransom remains unpaid. Further into the year, our tracking of these threats, as well as of older ransomware families, shows which attacks are gaining momentum and which families are particularly dangerous for enterprises and private users. 


[**Volvo Confirms R&D Data Stolen in Breach**](https://www.darkreading.com/threat-intelligence/volvo-confirms-r-d-data-stolen-in-breach)


Volvo Cars has confirmed a limited amount of its R&D property was stolen when a third party illegally accessed one of its file repositories. After detecting the breach, Volvo implemented countermeasures, including steps to prevent further access to its property, and alerted authorities.


[**Addressing Cloud-Related Threats to the IoT**](https://www.trendmicro.com/vinfo/tmr/?/us/security/news/internet-of-things/addressing-cloud-related-threats-to-the-iot)


The Covid-19 pandemic has made digital transformation an urgent necessity for organizations, pushing the adoption of a hybrid work model marked by remote connection and enabled by the convergence of the internet of things (IoT) and cloud computing.While large-scale IoT deployments provide a number of benefits, more IoT devices — and consequently, a more complex IoT ecosystem — also mean more security vulnerabilities from the edge to the cloud.


What do you think about the Log4j vulnerability? Share in the comments below or follow me on Twitter to continue the conversation: [@JonLClay](https://www.twitter.com/@JonLClay).  









## Tags:

#### Threatactor:
[[threatactor.name=Tropic Trooper]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Chaos]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Agriculture]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Oman]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=Romania]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Log4j]] [[Ransomware]] [[Iot]] [[Sql]] [[Volvo]] [[Trend Micro]]
#### CVE's
[[CVE-2021-44228]]

