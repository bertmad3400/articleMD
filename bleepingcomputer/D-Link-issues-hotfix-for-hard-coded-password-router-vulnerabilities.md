# D-Link issues hotfix for hard-coded password router vulnerabilities
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/d-link-issues-hotfix-for-hard-coded-password-router-vulnerabilities/)
+ Date: July 16, 2021
+ Author: Sergiu Gatlan


## Article:
![D-Link issues hotfix for hard-coded password router vulnerabilities](https://www.bleepstatic.com/content/hl-images/2021/07/16/Dlink-router-fringe.jpg)


D-Link has issued a firmware hotfix to address multiple vulnerabilities in the [DIR-3040](https://us.dlink.com/en/products/dir-3040-smart-ac3000-high-power-wi-fi-tri-band-gigabit-router) AC3000-based wireless internet router.


Following successful exploitation, they can let attackers execute arbitrary code on unpatched routers, gain access to sensitive information or crash the routers after triggering a denial of service state.


The DIR-3040 security flaws discovered and [reported by Cisco Talos security researcher Dave McDaniel](https://blog.talosintelligence.com/2021/07/vuln-spotlight-d-link.html) include hardcoded passwords, command injection, and information disclosure bugs.




Authentication bypass via specially crafted requests
----------------------------------------------------


The [CVE-2021-21818](https://talosintelligence.com/vulnerability_reports/TALOS-2021-1283) and [CVE-2021-21820](https://talosintelligence.com/vulnerability_reports/TALOS-2021-1285) hard-coded password and credentials vulnerabilities [[1](https://cwe.mitre.org/data/definitions/259.html), [2](https://cwe.mitre.org/data/definitions/798.html)] exist in the router's Zebra IP Routing Manager and the Libcli Test Environment functionality.


Both of them allow threat actors targeting vulnerable D-Link DIR-3040 routers to bypass the authentication process configured by the software administrator.


Attackers can trigger them by sending a sequence of specially crafted network requests that lead either to denial of service and code execution on the targeted router, respectively.


[CVE-2021-21819](https://talosintelligence.com/vulnerability_reports/TALOS-2021-1284), a critical [OS command injection](https://cwe.mitre.org/data/definitions/78.html) vulnerability found in the router's Libcli Test Environment functionality, can also be abused by adversaries for code execution.


Additionally, it makes it possible to start a "hidden telnet service can be started without authentication by visiting *https:///start\_telnet"* and log into the Libcli test environment using a default password stored in unencrypted form on the router.


Vulnerabilities addressed in firmware hotfix
--------------------------------------------


D-Link has [resolved the bugs](https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10228) found in firmware version 1.13B03 and has issued a [firmware hotfix](https://support.dlink.com/resource/SECURITY_ADVISEMENTS/DIR-3040/REVA/DIR-3040_REVA_RELEASE_NOTES_v1.13B03_HOTFIX.pdf) for all affected customers on July 15, 2021, available for download [here](https://support.dlink.com/productinfo.aspx?m=DIR-3040-US).


The complete list of vulnerabilities addressed by D-Link with these hotfix includes:


* CVE-2021-21816 - Syslog information disclosure vulnerability
* CVE-2021-21817 - Zebra IP Routing Manager information disclosure vulnerability
* CVE-2021-21818 - Zebra IP Routing Manager hard-coded password vulnerability
* CVE-2021-21819 - Libcli command injection vulnerability
* CVE-2021-21820 - Libcli Test Environment hard-coded password vulnerability


D-Link says that the firmware hotfix released to address the bugs found by Cisco Talos is "a device beta software, beta firmware, or hot-fix release which is still undergoing final testing before its official release."


The table below lists the vulnerable router models and links to the updated firmware version containing the fix.





| **Model** | **Hardware Revision** | **Affected FW** | **Fixed FW** | **Recommendation** | **Last Updated** |
| DIR-3040 | All Ax Hardware Revisions | v1.13B03 & Below | [v1.13B03 Hotfix](https://support.dlink.com/resource/SECURITY_ADVISEMENTS/DIR-3040/REVA/DIR-3040_REVA_FIRMWARE_v1.13B03_HOTFIX.zip) | 1) Please Download Patch and Update Device


2) Full QA Firmware under test for automatic F/W update notification on D-Link Wifi mobile App

 | 06/09/2021 |


D-Link has patched other severe vulnerabilities in multiple router models in the past, including remote command injection bugs enabling attackers to [take complete control of vulnerable devices](https://www.bleepingcomputer.com/news/security/d-link-vpn-routers-get-patch-for-remote-command-injection-bugs/).


Previously, the company [fixed five critical vulnerabilities](https://www.bleepingcomputer.com/news/security/5-severe-d-link-router-vulnerabilities-disclosed-patch-now/) impacting some of its routers that made it possible for threat actors to steal admin credentials, bypass authentication, and execute arbitrary code in reflected Cross-Site Scripting (XSS) attacks.




#### Tags:
[[D-Link]] [[hotfix]] [[Libcli]] [[-]] [[DIR-3040]] [[hard-coded]] [[IP]] [[13B03]] [[Bleeping Computer]]
