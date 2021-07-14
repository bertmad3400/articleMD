# SonicWall warns of 'critical' ransomware risk to EOL SMA 100 VPN appliances
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-critical-ransomware-risk-to-eol-sma-100-vpn-appliances/)
+ Date: July 14, 2021
+ Author: Sergiu Gatlan


## Article:
![SonicWall warns of 'critical' ransomware risk to SMA 100 VPN appliances](https://www.bleepstatic.com/content/hl-images/2021/05/28/SonicWall.jpg)


SonicWall has issued an "urgent security notice" warning customers of ransomware attacks targeting unpatched [end-of-life](https://www.sonicwall.com/support/product-lifecycle-tables/sonicwall-secure-mobile-access-100-series/hardware/) (EoL) Secure Mobile Access (SMA) 100 series and Secure Remote Access (SRA) products.


"Through the course of collaboration with trusted third parties, SonicWall has been made aware of threat actors actively targeting Secure Mobile Access (SMA) 100 series and Secure Remote Access (SRA) products running unpatched and end-of-life (EOL) 8.x firmware in an **imminent ransomware campaign using stolen credentials**," the company said.



According to SonicWall, the attacks target a known vulnerability patched in newer versions of firmware, and they do not impact SMA 1000 series products.


"Organizations that fail to take appropriate actions to mitigate these vulnerabilities on their SRA and SMA 100 series products are **at imminent risk of a targeted ransomware attack**," SonicWall [warns](https://www.sonicwall.com/support/product-notification/urgent-security-notice-critical-risk-to-unpatched-end-of-life-sra-sma-8-x-remote-access-devices/210713105333210/).


Disconnect or update affected devices
-------------------------------------


Companies still using EoL SMA and/or SRA devices with 8.x firmware are urged to update the firmware immediately or disconnect the appliances as soon as possible to fend off the critical risk of ransomware attacks.


Customers using actively supported SMA 210/410/500v devices with the vulnerable 8.x firmware targeted in these attacks are also advised to immediately update to the latest version, which mitigates vulnerabilities discovered in early 2021.


"As additional mitigation, you should also immediately reset all credentials associated with your SMA or SRA device, as well as any other devices or systems using the same credentials," SonicWall adds. "As always, we strongly recommend enabling multifactor authentication (MFA)."




> 
> In Enterprise IT it is very very (very) common to run end of life software, risk accepted.  
>   
> 
> Don't do that with internet boundary appliances. <https://t.co/9JWUJeIMYO>
> 
> 
> — Kevin Beaumont (@GossiTheDog) [July 14, 2021](https://twitter.com/GossiTheDog/status/1415326511150813184?ref_src=twsrc%5Etfw)


Depending on the product they use, SonicWall recommends organizations to:


* **SRA 4600/1600** (EOL 2019)
	+ Disconnect immediately
	+ Reset passwords


* **SRA 4200/1200** (EOL 2016)
	+ Disconnect immediately
	+ Reset passwords


* **SSL-VPN 200/2000/400** (EOL 2013/2014)
	+ Disconnect immediately
	+ Reset passwords


* **SMA 400/200** (Still Supported, in Limited Retirement Mode)
	+ Update to **10.2.0.7-34** or **9.0.0.10** immediately
	+ Reset passwords
	+ Enable MFA


SonicWall shared the following statement with BleepingComputer regarding the attacks.



> 
> "Threat actors will take any opportunity to victimize organizations for malicious gain. This exploitation targets a long-known vulnerability that was patched in newer versions of firmware released in early 2021. SonicWall immediately and repeatedly contacted impacted organizations of mitigation steps and update guidance.  
> 
> 
> Even though the footprint of impacted or unpatched devices is relatively small, SonicWall continues to strongly advise organizations to patch supported devices or decommission security appliances that are no longer supported, especially as it receives updated intelligence about emerging threats. The continued use of unpatched firmware or end-of-life devices, regardless of vendor, is an active security risk." - SonicWall
> 
> 
> 


BleepingComputer had also asked what ransomware operation was utilizing the vulnerability but was told that they could not provide that info.


SonicWall devices previously targeted by ransomware
---------------------------------------------------


In April, threat actors also exploited a zero-day bug in SonicWall SMA 100 Series VPN appliances to deploy a [new ransomware strain known as FiveHands](https://www.bleepingcomputer.com/news/security/new-ransomware-group-uses-sonicwall-zero-day-to-breach-networks/) on the networks of North American and European targets.


This threat group, tracked by Mandiant as UNC2447, exploited the [CVE-2021-20016](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0001) SonicWall vulnerability to breach systems and deliver FiveHands ransomware payloads before SonicWall released patches in [late February 2021](https://www.bleepingcomputer.com/news/security/sonicwall-firewall-maker-hacked-using-zero-day-in-its-vpn-device/).


The same zero-day was also abused in attacks [targeting SonicWall's internal systems](https://www.bleepingcomputer.com/news/security/sonicwall-firewall-maker-hacked-using-zero-day-in-its-vpn-device/) in January and later [exploited indiscriminately in the wild](https://www.bleepingcomputer.com/news/security/sonicwall-sma-100-zero-day-exploit-actively-used-in-the-wild/).


In March, Mandiant threat analysts discovered [three more zero-day vulnerabilities](https://www.bleepingcomputer.com/news/security/sonicwall-warns-customers-to-patch-3-zero-days-exploited-in-the-wild/) in SonicWall's on-premises and hosted Email Security (ES) products.


These zero-days were also actively exploited by a group tracked as UNC2682 to backdoor systems using BEHINDER web shells, allowing them to move laterally through victims' networks and gain access to emails and files.




#### Tags:
[[SonicWall]] [[ransomware]] [[SRA]] [[EOL]] [[end-of-life]] [[zero-day]] [[Bleeping Computer]]
