# Cisco fixes highly critical vulnerabilities in IOS XE Software
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/cisco-fixes-highly-critical-vulnerabilities-in-ios-xe-software/)
+ Date: September 24, 2021
+ Author: Ionut Ilascu


## Article:
![Cisco fixes highly critical vulnerabilities in IOS XE Software](https://www.bleepstatic.com/content/hl-images/2021/02/03/Cisco.jpg)


Cisco has patched three critical vulnerabilities affecting components in its IOS XE internetworking operating system powering routers and wireless controllers, or products running with a specific configuration.


The worst of the flaws received the highest severity rating, 10 out of 10; it affects the Cisco Catalyst 9000 Family Wireless Controllers that includes the enterprise-class Catalyst 9800-CL Wireless Controllers for Cloud.


### Remotely exploitable, no authentication


The security issues are part of Cisco’s updates for September 2021 and the full list of fixes [counts 31 bugs](https://tools.cisco.com/security/center/Search.x?publicationTypeIDs=1&firstPublishedStartDate=2021%2F09%2F21&firstPublishedEndDate=2021%2F09%2F23&limit=50), with more than a dozen of them being rated with a high-severity score or worse.


At the top of the list in terms of severity is [CVE-2021-34770](https://nvd.nist.gov/vuln/detail/CVE-2021-34770), a vulnerability that could be exploited remotely by an unauthenticated attacker to run arbitrary code with root privileges, a Cisco [advisory](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ewlc-capwap-rce-LYgj8Kf) informs.


The issue is in the Control and Provisioning of Wireless Access Points (CAPWAP) protocol processing of Cisco IOS XE Software for Cisco Catalyst 9000 Family Wireless Controllers. Affected by CVE-2021-34770 include:


* Catalyst 9800 Embedded Wireless Controller for Catalyst 9300, 9400, and 9500 Series Switches
* Catalyst 9800 Series Wireless Controllers
* Catalyst 9800-CL Wireless Controllers for Cloud
* Embedded Wireless Controller on Catalyst Access Points


Another critical-severity vulnerability, albeit with a lower score (9.8/10), is now identified as [CVE-2021-34727](https://nvd.nist.gov/vuln/detail/CVE-2021-34727). Caused by insufficient bounds checking, it is in the vDaemon process in Cisco IOS XE SD-WAN Software, [Cisco notes](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxesdwan-rbuffover-vE2OB6tp).


An attacker can leverage it remotely without authentication by sending modified traffic to a vulnerable target device. Successful exploitation could lead to executing arbitrary commands with the highest privileges or at least cause a denial-of-service (DoS) condition.


The following products are vulnerable if they run an outdated version of Cisco IOS XE SD-WAN software and have the SD-WAN feature active (disabled by default):


* 1000 Series Integrated Services Routers (ISRs)
* 4000 Series ISRs
* ASR 1000 Series Aggregation Services Routers
* Cloud Services Router 1000V Series


Last on the list of critical bugs that Cisco patched this month is [CVE-2021-1619](https://nvd.nist.gov/vuln/detail/CVE-2021-1619), a security issue in the authentication, authorization, and accounting (AAA) function of Cisco IOS XE software.


A remote, unauthenticated adversary could use it to “install, manipulate, or delete the configuration of an affected device.” The smallest risk is creating a DoS condition.



“This vulnerability is due to an uninitialized variable. An attacker could exploit this vulnerability by sending a series of NETCONF or RESTCONF requests to an affected device. A successful exploit could allow the attacker to use NETCONF or RESTCONF to install, manipulate, or delete the configuration of a network device or to corrupt memory on the device, resulting a DoS” - [Cisco](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-aaa-Yx47ZT8Q)



The issue impacts devices running Cisco IOS XE if set up in autonomous or controller mode, and Cisco IOS XE SD-WAN. In either case, the condition for a product to be vulnerable is to have configured all of the following:


* AAA
* NETCONF, RESTCONF, or both
* enable password without enable secret


Cisco’s advisory for CVE-2021-1619 provides the commands to check if the device is configured in a way that makes it vulnerable. If the latest update cannot be installed right away, a [workaround and mitigation](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-aaa-Yx47ZT8Q) exist.


At this time, there is no public information that any of the above critical vulnerabilities have been exploited in the wild.




#### Tags:
[[XE]] [[SD-WAN]] [[Bleeping Computer]]
