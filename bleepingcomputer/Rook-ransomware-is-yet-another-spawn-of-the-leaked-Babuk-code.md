# Rook ransomware is yet another spawn of the leaked Babuk code
### A new ransomware operation named Rook has appeared recently on the cyber-crime space, declaring a desperate need to make a lot of money by breaching corporate networks and encrypting devices.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/rook-ransomware-is-yet-another-spawn-of-the-leaked-babuk-code/
+ Date: 2021-12-24T11:26:18-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/24/rook.jpg)

![rook](https://www.bleepstatic.com/content/hl-images/2021/12/24/rook.jpg?rand=1839799306)


A new ransomware operation named Rook has appeared recently on the cyber-crime space, declaring a desperate need to make "a lot of money" by breaching corporate networks and encrypting devices.


Although the introductory statements on their data leak portal were marginally funny, the first victim announcements on the site have made it clear that Rook is not playing games.



![About Us section on Rook's leak portal](https://www.bleepstatic.com/images/news/u/1220909/Website%20snaps/about_us(1).jpg)**About Us section on Rook's leak portal**
Researchers at SentinelLabs have taken a deep dive into the new strain, revealing its technical details, infection chain, and how it overlaps with the Babuk ransomware.


Infection process
-----------------


The Rook ransomware payload is usually delivered via Cobalt Strike, with phishing emails and shady torrent downloads being reported as the initial infection vector.


The payloads are packed with UPX or other crypters to help evade detection. When executed, the ransomware attempts to terminate processes related to security tools or anything that could interrupt the encryption.



![Terminated services](https://www.bleepstatic.com/images/news/u/1220909/ransomware/services_terminated.jpg)**Terminated services**  
*Source: SentinelLabs*
"Interestingly, we see the `kph.sys` driver from Process Hacker come into play in process termination in some cases but not others," SentinelLabs explains in [its report](http://www.sentinelone.com/labs/new-rook-ransomware-feeds-off-the-code-of-babuk/).


"This likely reflects the attacker’s need to leverage the driver to disable certain local security solutions on specific engagements."



![Volume shadow copy wiping process](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Volume shadow copy wiping process**  
*Source: SentinelLabs*
Rook also uses vssadmin.exe to delete volume shadow copies, a standard tactic used by ransomware operations to prevent shadow volumes from being [used to recover files](https://www.bleepingcomputer.com/tutorials/how-to-recover-files-and-folders-using-shadow-volume-copies/).


Analysts have found no persistence mechanisms, so Rook will encrypt the files, append the "**.Rook**" extension and then delete itself from the compromised system.



![Files encrypted by Rook](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Files encrypted by Rook**  
*Source: SentinelLabs*
Based on Babuk
--------------


SentinelLabs has found numerous code similarities between Rook and Babuk, a defunct RaaS that had its complete [source code leaked](https://www.bleepingcomputer.com/news/security/babuk-ransomwares-full-source-code-leaked-on-hacker-forum/) on a Russian-speaking forum in September 2021.


For example, Rook uses the same API calls to retrieve the name and status of each running service and the same functions to terminate them.


Also, the list of processes and Windows services that are stopped are the same for both ransomware.


This includes the Steam gaming platform, the Microsoft Office and Outlook email client, and Mozilla Firefox and Thunderbird.


Other similarities include how the encryptor deletes shadow volume copies, uses the Windows Restart Manager API, and enumerates local drives.



![Enumerating local drives alphabetically](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Enumerating local drives alphabetically**  
*Source: SentinelLabs*
Due to these code similarities, Sentinel One believes that Rook is based on the leaked source code for the Babuk Ransomware operation.


Is Rook a serious threat?
-------------------------


While it is too soon to tell how sophisticated Rook's attacks are, the consequences of an infection are still severe, leading to encrypted and stolen data.


The Rook data leak site currently contains two victims, a bank and an Indian aviation and aerospace specialist.


Both were added this month, so we are at an early stage in the group's activities.


If skilled affiliates join the new RaaS, Rook could become a significant threat in the future.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Babuk]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Sentinellabs]] [[Ransomware]] [[Babuk]] [[Bleeping Computer]]

