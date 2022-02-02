# UEFI firmware vulnerabilities affect at least 25 computer vendors
### Researchers from firmware protection company Binarly have discovered critical vulnerabilities in the UEFI firmware from InsydeH2O used by multiple computer vendors such as Fujitsu, Intel, AMD, Lenovo, Dell, ASUS, HP, Siemens, Microsoft, and Acer.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/uefi-firmware-vulnerabilities-affect-at-least-25-computer-vendors/
+ Date: 2022-02-02T06:17:31-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/20/motherboard.jpg)

![23 flaws found in InsydeH2O UEFI firmware](https://www.bleepstatic.com/content/hl-images/2022/01/20/motherboard.jpg?rand=1507447089)


Researchers from firmware protection company Binarly have discovered critical vulnerabilities in the UEFI firmware from InsydeH2O used by multiple computer vendors such as Fujitsu, Intel, AMD, Lenovo, Dell, ASUS, HP, Siemens, Microsoft, and Acer.


UEFI (Unified Extensible Firmware Interface) software is an interface between a device’s firmware and the operating system, which handles the booting process, system diagnostics, and repair functions.


In total, [Binarly](https://binarly.io/) found 23 flaws in the InsydeH2O UEFI firmware, most of them in the software's System Management Mode (SMM) that provides system-wide functions such as power management and hardware control.


SMM’s privileges exceed those of the OS kernel, so any security issues in this space can have severe consequences for the vulnerable system.


More specifically, a local or remote attacker with administrative privileges exploiting SMM flaws could perform the following tasks:


* Invalidate many hardware security features (SecureBoot, Intel BootGuard)
* Install persistent software that cannot be easily erased
* Create backdoors and back communications channels to steal sensitive data


![Diagram of potential impact of post-exploitation](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/impact.png)**Diagram of potential impact of post-exploitation**  
*Source: [Binarly](https://binarly.io/)*
The 23 flaws are tracked as: CVE-2020-27339, CVE-2020-5953, CVE-2021-33625, CVE-2021-33626, CVE-2021-33627, CVE-2021-41837, CVE-2021-41838, CVE-2021-41839, CVE-2021-41840, CVE-2021-41841, CVE-2021-42059, CVE-2021-42060, CVE-2021-42113, CVE-2021-42554, CVE-2021-43323, CVE-2021-43522, CVE-2021-43615, CVE-2021-45969, CVE-2021-45970, CVE-2021-45971, CVE-2022-24030, CVE-2022-24031, CVE-2022-24069.


Of the above, [CVE-2021-45969](https://nvd.nist.gov/vuln/detail/CVE-2021-45969), [CVE-2021-45970](https://nvd.nist.gov/vuln/detail/CVE-2021-45970), and [CVE-2021-45971](https://nvd.nist.gov/vuln/detail/CVE-2021-45971) in the SMM are rated with critical severity, receiving a 9.8 score out of 10.


Ten of the discovered vulnerabilities could be exploited for privilege escalation, twelve memory corruption flaws in SMM, and one is a memory corruption vulnerability in InsydeH2O's Driver eXecution Environment (DXE).



![UEFI flaws affecting over 25 vendors](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/table.jpg)**UEFI flaws affecting over 25 vendors**  
*Source: [Binarly](https://binarly.io/)*
“The root cause of the problem was found in the reference code associated with InsydeH2O firmware framework code,” explains [Binarly’s disclosure report](https://www.binarly.io/posts/An_In_Depth_Look_at_the_23_High_Impact_Vulnerabilities/index.html).


“All of the aforementioned vendors (over 25) were using Insyde-based firmware SDK to develop their pieces of (UEFI) firmware,” the company notes. At the moment, the U.S. CERT Coordination Center [confirmed](https://kb.cert.org/vuls/id/796611) three vendors with products affected by the security issues found in the InsydeH2O firmware: Fujitsu, Insyde Software Corporation, and Intel (only CVE-2020-5953)


Addressing the problems
-----------------------


Insyde Software has [released firmware updates](https://www.insyde.com/press_news/press-releases/insyde%C2%AE-software-credits-binarly%E2%80%99s-ai-powered-firmware-threat-detection) to fix all identified security vulnerabilities and published [detailed bulletins](https://www.insyde.com/security-pledge) to assign severity and description for every flaw.


However, these security updates need to be adopted original equipment manufacturers (OEMs) and pushed to affected products.


The entire process will take a considerable amount of time for the security updates to reach end-users. It is unlikely that all issues will be addressed in all impacted products, though, because some devices have reached end-of-life and are no longer supported, while others may become obsolete before a patch is ready for them.


At the time of writing, only Insyde, Fujitsu, and Intel have confirmed themselves as affected by the flaws, while Rockwell, Supermicro, and Toshiba were confirmed as not impacted. The rest are investigating.


Binarly credits Fujitsu’s incident response team for its quick reaction when receiving the vulnerability reports, and its hands-on approach in helping to scope them correctly.


If you would like to scan your system for the existence of the above flaws, Binarly has published these FwHunt rules [on GitHub](https://github.com/binarly-io/FwHunt/tree/main/rules) to assist with detection.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Binarly]] [[Insydeh2o]] [[Uefi]] [[Fujitsu]] [[Smm]] [[Insyde]] [[Bleeping Computer]]
#### CVE's
[[CVE-2020-27339]] [[CVE-2020-5953]] [[CVE-2021-33625]] [[CVE-2021-33626]] [[CVE-2021-33627]] [[CVE-2021-41837]] [[CVE-2021-41838]] [[CVE-2021-41839]] [[CVE-2021-41840]] [[CVE-2021-41841]] [[CVE-2021-42059]] [[CVE-2021-42060]] [[CVE-2021-42113]] [[CVE-2021-42554]] [[CVE-2021-43323]] [[CVE-2021-43522]] [[CVE-2021-43615]] [[CVE-2021-45969]] [[CVE-2021-45970]] [[CVE-2021-45971]] [[CVE-2022-24030]] [[CVE-2022-24031]] [[CVE-2022-24069]]

