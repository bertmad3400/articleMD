# Silent danger: One in five aged domains is malicious, risky, or unsafe
### The number of malicious dormant domains is on the rise, and as researchers warn, roughly 22.3% of strategically aged domains pose some form of danger.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/silent-danger-one-in-five-aged-domains-is-malicious-risky-or-unsafe/
+ Date: 2021-12-29T15:42:14-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/29/Internet_domain.jpg)

![Silent danger: One in five aged domains is malicious, risky, or unsafe](https://www.bleepstatic.com/content/hl-images/2021/12/29/Internet_domain.jpg)


The number of malicious dormant domains is on the rise, and as researchers warn, roughly 22.3% of strategically aged domains pose some form of danger.


This was a realization that struck analysts when it was revealed that the SolarWinds threat actors relied on domains registered years before their malicious activities began.


Based on that, efforts in detecting strategically aged domains before they get the chance to launch attacks and support malicious activities have picked up pace.


A report from Palo Alto Networks' Unit42 reveals their researchers' findings after looking at tens of thousands of domains each day throughout September 2021.


They concluded that approximately 3.8% are straight-out malicious, 19% are suspicious, and 2% are unsafe for work environments.



![Percentage of suspicious domains among those analyzed](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/pie.jpg)**Percentage of suspicious domains among those analyzed**  
*Source: Unit42*
Why let a domain age
--------------------


The goal behind registering a domain long before the threat actors will use it is to create a "clean record" that will prevent security detection systems from undermining the success of malicious campaigns.


Typically, newly registered domains (NRDs) are [more likely to be malicious](https://www.bleepingcomputer.com/news/security/fbi-warns-of-newly-registered-domains-spoofing-us-census-bureau/), so security solutions treat them as suspicious and have more chances to flag them.


However, Unit42 explains in its report that strategically aged domains are three times more likely to be malicious than NRDs.


In some cases, these domains stayed dormant for two years before their DNS traffic suddenly increased by 165 times, indicating the launch of an attack.


Signs of “snake eggs”
---------------------


An obvious sign of a malicious domain is the sudden spike in its traffic. Legitimate services that registered their domains and launched services months or years later exhibit gradual traffic growth.


The domains that weren’t destined for legitimate use generally have incomplete, cloned, or generally questionable content. As expected, WHOIS registrant details are missing too.



![DGA-spawned website hosting suspicious content](https://www.bleepstatic.com/images/news/u/1220909/Website%20snaps/content.png)**DGA-spawned website hosting suspicious content**  
*Source: Unit42*
Another clear sign of a purposefully aged domain that is meant to be used in malicious campaigns is DGA subdomain generation.


DGA (domain generation algorithm) is [an established method](https://www.bleepingcomputer.com/news/security/ad-network-uses-dga-algorithm-to-bypass-ad-blockers-and-deploy-in-browser-miners/) of generating unique domain names and IP addresses to serve as new C2 communication points. The goal is to [evade detection](https://www.bleepingcomputer.com/news/security/dmsniff-point-of-sale-malware-silently-attacked-smbs-for-years/) and blocklists.


By looking at the DGA element alone, Palo Alto’s detectors identified two suspicious domains each day, spawning hundreds of thousands of subdomains on the day of its activation.


Real examples
-------------


One notable case captured by Unit42 in September was a Pegasus spying campaign that used two C2 domains registered in 2019 and awoke in July 2021.


DGA domains played a vital role in that campaign, carrying 23.22% of the traffic on the activation day, which spiked 56 times higher than normal DNS traffic volumes. A few days later, DGA traffic reached 42.04% of the total.



![Traffic spike in Pegasus campaign](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Traffic spike in Pegasus campaign**  
*Source: Unit42*
Other real-world examples detected by the researchers include phishing campaigns that used DGA subdomains as cloaking layers that will direct ineligible visitors and crawlers to legitimate sites while pushing victims to the phishing pages.


This shows that these DGAs serve not only as C2 domains but also as proxy layers that can be explicitly configured to the campaign's needs.


Finally, there were also cases of wildcard DNS abuse, with multiple subdomains all pointing to the same IP address.


“These hostnames serve randomly generated websites that fill out some website templates with random strings,” details the [Unit42 report](https://unit42.paloaltonetworks.com/strategically-aged-domain-detection/). 


“They could be used for black hat SEO. Specifically, these web pages link to each other to obtain a high rank from search engine crawlers without providing valuable information.”


In most cases, strategically aged domains are used by sophisticated actors who operate in a more organized context and have long-term plans.


They're used for leveraging DGA to exfiltrate data through DNS traffic, serve as proxy layers, or mimic the domains of well-known brands (cybersquatting).


Although detecting DGA activity is still challenging, defenders can achieve a lot by monitoring DNS data like queries, responses, and IP addresses and focusing on identifying patterns.





## Tags:

#### Threatactor:
[[threatactor.name=Turla]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Dga]] [[Unit42]] [[Dns]] [[Ip]] [[C2]] [[Bleeping Computer]]

