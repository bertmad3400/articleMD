# New 'Karakurt' hacking group focuses on data theft and extortion
### A sophisticated cybercrime group known as 'Karakurt' who has been quietly working from the shadows has had its tactics and procedures exposed by researchers who tracked recent cyberattacks conducted by the hackers.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/new-karakurt-hacking-group-focuses-on-data-theft-and-extortion/
+ Date: 2021-12-10T06:00:00-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/09/cobweb.jpg)

![cobweb](https://www.bleepstatic.com/content/hl-images/2021/12/09/cobweb.jpg?rand=1311989289)


A sophisticated cybercrime group who has been quietly working from the shadows has had its tactics and procedures exposed by researchers who tracked recent cyberattacks conducted by the hackers.


The hacking group calls itself 'Karakurt' and is a financially motivated threat actor that has ramped up its cyber-attacks in Q3 2021.


The first signs of Karakurt activity were identified in June 2021, with the registration of two domains and the creation of a Twitter handle.



![Karakurt activity timeline](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/timeline(2).jpg)**Karakurt activity timeline**  
*Source: Accenture*
The actors focus almost exclusively on data exfiltration and extortion and are not using ransomware to lock their victims' files.


The report on Karakurt comes from researchers at Accenture Security, who managed to track the group's "living off the land" tactics, toolset, and intrusion techniques.


The threat group claims to have compromised over 40 victims between September and November 2021 and has posted downloadable stolen file packs on its sites.



![Karakurt website advertising stolen files](https://www.bleepstatic.com/images/news/u/1220909/Website%20snaps/data_leaks.jpg)**Karakurt website advertising stolen files**  
*Source: Accenture*
Roughly 95% of these victims are based in North America, while the rest are European entities. Karakurt isn't focused on a particular industry, so the victimology appears random.



![Karakurt victims by sector](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Karakurt victims by sector**  
*Source: Accenture*
Entry, escalation, and exfiltration
-----------------------------------


The actor primarily uses VPN credentials to gain initial access to a victim's network, either by sourcing them from sellers or phishing them themselves.


The persistence is established by dropping the widely abused Cobalt Strike remote access tool, although, in recent attacks, Karakurt switched to using AnyDesk. 


With Cobalt Strike beacons becoming more aggressively detected by security software, AnyDesk has become increasingly popular among threat actors, such as the [Conti ransomware gang](https://www.bleepingcomputer.com/news/security/conti-ransomware-now-hacking-exchange-servers-with-proxyshell-exploits/).


Next, the actor steals additional credentials belonging to administrators by employing Mimikatz and uses them for undetectable privilege escalation.


"In one intrusion, Accenture Security also observed the threat group avoiding the use of common post-exploitation tools or commodity malware in favor of credential access," explained the report by [Accenture](https://www.accenture.com/us-en/blogs/cyber-defense/karakurt-threat-mitigation).


"This approach enabled it to evade detection and bypass security tools such as common endpoint detection and response (EDR) solutions."


For the exfiltration of the data, Karakurt uses 7zip and WinZip to compress the files and then sends everything to Mega.io via Rclone or FileZilla.


Encryption-less attacks
-----------------------


While these attacks appear less damaging compared to ransomware infections that encrypt data and wipe backups, they can still be quite detrimental.


Threatening publishing stolen files can bring a company to its knees even if its operational status is left unruffled, with less overhead involved in conducting attacks.


For this reason, new hacking groups like [SnapMC](https://www.bleepingcomputer.com/news/security/snapmc-hackers-skip-file-encryption-and-just-steal-your-files/) are focusing solely on data exfiltration and extortion as their threat model.


However, [paying a ransom doesn't guarantee](https://www.bleepingcomputer.com/news/security/scam-psa-ransomware-gangs-dont-always-delete-stolen-data-when-paid/) that threat actors will wipe stolen data or that it won't be sold to others, so it is never wise to pay a ransom solely to prevent a data breach.


Instead, organizations should focus on defense, prevention, and detection measures to keep these threats off their networks.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Conti]] [[action.malware.name=Mimikatz]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Accenture]] [[Ransomware]] [[Bleeping Computer]]

