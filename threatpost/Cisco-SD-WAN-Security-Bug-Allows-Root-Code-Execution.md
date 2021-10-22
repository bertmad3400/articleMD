# Cisco SD-WAN Security Bug Allows Root Code Execution
### The high-severity bug, tracked as CVE-2021-1529, is an OS command-injection flaw.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175669)
+ Date: October 22, 2021  10:48 am
+ Author: Tara Seals


## Article:
![cisco patch DCNM](https://media.threatpost.com/wp-content/uploads/sites/103/2020/07/30102437/cisco-patch.png)
Cisco SD-WAN implementations are vulnerable to a high-severity privilege-escalation vulnerability in the IOS IE operating system that could allow arbitrary code execution.


Cisco’s SD-WAN portfolio allows businesses of all sizes to connect disparate office locations via the cloud using various networking technologies, including standard internet connections. Appliances at each location enable advanced analytics, monitoring, application-specific performance specifications and automation for any connection across a company’s wide-area network.


IOS XE, meanwhile, is the vendor’s operating system that runs those appliances. It’s a combination of a Linux kernel and a monolithic application that runs on top of that kernel.


The bug (CVE-2021-1529) is an [OS command-injection issue](https://cwe.mitre.org/data/definitions/78.html), which enables attackers to execute unexpected, dangerous commands directly on the operating system that normally wouldn’t be accessible. It specifically exists in the command-line interface (CLI) for Cisco’s IOS XE SD-WAN software, and could allow an authenticated, local attacker to execute arbitrary commands with root privileges.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“The vulnerability is due to insufficient input validation by the system CLI,” according to Cisco’s advisory, [posted this week](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sd-wan-rhpbE34A). “A successful exploit could allow the attacker to execute commands on the underlying operating system with root privileges.”


The advisory also noted that the exploitation path would involve authenticating to a vulnerable device and submitting “crafted input” to the system CLI. A successful compromise would give an attacker the ability to read and write any files on the system, perform operations as any user, change system configurations, install and remove software, upgrade the OS and/or firmware, and much more, including follow-on access to a corporate network.


CVE-2021-1529 rates 7.8 on the CVSS vulnerability-severity scale, and researchers and the Cybersecurity and Infrastructure Security Agency (CISA) [warned that](https://us-cert.cisa.gov/ncas/current-activity/2021/10/21/cisco-releases-security-updates-ios-xe-sd-wan-software) businesses should patch the bug as soon as possible.


Greg Fitzgerald, co-founder at Sevco Security, warned that some organizations may have outdated boxes still attached to their networks, which can be a hidden danger with bugs like these.


“The vast majority of organizations do an excellent job patching the vulnerabilities on the systems they know about,” he said via email. “The problem arises when enterprises do not have complete visibility into their asset inventory, because even the most responsive IT and security teams can’t patch a vulnerability for an asset they don’t know is connected to their network. Abandoned and unknown IT assets are often the path of least resistance for malicious actors trying to access your network or data.”


This is only the latest SD-WAN vulnerability that Cisco has patched this year. In January, [it fixed](https://threatpost.com/critical-cisco-sd-wan-bugs-rce-attacks/163204/) multiple, critical buffer-overflow and command-injection SD-WAN bugs, the most serious of which could be exploited by an unauthenticated, remote attacker to execute arbitrary code on the affected system with root privileges.


In May, Cisco addressed two critical security vulnerabilities in the SD-WAN vManage Software, one of [which could allow](https://threatpost.com/critical-cisco-sd-wan-hyperflex-bugs/165923/) an unauthenticated attacker to carry out remote code execution (RCE) on corporate networks or steal information.


And just last month, Cisco [disclosed](https://threatpost.com/critical-cisco-bugs-wireless-sd-wan/174991/) two critical security vulnerabilities affecting the IOS XE software and its SD-WAN, the most severe of which would allow unauthenticated RCE and denial-of-service (DoS).


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[SD-WAN]] [[Cisco’s]] [[network.]] [[“The]] [[ThreatPost]]
