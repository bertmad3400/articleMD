# FritzFrog botnet grows 10x, hits healthcare, edu, and govt systems
### The FritzFrog botnet that's been active for more than two years has resurfaced with an alarming infection rate, growing ten times in just a month of hitting healthcare, education, and government systems with an exposed SSH server.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/fritzfrog-botnet-grows-10x-hits-healthcare-edu-and-govt-systems/
+ Date: 2022-02-10T09:08:24-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/02/10/frog.jpg)

![frog](https://www.bleepstatic.com/content/hl-images/2022/02/10/frog.jpg?rand=238790067)


The FritzFrog botnet that's been active for more than two years has resurfaced with an alarming infection rate, growing ten times in just a month of hitting healthcare, education, and government systems with an exposed SSH server.


Discovered in [August 2020](https://www.bleepingcomputer.com/news/security/fritzfrog-malware-attacks-linux-servers-over-ssh-to-mine-monero/), the malware is written in Golang and is considered to be a sophisticated threat that relies on custom code, runs in memory, and is decentralized -- peer-to-peer (P2P), so it does not need a central management server.


Researchers at internet security company Akamai spotted a new version of the FritzFrog malware, which comes with interesting new functions, like using the Tor proxy chain.


The new botnet variant also shows indications that its operators are preparing to add capabilities to target WordPress servers.



![Second campaign having more significant infections than the previous](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/campaign.jpg)**Second campaign having more infections than the first** *(Akamai)*
Next-gen trouble
----------------


Akamai calls FritzFrog a “next-generation” botnet because it combines features that make it stand out from other threats in the same category.


The malware is better equipped to evade detection and keep a low profile due to using a "completely proprietary" P2P protocol for communications.


It relies on an extensive dictionary for brute-force attacks to find SSH credentials, which allows it to compromise a larger number of devices.


FritzFrog is constantly updating the list of targets and breached machines are constantly updated and its node distribution system ensures an equal number of targets to each node to keep the botnet balanced.


Second wave with new abilities
------------------------------


Akamai global network of sensors detected 24,000 attacks but the botnet claimed only 1,500 victims so far. Most of the infected hosts are in China, but among the compromised systems are in a European TV network, a Russian healthcare firm, and various universities in East Asia.



![FritzFrog second campaign victims](https://www.bleepstatic.com/images/news/u/1220909/Nations%20and%20Flags/map(1).jpg)**FritzFrog second campaign victims** *(Akamai)*
The actors have implemented a filtering list to skip low-powered devices such as Raspberry Pi boards, while the malware now contains code that lays the groundwork for targeting WordPress sites.



![Code preparing the implementation of WP detection](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Preliminary code for the implementation of WP detection** *(Akamai)*
Considering that the botnet is known for cryptocurrency mining, this function is a curious addition. However, [Akamai assumes](https://www.akamai.com/blog/security/fritzfrog-p2p) that the actors have found other monetization avenues, such as deploying ransomware, or data leaks. Currently, this capability is inactive as it is being worked on.


The researchers note that FritzFrog is constantly under development, bugs being fixed on a daily basis, sometimes multiple times a day.


Another novelty in the latest FritzFrog sample is proxying outgoing SSH connections through Tor, obscuring the network structure and limiting the visibility from infected nodes to the botnet network. Although this feature looks complete, the developers have yet to activate it.


Finally, the copying system (used to infect new systems) is now based on SCP (security copy protocol), replacing the *cat* command present in the previous version.


Clues point to operators in China
---------------------------------


At this time, the threat analysts at Akamai don’t have a definitive attribution for the operation of FritzFrog, but the evidence points to China.


Because the malware incorporates unique code components, some can be traced to unique GitHub repositories set up by Shanghai-based users.


Moreover, the wallet addresses linked to the second campaign's mining operations were also used in the Mozi botnet, which was eventually confirmed to originate from China.


Finally, roughly 37% of all of FritzFrog's active nodes are located in China, which may mean that the actor operates from there.


Defense strategy
----------------


FritzFrog targets any device that exposes an SSH server, so admins of data center servers, cloud instances, and routers need to stay vigilant.


Akamai shares the following indicators of FritzFrog running on a system:


* Running processes named nginx, ifconfig, php-fpm, apache2, or libexec, whose executable file no longer exists on the file system
* Listening on port 1234
* TCP traffic over port 5555 can indicate network traffic to the Monero pool

Akamai's security recommendations are:


* Enable system login auditing with alerting
* Monitor the authorized\_hosts file on Linux
* Configure explicit allow list of SSH login
* Disable root SSH access
* Enable cloud-based DNS protection with threats and unrelated business applications such as coin mining set to block





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=ifconfig]] [[action.malware.name=Net]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Healthcare]] [[victim.industry.name=Mining]]

#### Location:
[[victim.continent.name=Asia]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Fritzfrog]] [[Botnet]] [[Ssh]] [[Malware]] [[(akamai)]] [[Bleeping Computer]]

