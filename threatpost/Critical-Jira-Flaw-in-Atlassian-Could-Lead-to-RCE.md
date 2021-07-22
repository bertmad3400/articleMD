# Critical Jira Flaw in Atlassian Could Lead to RCE
### The software-engineering platform is urging users to patch the critical flaw ASAP.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168053)
+ Date: July 22, 2021  4:52 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/22161625/Atlassian-Jira.png)
Atlassian has dropped a patch for a critical vulnerability in many versions of its Jira Data Center and Jira Service Management Data Center products, which can lead to arbitrary code execution.


Atlassian is a platform that’s used by 180,000 customers to engineer software and manage projects, and Jira is its proprietary bug-tracking and agile project-management tool.


On Wednesday, Atlassian issued a security [advisory](https://confluence.atlassian.com/adminjiraserver/jira-data-center-and-jira-service-management-data-center-security-advisory-2021-07-21-1063571388.html) concerning the vulnerability, which is tracked as CVE-2020-36239. The bug could enable remote, unauthenticated attackers to execute arbitrary code in some Jira Data Center products.



[BleepingComputer](https://www.bleepingcomputer.com/news/security/atlassian-asks-customers-to-patch-critical-jira-vulnerability/) got ahold of an email Atlassian sent to enterprise customers on Wednesday that urged them to update ASAP.


The vulnerability has to do with a missing authentication check in Jira’s implementation of Ehcache, which is an open-source, Java distributed cache for general-purpose caching, Java EE and lightweight containers that’s used for performance and which simplifies scalability.


Atlassian said that the bug was introduced in version 6.3.0 of Jira Data Center, Jira Core Data Center, Jira Software Data Center and Jira Service Management Data Center (known as Jira Service Desk prior to 4.14).


According to Atlassian’s security advisory, that list of products exposed a Ehcache remote method invocation (RMI) network service that attackers – who can connect to the service on port 40001 and potentially 40011 – could use to “execute arbitrary code of their choice in Jira” through deserialization, due to missing authentication.


RMI is an API that acts as a mechanism to enable remote communication between programs written in Java. It allows an object residing in one Java virtual machine (JVM) to invoke an object running on another JVM; Often, it involves one program on a server and one on a client. The advantage of RMI, as BleepingComputer describes it, is that “programmers can invoke methods present in remote objects—such as those present within an application running on a shared network, right from their application as they would run a local method or procedure.”


Atlassian “strongly suggests” restricting access to the Ehcache ports to only Data Center instances, but noted that there’s a caveat: “Fixed versions of Jira will now require a shared secret in order to allow access to the Ehcache service,” according to the advisory.


Affected Versions
-----------------


These are the affected versions of Jira Data Center and Jira Service Management Data Center:


**Jira Data Center, Jira Core Data Center, and Jira Software Data Center – ranges**


**Jira Service Management Data Center – ranges**


**Jira Data Center, Jira Core Data Center, and Jira Software Data Center**


**Jira Service Management Data Center**


Atlassian’s advisory said that customers who have downloaded and installed any affected versions “must upgrade their installations immediately to fix this vulnerability.” Having said that, Atlassian also noted that the “critical” rating is its own assessment and that customers “should evaluate its applicability to your own IT environment.”


Non-Affected Versions
---------------------


Here’s the list of products that aren’t affected by the flaw:


Also, customers who have upgraded Jira Data Center, Jira Core Data Center, Jira Software Data Center to versions 8.5.16, 8.13.8, 8.17.0 and/or Jira Service Management Data Center to versions 4.5.16, 4.13.8 or 4.17.0 are off the hook: They don’t need to upgrade.


Atlassian is Attacker Catnip
----------------------------


Some of the largest enterprises with the most sophisticated product development use Atlassian products. Among its more than 65,000 users, Jira counts some big fans, including the likes of the Apache Software Foundation, Cisco, Fedora Commons, Hibernate, Pfizer and Visa.


Unfortunately, its popularity – particularly with the big fish – and its capabilities make it a tempting target for attackers.


In June, researchers uncovered [Atlassian bugs](https://threatpost.com/atlassian-bugs-could-have-led-to-1-click-takeover/167203/) that could have led to one-click takeover: A scenario that brought to mind the potential for an exploit that would have been similar to the [SolarWinds](https://threatpost.com/solarwinds-default-password-access-sales/162327/) supply-chain attack, in which attackers used a default password as an open door into a software-updating mechanism.


Chris Morgan, senior cyber-threat intelligence analyst at digital-risk provider Digital Shadows, said that the vulnerability at the heart of Wednesday’s advisory is just the latest in a series of bugs facing software engineering and management platforms that, if exploited, “could lead to a range of pernicious outcomes.”


While there’s no evidence of active exploitation at this time, we can expect attempts to show up in the coming one to three months, Morgan predicted. “CVE-2020-36239 can be remotely exploited to achieve arbitrary code execution and will likely be of great interest to both cybercriminals and nation-state-associated actors,” he said. He pointed to several recent supply-chain attacks, including attacks against software providers [Accellion](https://threatpost.com/accellion-zero-day-attacks-clop-ransomware-fin11/164150/) and [Kaseya](https://threatpost.com/kaseya-patches-zero-days-revil-attacks/167670/), that have leveraged vulnerabilities to gain initial access and to compromise software builds “known to be used by a diverse client base.”


Other security experts agreed with Morgan’s assessment. Andrew Barratt, managing principal of solutions and investigations at cybersecurity advisory firm Coalfire, told Threatpost on Thursday that the vulnerability Atlassian disclosed on Wednesday “shows that attackers are still looking to leverage economies of scale and compromise multiple parties using single platform-wide vulnerabilities.”


Expect Exploitation, In the Wild Attacks
----------------------------------------


TL;DR: Apply the update ASAP, or implement Atlassian’s workarounds, Morgan emphasized.


That said, the real impact depends on the exposure of the RMI APIs, Barratt suggested. “This could lead to targeted campaigns that focus on developers (historically who have lots of privileges and useful tools on their machines) that then seek to drop malware that exploits the Atlassian vulnerabilities for further manipulation of product development,” he said.


On the optimistic side, the issue may blow over before it gets dire, given that Atlassian is already issuing patches and advising on temporary mitigations, Barratt added. “Hopefully the window for this to be a problem will be minimal – and some follow-up review of the systems to check for indicators of compromise will give confidence that nothing serious has gone wrong.”


Barratt thinks that the most concerning thing should be “the renewed focus on potentially a gold mine of opportunity.” While targeting developers isn’t new, he said, targeting their tools, platform and reducing potential confidence in the product “shows the need for security orchestration tools that can help bring the diversity of the problem to single-management view.”


On the technical side of things, Shawn Smith – director of infrastructure at application security provider nVisium – posited that supply-chain attacks are a good argument against auto-updating dependencies, but “this also means that security teams have to monitor and manage them effectively and efficiently,” as he told Threatpost via email on Thursday.


“Any updates to dependencies should be vetted prior to use, and systems should be using version-locked dependencies to prevent CI/CD systems from grabbing the latest updates by default,” he added. “At the same time, security teams should be monitoring to ensure that vulnerabilities are not tainting versions that are being used and advise developers and operations teams as issues arise.”


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Jira]] [[Atlassian]] [[Ehcache]] [[RMI]] [[Barratt]] [[supply-chain]] [[Threatpost]] [[teams]] [[ThreatPost]]
