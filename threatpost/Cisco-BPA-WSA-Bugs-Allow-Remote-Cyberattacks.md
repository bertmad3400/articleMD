# Cisco BPA, WSA Bugs Allow Remote Cyberattacks
### The high-severity security vulnerabilities allow elevation of privileges, leading to data theft and more.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167654)
+ Date: July 9, 2021  1:31 pm
+ Author: Tara Seals


## Article:
![cisco IOS XE Flaw](https://media.threatpost.com/wp-content/uploads/sites/103/2020/11/11092729/cisco.jpg)
A set of high-severity privilege-escalation vulnerabilities affecting Business Process Automation (BPA) application and Cisco’s Web Security Appliance (WSA) and could allow authenticated, remote attackers to access sensitive data or take over a targeted system.


The first two bugs (CVE-2021-1574 and CVE-2021-1576) exist in the web-based management interface of the Cisco Business Process Automation (BPA), which is used to streamline various IT processes. Its functions include OS upgrades, device activation, compliance checks and server migration.


The flaws, which both rate 8.8 out of 10 on the CVSS vulnerability-severity scale, could allow an authenticated, remote attacker to elevate privileges to administrator-level. A successful exploit would involve sending crafted HTTP messages to an affected system.



“These vulnerabilities are due to improper authorization enforcement for specific features and for access to log files that contain confidential information,” according to Cisco’s [Thursday advisory](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-bpa-priv-esc-dgubwbH4). Exploitation could result in an adversary “performing unauthorized actions with the privileges of an administrator, or by retrieving sensitive data from the logs and using it to impersonate a legitimate privileged user,” the company noted.


The vulnerabilities affect Cisco BPA releases earlier than Release 3.1.


Meanwhile, the third bug affects Cisco’s WSA appliance, which provides protection for those using a corporate network to access the web, by automatically blocking risky sites and testing unknown sites before allowing users to click on them.


The issue (CVE-2021-1359, with a CVSS score of 6.3 out of 10) exists in the configuration management of the Cisco AsyncOS operating system that powers the WSA. According to Cisco’s [advisory](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-scr-web-priv-esc-k3HCGJZ), it could allow an authenticated, remote attacker to perform command injection and elevate privileges to root.


“This vulnerability is due to insufficient validation of user-supplied XML input for the web interface,” the networking giant explained. “An attacker could exploit this vulnerability by uploading crafted XML configuration files that contain scripting code to a vulnerable device. A successful exploit could allow the attacker to execute arbitrary commands on the underlying operating system and elevate privileges to root.”


The bug rates high-severity rather than critical since any would-be attacker would need a valid user account with the rights to upload configuration files in order to exploit the bug – something that could be achieved via another exploit or phishing attack.


The issue affects both the virtual and hardware-based iterations of the appliances, in Releases 11.8 and earlier, 12.0 and 12.5.


These are just the latest patches that Cisco has issued; last month, [it patched](https://threatpost.com/cisco-smart-switches-security-holes/167031/) several high-severity security vulnerabilities in its Small Business 220 Series Smart Switches, which are intro-level networking gear for SMBs. The flaws could allow remote attacks designed to steal information, drop malware and disrupt operations, via session hijacking, arbitrary code execution, cross-site scripting (XSS) and HTML injection.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[high-severity]] [[BPA]] [[WSA]] [[ThreatPost]]
