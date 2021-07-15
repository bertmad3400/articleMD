# SonicWall Warns Firewall Hardware Bugs Under Attack
### SonicWall issued an urgent security alert warning customers that some of its current and legacy firewall appliances were under active attack. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167824)
+ Date: July 15, 2021  11:41 am
+ Author: Tom Spring


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/15105723/firewall_locks.jpg)
Security vendor SonicWall is warning customers to patch its enterprise firewall hardware to thwart an “imminent ransomware campaign using stolen credentials” that’s exploiting security holes in current models and those running legacy firmware.


Targeted are the company’s Secure Mobile Access (SMA) 100 series and Secure RIn emote Access (SRA) firewall appliances with both unpatched and end-of-life (EoL) 8.x firmware. In a Thursday security [notice](https://www.sonicwall.com/support/product-notification/urgent-security-notice-critical-risk-to-unpatched-end-of-life-sra-sma-8-x-remote-access-devices/210713105333210/), the company reported that researchers at Mandiant identified “threat actors actively targeting” three SMA 100 models and nine older SRA-series firewall products no longer supported by SonicWall.


“Organizations that fail to take appropriate actions to mitigate these vulnerabilities on their SRA and SMA 100 series products are at imminent risk of a targeted ransomware attack,” according to the security bulletin.



According reporting by The Record, the bugs and attacks are ongoing, tracing back to research published [in June by Crowdstrike](https://www.crowdstrike.com/blog/how-ecrime-groups-leverage-sonicwall-vulnerability-cve-2019-7481/). Researchers there asserted that Thursday’s SonicWall security notice is part of an ongoing exploitation of a vulnerability ([CVE-2019-7481](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-7481)), which they disclosed last month.


“CrowdStrike Services incident-response teams identified eCrime actors leveraging an older SonicWall VPN vulnerability, CVE-2019-7481, that affects Secure Remote Access (SRA) 4600 devices; the ability to leverage the vulnerability to affect SRA devices was previously undisclosed by SonicWall,” [it wrote](https://www.crowdstrike.com/blog/how-ecrime-groups-leverage-sonicwall-vulnerability-cve-2019-7481/).


**What SonicWall Patches and Mitigation Are Available?**
--------------------------------------------------------


Customers are urged to upgrade firmware immediately on those appliances still supported and to “disconnect immediately” legacy products, including SRA 4600/1600 (EoL 2019), SRA 4200/1200 (EoL 2016) and SSL-VPN 200/2000/400 (EoL 2013/2014).


“If your organization is using a legacy SRA appliance that is past end-of life status and cannot update to 9.x firmware, continued use may result in ransomware exploitation,” SonicWall said.


If legacy hardware is unable to be updated to 9.x or 10.x versions of SonicWall’s firmware, the company said a free version of its virtual SMA 500v is available for the next 108 days, with the freebie expiring October 31.


For SRA-series firewall products actively supported (210/410/500v), SonicWall advised customers running firmware 9.x to immediately update to 9.0.0.10-28sv or later. For those SRA customers running firmware 10.x, SonicWall said customers should immediately update to 10.2.0.7-34sv or later.


**Beyond the Firmware Flub**
----------------------------


In addition to the above urged mitigations, SonicWall highly recommended resetting the credentials used for its SMA and SRA products.


“As additional mitigation, you should also immediately reset all credentials associated with your SMA or SRA device, as well as any other devices or systems using the same credentials,” the company wrote.


SonicWall ranked sixth, with 3 percent market share, [in IDC’s rankings](https://infotechlead.com/security/palo-alto-networks-leads-security-appliance-market-beating-cisco-65587) for global security appliance hardware in Q4 of 2020, behind Huawei (4 percent). More specifically within the enterprise firewall market, SonicWall is considered a top player, ranking sixth according to JC Market Research.


Year-to-date, SonicWall has had a number of security fires to put out. In June, the company was forced to roll out [an updated fix for a flaw](https://threatpost.com/sonicwall-botches-critical-vpn-bug/167152/) affecting some 800,000 devices that could result in crashes or prevent users from connecting to corporate resources. In March, researchers reported a Mirai variant was targeting known [flaws in SonicWall devices](https://threatpost.com/sonicwall-breach-zero-days-in-remote-access/163290/). And in January, the security vendor investigated [zero-day vulnerabilities](https://threatpost.com/sonicwall-breach-zero-days-in-remote-access/163290/) in its SMA 100 series hardware.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[SonicWall]] [[SRA]] [[EoL]] [[ransomware]] [[ThreatPost]]
