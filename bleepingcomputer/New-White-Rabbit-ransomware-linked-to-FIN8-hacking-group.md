# New White Rabbit ransomware linked to FIN8 hacking group
### A new ransomware family called 'White Rabbit' appeared in the wild recently, and according to recent research findings, could be a side-operation of the FIN8 hacking group.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/new-white-rabbit-ransomware-linked-to-fin8-hacking-group/
+ Date: 2022-01-18T11:56:00-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/18/white-rabbit-header-larger.jpg)

![White Rabbit looking down a rabbit hole](https://www.bleepstatic.com/content/hl-images/2022/01/18/white-rabbit-header-larger.jpg)


A new ransomware family called 'White Rabbit' appeared in the wild recently, and according to recent research findings, could be a side-operation of the FIN8 hacking group.


FIN8 is a financially motivated actor who has been spotted targeting financial organizations for several years, primarily by [deploying POS malware](https://www.bleepingcomputer.com/news/security/visa-warns-of-ongoing-cyber-attacks-on-gas-pump-pos-systems/) that can steal credit card details.


A simple tool to deliver double-extortion
-----------------------------------------


The first public mention of the White Rabbit ransomware was in a tweet by ransomware expert Michael Gillespie, seeking a sample of the malware.



> 
> [#Ransomware](https://twitter.com/hashtag/Ransomware?src=hash&ref_src=twsrc%5Etfw) Hunt: "White Rabbit" with extension ".scrypt", drops note for each encrypted file with ".scrypt.txt" with victim-specific information: <https://t.co/ZjVay8A3Ch>  
> 
> "Follow the White Rabbit..." [pic.twitter.com/lhzHi5t1KK](https://t.co/lhzHi5t1KK)
> 
> 
> — Michael Gillespie (@demonslay335) [December 14, 2021](https://twitter.com/demonslay335/status/1470823608725475334?ref_src=twsrc%5Etfw)


In a new report by Trend Micro, researchers analyze a sample of the White Rabbit ransomware obtained during an attack on a US bank in December 2021.


The ransomware executable is a small payload, weighing in at 100 KB file, and requires a password to be entered on command line execution to decrypt the malicious payload.


A password to execute the malicious payload has been used previously by other ransomware operations, including Egregor, MegaCortex, and [SamSam](https://www.bleepingcomputer.com/news/security/new-samsam-variant-requires-special-password-before-infection/).


Once executed with the correct password, the ransomware will scan all folders on the device and encrypt targeted files, creating ransom notes for each file it encrypts.


For example, a file named test.txt would be encrypted as **test.txt.scrypt**, and a ransom note would be created named **test.txt.scrypt.txt**.


While encrypting a device, removable and network drives are also targeted, with Windows system folders excluded from encryption to prevent rendering the operating system unusable.


The ransom note informs the victim that their files had been exfiltrated and threatens to publish and/or sell the stolen data if the demands are not met.



![White Rabbit ransom note](https://www.bleepstatic.com/images/news/u/1220909/ransomware/white-rabbit-note.jpg)**White Rabbit ransom note**  
*Source: Trend Micro*
The deadline for the victim to pay a ransom is set to four days, after which the actors threaten to send the stolen data to data protection authorities, leading to data breach GDPR penalties.


The evidence of the stolen files is uploaded to services such as 'paste[.]com' and 'file[.]io,' while the victim is offered a live chat communication channel with the actors on a Tor negotiation site.


The Tor site includes a 'Main page,' used to display proof of stolen data, and a Chat section where the victim can communicate with the threat actors and negotiate a ransom demand, as shown below.



![White Rabbit's private Tor site](https://www.bleepstatic.com/images/news/ransomware/w/white-rabbit/white-rabbit-chat-page.jpg)**White Rabbit's private Tor site**
Links to FIN8
-------------


As noted in the [Trend Micro report](https://www.trendmicro.com/en_us/research/22/a/new-ransomware-spotted-white-rabbit-and-its-evasion-tactics.html), evidence that connects FIN8 and 'White Rabbit' is found in the ransomware's deployment stage.


More specifically, the novel ransomware uses a never-before-seen version of Badhatch (aka "[Sardonic](https://www.bleepingcomputer.com/news/security/fin8-cybercrime-gang-backdoors-us-orgs-with-new-sardonic-malware/)"), a backdoor associated with FIN8.


Typically, these actors keep their custom backdoors to themselves and continue to develop them privately.


This finding is also confirmed by a different report on the same ransomware family undertaken by Lodestone researchers.


They too found Badhatch in 'White Rabbit' attacks, while they also noticed PowerShell artifacts similar to FIN8-associated activity from last summer.


As [the Lodestone report](https://lodestone.com/insight/white-rabbit-ransomware-and-the-f5-backdoor/) concludes: "Lodestone identified a number of TTPs suggesting that White Rabbit, if operating independently of FIN8, has a close relationship with the more established threat group or is mimicking them."


For now, White Rabbit has limited itself to only targeting a few entities but is considered an emerging threat that could turn into a severe menace to companies in the future.


At this point, it can be contained by taking standard anti-ransomware measures like the following:


* Deploy cross-layered detection and response solutions.
* Create an incident response playbook for attack prevention and recovery.
* Conduct ransomware attack simulations to identify gaps and evaluate performance.
* Perform backups, test backups, verify backups, and keep offline backups.





## Tags:

#### Threatactor:
[[threatactor.name=FIN8]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Bad Rabbit]] [[action.malware.name=Conti]] [[action.malware.name=Egregor]] [[action.malware.name=Elise]] [[action.malware.name=MegaCortex]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=SamSam]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Fin8]] [[Bleeping Computer]]
#### urls
https://t.co/ZjVay8A3Ch

