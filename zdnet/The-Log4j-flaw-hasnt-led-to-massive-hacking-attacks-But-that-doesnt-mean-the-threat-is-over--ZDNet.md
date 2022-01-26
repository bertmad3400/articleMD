# The Log4j flaw hasn't led to massive hacking attacks. But that doesn't mean the threat is over | ZDNet
### An early analysis of Log4Shell suggests quick action by tech vendors and open-source software developers averted a crisis. But the bug will lurk in systems for years to come.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/the-log4j-flaw-hasnt-led-to-massive-hacking-attacks-but-that-doesnt-mean-the-threat-is-over/
+ Date: 2022-01-26 11:46:00
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/319bb942a569da4250335330f3f70add34110be3/2020/07/24/a7802dcb-d40d-440d-bb86-0ef1c7490d5f/istock-1210442293.jpg?width=770&height=578&fit=crop&auto=webp)

Log4Shell affected hundreds of millions of devices and was cast as a critical tech emergency that would almost certainly be exploited attackers around the globe. 

But a month after the Apache Software Foundation disclosed Log4Shell in its Log4J library on December 9, the US Cybersecurity and Infrastructure Security Agency (CISA) said it [hasn't seen any major breach arise from the attack](https://www.zdnet.com/article/cisa-director-we-have-not-seen-significant-intrusions-from-log4j/), with the exception of an attack on the Belgian Defense Ministry. 


The reason for the initial concern was that the Java-based application error logging component was embedded in so many in-house enterprise applications and hundreds of products from VMWare, Oracle, IBM, Cisco and others.

**SEE:** [**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/#link=%7B%22role%22:%22standard%22,%22href%22:%22http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/%22,%22target%22:%22_blank%22,%22absolute%22:%22%22,%22linkText%22:%22%3Cstrong%3EA%20winning%20strategy%20for%20cybersecurity%3C/strong%3E%22%7D) **(ZDNet special report)**

Despite this, exploits using the vulnerability have been limited. For example, security firm Rapid7 saw a surge in [exploit attempts against VMWare's Horizon servers](https://www.zdnet.com/article/log4j-attackers-continue-targeting-vmware-horizon-servers/) and Microsoft also observed a China-based [double extortion ransomware gang NightSky targeting vulnerable instances of Horizon](https://www.zdnet.com/article/ransomware-warning-hackers-are-using-log4j-flaw-as-part-of-their-attacks-warns-microsoft/).  

Despite the absence of immediate mass exploitation, Sophos security's Chester Wisniewski backs the view that it will be a target for exploitation for years to come. 

Microsoft [continues to rate the Log4j vulnerabilities](https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/#nation-state) as a "high-risk situation" for companies across the globe and reckons there is high potential for their expanded use. But for now, Wisniewski believes an immediate crisis has been swerved.   






"[T]he immediate threat of attackers mass exploiting Log4Shell was averted because the severity of the bug united the digital and security communities and galvanised people into action. This was seen back in 2000 with the Y2K bug and it seems to have made a significant difference here," [says Wisniewski](https://news.sophos.com/en-us/2022/01/24/log4shell-no-mass-abuse-but-no-respite-what-happened/).

Sophos detected a huge surge in internet-scanning activity in mid-December – conducted by researchers or threat actors – that petered out by the end of January, when most exploitation was by crypto coin-mining malware. 

While Log4Shell is easy to exploit on some systems, Log4J is embedded in many applications, making actual exploitation more challenging. 

"Another factor to consider when evaluating the scanning numbers is that a Log4Shell type of flaw is exploited differently based on which application the Log4J code is in and how it has been integrated with that application. This results in a high volume of redundant scans trying different ways to exploit different applications," says Wisniewski. 

CISA warned, however, that attackers might be waiting to use access gained through Log4Shell until alert levels fall. That is, attackers could lay dormant within a network, waiting to deploy malware months later. Wisniewski supports CISA's cautionary stance.

"Sophos has observed countries such as Iran and North Korea pounce on VPN vulnerabilities to gain access to targets' networks and install backdoors before the targets have had a chance to deploy the patches, and then waiting months before using that access in an attack," he says. 

As for the duration of Log4Shell, Wisniewski reckons internet-facing applications will be found and patched or taken offline. But that still leaves a ton of internally vulnerable systems that might never be discovered, hence Log4Shell will live on for years as a favorite target for penetration testers and state-backed threat actors. 

Though not the first major open-source software to rattle the internet, it did prompt [talks in January between major tech players and the White House](https://www.zdnet.com/article/after-log4j-white-house-worries-about-the-next-big-open-source-flaw/) aimed at figuring out how to respond to and avert the next major open-source bug, in particular the transparency of the software supply chain.   





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4shell]] [[Wisniewski]] [[Log4j]] [[ZDNet]]

