# Google unleashes security 'fuzzer' on Log4Shell bug in open source software | ZDNet
### OSS-Fuzz is now on the lookout for the Log4j Java library flaw.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/google-unleashes-security-fuzzer-on-log4shell-bug-in-open-source-software/
+ Date: 2021-12-17 13:00:00
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/ae6dde29f4169536dfcbb4378c12ec3788c82be5/2020/10/27/8dbe6a3a-f155-43c4-9d3a-b887ec216a18/istock-1154834209.jpg?width=770&height=578&fit=crop&auto=webp)

The remotely exploitable flaw in Log4j – the widely deployed Java error logging library -- is [being attacked by multiple actors](https://www.zdnet.com/article/log4j-flaw-now-state-backed-hackers-are-using-bug-as-part-of-attacks-warns-microsoft/) and [likely will remain so for many more months](https://www.zdnet.com/article/log4j-update-experts-say-log4shell-exploits-will-persist-for-months-if-not-years/) as open-source projects, product vendors, and end-user organisations patch affected systems. 

Google is now [adding OSS-Fuzz to the pool of answers](https://security.googleblog.com/2021/12/improving-oss-fuzz-and-jazzer-to-catch.html) to the internet-wide Log4j flaw, also known as Log4Shell. The bug is tracked as CVE 2021-44228 and was partially fixed in Apache Foundation's release of Log4j version 2.15.0 last week. 

OSS-Fuzz is Google's free service for fuzzing open-source software projects and is currently used by over 500 critical projects. Fuzzing involves throwing random code at software to produce an error, like a crash, and uncover potential security flaws. 



---

###  **LOG4J flaw coverage -- What you need to know now:**

* **[US warns Log4j flaw puts hundreds of millions of devices at risk](https://www.zdnet.com/article/log4j-flaw-puts-hundreds-of-millions-of-devices-at-risk-says-us-cybersecurity-agency/).**
* [**Log4j flaw: Attackers are making thousands of attempts to exploit this severe vulnerability**](https://www.zdnet.com/article/log4j-flaw-attackers-are-making-thousands-of-attempts-to-exploit-this-severe-vulnerability#link=%7B%22linkText%22:%22Log4j%20flaw:%20Attackers%20are%20making%20thousands%20of%20attempts%20to%20exploit%20this%20severe%20vulnerability%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/log4j-flaw-attackers-are-making-thousands-of-attempts-to-exploit-this-severe-vulnerability%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D).
* [**Log4j RCE activity began on December 1 as botnets start using vulnerability**](https://www.zdnet.com/article/log4j-rce-activity-began-on-december-1-as-botnets-start-using-vulnerability/#link=%7B%22linkText%22:%22Log4j%20RCE%20activity%20began%20on%20December%201%20as%20botnets%20start%20using%20vulnerability%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/log4j-rce-activity-began-on-december-1-as-botnets-start-using-vulnerability/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D).



---

To seek out Log4Shell weaknesses in newly built open-source software, Google is partnering with security firm [Code Intelligence](https://www.code-intelligence.com/) to [provide continuous fuzzing for Log4j](https://github.com/google/oss-fuzz/pull/7016). 

Code Intelligence makes [Jazzer](https://github.com/CodeIntelligenceTesting/jazzer), an open-source fuzzing engine that's now part of OSS-Fuzz, and has been modified to identify Log4j vulnerabilities in code in development. Google awarded Code Intelligence $25,000 for its work on the Log4j fuzzing.  

"Since Jazzer is part of [OSS-Fuzz](https://security.googleblog.com/2021/03/fuzzing-java-in-oss-fuzz.html), all integrated open-source projects written in Java and other JVM-based languages are now continuously searched for similar vulnerabilities," Code Intelligence [notes in a press release](https://www.code-intelligence.com/blog/java-fuzzing-log4j-rce). 

Jazzer is also capable of [detecting remote JNDI lookups](https://github.com/CodeIntelligenceTesting/jazzer/blob/3fed476bed7c61370e12062b5b97a939e3c5e591/sanitizers/src/main/java/com/code_intelligence/jazzer/sanitizers/NamingContextLookup.kt#L90) -- a strong sign that potential attackers are scanning a network for the flaw.  






JNDI (Java Naming and Directory Interface) is an interface for connecting to directories in Lightweight Directory Access Protocol (LDAP) servers, and the flaw in Log4j is found in its implementation of JNDI. 

[As Cisco's Talos researchers explain](https://blog.talosintelligence.com/2021/12/apache-log4j-rce-vulnerability.html), the flaw allows a remote attacker to use a simple LDAP request to trigger the vulnerability in pre-2.15 versions of Log4j, then retrieve a payload from a remote server and execute it locally on a vulnerable device. 

Apache Foundation this week released [Log4j version 2.16.0 to fix a second related flaw stemming from JNDI that's being tracked as CVE 2021-45046](https://www.zdnet.com/article/second-log4j-vulnerability-found-apache-log4j-2-16-0-released/). That flaw allowed an attacker to craft data patterns in a JNDI message lookup and cripple a machine with a denial of service (DoS). 

Log4j 2.16.0 disables access to JNDI by default and limits the default protocols to Java, LDAP and LDAPS. Disabling JNDI was previously a manual step to mitigate attacks against the original flaw. 

Most efforts are now focussed on vendors updating Log4j in their products and end-user organisations applying updates as they become available. For example, the US Cybersecurity and Infrastructure Security Agency (CISA) has [given federal agencies until 24 December to identify all applications affected by Log4Shell](https://www.zdnet.com/article/log4j-flaw-now-state-backed-hackers-are-using-bug-as-part-of-attacks-warns-microsoft/). Cisco, VMware, IBM and Oracle are busy developing patches for their affected products. 



---

###  **LOG4J flaw coverage -- How to keep your company safe:**

* **[**Log4j zero-day flaw: What you need to know and how to protect yourself**](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/#link=%7B%22linkText%22:%22Log4j%20zero-day%20flaw:%20What%20you%20need%20to%20know%20and%20how%20to%20protect%20yourself%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D).**
* **[**Security warning: New zero-day in the Log4j Java library is already being exploited**](https://www.zdnet.com/article/security-warning-new-zero-day-in-the-log4j-java-library-is-already-being-exploited/#link=%7B%22linkText%22:%22Security%20warning:%20New%20zero-day%20in%20the%20Log4j%20Java%20library%20is%20already%20being%20exploited%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/security-warning-new-zero-day-in-the-log4j-java-library-is-already-being-exploited/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D).**
* **[**Log4j flaw could be a problem for industrial networks 'for years to come'**](https://www.zdnet.com/article/log4j-flaw-could-be-a-problem-for-industrial-networks-for-years-to-come/#link=%7B%22linkText%22:%22Log4j%20flaw%20could%20be%20a%20problem%20for%20industrial%20networks%20'for%20years%20to%20come'%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/log4j-flaw-could-be-a-problem-for-industrial-networks-for-years-to-come/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D).**



---

Google's OSS-Fuzz tackles Log4j from another angle, aiming to prevent developers from accidentally inserting the flaw in new software projects that may eventually be deployed in production environments. 

"Vulnerabilities like Log4Shell are an eye-opener for the industry in terms of new attack vectors. With OSS-Fuzz and Jazzer, we can now detect this class of vulnerability so that they can be fixed before they become a problem in production code," says Jonathan Metzman from the Google Open Source Security Team. 






## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Jndi]] [[Oss-fuzz]] [[Open-source]] [[Google]] [[Log4shell]] [[ZDNet]]

