# FBI links Diavol ransomware to the TrickBot cybercrime group
### The FBI has formally linked the Diavol ransomware operation to the TrickBot Group, the malware developers behind the notorious TrickBot banking trojan.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/fbi-links-diavol-ransomware-to-the-trickbot-cybercrime-group/
+ Date: 2022-01-20T13:37:25-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/08/18/DiavolRansomware.jpg)

![Diavol Ransomware](https://www.bleepstatic.com/content/hl-images/2021/08/18/DiavolRansomware.jpg)


The FBI has formally linked the Diavol ransomware operation to the TrickBot Group, the malware developers behind the notorious TrickBot banking trojan.


The TrickBot Gang, aka Wizard Spider, are the developers of malware infections that have played havoc on corporate networks for years, commonly leading to Conti and Ryuk ransomware attacks, network infiltration, financial fraud, and corporate espionage.


The TrickBot Gang is most known for its namesake, the TrickBot banking trojan, but is also behind the development of the [BazarBackdoor](https://www.bleepingcomputer.com/news/security/bazarbackdoor-trickbot-gang-s-new-stealthy-network-hacking-malware/) and [Anchor backdoors](https://www.bleepingcomputer.com/news/security/lazarus-hackers-use-trickbot-to-infect-high-end-victims/).


Prior analysis linked Diavol to TrickBot Group
----------------------------------------------


In July 2021, researchers from FortiGuard Labs [released an analysis of a new ransomware called Diavol (](https://www.bleepingcomputer.com/news/security/trickbot-cybercrime-group-linked-to-new-diavol-ransomware/)Romanian for Devil) that was seen targeting corporate victims.


The researchers saw both Diavol and Conti ransomware payloads deployed on a network in the same ransomware attack in early June 2021.


After analyzing the two ransomware samples, similarities were discovered, such as their use of asynchronous I/O operations for file encryption queuing and almost identical command-line parameters for the same functionality.


At the time, there was not enough evidence to formally link the two operations.


However, a month later, IBM X-Force researchers established[a stronger connection](https://www.bleepingcomputer.com/news/security/diavol-ransomware-sample-shows-stronger-connection-to-trickbot-gang/) between Diavol ransomware and other TrickBot Gang's malware, such as Anchor and TrickBot.


FBI links Diavol ransomware to TrickBot gang
--------------------------------------------


Today, the FBI has formally announced that they have linked the Diavol Ransomware operation to the TrickBot Gang in a new advisory sharing indicators of compromise seen in previous attacks.


"The FBI first learned of Diavol ransomware in October 2021. Diavol is associated with developers from the Trickbot Group, who are responsible for the Trickbot Banking Trojan," the FBI states in a new [FBI Flash advisory](http://www.ic3.gov/Media/News/2022/220120.pdf).


Since then, the FBI has seen ransom demands ranging between $10,000 and $500,000, with lower payments accepted after ransom negotiations.



![Warning.txt ransom note from Diavol ransomware](https://www.bleepstatic.com/images/news/ransomware/d/diavol/diavol-ransom-note.jpg)**Warning.txt ransom note from Diavol ransomware**
These amounts are in stark contrast to the higher ransoms demanded by other ransomware operations linked to TrickBot, such as Conti and Ryuk, who have historically asked for multi-million dollar ransoms.


For example, in April, the Conti ransomware operation [demanded $40 million](https://www.bleepingcomputer.com/news/security/ransomware-gang-wanted-40-million-in-florida-schools-cyberattack/) from Florida's Broward County School district and [$14 million from chip maker Advantech](https://www.bleepingcomputer.com/news/security/iot-chip-maker-advantech-confirms-ransomware-attack-data-theft/).


The FBI was likely able to formally link Diavol to the TrickBot Gang after the[arrest of Alla Witte](https://www.bleepingcomputer.com/news/security/us-charges-latvian-for-helping-develop-the-trickbot-malware/), a Latvian woman involved in the development of ransomware for the malware gang.


[Vitali Kremez](https://twitter.com/VK_Intel), CEO of AdvIntel, who has been tracking the TrickBot operations, told BleepingComputer that Witte was responsible for the development of the new TrickBot-linked ransomware.


"Alla Witte played a critical role for the TrickBot operations and based on the previous AdvIntel deep adversarial insight she was responsible for the development of the Diavol ransomware and frontend/backend project meant to support TrickBot operations with the specific tailored ransomware with the bot backconnectivity between TrickBot and Diavol," Kremez told BleepingComputer in a conversation.


"Another name for the Diavol ransomware was called "Enigma" ransomware leveraged by the TrickBot crew before the Diavol re-brand."


The FBI's advisory contains numerous indicators of compromise and mitigations for Diavol, making it an essential read for all security professionals and Windows/network administrators.


It should be noted that the Diavol ransomware originally created ransom notes named 'README\_FOR\_DECRYPT.txt' as pointed out by the FBI advisory, but BleepingComputer has seen the ransomware gang switch in November to ransom notes named 'Warning.txt.'


The FBI also urges all victims, regardless of whether they plan to pay a ransom, to promptly notify law enforcement of attacks to collect fresh IOCs that they can use for investigative purposes and law enforcement operations.


If you are affected by a Diavol attack, it is also important to notify the FBI before paying as they "may be able to provide threat mitigation resources to those impacted by Diavol ransomware."





## Tags:

#### Threatactor:
[[threatactor.name=Indrik Spider]] [[threatactor.name=Wizard Spider]]

#### Action:
[[action.malware.name=Anchor]] [[action.malware.name=at]] [[action.malware.name=Bazar]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Ryuk]] [[action.malware.name=Tor]] [[action.malware.name=TrickBot]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Finance]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Oman]] [[victim.continent.name=Asia]] [[victim.country.name=Latvia]] [[victim.continent.name=Europe]] [[victim.country.name=Romania]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Diavol]] [[Trickbot]] [[Malware]] [[Conti]] [[Witte]] [[Bleepingcomputer]] [[Bleeping Computer]]

