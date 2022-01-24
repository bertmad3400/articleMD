# Attackers now actively targeting critical SonicWall RCE bug
### A critical severity vulnerability impacting SonicWall's Secure Mobile Access (SMA) gateways addressed last month is now targeted in ongoing exploitation attempts.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/attackers-now-actively-targeting-critical-sonicwall-rce-bug/
+ Date: 2022-01-24T16:48:56-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/24/Sonicwall.jpg)

![SonicWall ](https://www.bleepstatic.com/content/hl-images/2022/01/24/Sonicwall.jpg)


A critical severity vulnerability impacting SonicWall's Secure Mobile Access (SMA) gateways addressed last month is now targeted in ongoing exploitation attempts.


The bug is an unauthenticated stack-based buffer overflow tracked as CVE-2021-20038 that impacts SMA 100 series appliances (including SMA 200, 210, 400, 410, and 500v) even when the web application firewall (WAF) is enabled.


Successful exploitation can let remote unauthenticated attackers execute code as the 'nobody' user in compromised SonicWall appliances.


"There are no temporary mitigations. SonicWall urges impacted customers to implement applicable patches as soon as possible," [the company said in December](https://www.bleepingcomputer.com/news/security/sonicwall-strongly-urges-customers-to-patch-critical-sma-100-bugs/) after releasing CVE-2021-20038 security updates adding that it found no evidence the bug was exploited in the wild at the time.


However, today, Richard Warren, a Principal Security Consultant at NCC Group and the one who found and reported the vulnerability, said that threat actors are now attempting to exploit the vulnerability in the wild.


Warren added that attackers are also trying to brute force their way in by password spraying known SonicWall appliances default passwords.


"Some attempts itw on CVE-2021-20038 (SonicWall SMA RCE). Also some password spraying of default passwords from the past few days. Remember to update AND change default password," the security researcher [tweeted](https://twitter.com/buffaloverflow/status/1485671824725786633) today.


"They don't look successful as far as I can tell," Warren also told BleepingComputer. "Using that exploit you need to make a huge number of requests (like a million). They are probably just trying their luck or don't understand the exploit."


Patch now to defend against attackers
-------------------------------------


While these ongoing attacks haven't yet been successful, SonicWall customers are advised to patch their SMA 100 appliances to block hacking attempts.


SMA 100 users are recommended to log in to their [MySonicWall.com](https://mysonicwall.com/) accounts to upgrade the firmware to versions outlined in this [SonicWall PSIRT Advisory](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0026).


Assistance on how to upgrade the firmware is available [in this knowledgebase article](https://www.sonicwall.com/support/knowledge-base/how-to-upgrade-firmware-on-sma-100-series-appliances/170502339501169/) or by contacting [SonicWall's support](https://www.sonicwall.com/support/contact-support/).


SonicWall SMA 100 appliances have been targeted in multiple campaigns since the start of 2021, including in attacks coordinated by ransomware gangs.


For instance, the [CVE-2021-20016](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0001) SMA 100 zero-day was used [to deploy FiveHands ransomware](https://www.bleepingcomputer.com/news/security/new-ransomware-group-uses-sonicwall-zero-day-to-breach-networks/) starting with January 2021 when it was also exploited in attacks against [SonicWall's internal systems](https://www.bleepingcomputer.com/news/security/sonicwall-firewall-maker-hacked-using-zero-day-in-its-vpn-device/). Before being patched almost two months later, in [late February 2021](https://www.bleepingcomputer.com/news/security/sonicwall-firewall-maker-hacked-using-zero-day-in-its-vpn-device/), the same flaw was also [abused indiscriminately in the wild](https://www.bleepingcomputer.com/news/security/sonicwall-sma-100-zero-day-exploit-actively-used-in-the-wild/).


In July, SonicWall warned of [the increased risk of ransomware attacks](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-critical-ransomware-risk-to-eol-sma-100-vpn-appliances/) targeting unpatched end-of-life SMA 100 series and Secure Remote Access products. However, CrowdStrike, Coveware security researchers, and CISA warned that [HelloKitty ransomware operators were already targeting SonicWall appliances](https://www.bleepingcomputer.com/news/security/hellokitty-ransomware-is-targeting-vulnerable-sonicwall-devices/).


[Over 500,000 business customers](https://blog.sonicwall.com/en-us/2021/08/sonicwall-celebrating-three-decades-of-putting-customers-first/) from 215 countries are using SonicWall products worldwide, many of them deployed on the networks of government agencies and the world's largest companies.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=FIVEHANDS]] [[action.malware.name=HELLOKITTY]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Sonicwall]] [[Ransomware]] [[Cve-2021-20038]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-20038]] [[CVE-2021-20016]]

