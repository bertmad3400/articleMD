# The Week in Ransomware - January 28th 2022 - Get NAS devices off the Internet
### It's been a busy week with ransomware attacks tied to political protests, new attacks on NAS devices, amazing research released about tactics, REvil's history, and more.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/the-week-in-ransomware-january-28th-2022-get-nas-devices-off-the-internet/
+ Date: 2022-01-28T16:57:32-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2020/09/24/padlock.jpg)

![Lock](https://www.bleepstatic.com/content/hl-images/2020/09/24/padlock.jpg)


It's been a busy week with ransomware attacks tied to political protests, new attacks on NAS devices, amazing research released about tactics, REvil's history, and more.


This week's biggest news is about a new ransomware operation called DeadBolt encrypted QNAP devices worldwide, illustrating how threat actors can still earn a lot of money by targeting consumers and small businesses.


The [attacks started on January 25th](https://www.bleepingcomputer.com/news/security/new-deadbolt-ransomware-targets-qnap-devices-asks-50-btc-for-master-key/) and have since encrypted over [4,300 QNAP NAS devices](https://t.co/uZKLQprSDE) where they demand 0.03 bitcoins, worth approximately $1,100, for a decryption key.


Unfortunately, many victims have reported paying, leading this attack to be very successful for the threat actors.


Other attacks this week include a [Conti attack on Apple and Tesla contractor Delta](https://www.bleepingcomputer.com/news/security/taiwanese-apple-and-tesla-contractor-hit-by-conti-ransomware/) and an [attack on Belarusian Railway](https://www.bleepingcomputer.com/news/security/hackers-say-they-encrypted-belarusian-railway-servers-in-protest/) in protest of Russia using Belarusian Railway's rail transport network to move military units and equipment into the country.


Other interesting stories this week are [ransomware gangs calling people](https://www.nbcnews.com/tech/security/ransomware-hackers-new-tactic-calling-directly-rcna6466) whose data was stolen, an [increase in attempts to recruit insiders](https://www.bleepingcomputer.com/news/security/ransomware-gangs-increase-efforts-to-enlist-insiders-for-attacks/), the analysis of [LockBit's ESXI encryptor](https://www.bleepingcomputer.com/news/security/linux-version-of-lockbit-ransomware-targets-vmware-esxi-servers/), and a fantastic report detailing the [history of REvil](https://analyst1.com/file-assets/History-of-REvil.pdf).


Contributors and those who provided new ransomware information and stories this week include: [@PolarToffee](https://twitter.com/PolarToffee), [@Ionut\_Ilascu](https://twitter.com/Ionut_Ilascu), [@demonslay335](https://twitter.com/demonslay335), [@BleepinComputer](https://twitter.com/BleepinComputer), [@VK\_Intel](https://twitter.com/VK_Intel), [@malwareforme](https://twitter.com/malwareforme), [@struppigel](https://twitter.com/struppigel), [@fwosar](https://twitter.com/fwosar), [@FourOctets](https://twitter.com/FourOctets), [@billtoulas](https://twitter.com/billtoulas), [@Seifreed](https://twitter.com/Seifreed), [@malwrhunterteam](https://twitter.com/malwrhunterteam), [@jorntvdw](https://twitter.com/jorntvdw), [@DanielGallagher](https://twitter.com/DanielGallagher), [@LawrenceAbrams](https://twitter.com/LawrenceAbrams), [@serghei](https://twitter.com/serghei), [@kevincollier](https://twitter.com/kevincollier), [@Jon\_\_DiMaggio](https://twitter.com/Jon__DiMaggio), [@UseAnalyst1](https://twitter.com/UseAnalyst1), [@fbgwls245](https://twitter.com/fbgwls245), [@JakubKroustek](https://twitter.com/JakubKroustek), [@pcrisk](https://twitter.com/pcrisk), [@TrendMicro](https://twitter.com/trendmicro), [@Hitachi\_ID](https://twitter.com/hitachi_id), [@emsisoft](https://twitter.com/emsisoft), [@BushidoToken](https://twitter.com/BushidoToken), [@SteveD3](https://twitter.com/steved3), [@SttyK](https://twitter.com/SttyK), [@CuratedIntel](https://twitter.com/CuratedIntel), and [@vinopaljiri](https://twitter.com/vinopaljiri).


January 22nd 2022
-----------------


### [New Paradise ransomware variant](https://twitter.com/fbgwls245/status/1484897702773026821)


[dnwls0719](https://twitter.com/fbgwls245) found a new Paradise .NET variant that appends the **.iskaluz** extension to encrypted files.


January 24th 2022
-----------------


### [Ransomware gangs increase efforts to enlist insiders for attacks](https://www.bleepingcomputer.com/news/security/ransomware-gangs-increase-efforts-to-enlist-insiders-for-attacks/)


A recent survey of 100 large (over 5,000 employees) North American IT firms shows that ransomware actors are making greater effort to recruit insiders in targeted firms to aid in attacks.


### [Hackers say they encrypted Belarusian Railway servers in protest](https://www.bleepingcomputer.com/news/security/hackers-say-they-encrypted-belarusian-railway-servers-in-protest/)


A group of hackers (known as Belarusian Cyber-Partisans) claim they breached and encrypted servers belonging to the Belarusian Railway, Belarus's national state-owned railway company.


### [New STOP Ransomware variant](https://twitter.com/JakubKroustek/status/1485715665256435718)


[Jakub Kroustek](https://twitter.com/JakubKroustek) found a new STOP ransomware variant that appends the **.qqqw** extension.


January 25th 2022
-----------------


### [New DeadBolt ransomware targets QNAP devices, asks 50 BTC for master key](https://www.bleepingcomputer.com/news/security/new-deadbolt-ransomware-targets-qnap-devices-asks-50-btc-for-master-key/)


A new DeadBolt ransomware group is encrypting QNAP NAS devices worldwide using what they claim is a zero-day vulnerability in the device's software.


### [Ransomware hackers' new tactic: Calling you directly](https://www.nbcnews.com/tech/security/ransomware-hackers-new-tactic-calling-directly-rcna6466)


Wayne didn’t know his son’s school district had been hacked — its files stolen and computers locked up and held for ransom — until last fall when the hackers started emailing him directly with garbled threats.


### [Hacktivist group shares details related to Belarusian Railways hack](https://www.curatedintel.org/2022/01/hacktivist-group-shares-details-related.html)


The Belarusian Cyber Partisans have shared documents related to another hack, and explained that Curated Intel member, SttyK, would “understand some of the methods used.”


### [New ransomware appends 'exploit'](https://twitter.com/fbgwls245/status/1485973082095321091)


dnwls0719 found a new ransomware appending the .exploit extension to encrypted files.


![Exploit ransomware](https://www.bleepstatic.com/images/news/columns/week-in-ransomware/2022/january/28/exploit-ransomware.jpg)


January 26th 2022
-----------------


### [QNAP warns of new DeadBolt ransomware encrypting NAS devices](https://www.bleepingcomputer.com/news/security/qnap-warns-of-new-deadbolt-ransomware-encrypting-nas-devices/)


QNAP is warning customers again to secure their Internet-exposed Network Attached Storage (NAS) devices to defend against ongoing and widespread attacks targeting their data with the new DeadBolt ransomware strain.


### [Linux version of LockBit ransomware targets VMware ESXi servers](https://www.bleepingcomputer.com/news/security/linux-version-of-lockbit-ransomware-targets-vmware-esxi-servers/)


LockBit is the latest ransomware gang whose Linux encryptor has been discovered to be focusing on the encryption of VMware ESXi virtual machines.


### [New Babuk knockoff ransomware variant](https://twitter.com/fbgwls245/status/1486468803990986752)


dnwls0719 found a new Babuk knockoff appending the **.king** extension to encrypted files.


January 27th 2022
-----------------


### [Taiwanese Apple and Tesla contractor hit by Conti ransomware](https://www.bleepingcomputer.com/news/security/taiwanese-apple-and-tesla-contractor-hit-by-conti-ransomware/)


Delta Electronics, a Taiwanese electronics company and a provider for Apple, Tesla, HP, and Dell, disclosed that it was the victim of a cyberattack discovered on Friday morning.


### [A history of REvil](https://analyst1.com/file-assets/History-of-REvil.pdf)


In our previous research we investigated a ransom cartel, and then we conducted a study on ransomware gangs and their links to Russian intelligence organizations. Now, we are conducting a use case into one of the world’s most notorious ransomware gangs, REvil. This particular case is fascinating because the gang has existed for several years, conducted many high-profile attacks, inspired several spin-off gangs, and in the end, caused major turmoil among partnering hackers who supported them.


### [New MedusaLocker variant](https://twitter.com/fbgwls245/status/1486903692842311685)


dnwls0719 found a new MeduaLocker ransomware variant that appends the **.farattack** extension to encrypted files.


January 28th 2022
-----------------


### [QNAP force-installs update after DeadBolt ransomware hits 3,600 devices](https://www.bleepingcomputer.com/news/security/qnap-force-installs-update-after-deadbolt-ransomware-hits-3-600-devices/)


QNAP force-updated customer's Network Attached Storage (NAS) devices with firmware containing the latest security updates to protect against the DeadBolt ransomware, which has already encrypted over 3,600 devices.


### [Emsisoft releases a decryption tool for DeadBolt](https://twitter.com/emsisoft/status/1487121808406953985)


Emsisoft has released a decryption tool for DeadBolt, but users will still need to obtain a decryption key by paying the ransom.


### [New STOP ransomware variants](https://twitter.com/pcrisk/status/1486940888618123264)


[PCrisk](https://twitter.com/pcrisk) found two new STOP ransomware variants that append the **.qqqe** or **.yoqs** extensions.


### [Thanos builder used to create new ransomware](https://twitter.com/vinopaljiri/status/1487095501799538695)


[Jirí Vinopal](https://twitter.com/vinopaljiri) found a new ransomware that was created by the Thanos builder that appends the **.NARUMI** extension.


### That's it for this week! Hope everyone has a nice weekend!





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Babuk]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=REvil]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]]

#### Location:
[[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Taiwan]] [[victim.continent.name=Asia]] [[victim.country.name=Belarus]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Deadbolt]] [[Qnap]] [[Belarusian]] [[Nas]] [[Revil]] [[Dnwls0719]] [[Lockbit]] [[Ransomware]] [[Bleeping Computer]]

