# Jenkins Hit as Atlassian Confluence Cyberattacks Widen
### Patch now: The popular biz-collaboration platform is seeing mass scanning and exploitation just two weeks after a critical RCE bug was disclosed.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169249)
+ Date: September 7, 2021  12:07 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/07115800/confluence-e1631030298396.jpg)
A just-patched, critical remote code-execution (RCE) vulnerability in the Atlassian Confluence server platform is suffering wide-scale exploitation, the Feds have warned – as evidenced by an attack on the popular Jenkins open-source automation engine.


Atlassian Confluence is a collaboration platform where business teams can organize its work in one place: “Dynamic pages give your team a place to create, capture, and collaborate on any project or idea,” according to [the website](https://www.atlassian.com/software/confluence/guides/get-started/confluence-overview). “Spaces help your team structure, organize and share work, so every team member has visibility into institutional knowledge and access to the information they need to do their best work.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


In other words, it can house a treasure trove of sensitive business information as well as supply-chain information that could be used for follow-on attacks on partners, suppliers and customers.


**Jenkins Hack – Just a Cryptomining Hit**
------------------------------------------


For its part, Jenkins identified a “successful attack against our deprecated Confluence service,” it said in [a statement](https://www.jenkins.io/blog/2021/09/04/wiki-attacked/) over the weekend. Thankfully, “we have no reason to believe that any Jenkins releases, plugins or source code have been affected,” the team added.


The attackers were able to exploit the bug in question ([CVE-2021-26084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-26084)) to install a Monero cryptominer in the container running the service, according to the statement – no cyberespionage in this case. The team took the server offline immediately and rotated all passwords, and there’s no plan to bring Confluence back, it said.


“An attacker would not be able to access much of our other infrastructure,” the statement continued, adding that the server hasn’t been used in daily operations since late 2019. “Confluence did integrate with our integrated identity system which also powers Jira, Artifactory, and numerous other services.”


The hack comes on the heels of an urgent pre-Labor Day warning from U.S. Cybercommand that the flaw is firmly in the sites of cybercriminals aiming at U.S. businesses, less than 10 days after it was disclosed on August 25:



It’s a finding that echoes researchers from Bad Packets, who said [via Twitter](https://twitter.com/bad_packets/status/1433157632370511873) that it began to see mass scanning and exploitation for CVE-2021-26084 around Sept. 1.


On Tuesday, Japan-CERT [issued guidance](https://www.jpcert.or.jp/english/at/2021/at210037.html) that active exploits were being deployed in Japan as well.


**RCE with CVE-2021-26084**
---------------------------


The bug is an Object-Graph Navigation Language (OGNL) injection vulnerability that affects Confluence Server and Data Center (affected versions are before version 6.13.23, from version 6.14.0 before 7.4.11, from version 7.5.0 before 7.11.6, and from version 7.12.0 before 7.12.5). OGNL it is an expression language for getting and setting properties of Java objects, which can be used to create or change executable code.


In some cases, an unauthenticated attacker could execute arbitrary code on a computer running a Confluence Server or Data Center instance – which earned the issue a critical 9.8 out of 10 rating on the CVSS vulnerability-rating scale.


“If the vulnerability is exploited, threat actors could bypass authentication and run arbitrary code on unpatched systems,” [explained](https://unit42.paloaltonetworks.com/cve-2021-26084/) researchers at Palo Alto Networks, who also confirmed the exploitation activity.


Kaspersky researchers explained that the vulnerability is only usable for unauthenticated RCE if the option *“*Allow people to sign up to create their account*”*is active.


“Several proof-of-concepts for exploiting it, including a version that permits RCE, are already available online,” Kaspersky noted [in its writeup](https://www.kaspersky.com/blog/confluence-server-cve-2021-26084/41635/), issued Monday.


Atlassian [has released updates](https://www.atlassian.com/software/confluence/download-archives) for versions 6.13.23, 7.4.11, 7.11.6, 7.12.5 and 7.13.0. The bug doesn’t affect Confluence Cloud users.


**Atlassian’s Summer of Security Woes**
---------------------------------------


In July, Atlassian patched a serious flaw in its Jira platform, which is a proprietary bug-tracking and agile project-management tool used for software development. It’s often tied to ([PDF](https://media.threatpost.com/wp-content/uploads/sites/103/2021/06/23175805/Atlassian-ATO-CPR-blog-FINAL.pdf)) the Confluence platform through single sign-on (SSO) capabilities.


The issue tracked as CVE-2020-36239 could enable remote, unauthenticated attackers to execute arbitrary code in some Jira Data Center products, thanks to a missing authentication check in Jira’s implementation of Ehcache, which is an open-source, Java distributed cache for general-purpose caching.


“CVE-2020-36239 can be remotely exploited to achieve arbitrary code execution and will likely be of great interest to both cybercriminals and nation-state-associated actors,” Chris Morgan, senior cyber-threat intelligence analyst at digital-risk provider Digital Shadows, [said at the time](https://threatpost.com/atlassian-critical-jira-flaw/168053/). He pointed to several recent supply-chain attacks, including attacks against software providers Accellion and Kaseya, that have leveraged vulnerabilities to gain initial access and to compromise software builds “known to be used by a diverse client base.”


Earlier, in June, researchers uncovered a chain of Atlassian bugs that [could be tied together](https://threatpost.com/atlassian-bugs-could-have-led-to-1-click-takeover/167203/) for one-click information disclosure from Jira accounts. Sensitive information could have been easily siphoned out of the platform, researchers at Check Point Research said: “Anything related to managing a team or writing…code that you can encounter bugs in.”


**It’s time to evolve threat hunting into a pursuit of adversaries.**[**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**Threatpost and Cybersixgill for**[**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**and get a guided tour of the dark web and learn how to track threat actors before their next attack.**[**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with independent researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**


 




#### Tags:
[[Atlassian]] [[Jenkins]] [[It’s]] [[Jira]] [[ThreatPost]]
