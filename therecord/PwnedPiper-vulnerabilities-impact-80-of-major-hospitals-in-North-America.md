# PwnedPiper vulnerabilities impact 80% of major hospitals in North America
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/pwnedpiper-vulnerabilities-impact-80-of-major-hospitals-in-north-america/)
+ Date: August 2, 2021
+ Author: Catalin Cimpanu


## Article:
![PwnedPiper vulnerabilities impact 80% of major hospitals in North America](https://therecord.media/wp-content/uploads/2021/08/TransLogic-PTS.jpg)

Details have been published today about a collection of nine vulnerabilities known as **PwnedPiper** that impact common a type of medical equipment that’s installed in roughly 80% of all major hospitals in North America.


The [TransLogic Pneumatic Tube Systems (PTS)](https://www.swisslog-healthcare.com/en-us/products/transport-automation/translogic-pneumatic-tube-system), from Swisslog Healthcare, is a complex system that uses compressed air to move medical supplies (lab samples, medicine, blood products, etc.) using tubes that connect different departments inside large hospitals.


Installed in more than 3,000 hospitals, TransLogic systems effectively work as the blood vessels of modern hospitals as they allow the movement of sensitive medical material while keeping nurses free to provide patient care.


In [research](https://www.armis.com/pwnedpiper) published today, IoT security firm Armis said it discovered nine vulnerabilities in the Nexus Control Panel, the software that doctors and nurses use to control how medical material moves between hospital sections.


“These vulnerabilities can enable an unauthenticated attacker to take over Translogic PTS stations and essentially gain complete control over the PTS network of a target hospital,” the Armis team said today.


“This type of control could enable sophisticated and worrisome ransomware attacks, as well as allow attackers to leak sensitive hospital information,” the company added.


While the vulnerabilities can be exploited only if an attacker can connect or has a foothold on the hospital’s internal network, the PwndPiper issues were deemed extremely severe due to the prevalence of TransLogic devices across North America and how easy they could be weaponized to impact a hospital’s ability to provide proper medical care.


The issues —listed at the bottom of this article— were discovered in May and reported to Swisslog Healthcare, Armis said.


“A software update for all but one of the vulnerabilities has been developed, and specific mitigation strategies for the remaining vulnerability are available for customers,” a Swisslog Healthcare spokesperson told *The Record* in an email.


The company has released today version 7.2.5.7 of the Nexus Control Panel, along with a [blog post](https://www.swisslog-healthcare.com/en-us/company/news/2021/07/translogic-firmware-vulnerabilities.) with additional information for its customers. It also said the issue is primarily restricted to hospitals in North America, where most of these tube systems are installed, and that a patch for the ninth issue is expected later this year.


#### PwnedPiper vulnerabilities:


Details about the nine PwndPiper vulnerabilities are listed below. The Armis team is also scheduled to present its findings at the [Black Hat security conference](https://www.blackhat.com/us-21/briefings/schedule/index.html#a-hole-in-the-tube-uncovering-vulnerabilities-in-critical-infrastructure-of-healthcare-facilities-23546) this week, on Wednesday.


* **CVE-2021-37163 – Two hardcoded passwords accessible through the Telnet server:** Two vulnerabilities that are hardcoded passwords of user and root accounts, that can be accessed by login to the Telnet server on the Nexus Control Panel – that is enabled by default, and can not be turned off by native configuration of the system.
* **CVE-2021-37167 – User script run by root can be used for PE:** A privilege escalation vulnerability due to a user script being run by root. By using the hardcoded credentials of the user account, through the telnet server, the user can leverage this PE to gain root access.
* **CVE-2021-37161 – Underflow in udpRXThread; CVE-2021-37162 – Overflow in sccProcessMsg; CVE-2021-37165 – Overflow in hmiProcessMsg; CVE-2021-37164 – Off-by-three stack overflow in tcpTxThread:** Four memory corruption bugs in the implementation of the TLP20 protocol as used in the Nexus Control Panel, that can lead to remote-code-execution and denial-of-service. The TLP20 protocol is the control protocol for all Translogic stations.
* **CVE-2021-37166 – GUI socket Denial Of Service:** A denial-of-service vulnerability that is a result of the GUI process on the Nexus Control Panel binding a local service on all interfaces, allowing external connections to hijack it’s connection. This can allow an attacker to mimic the GUI commands versus the low-level process that controls the Nexus Control Panel, effectively accessing all GUI commands through the network.
* **CVE-2021-37160 – Unauthenticated, unencrypted, unsigned firmware upgrade:** A design flaw in which firmware upgrades on the Nexus Control Panel are unencrypted, unauthenticated and do not require any cryptographic signature. This is the most severe vulnerability, since it can allow an attacker to gain unauthenticated remote-code-execution by initiating a firmware update procedure while also maintaining persistence on the device. **[Unpatched]**








#### Tags:
[[Armis]] [[Panel,]] [[GUI]] [[TransLogic]] [[Swisslog]] [[hardcoded]] [[The Record]]
