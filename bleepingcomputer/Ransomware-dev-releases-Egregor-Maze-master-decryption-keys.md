# Ransomware dev releases Egregor, Maze master decryption keys
### The master decryption keys for the Maze, Egregor, and Sekhmet ransomware operations were released last night on the BleepingComputer forums by the alleged malware developer.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/ransomware-dev-releases-egregor-maze-master-decryption-keys/
+ Date: 2022-02-09T10:26:31-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/02/09/Maze.jpg)

![Maze ransomware](https://www.bleepstatic.com/content/hl-images/2022/02/09/Maze.jpg)


The master decryption keys for the Maze, Egregor, and Sekhmet ransomware operations were released last night on the BleepingComputer forums by the alleged malware developer.


The [Maze ransomware began operating in May 2019](https://www.bleepingcomputer.com/news/security/maze-ransomware-says-computer-type-determines-ransom-amount/) and quickly rose to fame as they were [responsible for the use of data theft and double-extortion tactics](https://www.bleepingcomputer.com/news/security/allied-universal-breached-by-maze-ransomware-stolen-data-leaked/) now used by many ransomware operations.


After [Maze announced its shutdown](https://www.bleepingcomputer.com/news/security/maze-ransomware-is-shutting-down-its-cybercrime-operation/) in October 2020, they [rebranded in September as Egregor](https://www.bleepingcomputer.com/news/security/crytek-hit-by-egregor-ransomware-ubisoft-data-leaked/), who later disappeared after [members were arrested in Ukraine](http://law%20enforcement%20operations./).


The Sekhmet operation was somewhat of an outlier as it launched in March 2020, while Maze was still active.


Master decryption keys released
-------------------------------


Fast forward 14 months later, and the decryption keys for these operations have now been [leaked in the BleepingComputer forums](https://www.bleepingcomputer.com/forums/t/768330/leak-maze-egregor-sekhmet-keys-along-with-m0yv-expiro-source-code/) by a user named 'Topleak' who claims to be the developer for all three operations.


The poster said that this was a planned leak and is not related to recent law enforcement operations that have led to the [seizing of servers](https://www.bleepingcomputer.com/news/security/revil-ransomware-shuts-down-again-after-tor-sites-were-hijacked/) and the [arrests of ransomware affiliates](https://www.bleepingcomputer.com/news/security/russia-arrests-revil-ransomware-gang-members-seize-66-million/).


"Since it will raise too much clues and most of them will be false, it is necessary to emphasize that it is planned leak, and have no any connections to recent arrests and takedowns," explained the alleged ransomware developer.


They further stated that none of their team members will ever return to ransomware and that they destroyed all of the source code for their ransomware.



![Forum post leaking Maze, Egregor, and Sekhmet decryption keys](https://www.bleepstatic.com/images/news/ransomware/m/maze/master-decryption-keys/topleak-forum-post.jpg)**Forum post leaking Maze, Egregor, and Sekhmet decryption keys**  
*Source: BleepingComputer*
The post includes a download link for a 7zip file with four archives containing the Maze, Egregor, and Sekhmet decryption keys, and the source code for a 'M0yv' malware used by the ransomware gang.



![](https://www.bleepstatic.com/images/news/ransomware/m/maze/master-decryption-keys/archive.jpg)**Archive containing the leaked decryption keys**  
*Source: BleepingComputer*
Each of these archives contains the public master encryption key and the private master decryption key associated with a specific "advert", or affiliate of the ransomware operation.


In total, the following are the number of RSA-2048 master decryption keys released per ransomware operation:


* **Maze:** 9 master decryption keys for the original malware that targeted non-corporate users.
* **Maze:** 30 master decryption keys.
* **Egregor:** 19 master decryption keys.
* **Sekhmet**: 1 master decryption key.

Emsisoft's [Michael Gillespie](https://twitter.com/demonslay335) and [Fabian Wosar](https://twitter.com/fwosar) has reviewed the decryption keys and confirmed to BleepingComputer that they are legitimate and can be used to decrypt files encrypted by the three ransomware families.


Gillespie told us that the keys are used to decrypt a victim's encrypted keys that are embedded in a ransom note. Due to this, victims will need the ransom note created during the attack to use Emsisoft's decryptor.



![Encrypted key in Maze ransom note](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Encrypted key in Maze ransom note**  
*Source: BleepingComputer*
Emsisoft has [released a decryptor](https://www.emsisoft.com/ransomware-decryption-tools/maze-sekhmet-egregor) to allow any Maze, Egregor, and Sekhmet victims who have been waiting to recover their files for free.


Bonus M0yv malware source code
------------------------------


The archive also includes the source code for the M0yv 'modular x86/x64 file infector' developed by the Maze ransomware operation and used previously in attacks.


"Also there is a little bit harmless source code of polymorphic x86/x64 modular EPO file infector m0yv detected in the wild as Win64/Expiro virus, but it is not expiro actually, but AV engines detect it like this, so no single thing in common with gazavat," the ransomware developer said in the forum post.


"M0yv source is a bonus, because there was no any major source code of resident software for years now, so here we go," the developer later explained.


This source code come in the form of a Microsoft Visual Studio project and includes some already compiled DLLs.



![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Source code snippet for the M0yv malware**  
*Source: BleepingComputer*
The todo.txt file indicates the source code for this malware was last updated on January 19th, 2022.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Egregor]] [[action.malware.name=Maze]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Ukraine]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Bleepingcomputer]] [[Egregor]] [[Sekhmet]] [[Malware]] [[Emsisoft]] [[M0yv]] [[Bleeping Computer]]

