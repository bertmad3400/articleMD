# LockBit ransomware now encrypts Windows domains using group policies
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/lockbit-ransomware-now-encrypts-windows-domains-using-group-policies/)
+ Date: July 27, 2021
+ Author: Lawrence Abrams


## Article:
![LockBit](https://www.bleepstatic.com/content/hl-images/2021/07/27/Lockbit-2.jpg)


A new version of the LockBit 2.0 ransomware has been found that automates the encryption of a Windows domain using Active Directory group policies.


The LockBit ransomware operation launched in September 2019 as a ransomware-as-a-service, where threat actors are recruited to breach networks and encrypt devices.


In return, the recruited affiliates earn 70-80% of a ransom payment, and the LockBit developers keep the rest.


Over the years, the ransomware operation has been very active, with a representative of the gang promoting the activity and providing support on hacking forums.


After ransomware topics were banned on hacking forums [[1](https://www.bleepingcomputer.com/news/security/ransomware-ads-now-also-banned-on-exploit-cybercrime-forum/), [2](https://www.bleepingcomputer.com/news/security/popular-russian-hacking-forum-xss-bans-all-ransomware-topics/)], LockBit  began promoting the new LockBit 2.0 ransomware-as-a-service operation on their data leak site.



![LockBit 2.0 affiliate program features](https://www.bleepstatic.com/images/news/ransomware/l/lockbit/lockbit-2.0/lockbit-affiliate-program.jpg)**LockBit 2.0 affiliate program features**
Included with the new version of LockBit are numerous advanced features, with two of them outlined below.


Uses group policy update to encrypt network
-------------------------------------------


LockBit 2.0 promotes a long list of features with many used by other ransomware operations in the past.


However, one promoted feature stuck out where the developers claim to have automated the ransomware distribution throughout a Windows domain without the need for scripts.


When threat actors breach a network and finally gain control of the domain controller, they utilize third-party software to deploy scripts that disable antivirus and then execute the ransomware on the machines on the network.


In samples of the LockBit 2.0 ransomware discovered by [MalwareHunterTeam](https://twitter.com/malwrhunterteam) and analyzed by BleepingComputer and [Vitali Kremez](https://twitter.com/VK_Intel), the threat actors have automated this process so that the ransomware distributes itself throughout a domain when executed on a domain controller.


When executed, the ransomware will create new group policies on the domain controller that are then pushed out to every device on the network. 


These policies disable Microsoft Defender's real-time protection, alerts, submitting samples to Microsoft, and default actions when detecting malicious files, as shown below.


Other group policies are created, including one to create a scheduled task on Windows devices that launch the ransomware executable.


The ransomware will then run the following command to push the group policy update to all of the machines in the Windows domain.


Kremez told BleepingComputer that during this process, the ransomware will also use Windows Active Directory APIs to perform LDAP queries against the domain controller's ADS to get a list of computers.


Using this list, the ransomware executable will be copied to each device's desktop and the scheduled task configured by group policies will launch the ransomware using the UAC bypass below:


As the ransomware will be executed using a UAC bypass, the program will run silently in the background without any outward alert on the device being encrypted.


While [MountLocker had previously used Windows Active Directory APIs](https://www.bleepingcomputer.com/news/security/mountlocker-ransomware-uses-windows-api-to-worm-through-networks/) to perform LDAP queries this is the first time we have seen a ransomware automate the distribution of the malware via group policies.


"This is the first ransomware operation to automate this process, and it allows a threat actor to disable Microsoft Defender and execute the ransomware on the entire network with a single command," Kremez told BleepingComputer.


"A new version of the LockBit 2.0 ransomware has been found that automates the interaction and subsequent encryption of a Windows domain using Active Directory group policies."  
  

"The malware added a novel approach of interacting with active directory propagating ransomware to local domains as well as built-in updating global policy with anti-virus disable making "pentester" operations easier for new malware operators."


LockBit 2.0 print bombs network printers
----------------------------------------


LockBit 2.0 also includes a feature previously [used by the Egregor Ransomware operation](https://www.bleepingcomputer.com/news/security/egregor-ransomware-print-bombs-printers-with-ransom-notes/) that print bombs the ransom note to all networked printers.


When the ransomware has finished encrypting a device, it will repeatedly print the ransom note to any connected network printers to get the victim's attention, as shown below.



![Print bomb of ransom notes](https://www.bleepstatic.com/images/news/ransomware/l/lockbit/lockbit-2.0/print-bomb.jpg)**Print bomb of ransom notes**
In an Egregor attack against [retail giant Cencosud](https://www.bleepingcomputer.com/news/security/retail-giant-cencosud-hit-by-egregor-ransomware-attack-stores-impacted/), this feature caused ransom notes to shoot out of receipt printers after they conducted the attack.




#### Tags:
[[ransomware]] [[LockBit]] [[Windows]] [[below.]] [[malware]] [[Bleeping Computer]]
