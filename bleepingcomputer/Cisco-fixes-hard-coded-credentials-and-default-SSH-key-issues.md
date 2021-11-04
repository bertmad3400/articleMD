# Cisco fixes hard-coded credentials and default SSH key issues
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/cisco-fixes-hard-coded-credentials-and-default-ssh-key-issues/)
+ Date: November 4, 2021
+ Author: Sergiu Gatlan


## Article:
![Cisco fixes hard-coded credentials and default SSH key issues](https://www.bleepstatic.com/content/hl-images/2021/05/13/Cisco.jpg)


Cisco has released security updates to address critical security flaws allowing unauthenticated attackers to log in using hard-coded credentials or default SSH keys to take over unpatched devices.


CISA also [encouraged](https://us-cert.cisa.gov/ncas/current-activity/2021/11/04/cisco-releases-security-updates-multiple-products) users and administrators today to review Cisco's advisories and apply all the necessary updates to block attempts to take over impacted systems.


Catalyst PON Switch hard-coded credentials
------------------------------------------


The first of the two flaws patched on Wednesday (tracked as [CVE-2021-34795](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-catpon-multivulns-CE3DSYGr)) comes with a perfect 10/10 CVSS score and was found in the Cisco Catalyst Passive Optical Network (PON) Series Switches Optical Network Terminal (ONT).


"A vulnerability in the Telnet service of Cisco Catalyst PON Series Switches ONT could allow an unauthenticated, remote attacker to log in to the affected device by using a debugging account that has a default, static password," the company explains in an advisory published yesterday.


Luckily, this vulnerability can only be exploited by establishing a Telnet session to vulnerable devices and logging in with the hard-coded credential.


Since Telnet is not enabled by default on affected devices, this drastically limits the number of targets threat actors could attack.


The list of affected devices includes CGP-ONT-1P, CGP-ONT-4P, CGP-ONT-4PV, CGP-ONT-4PVC, and CGP-ONT-4TVCW Catalyst PON switches.


Cisco confirmed that CVE-2021-34795 does not impact Catalyst PON Switch CGP-OLT-8T and Catalyst PON Switch CGP-OLT-16T.


Default SSH keys in Cisco Policy Suite
--------------------------------------


The second critical security flaw patched yesterday is tracked as [CVE-2021-40119](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cps-static-key-JmS92hNv) and is caused by the re-use of static SSH keys across Cisco Policy Suite installations.


"A vulnerability in the key-based SSH authentication mechanism of Cisco Policy Suite could allow an unauthenticated, remote attacker to log in to an affected system as the root user," Cisco [explains](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cps-static-key-JmS92hNv).


"An attacker could exploit this vulnerability by extracting a key from a system under their control."


Cisco Policy Suite software releases 21.2.0 and later will automatically create new SSH keys during the install process but not during upgrades.


To generate new SSH keys and propagate them to all machines, you can use the steps detailed in the [Fixed Releases section of Cisco's advisory](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cps-static-key-JmS92hNv#:~:text=a%20free%20upgrade.-,Fixed%20Releases,-Customers%20are%20advised).


Cisco's Product Security Incident Response Team (PSIRT) said that there is no public proof-of-concept exploit code available online for these two vulnerabilities and added that it's not aware of any ongoing exploitation in the wild.




#### Tags:
[[SSH]] [[hard-coded]] [[Telnet]] [[Bleeping Computer]]
