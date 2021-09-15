# Cybercriminals recreate Cobalt Strike in Linux
### The new malware strain has gone unnoticed by detection tools.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/cybercriminals-recreate-cobalt-strike-in-linux/)
+ Date: September 15, 2021 -- 10:55 GMT (11:55 BST)
+ Author: Charlie Osborne


## Article:
Unknown

A re-implementation of Cobalt Strike has been "written from scratch" to attack Linux systems.


Dubbed [Vermilion Strike](https://www.intezer.com/blog/malware-analysis/vermilionstrike-reimplementation-cobaltstrike/), Intezer said on Tuesday that the new variation leans on Cobalt Strike functionality, including its command-and-control (C2) protocol, its remote access functionality, and its ability to run shell instructions.  

Cobalt Strike is a legitimate penetration testing tool for Windows systems. Released in 2012, the tool has been [constantly abused](https://www.zdnet.com/article/this-is-how-the-cobalt-strike-penetration-testing-tool-is-being-abused-by-cybercriminals/) by threat actors including advanced persistent threat (APT) groups such as Cozy Bear and campaigns designed to spread Trickbot and the Qbot/Qakbot banking Trojan.  

Cobalt Strike's source code for version 4.0 was allegedly [leaked online](https://cyware.com/news/source-code-of-cobalt-strike-allegedly-shared-online-94ff7fe9), however, most threat actors tracked by cybersecurity teams appear to rely on pirate and cracked copies of the software. 

Until now, at least. 

In August, Intezer uncovered the new ELF implementation of Cobalt Strike's beacon, which appears to have originated from Malaysia.  

When the researchers reported Vermilion Strike, it went undetected on VirusTotal as malicious software. (However, as of the time of writing, [24 antivirus vendors](https://www.virustotal.com/gui/file/294b8db1f2702b60fb2e42fdc50c2cee6a5046112da9a5703a548a4fa50477bc) have now registered the threat.) 






Built on a Red Hat Linux distribution, the malware is capable of launching beacons, listing files, changing and pulling working directories, appending and writing to files, uploading data to its C2, executing commands via the popen function, and analyzing disk partitions.  

While capable of attacking Linux builds, Windows samples have also been found that use the same C2 server and contain the same functionality. 

The researchers worked with McAfee Enterprise ATR to examine the software and have come to the conclusion that Vermilion Strike is being used in targeted attacks against telecoms, government, IT, advisory, and financial organizations worldwide. 

"The sophistication of this threat, its intent to conduct espionage, and the fact that the code hasn't been seen before in other attacks, together with the fact that it targets specific entities in the wild, leads us to believe that this threat was developed by a skilled threat actor," Intezer says.  

This is not the only unofficial port of Cobalt Strike, however. There is also [geacon](https://github.com/darkr4y/geacon), an open source project based on the Golang programming language. 

###  Previous and related coverage

* [This is how the Cobalt Strike penetration testing tool is being abused by cybercriminals](https://www.zdnet.com/article/this-is-how-the-cobalt-strike-penetration-testing-tool-is-being-abused-by-cybercriminals/)  

* [Cobalt Strike and Metasploit accounted for a quarter of all malware C&C servers in 2020](https://www.zdnet.com/article/cobalt-strike-and-metasploit-accounted-for-a-quarter-of-all-malware-c-c-servers-in-2020/)  

* [This major ransomware attack was foiled at the last minute. Here's how they spotted it](https://www.zdnet.com/article/this-ransomware-attack-was-foiled-at-the-last-minute-heres-how-they-spotted-it/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Linux]] [[Strike,]] [[Intezer]] [[ZDNet]]
