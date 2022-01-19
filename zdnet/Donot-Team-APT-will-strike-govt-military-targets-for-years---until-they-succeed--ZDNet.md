# Donot Team APT will strike gov't, military targets for years - until they succeed | ZDNet
### The group has been described as remarkably persistent in cyberattacks.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/donot-team-apt-will-strike-govt-targets-for-years-until-they-succeed/
+ Date: 2022-01-19 09:40:09
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/847748be18bb84f0faa006ede45a39882393480c/2021/07/16/fd81c075-348a-480c-9d93-affd102e5175/python-programming-language-code-data.jpg?width=770&height=578&fit=crop&auto=webp)

Researchers have exposed the inner workings of Donot Team, a threat group that will strike the same targets for years if that's what it takes to succeed. 


Also known as APT-C-35 and SectorE02, the Electronic Frontier Foundation (EFF) has previously tied Donot Team [to Innefu Labs](https://www.amnesty.org/en/latest/news/2021/10/togo-activist-targeted-with-spyware-by-notorious-hacker-group/), an Indian 'cybersecurity' company that claims to work with the government. 

According to the EFF, Innefu Labs does not appear to perform "human rights due diligence" on clients and its surveillance solutions, "despite the enormous risks their products pose to civil society." 

Active since at least 2016, Donot Team tends to focus on a small number of targets in Asian countries including Bangladesh, Sri Lanka, Pakistan, and Nepal. Entities including local government departments, embassies, military units, and Ministries of Foreign Affairs are on the victim list. 

While the advanced persistent threat (APT) group tends to stay within this geographical area, Donot Team has also been traced to attacks against embassies in the Middle East, Latin America, North America, and Europe.  

Donot Team group members leverage a custom "yty" malware framework in attacks. Malware in use is suitable for Windows machines and Android handsets.  

What makes this APT interesting is its consistency and how persistent Donot Team can be. According [to ESET researchers](https://www.welivesecurity.com/2022/01/18/donot-go-do-not-respawn/), the group will constantly hammer at a target network, in some cases for years, until they have found a way in.  






"It's not a rarity for APT operators to attempt to regain access to a compromised network after they have been ejected from it," ESET says. "In some cases, this is achieved through the deployment of a stealthier backdoor that remains quiet until the attackers need it; in other cases, they simply restart their operation with new malware or a variant of the malware they used previously. The latter is the case with Donot Team operators, only that they are remarkably persistent in their attempts." 

The cybersecurity researchers say that phishing emails will be sent every two to four months to the same targets. This consistency, which is aimed at luring an employee into opening a malicious Office attachment, was not gained through spoofing; instead, it appears that compromised email accounts – or overall email servers – obtained in earlier campaigns are used to conduct further phishing attempts.  

If a victim opens an attachment, they are at risk through malicious macros or .RTF files with .doc extensions that contain an exploit for [CVE‑2017‑11882](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2017-11882), a Microsoft Office memory corruption flaw leading to remote code execution (RCE).  

In addition, the .RTFs contain embedded .DLLs that can be used to download further malicious components and to deploy shellcode. 

The shellcode is used to deliver DarkMusical and Gedit malware. DarkMusical is comprised of a chain of downloaders and droppers, leading to the launch of a basic backdoor tasked with handling command-and-control (C2) server communication, file & folder creation, and data exfiltration.   

Gedit is also connected to the yty framework. This malware variant downloads components to maintain persistence – such as through scheduled tasks – and also contains reverse shell capabilities, screenshot functionality, and is able to collect and steal files.  

"Donot Team makes up for its low sophistication with tenacity," ESET says. "We expect that it will continue to push on regardless of its many setbacks. Only time will tell if the group evolves its current TTPs and malware." 

###  Previous and related coverage

* [New advanced hacking group targets governments, engineers worldwide](https://www.zdnet.com/article/new-advanced-hacking-group-targets-governments-engineers-worldwide/)
* [Aquatic Panda infiltrated academic institution through Log4j vulnerability, says CrowdStrike](https://www.zdnet.com/article/apt-group-seen-attacking-academic-institution-through-log4j-vulnerability-crowdstrike/)
* [Chinese APT LuminousMoth abuses Zoom brand to target gov't agencies](https://www.zdnet.com/article/chinese-apt-luminousmoth-abuses-zoom-brand-to-target-govt-agencies/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=RTM]] [[action.malware.name=Tor]] [[action.malware.name=yty]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.continent.name=Asia]] [[victim.country.name=Bangladesh]] [[victim.continent.name=Asia]] [[victim.city.name=Dili]] [[victim.country.name=East Timor]] [[victim.continent.name=Asia]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=Nepal]] [[victim.continent.name=Asia]] [[victim.country.name=Pakistan]] [[victim.continent.name=Asia]] [[victim.country.name=Sri Lanka]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Donot]] [[Malware]] [[Eset]] [[ZDNet]]

