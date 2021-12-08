# SonicWall ‘strongly urges’ customers to patch critical SMA 100 bugs
### SonicWall 'strongly urges' organizations using SMA 100 series appliances to immediately patch them against multiple security flaws rated with CVSS scores ranging from medium to critical.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/sonicwall-strongly-urges-customers-to-patch-critical-sma-100-bugs/
+ Date: 2021-12-08T08:11:50-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/05/28/SonicWall.jpg)

![SonicWall ‘strongly urges’ customers to patch critical SMA 100 bugs](https://www.bleepstatic.com/content/hl-images/2021/05/28/SonicWall.jpg)


SonicWall 'strongly urges' organizations using SMA 100 series appliances to immediately patch them against multiple security flaws rated with CVSS scores ranging from medium to critical.


The bugs (reported by Rapid7's [Jake Baines](https://twitter.com/junior_baines) and NCC Group's [Richard Warren](https://twitter.com/buffaloverflow/status/1468319868600692739)) impact SMA 200, 210, 400, 410, and 500v appliances even when the web application firewall (WAF) is enabled.


The highest severity flaws patched by SonicWall this week are [CVE-2021-20038](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20038) and [CVE-2021-20045](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20045), two critical Stack-based buffer overflow vulnerabilities that can let remote unauthenticated attackers execute as the 'nobody' user in compromised appliances.


Other bugs patched by the company on Tuesday enable authenticated threat actors to gain remote code execution, inject arbitrary commands, or upload crafted web pages and files to any directory in the appliance following successful exploitation.


However, the most dangerous one if left unpatched is [CVE-2021-20039](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20039). This high severity security issue can let authenticated attackers inject arbitrary commands as the root user leading to a remote takeover of unpatched devices.


Luckily, SonicWall says that it hasn't yet found any evidence of any of these security vulnerabilities being exploited in the wild.





| **CVE** | **Summary**  | **CVSS Score**  |
| [CVE-2021-20038](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20038) | Unauthenticated Stack-based Buffer Overflow | 9.8 High |
| [CVE-2021-20039](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20039) | Authenticated Command Injection Vulnerability as Root | 7.2 High |
| [CVE-2021-20040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20040) | Unauthenticated File Upload Path Traversal Vulnerability | 6.5 Medium |
| [CVE-2021-20041](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20041) | Unauthenticated CPU Exhaustion Vulnerability | 7.5 High |
| [CVE-2021-20042](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20042) | Unauthenticated "Confused Deputy" Vulnerability  | 6.3 Medium |
| [CVE-2021-20043](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20043) | getBookmarks Heap-based Buffer Overflow  | 8.8 High |
| [CVE-2021-20044](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20044) | Post-Authentication Remote Code Execution (RCE) | 7.2 High |
| [CVE-2021-20045](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20045) | Multiple Unauthenticated File Explorer Heap-based and Stack-based Buffer Overflows  | 9.4 High |


"SonicWall urges impacted customers to implement applicable patches as soon as possible," the company says in a [security advisory](https://www.sonicwall.com/support/product-notification/product-security-notice-sma-100-series-vulnerability-patches-q4-2021/211201154715443/) published Tuesday.


Customers using SMA 100 series appliances are advised to immediately log in to their [MySonicWall.com](https://mysonicwall.com/) accounts to upgrade the firmware to versions outlined in this [SonicWall PSIRT Advisory](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0026).


Upgrade assistance on how to upgrade the firmware on SMA 100 appliances is available [in this knowledgebase article](https://www.sonicwall.com/support/knowledge-base/how-to-upgrade-firmware-on-sma-100-series-appliances/170502339501169/) or by contacting [SonicWall's support](https://www.sonicwall.com/support/contact-support/).


To put the importance of patching these security flaws into perspective, SonicWall SMA 100 appliances have been targeted by ransomware gangs multiple times since the start of 2021.


For instance, Mandiant said in April that the [CVE-2021-20016](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0001) SMA 100 zero-day was exploited to deploy a [new ransomware strain known as FiveHands](https://www.bleepingcomputer.com/news/security/new-ransomware-group-uses-sonicwall-zero-day-to-breach-networks/) starting with January when it was also used to target [SonicWall's internal systems](https://www.bleepingcomputer.com/news/security/sonicwall-firewall-maker-hacked-using-zero-day-in-its-vpn-device/). Before patches were released in [late February 2021](https://www.bleepingcomputer.com/news/security/sonicwall-firewall-maker-hacked-using-zero-day-in-its-vpn-device/), the same bug was [abused indiscriminately in the wild](https://www.bleepingcomputer.com/news/security/sonicwall-sma-100-zero-day-exploit-actively-used-in-the-wild/).


In July, SonicWall also warned of the [increased risk of ransomware attacks](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-critical-ransomware-risk-to-eol-sma-100-vpn-appliances/) targeting unpatched end-of-life SMA 100 series and Secure Remote Access products. However, CrowdStrike, Coveware security researchers, and CISA warned that SonicWall appliances were [already targeted by HelloKitty ransomware](https://www.bleepingcomputer.com/news/security/hellokitty-ransomware-is-targeting-vulnerable-sonicwall-devices/).


SonicWall's products are [used by over 500,000 business customers](https://blog.sonicwall.com/en-us/2021/08/sonicwall-celebrating-three-decades-of-putting-customers-first/) from 215 countries and territories worldwide, many deployed on the networks of the world's largest companies and government agencies.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=FIVEHANDS]] [[action.malware.name=HELLOKITTY]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Sonicwall]] [[Ransomware]] [[Stack-based]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-20038]] [[CVE-2021-20045]] [[CVE-2021-20039]] [[CVE-2021-20040]] [[CVE-2021-20041]] [[CVE-2021-20042]] [[CVE-2021-20043]] [[CVE-2021-20044]] [[CVE-2021-20016]]

