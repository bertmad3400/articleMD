# FritzFrog botnet returns to attack healthcare, education, government sectors | ZDNet
### The botnet managed to strike at least 500 government and enterprise SSH servers in eight months.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/fritzfrog-botnet-strikes-healthcare-education-government-sectors/
+ Date: 2022-02-10 14:00:00
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/7b2e093917fa73490365ebd31e1919a87c2b183b/2021/07/23/7a429a9c-d2fa-400a-ba78-4b68185b54d5/cloud-security-malware.jpg?width=770&height=578&fit=crop&auto=webp)

The FritzFrog botnet has reappeared with a new P2P campaign, showing growth of 10x within only a month.

FritzFrog is [a peer-to-peer botnet](https://www.zdnet.com/article/new-fritzfrog-p2p-botnet-has-breached-at-least-500-enterprise-government-servers/)¬†discovered in January 2020. Over a period of eight months, the botnet managed to strike at least 500 government and enterprise SSH servers.


The P2P botnet, written in the Golang programming language, is decentralized in nature and will attempt to brute-force servers, cloud instances, and other devices -- including routers -- that have exposed entry points on the internet.¬† 

On Thursday, cybersecurity researchers from [Akamai Threat Labs](https://www.akamai.com/our-thinking/threat-research) said that despite having gone quiet after its previous attack wave, since December, the botnet has reappeared with an exponential growth surge.¬† 

"FritzFrog propagates over SSH," the researchers say. "Once it finds a server's credentials using a simple (yet aggressive) brute force technique, it establishes an SSH session with the new victim and drops the malware executable on the host. The malware then starts listening and waiting for commands." 

In total, 24,000 attacks have been detected to date. And 1,500 hosts have been infected, the majority of which are located in China. The botnet is used to mine for cryptocurrency.

Healthcare, education, and government sectors are all on the target list. Thanks to new functionality and the usage of a proxy network, the malware is also being prepared to hone in on websites running the WordPress content management system (CMS).¬† 






A TV channel in Europe, a Russian healthcare equipment manufacturer, and universities in Asia have been compromised.¬† 


Akamai considers FritzFrog a "next-generation" botnet due to a number of key features. This includes consistent update and upgrade cycles, an extensive dictionary used in brute-force attacks, and its decentralized architecture, which is described as "proprietary." In other words, the botnet doesn't rely on other P2P protocols to function.¬† 

The latest FritzFrog is updated daily -- sometimes more than once a day. Alongside bug fixes, the operators have included the new WordPress function to add websites based on this CMS to a target list. 

However, at the time of writing, the lists are empty, which suggests this is an attack feature in the development pipeline.¬† 

Akamai isn't certain of the botnet's origin, but there are some indicators that the operators are either based in China or are impersonating operators in the country. A newly-added file transfer library, for example, links to a GitHub repository owned by a user in Shanghai.¬† 

In addition, the botnet's cryptocurrency mining activity links to wallet addresses also used by the Mozi botnet, in which operators were arrested in China.¬† 

The cybersecurity firm has provided a FritzFrog detection tool [on GitHub](https://github.com/guardicore/labs_campaigns/blob/master/FritzFrog/detect_fritzfrog.sh).

### **Previous and related coverage**

* [Mirai splinter botnets dominate IoT attack scene](https://www.zdnet.com/article/mirai-splinter-botnets-dominate-iot-attack-scene/)
* [This ransomware-spreading malware botnet just won't go away](https://www.zdnet.com/article/this-ransomware-spreading-malware-botnet-just-wont-go-away/)
* [Dark web crooks are now teaching courses on how to build botnets](https://www.zdnet.com/article/college-for-cyber-criminals-dark-web-crooks-are-teaching-courses-on-how-to-build-botnets/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Healthcare]] [[victim.industry.name=Mining]]

#### Location:
[[victim.continent.name=Asia]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Botnet]] [[Fritzfrog]] [[Malware]] [[P2p]] [[Ssh]] [[ZDNet]]

