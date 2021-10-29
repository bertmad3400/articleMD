# Hive ransomware now encrypts Linux and FreeBSD systems
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/hive-ransomware-now-encrypts-linux-and-freebsd-systems/)
+ Date: October 29, 2021
+ Author: Sergiu Gatlan


## Article:
![Hive ransomware now encrypts Linux and FreeBSD systems](https://www.bleepstatic.com/content/hl-images/2021/10/29/Hive_Ransomware.jpg)


The Hive ransomware gang now also encrypts Linux and FreeBSD using new malware variants specifically developed to target these platforms.


However, as Slovak internet security firm ESET discovered, Hive's new encryptors are still in development and still lack functionality.


The Linux variant also proved to be quite buggy during ESET's analysis, with the encryption completely failing when the malware was executed with an explicit path.


It also comes with support for a single command line parameter (-no-wipe). In contrast, Hive's Windows ransomware comes with up to 5 execution options, including killing processes and skipping disk cleaning, uninteresting files, and older files.


The ransomware's Linux version also fails to trigger the encryption if executed without root privileges because it attempts to drop the ransom note on compromised devices' root file systems.


"Just like the Windows version, these variants are written in Golang, but the strings, package names and function names have been obfuscated, likely with gobfuscate," ESET Research Labs [said](https://twitter.com/ESETresearch/status/1454100591261667329).



![Hive ransom note](https://www.bleepstatic.com/images/news/u/1109292/2021/Hive_ransom_note.png)*Hive ransom note (ESET Research Labs)*
Ransomware now interested in Linux servers
------------------------------------------


[Hive](https://www.bleepingcomputer.com/tag/hive-ransomware/), a ransomware group active since [at least June 2021](https://twitter.com/fbgwls245/status/1408632067181604865), has already hit over 30 organizations, counting only victims who refused to pay the ransom.


They're just one of many ransomware gangs that have begun targeting Linux servers after their enterprise targets have slowly migrated to virtual machines for easier device management and more efficient use of resources.


By targeting virtual machines, ransomware operators can also encrypt multiple servers at once with a single command.


In June, researchers spotted a [new REvil ransomware Linux encryptor](https://www.bleepingcomputer.com/news/security/revil-ransomwares-new-linux-encryptor-targets-esxi-virtual-machines/) designed to target VMware ESXi virtual machines, a popular enterprise virtual machine platform.


Emsisoft CTO [Fabian Wosar](https://twitter.com/fwosar) told BleepingComputer that other ransomware groups, such as Babuk, RansomExx/Defray, Mespinoza, GoGoogle, DarkSide, and Hellokitty have also created their own Linux encryptors.


"The reason why most ransomware groups implemented a Linux-based version of their ransomware is to target ESXi specifically," Wosar said.


HelloKitty and BlackMatter ransomware Linux encryptors were later discovered in the wild by security researchers in [July](https://www.bleepingcomputer.com/news/security/linux-version-of-hellokitty-ransomware-targets-vmware-esxi-servers/) and [August](https://www.bleepingcomputer.com/news/security/linux-version-of-blackmatter-ransomware-targets-vmware-esxi-servers/), confirming Wosar's statement.


One month later, it was discovered that some of [these Linux malware strains are also buggy](https://www.bleepingcomputer.com/news/security/ransomexx-ransomware-linux-encryptor-may-damage-victims-files/) and could damage victims' files during encryption.


In the past, the Snatch and PureLocker ransomware operations have also used Linux variants on their attacks.




#### Tags:
[[ransomware]] [[Linux]] [[malware]] [[ESET]] [[Wosar]] [[Bleeping Computer]]
