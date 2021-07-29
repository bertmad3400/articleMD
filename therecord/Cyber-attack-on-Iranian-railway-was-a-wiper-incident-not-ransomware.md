# Cyber-attack on Iranian railway was a wiper incident, not ransomware
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/cyber-attack-on-iranian-railway-was-a-wiper-incident-not-ransomware/)
+ Date: July 29, 2021
+ Author: Catalin Cimpanu


## Article:
![Cyber-attack on Iranian railway was a wiper incident, not ransomware](https://therecord.media/wp-content/uploads/2021/07/meteor-wiper.jpg)

* Unidentified hackers deployed never-before-seen wiper against Iran's railway system.
* The new malware, named Meteor, appears to have been assembled months before the attack.
* Code analysis by SentinelOne suggests the malware is both clunky and advanced at the same time.


The [cyber-attack that paralyzed Iran’s national railway system](https://therecord.media/cyber-attack-disrupts-irans-national-railway-system/) at the start of the month was caused by a disk-wiping malware strain named **Meteor** and not by a ransomware attack, according to research published by security firms [Amnpardaz](https://threats.amnpardaz.com/malware/trojan-win32-breakwin/) and [SentinelOne](https://s1.ai/meteor), which managed to obtain a copy of the malware.


Juan Andres Guerrero-Saade, Principal Threat Researcher at SentinelOne, said this is the first known incident where this malware was deployed.


Guerrero-Saade, who has a long history of tracking advanced persistent threat actors, said they have not yet been able to link Meteor to a previously known entity.


### Meteor malware part of a well-orchestrated attack


According to the company’s analysis, the Meteor wiper was just one of three parts of a larger malware arsenal deployed on the computers of the Iranian railway company on July 9.


The attacks, which SentinelOne tracked under the codename of MeteorExpress, and led to trains being canceled or delayed across Iran, involved:


* **Meteor**– malware that wiped the infected computer’s filesystem.
* A file named **mssetup.exe** that played the role of an old-school screenlocker to lock the user out of their PC.
* And a file named **nti.exe** that rewrote the victim computer’s master boot record (MBR).


Information on how the attack started or where it originated was not available, but Guerrero-Saade said that once inside a network, the attackers used group policies to deploy their malware, delete shadow volume copies to prevent data recovery, and disconnected infected hosts from their local domain controller, to prevent sysadmins from quickly remediating infected systems.


![Meteor-components](https://www-therecord.recfut.com/wp-content/uploads/2021/07/Meteor-components-1024x620.png)Image: SentinelOne
Once the attack was over, infected computers had their filesystem wiped, and their screens showed a message telling victims to call a phone number that belonged to the office of Supreme Leader Ayatollah Ali Khamenei, all as a joke from the attackers’ point of view.


![locked-PC](https://www-therecord.recfut.com/wp-content/uploads/2021/07/locked-PC.jpg)Image via @zero\_0\_days/Twitter
But while the MeteorExpress campaign and wiper attacks looked like a clever prank aimed at Iranian government officials, the malware used was not.


Meteor and all of the other components used in the MeteorExpress attacks contained what Guerrero-Saade described as “a bizarre amalgam of custom code” that mixed open-source components with ancient software and custom-written parts that were “rife with sanity checks, error checking, and redundancy in accomplishing its goals.”


Some parts of the Meteor code contained the same functionality found in the screen-locking component or the adjacent deployment batch scripts.


“Even their batch scripts include extensive error checking, a feature seldom encountered with deployment scripts,” the SentinelOne researcher said.


However, Guerrero-Saade also points out that while some parts of the malware appeared to have been written by an experienced and professional developer, the disorganized nature of the MeteorExpress attack might suggest the malware and the entire operation might have been put together in a hurry by multiple teams.



> The attacker is an intermediate level player whose different operational components sharply oscillate from clunky and rudimentary to slick and well-developed. […] We see an adversary that doesn’t yet have a handle on their deployment pipeline, using a sample of their malware that contains extensive debug features and burning functionality irrelevant to this particular operation. There’s feature redundancy between different attack components that suggests an uncoordinated division of responsibilities across teams. And files are dispensed in a clunky, verbose, and disorganized manner unbecoming of advanced attackers.
> 
> Juan Andres Guerrero-Saade, Principal Threat Researcher at SentinelOne


Compiled just six months before the attack on the Iranian railway system, SentinelOne said it is unclear if Meteor was put together just for this operation or if we’ll see the malware strain in a new form in the future.





#### Tags:
[[malware]] [[SentinelOne]] [[Guerrero-Saade,]] [[Guerrero-Saade]] [[MeteorExpress]] [[The Record]]
