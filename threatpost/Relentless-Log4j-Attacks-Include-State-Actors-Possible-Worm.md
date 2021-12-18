# Relentless Log4j Attacks Include State Actors, Possible Worm
### More than 1.8 million attacks, against half of all corporate networks, have already launched to exploit Log4Shell.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177088
+ Date: 2021-12-15T23:18:44+00:00
+ Author: Becky Bracken


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/15175859/logjam-e1639609200547.jpeg)

Call it a “logjam” of threats: Attackers including nation-state actors have already targeted half of all corporate global networks in security companies’ telemetry using at least 70 distinct malware families — and the fallout from the Log4j vulnerability is just beginning.


Researchers manning keyboards all over the world have spent the past several days chasing [attacks aimed at a now-infamous Log4j](https://threatpost.com/log4shell-attacks-origin-botnet/176977/) Java library bug, dubbed [Log4Shell (CVE-2021-44228).](https://threatpost.com/apache-log4j-log4shell-mutations/176962/) Side note: Log4j is pronounced, “log forge” — although that’s disputed, because it’s also referred to in conversation as “log-four-jay.” Dealer’s choice there.


First discovered among Minecraft players last week, the newly discovered vulnerability has opened a massive opportunity for threat actors to hijack servers, mostly with coin miners and botnets, but also a cornucopia of other malware such as the [StealthLoader trojan](https://blog.checkpoint.com/2021/12/14/a-deep-dive-into-a-real-life-log4j-exploitation/) — and that’s just so far.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“We’ve seen a lot of chatter on Dark Web forums, including sharing scanners, bypasses and exploits,” Erick Galinkin, an artificial intelligence researcher at Rapid7, told Threatpost. “At this point, more than 70 distinct malware families have been identified by us and other security researchers.”


For instance, Bitdefender researchers this week [discovered](https://businessinsights.bitdefender.com/technical-advisory-zero-day-critical-vulnerability-in-log4j2-exploited-in-the-wild) that threat actors are attempting to exploit Log4Shell to deliver a new ransomware called Khonsari to Windows machines.


Check Point research reported Wednesday that since last Friday, its team has detected 1.8 million Log4j [exploit attempts](https://blog.checkpoint.com/2021/12/11/protecting-against-cve-2021-44228-apache-log4j2-versions-2-14-1/) on almost half of all corporate networks that they track.


These threat actors aren’t low-skilled hobbyists. Check Point added that as of Wednesday, Iranian hacking group Charming Kitten, also known as APT 35 and widely believed to be working as a [nation-state actor](https://blog.checkpoint.com/2021/12/11/protecting-against-cve-2021-44228-apache-log4j2-versions-2-14-1/), is actively targeting seven specific Israeli organizations across the government and business sectors.


“Our reports of the last 48 hours prove that both criminal-hacking groups and nation state actors are engaged in the exploration of this vulnerability, and we should all assume more such actors’ operations are to be revealed in the coming days,” Check Point added.


Microsoft meanwhile reported that nation-state groups Phosphorus (Iran) and [Hafnium](https://threatpost.com/microsoft-exchange-zero-day-attackers-spy/164438/) (China), as well as unnamed APTs from North Korea and Turkey are actively exploiting Log4Shell (CVE-2021-44228) in targeted attacks. Hafnium is known for targeting Exchange servers with the ProxyLogon zero-days back in March, while Phosphorus [made headlines](https://threatpost.com/microsoft-iranian-apt-t20-summit-munich-security-conference/160654/) for targeting global summits and conferences in 2020.


“This activity ranges from experimentation during development, integration of the vulnerability to in-the-wild payload deployment and exploitation against targets to achieve the actor’s objectives,” the company said in [a posting](https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/).


**Is a Log4j Worm Next?**
-------------------------


Researcher Greg Linares meanwhile has reported seeing evidence that a self-propagating worm is being developed and will likely emerge in a day or less.




There is wide agreement within the cybersecurity community that he’s correct, but many experts don’t think the fallout will be as bad with Log4j as it was with past incidents like [WannaCry or NotPetya](https://threatpost.com/one-year-after-wannacry-a-fundamentally-changed-threat-landscape/132047/).


“While it’s possible that we could see a worm developed to spread among susceptible Log4j devices, there hasn’t been any evidence to suggest this is a priority for threat actors at this time,” Chris Morgan, senior cyber threat intelligence analyst at Digital Shadows, told Threatpost. “Developing malware of this nature takes a significant amount of time and effort.”


“This activity differs from the WannaCry incident, which saw a perfect storm of a highly exploitable vulnerability coinciding with an NSA-level exploit breach in EternalBlue,” Morgan added.


“It’s still very much early days with regards to Log4j,” Morgan said. “While many threat actors will likely be at different stages of the kill chain, most actors will likely still be scanning for susceptible systems, attempting to establish a foothold, and identifying further opportunities, depending on their motivations. Efforts among actors at this stage are rushing to exploit before companies have a chance to patch, rather than spending time developing a worm.”


The emergence of a Log4j worm isn’t the worst-case scenario, researchers like Yaniv Balmas from Salt Security explained to Threatpost.


“While not neglecting the impact of such a worm, that might not be the worst scenario because of the unbelievable easiness that this attack can be applied,” Balmas said. “Everyone with a basic computer and internet access could launch an attack against millions of online services within minutes. This achieves quite a similar impact as a worm – it is distributed and unpredictable, and the damage extent might even be higher than a worm since a worm works ‘blindly’ in an automated manner.”


He added, “in this other scenario, there are actual humans behind the attacks which may target specific entities or institutions and enable attackers to fine-tune their attacks as they progress.”


The tireless work being done by security teams to [patch up Log4j against exploits](https://threatpost.com/patching-time-log4j-exploits-vaccine/177017/) is a big help against the development of any worms on the horizon, John Bambenek, principal threat hunter at Netenrich, told Threatpost.


“This vulnerability certainly looks wormable, however, the good news is we’ve already had almost a week to start dealing with detection, mitigation [and patching](https://threatpost.com/apache-patch-log4shell-log4j-dos-attacks/177064/),”Bambenek said. “There will be lots of vulnerable machines out there, but by now a good deal of the vulnerable machines have been handled and many more are protected with web application firewall (WAF) rules (for instance, Cloudflare deployed protection over the weekend). The worst case would have been a worm last week, we’re in a better place now.”


**Log4j’s Long Tail**
---------------------


Beyond emergency patching measures, Galinkin explained to Threatpost that his concern is with lingering unpatched devices and systems that will be vulnerable long after Log4j has fallen out of the headlines, particularly in sectors like academia and healthcare.


“One crucial thing to note about this vulnerability is that it’s going to have an extremely long tail,” he said. “Hospitals tend to purchase software once, but sometimes the vendors become defunct — leading to unsupported software that will never receive a patch.”


He added, “in academia, loads of software is written once by grad students or professors, but those individuals may not be aware of the bug, or they simply no longer maintain the software — software that is in use in physics, pharmacology and bioinformatics. This suggests that we will continue to see exploitation of this vulnerability — potentially in isolated incidents — long into the future.”


121621 16:21 UPDATE: Corrected spelling of John Bambenek’s name.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=HAFNIUM]] [[threatactor.name=Magic Hound]] [[threatactor.name=Magic Hound]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=NotPetya]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]] [[action.malware.name=WannaCry]]

#### Industry:
[[victim.industry.name=Healthcare]] [[victim.industry.name=Healthcare]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.country.name=Israel]] [[victim.continent.name=Asia]] [[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Turkey]] [[victim.continent.name=Asia]] [[victim.country.name=Turkey]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Threatpost]] [[Malware]] [[Nation-state]] [[Log4shell]] [[“this]] [[“while]] [[ThreatPost]]
#### CVE's
[[CVE-2021-44228]]

