# Arid Viper hackers strike Palestine with political lures - and Trojans | ZDNet
### The threat group is suspected of being located in Gaza.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/arid-viper-hackers-strike-palestine-with-political-lures-and-trojans/
+ Date: 2022-02-02 13:00:01
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/20bd8d60a4db4594161c3039ba0dcea2118a987b/2018/08/23/549238a0-a1ae-4b18-b272-8a2eae611d79/lovely-trojan-horse.jpg?width=770&height=578&fit=crop&auto=webp)

The Arid Viper cyberattack group is back with a new campaign targeting Palestinian organizations and activists. 


The [advanced persistent threat](https://blog.talosintelligence.com/2017/06/palestine-delphi.html) (APT) group, believed to be located in Gaza -- an area of conflict and hotbed of tension between Israel and Palestine -- attacks organizations worldwide but now currently appears to be focused on entities related to the politics surrounding Palestine. 

Arid Viper, also known as Desert Falcon, Two-tailed Scorpion, or APT C-23, has been around since at least 2015. In the past, the group has been responsible for spear phishing [attacks against](https://apt.360.cn/orgDetail/27) Palestinian law enforcement, [the military](https://research.checkpoint.com/2020/hamas-android-malware-on-idf-soldiers-this-is-how-it-happened/), educational establishments, and the Israel Security Agency (ISA).  

Windows and [Android malware](https://www.welivesecurity.com/2020/09/30/aptc23-group-evolves-its-android-spyware/) have been utilized previously, the latter of which is spread through [fake app stores](https://www.welivesecurity.com/2020/09/30/aptc23-group-evolves-its-android-spyware/). Delphi malware, however, has featured heavily in previous campaigns and still seems to be the weapon of choice for Arid Viper. 

On Wednesday, researchers [from Cisco Talos](https://blog.talosintelligence.com/2022/02/arid-viper-targets-palestine.html) said the ongoing campaign uses a Delphi-based Micropsia implant to strike activists.  

"The most recent samples found by Talos lead us to believe this is a campaign linked to the previous campaign we reported on in 2017," the researchers say, adding that the main focus of Arid Viper is on cyberespionage – and targets are selected by the operators based on the political motivation of the "liberation of Palestine." 

The initial attack vector is phishing emails, with included content linked to the political Palestinian situation and usually stolen from news agencies. For example, one decoy document was related to Palestinian family reunification, published in 2021, whereas another contained a record of activist questions.  






If an intended victim opens one of these documents, the implant triggers, extracting a range of Remote Access Trojan (RAT) capabilities. The malware will collect operating system and antivirus data, exfiltrate it to the operator's command-and-control (C2) server, steal content on the machine, take screenshots, and conduct further surveillance activities.  

A timer contained in the implant will also establish persistence on the target machine through the Startup folder. 

"The continued use of the same TTPs over the past four years indicates that the group doesn't feel affected by the public exposure of its campaigns and implants, and continues to operate business as usual," Talos says. "This complete lack of deterrence makes them a dangerous group once they decide to target an organization or individual." 

In related news this week, Talos and Cybereason disclosed three separate APT campaigns believed to be the work of state-backed Iranian cybercriminals. [MuddyWater](https://www.zdnet.com/article/state-sponsored-iranian-hackers-attack-turkish-govt-organizations/), [Phosphorus, and Moses Staff](https://www.zdnet.com/article/these-hackers-are-hitting-victims-with-ransomware-in-an-attempt-to-cover-their-tracks/) are targeting entities in Turkey, the US, Israel, Europe, and the Middle East.  

###  Previous and related coverage

* [Chinese APT deploys MoonBounce implant in UEFI firmware](https://www.zdnet.com/article/chinese-apt-deploy-moonbounce-malware-in-uefi-firmware/)
* [Donot Team APT will strike gov't, military targets for years - until they succeed](https://www.zdnet.com/article/donot-team-apt-will-strike-govt-targets-for-years-until-they-succeed/)
* [New advanced hacking group targets governments, engineers worldwide](https://www.zdnet.com/article/new-advanced-hacking-group-targets-governments-engineers-worldwide/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Threatactor:
[[threatactor.name=Magic Hound]] [[threatactor.name=MuddyWater]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=ChChes]] [[action.malware.name=Conti]] [[action.malware.name=Desert Scorpion]] [[action.malware.name=Micropsia]] [[action.malware.name=Sakula]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]]

#### Location:
[[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.country.name=Israel]] [[victim.continent.name=Asia]] [[victim.country.name=Palestine]] [[victim.continent.name=Asia]] [[victim.country.name=Turkey]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=Turkey]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Talos]] [[Malware]] [[ZDNet]]

