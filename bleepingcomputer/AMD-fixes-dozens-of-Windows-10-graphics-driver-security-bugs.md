# AMD fixes dozens of Windows 10 graphics driver security bugs
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/amd-fixes-dozens-of-windows-10-graphics-driver-security-bugs/)
+ Date: November 11, 2021
+ Author: Sergiu Gatlan


## Article:
![AMD fixes dozens of vulnerabilities in Windows 10 graphics driver](https://www.bleepstatic.com/content/hl-images/2021/11/11/AMD.jpg)


*Image: [Timothy Dykes](https://unsplash.com/@timothycdykes)*


AMD has fixed a long list of security vulnerabilities found in its graphics driver for Windows 10 devices, allowing attackers to execute arbitrary code and elevate privileges on vulnerable systems.


The potential impact and the flaws' severity vary, with AMD tagging more than a dozen bugs as high severity.


"In a comprehensive analysis of the AMD Escape calls, a potential set of weaknesses in several APIs was discovered, which could result in escalation of privilege, denial of service, information disclosure, KASLR bypass, or arbitrary write to kernel memory," AMD explained.


The security flaws were discovered by both independent security researchers Ori Nimron and driverThru\_BoB 9th, as well as Eran Shimony of CyberArk Labs and Lucas Bouillot, of the Apple Media Products RedTeam.


The complete list of patched bugs includes:


* Ori Nimron (@orinimron123) : CVE-2020-12892, CVE-2020-12893, CVE-2020-12894, CVE-2020-12895, CVE-2020-12897, CVE-2020-12898, CVE-2020-12899, CVE-2020-12900, CVE-2020-12901, CVE-2020-12902, CVE-2020-12903, CVE-2020-12904, CVE-2020-12905, CVE-2020-12963, CVE-2020-12964, CVE-2020-12980, CVE-2020-12981, CVE-2020-12982, CVE-2020-12983, CVE-2020-12986, CVE-2020-12987
* Eran Shimony of CyberArk Labs: CVE-2020-12892
* Lucas Bouillot, of the Apple Media Products RedTeam: CVE-2020-12929
* driverThru\_BoB 9th: CVE-2020-12960


A full list of vulnerabilities found in the AMD Graphics Driver for Windows 10 and their description is available in the [security advisory](https://www.amd.com/en/corporate/product-security/bulletin/amd-sb-1000) published this week.


An AMD spokesperson was not immediately available to provide additional details when contacted by BleepingComputer today


AMD EPYC server processor bug fixes
-----------------------------------


This week, AMD also patched medium and high severity security flaws impacting [the company's 1st/2nd/3rd Gen AMD EPYC server processors](https://www.amd.com/en/corporate/product-security/bulletin/amd-sb-1021) that could lead to arbitrary code execution, bypassing SPI ROM protections, loss of integrity, denial of service, information disclosure, and more.


"During security reviews in collaboration with Google, Microsoft, and Oracle, potential vulnerabilities in the AMD Platform Security Processor (PSP), AMD System Management Unit (SMU), AMD Secure Encrypted Virtualization (SEV) and other platform components were discovered and have been mitigated in AMD EPYC AGESA PI packages," AMD said.


The company also addressed an improper access control vulnerability (CVE-2021-26334) found by Michal Poslušný from ESET Research in the AMDPowerProfiler.sys driver of the AMD μProf tool.


AMD μProf is a performance analysis utility that can be used to inspect Windows, Linux, and FreeBSD applications.


Successful exploitation of this flaw would allow attackers without enough privileges to gain access to kernel model-specific registers, which leads to privilege escalation and ring-0 code execution that gives the attacker full control over the vulnerable system.


Windows 11 performance issues addressed in October
--------------------------------------------------


In early October, right after Windows 11 began rolling out, AMD has also [warned of significant performance hits on Windows 11-compatible AMD processors](https://www.bleepingcomputer.com/news/microsoft/amd-warns-of-up-to-15-percent-windows-11-performance-decrease/), including the latest Ryzen CPUs, when using some applications.


One of the compatibility issues led to increased measured and functional L3 cache latency which had a direct impact on the access time to the memory subsystem for some apps.


While for some of the affected apps the expected performance impact was between 3 to 5%, for eSports games AMD said that customers could see a performance decrease of 10-15% on Windows 11.


The AMD CPU issues were addressed two weeks later with the optional [KB5006746 cumulative update preview for Windows 11](https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5006746-update-fixes-gaming-performance-issues/) released on October 21.


"Addresses an L3 caching issue that might affect performance in some applications on devices that have AMD Ryzen processors after upgrading to Windows 11 (original release)," Microsoft explained in the release notes.




#### Tags:
[[AMD]] [[Windows]] [[EPYC]] [[Bleeping Computer]]
