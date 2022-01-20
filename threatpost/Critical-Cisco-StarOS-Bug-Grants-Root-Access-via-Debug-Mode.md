# Critical Cisco StarOS Bug Grants Root Access via Debug Mode
### Cisco issued a critical fix for a flaw in its Cisco RCM for Cisco StarOS Software that could give attackers RCE on the application with root-level privileges.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177832
+ Date: 2022-01-20T19:35:29+00:00
+ Author: Becky Bracken


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2020/08/27153752/cisco.jpg)

Cisco released a security update warning about a handful of vulnerabilities lurking in its networking technology, led by a critical bug in the company’s StarOS debug services.


[Cisco pushed out a fix](https://www.cisa.gov/uscert/ncas/current-activity/2022/01/20/cisco-releases-security-updates-multiple-products) for its Cisco StarOS Software on Wednesday. Jan. 19. In its [advisory](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-rcm-vuls-7cS3Nuq), the company said that the flaw in its debug service could allow an attacker to access sensitive debugging data.


Cisco StarOS Software works with [Cisco ASR 5000 devices](https://www.cisco.com/c/en/us/products/wireless/asr-5000-series/index.html) to operate virtual mobile networks for enterprises and service providers.


The critical bug – tracked as CVE-2022-20649 – is in the software’s Redundancy Configuration Manager. It was given a CVSS score of 9, since it could potentially allow an attacker root access to execute commands of their choice.


“This vulnerability exists because the debug mode is incorrectly enabled for specific services,”  

Cisco’s alert said. “An attacker could exploit this vulnerability by connecting to the device and navigating to the service with debug mode enabled.”


Cisco has released an [update for the vulnerability](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-rcm-vuls-7cS3Nuq#vp), which has no workaround. Cisco’s Product Security Incident Response Team (PSIRT) said that the company isn’t aware of the vulnerability being exploited in the wild.


In addition to the fix for its Cisco StarOS Software debug service, Cisco also provided the following trio of security updates for mobile network operators running both Cisco hardware and software for virtualization.


**Snort Modbus DOS Vuln**
-------------------------


An additional fix was issued for a denial-of-service (DoS) vulnerability in the Modbus processor of the [Snort detection engine](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort-dos-9D3hJLuj) deployed by virtual mobile network operators.


Snort is an open-source solution that sniffs out malicious mobile network traffic.


The affected [Cisco products](https://threatpost.com/critical-cisco-contact-center-bug/177681/) include Cybervision Software, Firepower Threat Defense (FTD) Software across all platforms and Meraki MX Series Software. Other Cisco products that are running an outdated version of the Cisco Unified Threat Defense (UTD) Snort Intrusion Prevention System (IPS) Engine for Cisco IOS XE Software or Cisco UTD Engine for Cisco IOS XE SD-WAN Software are also vulnerable, which could include Cisco routers and edge platforms, the company warned.


“This vulnerability is due to an integer overflow while processing Modbus traffic,” Cisco said. ‘An attacker could exploit this vulnerability by sending crafted Modbus traffic through an affected device. A successful exploit could allow the attacker to cause the Snort process to hang, causing traffic inspection to stop.”


The Snort Modbus bug (CVE-2022-20685) was assigned a CVSS score of 7.5.


**CoffD CLI Command Injection Vuln**
------------------------------------


Cisco also alerted customers about a [vulnerability in the ConfD configuration](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-confdcli-cmdinj-wybQDSSh) management system that could allow a command injection attack by an authenticated, local threat actor in the area with a device running ConfD, the company said.


“The vulnerability is due to insufficient validation of a process argument on an affected device,” the Cisco security alert added. “An attacker could exploit this vulnerability by injecting commands during the execution of this process.”


If successful, the attacker could gain access with the ConfD privilege access, which is typically root access, Cisco warned.


The ConfD CLI (CVE-2022-20655) exploit was assigned a CVSS score of 8.8.


**Cisco CLI Command Injection Vuln Across ‘Many’ Products**
-----------------------------------------------------------


Network operators running [Cisco products](https://threatpost.com/cisco-smart-switches-security-holes/167031/) for mobile internet, network management and provisioning, optical networking, enterprise and service provider routing and switching are likely vulnerable to a command injection vulnerability caused by a [faulty implementation of the Command Line Interface](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cli-cmdinj-4MttWZPB) (CLI).


“This vulnerability is due to insufficient validation of a process argument on an affected product,” according to Cisco’s advisory. “An attacker could exploit this vulnerability by injecting commands during the execution of this process. A successful exploit could allow the attacker to execute arbitrary commands on the underlying operating system with the privileges of the management framework process, which are commonly root privileges.”


***Password******Reset:*** [**On-Demand Event**](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)***:*** *Fortify 2022 with a password-security strategy built for today’s threats. This* [*Threatpost Security Roundtable*](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)*, built for infosec professionals, centers on enterprise credential management, the new password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken.* [**Register & stream this FREE session today**](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/) *– sponsored by Specops Software.*





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Modbus]] [[Staros]] [[Confd]] [[Cvss]] [[“this]] [[“an]] [[ThreatPost]]
#### CVE's
[[CVE-2022-20649]] [[CVE-2022-20685]] [[CVE-2022-20655]]

