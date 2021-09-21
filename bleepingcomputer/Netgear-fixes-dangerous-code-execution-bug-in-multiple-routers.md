# Netgear fixes dangerous code execution bug in multiple routers
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/netgear-fixes-dangerous-code-execution-bug-in-multiple-routers/)
+ Date: September 21, 2021
+ Author: Sergiu Gatlan


## Article:
![Computer networking vendor Netgear has fixed a high severity remote code execution (RCE) vulnerability found in the Circle Parental Control Service which runs with root perrmissions on many modern Small Offices/Home Offices (SOHO) Netgear routers. ](https://www.bleepstatic.com/content/hl-images/2021/08/06/Router.jpg)


Netgear has fixed a high severity remote code execution (RCE) vulnerability found in the Circle parental control service, which runs with root permissions on almost a dozen modern Small Offices/Home Offices (SOHO) Netgear routers.


While one would expect the attack vector exposed by [Circle](https://www.netgear.com/home/services/circle-smart-parental-controls/) security flaw (tracked as **CVE-2021-40847**) would be removed after the service is stopped, the Circle update daemon containing the bug is enabled by default and it can be exploited even if the service is disabled.


"The update process of the Circle Parental Control Service on various Netgear routers allows remote attackers with network access to gain RCE as root via a Man-in-the-Middle (MitM) attack," GRIMM security researcher Adam Nichols [explained](https://blog.grimm-co.com/2021/09/mama-always-told-me-not-to-trust.html).


"While the parental controls themselves are not enabled by default on the routers, the Circle update daemon, *circled*, is enabled by default."


Successfully exploiting this vulnerability requires the attackers to modify network traffic or intercept traffic while on the same network to gain RCE as root on the targeted router.


After gaining root access, the attacker can take complete control of the network traffic passing through the compromised router allowing for reading encrypted data exchanged with other devices, including those on the victim's corporate network.


Nichols also shared a potential chain of attack threat actors can use to breach an enterprise network after compromising one of its employee's Netgear routers:



* The attacker performs some initial reconnaissance to determine the ISP that employees of the target corporation use.


* The attacker compromises this ISP via some other mean (phishing, exploit, etc).


* From within the ISP, the attacker will be able to compromise any routers vulnerable to the Circle Parental Control Service vulnerability.


* From the compromised routers, the attacker can directly communicate with any corporate computers that are connected to the router. Then, using an exploit for a separate vulnerability, such as the recent PrintNightmare vulnerability, the attackers can compromise these computers.


* Once the attackers have compromised the corporate computers, they can pivot to the corporate network and exfiltrate corporate data or launch further attacks on the corporation.





How to update your router's firmware
------------------------------------


In a security advisory published on Monday, Netgear urged customers to download the latest firmware for their devices as soon as possible.


The complete list of Netgear routers vulnerable to CVE-2021-40847 exploits and patched firmware versions are listed below.





| **Vulnerable Netgear router** | **Patched version** |
| R6400v2 | Firmware version 1.0.4.120 |
| R6700 | Firmware version 1.0.2.26 |
| R6700v3 | Firmware version 1.0.4.120 |
| R6900 | Firmware version 1.0.2.26 |
| R6900P | Firmware version 3.3.142\_HOTFIX |
| R7000 | Firmware version 1.0.11.128 |
| R7000 | Firmware version 1.3.3.142\_HOTFIX |
| R7850 | Firmware version 1.0.5.76 |
| R7900 | Firmware version 1.0.4.46 |
| R8000 | Firmware version 1.0.4.76 |
| RS400 | Firmware version 1.5.1.80 |


To download and install the latest firmware for your Netgear device, you have to follow this procedure:


1. Visit [NETGEAR Support](https://www.netgear.com/support/).
2. Start typing your model number in the search box, then select your model from the drop-down menu as soon as it appears.  

If you do not see a drop-down menu, make sure that you entered your model number correctly, or select a product category to browse for your product model.
3. Click **Downloads**.
4. Under **Current Versions**, select the first download whose title begins with **Firmware Version**.
5. Click **Release Notes**.
6. Follow the instructions in the firmware release notes to download and install the new firmware.


If you cannot immediately install these firmware updates, you can also use Nichols' mitigation advice.


"To mitigate the risks to corporate environments posed by vulnerable SOHO routers, GRIMM recommends the provisioning and use of Virtual Private Network (VPN) clients," the researcher said.


"These clients should be configured to handle all traffic to ensure that an attacker cannot read or modify network traffic in a way that cannot be detected by the VPN endpoints."


Earlier this month, Netgear [fixed three severe security vulnerabilities dubbed Demon's Cries, Draconian Fear, and Seventh Inferno,](https://www.bleepingcomputer.com/news/security/netgear-fixes-severe-security-bugs-in-over-a-dozen-smart-switches/) impacting over a dozen of its smart switches, allowing threat actors to bypass authentication and take over unpatched devices.


In June, [Microsoft disclosed critical firmware vulnerabilities found in some Netgear routers](https://www.bleepingcomputer.com/news/security/microsoft-finds-netgear-router-bugs-enabling-corporate-breaches/) that can let attackers breach corporate networks after successful exploitation.


Last year, GRIMM and VNPT ISC security researchers also independently discovered a [zero-day bug in 79 Netgear router models](https://www.bleepingcomputer.com/news/security/79-netgear-router-models-risk-full-takeover-due-to-unpatched-bug/) allowing attackers to take control of vulnerable devices remotely.




#### Tags:
[[Netgear]] [[Nichols]] [[routers,]] [[Bleeping Computer]]
