# Critical Cisco Bugs Allow Code Execution on Wireless, SD-WAN
### Unauthenticated cyberattackers can also wreak havoc on networking device configurations.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=174991)
+ Date: September 24, 2021  10:01 am
+ Author: Tara Seals


## Article:
![cisco IOS XE Flaw](https://media.threatpost.com/wp-content/uploads/sites/103/2020/11/11092729/cisco.jpg)
Cisco is warning three critical security vulnerabilities affect its flagship IOS XE software, the operating system for most of its enterprise networking portfolio. The flaws impact Cisco’s wireless controllers, SD-WAN offering and configuration mechanisms in use for scads of products.


The networking giant has released patches for all of them, as part of a comprehensive 32-bug update [released this week](https://tools.cisco.com/security/center/Search.x?publicationTypeIDs=1&firstPublishedStartDate=2021%2F09%2F21&firstPublishedEndDate=2021%2F09%2F23&limit=50).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The most severe of the critical bugs is an unauthenticated remote-code-execution (RCE) and denial-of-service (DoS) bug, affecting the Cisco Catalyst 9000 family of wireless controllers.


**CVE-2021-34770: RCE and DoS for Wireless Controllers**
--------------------------------------------------------


Boasting a rare 10 out of 10 CVSS vulnerability-severity rating, the issue ([CVE-2021-34770](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ewlc-capwap-rce-LYgj8Kf)) specifically exists in the control and provisioning of wireless access points (CAPWAP) protocol processing used by the Cisco IOS XE software that powers the devices.


“The vulnerability is due to a logic error that occurs during the validation of CAPWAP packets,” Cisco explained in its advisory this week. “An attacker could exploit this vulnerability by sending a crafted CAPWAP packet to an affected device. A successful exploit could allow the attacker to execute arbitrary code with administrative privileges or cause the affected device to crash and reload, resulting in a DoS condition.”


Absent a workaround or mitigation, admins should patch as soon as possible to avoid compromise. The affected products are:


**RCE and DoS for Cisco SD-WAN**
--------------------------------


The next two critical bugs both rate 9.8 out of 10 on the CVSS scale. The first of these is a software-buffer-overflow issue ([CVE-2021-34727](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxesdwan-rbuffover-vE2OB6tp)) in Cisco’s SD-WAN software (which can be enabled via IOS XE software), which could allow unauthenticated RCE as root and DoS attacks. It arises in the vDaemon process, according to the advisory.


“This vulnerability is due to insufficient bounds-checking when an affected device processes traffic,” according to Cisco. “An attacker could exploit this vulnerability by sending crafted traffic to the device. A successful exploit could allow the attacker to cause a buffer overflow and possibly execute arbitrary commands with root-level privileges, or cause the device to reload, which could result in a denial-of-service condition.”


Once again there are no workarounds or mitigations for this one, so patching promptly is a good idea. The following products are vulnerable if orgs are using the SD-WAN feature:


**CVE-2021-1619: Endangering Device Configurations**
----------------------------------------------------


The last critical bug is an authentication-bypass vulnerability in the IOS XE software – specifically affecting the network configuration protocol (NETCONF) used to install, manipulate and delete the configuration of network devices through a network management system; and the RESTCONF protocol, which is a REST-based HTTP interface used to query and configure devices with NETCONF configuration datastores.


The issue ([CVE-2021-1619](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-aaa-Yx47ZT8Q)) specifically resides in the authentication, authorization and accounting (AAA) function, Cisco explained, which could allow an unauthenticated, remote attacker to bypass NETCONF or RESTCONF authentication and wreak havoc in a couple of ways:


“This vulnerability is due to an uninitialized variable,” according to the advisory. “An attacker could exploit this vulnerability by sending a series of NETCONF or RESTCONF requests to an affected device.”


This vulnerability affects devices running the following:


**Workaround, Mitigation Available**
------------------------------------


Unlike the previous two bugs, this one has both a workaround and a mitigation.


On the workaround front, it’s important to note that to be vulnerable, three things must be configured:


Thus, users can remove the “enable password” configuration and configure “enable secret” instead, in order to protect themselves.


As for a mitigation, to limit the attack surface, admins can ensure that access control lists (ACLs) are in place for NETCONF and RESTCONF to prevent attempted access from untrusted subnets, Cisco advised.


***Rule #1 of Linux Security:****No cybersecurity solution is viable if you don’t have the basics down. [**JOIN**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the [**4 Golden Rules of Linux Security**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar). Your top takeaway will be a Linux roadmap to getting the basics right! [**REGISTER NOW**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.*




#### Tags:
[[Linux]] [[XE]] [[SD-WAN]] [[RESTCONF]] [[NETCONF]] [[RCE]] [[“An]] [[workaround]] [[ThreatPost]]
