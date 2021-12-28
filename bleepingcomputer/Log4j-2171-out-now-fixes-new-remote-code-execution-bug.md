# Log4j 2.17.1 out now, fixes new remote code execution bug
### Apache has released another Log4j version, 2.17.1 fixing a newly discovered remote code execution (RCE) vulnerability in 2.17.0, tracked as CVE-2021-44832. Prior to today, 2.17.0 was the most recent version of Log4j and deemed the safest release to upgrade to, but that advice has now evolved.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/log4j-2171-out-now-fixes-new-remote-code-execution-bug/
+ Date: 2021-12-28T15:12:01-05:00
+ Author: Ax Sharma


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j___logo.jpg)

![log4j](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j___logo.jpg)


Apache has released another Log4j version, 2.17.1 fixing a newly discovered remote code execution (RCE) vulnerability in 2.17.0, tracked as CVE-2021-44832.


Prior to today, 2.17.0 was the most recent version of Log4j and deemed the safest release to upgrade to, but that advice has now evolved.


Fifth Log4j CVE in under a month
--------------------------------


Mass exploitation of the original [Log4Shell vulnerability](https://www.bleepingcomputer.com/news/security/new-zero-day-exploit-for-log4j-java-library-is-an-enterprise-nightmare/) (CVE-2021-44228) by threat actors began around December 9th, when a [PoC exploit](http://web.archive.org/web/20211210193908/https://github.com/tangxiaofeng7/apache-log4j-poc) for it surfaced on GitHub.


Given Log4j's vast usage in the majority of Java applications, Log4Shell soon turned into a [nightmare for enterprises and governments](https://www.bleepingcomputer.com/news/security/new-zero-day-exploit-for-log4j-java-library-is-an-enterprise-nightmare/) worldwide.


While the critical risk posed by the original Log4Shell exploit is paramount, milder variants of the vulnerability emerged in Log4j versions, including 2.15 and 2.16—previously believed to be fully patched.


BleepingComputer earlier reported on [four different CVEs impacting Log4j](https://www.bleepingcomputer.com/news/security/all-log4j-logback-bugs-we-know-so-far-and-why-you-must-ditch-215/) and one discovered in the 'logback' framework. After the discovery of a DoS flaw in version 2.16, the advice had swiftly shifted towards [upgrading to version 2.17.0](https://www.bleepingcomputer.com/news/security/upgraded-to-log4j-216-surprise-theres-a-217-fixing-dos/), deemed the safest of all.


But now a fifth vulnerability—an RCE flaw, tracked as CVE-2021-44832 has been discovered in 2.17.0, with a patch applied to the [newest release 2.17.1](http://logging.apache.org/log4j/2.x/security.html) which is out.


Rated 'Moderate' in severity and assigned a 6.6 score on the CVSS scale, the vulnerability stems from the lack of additional controls on JDNI access in log4j.


"JDBC Appender should use JndiManager when accessing JNDI. JNDI access should be controlled via a system property," states the issue description seen by BleepingComputer.


"Related to CVE-2021-44832 where an attacker with permission to modify the logging configuration file can construct a malicious configuration using a JDBC Appender with a data source referencing a JNDI URI which can execute remote code."


Checkmarx security researcher [Yaniv Nizry](https://www.linkedin.com/in/yaniv-n-8b4a76193/) claimed credit for reporting the vulnerability to Apache:



> 
> Stay tuned for a blogpost ;) [pic.twitter.com/D56WpVsuF3](https://t.co/D56WpVsuF3)
> 
> 
> — Yaniv Nizry (@YNizry) [December 28, 2021](https://twitter.com/YNizry/status/1475764153373573120?ref_src=twsrc%5Etfw)


Nizry's tweet quickly exploded in traffic, attracting remarks and [memes](https://twitter.com/cyb3rops/status/1475844554322595840) from security experts and 'victims' of the ongoing log4j-patching fatigue.


"I hope this is a joke, I hope so much Pensive face #log4j," [tweeted](https://twitter.com/mynameisv_/status/1475835347456208896) one user in response.


"We are LONG past the point where the only responsible thing to do is put up a giant flashing neon sign that reads 'LOG4J CANNOT BE FIXED, DO NOT USE IT FOR ANYTHING.'" [taunted](https://twitter.com/rootwyrm/status/1475851798908964864) another.


Security expert Kevin Beaumont [labeled](https://twitter.com/GossiTheDog/status/1475875272503222285) the instance another "failed Log4j disclosure in motion" during the holidays.


Disclosed too soon?
-------------------


At the time of Nizry's tweet, BleepingComputer did not see an official advisory or memo indicating the presence of an RCE bug in log4j 2.17.


The tweet itself contained no details about the vulnerability or how it could be exploited but, within minutes, led a pack of security pros and netizens to start investigating the claim.


Disclosing security vulnerabilities prematurely can lure threat actors to conduct malicious scanning and exploitation activities, as evident from the Log4Shell exploit leak of December 9th.


Marc Rogers, VP of cybersecurity at Okta first disclosed the vulnerability identifier (CVE-2021-44832) and that the exploitation of the bug depends on a non-default log4j setup where configuration is being loaded from a remote server:



> 
> Looks like log4j CVE-2021-44832 has non default preconditions: “You are loading configuration from a remote server and/or someone can hijack/modify your log4j configuration file  
> 
> You are using the JDBC log appender with a dynamic URL address.”
> 
> 
> — Marc Rogers (@marcwrogers) [December 28, 2021](https://twitter.com/marcwrogers/status/1475872692242825217?ref_src=twsrc%5Etfw)


Up until now, log4j vulnerabilities have been exploited by all kinds of threat actors from [state-backed hackers](https://www.bleepingcomputer.com/news/security/log4j-vulnerability-now-used-by-state-backed-hackers-access-brokers/) to [ransomware gangs](https://www.bleepingcomputer.com/news/security/new-ransomware-now-being-deployed-in-log4shell-attacks/) and others to [inject Monero miners](https://www.bleepingcomputer.com/news/security/log4j-attackers-switch-to-injecting-monero-miners-via-rmi/) on vulnerable systems.


The Conti ransomware gang has been seen  eying [vulnerable VMWare vCenter servers](https://www.bleepingcomputer.com/news/security/conti-ransomware-uses-log4j-bug-to-hack-vmware-vcenter-servers/). Whereas, attackers breaching Vietnamese crypto platform ONUS via log4shell [demanded a $5 million ransom](https://cystack.net/research/the-attack-on-onus-a-real-life-case-of-the-log4shell-vulnerability). 


Log4j users should immediately upgrade to the latest [release 2.17.1](https://logging.apache.org/log4j/2.x/download.html) (for Java 8). Backported versions 2.12.4 (Java 7) and 2.3.2 (Java 6) containing the fix are also expected to be released shortly.


BleepingComputer has reached out to Checkmarx for comment in advance of writing and we are awaiting their response.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Vietnam]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Log4j]] [[Cve-2021-44832]] [[Log4shell]] [[Bleepingcomputer]] [[Nizry]] [[Jndi]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-44832]] [[CVE-2021-44228]]

