# 12 New Flaws Used in Ransomware Attacks in Q3
### The Q3 2021 report revealed a 4.5% increase in CVEs associated with ransomware and a 3.4% increase in ransomware families compared with Q2 2021.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176137)
+ Date: November 9, 2021  1:06 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/05121727/ransomware7-e1636129059903.jpg)
A dozen new vulnerabilities were used in ransomware attacks this quarter, bringing the total number of bugs associated with ransomware to 278. That’s a 4.5 percent increase over Q2, according to researchers.


Five of the newbies can be used to achieve remote code execution (RCE), while two can be used to exploit web apps and launch denial-of-service (DoS) attacks. That’s never good news, but it’s particularly teeth-grinding given that this quarter also saw distributed DoS (DDoS) attacks [shatter records](https://threatpost.com/ddos-attacks-records-q3/176082/), according to a separate study.


The news about the new vulnerabilities that have been pounced on by ransomware operators comes from Ivanti’s Q3 2021 ransomware index spotlight report, [published](https://www.ivanti.com/lp/security/reports/2021-q3-ransomware-index-spotlight-report) on Tuesday and conducted with Cyber Security Works and Cyware.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

Aaron Sandeen, Cyber Security Works CEO, said in a press release that Q3 was a copy-paste of the ransomware trends from the rest of the year. Namely, “We continued to see ransomware attacks aggressively increase in sophistication and frequency in Q3.”


The Early Bird Gets the Worm
----------------------------


The quarterly ransomware analysis also found that ransomware groups are still finding and exploiting zero-day weaknesses, before CVEs are hatched and patched. Case in point: The much-reviled [REvil](https://threatpost.com/revil-affiliates-arrested-doj-europol/176087/) ransomware gang found and exploited flaws in Kaseya VSA software as the company’s security team was still working on a trio of patches.


On July 2, the [REvil gang wrenched open](https://threatpost.com/kaseya-patches-zero-day-exploits/167548/) the three zero-days in Kaseya’s Virtual System/Server Administrator (VSA) platform in [more than 5,000 attacks](https://securelist.com/revil-ransomware-attack-on-msp-companies/103075/). As of July 5, the worldwide assault had been unleashed in 22 countries, reaching not only Kaseya’s managed service provider (MSP) customer base but also, given that many of them use VSA to manage the networks of other businesses, clawing at those MSPs’ own customers.


Ransomware Numbers Creep Up on All Fronts
-----------------------------------------


The third quarter also saw nine new vulnerabilities with lower severity ratings being associated with ransomware. Also, the Q3 ransomware index update for 2021 identified ransomware groups expanding their attack arsenal with 12 new vulnerability associations in Q3,


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/09120618/Ivanti-scaled-e1636477594339.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/09120618/Ivanti-scaled-e1636477594339.jpg)


Riding Brand-New Bugs, Bearing Shiny New Toys
---------------------------------------------


Q3 analysis also identified five new ransomware families, bringing the total to 151. The new ransomware groups were quick to jump on some of the most dangerous vulnerabilities out there just weeks after they began to trend in the wild, such as [PrintNightmare](https://threatpost.com/microsoft-unpatched-printnightmare-zero-day/168613/), [PetitPotam](https://threatpost.com/microsoft-petitpotam-poc/168163/) and [ProxyShell](https://threatpost.com/tortilla-exchange-servers-proxyshell/175967/).


The techniques being used in ransomware attacks are also getting more sophisticated. One example cited in Ivanti’s analysis is dropper as-a-service – ​​a service that allows technically non-savvy/criminally inclined actors to distribute malware through dropper programs that can execute a malicious payload onto a victim’s computer.


Another is trojan-as-a-service, also known as malware-as-a-service: a service that lets anyone with an internet connection rent customized malware services, allowing them to acquire, implement and cash in on the service, all on the cloud with zero installation.


All bad things seem to be rentable: [Ransomware-as-a-service (RaaS)](https://threatpost.com/ransomware-as-a-service-intel-sharing/167508/), for example, is fueling the spread of ransomware, sparing crook wannabes the need to tangle with code.


Old Wine, New Ransomware Bottles
--------------------------------


The report also found that three vulnerabilities dating to 2020 or earlier became newly associated with ransomware in Q3 2021, bringing the total count of older vulnerabilities associated with ransomware to 258: a whopping 92.4 percent of all vulnerabilities tied to ransomware.


The analysis pointed to the [Cring](https://threatpost.com/hackers-exploit-flaw-cring-ransomware/165300/) ransomware group being a notable example: The gang [targeted](https://thehackernews.com/2021/09/cring-ransomware-gang-exploits-11-year.html) two older ColdFusion vulnerabilities – CVE-2009-3960 and CVE-2010-2861 – that have been patched for 11 years.


Srinivas Mukkamala, Ivanti’s senior vice president of security products, said in a [press release](https://finance.yahoo.com/news/ransomware-index-spotlight-report-reveals-130000954.html) that automation can save your bacon: “It’s critical that organizations take a proactive, risk-based approach to patch management and leverage automation technologies to reduce the mean time to detect, discover, remediate, and respond to ransomware attacks and other cyber-threats.”


Anuj Goel, Cyware CEO, was quoted as saying yes to the automation, and also to intel sharing to protect organizations from ransomware: “This research underscores that ransomware is continuing to evolve and is becoming more dangerous based on the catastrophic damage it can inflict on target organizations. What is more complex for many organizations is the inability of vertical industries to rapidly share specific IOC’s irrespective of their industry, in a way that is easy to curate, operationalize and disseminate to take action before an attack hits.


“Managing organizational risk means companies should be looking to a collective defense strategy to have continuously visibility into the attack and risk surfaces respectively, to reduce huge losses to reputation, customers, and finances. The more that cyber teams can tie into IT automation and processes, the better and more efficient they’ll be in countering ransomware.”


***Cybersecurity for multi-cloud environments is notoriously challenging. OSquery and CloudQuery is a solid answer. Join Uptycs and Threatpost on Tues., Nov. 16 at 2 p.m. ET for “***[***An Intro to OSquery and CloudQuery***](https://bit.ly/3wf2vTP)***,” a LIVE, interactive conversation with Eric Kaiser, Uptycs’ senior security engineer, about how this open-source tool can help tame security across your organization’s entire campus.***


[***Register NOW***](https://bit.ly/3wf2vTP) ***for the LIVE event and submit questions ahead of time to Threatpost’s Becky Bracken at*** [***becky.bracken@threatpost.com***](mailto:becky.bracken@threatpost.com)***.***




#### Tags:
[[ransomware]] [[Q3]] [[Ivanti’s]] [[ThreatPost]]
