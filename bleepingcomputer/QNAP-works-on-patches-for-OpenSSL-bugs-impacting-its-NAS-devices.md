# QNAP works on patches for OpenSSL bugs impacting its NAS devices
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/qnap-works-on-patches-for-openssl-bugs-impacting-its-nas-devices/)
+ Date: August 30, 2021
+ Author: Sergiu Gatlan


## Article:
![QNAP works on patches for OpenSSL bugs impacting its NAS devices](https://www.bleepstatic.com/content/hl-images/2021/04/29/QNAP-headpic.jpg)


Network-attached storage (NAS) maker QNAP is investigating and working on security updates to address remote code execution (RCE) and denial-of-service (DoS) vulnerabilities patched by OpenSSL last week.


The security flaws tracked as [CVE-2021-3711](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3711) and [CVE-2021-3712](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3712), impact QNAP NAS device running QTS, QuTS hero, QuTScloud, and HBS 3 Hybrid Backup Sync (a backup and disaster recovery app), according to advisories [[1](https://www.qnap.com/en-us/security-advisory/QSA-21-40), [2](https://www.qnap.com/en-us/security-advisory/QSA-21-39)] published earlier today.


The [heap-based buffer overflow](https://cwe.mitre.org/data/definitions/122.html) in the SM2 cryptographic algorithm behind CVE-2021-3711 would likely lead to crashes but can also be abused by attackers for arbitrary code execution.


The CVE-2021-3712 vulnerability is caused by a [read buffer overrun](https://cwe.mitre.org/data/definitions/119.html) weakness while processing ASN.1 strings. Threat actors can exploit it to crash vulnerable apps or gain access to private memory contents such as private keys or similar sensitive info.


As QNAP explains, if successfully exploited, the vulnerabilities allow remote attackers to gain access to memory data without authorization, trigger denial-of-service (DoS) states, or run arbitrary code with the permissions of the user running the HBS 3 app.


While the OpenSSL development team published [OpenSSL 1.1.1l](https://www.openssl.org/news/vulnerabilities.html) to address the flaws a week ago, on August 24, QNAP did not provide an estimated time of arrival for incoming security updates.


However, the company did say that it's "thoroughly investigating the case" and "will release security updates and provide further information as soon as possible."


Synology customers also waiting for security updates
----------------------------------------------------


Last week, [Taiwan-based NAS maker Synology also said](https://www.bleepingcomputer.com/news/security/synology-multiple-products-impacted-by-openssl-rce-vulnerability/) multiple models in its NAS line (including DSM 7.0, DSM 6.2, DSM UC, SkyNAS, VS960HD, SRM 1.2, VPN Plus Server, and VPN Server) are affected by the same two security flaws.


"Multiple vulnerabilities allow remote attackers to conduct denial-of-service attack or execute arbitrary code via a susceptible version of Synology DiskStation Manager (DSM), Synology Router Manager (SRM), VPN Plus Server or VPN Server," the company explained.


Just as QNAP, Synology hasn't yet issued security updates to address these flaws, tagging them as "pending" and "ongoing."


Earlier this month, Palo Alto Networks' Unit 42 revealed that a newly discovered eCh0raix ransomware variant had added [support for encrypting both QNAP and Synology NAS devices](https://www.bleepingcomputer.com/news/security/ech0raix-ransomware-now-targets-both-qnap-and-synology-nas-devices/).


One month earlier, [QNAP fixed a critical HBS 3 security vulnerability](https://www.bleepingcomputer.com/news/security/qnap-fixes-critical-bug-in-nas-backup-disaster-recovery-app/) that enabled attackers to escalate privileges, read sensitive info without authorization, or execute commands remotely.




#### Tags:
[[QNAP]] [[Synology]] [[NAS]] [[VPN]] [[denial-of-service]] [[OpenSSL]] [[HBS]] [[DSM]] [[Bleeping Computer]]
