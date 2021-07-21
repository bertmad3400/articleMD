# New Sequoia bug gives you root access on most Linux systems
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/new-sequoia-bug-gives-you-root-access-on-most-linux-systems/)
+ Date: July 20, 2021
+ Author: Catalin Cimpanu


## Article:
![New Sequoia bug gives you root access on most Linux systems](https://therecord.media/wp-content/uploads/2021/07/Sequoia.png)

Security auditing firm Qualys said today it discovered a new vulnerability in the Linux operating system that can grant attackers root access on most distros, such as Ubuntu, Debian, and Fedora.


Named **Sequoia** and tracked as [CVE-2021-33909](https://www.qualys.com/2021/07/20/cve-2021-33909/sequoia-local-privilege-escalation-linux.txt), the new vulnerability was discovered in the Linux filesystem layer, the OS component that interacts and manages local files.


According to Qualys security researcher Bharat Jogi, by creating, mounting, and then deleting a very long directory structure that has a path length that exceeds 1GB, the Sequoia bug (an [out-of-bounds read](https://cwe.mitre.org/data/definitions/125.html)) occurs in the Linux OS filesystem component, allowing any low-privileged local account to run code with root privileges.


“We successfully exploited this uncontrolled out-of-bounds write, and obtained full root privileges on default installations of Ubuntu 20.04, Ubuntu 20.10, Ubuntu 21.04, Debian 11, and Fedora 34 Workstation,” Jogi said today.


“Other Linux distributions are likely vulnerable and probably exploitable.”





Patches to address this issue have been released today by several Linux distros after Qualys notified the Linux kernel team in early June.


The vulnerability cannot be used to remotely break into Linux distros, but once attackers have a foothold on any system, the Sequoia bug can be used to hijack the entire OS, making it an ideal second-stage payload.


Since the vulnerability impacts most Linux distros, it should be expected that the Sequoia bug would be integrated into exploit chains targeting Linux-powered devices such as servers, workstations, cloud infrastructure, IoT devices, and smartphones.


Something similar happened in 2017 after security researchers disclosed the [Dirty COW (CVE-2016-5195)](https://dirtycow.ninja/)privilege escalation bug, which saw widespread use after its disclosure.





#### Tags:
[[Linux]] [[distros]] [[Ubuntu]] [[Qualys]] [[The Record]]
