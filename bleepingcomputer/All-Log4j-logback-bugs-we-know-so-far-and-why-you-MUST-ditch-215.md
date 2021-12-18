# All Log4j, logback bugs we know so far and why you MUST ditch 2.15
### Everyone's heard of the critical log4j zero-day by now. Dubbed 'Log4Shell,' the vulnerability has set the internet on fire. Below we summarize the four or more CVEs identified thus far, and pretty good reasons to ditch log4j version 2.15.0 for 2.16.0.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/all-log4j-logback-bugs-we-know-so-far-and-why-you-must-ditch-215/
+ Date: 2021-12-17T07:20:07-05:00
+ Author: Ax Sharma


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j.jpg)

![log4j fire](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j.jpg)


Everyone's heard of the critical log4j zero-day by now. Dubbed 'Log4Shell,' the vulnerability has already set the internet on fire.


Thus far, the log4j vulnerability, tracked as CVE-2021-44228, has been abused by all kinds of threat actors from [state-backed hackers](https://www.bleepingcomputer.com/news/security/log4j-vulnerability-now-used-by-state-backed-hackers-access-brokers/) to [ransomware gangs](https://www.bleepingcomputer.com/news/security/new-ransomware-now-being-deployed-in-log4shell-attacks/) and others to [inject Monero miners](https://www.bleepingcomputer.com/news/security/log4j-attackers-switch-to-injecting-monero-miners-via-rmi/) on vulnerable systems.


Log4j usage is rampant among many software products and multiple [vendor advisories](https://www.bleepingcomputer.com/news/security/log4j-list-of-vulnerable-products-and-vendor-advisories/) have since surfaced. And, it now seems, 'logback' isn't all that immune either.


Below we summarize the multiple relevant CVEs identified thus far, and pretty good reasons to ditch log4j version 2.15.0, in favor of 2.16.0.


*Update Dec 18th, 05:33 AM ET: New 2.17.0 version is out now replacing 2.16.0 that has been found to be vulnerable to CVE-2021-45105, a DoS flaw.  

The article below has been updated to include this new CVE along with an [additional report](https://www.bleepingcomputer.com/news/security/upgraded-to-log4j-216-surprise-theres-a-217-fixing-dos/) released by BleepingComputer today.*


What all CVEs should I be concerned about?
------------------------------------------


It all began last Thursday, December 9th, when a [PoC exploit](http://web.archive.org/web/20211210193908/https://github.com/tangxiaofeng7/apache-log4j-poc) for the critical Log4j zero-day hit GitHub.


What followed was the vulnerability [disclosure](https://github.com/advisories/GHSA-jfh8-c2jp-5v3q) and [mass-scanning](https://twitter.com/bad_packets/status/1469225135504650240) activity from attackers targeting vulnerable servers.


Given Log4j's vast usage in the majority of Java applications, Log4Shell soon turned into a [nightmare for enterprises and governments](https://www.bleepingcomputer.com/news/security/new-zero-day-exploit-for-log4j-java-library-is-an-enterprise-nightmare/) worldwide.


Below are the CVEs in the order that they emerged that you should know about:


* [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) **[Critical]**: The original 'Log4Shell' vulnerability is an [untrusted deserialization](https://cwe.mitre.org/data/definitions/502.html) flaw. Rated critical in severity, this one scores a 10 on the [CVSS](https://www.first.org/cvss/) scale and grants remote code execution (RCE) abilities to unauthenticated attackers, allowing complete system takeover.  
  

Reported by Chen Zhaojun of Alibaba Cloud Security Team to Apache on November 24th, CVE-2021-44228 impacts the default configurations of multiple Apache frameworks, including Apache Struts2, Apache Solr, Apache Druid, Apache Flink, and others.  
  

Being the most dangerous of them all, this vulnerability lurks in the [log4j-core](https://search.maven.org/artifact/org.apache.logging.log4j/log4j-core) component, limited to 2.x versions: from 2.0-beta9 up to and including 2.14.1. A fix for Log4Shell was rolled out in version 2.15.0 but deemed incomplete (keep reading).  
  

Threat intel analyst Florian Roth shared Sigma rules [[1](https://github.com/SigmaHQ/sigma/blob/master/rules/web/web_cve_2021_44228_log4j_fields.yml), [2](https://github.com/SigmaHQ/sigma/blob/master/rules/web/web_cve_2021_44228_log4j.yml)] that can be employed as one of the defenses.
* [CVE-2021-45046](https://nvd.nist.gov/vuln/detail/CVE-2021-45046) [**Critical**, previously Low]: This one is a Denial of Service (DoS) flaw scoring a ~~3.7~~ 9.0. The flaw arose as a result of an incomplete fix that went into 2.15.0 for CVE-2021-44228. While the fix applied to 2.15.0 did largely resolve the flaw, that wasn't quite the case for certain non-default configurations.  
  

Log4j 2.15.0 makes "a best-effort attempt" to restrict JNDI LDAP lookups to *localhost* by default. But, attackers who have control over the Thread Context Map (MDC) input data can craft malicious payloads via the JNDI Lookup patterns to cause DoS attacsk. This applies to non-default configurations in which a non-default Pattern Layout using either a Context Lookup, e.g. $${ctx:loginId}, or a Thread Context Map pattern (%X, %mdc, or %MDC).  
  

"Log4j 2.16.0 fixes this issue by removing support for message lookup patterns and disabling JNDI functionality by default," states the NVD advisory. For those on 2.12.1 branch, a fix was backported into 2.12.2.
* [CVE-2021-4104](https://nvd.nist.gov/vuln/detail/CVE-2021-4104) **[High]**: Did we say Log4j 2.x versions were vulnerable? What about Log4j 1.x?  
  

While previously thought to be safe, Log4Shell found a way to lurk in the older Log4j too. Essentially, non-default configuration of Log4j 1.x instances using the *JMSAppender*class also become susceptible to the untrusted deserialization flaw.  
  

Although a less severe variant of CVE-2021-44228, nonetheless, this CVE impacts all versions of the [log4j:log4j](https://search.maven.org/artifact/log4j/log4j) and [org.apache.log4j:log4j](https://mvnrepository.com/artifact/org.apache.log4j/log4j) components for which only 1.x releases exist. Because these are [end-of-life](https://logging.apache.org/log4j/1.2/) versions, a fix for 1.x branch does not exist anywhere, and one should upgrade to *log4j-core* 2.16.0.
* [CVE-2021-42550](https://nvd.nist.gov/vuln/detail/CVE-2021-42550) **[Moderate]:** This is a vulnerability in the Logback logging framework. A successor to the Log4j 1.x library, Logback claims to pick up "where log4j 1.x leaves off."  
  

Up until last week, Logback also [bragged](https://archive.md/QkzIy) that being "unrelated to log4j 2.x, [logback] does not share its vulnerabilities."  
  

That assumption quickly faded when CVE-2021-4104 was discovered to impact Log4j 1.x as well, and the possibility of potential impact to Logback was [assessed](https://jira.qos.ch/browse/LOGBACK-1591). Newer Logback versions, 1.3.0-alpha11 and 1.2.9 addressing this less severe vulnerability have now been [released](https://search.maven.org/artifact/ch.qos.logback/logback-classic).
* CVE-2021-45105 **[High]**: Log4j 2.16.0 was found out to be vulnerable to a DoS flaw rated 'High' in severity. Apache has since released a log4j 2.17.0 version fixing the CVE. More details on this development are provided in BleepingComputer's [latest report](https://www.bleepingcomputer.com/news/security/upgraded-to-log4j-216-surprise-theres-a-217-fixing-dos/).
* **One more CVE...?**Keep reading.

Ditch Log4j 2.15: DNS exfiltration & RCE possible
-------------------------------------------------


Log4j 2.15.0 might contain even more severe vulnerabilities than the ones discovered so far, which is why 2.16.0 is by far a safer bet.


Because of CVE-2021-45046 described above, the maximum impact from the flaw initially appeared to be DoS, but that assumption is evolving, BleepingComputer has learned.


Cloud security firm Praetorian demonstrated how Log4j 2.15.0 versions could still be abused for DNS-based data exfiltration from external hosts, and is working with Apache towards a coordinated disclosure.


In an email interview with BleepingComputer, Praetorian's principal security engineer, Anthony Weems sheds more light on the research:


"The Praetorian [blog post](https://www.praetorian.com/blog/log4j-2-15-0-stills-allows-for-exfiltration-of-sensitive-data/) is in response to CVE-2021-45046, which applies to Log4j version 2.15. The CVE description states that—when using a specific type of Pattern Layout—this vulnerability can lead to a denial of service. The reason they state it is DoS only is due to the *localhost* allowlist," Weems tells BleepingComputer.


"We've developed a bypass for this 'localhost' allowlist and sent the details to Apache. At minimum, this means systems that are vulnerable to CVE-2021-45046 are not just vulnerable to DoS, but also DNS exfil of potentially sensitive environment variables."


Praetorian shared a PoC video demonstrating just this:



"Apache has confirmed receipt of our write-up; whether this merits an edit of the CVE or a new CVE is a good question - however, the action required by defenders is clear cut in either case: moving to 2.16.0 where *jndi* is disabled by default is the safest course of action, and is the approach we're recommending for our customers," concluded Praetorian in their statement to BleepingComputer.


Moreover, at the time of writing, BleepingComputer came across multiple security researchers claiming that it is possible to achieve full-on RCE, even with 2.15.0.


"Here is a PoC in how to bypass *allowedLdapHost* and *allowedClasses* checks in Log4J 2.15.0. to achieve RCE... and to bypass *allowedClasses* just choose a name for a class in the JDK. Deserialization will occur as usual," explains researcher Márcio Almeida:



> 
> This happens because how the check was done. the <https://t.co/KrgP5x639Q>.URI getHost() method returns the value before the # as the real host. But the JNDI/LDAP resolver will resolve to the full hostname string attempting to connect to the malicious LDAP server. 2/n [pic.twitter.com/HuZtYekuHw](https://t.co/HuZtYekuHw)
> 
> 
> — Márcio Almeida (@marcioalm) [December 17, 2021](https://twitter.com/marcioalm/status/1471742744347348997?ref_src=twsrc%5Etfw)


Similarly, Alvaro Muñoz of GitHub Security Lab shared success with bypassing the fixes made to 2.15.0 to achieve remote code execution:



> 
> [@\_atorralba](https://twitter.com/_atorralba?ref_src=twsrc%5Etfw)  
> 
> and I just managed to bypass the allowedLdapHost and allowedClasses checks. 2.15 with no formatMsgNoLookups mitigations is still vulnerable to RCE. 2.15.0 w/o those mitigations is vulnerable only if attackers can control non-message parts of the pattern layout
> 
> 
> — Alvaro Muñoz (@pwntester) [December 16, 2021](https://twitter.com/pwntester/status/1471465662975561734?ref_src=twsrc%5Etfw)


"As a side note, the default settings will not be affected. Lookup must be enabled by specifying *%m{lookups}* or by a method such as CVE-2021-45046," [says](https://twitter.com/ryotkak/status/1471485869685374984) security researcher *RyotaK,* adding to Muñoz's research.


The worst possible scenario resulting from Log4j 2.15.0 is yet to be fully determined, but suffice to say, it doesn't seem like it's just limited to DoS.


As the situation continues to evolve, organizations and developers are encouraged to upgrade to version 2.16.0, and to continue to monitor Apache's Log4j [advisory page](https://logging.apache.org/log4j/2.x/security.html) for updates.


*Update 09:11 AM ET: Severity for CVE-2021-45046 changed to Critical/9.0 according to Apache's updated advisory page.*





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Agriculture]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Cve-2021-44228]] [[Log4j]] [[Cves]] [[Cve-2021-45046]] [[Non-default]] [[Bleeping Computer]]
#### urls
https://t.co/KrgP5x639Q.URI
#### CVE's
[[CVE-2021-44228]] [[CVE-2021-45105]] [[CVE-2021-45046]] [[CVE-2021-4104]] [[CVE-2021-42550]]

