# The Week in Ransomware - September 3rd 2021 - Targeting Exchange
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/the-week-in-ransomware-september-3rd-2021-targeting-exchange/)
+ Date: September 3, 2021
+ Author: Lawrence Abrams


## Article:
![Ransomware](https://www.bleepstatic.com/content/hl-images/2020/11/03/Ransomware.jpg)


Over the past two weeks, it has been busy with ransomware news ranging from a gang shutting down and releasing a master decryption key to threat actors turning to Microsoft Exchange exploits to breach networks.


The biggest news is the [Ragnarok ransomware operation shutting down](https://www.bleepingcomputer.com/news/security/ragnarok-ransomware-releases-master-decryptor-after-shutdown/) and releasing a master decryptor on their site. Using the released keys, Emsisoft was able to [create its own decryptor](https://www.emsisoft.com/ransomware-decryption-tools/ragnarok).


We have also seen ransomware gangs, such as [LockFile](https://www.bleepingcomputer.com/news/security/microsoft-exchange-servers-being-hacked-by-new-lockfile-ransomware/) and [Conti](https://www.bleepingcomputer.com/news/security/conti-ransomware-now-hacking-exchange-servers-with-proxyshell-exploits/), begin to use the recently disclosed [Microsoft Exchange ProxyShell vulnerabilities](https://www.bleepingcomputer.com/news/microsoft/microsoft-exchange-servers-are-getting-hacked-via-proxyshell-exploits/).


The FBI and CISA have also been busy, releasing advisories warning of [ransomware attacks over holiday weekends](https://www.bleepingcomputer.com/news/security/fbi-cisa-ransomware-attack-risk-increases-on-holidays-weekends/), [gangs targeting food and agriculture organizations](https://www.bleepingcomputer.com/news/security/fbi-warns-of-ransomware-gangs-targeting-food-agriculture-orgs/), [information about the 1% group](https://www.bleepingcomputer.com/news/security/fbi-onepercent-group-ransomware-targeted-us-orgs-since-nov-2020/), and [IOCs for the Hive Ransomware](https://www.bleepingcomputer.com/news/security/fbi-shares-technical-details-for-hive-ransomware/).


A threat actor [released the complete source code for the Babuk Ransomware](https://www.bleepingcomputer.com/news/security/babuk-ransomwares-full-source-code-leaked-on-hacker-forum/), allowing any wannabe threat actor to start their own ransomware operation. Unfortunately, this leak will lead to many threat actors worldwide creating their own Ransomware-as-a-Service.


Finally, [leaked Conti training material](https://www.bleepingcomputer.com/news/security/translated-conti-ransomware-playbook-gives-insight-into-attacks/) and a [Pysa data exfiltration script](https://www.bleepingcomputer.com/news/security/ransomware-gangs-script-shows-exactly-the-files-theyre-after/) have given us insight into how ransomware gangs conduct their attacks and what data they are targeting.


Contributors and those who provided new ransomware information and stories this week include: [@VK\_Intel](https://twitter.com/VK_Intel), [@fwosar](https://twitter.com/fwosar), [@struppigel](https://twitter.com/struppigel), [@malwrhunterteam](https://twitter.com/malwrhunterteam), [@PolarToffee](https://twitter.com/PolarToffee), [@Ionut\_Ilascu](https://twitter.com/Ionut_Ilascu), [@BleepinComputer](https://twitter.com/BleepinComputer), [@demonslay335](https://twitter.com/demonslay335), [@LawrenceAbrams](https://twitter.com/LawrenceAbrams), [@jorntvdw](https://twitter.com/jorntvdw), [@FourOctets](https://twitter.com/FourOctets), [@DanielGallagher](https://twitter.com/DanielGallagher), [@Seifreed](https://twitter.com/Seifreed), [@serghei](https://twitter.com/serghei), [@malwareforme](https://twitter.com/malwareforme), [@vxunderground](https://twitter.com/vxunderground), [@AltShiftPrtScn](https://twitter.com/AltShiftPrtScn), [@thepacketrat](https://twitter.com/thepacketrat), [@TalosSecurity](https://twitter.com/talossecurity), [@GossiTheDog](https://twitter.com/GossiTheDog), [@pcrisk](https://twitter.com/pcrisk), [@fbgwls245](https://twitter.com/fbgwls245), [@ddd1ms](https://twitter.com/ddd1ms), and [@darktracer\_int](https://twitter.com/darktracer_int).


August 21st 2021
----------------


### Microsoft Exchange servers being hacked by new LockFile ransomware


A new ransomware gang known as LockFile encrypts Windows domains after hacking into Microsoft Exchange servers using the recently disclosed ProxyShell vulnerabilities.


August 23rd 2021
----------------


### FBI: OnePercent Group Ransomware targeted US orgs since Nov 2020


The Federal Bureau of Investigation (FBI) has shared info about a threat actor known as OnePercent Group that has been actively targeting US organizations in ransomware attacks since at least November 2020.


### Nokia subsidiary discloses data breach after Conti ransomware attack


SAC Wireless, a US-based Nokia subsidiary, has disclosed a data breach following a ransomware attack where Conti operators were able to successfully breach its network, steal data, and encrypt systems.


### New STOP ransomware variant


[PCRisk](https://twitter.com/pcrisk) found a new STOP ransomware variant that appends the **.orkf** extension.


### New Dharma ransomware variant


PCRisk found a new Dharma ransomware variant that appends the **.dts** extension.


August 24th 2021
----------------


### Ransomware gang's script shows exactly the files they're after


A PowerShell script used by the Pysa ransomware operation gives us a sneak peek at the types of data they attempt to steal during a cyberattack.


### New BlackKingdom ransomware variant


[dnwls0719](https://twitter.com/fbgwls245) found a BlackKingdom variant that appends the **.svyx** extension.


![Black Kingdom](https://www.bleepstatic.com/images/news/columns/week-in-ransomware/2021/september/3/black-kingdom.jpg)


August 26th 2021
----------------


### Ragnarok ransomware releases master decryptor after shutdown


Ragnarok ransomware gang appears to have called it quits and released the master key that can decrypt files locked with their malware.


### FBI shares technical details for Hive ransomware


The Federal Bureau of Investigation (FBI) has released some technical details and indicators of compromise associated with Hive ransomware attacks.


### New Dharma ransomware variants


PCRisk found new Dharma ransomware variants that appends the **.6ix9**and **.TCYO** extensions.


### New Phobos ransomware variant


PCRisk found a new Phobos ransomware variant that appends the **.PERDAK** extension.


August 27th 2021
----------------


### Boston Public Library discloses cyberattack, system-wide technical outage


The Boston Public Library (BPL) has disclosed today that its network was hit by a cyberattack on Wednesday, leading to a system-wide technical outage.


### New Dharma ransomware variant


PCRisk found a new Dharma ransomware variant that appends the **.RZA** extension.


### New HQ\_52\_42 ransomware


dnwls0719 found a new ransomware called HQ\_52\_42 that appends the **.HQ\_52\_42** extension.


![HQ_52_42](https://www.bleepstatic.com/images/news/columns/week-in-ransomware/2021/september/3/HQ_52_42.jpg)


August 28th 2021
----------------


### New SanwaiWare 2021 ransomware


dnwls0719 found a new ransomware called SanwaiWare 2021 that appends the **.sanwai** extension.


![SanwaiWare 2021](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)


August 30th 2021
----------------


### New STOP ransomware variant


PCRisk found a new STOP ransomware variant that appends the **.lqqw** extension.


New Loki Locker ransomware
--------------------------


[dnwls0719](https://twitter.com/fbgwls245) found a new ransomware called Loki Locker that appends the **.Loki** extension.


![Loki Locker](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)


August 31st 2021
----------------


### FBI, CISA: Ransomware attack risk increases on holidays, weekends


The FBI and CISA urged organizations not to let down their defenses against ransomware attacks during weekends or holidays in a joint cybersecurity advisory issued earlier today.


September 1st 2021
------------------


### LockBit gang leaks Bangkok Airways data, hits Accenture customers


Bangkok Airways, a major airline company in Thailand, confirmed it was the victim of a cyberattack earlier this month that compromised personal data of passengers.


### BlackMatter x Babuk : Using the same web server for sharing leaked files


In this post, we mentioned the fact of BlackMatter and Babuk using the same web server for sharing the leaked files.


September 2nd 2021
------------------


### Translated Conti ransomware playbook gives insight into attacks


Almost a month after a disgruntled [Conti affiliate leaked](https://www.bleepingcomputer.com/news/security/angry-conti-ransomware-affiliate-leaks-gangs-attack-playbook/) the gang’s attack playbook, security researchers shared a translated variant that clarifies any misinterpretation caused by automated translation.


### FBI warns of ransomware gangs targeting food, agriculture orgs


The FBI says ransomware gangs are actively targeting and disrupting the operations of organizations in the food and agriculture sector, causing financial loss and directly affecting the food supply chain.


September 3rd 2021
------------------


### Conti ransomware now hacking Exchange servers with ProxyShell exploits


The Conti ransomware gang is hacking into Microsoft Exchange servers and breaching corporate networks using recently disclosed ProxyShell vulnerability exploits.


### Babuk ransomware's full source code leaked on hacker forum


A threat actor has leaked the complete source code for the Babuk ransomware on a Russian-speaking hacking forum.


### Babuk, BlackMatter, and Groove share the same data leak site


[DarkTracer](https://twitter.com/darktracer_int) found that all three ransomware groups are utilizing the same Tor data leak site. They are not believed to be affiliated, other than possible being part of the same cartel.


### Mount Locker, Astro Team, and XING Locker share same Tor site


DarkTracer found that Astro Team, Mount Locker, and XING Locker are sharing the same Tor network infrastructure. Astro Team and MountLocker are believed to be [affiliated with each other](https://www.bleepingcomputer.com/news/security/mountlocker-ransomware-uses-windows-api-to-worm-through-networks/).


Get ready for new ransomware variants based on Babuk
----------------------------------------------------


[Dmitry Smilyanets](https://twitter.com/ddd1ms) noted that threat actors worldwide will likely launch their own ransomware operations based on the [leaked Babuk ransomware source code](https://www.bleepingcomputer.com/news/security/babuk-ransomwares-full-source-code-leaked-on-hacker-forum/).


### New STOP ransomware variant


PCRisk found a new STOP ransomware variant that appends the **.efdc** extension.


### That's it for this week! Hope everyone has a nice weekend!




#### Tags:
[[ransomware]] [[extension.]] [[Babuk]] [[Conti]] [[PCRisk]] [[Microsoft]] [[ProxyShell]] [[dnwls0719]] [[LockFile]] [[Ransomware]] [[Bleeping Computer]]
