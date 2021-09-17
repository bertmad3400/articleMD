# The Week in Ransomware - September 17th 2021 - REvil decrypted
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/the-week-in-ransomware-september-17th-2021-revil-decrypted/)
+ Date: September 17, 2021
+ Author: Lawrence Abrams


## Article:
![Decryption key](https://www.bleepstatic.com/content/hl-images/2021/02/07/brighter-key.jpg)


It has been an interesting week with decryptors released, ransomware gangs continuing to rail against negotiators, and the US government expected to sanction crypto exchanges next week.


This week's biggest news is that soon after [REvil returned from its two-month absence](https://www.bleepingcomputer.com/news/security/revil-ransomware-is-back-in-full-attack-mode-and-leaking-data/), Bitdefender [released a master decryptor](https://www.bleepingcomputer.com/news/security/free-revil-ransomware-master-decrypter-released-for-past-victims/) that allows victims encrypted by REvil before July 13th to recover their files for free.


While the [decryptior has a few bugs](https://twitter.com/fwosar/status/1438946235436707848) that still need to be worked out that lead to corrupted data in certain situations, our decryption tests show that it works against REvil samples as far back as May 2019.


The US government is expected to disrupt further ransomware attacks by [sanctioning crypto exchanges](https://www.bleepingcomputer.com/news/security/us-to-sanction-crypto-exchanges-wallets-used-by-ransomware/), wallets, and traders that aid cybercriminals.


Finally, ransomware gangs use phishing attacks with malicious Word documents that [utilize the Windows MSHTML vulnerability](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-mshtml-bug-now-exploited-by-ransomware-gangs/) tracked as CVE-2021-40444. When opened, the malicious documents would install Cobalt Strike to provide network access to the attackers.


Finally, ransomware gangs continue to [rail against negotiators](https://www.bleepingcomputer.com/news/security/ransomware-gang-threatens-to-wipe-decryption-key-if-negotiator-hired/) in posts from both DoppelPaymer and the Grief ransomware operations, which are believed to be [run by the same threat actors](https://www.bleepingcomputer.com/news/security/doppelpaymer-ransomware-gang-rebrands-as-the-grief-group/).


Contributors and those who provided new ransomware information and stories this week include: [@demonslay335](https://twitter.com/demonslay335), [@Seifreed](https://twitter.com/Seifreed), [@DanielGallagher](https://twitter.com/DanielGallagher), [@malwrhunterteam](https://twitter.com/malwrhunterteam), [@FourOctets](https://twitter.com/FourOctets), [@malwareforme](https://twitter.com/malwareforme), [@jorntvdw](https://twitter.com/jorntvdw), [@fwosar](https://twitter.com/fwosar), [@VK\_Intel](https://twitter.com/VK_Intel), [@serghei](https://twitter.com/serghei), [@PolarToffee](https://twitter.com/PolarToffee), [@BleepinComputer](https://twitter.com/BleepinComputer), [@LawrenceAbrams](https://twitter.com/LawrenceAbrams), [@struppigel](https://twitter.com/struppigel), [@Ionut\_Ilascu](https://twitter.com/Ionut_Ilascu), [@RiskIQ](https://twitter.com/riskiq), [@sixdub](https://twitter.com/sixdub), [@Bitdefender](https://twitter.com/Bitdefender), [@zackwhittaker](https://twitter.com/zackwhittaker), [@AdvIntel](https://twitter.com/AdvIntel), [@siri\_urz](https://twitter.com/siri_urz), [@martinmatishak](https://twitter.com/martinmatishak), [@pcrisk](https://twitter.com/pcrisk), [@TheDFIRReport](https://twitter.com/TheDFIRReport), and [@PogoWasRight](https://twitter.com/PogoWasRight).


September 11th 2021
-------------------


### REvil ransomware is back in full attack mode and leaking data


The REvil ransomware gang has fully returned and is once again attacking new victims and publishing stolen files on a data leak site.


September 12th 2021
-------------------


### Missouri Delta Medical Center silent about patient data dump and claimed ransomware attack


And if they weren’t struggling enough already, it appears that Missouri Delta Medical Center (MDMC) might also be dealing with a ransomware attack by Hive threat actors. So far, however, MDMC has been tight-lipped about the claimed attack and has not responded to inquiries asking them to confirm or deny the claim.


September 13th 2021
-------------------


### BlackMatter ransomware hits medical technology giant Olympus


Olympus, a leading medical technology company, is investigating a "potential cybersecurity incident" that impacted some of its EMEA (Europe, Middle East, Africa) IT systems last week.


### BazarLoader to Conti Ransomware in 32 Hours


In July we witnessed a BazarLoader campaign that deployed Cobalt Strike and ended with domain wide encryption using Conti ransomware.


### New STOP ransomware variant


[PCrisk](https://twitter.com/pcrisk) found a new STOP ransomware variant that appends the **.wiot** extension.


### New JamesBond Ransomware


PCrisk found the new JamesBond Ransomware that appends the **.jamesbond2021[@]tutanotacom\_jamesbond** extension and drops a ransom note named **read\_it.txt**.


### New Dharma Ransomware


PCrisk found a new Dharma variant that appends the **.yUixN** extension.


September 14th 2021
-------------------


### ‘No indication’ Russia has cracked down on ransomware gangs, top FBI official says


The FBI’s No. 2 on Tuesday said the agency has seen no evidence that the Russian government has moved against ransomware gangs operating on its soil.


### New Atom Slio ransomware variant


[S!Ri](https://twitter.com/siri_urz) found a new ransomware variant called Atom Slio that appends the **.ATOMSILO** extension to encrypted files.


![Atom Silo](https://www.bleepstatic.com/images/news/columns/week-in-ransomware/2021/september/atom-silo.jpg)


September 15th 2021
-------------------


### Ransomware gang threatens to wipe decryption key if negotiator hired


The Grief ransomware gang is threatening to delete victim's data if they hire a negotiation firm, making it impossible to recover encrypted files.


### "Russian hacker" confirmed the resurrection of the most famous Russian group


A "Russian hacker" who collaborated with the well-known REvil group confirmed to Lente.ru that cybercriminals returned to active activity after a two-month break. He named political reasons as the main reason for their withdrawal into the shadows. This refutes the claims of the REvil members themselves, who explained the short-term simple precautions following the disappearance of one of the community members.


September 16th 2021
-------------------


### Free REvil ransomware master decrypter released for past victims


A free master decryptor for the REvil ransomware operation has been released, allowing all victims encrypted before the gang disappeared to recover their files for free.


### Microsoft: Windows MSHTML bug now exploited by ransomware gangs


Microsoft says multiple threat actors, including ransomware affiliates, are targeting the recently patched Windows MSHTML remote code execution security flaw.


September 17th 2021
-------------------


### U.S. to sanction crypto exchanges, wallets used by ransomware


The Biden administration is expected to issue sanctions against crypto exchanges, wallets, and traders used by ransomware gangs to convert ransom payments into fiat money.


### That's it for this week! Hope everyone has a nice weekend!




#### Tags:
[[ransomware]] [[REvil]] [[Ransomware]] [[exchanges,]] [[Windows]] [[MSHTML]] [[PCrisk]] [[Bleeping Computer]]
