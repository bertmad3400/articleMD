# US orders federal govt agencies to patch critical Log4j bug
### US Federal Civilian Executive Branch agencies have been ordered to patch the critical and actively exploited Log4Shell security vulnerability in the Apache Log4j library within the next six days.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/us-orders-federal-govt-agencies-to-patch-critical-log4j-bug/
+ Date: 2021-12-17T12:35:43-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j___logo.jpg)

![US orders federal govt agencies to patch critical Log4j bug](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j___logo.jpg)


US Federal Civilian Executive Branch agencies have been ordered to patch the critical and actively exploited Log4Shell security vulnerability in the Apache Log4j library within the next six days.


The order comes through an emergency directive issued by the Cybersecurity and Infrastructure Security Agency (CISA) today.


This is not surprising given the risk the ongoing exploitation of this vulnerability poses and seeing that the security flaw (tracked as CVE-2021-44228) has also [recently been added Known Exploited Vulnerabilities Catalog](https://www.bleepingcomputer.com/news/security/cisa-orders-federal-agencies-to-patch-log4shell-by-december-24th/), which also required expedited action in mitigating the bug until December 24.


"To be clear, this vulnerability poses a severe risk. We will only minimize potential impacts through collaborative efforts between government and the private sector. We urge all organizations to join us in this essential effort and take action," CISA Director Jen Easterly said at the time.


Log4Shell mitigation required until December 23
-----------------------------------------------


The new emergency directive ([ED 22-02](https://www.cisa.gov/emergency-directive-22-02)) further requires federal agencies to find all Internet-exposed devices vulnerable to Log4Shell exploits, patch them if a patch is available, mitigate the [risk of exploitation](https://www.cisa.gov/uscert/ed-22-02-apache-log4j-recommended-mitigation-measures), or remove vulnerable software from their networks until December 23.


CISA also says that all devices running software vulnerable to Log4Shell attacks should be assumed to be already compromised and requires looking for signs of post-exploitation activity and monitoring for any suspicious traffic patterns.


The federal agencies were also given five more days, until December 28 to report all affected Java products on their networks, including application and vendor names, the app's version, and the action taken to block exploitation attempts.


"Although ED 22-02 applies to FCEB agencies, CISA strongly recommends that all organizations review [ED 22-02](https://www.cisa.gov/emergency-directive-22-02) for mitigation guidance," CISA added today.



> 
> We are working with key private & public partners via [#JCDC](https://twitter.com/hashtag/JCDC?src=hash&ref_src=twsrc%5Etfw) & federal partners like [@FBI](https://twitter.com/FBI?ref_src=twsrc%5Etfw) & [@NSACyber](https://twitter.com/NSACyber?ref_src=twsrc%5Etfw) to manage this evolving threat. We will continue to update our consolidated Log4j webpage with the latest info to help all orgs reduce their risk: <https://t.co/qlZw2rh8y8>
> 
> 
> — Jen Easterly (@CISAJen) [December 17, 2021](https://twitter.com/CISAJen/status/1471886563453939714?ref_src=twsrc%5Etfw)


Log4Shell mitigation guidance
-----------------------------


Earlier this week, CISA published a [dedicated page](https://www.cisa.gov/uscert/apache-log4j-vulnerability-guidance) with technical details regarding the Log4Shell flaw and patching information for impacted organizations.


CISA asks organizations to upgrade to Log4j version 2.16.0 or immediately apply appropriate vendor-recommended mitigations.


The list of actions organizations using products exposed to attacks using Log4Shell exploits includes:


* **Reviewing Apache's**[**Log4j Security Vulnerabilities page**](https://logging.apache.org/log4j/2.x/security.html) for additional information.
* **Applying available patches immediately**. See [CISA's upcoming GitHub repository](https://github.com/cisagov/log4j-affected-db) for known affected products and patch information.
* **Conducting a security review**to determine if there is a security concern or compromise. The log files for any services using affected Log4j versions will contain user-controlled strings.
* **Reporting compromises immediately** to [CISA](https://us-cert.cisa.gov/report) and the [FBI](mailto:CyWatch@fbi.gov)

CISA's push for urgently patching systems vulnerable to Log4Shell attacks follows threat actors' head start in [exploiting Log4Shell vulnerable systems](https://www.bleepingcomputer.com/news/security/hackers-start-pushing-malware-in-worldwide-log4shell-attacks/) to deploy malware.


As we previously reported, these attacks have been orchestrated by financially-motivated attackers who [injected Monero miners](https://www.bleepingcomputer.com/news/security/log4j-attackers-switch-to-injecting-monero-miners-via-rmi/), [state-backed hackers](https://www.bleepingcomputer.com/news/security/log4j-vulnerability-now-used-by-state-backed-hackers-access-brokers/), and even ransomware gangs [[1](https://www.bleepingcomputer.com/news/security/conti-ransomware-uses-log4j-bug-to-hack-vmware-vcenter-servers/), [2](https://www.bleepingcomputer.com/news/security/new-ransomware-now-being-deployed-in-log4shell-attacks/)].


Following reporting of Log2Shell's ongoing exploitation in widespread attacks, we have also published several dedicated articles sharing a [list of vulnerable products and vendor advisories](https://www.bleepingcomputer.com/news/security/log4j-list-of-vulnerable-products-and-vendor-advisories/), the reason [why you must upgrade to Log4j2.16.0 immediately](https://www.bleepingcomputer.com/news/security/all-log4j-logback-bugs-we-know-so-far-and-why-you-must-ditch-215/), as well as more information on the [Log4Shell vulnerability](https://www.bleepingcomputer.com/tag/log4shell/).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Agriculture]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4shell]] [[Cisa]] [[Log4j]] [[Bleeping Computer]]
#### urls
https://t.co/qlZw2rh8y8
#### CVE's
[[CVE-2021-44228]]

