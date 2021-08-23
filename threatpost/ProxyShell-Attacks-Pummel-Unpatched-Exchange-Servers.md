# ProxyShell Attacks Pummel Unpatched Exchange Servers
### CISA is warning about a surge of ProxyShell attacks, as Huntress discovered 140 webshells launched against 1,900 unpatched Microsoft Exchange servers.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168879)
+ Date: August 23, 2021  2:54 pm
+ Author: Becky Bracken


## Article:
![microsoft exchange server](https://media.threatpost.com/wp-content/uploads/sites/103/2020/04/07164022/microsoft-exchange.jpg)
Over the weekend, the Cybersecurity & Infrastructure Security Agency (CISA) issued an urgent alert that attackers are [actively attacking ProxyShell vulnerabilities](https://us-cert.cisa.gov/ncas/current-activity/2021/08/21/urgent-protect-against-active-exploitation-proxyshell) in unpatched Microsoft Exchange Servers, joining researchers in urging organizations to immediately install the latest Microsoft Security Update.


Security researchers at Huntress reported seeing [ProxyShell vulnerabilities](https://www.huntress.com/blog/rapid-response-microsoft-exchange-servers-still-vulnerable-to-proxyshell-exploit) being actively exploited throughout the month of August to install backdoor access once the [ProxyShell exploit code](https://peterjson.medium.com/reproducing-the-proxyshell-pwn2own-exploit-49743a4ea9a1) was published on Aug. 6. But starting Friday night, Huntress reported a “surge” in attacks after finding 140 webshells launched against 1,900 unpatched Exchange servers.


“Impacted orgs thus far include building mfgs, seafood processors, industrial machinery, auto repair shops, a small residential airport and more,” Huntress researcher [Kyle Hanslovan said in an Aug. 20 tweet](https://twitter.com/KyleHanslovan/status/1428804893423382532).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Considering the industries represented, it’s unsurprising that CISA jumped in to call for organizations to shore up defenses against the wave of attacks.


**Webshells & LockFile Ransomware**
-----------------------------------


Huntress researcher John Hammond, working in collaboration with Kevin Beumont and Rich Warren, were able to establish that in addition to webshell attacks, threat actors were also exploiting ProxyShell to deliver [LockFile ransomware](https://pbs.twimg.com/media/E9TmPo6XMAYCnO-?format=jpg&name=4096x4096).


The most common webshells deployed against [Exchange servers](https://threatpost.com/how-to-reduce-exchange-server-downtime/168344/) was XSL Transform (used 130 times), followed by Encrypted Reflected Assembly Loader, Comment Separation and Obfuscation of the “unsafe” Keyword, Jscript Base64 Encoding and Character Typecasting and Arbitrary File Uploader, according to Huntress.


The Huntress team analyzed one system infected with ProxyShell and LockFile ransomware and found a unique tactic.


“The configuration file for the Exchange internet service was modified to include a new ‘virtual directory,’ which practically redirects one URL endpoint to another location on the filesystem,” Huntress’ John Hammond wrote.


He explained this helps an attacker hide the webshell outside of areas monitored by ASP directories.


“If you don’t know to look for this, this is going to slip under the radar and the hackers will persist in the target environment. Additionally, the hidden webshell discovered on this host uses the same XML/XLS transform technique that we have seen previously,” Hammond advised.



[ProxyShell attacks](https://threatpost.com/exchange-servers-attack-proxyshell/168661/) were first publicly documented at Black Hat in early August by Devcore researcher Orange Tsai. Just a week later, a Shodan scan by the SANS Internet Storm Center’s Jan Kopriva found more than 30,000 vulnerable Exchange Servers.


Yet, many servers remain unpatched against ProxyShell attacks.


**Microsoft Messaging to Blame for Lag in Patching?**
-----------------------------------------------------


Researcher Kevin Beaumont is [critical of Microsoft’s messaging efforts](https://doublepulsar.com/multiple-threat-actors-including-a-ransomware-gang-exploiting-exchange-proxyshell-vulnerabilities-c457b1655e9c) surrounding the vulnerability and the critical need for its customers to update their Exchange Server security.


“Microsoft decided to downplay the importance of the patches and treat them as a standard monthly Exchange patch, which [has] been going on for – obviously – decades,” Beaumont explained. “You may remember how much negative publicity March’s Exchange patches caused Microsoft, with headlines such as ‘Microsoft emails hacked’.”


But Beaumont said these remote code execution (RCE) vulnerabilities are “…as serious as they come.”


“To make matters worse, Microsoft failed to allocate CVEs for these vulnerabilities until July – 4 months after the patches were issued,” he wrote. “Given many organizations’ vulnerability [to] manage via CVE, it created a situation where Microsoft’s customers were misinformed about the severity of one of the most critical enterprise security bugs of the year.”


In order of patching priority, according to Beaumont, the vulnerabilities are: CVE-2021–34473, CVE-2021–34523 and CVE-2021–31207.


Beaumont said he worked with Shodan to add a plug-in to identify vulnerable systems. He added that Microsoft should be asked to pay bug bounties for on-premise Exchange servers and criticized the company, saying it had “completely failed to deal with their own problems” while openly touting bugs in other vendors’ problems, like [Netgear](https://www.microsoft.com/security/blog/2021/06/30/microsoft-finds-new-netgear-firmware-vulnerabilities-that-could-lead-to-identity-theft-and-full-system-compromise/).


For its part, CISA is cautioning every organization to update Exchange software as soon as possible.


“CISA strongly urges organizations to identify vulnerable systems on their networks and immediately apply Microsoft’s Security Update from May 2021 – which remediates all three ProxyShell vulnerabilities – to protect against these attacks,” the alert said.  

***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[ProxyShell]] [[Microsoft]] [[LockFile]] [[webshell]] [[Microsoft’s]] [[ThreatPost]]
