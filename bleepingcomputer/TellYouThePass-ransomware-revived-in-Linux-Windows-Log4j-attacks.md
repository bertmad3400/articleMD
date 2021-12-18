# TellYouThePass ransomware revived in Linux, Windows Log4j attacks
### Threat actors have revived an old and relatively inactive ransomware family known as TellYouThePass, deploying it in attacks against Windows and Linux devices targeting a critical remote code execution bug in the Apache Log4j library.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/tellyouthepass-ransomware-revived-in-linux-windows-log4j-attacks/
+ Date: 2021-12-17T15:25:06-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j__logo.jpg)

![TellYouThePass ransomware revived in Linux, Windows Log4j attacks](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j__logo.jpg)


Threat actors have revived an old and relatively inactive ransomware family known as TellYouThePass, deploying it in attacks against Windows and Linux devices targeting a critical remote code execution bug in the Apache Log4j library.


KnownSec 404 Team's Heige first reported these attacks [on Twitter](https://twitter.com/80vul/status/1470272820571963392) on Monday after observing that the ransomware was dropped on old Windows systems using exploits abusing the flaw tracked as CVE-2021-44228 and known as [Log4Shell](https://www.bleepingcomputer.com/tag/log4shell/).


Heige's report was confirmed by the Sangfor Threat Intelligence Team, who successfully captured one of the TellYouThePass ransomware samples deployed in attacks using Log4Shell exploits mostly impacting Chinese targets, according to [Curated Intelligence](https://www.curatedintel.org/2021/12/tellyouthepass-ransomware-via-log4shell.html).


As they further discovered (findings that [CronUP's Germán Fernández](https://twitter.com/1ZRR4H/status/1471717338491797504/) also confirmed), the ransomware has a Linux version that harvests SSH keys and moves laterally throughout victims' networks.


"It is worth noting that this is not the first time that Tellyouthepass ransomware has used high-risk vulnerabilities to launch attacks," [Sangfor researchers said](https://www.secpulse.com/archives/171335.html). "As early as last year, it had used Eternal Blue vulnerabilities to attack multiple organizational units."


Other security researchers [[1](https://twitter.com/Myrtus0x0), [2](https://twitter.com/nokae8)] have also analyzed one of the ransomware samples deployed in these attacks and tagged it as "likely belonging" to the TellYouThePass family.


According to submission stats to the ID Ransomware service, [TellYouThePass ransomware](https://www.bleepingcomputer.com/forums/t/693707/tellyouthepass-ransomware-locked;-readmehtml-support-topic/) has seen a massive and [sudden spike](https://twitter.com/PolarToffee/status/1470372924804800514) in activity after [Log4Shell proof-of-concept exploits were released online](https://www.bleepingcomputer.com/news/security/new-zero-day-exploit-for-log4j-java-library-is-an-enterprise-nightmare/).



![TellYouThePass ransomware submissions](https://www.bleepstatic.com/images/news/u/1109292/2021/TellYouThePass%20ransomware%20submissions.png)*TellYouThePass ransomware submissions (ID Ransomware)*
Log4Shell exploited in ransomware attacks
-----------------------------------------


TellYouThePass is not the first ransomware strain deployed in Log4Shell attacks since financially-motivated attackers began [injecting Monero miners](https://www.bleepingcomputer.com/news/security/log4j-attackers-switch-to-injecting-monero-miners-via-rmi/) on compromised systems and [state-backed hackers started exploiting it](https://www.bleepingcomputer.com/news/security/log4j-vulnerability-now-used-by-state-backed-hackers-access-brokers/) to create footholds for follow-on activity.


BitDefender first reported [they found a new ransomware family](https://www.bleepingcomputer.com/news/security/new-ransomware-now-being-deployed-in-log4shell-attacks/) (tagged by some as a wiper) they dubbed Khonsari being installed directly via Log4Shell exploits.


The Microsoft 365 Defender Threat Intelligence Team also saw Khonsari ransomware payloads [dropped on self-hosted Minecraft servers](https://www.bleepingcomputer.com/news/security/microsoft-khonsari-ransomware-hits-self-hosted-minecraft-servers/).


Last but not least, [Conti ransomware operators have also added a Log4Shell exploit to their arsenal](https://www.bleepingcomputer.com/news/security/conti-ransomware-uses-log4j-bug-to-hack-vmware-vcenter-servers/) to move laterally through targets' networks, gain access to VMware vCenter Server instances, and encrypt virtual machines.


In related news, [CISA ordered Federal Civilian Executive Branch agencies today](https://www.bleepingcomputer.com/news/security/us-emergency-directive-orders-govt-agencies-to-patch-log4j-bug/) to patch their systems against the Log4Shell vulnerability within the next six days, until December 23.


The cybersecurity agency has also recently added the flaw to its [Known Exploited Vulnerabilities Catalog](https://www.bleepingcomputer.com/news/security/cisa-orders-federal-agencies-to-patch-log4shell-by-december-24th/), which also requires expedited action from federal agencies to mitigate the bug until December 24.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=Tor]] [[action.malware.name=Wiper]]

#### Industry:
[[victim.industry.name=Agriculture]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Log4shell]] [[Tellyouthepass]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-44228]]

