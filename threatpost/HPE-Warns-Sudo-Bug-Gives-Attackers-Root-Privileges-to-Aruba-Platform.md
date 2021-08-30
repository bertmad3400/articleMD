# HPE Warns Sudo Bug Gives Attackers Root Privileges to Aruba Platform
### HPE joins Apple in warning customers of a high-severity Sudo vulnerability. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169038)
+ Date: August 30, 2021  5:46 pm
+ Author: Tom Spring


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/05/03132821/HPE-corp-logo.jpg)
Hewlett Packard Enterprise (HPE) is warning a [vulnerability in Sudo](https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=hpesbnw04188en_us), an open-source program used within its Aruba AirWave management platform, could allow any unprivileged and unauthenticated local user to gain root privileges on a vulnerable host.


Rated high in severity, HPE warns the Sudo flaw could be part of a “chained attack” where an “attacker has achieved a foothold with lower privileges via another vulnerability and then uses this to escalate privileges,” according to a recent HPE security bulletin.


The Aruba AirWave management platform is HPE’s real-time monitoring and security alert system for wired and wireless infrastructures. The Sudo bug ([CVE-2021-3156](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3156)) was [reported in January](https://threatpost.com/sudo-bug-root-access-linux-2/163395/) by [Qualys](https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txthttps:/www.helpnetsecurity.com/tag/qualys/) researchers and is believed to impact millions of endpoint devices and systems.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Sudo is a program used by other platforms that “allows a system administrator to delegate authority to give certain users (or groups of users) the ability to run some (or all) commands as root or another user,” according to the [Sudo license](https://www.sudo.ws/).


**Sudo Returns**
----------------


At the time the Sudo bug was found, Mehul Revankar, Qualys’ VP of Product Management and Engineering, described the Sudo flaw in a research note as, “perhaps the most significant Sudo vulnerability in recent memory (both in terms of scope and impact) and has been hiding in plain sight for nearly 10 years.”


For HPE’s part, the company publicly disclosed the flaw last week and said it affected the AirWave management platform prior to version 8.2.13.0 – release on June 18, 2021.


“A vulnerability in the command line parameter parsing code of Sudo could allow an attacker with access to Sudo to execute commands or binaries with root privileges,” according to the security bulletin.


Qualys researchers named the Sudo vulnerability “Baron Samedit” and said the bug was introduced into the Sudo code in July 2011. The bug was first only believed to impact Linux and BSD operating systems, including versions of Linux ranging from [Ubuntu](https://threatpost.com/billions-of-devices-impacted-secure-boot-bypass/157843/) 20.04 (Sudo 1.8.31), Debian 10 (Sudo 1.8.27) and Fedora 33 (Sudo 1.9.2). Since then, additional vendors have come forward with security warnings.


HPE may be the latest to report a Sudo dependency in its code, but it likely won’t be the last.


But in February, an Apple security bulletin warned that macOS (macOS Big Sur 11.2, macOS Catalina 10.15.7, macOS Mojave 10.14.6) contained the Sudo flaw inside an unspecified app. The news was followed by Apple’s release of a Sudo patch (Sudo version 1.9.5p2) to [mitigate the issue](https://support.apple.com/en-us/HT212177).


**HPE Offers Mitigation Against Sudo**
--------------------------------------


In the context of Aruba AirWave management platform, according to researchers, the bug could be used to carry out privilege escalation attacks. “By triggering a ‘heap overflow’ in the app, it becomes possible to change a user’s low-privilege access to that of a root-level user. This is possible either by planting malware on a device or carrying out a brute force attack on a low-privilege Sudo account,” researchers wrote.


The Sudo bug is a heap-based buffer overflow, which lets any local user trick Sudo into running in “shell” mode. When [Sudo is running in shell mode](https://www.sudo.ws/alerts/unescape_overflow.html), researchers explain, “it escapes special characters in the command’s arguments with a backslash.” Then, a policy plug-in removes any escape characters before deciding on the Sudo user’s permissions.”


HPE says to mitigate the issue users should upgrade to AirWave management platform to 8.2.13.0 and above. Sudo also [released a patch earlier this year](https://www.sudo.ws/). A technical workaround also is available for HPE AirWave customers:


“To minimize the likelihood of an attacker exploiting these vulnerabilities, Aruba recommends that the CLI and web-based  management interfaces for AirWave be restricted to a dedicated  layer 2 segment/VLAN and/or controlled by firewall policies at  layer 3 and above,” wrote HPE.




#### Tags:
[[Sudo]] [[HPE]] [[Aruba]] [[(Sudo]] [[macOS]] [[ThreatPost]]
