# Hacker-made Linux Cobalt Strike beacon used in ongoing attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/hacker-made-linux-cobalt-strike-beacon-used-in-ongoing-attacks/)
+ Date: September 13, 2021
+ Author: Sergiu Gatlan


## Article:
![Hacker-made Linux Cobalt Strike beacon used in ongoing attacks](https://www.bleepstatic.com/content/hl-images/2021/09/13/Cobalt-Strike.jpg)


An unofficial Cobalt Strike Beacon Linux version made by unknown threat actors from scratch has been spotted by security researchers while actively used in attacks targeting organizations worldwide.


[Cobalt Strike](https://attack.mitre.org/software/S0154/) is a legitimate penetration testing tool designed as an attack framework for red teams (groups of security professionals who act as attackers on their own org's infrastructure to discover security gaps and vulnerabilities.)


Cobalt Strike is also used by threat actors (commonly dropped in ransomware attacks) for post-exploitation tasks after deploying so-called beacons, which provide persistent remote access to compromised devices. Using beacons, attackers can later access breached servers to harvest data or deploy further malware payloads.


Over time, cracked copies of Cobalt Strike have been obtained and shared by threat actors, becoming one of the most common tools used in cyberattacks leading to data theft and ransomware. However, Cobalt Strike has always had a weakness — it only supports Windows devices and does not include Linux beacons.


In a [new report by security firm Intezer](https://www.intezer.com/blog/malware-analysis/vermilionstrike-reimplementation-cobaltstrike/), researchers explain how threat actors have taken it upon themselves to create their Linux beacons compatible with Cobalt Strike. Using these beacons, threat actors can now gain persistence and remote command execution on both Windows and Linux machines.


Fully undetected in VirusTotal
------------------------------


Intezer researchers, who first spotted the beacon re-implementation in August and dubbed it **Vermilion Strike**, said that the Cobalt Strike ELF binary [[VirusTotal](https://www.virustotal.com/gui/file/294b8db1f2702b60fb2e42fdc50c2cee6a5046112da9a5703a548a4fa50477bc)] they discovered is currently fully undetected by anti-malware solutions.


Vermilion Strike comes with the same configuration format as the official Windows beacon and can speak with all Cobalt Strike servers, but doesn't use any of Cobalt Strike's code.


This new Linux malware also features technical overlaps (the same functionality and command-and-control servers) with Windows DLL files hinting at the same developer.



![Vermilion Strike configuration decryption function comparison](https://www.bleepstatic.com/images/news/u/1109292/2021/Configuration%20decryption%20function%20comparison.png)*Vermilion Strike configuration decryption function comparison (Intezer)*
"The stealthy sample uses Cobalt Strike’s Command and Control (C2) protocol when communicating to the C2 server and has Remote Access capabilities such as uploading files, running shell commands and writing to files," Intezer said. 


"The malware is fully undetected in VirusTotal at the time of this writing and was uploaded from Malaysia."


Vermilion Strike can perform the following tasks once deployed on a compromised Linux system:


* Change working directory
* Get current working directory
* Append/write to file
* Upload file to C2
* Execute command via popen
* Get disk partitions
* List files


Deployed in ongoing attacks since August
----------------------------------------


Using telemetry data provided by McAfee Enterprise ATR, Intezer also found multiple orgs targeted using Vermilion Strike since August 2021 from various industry sectors ranging from telecom companies and government agencies to IT companies, financial institutions, and advisory companies worldwide.


It's also worth mentioning that Vermilion Strike is not the first or only port of Cobalt Strike's Beacon to Linux, with [geacon](https://github.com/darkr4y/geacon), an open-source Go-based implementation, publicly available for the last two years.


However, as Intezer told BleepingComputer, "this is the first Linux implementation that has been used for real attacks." Unfortunately, there is no info on the initial attack vector the attackers use to target Linux systems.


"The sophistication of this threat, its intent to conduct espionage, and the fact that the code hasn't been seen before in other attacks, together with the fact that it targets specific entities in the wild, leads us to believe that this threat was developed by a skilled threat actor," Intezer concluded.




#### Tags:
[[Linux]] [[Intezer]] [[Windows]] [[beacons,]] [[malware]] [["The]] [[Bleeping Computer]]
