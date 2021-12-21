# FBI: Another Zoho ManageEngine Zero-Day Under Active Attack
### APT attackers are using a security vulnerability in ManageEngine Desktop Central to take over servers, deliver malware and establish network persistence.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177178
+ Date: 2021-12-21T14:42:02+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27112232/zero-day.jpeg)

Another Zoho ManageEngine zero-day vulnerability is under active attack from an APT group, this time looking to override legitimate functions of servers running ManageEngine Desktop Central and elevate privileges — with an ultimate goal of dropping malware onto organizations’ networks, the FBI has warned.


APT actors have been exploiting the bug, tracked as [CVE-2021-44515](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-44515), since at least late October, the feds revealed in an [FBI Flash alert](https://www.ic3.gov/Media/News/2021/211220.pdf) released last week. There is also evidence to support that it’s being used in an attack chain with two other Zoho bugs that researchers have observed under attack since September, according to the alert.


The latest vulnerability is an authentication-bypass vulnerability in ManageEngine Desktop Central that can allow an attacker to execute arbitrary code in the Desktop Central server, according to a Zoho [advisory](https://www.manageengine.com/products/desktop-central/cve-2021-44515-authentication-bypass-filter-configuration.html) that addressed the issue, published earlier this month.


Indeed, the feds said they observed APT actors doing exactly that. More specifically, researchers observed attackers “compromising Desktop Central servers, dropping a webshell that overrides a legitimate function of Desktop Central, downloading post-exploitation tools, enumerating domain users and groups, conducting network reconnaissance, attempting lateral movement and dumping credentials,” according to the Flash Alert.


Zoho has addressed the vulnerability and is urging organizations to update to the appropriate latest builds of ManageEngine Desktop Central due to “indications of exploitation,” the company said in its advisory.


Specifically, the company is advising enterprise customers who have builds10.1.2127.17 and below deployed to upgrade to build [10.1.2127.18](https://downloads.zohocorp.com/dnd/Desktop_Central/vSfr4V3f7NXjEJK/ManageEngine_Desktop_Central_10_1_0_SP-2127_18.ppm); and those using builds 10.1.2128.0 to 10.1.2137.2 to upgrade to build [10.1.2137.3](https://downloads.zohocorp.com/dnd/Desktop_Central/5fbkfifZFuh9mVx/ManageEngine_Desktop_Central_10_1_0_SP-2137_3.ppm).


**Zoho Under Fire**
-------------------


The bug is the third zero-day under active attack that researchers have discovered in the cloud platform company’s ManageEngine suite since September, spurring dire warnings from the FBI and researchers alike.


Though no one has yet conclusively identified the APT responsible, it’s likely the attacks are linked and those responsible are from China, previous evidence has shown.


Earlier this month, researchers at Palo Alto Networks Unit 42 [revealed](https://threatpost.com/threat-group-takes-aim-again-at-cloud-platform-provider-zoho/176732/) that state-backed adversaries were using vulnerable versions of ManageEngine ServiceDesk Plus to target a number of U.S. organizations between late October and November.


The attacks were related to a bug revealed in a Nov. 22 [security advisory](https://pitstop.manageengine.com/portal/en/community/topic/security-advisory-for-cve-2021-44077-unauthenticated-rce-vulnerability-in-servicedesk-plus-versions-up-to-11305-22-11-2021) by Zoho alerting customers of active exploitation against newly registered [CVE-2021-44077](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44077) found in Manage Engine ServiceDesk Plus. The vulnerability, which allows for unauthenticated remote code execution, impacts ServiceDesk Plus versions 11305 and below.


That news came on the heels of [warnings](https://threatpost.com/cisa-fbi-state-backed-apts-exploit-critical-zoho-bug/174768/) in September by the FBI, CISA and the U.S. Coast Guard Cyber Command (CGCYBER) that an unspecified APT was exploiting a then-zero-day vulnerability in Zoho ManageEngine’s password management solution called ADSelfService Plus.


Zoho issued [a fix](https://threatpost.com/zoho-password-manager-zero-day-attack/169303/) for the vulnerability, tracked as [CVE-2021-40539](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-40539), soon after; still, researchers observed attackers [exploiting it](https://threatpost.com/zoho-password-manager-flaw-godzilla-webshell/176063/) later in November in their continued assault on defense, energy and healthcare organizations.


Unit 42 researchers combined the two previously known active attack fronts against Zoho’s ManageEngine as the [“TitledTemple”](https://unit42.paloaltonetworks.com/tiltedtemple-manageengine-servicedesk-plus/) campaign, and said earlier this month that there is evidence to link the APT responsible to China, although it is not conclusive.


The latest Flash Alert released by the FBI also shows a correlation between earlier APT attacks on ManageEngine and AdSelfService Plus, with malicious samples of code observed in the latest exploitation “downloaded from likely compromised ManageEngine  

ADSelfService Plus servers,” according to the alert.


**Inside the Exploitation**
---------------------------


Those samples show initial exploitation of a Desktop Central API URL that allowed for an unauthenticated file upload of two different variants of webshells; the first variant was delivered using either the file name “emsaler.zip” or “eco-inflect.jar” in late October and mid-November, respectively; and a second variant using the file name “aaa.zip” in late November.


The webshell overrides the legitimate Desktop Central API servlet endpoint, “/fos/statuscheck,” and either filters inbound GET in the case of the second variant, or POST requests in the case of the first variant, to that URL path, according to the FBI. It then allows attackers to execute commands as the SYSTEM user with elevated privileges if the inbound requests pass the filter check.


The webshell allows attackers to conduct initial reconnaissance and domain enumeration, after which the actors use BITSAdmin to download a likely ShadowPad variant dropper with filename mscoree.dll, and a legitimate Microsoft AppLaunch binary, iop.exe, according to the FBI. Attackers then sideload the dropper through AppLaunch execution, creating a persistent service to execute the AppLaunch binary moving forward.


“Upon execution, the dropper creates an instance of svchost and injects code with RAT-like functionality that initiates a connection to a command and control server,” according to the FBI.


Threat actors conduct follow-on intrusion activity through the RAT, including attempted lateral movement to domain controllers and credential dumping techniques using Mimikatz, comsvcs.dll LSASS process memory dumping, and a WDigest downgrade attack with subsequent LSASS dumping through pwdump, researchers observed.


The FBI Flash Alert includes a detailed list of indicators of compromise so organizations using Zoho’s ManageEngine Desktop Central can check to see if they are at risk or have been a victim of attack.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=BITSAdmin]] [[action.malware.name=Conti]] [[action.malware.name=Mimikatz]] [[action.malware.name=Net]] [[action.malware.name=P.A.S. Webshell]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=pwdump]] [[action.malware.name=Reg]] [[action.malware.name=ShadowPad]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Healthcare]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Manageengine]] [[Zoho]] [[Webshell]] [[Servicedesk]] [[Applaunch]] [[ThreatPost]]
#### CVE's
[[CVE-2021-44515]] [[CVE-2021-44077]] [[CVE-2021-40539]]

