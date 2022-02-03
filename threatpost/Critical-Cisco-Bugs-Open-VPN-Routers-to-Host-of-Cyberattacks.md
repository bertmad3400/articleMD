# Critical Cisco Bugs Open VPN Routers to Host of Cyberattacks
### The RV line of small-business routers contains 15 flaws that could enable RCE, corporate network access or DoS – and many have exploits circulating.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178199
+ Date: 2022-02-03T20:15:54+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2020/09/03125515/cisco-jabber.jpg)

Critical security vulnerabilities in Cisco’s Small Business RV Series routers could allow privilege escalation, remote code execution (RCE) with root privileges on the devices and more.


The RV series is a set of affordable VPN appliances that enable remote workers to connect to a company network. They come with built-in firewalls, advanced encryption and authentication features.


The critical bugs are part of 15 total vulnerabilities affecting the RV product line that Cisco disclosed this week. Some of the issues are exploitable on their own, while others must be chained together, the networking giant said – but they all could lead to a concerning cornucopia of bad outcomes.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


According to Cisco’s [Wednesday advisory](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-smb-mult-vuln-KA9PK6D), attackers could exploit the bugs (which variously affect the RV160, RV260, RV340 and RV345 appliances) to do the following:


* Execute arbitrary code
* Elevate privileges
* Execute arbitrary commands
* Bypass authentication and authorization protections
* Fetch and run unsigned software
* Cause denial of service (DoS)


Cisco also said that proof-of-concept exploits are available for “several of the vulnerabilities,” but the company didn’t offer details on any in-the-wild attacks.


Some of the flaws only affect the RV340/RF345 line of Dual WAN Gigabit VPN routers, noted where applicable below. These affect version 1.0.03.24 and earlier and are patched in version 1.0.03.26.


For the RV160 and RV260 series, Cisco noted that versions 1.0.01.05 and earlier are affected. January’s release of firmware version 1.0.01.07 addressed some of the issues, according to the release notes ([PDF](https://www.cisco.com/c/dam/en/us/td/docs/routers/csbr/RV260/Release_notes/RV16x_Rv26x_relnote_v1_0_01_07.pdf)), but Cisco’s advisory appears to indicate that a first fixed release is as yet forthcoming. Threatpost has reached out for clarification. In the meantime, no workarounds are available.


**Critical Cisco Bugs in RV Routers**
-------------------------------------


### **Remote Code Execution**


The most concerning critical vulnerability rates 10 out of 10 on the CVSS vulnerability-severity scale. It arises in the SSL VPN module of Cisco Small Business RV340, RV340W, RV345 and RV345P Dual WAN Gigabit VPN routers. It could allow unauthenticated RCE, according to the advisory. At worst, device takeover would allow unfettered access to the business network on the part of an attacker.


“This vulnerability is due to insufficient boundary checks when processing specific HTTP requests,” the advisory reads. “An attacker could exploit this vulnerability by sending malicious HTTP requests to the affected device that is acting as an SSL VPN Gateway. A successful exploit could allow the attacker to execute code with root privileges on the affected device.”


This one’s of note, researchers said, because it exists in a favorite cybercrime target.


“With the increase in usage of SSL VPNs over the last three years since the beginning of the pandemic, SSL VPNs are a favored attack vector for cybercriminals, as they recognize that organizations need to ensure access to internal resources for remote employees,” Satnam Narang, staff research engineer at Tenable, said via email.


### **Privilege-Escalation Vulnerabilities**


The flaws tracked as CVE-2022-20700, CVE-2022-20701 and CVE-2022-20702 meanwhile exist in the web-based management interface of Cisco Small Business RV Series Routers and could allow a remote attacker to elevate privileges to root.


CVE-2022-20700 and CVE-2022-20701 both rate critical, with CVSS scores of 10 and 9, respectively, whileCVE-2022-20702 is rated medium-severity with a CVSS score of 6.


“These vulnerabilities are due to insufficient authorization enforcement mechanisms,” according to the advisory. “An attacker could exploit these vulnerabilities by submitting specific commands to an affected device. A successful exploit could allow the attacker to elevate privileges to root and execute arbitrary commands on the affected system.”


### **Running Unsigned Software**


A critical bug tracked as CVE-2022-20703 (with a CVSS score of 9.3) is a vulnerability in the software image verification feature of the RV series that an unauthenticated, local adversary could exploit to install and boot a malicious software image or execute unsigned binaries.


“This vulnerability is due to improper verification of software images as they are installed on an affected device. An attacker could exploit this vulnerability by loading unsigned software on the device,” the advisory reads.


### **Critical Command-Injection Bugs**


Three bugs affecting the RV340, RV340W, RV345 and RV345P Dual WAN Gigabit VPN routers could allow an unauthenticated, remote attacker to inject and execute arbitrary commands on the underlying Linux operating system, Cisco warned.


The first, CVE-2022-20707, is critical and carries a CVSS rating of 10. CVE-2022-20708 and CVE-2022-20749 are both high-severity, with CVSS ratings of 7.3.


“These vulnerabilities are due to insufficient validation of user-supplied input. An attacker could exploit these vulnerabilities by sending malicious input to an affected device,” according to the advisory.


**Other Cisco Bugs in the RV Line**
-----------------------------------


Cisco also disclosed several high- and medium-severity vulnerabilities.


### **High-Severity Command Injection**


A vulnerability in the Open Plug and Play (PnP) module (CVE-2022-20706, CVSS score of 8.3) of the appliances could allow an unauthenticated, remote attacker to inject and execute arbitrary commands on the underlying Linux operating system, Cisco said.


“This vulnerability is due to insufficient validation of user-supplied input,” Cisco explained. “An attacker could exploit this vulnerability by sending malicious input to an affected device.”


One caveat: A successful exploit requires the attacker to be in a man-in-the-middle (MitM) position or have control of a device connected to the vulnerable router.


### **High-Severity Authentication-Bypass Bug**


A high-severity vulnerability in the session management of the web interface for the RV appliances (CVE-2022-20705, CVSS score of 5.3) could be exploited by an unauthenticated, remote attacker to bypass authentication.


“A successful exploit could allow the attacker to take actions within the web UI with privileges up to the level of the administrative user and launch further attacks, exploiting the other vulnerabilities described in this advisory,” according to Cisco. “The attacker could obtain partial administrative privileges and perform unauthorized actions.”


The bug is due to “weak entropy for session identifier generation functions,” which a cyberattacker could exploit by brute-forcing a current session identifier, then reusing it to take over an ongoing session. Alternatively, an adversary could craft a new, valid session identifier and bypass the authentication mechanism entirely.


### **High-Severity Arbitrary File Overwrite Bug**


The bug tracked as CVE-2022-20711 (with a CVSS score of 8.2) is found in the web interface of the RV340, RV340W, RV345 and RV345P Dual WAN Gigabit VPN routers. It  could allow an unauthenticated, remote attacker to overwrite certain files on an affected device.


“This vulnerability is due to insufficient input validation for specific components of the web UI,” Cisco explained. “An attacker could exploit this vulnerability by sending crafted HTTP requests to an affected device. A successful exploit could allow the attacker to overwrite existing files or exfiltrate confidential data by tampering with the files that are served by the web UI process.”


### **High-Severity RCE**


A vulnerability in the upload module of the RV devices (CVE-2022-20712) could allow RCE as a non-root user. It rates 7.3 on the CVSS scale.


“This vulnerability is due to insufficient boundary checks when processing specific HTTP requests,” according to Cisco. “An attacker could exploit this vulnerability by sending malicious HTTP requests to an affected device.”


### **Medium-Severity MitM Exploit for Server Communications**


The CVE-2022-20704 bug (medium-severity, with a CVSS score of 4.8) in the software-upgrade module of the RV series could allow an unauthenticated, remote attacker to view or alter information being shared between an affected device and specific Cisco servers (cloudsso.cisco.com and api.cisco.com).


It’s due to improper validation of the SSL server certificate that is received when establishing the server connections, according to the advisory.


“An attacker could exploit this vulnerability by using man-in-the-middle techniques to intercept the traffic between the affected device and the server, and then using a forged certificate to impersonate the server,” Cisco explained. “A successful exploit could allow the attacker to force the affected device to download arbitrary software images and launch further attacks, combining other vulnerabilities.”


### **Medium-Severity Arbitrary File Upload Vulnerability**


A vulnerability in the web-based management interface of Cisco RV340, RV340W, RV345 and RV345P Dual WAN Gigabit VPN Routers (CVE-2022-20709, with a CVSS rating of 5.3) could allow an unauthenticated, remote attacker to upload arbitrary files to an affected device.


“This vulnerability is due to insufficient authorization enforcement mechanisms in the context of file uploads,” according to Cisco. “An attacker could exploit this vulnerability by sending a crafted HTTP request to an affected device.”


### **Medium-Severity DoS Bug**


A vulnerability in the internal interprocess communication of the RV line (CVE-2022-20710, with a CVSS score of 5.3) could allow DoS attacks from an unauthenticated, remote attacker.


The issue specifically affects the log-in functionality of the web-based management interface for the appliances, which “erroneously handled exceptions during failed login attempts,” according to Cisco.


“An attacker could exploit this vulnerability by submitting a crafted HTTP packet to an affected device,” the advisory reads. “A successful exploit could allow the attacker to prevent users from logging in to the affected device. Successful exploitation of this vulnerability would not impact users who are already logged in.”


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


 


 


 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=route]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Cvss]] [[Rv]] [[Vpn]] [[“an]] [[Http]] [[“this]] [[Rv340]] [[Rv345]] [[Ssl]] [[Rv340w]] [[ThreatPost]]
#### ipv4-adresses
1.0.03.24 1.0.03.26 1.0.01.05 1.0.01.07
#### CVE's
[[CVE-2022-20700]] [[CVE-2022-20701]] [[CVE-2022-20702]] [[CVE-2022-20703]] [[CVE-2022-20707]] [[CVE-2022-20708]] [[CVE-2022-20749]] [[CVE-2022-20706]] [[CVE-2022-20705]] [[CVE-2022-20711]] [[CVE-2022-20712]] [[CVE-2022-20704]] [[CVE-2022-20709]] [[CVE-2022-20710]]

