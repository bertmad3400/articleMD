# These hackers are hitting victims with ransomware in an attempt to cover their tracks | ZDNet
### Cyber-espionage campaigns linked to the Iranian government are using new malware to secretly snoop around networks, and then drop malware to hide any trace of activity.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/these-hackers-are-hitting-victims-with-ransomware-in-an-attempt-to-cover-their-tracks/
+ Date: 2022-02-01 13:00:15
+ Author: Danny Palmer


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/36eacd57be8cf45d5617f398302d88af4e47917b/2021/12/06/65e99cdf-bb9a-43e6-b9f2-7bbcfab2c195/hacker-hands-typing-on-a-keyboard.jpg?width=770&height=578&fit=crop&auto=webp)

Iranian hackers are targeting a range of organisations around the world in campaigns that use previously unidentified malware to conduct cyber-espionage actions and steal data from victims – and in some cases, the state-backed attackers are also launching ransomware in a dual effort to embarrass victims and cover their tracks. 

The two separate campaigns have been detailed by cybersecurity researchers at Cybereason, who've attributed the activity to an Iranian hacking group [they track as Phosphorus](https://www.cybereason.com/blog/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage) – [also known as APT35 and Charming Kitten](https://www.zdnet.com/article/these-iranian-hackers-posed-as-academics-in-a-bid-to-steal-email-passwords/) – along with another Iranian-linked cyber operation, [dubbed Moses Staff](https://www.cybereason.com/blog/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations).


The attacks by Phosphorus have a more 'traditional' approach to cyber espionage, in that they're designed to steal information and conduct operations that run in the interests of Tehran.  

**SEE:**[**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/#link=%7B%22role%22:%22standard%22,%22href%22:%22http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/%22,%22target%22:%22_blank%22,%22absolute%22:%22%22,%22linkText%22:%22%3Cstrong%3EA%20winning%20strategy%20for%20cybersecurity%3C/strong%3E%22%7D)**(ZDNet special report)**

The group is suspected of being behind multiple espionage campaigns against organisations and individuals in the United States, Europe and the Middle East, [as well as attempts to interfere with the US presidential elections](https://www.zdnet.com/article/us-slaps-sanctions-on-iranian-entities-for-interfering-with-2020-presidential-election/).

Now Phosphorus has added a new tool to their arsenal, [trojan malware](https://www.zdnet.com/article/trojan-malware-the-hidden-cyber-threat-to-your-pc/), which researchers have called PowerLess Backdoor, that allows attackers to conduct activity with little chance of being detected.  

Once installed on a compromised machine, PowerLess allows attackers to download additional payloads, and steal information, while a keylogging tool sends all the keystrokes entered by the user direct to the attacker. 






Analysis of PowerLess backdoor campaigns appear to link attacks to tools, techniques and motivations associated with Phosphorus campaigns. In addition to this, analysis of the activity seems to link the Phosphorus threat group to ransomware attacks.  

One of the IP addresses being used in the campaigns also serves as a command and control server for the recently discovered Momento ransomware, leading researchers to suggest there could be a link between the ransomware attacks and state-backed activity. 

"A connection between Phosphorus and the Memento ransomware was also found through mutual TTP patterns and attack infrastructure, strengthening the connection between this previously unattributed ransomware and the Phosphorus group," said the report. 

Cybereason also found a link between a second Iranian hacking operation, named Moses Staff, and additional ransomware attacks, which are deployed with the aid of another newly identified trojan backdoor, dubbed StrifeWater.  

The trojan is used for the initial phases of the attack, before it removes itself after being replaced with other tools. The way StrifeWater removes itself relatively early in the infection process is the reason it hasn't been detailed previously. 

Like Phosphorous, the key aim of Moses Staff is to conduct espionage and steal information "to advance Iran's geopolitical goals" with victims all over the world, including the US, Israel, Germany, Chile, Turkey, and the United Arab Emirates.  

But while the whole point of espionage is usually to stay under the radar, Moses Staff attacks actively deploy a form of ransomware after they've gathered what they need. 

"It's like a scorched earth policy," Assaf Dahan, head of threat research at the Cybereason Nocturnus Team, told ZDNet.

The malware attacks in a similar way to ransomware, in that files are encrypted and stolen, but unlike regular ransomware operations, there isn't a ransom demand – the attacks are launched purely with damage in mind. However, the similarity in design to ransomware could draw victims away from suspecting an espionage campaign as they rush to combat what looks like a standard ransomware attack.  

**SEE:** [**Why Iranian hacking operations could be a threat to your network**](https://www.zdnet.com/video/why-iranian-hacking-operations-could-be-a-threat-to-your-network/)

But while it looks like ransomware, those behind it haven't built a backend for accepting a ransom payment, let alone supplying an encryption key. 

"Their main goal is to disrupt business and disseminate fear," said Dahan, describing how Moses Staff attacks, while state-sponsored, also appear to take cues from hacktivism campaigns, with custom graphics and boasts about hacking victims. 

"They tried to appear as activists group operating on behalf of Iranian state interest," he explained, adding: "They have a website and a logo and everything, they say 'hey, it's us' and they're quite verbose and vocal about their mission."

It's thought that both campaigns remain active, but there are actions that organisations can take in an effort to avoid becoming a victim. Key among these is [patching software and systems](https://www.zdnet.com/article/this-one-change-could-protect-your-systems-from-attack-so-why-dont-more-companies-do-it/), because the attacks are known to exploit publicly available exploits, including the [ProxyShell vulnerabilities in Microsoft Exchange](https://www.zdnet.com/article/the-fbi-removed-hacker-backdoors-from-vulnerable-microsoft-exchange-servers-not-everyone-likes-the-idea/), as well [Log4j vulnerabilities](https://www.zdnet.com/article/hackers-are-using-the-log4j-flaw-to-deliver-this-new-modular-backdoor/). By applying security updates as soon as possible, it reduces the chances of any attackers having time to exploit disclosed vulnerabilities. 

It's also recommended that information security staff and network administrators are proactive in looking for threats, [by not only fully understanding their own network](https://www.zdnet.com/article/the-key-to-stopping-cyberattacks-understanding-your-own-systems-before-the-hackers-strike/) and being able to detect if something might be suspicious, but also to keep up to date with intelligence of the latest potential threats so they know what to look for. 

"Be proactive. Don't just wait for an alert to pop because, by the time it pops, it could be too late," said Dahan.

### **MORE ON CYBERSECURITY**

* [**US, UK, and Australia pin Iran for exploiting Fortinet and Exchange holes**](https://www.zdnet.com/article/us-uk-and-australia-pin-iran-for-exploiting-fortinet-and-exchange-holes/)
* [**Ransomware: Is the party almost over for the cyber crooks?**](https://www.zdnet.com/article/ransomware-is-the-party-almost-over-for-the-cyber-crooks/)
* [**Suspected Iranian hacking campaign targets European energy companies**](https://www.zdnet.com/article/suspected-iranian-hacking-campaign-targets-european-energy-sector/)
* [**A company spotted a security breach. Then investigators found this new mysterious malware**](https://www.zdnet.com/article/a-company-spotted-a-security-breach-then-investigators-found-this-new-mysterious-malware/)
* [**These hackers built an elaborate online profile to fool their targets into downloading malware**](https://www.zdnet.com/article/these-hackers-posed-as-an-aerobics-instructor-online-to-trick-their-targets-into-downloading-malware/)





## Tags:

#### Threatactor:
[[threatactor.name=APT3]] [[threatactor.name=Magic Hound]] [[threatactor.name=Magic Hound]] [[threatactor.name=Magic Hound]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.city.name=Tehran]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.country.name=Israel]] [[victim.continent.name=Asia]] [[victim.country.name=Turkey]] [[victim.continent.name=Asia]] [[victim.country.name=United Arab Emirates]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=Germany]] [[victim.continent.name=Europe]] [[victim.country.name=Turkey]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Chile]] [[victim.continent.name=South America]] [[victim.country.name=Australia]] [[victim.continent.name=Oceania]] [[victim.country.name=Australia]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Ransomware]] [[Malware]] [[Organisations]] [[Cybereason]] [[ZDNet]]

