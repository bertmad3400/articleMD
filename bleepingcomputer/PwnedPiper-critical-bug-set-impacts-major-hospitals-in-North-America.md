# PwnedPiper critical bug set impacts major hospitals in North America
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/pwnedpiper-critical-bug-set-impacts-major-hospitals-in-north-america/)
+ Date: August 2, 2021
+ Author: Ionut Ilascu


## Article:
![PwnedPiper critical bug set impacts major hospitals in North America](https://www.bleepstatic.com/content/hl-images/2021/08/02/PwnedPiper.jpg)


Pneumatic tube system (PTS) stations used in thousands of hospitals worldwide are vulnerable to a set of nine critical security issues collectively referred to as PwnedPiper.


PTS solutions are part of a hospital’s critical infrastructure as they are used to quickly deliver items like blood, tissue, lab samples, or medication to where they’re needed.



The flaws are in some of SwissLog’s TransLogic Pneumatic Tube System, an automated material transport solution for carrying medical items across longer distances in medium to large hospitals.


According to the maker, TransLogic PTS is present in more than 2,300 hospitals in North America and more than 3,000 units worldwide benefit from 24/7 customer support.


### Critical bug left unpatched


Research from [Armis](https://www.armis.com/), a connected device security company, revealed that an unauthenticated attacker could gain full control over some TransLogic PTS stations connected to the internet and then take over the entire PTS network of a target hospital.


Specifically, the company discovered nine critical vulnerabilities in the firmware powering the Nexus Control Panel for managing “all current models of Translogic PTS stations.”


While not all the issues could be exploited by a remote attacker, their severity level remains high, given a PTS' role in a hospital. 


Swisslog acknowledged the security issues and says that they impact the HMI-3 circuit board in Nexus Panels connected to the internet. The company notes in an advisory this weekend that the affected PTS products “are deployed primarily in hospitals within North America.”


Jennie MacQuade, Chief Privacy Officer for Swisslog Healthcare, says that the security issues are not present unless a mix of variables exists. 



"The potential for pneumatic tube stations (where the firmware is deployed) to be compromised is dependent on a bad actor who has access to the facility’s information technology network and who could cause additional damage by leveraging these exploits" - [Swisslog](https://www.swisslog-healthcare.com/en-us/company/news/2021/07/translogic-firmware-vulnerabilities)



When investigating the code powering the TransLogic PTS, Armis found the following vulnerabilities:


* CVE-2021-37163: two cases of always-active hardcoded passwords (user and root accounts), accessible over Telnet
* CVE-2021-37167: privilege escalation; using the hardcoded credentials, an attacker could run a user script with root privileges
* CVE-2021-37166: denial-of-service (DoS) caused by the GUI process of Nexus Control Panel binding a local service on all interfaces


Four memory corruption bugs in the control protocol (TLP20) of TransLogic stations that could lead to remote code execution or at least a denial–of-service (DoS) condition:


* CVE-2021-37161 - Underflow in udpRXThread
* CVE-2021-37162 - Overflow in sccProcessMsg
* CVE-2021-37165 - Overflow in hmiProcessMsg
* CVE-2021-37164 - Off-by-three stack overflow in tcpTxThread


And the most sever of all:


* CVE-2021-37160: unencrypted, unauthenticated firmware upgrades on the Nexus Control Panel. An attacker could leverage it to install malicious firmware on the system, essentially taking full control over it.


Armis reported the vulnerabilities on May 1 and worked with Swisslog to develop and test a viable patch (v7.2.5.7), as well as find mitigation steps for hospitals unable to apply the fix right away.


The current firmware update, however, addresses all but one vulnerability above, CVE-2021-37160, which is also the most severe of all. Swisslog will fix this, too, in a future firmware release.



### Defensive steps


For hospitals that cannot install the latest firmware update for TransLogic PTS Armis provides the following steps to defend against potential attacks:


* Block any use of Telnet (port 23) on the Translogic PTS stations (the Telnet service is not required in production)
* Deploy access control lists (ACLs), in which Translogic PTS components (stations, blowerd, diverters, etc.) are only allowed to communicate with the Translogic central server (SCC).
* Use the following Snort IDS rule to detect exploitation attempts of CVE-2021-37161, CVE-2021-37162 and CVE-2021-37165:


* Use the following Snort IDS rule to detect exploitation attempts of CVE-2021-37164:


Armis researchers Barak Hadad and Ben Seri explain the bugs in a [technical paper](https://info.armis.com/rs/645-PDC-047/images/Armis-PwnedPiper-WP.pdf) and how a local or remote attacker could exploit them. They will also [present the findings this week](https://www.blackhat.com/us-21/briefings/schedule/index.html#a-hole-in-the-tube-uncovering-vulnerabilities-in-critical-infrastructure-of-healthcare-facilities-23546) at the Black Hat security conference.




#### Tags:
[[TransLogic]] [[Swisslog]] [[Translogic]] [[Armis]] [[Telnet]] [[Bleeping Computer]]
