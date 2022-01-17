# Earth Lusca threat actor targets governments and cryptocurrency companies alike
### Cybersecurity researchers said they discovered a Chinese cyber-espionage group that, besides spying on strategic targets, also dabbled in financially-motivated attacks for their own profits.

## Information:
+ Source: The Record
+ Link: https://therecord.media/earth-lusca-threat-actor-targets-governments-and-cryptocurrency-companies-alike/
+ Date: 2022-01-17T15:51:26+00:00
+ Author: Catalin Cimpanu


## Article:
![Article Image](https://therecord.media/wp-content/uploads/2022/01/octopus-lusca-tentacles.jpg)

Cybersecurity researchers said they discovered a Chinese cyber-espionage group that, besides spying on strategic targets, also dabbled in financially-motivated attacks for their own profits.


Named**Earth Lusca**, the group has spent the past years spying on targets that could be considered of interest to the Chinese government, such as:


* Government institutions in Taiwan, Thailand, Philippines, Vietnam, United Arab Emirates, Mongolia, and Nigeria
* Educational institutions in Taiwan, Hong Kong, Japan, and France
* News media in Taiwan, Hong Kong, Australia, Germany, and France
* Pro-democracy and human rights political organizations and movements in Hong Kong
* Covid-19 research organizations in the United States
* Telecom companies in Nepal
* Religious movements that are banned in Mainland China


But while its primary activity has focused on intelligence collection, in a [report](https://www.trendmicro.com/en_us/research/22/a/earth-lusca-sophisticated-infrastructure-varied-tools-and-techni.html) released today, security firm Trend Micro says the group also orchestrated attacks against gambling companies in China and various cryptocurrency platforms, from where the group exfiltrated funds in attacks that appeared to be purely financially motivated.


### APT41, is that you?


The discovery of a government espionage group engaging in financially-motivated attacks would normally be a big finding, except it has recently become a pattern for threat actors to dabble in both.


For example, threat actors from Iran have been seen hacking into VPN devices across the globe, selecting important targets for intelligence collection, and selling off the excess on underground forums frequented by ransomware gangs.


North Korean threat actors are in their own category here, some of them being assigned and mandated by the state itself to engage in bank and cryptocurrency heists as a way to [raise money](https://therecord.media/north-korean-hackers-stole-nearly-400m-in-cryptocurrency-in-2021/) for the Pyongyang regime, which has been under heavy economic sanctions for the past three decades.


As for China, this duality in some of its espionage operations has also been seen before—in FireEye’s report on [APT41 (aka Double Dragon)](https://www.mandiant.com/resources/report-apt41-double-dragon-a-dual-espionage-and-cyber-crime-operation).


In fact, many of Earth Lusca’s tactics and attacks seem to perfectly describe APT41’s past and newer operations, and Earth Lusca may be another view into APT41 from Trend Micro’s angle, again confirming that APT41 is one of the largest and most active threat actors today.


### Phishing, watering hole attacks, and server exploitation


As for how Earth Lusca conducted its recent operations, Trend Micro said the group primarily used three methods during the attacks they have recently observed:


1. Exploiting unpatched vulnerabilities in public-facing servers and web applications (common targets included Oracle GlassFish and Microsoft Exchange servers)
2. Sending spear-phishing emails that contain links to malicious files or sites to targeted organizations.
3. Watering hole attacks, where they lure victims on compromised sites that attempt to infect the victims with malware.


Trend Micro said that in most cases, the attackers tried to deploy a version of Cobalt Strike on infect hosts. A tool used by security researchers to simulate attacks, Cobalt Strike has been widely adopted and abused by threat actors in recent years, which use it as a first point of infection and as a way to deploy additional malware.


Second-stage payloads spotted deployed by Earth Lusca this way included:


* the [Doraemon](https://www.welivesecurity.com/2021/08/24/sidewalk-may-be-as-dangerous-as-crosswalk/) backdoor
* the [ShadowPad](https://www.sentinelone.com/labs/shadowpad-a-masterpiece-of-privately-sold-malware-in-chinese-espionage/) backdoor
* the [Winn](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/higaisa-or-winnti-apt-41-backdoors-old-and-new/)[t](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/higaisa-or-winnti-apt-41-backdoors-old-and-new/)[i](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/higaisa-or-winnti-apt-41-backdoors-old-and-new/) backdoor
* the [FunnySwitch](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/higaisa-or-winnti-apt-41-backdoors-old-and-new/) backdoor
* the [AntSword](https://otx.alienvault.com/pulse/5e3844a3cf5bbf510c482c3f/history) web shell
* the [Behinder](https://www.fortiguard.com/encyclopedia/ips/49306) web shell


In addition, researchers also noted that the group also deployed cryptominers on infected hosts, although it remains unclear if they did so with the intention to generate funds for themselves or as a way to throw off security teams that may discover one of their intrusions, hoping to lead investigators to believe the hack was a mundane crypto-mining botnet and not a sophisticated cyber-espionage operation.





## Tags:

#### Threatactor:
[[threatactor.name=APT41]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=ShadowPad]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Finance]] [[victim.industry.name=Information]] [[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Niger]] [[victim.continent.name=Africa]] [[victim.country.name=Nigeria]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.country.name=Japan]] [[victim.continent.name=Asia]] [[victim.country.name=Mongolia]] [[victim.continent.name=Asia]] [[victim.country.name=Nepal]] [[victim.continent.name=Asia]] [[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.city.name=Pyongyang]] [[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Philippines]] [[victim.continent.name=Asia]] [[victim.country.name=Thailand]] [[victim.continent.name=Asia]] [[victim.country.name=Taiwan]] [[victim.continent.name=Asia]] [[victim.country.name=United Arab Emirates]] [[victim.continent.name=Asia]] [[victim.country.name=Vietnam]] [[victim.continent.name=Asia]] [[victim.country.name=Germany]] [[victim.continent.name=Europe]] [[victim.country.name=France]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Australia]] [[victim.continent.name=Oceania]] [[victim.country.name=Australia]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Lusca]] [[Apt41]] [[Backdoorthe]] [[The Record]]

