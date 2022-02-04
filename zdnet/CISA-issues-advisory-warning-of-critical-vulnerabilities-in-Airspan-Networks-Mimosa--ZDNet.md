# CISA issues advisory warning of critical vulnerabilities in Airspan Networks Mimosa | ZDNet
### The vulnerabilities go all the way up to 10 on the CVSS severity score.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/cisa-issues-advisory-warning-of-critical-vulnerabilities-in-airspan-networks-mimosa/
+ Date: 2022-02-04 10:05:06
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/0a23fd3fd1977148ea7e0c43698e65290bb65d8b/2021/11/02/0c449f08-f978-48e5-b0c2-6d0f588ad91e/sale-305237-article-image.jpg?width=770&height=578&fit=crop&auto=webp)

CISA has warned of critical vulnerabilities in Airspan Networks Mimosa, some of which have earned CVSS severity score ratings of 10, the highest possible. 


When security vulnerabilities are severe and the products they impact are popular or critical to the operations of key industries, the US Cybersecurity and Infrastructure Security Agency (CISA) will often issue advisories to make sure they reach the attention of IT administrators and security staff. 

On Thursday, CISA issued such [an advisory](https://www.cisa.gov/uscert/ics/advisories/icsa-22-034-02) for Airspan Networks Mimosa. [Mimosa](https://mimosa.co/) devices are offered to industrial and enterprise players for point-to-multipoint (PTMP) network deployment. 

Seven vulnerabilities have been included in the advisory, detailing bugs earning themselves CVSS v3 base scores ranging from 6.5 to 10.0. 

The Airspan Networks products impacted by the vulnerabilities are the Mimosa Management Platform (MMP) prior to v1.0.3; PTP C-series devices running firmware prior to v2.8.6.1, and both PTMP C-series and A5x devices running firmware below v2.5.4.1. 

Noam Moshe, of Claroty, reported the security issues, which are said to be exploitable remotely and with low attack complexity.  

"Successful exploitation of these vulnerabilities could allow an attacker to gain user data (including organization details) and other sensitive data, compromise Mimosa's AWS cloud EC2 instance and S3 buckets, and execute unauthorized remote code on all cloud-connected Mimosa devices," CISA says. 






The vulnerabilities are below: 

* **CVE-2022-21196** (CVSS 10.0): An improper authorization flaw caused by failures to conduct authentication checks across multiple API routes, leading to denial-of-service, information leaks, and remote code execution (RCE).
* **CVE-2022-21141** (CVSS 10.0): Additional failures to perform authorization checks on API functions, leading to the same attack vectors.
* **CVE-2022-21215** (CVSS 10.0): A server side request forgery (SSRF) flaw that can be exploited by an attacker to force a server to grant access to backend APIs.
* **CVE-2022-21176** (CVSS 8.6): The improper neutralization of elements in SQL commands. A lack of user input sanitization could lead to SQL injections and data leaks.
* **CVE-2022-0138** (CVSS 7.5): A deserialization function doesn't validate or check data input properly, allowing arbitrary classes to be created.
* **CVE-2022-21143** (CVSS 9.8): User input is not properly sanitized in some areas, giving attackers the opportunity to execute arbitrary commands.
* **CVE-2022-21800** (CVSS 6.5): The product line uses the MD5 algorithm for password hashing but failed to salt the hash, causing a higher risk of sensitive data being susceptible to cracking attempts.

There is no evidence that the vulnerabilities have been exploited in the wild. Airspan Networks recommends that customers upgrade to MMP v.1.0.4 or later, PTP C5x/C5c (v2.90 or later), and PTMP C-series/A5x v.2.9.0 or later.  

In January, CISA updated its Known Exploited Vulnerabilities catalog with [13 new vulnerabilities](https://www.zdnet.com/article/cisa-adds-13-exploited-vulnerabilities-to-list-9-with-feb-1-remediation-date/). In total, nine had a remediation date of February 1, and four have a remediation date of July 18.  

The bugs include a command injection flaw in the System Information Library for node.js, a Drupal unrestricted file upload issue, and command injection vulnerabilities in the Nagios XI operating system. 

ZDNet has reached out to the Airspan Networks Mimosa team and we will update when we hear back.  

###  Previous and related coverage

* [CISA adds 13 exploited vulnerabilities to list, 9 with Feb. 1 remediation date](https://www.zdnet.com/article/cisa-adds-13-exploited-vulnerabilities-to-list-9-with-feb-1-remediation-date/)
* [CISA warns - upgrade your cybersecurity now to defend against "potential critical threats"](https://www.zdnet.com/article/cisa-warns-upgrade-your-cybersecurity-now-to-defend-against-potential-critical-threats/)
* [CISA director: 'We have not seen significant intrusions' from Log4j -- yet](https://www.zdnet.com/article/cisa-director-we-have-not-seen-significant-intrusions-from-log4j/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Cisa]] [[(cvss]] [[Airspan]] [[ZDNet]]
#### CVE's
[[CVE-2022-21196]] [[CVE-2022-21141]] [[CVE-2022-21215]] [[CVE-2022-21176]] [[CVE-2022-0138]] [[CVE-2022-21143]] [[CVE-2022-21800]]

