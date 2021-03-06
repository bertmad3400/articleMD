# Apache Releases Third Major Log4j Update To Fix A DoS Flaw
### Apache has fixed the DoS bug with Log4j 2.17.0, the third major update since the Log4Shell vulnerability surfaced online. Update now.

## Information:
+ Source: Latest Hacking News
+ Link: https://latesthackingnews.com/2021/12/20/apache-releases-third-major-log4j-update-to-fix-a-dos-flaw/
+ Date: 2021-12-20
+ Author: Abeerah Hashim


## Article:
![Article Image](https://latesthackingnews.com/wp-content/uploads/2021/09/vulnerability-alert.jpg)
 Apache has released another update shortly after the second Log4j update addressing a previously “incomplete patch” for the Log4Shell zero-day. This third major update rolled out as Log4j 2.17.0 also addresses a severe DoS flaw that remained unfixed.

 Third Log4j Update Out As Version 2.17.0
----------------------------------------

 Emerged as zero-day that the threat actors quickly started exploiting for large-scale attacks, the [Log4shell vulnerability](https://latesthackingnews.com/2021/12/12/critical-log4shell-zero-day-vulnerability-wreaks-havoc-online/) (CVE-2021-44228) has created a disastrous situation for the internet world.

 Rushing up to contain the damages, Apache first released Log4j 2.15.0 to address the bug. However, it turned out to be an incomplete fix as this update failed to patch the vulnerability in non-default configurations. Hence, the threat for remote code execution attacks persisted even on updated systems.

 Addressing this issue, Apache [released Log4j 2.16.0](https://latesthackingnews.com/2021/12/16/another-apache-log4j-bug-discovered-patch-released-update-once-again/), remedying this issue identified as CVE-2021-45046. This vulnerability also received a critical severity rating with a CVSS score of 9.0.

 Nonetheless, it seems this subsequent update also failed to adequately fix the glitch. Instead, it triggered a denial-of-service vulnerability that further risked the systems’ security.

 Apache has now rolled out Log4j version 2.17.0, addressing this issue. Identified as CVE-2021-45105, the bug has received a high-severity rating with a CVSS score of 7.5. The vendors confirmed that this vulnerability affects all Log4j versions between 2.0 beta 9 to 2.16.0.

 Describing this matter in an [advisory](https://logging.apache.org/log4j/2.x/security.html), Apache stated,

 
> Apache Log4j2 versions 2.0-alpha1 through 2.16.0 did not protect from uncontrolled recursion from self-referential lookups. When the logging configuration uses a non-default Pattern Layout with a Context Lookup (for example, $${ctx:loginId}), attackers with control over Thread Context Map (MDC) input data can craft malicious input data that contains a recursive lookup, resulting in a StackOverflowError that will terminate the process. This is also known as a DOS (Denial of Service) attack.
> 
> 

 However, the vendors confirmed that this vulnerability has a limited impact. Specifically, it does not affect Log4j 1.x and apps using log4j-api JAR file without the log4j-core JAR file.

 To avoid potential risks, all users should rush to update their systems and apps with the latest Log4j version.

   


## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Latest Hacking News]]
#### CVE's
[[CVE-2021-44228]] [[CVE-2021-45046]] [[CVE-2021-45105]]

