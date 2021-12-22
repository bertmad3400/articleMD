# CISA releases Apache Log4j scanner to find vulnerable apps
### The Cybersecurity and Infrastructure Security Agency (CISA) has announced the release of a scanner for identifying web services impacted by& two Apache Log4j remote code execution vulnerabilities, tracked as CVE-2021-44228 and CVE-2021-45046.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/cisa-releases-apache-log4j-scanner-to-find-vulnerable-apps/
+ Date: 2021-12-22T10:23:40-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/04/08/CISA.jpg)

![](https://www.bleepstatic.com/content/hl-images/2021/04/08/CISA.jpg)


The Cybersecurity and Infrastructure Security Agency (CISA) has [announced](https://twitter.com/cisagov/status/1473401212468932609?s=12) the release of a scanner for identifying web services impacted by two Apache Log4j remote code execution vulnerabilities, tracked as CVE-2021-44228 and CVE-2021-45046.


"log4j-scanner is a project derived from other members of the open-source community by CISA's Rapid Action Force team to help organizations identify potentially vulnerable web services affected by the log4j vulnerabilities," the cybersecurity agency [explains](https://github.com/cisagov/log4j-scanner).


This scanning solution builds upon similar tools, including an [automated scanning framework](https://github.com/fullhunt/log4j-scan) for the CVE-2021-44228 bug (dubbed& Log4Shell)& developed by cybersecurity company FullHunt.


The tool enables security teams to scan network hosts for Log4j RCE exposure and spot web application firewall (WAF) bypasses that can allow threat actors to gain code execution within the organization's environment.


CISA highlights the following features on [log4j-scanner's project page](https://github.com/cisagov/log4j-scanner/tree/master/log4-scanner#features):


* Support for lists of URLs.
* Fuzzing for more than 60 HTTP request headers (not only 3-4 headers as previously seen tools).
* Fuzzing for HTTP POST Data parameters.
* Fuzzing for JSON data parameters.
* Supports DNS callback for vulnerability discovery and validation.
* WAF Bypass payloads.

CISA's Log4Shell response
-------------------------


This is just the latest step taken by CISA to help government and private organizations respond to ongoing attacks abusing these critical security flaws in Apache's Log4j logging library.


The agency was also behind a [joint advisory](https://www.cisa.gov/uscert/ncas/alerts/aa21-356a) issued today by cybersecurity agencies worldwide and US federal agencies with mitigation guidance on addressing the CVE-2021-44228, CVE-2021-45046, and CVE-2021-45105 Log4j vulnerabilities.


CISA's also spearheading a push for urgently patching devices vulnerable to Log4Shell attacks to block threat actors' attempts to [exploit Log4Shell vulnerable systems](https://www.bleepingcomputer.com/news/security/hackers-start-pushing-malware-in-worldwide-log4shell-attacks/) and infect them with malware.


On Friday, [CISA ordered Federal Civilian Executive Branch agencies](https://www.bleepingcomputer.com/news/security/us-emergency-directive-orders-govt-agencies-to-patch-log4j-bug/) to patch their systems against Log4Shell until December 23. The cybersecurity agency also recently added the flaw to the [Known Exploited Vulnerabilities Catalog](https://www.bleepingcomputer.com/news/security/cisa-orders-federal-agencies-to-patch-log4shell-by-december-24th/), thus also requiring expedited action from federal agencies to mitigate this critical flaw until December 24.


As BleepingComputer reported, Log4Shell attacks have been orchestrated by financially motivated attackers [deploying Monero miners](https://www.bleepingcomputer.com/news/security/log4j-attackers-switch-to-injecting-monero-miners-via-rmi/), ransomware gangs [[1](https://www.bleepingcomputer.com/news/security/conti-ransomware-uses-log4j-bug-to-hack-vmware-vcenter-servers/), [2](https://www.bleepingcomputer.com/news/security/new-ransomware-now-being-deployed-in-log4shell-attacks/)], and even [state-backed hackers](https://www.bleepingcomputer.com/news/security/log4j-vulnerability-now-used-by-state-backed-hackers-access-brokers/).


We also have articles with more information on the [Log4Shell vulnerability](https://www.bleepingcomputer.com/tag/log4shell/), a comprehensive [list of vendor advisories and vulnerable products](https://www.bleepingcomputer.com/news/security/log4j-list-of-vulnerable-products-and-vendor-advisories/), and [why you must upgrade to Log4j2.17.0](https://www.bleepingcomputer.com/news/security/upgraded-to-log4j-216-surprise-theres-a-217-fixing-dos/) as soon as possible.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Agriculture]] [[victim.industry.name=Information]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Cisa]] [[Log4shell]] [[Log4j]] [[Cybersecurity]] [[Cve-2021-44228]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-44228]] [[CVE-2021-45046]] [[CVE-2021-45105]]

