# Cisco: Firewall manager RCE bug is a zero-day, patch incoming
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/cisco-firewall-manager-rce-bug-is-a-zero-day-patch-incoming/)
+ Date: August 6, 2021
+ Author: Sergiu Gatlan


## Article:
![Cisco: Firewall manager RCE bug is a zero-day, patch incoming](https://www.bleepstatic.com/content/hl-images/2021/05/13/Cisco.jpg)


In a Thursday security advisory update, Cisco revealed that a remote code execution (RCE) vulnerability in the Adaptive Security Device Manager (ADSM) Launcher disclosed last month is a zero-day bug that has yet to receive a security update.


[Cisco ADSM](https://www.cisco.com/c/en/us/products/security/adaptive-security-device-manager/index.html) is a firewall appliance manager that provides a web interface for managing Cisco Adaptive Security Appliance (ASA) firewalls and AnyConnect Secure Mobility clients.


"At the time of publication, Cisco planned to fix this vulnerability in Cisco ASDM," the company says in the [updated advisory](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asdm-rce-gqjShXW).


"Cisco has not released software updates that address this vulnerability. There are no workarounds that address this vulnerability."


In a previous update, the company also tweaked the list of affected ADSM software versions, from releases '9.16.1 and earlier'—as listed in the initial advisory—to '7.16(1.150) and earlier.'


RCE bug exploitable via MiTM attack
-----------------------------------


The zero-day bug, tracked as [CVE-2021-1585](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asdm-rce-gqjShXW), is caused by improper signature verification for code exchanged between the ASDM and the Launcher.


Successful exploitation could enable an unauthenticated attacker to remotely execute arbitrary code on a target's operating system with the privileges assigned to the ASDM Launcher.


"An attacker could exploit this vulnerability by leveraging a man-in-the-middle position on the network to intercept the traffic between the Launcher and the ASDM and then inject arbitrary code," as Cisco [explains](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asdm-rce-gqjShXW) in the updated advisory.


"A successful exploit may require the attacker to perform a social engineering attack to persuade the user to initiate communication from the Launcher to the ASDM."


Additionally, the company says that its Product Security Incident Response Team (PSIRT) is not yet aware of proof-of-concept exploits for this zero-day or threat actors exploiting it in the wild.


Not the first rodeo
-------------------


In related news, three months ago, [Cisco fixed a six-month-old zero-day vulnerability](https://www.bleepingcomputer.com/news/security/cisco-fixes-6-month-old-anyconnect-vpn-zero-day-with-exploit-code/) (CVE-2020-3556) in the Cisco AnyConnect Secure Mobility Client VPN software, with publicly available proof-of-concept exploit code.


While Cisco PSIRT said that proof-of-concept exploit code was available publicly when the bug was disclosed, it also added that there was no evidence of in the wild abuse.


Cisco revealed the zero-day [in November 2020](https://www.bleepingcomputer.com/news/security/cisco-discloses-anyconnect-vpn-zero-day-exploit-code-available/) without security updates addressing the underlying weakness, but it did provide mitigation measures to decrease the attack surface.


Before addressing CVE-2020-3556 in May, no active exploitation was reported, likely because default VPN configurations were vulnerable to attacks and the bug could only be abused by authenticated local attackers.


However, last month, [attackers immediately pounced on a Cisco ASA bug](https://www.bleepingcomputer.com/news/security/cisco-asa-vulnerability-actively-exploited-after-exploit-released/) (partially patched in October 2020 and fully addressed in April 2021), immediately after Positive Technologies' Offensive Team published a PoC exploit.




#### Tags:
[[zero-day]] [[ASDM]] [[proof-of-concept]] [[Bleeping Computer]]
