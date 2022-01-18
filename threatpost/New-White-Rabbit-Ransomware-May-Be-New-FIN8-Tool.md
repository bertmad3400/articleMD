# New ‘White Rabbit’ Ransomware May Be New FIN8 Tool
### It's a double-extortion play that uses the command-line password ‘KissMe’ to hide its nasty acts and adorns its ransom note with cutesy ASCII bunny art.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177703
+ Date: 2022-01-18T17:23:12+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/18120214/white-bunny.jpg)

A new ransomware family, White Rabbit, chewed through a local U.S. bank last month — and it may be connected to the financially motivated advanced persistent threat (APT) group known as [FIN8](https://threatpost.com/fin8-bank-sardonic-backdoor/168982/), researchers said.


In a Tuesday [report](https://www.trendmicro.com/en_us/research/22/a/new-ransomware-spotted-white-rabbit-and-its-evasion-tactics.html), Trend Micro researchers said that this twicky wabbit knows how to burrow away where it can’t be spotted. In fact, it looks like the operators behind the White Rabbit ransomware have taken a page from the [more established](https://threatpost.com/egregor-ransomware-mass-media-corporate-data/159816/) ransomware family known as [Egregor](https://www.trendmicro.com/en_us/research/20/l/egregor-ransomware-launches-string-of-high-profile-attacks-to-en.html) when it comes to hiding their malicious activity, researchers said.


Egregor, which [claimed responsibility](https://threatpost.com/egregor-responsibility-barnes-noble/160401/) for a well-publicized cyberattack on Barnes & Noble in October 2020, is a ransomware-as-a-service (RaaS) player that [sparked](https://threatpost.com/fbi-egregor-attacks-businesses-worldwide/162885/) an FBI warning after compromising more than 150 organizations in short order after its birth.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


White Rabbit may be sneaky, but it leaves tracks. The ransomware was spotted by multiple security outfits, and was first [detected](https://lodestone.com/insight/white-rabbit-ransomware-and-the-f5-backdoor/) on Dec. 14 by the Lodestone Forensic Investigations team, which said that it had seen some White Rabbit activity a few days earlier, on Dec. 11.


But the earliest stirrings date back to July 10, when a PowerShell script was executed – a script that held script blocks that matched those described in a July 27 [Bitdefender article on FIN8](https://businessinsights.bitdefender.com/deep-dive-into-a-fin8-attack-a-forensic-investigation).


The Dec. 14 White Rabbit attack was also publicly [disclosed](https://twitter.com/demonslay335/status/1470823608725475334) on Twitter that same day by security researcher Michael Gillespie (@demonslay355).



> 
> 🔒 [#Ransomware](https://twitter.com/hashtag/Ransomware?src=hash&ref_src=twsrc%5Etfw) Hunt: "White Rabbit" with extension ".scrypt", drops note for each encrypted file with "<filename>.scrypt.txt" with victim-specific information: <https://t.co/ZjVay8A3Ch>  
> "Follow the White Rabbit…" 🐰🤔 [pic.twitter.com/lhzHi5t1KK](https://t.co/lhzHi5t1KK)
> 
> 
> — Michael Gillespie (@demonslay335) [December 14, 2021](https://twitter.com/demonslay335/status/1470823608725475334?ref_src=twsrc%5Etfw)
> 
> 



Gillespie included a link to the [ransom note,](https://pastebin.com/waLqSHCh) which includes cutesy bunny ASCII art. The note warns victims that if they’re reading it, their network infrastructure has been compromised, their critical data has leaked and their files are encrypted. In other words, the newcomer is using the same double-extortion shtick used by a [skyrocketing number](https://threatpost.com/double-extortion-ransomware-data-leaks/176723/) of RaaS players, threatening targets that their stolen data isn’t just encrypted but will also be published or sold.


Command-Line Password ‘KissMe’ Used to Hide Bad Acts
----------------------------------------------------


It gets cutesy-wutesy-er: Trend Micro researchers said that one of the most notable aspects of the new ransomware’s attack is the use of a specific command-line password to decrypt its internal configuration and launch its ransomware routine. In the particular case that they came across, that password is “KissMe,” as shown in the SysTracer screen capture below. SysTracer is a system utility tool that sniffs out changed data in a system’s registry and files.


“This method of hiding malicious activity is a trick that the ransomware family Egregor uses to hide malware techniques from analysis,” the Trend Micro researchers pointed out, adding that “other samples might use a different password” than KissMe.


The SysTracer image also shows the arguments accepted by the ransomware, which, researchers surmised, stand in for:


* -p: password/passphrase
* -f: file to be encrypted
* -l: logfile
* -t: malware’s start time


Cobalt Strike Link to FIN8
--------------------------


Trend Micro picked up on traces of Cobalt Strike commands – the PowerShell .exe, as shown below – that its researchers think “might have been used to reconnoiter, infiltrate and drop the malicious payload into the affected system,” according to the report.


Lodestone’s analysis of the ransomware group’s tactics, techniques, and procedures (TTPs) points to the White Rabbit group potentially being affiliated with FIN8.


FIN8 [has typically used](https://malpedia.caad.fkie.fraunhofer.de/actor/fin8) social engineering and spear-phishing to go after financial services and payment-card data from [point-of-sale (PoS) systems](https://threatpost.com/fin8-targets-card-data-fuel-pumps/151105/) – particularly those of retailers, restaurants and [the hotel industry](https://www.bankinfosecurity.com/fin8-group-returns-targeting-pos-devices-new-tools-a-12819). More recently, it has added ransomware to its bag of trucks. It’s been active since at least [January 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.htmlhttps://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html) and periodically pops in and out of dormancy in order to fine-tune its TTPs so as to evade detection and ramp up its success rate.


One example was in August, when the latest refinement of the APT’s BadHatch backdoor proved able to [leverage new malware](https://threatpost.com/fin8-bank-sardonic-backdoor/168982/) on the fly without redeployment, making it potent and nimble.


Besides BadHatch, FIN8’s well-stocked [arsenal](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/) has included [malware variants](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/) such as ShellTea – a backdoor also known as [PunchBuggy](https://www.fireeye.com/blog/threat-research/2016/05/windows-zero-day-payment-cards.html) –and the memory-scraping malware PunchTrack.


In the December attack, White Rabbit dragged in a previously unseen version of BadHatch that, based on characteristics of the malware sample acquired, Lodestone named F5.


“The exact relationship between the White Rabbit group and FIN8 is currently unknown,” Lodestone stipulated. “However, Lodestone identified a number of TTPs suggesting that White Rabbit, if operating independently of FIN8, has a close relationship with the more established threat group or is mimicking them.”


White Rabbit’s Ransomware Path
------------------------------


As Trend Micro tells it, the White Rabbit ransomware creates a note for each file it encrypts. “Each note bears the name of the encrypted file and is appended with ‘.scrypt.txt,'” researchers described. “Prior to the ransomware routine, the malware also terminates several processes and services, particularly antivirus-related ones.”


Next, if the -f argument isn’t given, it tries to encrypt files in fixed, removable and network drives, as well as in resources. Trend Micro provided the list below of the paths and directories the ransomware tries to skip, “to avoid crashing the system and destroying its own notes.”


* *.scrypt.txt
* *.scrypt
* c:\windows\*
* *:\sysvol\*
* *:\netlogon\*
* c:\filesource\*
* *.exe
* *.dll
* *\desktop.ini
* *:\windows\*
* c:\programdata\*
* *:\programfiles\*
* *:\program files (x86)\*
* *:\program files (x64)\*
* *.lnk
* *.iso
* *.msi
* *.sys
* *.inf
* %User Temp%\*
* *\thumbs.db


FIN8 Connection Still a Bit Sketchy
-----------------------------------


FIN8 and White Rabbit may be related, or they might actually share the same creator: It’s not a solid call just yet, Trend Micro said.


It could be that this is just another indication of how the group is doing what it’s known for: expanding its arsenal, past the infiltration and reconnaissance tools for which it’s well-known, to add ransomware to the toolkit. “So far, White Rabbit’s targets have been few, which could mean that they are still testing the waters or warming up for a large-scale attack,” Trend Micro researchers noted.


It has an “uncomplicated” ransomware routine, which likely means that it’s still under development, they said. Despite being a simple piece of malware, it’s still dangerous: “Despite being in this early stage, however, it is important to highlight that it bears the troublesome characteristics of modern ransomware: It is, after all, highly targeted and uses double extortion methods,” according to Trend Micro’s writeup. “As such, it is worth monitoring.”


Blocking White Rabbit Attacks
-----------------------------


Both Lodestone and Trend Micro included indicators of compromise in their White Rabbit writeups.


Trend Micro also had the following suggestions for setting up a multilayered defense to “help guard against modern ransomware and prevent the success of the evasion tactics they employ”:


* Deploy cross-layered detection and response solutions. Find solutions that can anticipate and respond to ransomware activities, techniques, and movements before the threat culminates.
* Create a playbook for attack prevention and recovery. Both an incident-response (IR) [playbook](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final) and IR [frameworks](https://www.cynet.com/incident-response/incident-response-sans-the-6-steps-in-depth/) allow organizations to plan for different attacks, including ransomware.
* Conduct attack simulations. Expose employees to a [realistic cyberattack simulation](https://www.nytimes.com/2021/06/03/us/politics/ransomware-cybersecurity-infrastructure.html) that can help decision-makers, security personnel, and IR teams identify and prepare for potential security gaps and attacks.


*Photo courtesy of [PxHere](https://pxhere.com/en/photo/696393?utm_content=clipUser&utm_medium=referral&utm_source=pxhere). [Licensing details](https://creativecommons.org/licenses/publicdomain/).*


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=BRONZE BUTLER]] [[threatactor.name=FIN8]] [[threatactor.name=Rocke]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Derusbi]] [[action.malware.name=Egregor]] [[action.malware.name=Elise]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=PUNCHBUGGY]] [[action.malware.name=PUNCHBUGGY]] [[action.malware.name=PUNCHTRACK]] [[action.malware.name=Reg]] [[action.malware.name=Spark]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Accomodation]] [[victim.industry.name=Accomodation]] [[victim.industry.name=Finance]] [[victim.industry.name=Retail]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Fin8]] [[Malware]] [[Egregor]] [[Gillespie]] [[Systracer]] [[Badhatch]] [[ThreatPost]]
#### urls
https://t.co/ZjVay8A3Ch

