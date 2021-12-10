# Zero Day in Ubiquitous Apache Log4j Tool Under Active Attack
### The Log4Shell vulnerability critically threatens anybody using the popular open-source Apache Struts framework and could lead to a “Mini internet meltdown soonish.”

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176937
+ Date: 2021-12-10T17:58:04+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/05155430/apache.png)

An excruciating, easily exploited flaw in the ubiquitous Java logging library Apache Log4j that allows unauthenticated remote code execution (RCE) and complete server takeover is being exploited in the wild.


Early Friday morning, the Cyber Emergency Response Team (CERT) of the Deutsche Telekom Group [tweeted](https://twitter.com/DTCERT/status/1469258597930614787) that it was seeing attacks on its honeypots coming from the Tor network as threat actors tried to exploit the new zero-day vulnerability, which is tracked as “Log4Shell” by [LunaSec](https://www.lunasec.io/docs/blog/log4j-zero-day/) and as [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228).



> 
> 🚨⚠️New #0-day vulnerability tracked under "Log4Shell" and CVE-2021-44228 discovered in Apache Log4j 🌶️‼️ We are observing attacks in our honeypot infrastructure coming from the TOR network. Find Mitigation instructions here: <https://t.co/tUKJSn8RPF> [pic.twitter.com/WkAn911rZX](https://t.co/WkAn911rZX)
> 
> 
> — Deutsche Telekom CERT (@DTCERT) [December 10, 2021](https://twitter.com/DTCERT/status/1469258597930614787?ref_src=twsrc%5Etfw)
> 
> 



Ditto for [CERT New Zealand](https://www.cert.govt.nz/it-specialists/advisories/log4j-rce-0-day-actively-exploited/) and people who’ve piped up on Twitter to warn that they’re also seeing in-the-wild exploits.


This problem is going to cause a mini-internet meltdown, experts said, given that Log4j is incorporated into scads of popular frameworks, including Apache Struts2, Apache Solr, Apache Druid and Apache Flink. That exposes an eye-watering number of third-party apps that may also be vulnerable to the same type of high-severity exploits as that spotted in Minecraft, as well as in cloud services such as Steam and Apple iCloud.


Even though a fix was rushed out, it’s going to take time to trickle down, given how extensively the logging library is incorporated downstream. “Expect a Mini internet meltdown soonish,” said British security specialist Kevin Beaumont, who [tweeted](https://twitter.com/GossiTheDog/status/1469255367049756676) that the fix “needs to flow downstream to Apache Struts2, Solr, Linux distributions, vendors, appliances etc.”


Max CVSS Score of 10
--------------------


The bug find has been credited to Chen Zhaojun of Alibaba. It’s been assigned the [maximum CVSS score of 10](https://logging.apache.org/log4j/2.x/security.html), given how relatively easy it is to exploit, attackers’ ability to seize control of targeted servers and the ubiquity of Log4j.


The internet’s reaction: “Umm, yikes.”


“This log4j (CVE-2021-44228) vulnerability is extremely bad,” [tweeted](https://twitter.com/MalwareTechBlog/status/1469289471463944198) security expert Marcus Hutchins. “Millions of applications use Log4j for logging, and all the attacker needs to do is get the app to log a special string.”


According to LunaSec’s Thursday report, cloud services including Steam, Apple iCloud and apps like Minecraft had already been found to be vulnerable, but as of Friday afternoon ET, reports of other affected apps were flooding in.


Just one example of the bug’s massive reach: On Friday morning, Rob Joyce, director of cybersecurity at the National Security Agency/ (NSA), [tweeted](https://twitter.com/NSA_CSDirector/status/1469305071116636167) that even the NSA’s [Ghidra](https://ghidra-sre.org/) – a suite of reverse-engineering tools developed by NSA’s Research Directorate – includes the buggy log4j library.



> “The log4j vulnerability is a significant threat for exploitation due to the widespread inclusion in software frameworks, even NSA’s GHIDRA. This is a case study in why the software bill of material (SBOM) concepts are so important to understand exposure.” —Rob Joyce, NSA Director of Cybersecurity
> 
> 


First Spotted on Minecraft Sites
--------------------------------


The flaw first turned up on sites that cater to users of the world’s favorite game, Minecraft, on Thursday. The sites [reportedly](https://arstechnica.com/information-technology/2021/12/minecraft-and-other-apps-face-serious-threat-from-new-code-execution-bug/) warned that attackers could unleash malicious code on either servers or clients running the Java version of Minecraft by manipulating log messages, including from text typed into chat messages.


According to CERT Austria, the zero day security hole can be exploited by simply logging a special string. Researchers told Ars Technica that Log4Shell is a Java deserialization bug that stems from the library making network requests through the Java Naming and Directory Interface (JNDI) to an LDAP server and executing any code that’s returned. It’s reportedly triggered inside of log messages with use of the ${} syntax.


“JNDI triggers a look-up on a server controlled by the attacker and executes the returned code,” according to CERT Austria’s advisory, posted Friday, which noted that code for an exploit proof-of-concept (PoC) was [published on GitHub](https://github.com/tangxiaofeng7/apache-log4j-poc).


Affected Versions
-----------------


On Thursday, [LunaSec](https://www.lunasec.io/docs/blog/log4j-zero-day/) explained that anybody who’s using Apache Struts – the popular open-source framework for developing web applications in the Java programming language – is probably vulnerable. The security firm said that we’ve seen similar vulnerabilities exploited before in breaches such as the massive [2017 Equifax breach](https://threatpost.com/equifax-settles-class-action-lawsuit/151873/).


The security firm said that affected versions are 2.0 <= Apache log4j <= 2.14.1.


It added that JDK versions greater than 6u211, 7u201, 8u191, and 11.0.1 aren’t affected by the LDAP attack vector, given that in those versions, “com.sun.jndi.ldap.object.trustURLCodebase is set to false meaning JNDI cannot load a remote codebase using LDAP.”


But there are “other attack vectors targeting this vulnerability which can result in RCE,” LunaSec continued. “Depending on what code is present on the server, an attacker could leverage this existing code to execute a payload,” pointing to a Veracode post on an attack targeting the class org.apache.naming.factory.BeanFactory that’s present on Apache Tomcat servers.


As of Friday, Version 2.15.0 had been released. log4j-core.jar is available on Maven Central [here](https://repo1.maven.org/maven2/org/apache/logging/log4j/log4j-core/2.15.0/), with release notes are [available here](https://logging.apache.org/log4j/2.x/changes-report.html#a2.15.0) and Apache’s log4j security announcements [available here](https://logging.apache.org/log4j/2.x/security.html).


LunaSec said that, “given how ubiquitous this library is, the impact of the exploit (full server control), and how easy it is to exploit, the impact of this vulnerability is quite severe.”


Organizations can tell if they’re affected by examining log files for services using affected Log4j versions. If they contain user-controlled strings – CERT-NZ uses the example of “Jndi:ldap” – they could be affected.


In order to mitigate vulnerabilities, users should switch log4j2.formatMsgNoLookups to true by adding:”‐Dlog4j2.formatMsgNoLookups=True” to the JVM command for starting the application.


To keep the library from being exploited, it’s urgently recommended that Log4j versions are [upgraded](https://logging.apache.org/log4j/2.x/security.html) to log4j-2.15.0-rc1.


“If you believe you may be impacted by CVE-2021-44228, Randori encourages all organizations to adopt an assumed breach mentality and review logs for impacted applications for unusual activity,” cybersecurity researchers at Randori [wrote in a blog post](https://www.randori.com/blog/cve-2021-44228/).


Temporary Mitigation
--------------------


For those who can’t update straight off, LunaSec pointed to a  [discussion on HackerNews](https://news.ycombinator.com/item?id=29507263) regarding a mitigation strategy available in version 2.10.0 and higher that was posted in the early hours of Friday morning.


That strategy is no longer necessary with version 2.15.0, which makes it [the default behavior](https://github.com/apache/logging-log4j2/pull/607/files).


For versions older than 2.10.0 that can’t be upgraded, these mitigation choices were suggested:


* Modify every logging pattern layout to say %m{nolookups} instead of %m in your logging config files ([here are Apache’s details](https://issues.apache.org/jira/browse/LOG4J2-2109)), or,
* Substitute a non-vulnerable or empty implementation of the class org.apache.logging.log4j.core.lookup.JndiLookup, in a way that your classloader uses your replacement instead of the vulnerable version of the class. Refer to your application’s or stack’s classloading documentation to understand this behavior.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]] [[victim.industry.name=Manufacturing]] [[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Austria]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.city.name=Quito]] [[victim.country.name=Ecuador]] [[victim.continent.name=South America]] [[victim.country.name=New Zealand]] [[victim.continent.name=Oceania]]

### Autogenerated Tags:
[[Log4j]] [[Minecraft]] [[Nsa]] [[Apps]] [[Log4j]] [[ThreatPost]]
#### urls
https://t.co/tUKJSn8RPF
#### CVE's
[[CVE-2021-44228]]

