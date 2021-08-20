# Critical Cisco Bug in Small Business Routers to Remain Unpatched
### The issue affects a range of Cisco Wireless-N and Wireless-AC VPN routers that have reached end-of-life.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168831)
+ Date: August 19, 2021  4:34 pm
+ Author: Tara Seals


## Article:
![cisco IOS XE Flaw](https://media.threatpost.com/wp-content/uploads/sites/103/2020/11/11092729/cisco.jpg)
A critical security vulnerability in Cisco Small Business Routers (RV110W, RV130, RV130W and RV215W models) allows remote code execution (RCE) and denial of service (DoS). The networking giant said that no patch or workaround will be coming for the bug, since the routers reached end-of-life back in 2019.


The bug ([CVE-2021-34730](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cisco-sb-rv-overflow-htpymMB5)) is one of six addressed by Cisco this week; it also issued an advisory for the critical BlackBerry QNX-2021-001 vulnerability unveiled earlier this week (CVE-2021-22156), which affects multiple vendors, well beyond Cisco.


**Patch Denied: Critical RCE for EoL Gear**
-------------------------------------------


The critical router issue, which carries a base CVSS score of 9.8 out of 10, affects the hardware’s Universal Plug-and-Play (UPnP) service, Cisco said. It could allow an unauthenticated attacker to achieve RCE or cause an affected device to restart unexpectedly.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“This vulnerability is due to improper validation of incoming UPnP traffic,” according to the advisory. “An attacker could exploit this vulnerability by sending a crafted UPnP request to an affected device. A successful exploit could allow the attacker to execute arbitrary code as the root user on the underlying operating system or cause the device to reload, resulting in a DoS condition.”


The issue affects a range of Cisco Wireless-N and Wireless-AC VPN routers, which [reached end-of-life](https://www.cisco.com/c/en/us/products/collateral/routers/small-business-rv-series-routers/eos-eol-notice-c51-742771.html) in September of 2019. Cisco stopped issuing bug fixes on Dec. 1 of last year. Affected companies should look to update their hardware to avoid compromise.


The other critical flaw addressed in the updates has to do with the BlackBerry QNX-2021-001 bug [disclosed this week](https://threatpost.com/blackberrys-qnx-devices-attacks/168772/), which allows threat actors to take over or launch DoS attacks on devices and critical infrastructure. Essentially, the known group of BadAlloc bugs tied to BlackBerry’s embedded QNX operating system (OS) now affects older devices.


Cisco’s advisory simply states, “Cisco is investigating its product line to determine which products and services may be affected by this vulnerability.” So far, no products have been listed.


**Medium-Severity Security Bugs in Cisco Gear**
-----------------------------------------------


The remaining five patches are all rated medium in severity, and affect products from across Cisco’s portfolio. These bugs are:


The first bug could allow an unauthenticated, remote attacker to bypass filtering technology on an affected device to execute a command-and-control attack on a compromised host and perform and exfiltrate data from a compromised host. The advisory is an interim one, and Cisco said it was still investigating which product versions are affected.


“This vulnerability is due to inadequate filtering of the SSL handshake,” according to the advisory. “An attacker could exploit this vulnerability by using data from the SSL client hello packet to communicate with an external server.”


The spam-quarantine-related vulnerability affects Cisco Secure Email and Web Manager releases earlier than Release 14.1. It could allow an authenticated, remote attacker to gain unauthorized access and modify the spam quarantine settings of another user, so that malicious messages could get through or attackers could read messages.


“This vulnerability exists because access to the spam quarantine feature is not properly restricted,” according to the advisory. “An attacker could exploit this vulnerability by sending malicious requests to an affected system.”


The third bug exists in the Link Layer Discovery Protocol (LLDP) implementation for Cisco Video Surveillance 7000 Series IP Cameras with firmware release 2.12.4. Exploitation could allow an unauthenticated, adjacent attacker to cause a DoS condition.


“This vulnerability is due to improper management of memory resources, referred to as a double free,” according to Cisco. “An attacker could exploit this vulnerability by sending crafted LLDP packets to an affected device.”


The last two vulnerabilities exist in the Expressway and TelePresence products and can be exploited by authenticated, remote attackers to execute code.


The first of these allows RCE with internal user privileges on the underlying operating system; it affects users running a release earlier than the first fixed release (the bug was introduced when support for validation of SHA512 checksums was introduced in Release X8.8).


The second allows RCE on the underlying operating system as the root user. It affects releases earlier than the first fixed release if users are running Release X8.6 or later.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[RCE]] [[“This]] [[“An]] [[advisory.]] [[ThreatPost]]
