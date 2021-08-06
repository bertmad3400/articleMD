# Critical Cisco Bug in VPN Routers Allows Remote Takeover
### Security researchers warned that at least 8,800 vulnerable systems are open to compromise.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168449)
+ Date: August 6, 2021  12:07 pm
+ Author: Tara Seals


## Article:
![cisco patch DCNM](https://media.threatpost.com/wp-content/uploads/sites/103/2020/07/30102437/cisco-patch.png)
A critical security vulnerability in a subset of Cisco Systems’ small-business VPN routers could allow a remote, unauthenticated attacker to take over a device – and researchers said there are at least 8,800 vulnerable systems open to compromise.


Cisco addressed the bugs (CVE-2021-1609) as part of a slew of patches rolled out this week. In total, the fixes and affected products are as follows:


**Critical RCE Security Bug in Gigabit VPN Routers**
----------------------------------------------------


The critical bug affects the vendor’s Dual WAN Gigabit VPN routers. According to the advisory, CVE-2021-1609 exists in the web management interface for the devices, and carries a CVSSv3 vulnerability-severity score of 9.8. It arises due to improper validation of HTTP requests.



According to [a Thursday analysis](https://www.tenable.com/blog/cve-2021-1609-critical-rce-vulnerability-cisco-small-business-vpn-routers) from Tenable, a remote, unauthenticated attacker could thus exploit the vulnerability by sending a specially crafted HTTP request to a vulnerable device, “resulting in arbitrary code-execution as well as the ability to reload the device, resulting in a denial of service (DoS).”


Remote management of these devices is disabled by default according to Cisco, which would thwart such attacks. However, researchers at Tenable found that more than 8,800 devices are publicly accessible and vulnerable to exploit.


Meanwhile, a second bug affecting the same devices, CVE-2021-1610, is a high-rated command-injection vulnerability in the same web management interface.


“While both flaws exist due to improper validation of HTTP requests and can be exploited by sending specially crafted HTTP requests, CVE-2021-1610 can only be exploited by an authenticated attacker with root privileges,” according to Tenable. “Successful exploitation would grant an attacker the ability to gain arbitrary command execution on the vulnerable device’s operating system.”


The web management interface for its small business VPN routers is available by default through local area network connections and can’t be disabled, Cisco noted, adding that that some versions of the router software may only be affected by one of the two vulnerabilities.


Though no in-the-wild exploitation has been seen thus far for the bugs, Tenable warned that this is likely to change.


“In January 2019, Cisco published advisories for two different vulnerabilities in its RV320 and RV325 WAN VPN routers,” according to the analysis. “A few days after the advisories were published, proof-of-concept exploit scripts for these flaws were published, which was followed by active scanning for vulnerable devices. Because of this historical precedent, we believe it is important that organizations patch these latest vulnerabilities as soon as possible.”


If patching isn’t possible, users should make sure that remote web management is disabled, the firm added.


**High-Severity Cisco Security Bugs**
-------------------------------------


Cisco also addressed several high-severity bugs, with severity ratings ranging between 8.8 and 7.8 on the CVSSv3 scale.


The bug tracked as CVE-2021-1602 exists in the web-based management interface of Cisco Small Business RV160, RV160W, RV260, RV260P, and RV260W VPN Routers – if exploited, it could allow an unauthenticated, remote attacker to execute arbitrary commands using root-level privileges, on the underlying operating system.


Like the Gigabit VPN router issues, the vulnerability is due to insufficient user input validation, and an attacker could exploit it by sending a crafted request to the web-based management interface. However, a mitigating factor is the fact that only commands without parameters can be executed, according to Cisco.


Meanwhile, a vulnerability in Cisco Packet Tracer for Windows (CVE-2021-1593) could allow an authenticated, local attacker to perform a DLL injection attack on an affected device. An attacker must have valid credentials on the Windows system in order to be successful, according to the advisory.


“This vulnerability is due to incorrect handling of directory paths at run time,” Cisco explained. “An attacker could exploit this vulnerability by inserting a configuration file in a specific path on the system, which can cause a malicious DLL file to be loaded when the application starts. A successful exploit could allow an attacker with normal user privileges to execute arbitrary code on the affected system with the privileges of another user’s account.”


The last high-severity security issue is tracked as CVE-2021-1572, and it affects both the Cisco Network Services Orchestrator (NSO) and ConfD options for the CLI Secure Shell (SSH) Server. It’s a privilege-escalation bug that could allow an authenticated, local attacker to execute arbitrary commands at the level of the account under which the service is running, which is commonly root.


To exploit the vulnerability, an attacker must have a valid account on an affected device.


“The vulnerability exists because the affected software incorrectly runs the SFTP user service at the privilege level of the account that was running when the built-in SSH server for CLI was enabled,” according to Cisco. “An attacker with low-level privileges could exploit this vulnerability by authenticating to an affected device and issuing a series of commands at the SFTP interface.”


Any user who can authenticate to the built-in SSH server could exploit the bug, the vendor warned.


Since Cisco bugs [are popular with cyberattackers](https://threatpost.com/cisco-asa-bug-exploited-poc/167274/), users should update to the latest versions of the affected products (patches available via links above).


**Worried about where the next attack is coming from? We’ve got your back.****[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)****for our upcoming live webinar,****[How to Think Like a Threat Actor](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)****, in partnership with Uptycs. Find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on Aug. 17 at 11AM EST for this****[LIVE](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)****discussion.**




#### Tags:
[[VPN]] [[HTTP]] [[ThreatPost]]
