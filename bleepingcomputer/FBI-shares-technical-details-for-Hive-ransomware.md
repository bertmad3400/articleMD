# FBI shares technical details for Hive ransomware 
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/fbi-shares-technical-details-for-hive-ransomware/)
+ Date: August 26, 2021
+ Author: Ionut Ilascu


## Article:
![FBI shares technical details for Hive ransomware](https://www.bleepstatic.com/content/hl-images/2021/08/26/HiveRansomware.jpg)


The Federal Bureau of Investigation (FBI) has released some technical details and indicators of compromise associated with Hive ransomware attacks.


In a rare occurrence, the FBI has included the link to the leak site where the ransomware gang publishes data stolen from companies that did not pay.


### Multiple tactics and techniques


Hive ransomware relies on a diverse set of tactics, techniques, and procedures, which makes it difficult for organizations to defend against its attacks, the FBI says.


Among the methods that the gang uses to gain initial access and to move laterally on the network, there are phishing emails with malicious attachments and the Remote Desktop Protocol (RDP).


Before deploying the encryption routine, the Hive ransomware steals files they deem valuable, to pressure the victim to pay the ransom under the threat of a data leak.


The FBI says that the threat actor searches for processes for backups, file copying, and security solutions (like Windows Defender) that would hinder the data encryption task and terminates them.


This stage is followed by dropping a **hive.bat** script that performs a cleanup routine by removing itself after deleting the Hive malware executable.


Another script called **shadow.bat** is tasked with deleting shadow copies, backup files, and system snapshots and then removes itself from the compromised host.


The FBI says that some Hive ransomware victims reported being contacted by the attacker asking them to pay the ransom in exchange for the stolen files.



“The initial deadline for payment fluctuates between 2 to 6 days, but actors have prolonged the deadline in response to contact by the victim company,” the agency notes in its [Flash bulletin](https://www.documentcloud.org/documents/21049431-fbi-flash-hive-ransomware-iocs).



Along with indicators of compromise (IoCs), the FBI also provides a link to the threat actor’s leak site, a detail that is typically hidden in technical reports.


Some of the files observed in Hive ransomware attacks include the following:


* **Winlo.exe** - used to drop 7zG.exe, a legitimate version of the 7-Zip file archiver
* **7zG.exe** - version 19.0.0 of the 7-Zip file archiver
* **Winlo\_dump\_64\_SCY.exe** - used to encrypt files with the .KEY extension and to drop the ransom note *HOW\_TO\_DECRYPT.txt*



![Hive Ransomware - ransom note](https://www.bleepstatic.com/images/news/u/1100723/Ransomware/Hive/HiveRansomwareNote.png)source: BleepingComputer
The FBI notes that the threat actor also relies on file-sharing services, many of them anonymous, like Anonfiles, MEGA, Send.Exploit, Ufile, or SendSpace.


Although it was first observed in late June, Hive ransomware has already breached more than 30 organizations this summer, a count that includes only victims that refused to pay the ransom.


A recent [victim of Hive ransomware is Memorial Health System](https://www.bleepingcomputer.com/news/security/hive-ransomware-attacks-memorial-health-system-steals-patient-data/), which offers a network of services that includes three hospitals and providers representing 64 clinics.


From files seen by BleepingComputer, the attacker stole databases containing information belonging to more than 200,000 patients.


The FBI does not recommend paying the threat actors to discourage then from continuing the activity. Furthermore, there is no guarantee that the attacker will destroy the stolen data instead of selling it or giving it to fellow criminals.


Regardless of ransomware victim's decision to pay or not, the FBI urges companies to report ransomware incidents to the local field office to help investigators with critical information to track the attackers, "hold them accountable under US law, and prevent future attacks."




#### Tags:
[[ransomware]] [[Bleeping Computer]]
