# The Week in Ransomware - August 13th 2021 - The rise of LockBit
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/the-week-in-ransomware-august-13th-2021-the-rise-of-lockbit/)
+ Date: August 13, 2021
+ Author: Lawrence Abrams


## Article:
![Keyhole](https://www.bleepstatic.com/content/hl-images/2021/03/10/lock-keyhole.jpg)


This week we saw an existing operation rise in attacks while existing ransomware operations turn to Windows vulnerabilities to elevate their privileges.


Over the past week, we have seen increasing LockBit 2.0 ransomware operation attacks, with the [Australian government issuing an alert](https://www.bleepingcomputer.com/news/security/australian-govt-warns-of-escalating-lockbit-ransomware-attacks/).



It was also revealed that the ransomware gang pulled off a [successful attack on IT giant Accenture](https://www.bleepingcomputer.com/news/security/accenture-confirms-hack-after-lockbit-ransomware-data-leak-threats/) and began leaking their data for a short time.


We also saw [REvil's universal decryption key used in the Kaseya attack](https://www.bleepingcomputer.com/news/security/kaseyas-universal-revil-decryption-key-leaked-on-a-hacking-forum/) leaked on a hacking forum, and [ransomware gangs begin](https://www.bleepingcomputer.com/news/security/ransomware-gang-uses-printnightmare-to-breach-windows-servers/) [using the Windows PrintNightmare vulnerability](https://www.bleepingcomputer.com/news/security/vice-society-ransomware-joins-ongoing-printnightmare-attacks/) to gain elevated privileges on compromised devices.


Finally, the SynAck ransomware operation [released their master decryption keys](https://www.bleepingcomputer.com/news/security/synack-ransomware-releases-decryption-keys-after-el-cometa-rebrand/) after rebranding as the El\_Cometa group.


Contributors and those who provided new ransomware information and stories this week include: [@BleepinComputer](https://twitter.com/BleepinComputer), [@DanielGallagher](https://twitter.com/DanielGallagher), [@malwareforme](https://twitter.com/malwareforme), [@FourOctets](https://twitter.com/FourOctets), [@jorntvdw](https://twitter.com/jorntvdw), [@malwrhunterteam](https://twitter.com/malwrhunterteam), [@PolarToffee](https://twitter.com/PolarToffee), [@Ionut\_Ilascu](https://twitter.com/Ionut_Ilascu), [@LawrenceAbrams](https://twitter.com/LawrenceAbrams), [@serghei](https://twitter.com/serghei), [@VK\_Intel](https://twitter.com/VK_Intel), [@Seifreed](https://twitter.com/Seifreed), [@demonslay335](https://twitter.com/demonslay335), [@fwosar](https://twitter.com/fwosar), [@struppigel](https://twitter.com/struppigel), [@pcrisk](https://twitter.com/pcrisk), [@markloman](https://twitter.com/markloman), [@SophosLabs](https://twitter.com/SophosLabs), [@TalosSecurity](https://twitter.com/talossecurity), [@pancak3lullz](https://twitter.com/pancak3lullz), [@Unit42\_Intel](https://twitter.com/Unit42_Intel), [@LiviuArsene](https://twitter.com/LiviuArsene), [@CrowdStrike](https://twitter.com/CrowdStrike), [@PogoWasRight](https://twitter.com/PogoWasRight), [@chum1ng0](https://twitter.com/chum1ng0), [@fbgwls245](https://twitter.com/fbgwls245), and [@AuCyble](https://twitter.com/AuCyble).


August 7th 2021
---------------


### New Zeppelin ransomware variant


[dnwls0719](https://twitter.com/fbgwls245) found a new Zeppelin Ransomware variant that appends the **.payfast500**extension.


![Zeppelin](https://www.bleepstatic.com/images/news/columns/week-in-ransomware/zeppelin.jpg)


August 8th 2021
---------------


### Australian govt warns of escalating LockBit ransomware attacks


The Australian Cyber Security Centre (ACSC) warns of an increase of LockBit 2.0 ransomware attacks against Australian organizations starting July 2021.


August 9th 2021
---------------


Taiwan-based NAS maker Synology has warned customers that the StealthWorker botnet is targeting their network-attached storage devices in ongoing brute-force attacks that lead to ransomware infections.


### Microsoft adds Fusion ransomware attack detection to Azure Sentinel


Microsoft says that the Azure Sentinel cloud-native SIEM (Security Information and Event Management) platform is now able to detect potential ransomware activity using the Fusion machine learning model.


### BlackMatter ransomware emerges from the shadow of DarkSide


In late July, a new RaaS appeared on the scene. Calling itself BlackMatter, the ransomware claims to fill the void left by DarkSide and REvil – adopting the best tools and techniques from each of them, as well as from the still-active LockBit 2.0.


### New STOP ransomware variant


[PCrisk](https://twitter.com/pcrisk) found a new STOP Ransomware variant that appends the **.repg** extension.


### New Dharma ransomware variant


[PCrisk](https://twitter.com/pcrisk) found a new Dharma Ransomware variant that appends the **.JRB** extension.


August 10th 2021
----------------


### eCh0raix ransomware now targets both QNAP and Synology NAS devices


A newly discovered eCh0raix ransomware variant has added support for encrypting both QNAP and Synology Network-Attached Storage (NAS) devices.


### Crytek confirms Egregor ransomware attack, customer data theft


Game developer and publisher Crytek has confirmed that the Egregor ransomware gang breached its network in October 2020, encrypting systems and stealing files containing customers' personal info later leaked on the gang's dark web leak site.


### k-12 school districts fall prey to Pysa ransomware


As a preface, we note that Pysa are not the only ransomware threat actors attacking the k-12 sector, which has a reputation of being “low-hanging fruit” for hacks. We have also seen many other groups attacking k-12 districts. A partial listing of ransomware attacks on k-12 is embedded below this discussion of Pysa victims.


August 11th 2021
----------------


### Kaseya's universal REvil decryption key leaked on a hacking forum


The universal decryption key for REvil's attack on Kaseya's customers has been leaked on hacking forums allowing researchers their first glimpse of the mysterious key.


![Kaseya decryption key](https://www.bleepstatic.com/images/news/ransomware/r/revil/kaseya-universal-decryptor/kaseya-decryptor-screen.jpg)


### Accenture confirms hack after LockBit ransomware data leak threats


Accenture, a global IT consultancy giant has allegedly been hit by a ransomware cyberattack from the LockBit ransomware gang.


### ​BlackMatter Ransomware Attack Impacting Multiple Financial Institutions


In the course of our routine threat hunting exercise, the Cyble Research Lab discovered that Pine Labs, an Indian merchant platform company that provides financing and last-mile retail transaction technology, was impacted by a ransomware attack. Our investigation showcased that the BlackMatter ransomware group is behind the attack on Pine Labs. The group has been garnering considerable media attention because of this attack.  


### New Phobos ransomware variant


dnwls0719 found a new Phobos Ransomware variant that appends the **.HORSEMONEY** extension.


![Phobos Horsemoney](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)


August 12th 2021
----------------


### Ransomware gang uses PrintNightmare to breach Windows servers


Ransomware operators have added PrintNightmare exploits to their arsenal and are targeting Windows servers to deploy Magniber ransomware payloads.


August 13th 2021
----------------


### Vice Society ransomware joins ongoing PrintNightmare attacks


The Vice Society ransomware gang is now also actively exploiting Windows print spooler PrintNightmare vulnerability for lateral movement through their victims' networks.


### SynAck ransomware releases decryption keys after El\_Cometa rebrand


The SynAck ransomware gang released the master decryption keys for their operation after rebranding as the new El\_Cometa group.


### That's it for this week! Hope everyone has a nice weekend!




#### Tags:
[[ransomware]] [[Ransomware]] [[LockBit]] [[Windows]] [[PrintNightmare]] [[REvil]] [[extension.]] [[k-12]] [[Kaseya]] [[SynAck]] [[Bleeping Computer]]
