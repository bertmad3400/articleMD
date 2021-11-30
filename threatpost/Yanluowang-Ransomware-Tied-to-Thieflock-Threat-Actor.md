# Yanluowang Ransomware Tied to Thieflock Threat Actor
### Links between the tactics and tools demonstrated in attacks suggest a former affiliate has switched loyalties, according to new research.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176640)
+ Date: November 30, 2021  8:56 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/30085123/thief1.jpg)
A threat actor previously tied to the Thieflock [ransomware](https://threatpost.com/ransomware-volumes-record-highs-2021/168327/) operation may now be using the emerging Yanluowang [ransomware](https://threatpost.com/feds-warn-blackmatter-ransomware-gang-is-poised-to-strike/175567/) in a series of attacks against U.S. corporations, researchers have found.


Researchers from Symantec, a division of Broadcom Software, found ties between Thieflock and Yanluowang, the latter of which they [revealed in October](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/yanluowang-targeted-ransomware) after observing its use against a large organization.


Researchers believe a threat actor has been using Yanluowang since August to target mainly financial companies in the United States, they said in a [report](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/yanluowang-ransomware-attacks-continue) published Tuesday. The actor also has attacked companies in the manufacturing, IT services, consultancy and engineering sectors with the novel ransomware, they said.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

Researchers found a “tentative link” between the new Yanluowang attacks and older attacks involving Thieflock, a [ransomware-as-a-service](https://threatpost.com/2-5-million-a-year-ransomware-as-a-service-ring-uncovered/119902/) (RaaS) developed by the Canthroid group, also known as Fivehands.


This demonstrates how “little loyalty” there is among ransomware actors, particularly those who act as affiliates of RaaS operations, Vikram Thakur, principal research manager at Symantec, a division of Broadcom, told Threatpost in an email interview on Monday ahead of the report’s release.


“Ransomware authors and affiliates pivot often,” he said. “Affiliates switch business based on profit margins offered by ransomware service operators, and in some cases [the] amount of heat from law enforcement against certain ransomware families. Little to no loyalty in their business.”


**Focus on Attacks, Not Development**
-------------------------------------


When researchers first observed Yanluowang in October, they characterized it as “somewhat under-developed.” Little has changed in that department regarding the latest attacks, Thakur told Threatpost.


“Not much enhancement has taken place,” he said. “Looks like Yanluowang and their affiliates have been focused on conducting attacks rather than making any major strides on code development.”


Researchers provided a rundown of some of the tools used in Yanluowang attacks, some of which share a similar activity of Thieflock attacks “that makes us believe the person behind the attacks is well-versed with how Thieflock used to be deployed,” Thakur told Threatpost.


Yanluowang attackers also use a host of open-source tools to compromise and conduct reconnaissance and data-stealing activities, according to the report.


In most scenarios, attackers use PowerShell to download tools to compromised systems, including BazarLoader, which assists in reconnaissance of a system before attacks occur, researchers said.


The attackers then enable RDP via registry to enable remote access, deploying the legitimate remote access tool ConnectWise, formerly known as ScreenConnect, once they’ve gained this access, they said.


**Specific Links to Thieflock**
-------------------------------


For lateral movement to identify systems of interest to target – i.e., an Active Directory server – Yanluowang attackers deploy Adfind, a free tool that can be used to query Active Directory; and SoftPerfect Network Scanner, or netscan.exe, a publicly available tool used for discovery of hostnames and network services. The use of the latter is similar to what has been seen in Thieflock attacks, researchers said.


Several tools are then used in the next phase of the attack for credential theft that Thieflock attackers also have been seen using. They include GrabFF, a tool that can dump passwords from Firefox; GrabChrome, a tool that can dump passwords from Chrome; and BrowserPassView, a tool that can dump passwords from Internet Explorer and a number of other browsers, researchers wrote.


Yanluowang attackers also use a number of open-source tools such as KeeThief, a PowerShell script to copy the master key from KeePass, as well as customized versions of open-source credential-dumping tools to dump credentials from the registry.


Data-capture tools are also part of the attack vector, including a screen capture tool and a file exfiltration tool (filegrab.exe), as well as [Cobalt Strike Beacon](https://threatpost.com/cobalt-strike-cybercrooks/167368/), which researchers saw deployed against at least one target.


Despite the links between the use of some tools and tactics in Yanluowang attacks that align with Thieflock, Thakur said that at this point it does not seem like the two [ransomware](https://threatpost.com/grief-ransomware-nra/175850/) variants share authorship.


“From an analytical perspective, this means one or more actors that deployed Thieflock in the past are now involved in deploying Yanluowang,” he said. “Affiliates move to different groups when they see greater financial benefits, or lesser attention from law enforcement.”


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** [***REGISTER TODAY***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article) ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This*** [***LIVE, interactive Threatpost Town Hall***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***, sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article) ***for the LIVE event!***




#### Tags:
[[Yanluowang]] [[Thieflock]] [[said.]] [[ransomware]] [[Threatpost]] [[attacks,]] [[open-source]] [[ThreatPost]]
