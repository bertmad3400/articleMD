# HelloKitty ransomware is targeting vulnerable SonicWall devices
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/hellokitty-ransomware-is-targeting-vulnerable-sonicwall-devices/)
+ Date: July 17, 2021
+ Author: Sergiu Gatlan


## Article:
![HelloKitty ransomware is targeting vulnerable SonicWall devices](https://www.bleepstatic.com/content/hl-images/2021/04/29/Sonicwall.jpg)


CISA warns of threat actors targeting "a known, previously patched, vulnerability" found in SonicWall Secure Mobile Access (SMA) 100 series and Secure Remote Access (SRA) products with end-of-life firmware.


As the US federal agency also [adds](https://us-cert.cisa.gov/ncas/current-activity/2021/07/15/ransomware-risk-unpatched-eol-sonicwall-sra-and-sma-8x-products), the attackers can exploit this security vulnerability as part of a targeted ransomware attack.


This alert comes after SonicWall issued an "urgent security notice" and sent emails to warn customers of the "[imminent risk of a targeted ransomware attack](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-critical-ransomware-risk-to-eol-sma-100-vpn-appliances/)." 


Even though the company said the risk of ransomware attacks is imminent, Coveware CEO Bill Siegel [confirmed](https://twitter.com/billseagull/status/1415352903817117699) CISA's warning saying that the campaign is ongoing. 


CISA urges users and administrators to review the SonicWall [security notice](https://www.sonicwall.com/support/product-notification/urgent-security-notice-critical-risk-to-unpatched-end-of-life-sra-sma-8-x-remote-access-devices/210713105333210/) and upgrade their devices to the latest firmware or immediately disconnect all end-of-life appliances.




> 
> Upgrade to the newest SonicWall firmware and disconnect EOL SonicWall appliances ASAP. Failing to follow SonicWall guidance may lead to targeted ransomware attacks. Read more at <https://t.co/ji96tw5Md4> [#Cybersecurity](https://twitter.com/hashtag/Cybersecurity?src=hash&ref_src=twsrc%5Etfw) [#InfoSec](https://twitter.com/hashtag/InfoSec?src=hash&ref_src=twsrc%5Etfw) [#Ransomware](https://twitter.com/hashtag/Ransomware?src=hash&ref_src=twsrc%5Etfw)
> 
> 
> — US-CERT (@USCERT\_gov) [July 15, 2021](https://twitter.com/USCERT_gov/status/1415764861217353731?ref_src=twsrc%5Etfw)


HelloKitty ransomware: one of the groups behind these attacks
-------------------------------------------------------------


While CISA and SonicWall did not reveal the identity of the threat attackers behind these attacks, BleepingComputer was told by a source in the cybersecurity industry that HelloKitty has been exploiting the vulnerability for the past few weeks.


Cybersecurity firm CrowdStrike also confirmed to BleepingComputer that the ongoing attacks are attributed to multiple threat actors, including HelloKitty.


[HelloKity](https://www.bleepingcomputer.com/tag/hellokitty/) is a human-operated ransomware operation active since [November 2020](https://www.bleepingcomputer.com/forums/t/750580/hellokitty-ransomware-crypt-read-me-unlocktxt-support-topic/), mostly known for encrypting the systems of [CD Projekt Red](https://www.bleepingcomputer.com/news/security/cd-projekt-red-gaming-studio-hit-by-ransomware-attack/) and claiming to have stolen Cyberpunk 2077, Witcher 3, Gwent, and other games' source code.


Even though the bug abused to compromise unpatched and EOL SMA and SRA products was not disclosed in CISA's warning or SonicWall's notice, CrowdStrike security researcher Heather Smith told BleepingComputer yesterday that the targeted vulnerability is tracked as CVE-2019-7481.


"This exploitation targets a long-known vulnerability that was patched in newer versions of firmware released in early 2021," SonicWall said in an emailed statement.


However, CrowdStrike's Heather Smith and Hanno Heinrichs [said in a report](https://www.crowdstrike.com/blog/how-ecrime-groups-leverage-sonicwall-vulnerability-cve-2019-7481/) published last month that "CrowdStrike Services incident response teams identified eCrime actors leveraging an older SonicWall VPN vulnerability, CVE-2019-7481, that affects Secure Remote Access (SRA) 4600 devices."


SonicWall credited the two security with reporting the actively exploited security flaw in a [security advisory](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0017) issued yesterday.


According to a Coveware report, Babuk ransomware is also targeting SonicWall VPNs likely vulnerable to [CVE-2020-5135](https://nvd.nist.gov/vuln/detail/CVE-2020-5135) exploits. This vulnerability was patched in October 2020 but it is still "heavily abused by ransomware groups today" per Coveware.


Ransomware vs. SonicWall devices
--------------------------------


A threat group tracked by Mandiant as UNC2447 has also exploited the [CVE-2021-20016](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0001) zero-day bug in SonicWall SMA 100 Series VPN appliances to deploy a [new ransomware strain known as FiveHands](https://www.bleepingcomputer.com/news/security/new-ransomware-group-uses-sonicwall-zero-day-to-breach-networks/) (a DeathRansom variant just as HelloKitty).


Their attacks targeted multiple North American and European targets before SonicWall released patches in [late February 2021](https://www.bleepingcomputer.com/news/security/sonicwall-firewall-maker-hacked-using-zero-day-in-its-vpn-device/).


The same zero-day was also abused in January in attacks [targeting SonicWall's internal systems](https://www.bleepingcomputer.com/news/security/sonicwall-firewall-maker-hacked-using-zero-day-in-its-vpn-device/) and later [indiscriminately exploited in the wild](https://www.bleepingcomputer.com/news/security/sonicwall-sma-100-zero-day-exploit-actively-used-in-the-wild/).


Mandiant threat analysts discovered [three other zero-day vulnerabilities](https://www.bleepingcomputer.com/news/security/sonicwall-warns-customers-to-patch-3-zero-days-exploited-in-the-wild/) in SonicWall's on-premises and hosted Email Security (ES) products in March.


These three zero-days were also actively exploited by a group Mandiant tracks as UNC2682 to backdoor systems using BEHINDER web shells, allowing them to move laterally through victims' networks and access emails and files.


"The adversary leveraged these vulnerabilities, with intimate knowledge of the SonicWall application, to install a backdoor, access files and emails, and move laterally into the victim organization's network," the Mandiant researchers [said](https://www.fireeye.com/blog/threat-research/2021/04/zero-day-exploits-in-sonicwall-email-security-lead-to-compromise.html) at the time.




#### Tags:
[[SonicWall]] [[ransomware]] [[CISA]] [[HelloKitty]] [[CrowdStrike]] [[Mandiant]] [[SRA]] [[emails]] [[Coveware]] [[BleepingComputer]] [[Bleeping Computer]]
