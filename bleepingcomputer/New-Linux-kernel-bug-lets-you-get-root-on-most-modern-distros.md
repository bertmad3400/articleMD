# New Linux kernel bug lets you get root on most modern distros
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-linux-kernel-bug-lets-you-get-root-on-most-modern-distros/)
+ Date: July 20, 2021
+ Author: Sergiu Gatlan


## Article:
![New Linux kernel bug lets you get root on most modern distros](https://www.bleepstatic.com/content/hl-images/2021/03/11/Linux.jpg)


Unprivileged attackers can gain root privileges by exploiting a local privilege escalation (LPE) vulnerability in default configurations of the Linux Kernel's filesystem layer on vulnerable devices.


As discovered by Qualys researchers, the LPE security flaw tracked as CVE-2021-33909 ([dubbed **Sequoia**](https://blog.qualys.com/vulnerabilities-threat-research/2021/07/20/sequoia-a-local-privilege-escalation-vulnerability-in-linuxs-filesystem-layer-cve-2021-33909)) is present in the filesystem layer used to manage user data, a feature universally used by all major (Linux) operating systems.



According to Qualys' research, the vulnerability impacts all Linux kernel versions released since 2014.


Once successfully exploited on a vulnerable system, the attackers get full root privileges on default installations of many modern distributions.


"We successfully exploited this uncontrolled out-of-bounds write, and obtained full root privileges on default installations of Ubuntu 20.04, Ubuntu 20.10, Ubuntu 21.04, Debian 11, and Fedora 34 Workstation," the researchers [said](https://www.qualys.com/2021/07/20/cve-2021-33909/sequoia-local-privilege-escalation-linux.txt).


They also added that "other Linux distributions are certainly vulnerable, and probably exploitable."


Since the attack surface exposed by the Sequoia vulnerability reaches over a wide range of distros and releases, Linux users are urged to immediately apply patches released earlier today.



Qualys has also discovered and disclosed earlier today a stack exhaustion denial-of-service vulnerability tracked as [CVE-2021-33910](https://blog.qualys.com/vulnerabilities-threat-research/2021/07/20/cve-2021-33910-denial-of-service-stack-exhaustion-in-systemd-pid-1) in systemd exploitable by unprivileged attackers to trigger a kernel panic.


systemd is a software suite included with most Linux operating systems used to start all other system components after booting.


This security flaw was introduced in April 2015 and is present in all systemd versions released since then, except for those published earlier today to patch the bug.


Qualys also created and attached proof-of-concept exploits to the two blog posts, PoC exploits designed to showcase how potential attackers could successfully abuse these two vulnerabilities


Earlier this year, Qualys researchers also [found a Sudo vulnerability](https://www.bleepingcomputer.com/news/security/new-linux-sudo-flaw-lets-local-users-gain-root-privileges/) that can let local users gain root privileges on Unix-like operating systems without requiring authentication.




#### Tags:
[[Linux]] [[Qualys]] [[Ubuntu]] [[systemd]] [[Bleeping Computer]]
