# Ransomware gang uses PrintNightmare to breach Windows servers
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/ransomware-gang-uses-printnightmare-to-breach-windows-servers/)
+ Date: August 12, 2021
+ Author: Sergiu Gatlan


## Article:
![Ransomware gang uses PrintNightmare to breach Windows servers](https://www.bleepstatic.com/content/hl-images/2021/05/17/Windows.jpg)


Ransomware operators have added PrintNightmare exploits to their arsenal and are targeting Windows servers to deploy Magniber ransomware payloads.


[PrintNightmare](https://www.bleepingcomputer.com/tag/printnightmare/) is a class of security vulnerabilities (tracked as [CVE-2021-1675](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-1675), [CVE-2021-34527](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527), and [CVE-2021-36958](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-another-windows-print-spooler-zero-day-bug/)) impacting the Windows Print Spooler service, Windows print drivers, and the Windows Point and Print feature.



Microsoft has released security updates to address CVE-2021-1675 and CVE-2021-34527 in [June](https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2021-patch-tuesday-fixes-6-exploited-zero-days-50-flaws/), [July](https://www.bleepingcomputer.com/news/security/microsoft-pushes-emergency-update-for-windows-printnightmare-zero-day/), and [August](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-print-spooler-printnightmare-vulnerability/).


The company has also published a security advisory on Wednesday providing a [workaround for CVE-2021-36958](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-another-windows-print-spooler-zero-day-bug/) (a zero-day bug allowing privilege escalation, with no patch available).


Threat actors can use these security flaws in local privilege escalation (LPE) or distribute malware as Windows domain admins via remote code execution (RCE) with SYSTEM privileges.


Ransomware now using PrintNightmare exploits
--------------------------------------------


And, as Crowdstrike researchers discovered last month, the Magniber ransomware gang is now using PrintNightmare exploits for these exact purposes in attacks against South Korean victims.


"On July 13, CrowdStrike successfully detected and prevented attempts at exploiting the PrintNightmare vulnerability, protecting customers before any encryption takes place," [said Liviu Arsene](https://www.crowdstrike.com/blog/magniber-ransomware-caught-using-printnightmare-vulnerability/), Crowdstrike's Director of Threat Research and Reporting.


After compromising servers unpatched against PrintNightmare, Magniber drops an obfuscated DLL loader, which gets first injected into a process and later unpacked to perform local file traversal and encrypt files on the compromised device.


In early February 2021, Crowdstrike observed Magniber being delivered via Magnitude EK onto South Korean devices running Internet Explorer unpatched against the [CVE-2020-0968](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-0968) vulnerability.


Magniber ransomware has been [active since October 2017](https://www.bleepingcomputer.com/news/security/goodbye-cerber-hello-magniber-ransomware/), when it was being deployed through malvertising using the Magnitude Exploit Kit (EK) as the successor of [Cerber ransomware](https://www.bleepingcomputer.com/news/security/the-cerber-ransomware-not-only-encrypts-your-data-but-also-speaks-to-you/).


While it initially focused on South Korean victims, the Magniber gang soon [expanded its operations worldwide](https://www.bleepingcomputer.com/news/security/magniber-ransomware-expands-from-south-korea-to-target-other-asian-countries/), switching targets to other countries, including China, Taiwan, Hong Kong, Singapore, Malaysia, and more.


More threat groups expected to add PrintNightmare to their arsenals
-------------------------------------------------------------------


At the moment we only have evidence that the Magniber ransomware gang is using PrintNightmware exploits in the wild to target potential victims.


However, other attackers (including ransomware groups) will likely join in (if they haven't already), seeing that there are other reports of in-the-wild PrintNightmare exploitation [[1](https://twitter.com/BushidoToken/status/1422492498241392647), [2](https://twitter.com/securitydoggo/status/1422241229392203777), [3](https://twitter.com/John_Fokker/status/1425749521569624065)] have surfaced since the vulnerability was reported and [proof-of-concept exploits were leaked](https://www.bleepingcomputer.com/news/security/public-windows-printnightmare-0-day-exploit-allows-domain-takeover/).


"CrowdStrike estimates that the PrintNightmare vulnerability coupled with the deployment of ransomware will likely continue to be exploited by other threat actors," Arsene concluded.


To defend against attacks that might target your network, you are advised to apply any available patches as soon as possible and implement workarounds provided by Microsoft to remove the attack vector if a security update is not yet available.


On July 13, CISA issued an emergency directive [ordering federal agencies](https://www.bleepingcomputer.com/news/security/cisa-orders-federal-agencies-to-patch-windows-printnightmare-bug/) to mitigate the actively exploited [PrintNightmare](https://www.bleepingcomputer.com/news/security/microsoft-printnightmare-security-updates-work-start-patching/) vulnerability on their networks.


The cybersecurity agency also published a [PrintNightmare alert](https://www.bleepingcomputer.com/news/security/cisa-disable-windows-print-spooler-on-servers-not-used-for-printing/) on July 1st, encouraging security professionals to disable the Windows Print Spooler service on all systems not used for printing.




#### Tags:
[[PrintNightmare]] [[Magniber]] [[Windows]] [[ransomware]] [[Crowdstrike]] [[Bleeping Computer]]
