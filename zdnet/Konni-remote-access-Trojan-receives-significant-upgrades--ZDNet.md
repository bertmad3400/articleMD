# Konni remote access Trojan receives 'significant' upgrades | ZDNet
### Researchers say the security community should keep a close eye on this malware strain.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/konni-remote-access-trojan-receives-significant-upgrades/
+ Date: 2022-01-27 10:17:15
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/96e6ad20d1153431ee5ab02f0a455df0f5c94e32/2020/12/02/d91169f7-50ff-46fd-8f40-fb36d4d1f8e5/istock-5193359161.jpg?width=770&height=578&fit=crop&auto=webp)

The Konni Remote Access Trojan (RAT) has recently received "significant" updates, researchers say, who also urge the community to keep a close eye on the malware.  


On Wednesday, cybersecurity firm Malwarebytes [published an advisory](https://blog.malwarebytes.com/threat-intelligence/2022/01/konni-evolves-into-stealthier-rat/) on the malware's latest developments, noting that the Trojan is under active development resulting in "major" changes. 

Konni has been detected in the wild for roughly eight years. A report on the malware published by [BlackBerry in 2017](https://blogs.blackberry.com/en/2017/08/threat-spotlight-konni-stealthy-remote-access-trojan) said that the malware made use of "basic" anti-analysis techniques and was employed for surveillance purposes, rather than the typical financial attacks often linked to RATs.  

Past campaigns have hinted strongly at a link with North Korea. Phishing documents used to spread the Trojan tend to have themes connected to the Hermit Kingdom, including content relating to [missile capabilities](https://blog.talosintelligence.com/2017/07/konni-references-north-korean-missile-capabilities.html), hydrogen bombs, and articles copied from the Yonhap news agency that talked about the country. 

The attached documents contained the payload, and once executed on a vulnerable Windows machine, Konni would gather data through file grabs, keystroke logs, and screen capturing.  

Konni is believed to be the work of the Kimsuky threat group, which has attacked South Korean [think tanks](https://www.zdnet.com/article/north-korean-hackers-target-the-souths-think-tanks-through-blog-posts/), political groups in [Russia](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/), and entities in both Japan and the United States.  

According to Malwarebytes, the old Trojan has now evolved into a "stealthier" version of itself. New samples show that the phishing attack vector has primarily stayed the same – with the payload deployed through malicious Office documents – but the Trojan, a .DLL file linked to an .ini file, now contains revised functionality. 






Older versions of the RAT relied on two branches to execute using a Windows service: svchost.exe and rundll32.exe strings. Malwarebytes explained: 

"New samples will not show these strings. In fact, rundll is no longer a valid way to execute the sample. Instead, when an execution attempt occurs using rundll, an exception is thrown in the early stages." 

The malware has also transitioned from base64 encoding to AES encryption to protect its strings and for obfuscation purposes. In addition, Konni now utilizes AES when configuration and support files are dropped – such as the .ini file that contains the command-and-control (C2) server address – as well as when files are sent to the C2. 

A previously-unknown packer was also used by some recent Konni samples, but threat data collected by the cybersecurity firm suggests it may have been left out of real-world scenarios.  

"As we have seen, Konni is far from being abandoned," Malwarebytes commented. "The authors are constantly making code improvements. In our point of view, their efforts are aimed at breaking the typical flow recorded by sandboxes and making detection harder, especially via regular signatures as critical parts of the executable are now encrypted." 

Earlier this month, Cisco Talos documented a [recent campaign](https://www.zdnet.com/article/remote-access-trojans-spread-through-microsoft-azure-aws-cloud-service-abuse/) in which cloud infrastructure provided by vendors including Microsoft Azure and Amazon Web Services (AWS) was being abused to spread commercial RATs.  

Strains including Nanocore, Netwire, and AsyncRAT were being deployed by the operators, who also abused DuckDNS to facilitate the download of malicious packages.  

###  Previous and related coverage

* [This dangerous mobile Trojan has stolen a fortune from over 10 million victims](https://www.zdnet.com/article/this-dangerous-mobile-trojan-has-stolen-a-fortune-from-over-10-million-victims-worldwide/)
* [New banking Trojan SharkBot makes waves across Europe, US](https://www.zdnet.com/article/new-banking-trojan-sharkbot-makes-waves-across-europe/)
* [Remote Access Trojans spread through Microsoft Azure, AWS cloud service abuse](https://www.zdnet.com/article/remote-access-trojans-spread-through-microsoft-azure-aws-cloud-service-abuse/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Threatactor:
[[threatactor.name=Kimsuky]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=KONNI]] [[action.malware.name=NanoCore]] [[action.malware.name=Net]] [[action.malware.name=NETWIRE]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Agriculture]] [[victim.industry.name=Finance]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Japan]] [[victim.continent.name=Asia]] [[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=South Korea]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Konni]] [[Malware]] [[Malwarebytes]] [[ZDNet]]

