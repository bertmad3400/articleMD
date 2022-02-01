# MuddyWater hacking group targets Turkey in new campaign
### The Iranian-backed MuddyWater hacking group is conducting a new malicious campaign targeting private Turkish organizations and governmental institutions.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/muddywater-hacking-group-targets-turkey-in-new-campaign/
+ Date: 2022-02-01T02:30:00-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/11/18/Iran_flag.jpg)

![iran](https://www.bleepstatic.com/content/hl-images/2021/11/18/Iran_flag.jpg?rand=1942522965)


The Iranian-backed MuddyWater hacking group is conducting a new malicious campaign targeting private Turkish organizations and governmental institutions.


This cyber-espionage group (aka Mercury, [SeedWorm](https://www.bleepingcomputer.com/news/security/seedworm-spy-gang-stores-malware-on-github-keeps-up-with-infosec-advances/), and [TEMP.Zagros](http://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)) was [linked this month](https://www.bleepingcomputer.com/news/security/us-links-muddywater-hacking-group-to-iranian-intelligence-agency/) to Iran's Ministry of Intelligence and Security (MOIS) by the US Cyber Command (USCYBERCOM).


The hacking group has been attributed to attacks against entities in Central and Southwest Asia and numerous public and privately-held organizations from Europe, Asia, and North America in the telecommunications, government (IT services), oil, and [airline industry](https://www.bleepingcomputer.com/news/security/state-sponsored-hackers-abuse-slack-api-to-steal-airline-data/) sectors.


When conducting attacks, the threat actors use various file types like PDFs, XLS files, and Windows executables to deploy obfuscated PowerShell-based downloaders and gain initial access to targeted networks. 


Two infection chains
--------------------


A new report by researchers at [Cisco Talos](https://blog.talosintelligence.com/2022/01/iranian-apt-muddywater-targets-turkey.html) links MuddyWater to recent attacks targeting Turkish private organizations and governmental agencies.


The attacks start with spear-phishing that uses files with Turkish language names and pretend to come from the country's Health or Interior ministry.


As part of the attack, the MuddyWater threat actors use two infection chains that begin with delivering a PDF file. In the first case, the PDF features an embedded button that fetches an XLS file upon clicking it.



![Decoy PDF file with button](https://www.bleepstatic.com/images/news/u/1220909/Phishing/error.png)**Decoy PDF file with button**  
*Source: Cisco Talos*
These files are typical XLS documents that carry malicious VBA macros which initiate the infection process and establish persistence by creating a new Registry key.



![Registry key which establishes persistence](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/key.png)**Registry key which establishes persistence**  
*Source: Cisco Talos*
On the same stage, a VBScript is fetched with a PowerShell downloader and executed through a "living off the land" DLL to evade detection, retrieving the primary payload from the C2.



![First infection chain](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**First infection chain based on a PDF**  
*Source: Cisco Talos*
The second infection chain uses an EXE file instead of an XLS, but it still employs the PowerShell downloader, the intermediate VBScript, and adds a new registry entry for persistence.



![Second infection chain diagram](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Second infection chain diagram**  
*Source: Cisco Talos*
Using canary tokens
-------------------


One notable difference in this campaign compared to older ones is the use of canary tokens to track code executions and any subsequent infections on neighboring systems.


The token hides inside the malicious attachment or the email itself and alerts the threat actors when the victim opens the lure and executes the macro.


"The malicious VBA macros consisted of the same set of functionalities for creating the malicious VBS and PS1 scripts, and achieving persistence across reboots," explains the [Cisco Talos report](http://blog.talosintelligence.com/2022/01/iranian-apt-muddywater-targets-turkey.html).


"However, there was one interesting addition to the macro functionality now. The latest versions of the VBA code deployed could make HTTP requests to a canary token from canarytokens.com."


These tokens can also be used as anti-analysis tools, providing timestamps to the actors and making it easy to identify research/analysis-induced inconsistencies.


Finally, if the token sends requests but the payload isn't fetched, it's an indication that the payload server is blocked, giving the actors valuable information on the situation and driving them to seek alternative delivery methods.


Attribution
-----------


The researchers attribute these attacks to the MuddyWater group based on the observed technical indicators, tactics, procedures, and C2 infrastructure.


Notably, the Turkish authorities identified some of the C2 IP addresses used in this campaign from previous attacks and are listed in [official threat advisories](https://bidb.trakya.edu.tr/news/kurum-ve-kuruluslara-yonelik-apt-saldirilari?_x_tr_sl%3Dtr%26_x_tr_tl%3Den%26_x_tr_hl%3Den%26_x_tr_pto%3Dsc).


Cisco has additional strong evidence that points to Iranian actors in the form of code and metadata similarities and other indicators that they didn't publish due to intelligence sharing sensitivities.





## Tags:

#### Threatactor:
[[threatactor.name=MuddyWater]] [[threatactor.name=MuddyWater]] [[threatactor.name=MuddyWater]] [[threatactor.name=MuddyWater]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Power Loader]] [[action.malware.name=PS1]] [[action.malware.name=PS1]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.continent.name=Asia]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Talos]] [[Muddywater]] [[Xls]] [[Pdf]] [[Vba]] [[C2]] [[Bleeping Computer]]

