# Indian Patchwork hacking group infects itself with remote access Trojan | ZDNet
### Researchers pounced on the opportunity the mistake created.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/indian-patchwork-hacking-group-infect-themselves-with-remote-access-trojan/
+ Date: 2022-01-10 13:55:00
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/96e6ad20d1153431ee5ab02f0a455df0f5c94e32/2020/12/02/d91169f7-50ff-46fd-8f40-fb36d4d1f8e5/istock-5193359161.jpg?width=770&height=578&fit=crop&auto=webp)

An Indian threat group's inner workings have been exposed after it accidentally infected its own development environment with a remote access Trojan (RAT).


Dubbed [Patchwork by Malwarebytes](https://blog.malwarebytes.com/threat-intelligence/2022/01/patchwork-apt-caught-in-its-own-web/) and tracked under names including Hangover Group, Dropping Elephant, Chinastrats, and Monsoon, the Indian group has been on the scene since at least 2015 and is actively launching campaigns designed to deploy RATs for the purposes of data theft and other malicious activities. 

In one of the latest attack waves connected to Patchwork, the group targeted individual faculty members from research institutions specializing in biomedical and molecular sciences. 

On January 7, the Malwarebytes team said it was able to delve into the advanced persistent threat (APT) group's activities after Patchwork managed to infect its own systems with its own RAT creation, "resulting in captured keystrokes and screenshots of their own computer and virtual machines." 

According to the cybersecurity researchers, Patchwork typically relies on spear-phishing attacks, with tailored emails sent to specific targets. These emails aim to drop RTF files containing the BADNEWS RAT, of which a new variant has now been found. 

The latest version of this malware, dubbed Ragnatela, was compiled in November 2021. The Trojan is capable of capturing screenshots, keylogging, listing OS processes and machine files, uploading malware, and executing additional payloads.  

After examining Patchwork's systems, the team ascertained that Ragnatela is stored in malicious RTF files as OLE objects, often crafted to be official communication from Pakistani authorities. An exploit for a known Microsoft Equation Editor vulnerability is used to execute the RAT.  






Based on the attacker's control panels, Malwarebytes was able to name the Pakistani government's Ministry of Defense, the National Defense University of Islamabad, the Faculty of Bio-Sciences (FBS) at UVAS University, the HEJ Research Institute at the University of Karachi, and the molecular medicine department at SHU University as organizations infiltrated by Patchwork.  

Patchwork managed to infect its own development machine with Ragnatela, and so the researchers were also able to see them make use of VirtualBox and VMware virtual machines (VMs) to conduct malware testing.  

"Other information that can be obtained is that the weather at the time was cloudy with 19 degrees and that they haven't updated their Java yet," Malwarebytes said. "On a more serious note, the threat actor uses VPN Secure and CyberGhost to mask their IP address." 

This is the first time the group has been connected to attacks against the biomedical research community, which may suggest a pivot in Patchwork's priority targets.  

###  Previous and related coverage

* [Chinese APT LuminousMoth abuses Zoom brand to target gov't agencies](https://www.zdnet.com/article/chinese-apt-luminousmoth-abuses-zoom-brand-to-target-govt-agencies/).
* [New advanced hacking group targets governments, engineers worldwide](https://www.zdnet.com/article/new-advanced-hacking-group-targets-governments-engineers-worldwide/).
* [Transparent Tribe APT targets government, military by infecting USB devices](https://www.zdnet.com/article/transparent-tribe-hacking-group-spreads-malware-by-infecting-usb-devices/).



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Threatactor:
[[threatactor.name=Equation]] [[threatactor.name=Patchwork]] [[threatactor.name=Patchwork]] [[threatactor.name=Patchwork]] [[threatactor.name=Patchwork]] [[threatactor.name=Patchwork]] [[threatactor.name=RTM]] [[threatactor.name=Transparent Tribe]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=BADNEWS]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=RTM]] [[action.malware.name=Tor]] [[action.malware.name=UPPERCUT]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Healthcare]] [[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=Pakistan]] [[victim.continent.name=Asia]] [[victim.city.name=Islamabad]] [[victim.country.name=Pakistan]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Malwarebytes]] [[Malware]] [[Ragnatela]] [[ZDNet]]

