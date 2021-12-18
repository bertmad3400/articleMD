# Upgraded to log4j 2.16? Surprise, there's a 2.17 fixing DoS
### Yesterday, BleepingComputer summed up all the log4j and logback CVEs known thus far. Ever since the critical log4j zero-day saga began last week, security experts have time and time again recommended version 2.16 as the safest release to be on. That changes today with version 2.17.0 out that fixes CVE-2021-45105, a DoS vulnerability.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/upgraded-to-log4j-216-surprise-theres-a-217-fixing-dos/
+ Date: 2021-12-18T05:29:24-05:00
+ Author: Ax Sharma


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j_headpic.jpg)

![log4j](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j_headpic.jpg)


All set for the weekend? Not so fast. Yesterday, BleepingComputer [summed up](https://www.bleepingcomputer.com/news/security/all-log4j-logback-bugs-we-know-so-far-and-why-you-must-ditch-215/) all the log4j and logback CVEs known thus far.


Ever since the critical log4j zero-day saga started last week, security experts have time and time again recommended version 2.16 as the safest release to be on.


That changes today with version 2.17.0 out that fixes a seemingly-minor, but 'High' severity Denial of Service (DoS) vulnerability that affects log4j 2.16.


And, yes, this DoS bug comes with yet another identifier: CVE-2021-45105.


Infinite recursion, finite releases?
------------------------------------


Suspicion of a DoS bug affecting log4j 2.16.0 arose on Apache's JIRA project about [three days ago](https://issues.apache.org/jira/browse/LOG4J2-3230), shortly after 2.15.0 was found to be vulnerable to a minor DoS vulnerability (CVE-2021-45046).


As reported by BleepingComputer yesterday though, severity for CVE-2021-45046 was upped from a Low (3.7) to a Critical (9.0) by Apache, after newer bypasses allowed [the possibility of data exfiltration](https://www.bleepingcomputer.com/news/security/all-log4j-logback-bugs-we-know-so-far-and-why-you-must-ditch-215/) via this exploit.


"If a string substitution is attempted for any reason on the following string, it will trigger an infinite recursion, and the application will crash," state the JIRA issue, with a PoC payload:


${${::-${::-$${::-j}}}}
A few hours ago, security researchers including *vx-underground* and [*Hacker Fantastic*](https://twitter.com/hackerfantastic/status/1471947572692590602) tweeted about a possible Denial of Service flaw affecting log4j version 2.16 as well:



> 
> New exploit on Friday, as is tradition: Researchers have discovered Log4J version 2.16 is vulnerable to DoS via "${${::-${::-$${::-j}}}}"  
>   
> 
> More info: <https://t.co/pzeWiQEa68>
> 
> 
> — vx-underground (@vxunderground) [December 17, 2021](https://twitter.com/vxunderground/status/1471943986705281029?ref_src=twsrc%5Etfw)


And it turns out, after debating the issue over a course of the last three days, Apache did assign a new CVE and has rolled out a fresh release.


log4j 2.17.0 out today, fixes DoS
---------------------------------


Tracked as [CVE-2021-45105](https://logging.apache.org/log4j/2.x/security.html), and scored 'High' (7.5) on the CVSS scale, the DoS flaw exists as log4j 2.16 "does not always protect from infinite recursion in lookup evaluation."


Although JNDI lookups were completely disabled in version 2.16, self-referential lookups remained a possibility under certain circumstances. 


"Apache Log4j2 versions 2.0-alpha1 through 2.16.0 did not protect from uncontrolled recursion from self-referential lookups," state the version's release notes seen by BleepingComputer.


"When the logging configuration uses a non-default Pattern Layout with a Context Lookup (for example, *``${dollar}${dollar}{ctx:loginId}``*), attackers with control over Thread Context Map (MDC) input data can craft malicious input data that contains a recursive lookup, resulting in a *StackOverflowError* that will terminate the process."


To fix the vulnerability, log4j version 2.17.0 (for Java 8) has been [released today](https://logging.apache.org/log4j/2.x/download.html) and allows only "lookup strings in configuration" to expand recursively. In any other usage, only the top-level lookup would be resolved, and not any nested lookups.


The version is expected to reach the largest Java package repository, [Maven Central](https://search.maven.org/search?q=g:org.apache.logging.log4j%20AND%20a:log4j-core) later today.


Although Apache has officially released details on the upcoming 2.17.0 release so far, GitHub commits seen by BleepingComputer indicate a release 2.12.3 might also be on its way for those on the 2.12.x branch versions.



![log4j 2.17.0 and 2.12.3 release notes](https://www.bleepstatic.com/images/news/u/1164866/2021/Dec-2021/log4j-2.17.0-release/apache-log4j-2_12_3-notes.jpg)**log4j 2.17.0 and 2.12.3 come with a fix for CVE-2021-45105**(BleepingComputer)
Google: Over 35,000 Java packages have Log4j flaws
--------------------------------------------------


The development comes around the same time as Google's analysis that reveals over 35,000 Java packages contain log4j vulnerabilities.


"More than 35,000 Java packages, amounting to over 8% of the Maven Central repository (the most significant Java package repository), have been impacted by the recently disclosed log4j vulnerabilities," explain James Wetter and Nicky Ringland of Google's Open Source Insights Team in yesterday's [blog post](https://security.googleblog.com/2021/12/understanding-impact-of-apache-log4j.html).


According to Google, the vast majority of vulnerable Java packages in Maven Central borrow log4j "indirectly"—that is log4j is a dependency of a dependency used by the package, a concept also referred to as [transitive dependencies](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#Transitive_Dependencies).



![Google identifies Java packages vulnerable to log4j](https://www.bleepstatic.com/images/news/u/1164866/2021/Dec-2021/log4j-2.17.0-release/google-maven-central-scan.png)**Majority of vulnerable Java packages use 'log4j' as indirect dependencies** (Google)
Out of the 35,863 packages identified by Google, just about 7,000 borrowed log4j directly, indicating not all developers may have adequate visibility into their software: 


"User's lack of visibility into their dependencies and transitive dependencies has made patching difficult; it has also made it difficult to determine the full blast radius of this vulnerability," explains Google.


Looking at the history of publicly disclosed critical vulnerabilities affecting Maven packages, and the fact less than 48% of these packages had a fix for these, Google researchers expect "a long wait, likely years" before log4j flaws are completely eliminated from all Java packages.


As reported by BleepingComputer, threat actors are targeting vulnerable servers with log4j exploits to [push malware](https://www.bleepingcomputer.com/news/security/hackers-start-pushing-malware-in-worldwide-log4shell-attacks/), with the Conti ransomware gang specifically eying [vulnerable VMWare vCenter servers](https://www.bleepingcomputer.com/news/security/conti-ransomware-uses-log4j-bug-to-hack-vmware-vcenter-servers/).


As such, organizations should upgrade to the latest log4j versions and continue to monitor Apache's advisories for updates.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Expand]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Agriculture]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Google]] [[Bleepingcomputer]] [[Bleeping Computer]]
#### urls
https://t.co/pzeWiQEa68
#### CVE's
[[CVE-2021-45105]] [[CVE-2021-45046]]

