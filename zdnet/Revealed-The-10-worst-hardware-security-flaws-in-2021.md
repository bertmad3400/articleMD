# Revealed: The 10 worst hardware security flaws in 2021
### Here are the hardware security flaws that could cause you big problems if you don't take care.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/revealed-the-10-worst-hardware-security-flaws-in-2021/)
+ Date: November 3, 2021
+ Author: Liam Tung


## Article:
Unknown

MITRE, which publishes a list of top software vulnerabilities in conjunction with US Department of Homeland Security's Cybersecurity and Infrastructure Security Agency (CISA), has now published a list of the most important hardware weaknesses, too.

MITRE publishes the the Common Weakness Enumeration (CWE) for software flaws, but this year has run a survey to create its first ever equivalent list for hardware flaws. 


The 2021 Hardware List aims to boost awareness of common hardware flaws and to prevent hardware security issues by educating designers and programmers on how to eliminate important mistakes early in the product development lifecycle.

**SEE:**[**Gartner releases its 2021 emerging tech hype cycle: Here's what's in and headed out**](https://www.zdnet.com/article/gartner-releases-its-2021-emerging-tech-hype-cycle-heres-whats-in-and-headed-out/#link=%7B%22role%22:%22standard%22,%22href%22:%22https://www.zdnet.com/article/gartner-releases-its-2021-emerging-tech-hype-cycle-heres-whats-in-and-headed-out/%22,%22target%22:%22_blank%22,%22absolute%22:%22%22,%22linkText%22:%22Gartner%20releases%20its%202021%20emerging%20tech%20hype%20cycle:%20Here's%20what's%20in%20and%20headed%20out%22%7D)

"Security analysts and test engineers can use the list in preparing plans for security testing and evaluation. Hardware consumers could use the list to help them to ask for more secure hardware products from their suppliers. Finally, managers and CIOs can use the list as a measuring stick of progress in their efforts to secure their hardware and ascertain where to direct resources to develop security tools or automation processes that mitigate a wide class of vulnerabilities by eliminating the underling root cause," [MITRE said.](https://cwe.mitre.org/scoring/lists/2021_CWE_MIHW.html) 

The list was determined by a survey of the CWE Team and members of the hardware special interest group.

The list, which isn't in any particular order, includes bugs that affect a range of devices including smartphones, Wi-Fi routers, PC chips, and cryptographic protocols for protecting secrets in hardware, flaws in protected memory areas, [Rowhammer-style bit-flipping bugs](https://www.zdnet.com/article/rambleed-rowhammer-attack-can-now-steal-data-not-just-alter-it/), and firmware update failures. 






The hardware weaknesses list is meant to serve as "authoritative guidance for mitigating and avoiding them" and is a companion to its annual 25 most dangerous software weaknesses list.

One submitted by Intel engineers, CWE-1231, regards "improper prevention of lock bit modification" that can be introduced during the design of integrated circuits. 

**SEE:**[**Cloud security in 2021: A business guide to essential tools and best practices**](https://www.zdnet.com/article/cloud-security-in-2021-a-business-guide-to-essential-tools-and-best-practices/)

"In integrated circuits and hardware intellectual property (IP) cores, device configuration controls are commonly programmed after a device power reset by a trusted firmware or software module (e.g., BIOS/bootloader) and then locked from any further modification," [MITRE notes](https://cwe.mitre.org/data/definitions/1231.html). 

"This behavior is commonly implemented using a trusted lock bit. When set, the lock bit disables writes to a protected set of registers or address regions. Design or coding errors in the implementation of the lock bit protection feature may allow the lock bit to be modified or cleared by software after it has been set. Attackers might be able to unlock the system and features that the bit is intended to protect." 

The entries also include past examples of the types of flaws, [such as CVE-2017-6283](https://nvidia.custhelp.com/app/answers/detail/a_id/4631/~/security-bulletin:-nvidia-shield-tv-security-updates-for-multiple), that affected the NVIDIA Security Engine. It contained a "vulnerability in the RSA function where the keyslot read/write lock permissions are cleared on a chip reset, which may lead to information disclosure."



| [CWE-1189](https://cwe.mitre.org/data/definitions/1189.html) | Improper Isolation of Shared Resources on System-on-a-Chip (SoC) |
| [CWE-1191](https://cwe.mitre.org/data/definitions/1191.html) | On-Chip Debug and Test Interface With Improper Access Control |
| [CWE-1231](https://cwe.mitre.org/data/definitions/1231.html) | Improper Prevention of Lock Bit Modification |
| [CWE-1233](https://cwe.mitre.org/data/definitions/1233.html) | Security-Sensitive Hardware Controls with Missing Lock Bit Protection |
| [CWE-1240](https://cwe.mitre.org/data/definitions/1240.html) | Use of a Cryptographic Primitive with a Risky Implementation |
| [CWE-1244](https://cwe.mitre.org/data/definitions/1244.html) | Internal Asset Exposed to Unsafe Debug Access Level or State |
| [CWE-1256](https://cwe.mitre.org/data/definitions/1256.html) | Improper Restriction of Software Interfaces to Hardware Features |
| [CWE-1260](https://cwe.mitre.org/data/definitions/1260.html) | Improper Handling of Overlap Between Protected Memory Ranges |
| [CWE-1272](https://cwe.mitre.org/data/definitions/1272.html) | Sensitive Information Uncleared Before Debug/Power State Transition |
| [CWE-1274](https://cwe.mitre.org/data/definitions/1274.html) | Improper Access Control for Volatile Memory Containing Boot Code |
| [CWE-1277](https://cwe.mitre.org/data/definitions/1277.html) | Firmware Not Updateable |
| [CWE-1300](https://cwe.mitre.org/data/definitions/1300.html) | Improper Protection of Physical Side Channels |





#### Tags:
[[]] [[ZDNet]]
