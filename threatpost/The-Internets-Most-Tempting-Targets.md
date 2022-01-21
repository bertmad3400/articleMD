# The Internet’s Most Tempting Targets
### What attracts the attackers? David moose Wolpoff, CTO at Randori, discusses how to evaluate your infrastructure for juicy targets.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177869
+ Date: 2022-01-21T21:03:23+00:00
+ Author: David \u201cmoose\u201d Wolpoff


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/21160156/peach-fruit-e1642798953322.jpg)

The number of exposed assets keeps climbing, but existing security strategies aren’t keeping up. Attack surfaces are getting more complex, and the excruciatingly hard part is figuring out where to focus.  For every 1,000 assets on an attack surface, there is often only one that’s truly interesting to an attacker. But how is a defender supposed to know which one that is?


This becomes especially difficult in the wake of[Log4j](https://www.randori.com/log4j/). Even [Jen Easterly](https://twitter.com/CISAJen/status/1470542712394989574) made a point to remind people that enumerating what’s on your attack surface is a key way to mitigate a Log4j incident.


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/21151630/Untitled.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/21151630/Untitled.png)


I’m a pretty busy person, so I’m always seeking out the path of least resistance — as are most attackers. We have to operate within limited budgets, and our technical capabilities have an upper bound — we’re not magicians. This is where flipping your perspective will help not only identify what’s exposed on your attack surface, but also what’s most likely to be targeted by an attacker. I guarantee it will dramatically improve your team’s efficiency, reduce overall risk and ensure you’re always focused on the highest value assets first.


 


[Randori](https://www.randori.com/ebooks/2021-attack-surface-report-the-internets-most-tempting-targets/) spent some time researching what internet-exposed software is most tempting to an attacker—we use six attributes we assess to determine a piece of software’s Temptation Score: enumerability, exploitability, criticality, applicability, post-exploitation potential, and research potential. Using some math and fancy algorithms we end up with a “Target Temptation” Score—basically calculating the attackability of an internet-facing asset.


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/21151624/Untitled-1.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/21151624/Untitled-1.png)


Using these assessments, we created a list of some of the more juicy targets we see on the web, and why.


Temptation Roll Call
--------------------


**Anything known to be using Log4j.** Log4j took the security community by storm as it’s one of the most widely used pieces of third-party code and extremely easy to exploit. Our attack team had an exploit within the hour, and was able to use it in live [VMware environments](https://www.randori.com/blog/vmsa-2021-0028-vmware-log4shell-impact-remediations/) the same day. Even though the security community rallied as fast as it could to apply patches and remediation strategies, there are likely some services still running vulnerable code. Because it’s so easy to exploit and new variations of the Log4Shell vulnerability are likely to emerge, it’s going to rank high on any attacker’s list.


**VPNs, my personal favorite.** VPNs are known to protect things of value, making them intrinsically interesting, yet they are often unpatched, misconfigured and not well protected. One cannot install any software on a VPN to defend it. If an attacker exploits this one device, they can reach out to additional devices it was protecting. They are known to be [targets for exploitation](https://www.randori.com/blog/cve-2021-3064/) too; in fact we discovered a [9.8 CVE on Palo Alto’s Global Protect product](https://www.randori.com/blog/cve-2021-3064/).


**Older versions of Solarwinds.** Despite all the attention on SolarWinds, one in 15 organizations appear to be running vulnerable versions of the software. Attackers likely put it top of their list because 1) there is a known exploit; 2) Solarwinds is typically a mission-critical technology for a business that could give an attacker privileged access; and 3) it’s widely used. One exploit could be used against many.


**Old versions of Microsoft IIS 6.** [Microsoft IIS](https://www.iis.net/) 6 has NOT been supported for more than half a decade. That’s right, half a decade! Attackers love old exposed software that is no longer supported. Our data shows 15 percent of companies have at least one instance of IIS 6 exposed online. Microsoft’s IIS version 6 is associated with Windows 2003, and Microsoft stopped supporting it in 2015. In 2015! With lots of known public weaknesses and high applicability, IIS 6 is something some might assume is a honeypot, but an attacker knows better—it’s a juicy target.


**Older versions of Microsoft OWA.** Microsoft’s Outlook Web Access (OWA) is a very widely used solution with lots and lots of publicly known CVEs. Remember the [Windows Exchange breach from last year](https://borncity.com/win/2021/03/03/exchange-server-0-day-exploits-werden-aktiv-ausgenutzt-patchen/) that impacted 30,000 companies? Despite the risks, many companies continue to have OWA exposed to the internet. [Several known vulnerabilities](https://support.microsoft.com/en-us/topic/description-of-the-security-update-for-microsoft-exchange-server-2019-2016-and-2013-march-2-2021-kb5000871-9800a6bb-0a21-4ee7-b9da-fa85b3e1d23b) can provide attacker’s with remote access and are known to be actively exploited.


Another thing: The more an attacker knows about a system, the more tempting it is. One aspect that often drives up OWA temptation scores for instance is the use of default settings that expose detailed version information. Services which expose the name, version, and better yet, configuration information, make it easier for an attacker to cross-check to see if there are any known public vulnerabilities or exploits weaponized against that specific version and to confirm if an exploit will land.


Pro tip: Always change the default settings so that the version number isn’t publicly visible. If you can’t patch it or upgrade it, at least hide it.


The Defender’s Move
-------------------


There’s a bit of an equation that goes into deciding what the most tempting targets are on an attack surface. While there isn’t an exact list of attributes an adversary uses to determine what to exploit, the logic above is pretty universal among attackers.


No system will ever be fully secure, but limiting the information attackers can get their hands on out of the gate goes a long way toward taking the wind out of their sails. This means burying the truly crucial information behind so many fail safes that it isn’t worth the effort for an attacker. This can mean adding logging/monitoring, web application firewalls or segmentation to critical assets on an attack surface — or even taking systems offline entirely if they don’t need to communicate with the internet.


As always, good ole-fashioned network segmentation and defense in depth will get better results than what you’d be getting otherwise.


***David “moose” Wolpoff  is CTO at [Randori.](https://www.randori.com/)***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by visiting our [microsite](https://threatpost.com/microsite/infosec-insiders-community/).***





## Tags:

#### Threatactor:
[[threatactor.name=Equation]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Iis]] [[Log4j]] [[Owa]] [[ThreatPost]]

