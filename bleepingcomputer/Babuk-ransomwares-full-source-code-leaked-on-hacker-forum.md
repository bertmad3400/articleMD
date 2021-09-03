# Babuk ransomware's full source code leaked on hacker forum
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/babuk-ransomwares-full-source-code-leaked-on-hacker-forum/)
+ Date: September 3, 2021
+ Author: Lawrence Abrams


## Article:
![Person in purge mask](https://www.bleepstatic.com/content/hl-images/2021/09/03/threat-actor.jpg)


A threat actor has leaked the complete source code for the Babuk ransomware on a Russian-speaking hacking forum.


Babuk Locker, also known internally as Babyk, is a ransomware operation [launched at the beginning of 2021](https://www.bleepingcomputer.com/news/security/babuk-locker-is-the-first-new-enterprise-ransomware-of-2021/) when it began targeting businesses to steal and encrypt their data in double-extortion attacks.


After [attacking the Washinton DC's Metropolitan Police Department](https://www.bleepingcomputer.com/news/security/dc-police-confirms-cyberattack-after-ransomware-gang-leaks-data/) (MPD) and feeling the heat from U.S. law enforcement, the ransomware gang claimed to have shut down their operation.


However, members of the same group splintered off to relaunch the ransomware as Babuk V2, where they continue to encrypt victims to this day.


Source code released on a hacking forum
---------------------------------------


As first noticed by security researcher [vx-underground](https://twitter.com/vxunderground), an alleged member of the Babuk group released the full source code for their ransomware on a popular Russian-speaking hacking forum.


This member claimed to be suffering from terminal cancer and decided to release the source code while they have to "live like a human."



![A translated forum post on a hacking forum](https://www.bleepstatic.com/images/news/ransomware/b/babuk-locker/leaked-source-code/english-forum-post-r.jpg)**A translated forum post on a hacking forum**

![Original post in Russian](https://www.bleepstatic.com/images/news/ransomware/b/babuk-locker/leaked-source-code/forum-post.jpg)**Original post in Russian**
As the leak contains everything a threat actor needs to create a functional ransomware executable, BleepingComputer has redacted the links to the source code.


The shared file contains different Visual Studio Babuk ransomware projects for VMware ESXi, NAS, and Windows encryptors, as shown below.



![ESXi, NAS, and Windows Babuk ransomware source code](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**ESXi, NAS, and Windows Babuk ransomware source code**
The Windows folder contains the complete source code for the Windows encryptor, decryptor, and what appears to be a private and public key generator.



![Babuk Windows encryptor source code](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Babuk Windows encryptor source code**
For example, the source code for the encryption routine in the Windows encryptor can be seen  below.



![Babuk encryption routine source code](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Babuk encryption routine source code**
Emsisoft CTO and ransomware expert [Fabian Wosar](https://twitter.com/fwosar) told BleepingComputer that the leak appears legitimate and may also contain some decryption keys for past victims.


Babuk ransomware uses elliptic-curve cryptography (ECC) as part of its encryption routine. Included in the leak are folders containing encryptors and decryptors compiled for specific victims of the ransomware gang.


Wosar told BleepingComputer that these folders also contain curve files that could be the ECC decryption keys for these victims, but this has not been confirmed yet.



![ECC curve file for Babuk victim](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**ECC curve file for Babuk victim**
In total, there are 15 folders with curve files containing possible decryption keys.


Of tales of betrayal and backstabbing
-------------------------------------


Babuk Locker has a sordid and public history involving betrayal and backstabbing that led to the group splintering.


BleepingComputer has learned from one of the Babuk ransomware gang members that the group splintered after the [attack on the Washinton DC's Metropolitan Police Department](https://www.bleepingcomputer.com/news/security/dc-police-confirms-cyberattack-after-ransomware-gang-leaks-data/) (MPD).


After the attack, the 'Admin' allegedly wanted to leak the MPD data for publicity, while the other gang members were against it. 



> 
> **"We're not good guys, but even for us it was too much. )" - Babuk threat actor**
> 
> 
> 


After the data leak, the group splintered with the original Admin forming the Ramp cybercrime forum and the rest launching Babuk V2, where they continue to perform ransomware attacks.


Soon after the Admin launched the Ramp cybercrime forum, it suffered a series of DDoS attacks to make the new site unusable. The Admin blamed his former partners for these attacks, while the Babuk V2 team told BleepingComputer that they were not responsible.


"We completely forgot about the old Admin. We are not interested in his forum," the threat actors told BleepingComputer.


To add to the group's controversy, a [Babuk ransomware builder was leaked](https://www.bleepingcomputer.com/news/security/leaked-babuk-locker-ransomware-builder-used-in-new-attacks/) on a file-sharing site and was used by another group to launch their own ransomware operation.


It appears that Babuk is not alone with stories of backstabbing and betrayals.


After Wosar setup up a Jabber account for threat actors to contact him, he tweeted that he has received intel from threat actors who feel "wronged" by their partners and decided to leak information in revenge.


[![Fabian Wosar tweet](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)](https://twitter.com/fwosar/status/1433050107218386944)


Wosar has told BleepingComputer that he has been able to use this intelligence to prevent ongoing ransomware attacks.




#### Tags:
[[Babuk]] [[ransomware]] [[BleepingComputer]] [[Windows]] [[Wosar]] [[attacks.]] [[Bleeping Computer]]
