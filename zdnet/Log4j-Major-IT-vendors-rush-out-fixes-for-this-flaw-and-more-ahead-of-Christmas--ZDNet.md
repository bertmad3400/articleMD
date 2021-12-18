# Log4j: Major IT vendors rush out fixes for this flaw and more ahead of Christmas | ZDNet
### IBM and Cisco release Log4j fixes as VMware patches critical non-Log4j flaw.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/vmware-patches-critical-non-log4j-flaw-as-ibm-cisco-release-log4j-fixes/
+ Date: 2021-12-17 12:28:00
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/7351a4d62e302e3e026b8e9d2efdafd1c53b0fa6/2021/12/09/8afcec0f-e4c5-49cd-8c26-9b06dd6b370e/shutterstock-2056455242.jpg?width=770&height=578&fit=crop&auto=webp)

The holiday season is shaping up to be busy for those patching systems affected by the critical flaw in the Log4j Java application error logging library. 

IBM has confirmed several of its major enterprise products are [affected by the Log4j bug](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/). On Thursday, the company [confirmed that the IBM Db2 Warehouse](https://www.ibm.com/blogs/psirt/security-bulletin-vulnerability-in-apache-log4j-affects-ibm-db2-warehouse-cve-2021-44228/), which uses Log4j, allowed a remote attacker to execute arbitrary code on the system. Log4j is used in the Db2 Federation feature. IBM has released a [special fix pack and mitigation notes](https://www.ibm.com/support/pages/node/6527322) for Db2 version 11.5 systems that are vulnerable if certain Federation features are configured. 

Since Wednesday, IBM has released Log4j fixes for over a dozen cloud products, spanning security and identity, analytics, databases, managed VMware services, and Watson AI products. It has also released fixes for 20 on-premises IBM products for Cognos business intelligence, Power hardware, WebSphere, Watson, and more. 



---

###  LOG4J FLAW COVERAGE - WHAT YOU NEED TO KNOW NOW

* **[**Log4j zero-day flaw: What you need to know and how to protect yourself**](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/#link=%7B%22linkText%22:%22Log4j%20zero-day%20flaw:%20What%20you%20need%20to%20know%20and%20how%20to%20protect%20yourself%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)**
* **[**Security warning: New zero-day in the Log4j Java library is already being exploited**](https://www.zdnet.com/article/security-warning-new-zero-day-in-the-log4j-java-library-is-already-being-exploited/#link=%7B%22linkText%22:%22Security%20warning:%20New%20zero-day%20in%20the%20Log4j%20Java%20library%20is%20already%20being%20exploited%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/security-warning-new-zero-day-in-the-log4j-java-library-is-already-being-exploited/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)**
* **[**Log4j flaw could be a problem for industrial networks 'for years to come'**](https://www.zdnet.com/article/log4j-flaw-could-be-a-problem-for-industrial-networks-for-years-to-come/#link=%7B%22linkText%22:%22Log4j%20flaw%20could%20be%20a%20problem%20for%20industrial%20networks%20'for%20years%20to%20come'%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/log4j-flaw-could-be-a-problem-for-industrial-networks-for-years-to-come/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)**



---

IBM is continually [updating the list of products affected by the flaw](https://www.ibm.com/blogs/psirt/an-update-on-the-apache-log4j-cve-2021-44228-vulnerability/#Remediated-Products) and those it has confirmed are not impacted.  

Dozens of Cisco products are affected by Log4j, too. On Friday, Cisco will release numerous firmware and hotfix updates that address the flaw, followed by more updates scheduled over the weekend and over the following week through to 24 December.  

Products scheduled for [updates on Friday include](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apache-log4j-qRuKNEbd) Cisco Identity Services Engine, DNA Spaces Connector, Cisco BroadWorks, and Cisco Finesee. On Saturday, it will release updates for several more products including Cisco Contact Center Domain Manager (CCDM), Cisco IOx Fog Director, Cisco Contact Center Management Portal (CCMP), Cisco Unified Communications Manager / Cisco Unified Communications Manager Session Management Edition, Cisco Video Surveillance Operations Manager, and Cisco Connected Mobile Experiences (CMX).   

VMware is also [updating its list of affected products](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), most of which are badged as 'critical' with a CVSS severity score of 10 out of 10, and currently marked as 'patch pending'. Where patches are not available, VMware is updating its recommended mitigations to factor in updates addressed by [Apache Foundation's Log4j version 2.16 release](https://www.zdnet.com/article/second-log4j-vulnerability-found-apache-log4j-2-16-0-released/), which addressed the incomplete patch it initially released last week. 






VMware had over 100 products affected by the bug popularly known as Log4Shell, and tracked as CVE 2021-44228. 

But the virtualisation giant has also released a patch to address a critical non-Log4j Server Side Request Forgery (SSRF) vulnerability in its Workspace ONE Unified Endpoint Management (UEM) console. 

Tracked as CVE-2021-22054, this flaw would allow an attacker with network access to UEM to "send their requests without authentication and may exploit this issue to gain access to sensitive information", [according to VMware's advisory](https://www.vmware.com/security/advisories/VMSA-2021-0029.html).  



---

###  LOG4J FLAW COVERAGE - WHAT YOU NEED TO KNOW NOW

* **[US warns Log4j flaw puts hundreds of millions of devices at risk](https://www.zdnet.com/article/log4j-flaw-puts-hundreds-of-millions-of-devices-at-risk-says-us-cybersecurity-agency/)**
* [**Log4j flaw: Attackers are making thousands of attempts to exploit this severe vulnerability**](https://www.zdnet.com/article/log4j-flaw-attackers-are-making-thousands-of-attempts-to-exploit-this-severe-vulnerability#link=%7B%22linkText%22:%22Log4j%20flaw:%20Attackers%20are%20making%20thousands%20of%20attempts%20to%20exploit%20this%20severe%20vulnerability%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/log4j-flaw-attackers-are-making-thousands-of-attempts-to-exploit-this-severe-vulnerability%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)
* [**Log4j RCE activity began on December 1 as botnets start using vulnerability**](https://www.zdnet.com/article/log4j-rce-activity-began-on-december-1-as-botnets-start-using-vulnerability/#link=%7B%22linkText%22:%22Log4j%20RCE%20activity%20began%20on%20December%201%20as%20botnets%20start%20using%20vulnerability%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/log4j-rce-activity-began-on-december-1-as-botnets-start-using-vulnerability/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)



---

The vulnerability got a CVSS score of 9.1 out of 10, and so should be added to the list of priorities for patching before the Christmas break. The bug affects the 2105, 2012, 2011, and 2008 versions of the Workspace ONE UEM console.  

The Cybersecurity and Infrastructure Security Agency and the White House [yesterday warned](https://www.zdnet.com/article/cisa-white-house-urge-organizations-to-get-ready-for-holiday-cyberattacks/) organisations in the US to beware of cyberattacks during the holiday season. Cyber criminals frequently launch major [ransomware attacks on public holidays to take advantage of skeleton staffing](https://www.zdnet.com/article/security-warning-ransomware-attackers-are-working-on-the-holidays-even-if-you-arent/). 

CISA has instructed federal agencies to [identify all applications affected by the Log4j flaw by 24 December](https://www.zdnet.com/article/log4j-flaw-now-state-backed-hackers-are-using-bug-as-part-of-attacks-warns-microsoft/).  

CISA has [published a list of vendors and products](https://github.com/cisagov/log4j-affected-db) affected by the Log4Shell flaw. The [Netherlands cybersecurity agency is also updating a list of affected products and vendors](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/), which it published earlier this week. 






## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Location:
[[victim.country.name=Netherlands]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Vmware]] [[Db2]] [[ZDNet]]
#### CVE's
[[CVE-2021-22054]]

