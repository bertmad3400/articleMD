# ‘Elephant Beetle’ Lurks for Months in Networks
### The group blends into an environment before loading up trivial, thickly stacked, fraudulent financial transactions too tiny to be noticed but adding up to millions of dollars.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177393
+ Date: 2022-01-05T22:18:28+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/05145410/elephant-beetle-e1641412467995.jpg)

Researchers have identified a threat group that’s been quietly siphoning off millions of dollars from financial- and commerce-sector companies, spending months patiently studying their targets’ financial systems and slipping in fraudulent transactions amongst regular activity.


The Sygnia Incident Response team has been tracking the group, which it named Elephant Beetle, aka TG2003, for two years.


In a Wednesday [report](https://blog.sygnia.co/elephant-beetle-an-organized-financial-theft-operation), the researchers called Elephant Beetle’s attack relentless, as the group has hidden “in plain sight” without the need to develop exploits.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Maybe Elephant Beetle doesn’t have exploits, but the attackers certainly don’t show up empty-handed. They rely on an arsenal of more than 80 unique tools and scripts to operate undetected “for vast amounts of time” as they patiently plant their bogus transactions, Sygnia said, “blending in with the target’s environment and going completely undetected while it quietly liberates organizations of exorbitant amounts of money.”


Elephant Beetle primarily focuses its attention on the Latin American market, but it doesn’t spare organizations that aren’t based there. Sygnia’s IR team recently discovered and responded to one incident at a company based in the U.S. that runs a branch in Latin America. “As such, both regional and global organizations should be on their guard,” Sygnia warned.


A Java-Chugging Bug
-------------------


This beetle adores Java. The group is “highly proficient” with Java-based attacks and often targets legacy Java apps running on Linux machines – primarily, the Java-based web servers WebSphere and WebLogic – as a means of initial entry to a target environment, the researchers explained. Beyond that, Elephant Beetle even deploys its own, complete Java web application to do the gang’s bidding on compromised machines that are, meanwhile, chugging along, running legitimate apps.


Sygnia’s full report ([PDF](https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf?__hstc=&__hssc=&hsCtaTracking=189ec409-ae2d-4909-8bf1-62dcdd694372%7Cca91d317-8f10-4a38-9f80-367f551ad64d)) lays out Elephant Beetle’s modus operandi, in-depth analysis of its capabilities, actionable insights, incidents of compromise (IOCs) and guidelines for defending against the attacks.


Attack Stages
-------------


But in a nutshell, here’s how the attack progresses:


1. For up to a month, the group builds operational cyber-capabilities in the compromised victim’s network, studying the digital landscape and planting backdoors, while customizing its tools to work within the victim’s network.
2. The attackers spend several months studying the victim’s environment, focusing on the financial operations and identifying any flaws. During this stage, Elephant Beetle observes the victim’s software and infrastructure to understand the technical process of legitimate financial transactions.
3. Next, the group injects fraudulent transactions into the network. “These transactions mimic legitimate behavior and siphon off incremental amounts of money from the victim, a classic salami tactic,” Sygnia researchers explained, referring to the so-called salami slicing form of financial cyberattack, in which the ripped-off funds are so insignificant that a single case goes completely unnoticed. The amounts may seem trivial, but the group keeps stacking them up to what amounts to millions of dollars before the attackers move on.
4. No biggie if the group’s activity is discovered and blocked: They’ll just lay low for a few months, then circle back to target a different system.


Picking Apart Vulnerabilities
-----------------------------


The group exploits known vulnerabilities to infiltrate organizations, then uses the compromised servers to establish persistent vectors in the network and to pivot to credential harvesting and lateral movement.


Sygnia observed the group using default credentials for authenticating myWebMethods (“WMS”) and the QLogic web management interface.


“For example, the group leveraged the default password ‘manage’ of the privileged system user ‘sysadmin’ of WMS servers,” researchers detailed.


Elephant Beetle also exploited the following four vulnerabilities to gain network access:


1. Primefaces Application Expression Language Injection ([CVE-2017-1000486](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-1000486)).
2. WebSphere Application Server SOAP Deserialization Exploit ([CVE-2015-7450](https://www.ibm.com/support/pages/security-bulletin-vulnerability-apache-commons-affects-ibm-websphere-application-server-cve-2015-7450)).
3. SAP NetWeaver Invoker Servlet Exploit ([CVE-2010-5326](https://nvd.nist.gov/vuln/detail/CVE-2010-5326)).
4. SAP NetWeaver ConfigServlet Remote Code Execution ([EDB-ID-24963](https://vuldb.com/?id.8517)).


All of the quartet of flaws enable the actors to execute arbitrary code remotely via a specially crafted and obfuscated web shell.


The security firm gave the following example of a web request that was sent by the threat group to one of the victim’s SAP portals. It exploits the SAP ConfigServlet remote code-execution issue and contains a one-line command that creates a web shell.


Laying Low
----------


In order to stay undetected for months at a time, Elephant Beetle lays low, engaged in low or no activity, and/or mimicks its surroundings by doing things like dropping the web shells into the resources folders of each web app, or by disguising themselves as fonts, images, CSS and JS resources, with similar names to original files in these folders – but with a ‘.JSP’ extension.


They ramp up when they’re ready to attack, using WAR archives to pack payloads. This tactic is considered to be “super-persistent” on some web servers, specifically WebSphere and WebMethods, “due to the fact that removal of the web shell files is insufficient, as the web pages are being loaded and held in the server’s process memory,” the researchers said.


Other tactics, techniques and procedures (TTPs) used by the group include:


* Modifying or replacing default web page files, enabling “almost guaranteed” access to their web shell from other servers or from the internet – access that’s not classified as suspicious.
* Pen-testing tactics: Elephant Beetle uses a custom Java-written scanner that supports scanning IP range/list of IP addresses for a specific port or for an HTTP interface. “It is used to scan targets in the asset’s proximity and then leveraged to identify installed applications, which could be exploited,” Sygnia said. Other pen-testing TTPs included downloading app source code.


Mal Hombres
-----------


Sygnia found a number of ties to Spanish-speaking countries:


* Hardcoded keywords and phrases in the group’s tools included, for example, a code variable named “ELEPHANTE” (mangled Spanish for elephant), as well as in output file names that the group uses, such as “windows\_para\_linux.”
* Most of the group’s command-and-control (C2) servers have IPs located in Mexico.
* The group’s targets are mainly Latin American. “For example, one of the tools that the group uses to scan internal networks ‘p.j’ was uploaded to VirusTotal from Argentina,” Sygnia said. “This again suggests the group targets Spanish-speaking victims.”


Defending Against Elefante Attacks
----------------------------------


Keeping up to date with patches is a no-brainer – particularly given how old the vulnerabilities are that Elephant Beetle is exploiting. Between that and other everyday security best practices, such as avoiding clear-text credentials used in scripts, Sygnia advised:


* Avoid using the ‘xp\_cmdshell’ procedure and disable it on MS-SQL servers. Monitor for configuration changes and the use of ‘xp\_cmdshell’.
* Monitor WAR deployments and validate that the packages deployment functionality is included in the logging policy of the relevant applications.
* Hunt and monitor for the presence and creation of suspicious .class file in the WebSphere applications temp folders.
* Monitor for processes that were executed by either web server parent services processes (i.e., ‘w3wp.exe’, ‘tomcat6.exe’) or by database-related processes (i.e., ‘sqlservr.exe’).
* Implement and verify segregation between DMZ and internal servers.


As well, organizations would be well-advised to proactively hunt for Elephant Beetle IOCs and TTPs, which it listed in its report, within their networks.


***Password** **Reset:** **[On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):** Fortify 2022 with a password-security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the new password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken. **[Register & stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)** – sponsored by Specops Software.*


*Image courtesy of* [*Phil*](https://www.flickr.com/photos/shuttersparks/4604552153)*.* [*Licensing details*](https://creativecommons.org/licenses/by-nc-sa/2.0/)*.*





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=cmd]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Agriculture]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mexico]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Argentina]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Sygnia]] [[Websphere]] [[ThreatPost]]
#### CVE's
[[CVE-2017-1000486]] [[CVE-2015-7450]] [[CVE-2010-5326]]

