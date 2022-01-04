# Log4j flaw attack levels remain high, Microsoft warns | ZDNet
### Organizations mights not realize their environments are already compromised.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/log4j-flaw-attacks-are-causing-lots-of-problems-microsoft-warns/
+ Date: 2022-01-04 13:11:00
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/95e4cf0375e6c5fb91e40046308b24c0f58c39ee/2020/01/23/5110af54-6fb2-4fc6-8d90-843d67aef1e0/businessman-annoyed-with-phone-call.jpg?width=770&height=578&fit=crop&auto=webp)

Microsoft has warned Windows and Azure customers to remain vigilant after observing state-sponsored and cyber-criminal attackers probing systems for the Log4j 'Log4Shell' flaw through December. 

Disclosed by the Apache Software Foundation [on December 9](https://www.zdnet.com/article/security-warning-new-zero-day-in-the-log4j-java-library-is-already-being-exploited/), Log4Shell will likely take years to remediate because of how widely the error-logging software component is used in applications and services. 

Microsoft warns that customers might not be aware of how widespread the Log4j issue is in their environment. Over the past month, Microsoft has released numerous updates, including to its Defender security software, to help customers identify the issue as attackers stepped up scanning activity. 



---

### LOG4J FLAW COVERAGE – WHAT YOU NEED TO KNOW NOW

* **[Log4j flaw: Attackers are making thousands of attempts to exploit this severe vulnerability](https://www.zdnet.com/article/log4j-flaw-attackers-are-making-thousands-of-attempts-to-exploit-this-severe-vulnerability)**
* **[Security warning: New zero-day in the Log4j Java library is already being exploited](https://www.zdnet.com/article/security-warning-new-zero-day-in-the-log4j-java-library-is-already-being-exploited/)**
* **[Log4j RCE activity began on December 1 as botnets start using vulnerability](https://www.zdnet.com/article/log4j-rce-activity-began-on-december-1-as-botnets-start-using-vulnerability/)**



---

"Exploitation attempts and testing have remained high during the last weeks of December. We have observed many existing attackers adding exploits of these vulnerabilities in their existing malware kits and tactics, from coin miners to hands-on-keyboard attacks," the Microsoft 365 Defender Threat Intelligence Team and the Microsoft Threat Intelligence Center (MSTIC) [said in a January 3 update](https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/). 

Microsoft said customers should "assume broad availability of exploit code and scanning capabilities to be a real and present danger to their environments." Hence, it's encouraging customers to utilize scripts and scanning tools to assess their risk and impact. 

"Microsoft has observed attackers using many of the same inventory techniques to locate targets. Sophisticated adversaries (like nation-state actors) and commodity attackers alike have been observed taking advantage of these vulnerabilities. There is high potential for the expanded use of the vulnerabilities," Microsoft added. 

The flaw likely left some security teams without much of a break over Christmas and prompted warnings from the UK's NCSC to [beware of burnout among staff responsible for remediation](https://www.zdnet.com/article/log4j-flaw-10-questions-you-should-be-asking/). 






Just ahead of New Year's Day, Microsoft [rolled out](https://twitter.com/MsftSecIntel/status/1475627081753112579) a new Log4j dashboard for threat and vulnerability management in the Microsoft 365 Defender portal for Windows 10 and 11, Windows Server, and Linux systems. This system aims to help customers find and fix files, software and devices affected by Log4j vulnerabilities. CISA and CrowdStrike [also released Log4j scanners ahead of Christmas](https://www.zdnet.com/article/multiple-log4j-scanners-released-by-cisa-crowdstrike-more/). 



---

### LOG4J FLAW COVERAGE - HOW TO KEEP YOUR COMPANY SAFE

* **[**Log4j zero-day flaw: What you need to know and how to protect yourself**](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/#link=%7B%22linkText%22:%22Log4j%20zero-day%20flaw:%20What%20you%20need%20to%20know%20and%20how%20to%20protect%20yourself%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)**
* **[**Security warning: New zero-day in the Log4j Java library is already being exploited**](https://www.zdnet.com/article/security-warning-new-zero-day-in-the-log4j-java-library-is-already-being-exploited/#link=%7B%22linkText%22:%22Security%20warning:%20New%20zero-day%20in%20the%20Log4j%20Java%20library%20is%20already%20being%20exploited%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/security-warning-new-zero-day-in-the-log4j-java-library-is-already-being-exploited/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)**
* **[**Log4j flaw could be a problem for industrial networks 'for years to come'**](https://www.zdnet.com/article/log4j-flaw-could-be-a-problem-for-industrial-networks-for-years-to-come/#link=%7B%22linkText%22:%22Log4j%20flaw%20could%20be%20a%20problem%20for%20industrial%20networks%20'for%20years%20to%20come'%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/log4j-flaw-could-be-a-problem-for-industrial-networks-for-years-to-come/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)**



---

CISA officials believe [hundreds of millions of devices are affected by Log4j](https://www.zdnet.com/article/log4j-flaw-puts-hundreds-of-millions-of-devices-at-risk-says-us-cybersecurity-agency/). Meanwhile, major tech vendors such as [Cisco](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) and [VMware](https://kb.vmware.com/s/article/87068) continue to release patches for affected products. 

The Log4Shell vulnerabilities now include the original CVE-2021-44228 and four related flaws, the latest of which was [CVE-2021-44832](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44832). However it was only a moderate severity issue [addressed in the Log4j version 2.17.1 update on December 28](https://logging.apache.org/log4j/2.x/security.html). The Apache Software Foundation has details about each of the Log4j vulnerabilities in [its advisory covering](https://logging.apache.org/log4j/2.x/security.html) CVE-2021-44228, [CVE-2021-45105](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45105), and [CVE-2021-45046](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45046). 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Expand]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Microsoft]] [[Windows]] [[Zero-day]] [[ZDNet]]
#### CVE's
[[CVE-2021-44228]] [[CVE-2021-44832]] [[CVE-2021-45105]] [[CVE-2021-45046]]

