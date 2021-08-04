# Cisco fixes critical, high severity pre-auth flaws in VPN routers
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/cisco-fixes-critical-high-severity-pre-auth-flaws-in-vpn-routers/)
+ Date: August 4, 2021
+ Author: Sergiu Gatlan


## Article:
![Cisco fixes critical, high severity pre-auth flaws in VPN routers](https://www.bleepstatic.com/content/hl-images/2021/05/13/Cisco_headpic.jpg)


Cisco has addressed pre-auth security vulnerabilities impacting multiple Small Business VPN routers and allowing remote attackers to trigger a denial of service condition or execute commands and arbitrary code on vulnerable devices.


The two security flaws tracked as CVE-2021-1609 (rated 9.8/10) and CVE-2021-1602 (8.2/10) were found in the web-based management interfaces and exist due to improperly validated HTTP requests and insufficient user input validation, respectively.


[CVE-2021-1609](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-rv340-cmdinj-rcedos-pY8J3qfy) impacts RV340, RV340W, RV345, and RV345P Dual WAN Gigabit VPN routers, while [CVE-2021-1602](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-rv-code-execution-9UVJr7k4) affects RV160, RV160W, RV260, RV260P, and RV260W VPN routers.


Both bugs are exploitable remotely without requiring authentication as part of low complexity attacks that don't require user interaction.


Attackers could exploit the vulnerabilities by sending maliciously crafted HTTP requests to the affected routers' web-based management interfaces.


Remote management disabled on all impacted routers
--------------------------------------------------


Luckily, as the company explains, the remote management feature is disabled by default on all affected VPN router models.


"The web-based management interface for these devices is available through local LAN connections by default and cannot be disabled there," Cisco says.


"The interface can also be made available through the WAN interface by enabling the remote management feature. By default, the remote management feature is disabled on affected devices."


To find out if remote management is enabled on your devices, you have to open the router's web-based management interface via a local LAN connection and check if the Basic Settings > Remote Management option is toggled on.


Cisco has released software updates to address these vulnerabilities and says no workarounds are available to remove the attack vectors.


To download the patched firmware from Cisco's Software Center, you must click Browse All on Cisco.com and navigate to *Downloads Home > Routers > Small Business Routers > Small Business RV Series Routers*.


No in the wild exploitation
---------------------------


While Cisco says that its "Product Security Incident Response Team (PSIRT) is not aware of any public announcements or malicious use" of the two security flaws, similar router vulnerabilities have been targeted in the past by attackers in the wild.


In August 2020, Cisco [warned of actively exploited zero-day bugs](https://www.bleepingcomputer.com/news/security/cisco-warns-of-actively-exploited-bugs-in-carrier-grade-routers/) (CVE-2020-3566 and CVE-2020-3569) in carrier-grade IOS XR routers with multicast routing enabled. The company [patched the zero-days](https://www.bleepingcomputer.com/news/security/cisco-fixes-actively-exploited-bugs-in-carrier-grade-routers/) during late September 2020, one month after the initial warning.


One month later, in October 2020, Cisco again warned of attacks actively targeting a separate high severity vulnerability (CVE-2020-3118) impacting the IOS XR Network OS deployed on the same router models.


The same day, the US National Security Agency (NSA) also included CVE-2020-3118 among [25 security vulnerabilities targeted or exploited by Chinese state-sponsored threat actors](https://www.bleepingcomputer.com/news/security/nsa-top-25-vulnerabilities-actively-abused-by-chinese-hackers/).


In July 2020, Cisco [fixed another actively exploited ASA/FTD firewall bug](https://www.bleepingcomputer.com/news/security/cisco-patches-asa-ftd-firewall-flaw-actively-exploited-by-hackers/) and a pre-auth critical remote code execution (RCE) flaw [that could lead to full device takeover](https://www.bleepingcomputer.com/news/security/cisco-fixes-critical-pre-auth-flaws-allowing-router-takeover/) on vulnerable devices.




#### Tags:
[[VPN]] [[web-based]] [[Bleeping Computer]]
