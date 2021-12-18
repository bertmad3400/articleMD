# The Week in Ransomware - December 17th 2021 - Enter Log4j
### A critical Apache Log4j vulnerability took the world by storm this week, and now it is being used by threat actors as part of their ransomware attacks.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/the-week-in-ransomware-december-17th-2021-enter-log4j/
+ Date: 2021-12-17T18:37:23-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2020/11/03/Ransomware.jpg)

![Ransomware](https://www.bleepstatic.com/content/hl-images/2020/11/03/Ransomware.jpg)


A critical Apache Log4j vulnerability took the world by storm this week, and now it is being used by threat actors as part of their ransomware attacks.


Last Friday, a researcher publicly released an [exploit for the Log4j vulnerability](https://www.bleepingcomputer.com/news/security/new-zero-day-exploit-for-log4j-java-library-is-an-enterprise-nightmare/), dubbed 'Log4Shell.' after it was already seen targeting vulnerable Minecraft servers.


While a patch was quickly released to fix the vulnerability, researchers and threat actors quickly began scanning for and exploiting vulnerable devices. With how fast it was adopted, it was only a matter of time until threat actors used it to deploy ransomware.


It didn't take long, as threat actors revived an old ransomware named [TellYouThePass](https://www.bleepingcomputer.com/news/security/tellyouthepass-ransomware-revived-in-linux-windows-log4j-attacks/) on Monday and began distributing it via Log4j exploits.


Soon after, [another ransomware (or wiper) called Khonsari](https://www.bleepingcomputer.com/news/security/new-zero-day-exploit-for-log4j-java-library-is-an-enterprise-nightmare/) was discovered that we later learned it was [targeting vulnerable Minecraft servers](https://www.bleepingcomputer.com/news/security/microsoft-khonsari-ransomware-hits-self-hosted-minecraft-servers/).


Finally, a report today shows how the [Conti ransomware gang is using the Log4j vulnerability](https://www.bleepingcomputer.com/news/security/conti-ransomware-uses-log4j-bug-to-hack-vmware-vcenter-servers/) to quickly gain access to internal VMWare vCenter servers to encrypt virtual machines.


Other ransomware news
---------------------


While the Log4j vulnerability has taken up most of the cybersecurity community's time this week, there have been other significant developments as well.


Romanian [police arrested a ransomware affiliate](https://www.bleepingcomputer.com/news/security/police-arrests-ransomware-affiliate-behind-high-profile-attacks/) for hacking and stealing sensitive info from the networks of multiple high-profile companies worldwide.


Emotet also [began distributing Cobalt Strike beacons](https://www.bleepingcomputer.com/news/security/emotet-starts-dropping-cobalt-strike-again-for-faster-attacks/) as a primary payload, allowing ransomware gangs quicker access to compromised networks to conduct attacks.


We also learned that the [Hive Ransomware operation is becoming a major player](https://www.bleepingcomputer.com/news/security/hive-ransomware-enters-big-league-with-hundreds-breached-in-four-months/) after breaching hundreds of companies in just four months.


Finally, a massive [ransomware attack against HR services provider Kronos](https://www.bleepingcomputer.com/news/security/hive-ransomware-enters-big-league-with-hundreds-breached-in-four-months/) has caused significant impact for many companies who use them for timekeeping and payroll. We also saw a [Conti attack on McMenamins breweries](https://www.bleepingcomputer.com/news/security/mcmenamins-breweries-hit-by-a-conti-ransomware-attack/), showing that nothing is sacred.


Contributors and those who provided new ransomware information and stories this week include: [@LawrenceAbrams](https://twitter.com/LawrenceAbrams), [@DanielGallagher](https://twitter.com/DanielGallagher), [@PolarToffee](https://twitter.com/PolarToffee), [@jorntvdw](https://twitter.com/jorntvdw), [@malwrhunterteam](https://twitter.com/malwrhunterteam), [@demonslay335](https://twitter.com/demonslay335), [@VK\_Intel](https://twitter.com/VK_Intel), [@malwareforme](https://twitter.com/malwareforme), [@serghei](https://twitter.com/serghei), [@Seifreed](https://twitter.com/Seifreed), [@FourOctets](https://twitter.com/FourOctets), [@struppigel](https://twitter.com/struppigel), [@Ionut\_Ilascu](https://twitter.com/Ionut_Ilascu), [@fwosar](https://twitter.com/fwosar), [@BleepinComputer](https://twitter.com/BleepinComputer), [@billtoulas](https://twitter.com/billtoulas), [@SANGFOR](https://twitter.com/SANGFOR), [@CuratedIntel](https://twitter.com/CuratedIntel), [@80vul](https://twitter.com/80vul), [@1ZRR4H](https://twitter.com/1ZRR4H), [@AdvIntel](https://twitter.com/AdvIntel), [@MsftSecIntel](https://twitter.com/MsftSecIntel), [@GroupIB\_GIB](https://twitter.com/GroupIB_GIB), [@Bitdefender\_Ent](https://twitter.com/Bitdefender_Ent), [@Cryptolaemus1](https://twitter.com/Cryptolaemus1), [@JRoosen](https://twitter.com/JRoosen), [@BroadcomS](https://twitter.com/BroadcomSW), [@fbgwls245](https://twitter.com/fbgwls245), [@Amigo\_A\_](https://twitter.com/Amigo_A_),[@JakubKroustek](https://twitter.com/JakubKroustek), and [@pcrisk](https://twitter.com/pcrisk).


December 11th 2021
------------------


### [New STOP Ransomware variant](https://twitter.com/JakubKroustek/status/1469820999696887809)


[Jakub Kroustek](https://twitter.com/JakubKroustek) found a new STOP ransomware variant that appends the **.yjqs** extension to encrypted files.


December 13th 2021
------------------


### [Police arrests ransomware affiliate behind high-profile attacks](https://www.bleepingcomputer.com/news/security/police-arrests-ransomware-affiliate-behind-high-profile-attacks/)


Romanian law enforcement authorities arrested a ransomware affiliate suspected of hacking and stealing sensitive info from the networks of multiple high-profile companies worldwide, including a large Romanian IT company with clients from the retail, energy, and utilities sectors.


### [Kronos ransomware attack may cause weeks of HR solutions downtime](https://www.bleepingcomputer.com/news/security/kronos-ransomware-attack-may-cause-weeks-of-hr-solutions-downtime/)


Workforce management solutions provider Kronos has suffered a ransomware attack that will likely disrupt many of their cloud-based solutions for weeks.


December 14th 2021
------------------


### [New ransomware now being deployed in Log4Shell attacks](https://www.bleepingcomputer.com/news/security/new-ransomware-now-being-deployed-in-log4shell-attacks/)


The first public case of the Log4j Log4Shell vulnerability used to download and install ransomware has been discovered by researchers.


### [New White Rabbit ransomware](https://twitter.com/demonslay335/status/1470823608725475334)


[Michael Gillespie](https://twitter.com/demonslay335) is looking for a sample of the new White Rabbit ransomware that appends the **.scrypt** extension.


![Whtie Rabbit ransomware](https://www.bleepstatic.com/images/news/columns/week-in-ransomware/2021/december/17/white-rabbit-ransomware.jpg)


December 15th 2021
------------------


### [Emotet starts dropping Cobalt Strike again for faster attacks](https://www.bleepingcomputer.com/news/security/emotet-starts-dropping-cobalt-strike-again-for-faster-attacks/)


Right in time for the holidays, the notorious Emotet malware is once again directly installing Cobalt Strike beacons for rapid cyberattacks.


### [New STOP Ransomware variant](https://twitter.com/pcrisk/status/1471011861155962883)


[PCrisk](https://twitter.com/pcrisk) found a new STOP ransomware variant that appends the **.Shgv** extension to encrypted files.


December 16th 2021
------------------


### [Hive ransomware enters big league with hundreds breached in four months](https://www.bleepingcomputer.com/news/security/hive-ransomware-enters-big-league-with-hundreds-breached-in-four-months/)


The Hive ransomware gang is more active and aggressive than its leak site shows, with affiliates attacking an average of three companies every day since the operation became known in late June.


### [McMenamins breweries hit by a Conti ransomware attack](https://www.bleepingcomputer.com/news/security/mcmenamins-breweries-hit-by-a-conti-ransomware-attack/)


Portland brewery and hotel chain McMenamins suffered a Conti ransomware attack over the weekend that disrupted the company's operations.


### [Microsoft: Khonsari ransomware hits self-hosted Minecraft servers](https://www.bleepingcomputer.com/news/security/microsoft-khonsari-ransomware-hits-self-hosted-minecraft-servers/)


Microsoft urges admins of self-hosted Minecraft servers to upgrade to the latest release to defend against Khonsari ransomware attacks exploiting the critical Log4Shell security vulnerability.


### [Noberus: Technical Analysis Shows Sophistication of New Rust-based Ransomware](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/noberus-blackcat-alphv-rust-ransomware)


Symantec, a division of Broadcom Software, tracks this ransomware as Ransom.Noberus and our researchers first spotted it on a victim organization on November 18, 2021, with three variants of Noberus deployed by the attackers over the course of that attack. This would appear to show that this ransomware was active earlier than was previously reported, with [MalwareHunterTeam having told](https://www.bleepingcomputer.com/news/security/alphv-blackcat-this-years-most-sophisticated-ransomware/) [*BleepingComputer*](https://www.bleepingcomputer.com/news/security/alphv-blackcat-this-years-most-sophisticated-ransomware/) [they first saw this ransomware on November 21](https://www.bleepingcomputer.com/news/security/alphv-blackcat-this-years-most-sophisticated-ransomware/).


### [New STOP Ransomware variant](https://twitter.com/pcrisk/status/1471463383375527941)


PCrisk found a new STOP ransomware variant that appends the **.hudf** extension to encrypted files.


December 17th 2021
------------------


### [Conti ransomware uses Log4j bug to hack VMware vCenter servers](https://www.bleepingcomputer.com/news/security/conti-ransomware-uses-log4j-bug-to-hack-vmware-vcenter-servers/)


Conti ransomware operation is using the critical Log4Shell exploit to gain rapid access to internal VMware vCenter Server instances and encrypt virtual machines.


### [Logistics giant warns of BEC emails following ransomware attack](https://www.bleepingcomputer.com/news/security/logistics-giant-warns-of-bec-emails-following-ransomware-attack/)


Hellmann Worldwide is warning customers of an increase in fraudulent calls and emails regarding payment transfer and bank account changes after a recent ransomware attack.


### [TellYouThePass ransomware revived in Linux, Windows Log4j attacks](https://www.bleepingcomputer.com/news/security/tellyouthepass-ransomware-revived-in-linux-windows-log4j-attacks/)


Threat actors have revived an old and relatively inactive ransomware family known as TellYouThePass, deploying it in attacks against Windows and Linux devices targeting a critical remote code execution bug in the Apache Log4j library.


### [New Dharma Ransomware variant](https://twitter.com/fbgwls245/status/1471842611044696071)


 


[dnwls0719](https://twitter.com/fbgwls245) found a new Dharma ransomware variant that appends the **.C1024** extension to encrypted files.


### That's it for this week! Hope everyone has a nice weekend!





## Tags:

#### Action:
[[action.malware.name=4H RAT]] [[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Conti]] [[action.malware.name=Emotet]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]] [[action.malware.name=Wiper]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Finance]] [[victim.industry.name=Retail]]

#### Location:
[[victim.country.name=Oman]] [[victim.continent.name=Asia]] [[victim.country.name=Romania]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Log4j]] [[Conti]] [[Ransomware]] [[Minecraft]] [[Log4shell]] [[Tellyouthepass]] [[Khonsari]] [[Vcenter]] [[High-profile]] [[Bleeping Computer]]

