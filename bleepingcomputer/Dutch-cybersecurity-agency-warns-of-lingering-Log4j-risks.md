# Dutch cybersecurity agency warns of lingering Log4j risks
### In a warning issued on Thursday, the Dutch National Cybersecurity Centre (NCSC) says organizations should still be aware of risks connected to Log4j attacks and remain vigilant for ongoing threats.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/dutch-cybersecurity-agency-warns-of-lingering-log4j-risks/
+ Date: 2022-01-22T10:00:00-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j___logo.jpg)

![Dutch cybersecurity agency warns of lingering Log4j risks](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j___logo.jpg)


In a warning issued on Thursday, the Dutch National Cybersecurity Centre (NCSC) says organizations should still be aware of risks connected to Log4j attacks and remain vigilant for ongoing threats.


Even though the aftermath of recent incidents connected to Log4Shell exploitation was "not too bad" because many organizations have acted quickly to mitigate these critical vulnerabilities, the NCSC says that threat actors are most likely still planning to breach new targets. 


"It is expected that malicious parties will continue to search for vulnerable systems and carry out targeted attacks in the coming period," the Dutch cybersecurity agency said.


"It is therefore important to remain vigilant. The NCSC advises organizations to continue to monitor whether vulnerable systems are used and to apply updates or mitigating measures where necessary.


"In addition, the NCSC advises directors to stay alert by informing themselves about Log4j and the possible impact of abuse on business continuity."


Log4j vulnerabilities (including [Log4Shell](https://www.bleepingcomputer.com/tag/log4shell/)) are a very appealing attack vector for both financially motivated and state-backed attackers, given that the open-source Apache Log4j logging library is used in a wide range of systems from [dozens of vendors](https://www.bleepingcomputer.com/news/security/log4j-list-of-vulnerable-products-and-vendor-advisories/).


Log4Shell, in particular, can be leveraged remotely on servers exposed to local or Internet access to allow attackers to move laterally through a network until they reach sensitive internal systems.


After its disclosure, [multiple threat actors started deploying Log4Shell exploits](https://www.bleepingcomputer.com/news/security/log4j-vulnerability-now-used-by-state-backed-hackers-access-brokers/), including hacking groups linked to governments in China, Iran, North Korea, and Turkey and access brokers used by ransomware gangs.


Log4j is still under active exploitation
----------------------------------------


NCSC's warning is well-timed, seeing that multiple alerts of ongoing Log4j exploitation around the world were issued by government and private organizations worldwide. 


For instance, a report published by Microsoft on Wednesday mentions attempts made by unknown threat actors [to propagate Log4j attacks](https://www.bleepingcomputer.com/news/microsoft/microsoft-solarwinds-fixes-serv-u-bug-exploited-for-log4j-attacks/) to an organization's internal LDAP servers by exploiting a SolarWinds Serv-U zero-day.


However, the attacks failed because the Windows domain controllers targeted in the incident were not vulnerable to Log4j exploits.


One week earlier, Microsoft warned of a Chinese threat actor tracked as DEV-0401 [using Log4Shell exploits on Internet-exposed VMware Horizon servers](https://www.bleepingcomputer.com/news/security/night-sky-ransomware-uses-log4j-bug-to-hack-vmware-horizon-servers/) to deploy Night Sky ransomware.


"As early as January 4, attackers started exploiting the CVE-2021-44228 vulnerability in internet-facing systems running VMware Horizon," Microsoft said.


"Our investigation shows that successful intrusions in these campaigns led to the deployment of the NightSky ransomware."


Microsoft's reports were preceded by another alert issued by UK's National Health Service (NHS) on January 5 about [attackers targeting VMware Horizon systems with Log4Shell exploits](https://www.bleepingcomputer.com/news/security/nhs-warns-of-hackers-exploiting-log4shell-in-vmware-horizon/).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Turkey]] [[victim.continent.name=Asia]] [[victim.country.name=Turkey]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Log4shell]] [[Ncsc]] [[Microsoft]] [[Ransomware]] [[Vmware]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-44228]]

