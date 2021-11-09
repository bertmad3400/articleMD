# TeamTNT hackers target your poorly configured Docker servers
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/teamtnt-hackers-target-your-poorly-configured-docker-servers/)
+ Date: November 9, 2021
+ Author: Bill Toulas


## Article:
![dockerhub](https://www.bleepstatic.com/content/hl-images/2021/11/09/DockerHub.jpg?rand=1805089743)


Poorly configured Docker servers and being actively targeted by the TeamTNT hacking group in an ongoing campaign started last month.


According to a report by researchers at TrendMicro, the actors have three distinct goals: to install Monero cryptominers, scan for other vulnerable Internet-exposed Docker instances, and perform container-to-host escapes to access the main network.


As illustrated in an attack workflow, the attack starts with creating a container on the vulnerable host using an exposed Docker REST API.



![TeamTNT Docker abuse workflow](https://www.bleepstatic.com/images/news/security/attack-workflow.jpg)**TeamTNT Docker abuse workflow**  
*Source: TrendMicro*
TeamTNT then uses compromised, or actor-controlled Docker Hub accounts to host malicious images and deploy them on a targeted host.


TrendMicro has seen over 150,000 pulls of images from the malicious Docker Hub accounts as part of this campaign.


Next, the dropped container executes cronjobs and fetches various post-exploitation and lateral movement tools, including container escaping scripts, credential stealers, and cryptocurrency miners.


When scanning for other vulnerable instances, the threat actors check ports 2375, 2376, 2377, 4243, 4244, which has been observed in past DDoS botnet campaigns.


The actors also attempt to collect server info such as the OS type, architecture, number of CPU cores, container registry, and the current swarm participation status.


The container image that is created is based on the AlpineOS system and is executed with flags that allow root-level permissions on the underlying host.



![Similarities between old and past container samples](https://www.bleepstatic.com/images/news/u/1220909/Security/similarities.png)**Similarities between old and past container image samples**  
*Source: TrendMicro*
Finally, the IP address that is used for TeamTNT’s current infrastructure (45[.]9[.]148[.]182) has been associated with multiple domains that served malware in the past.


Previous campaign laid the groundwork
-------------------------------------


TrendMicro reports that this campaign also uses compromised Docker Hub accounts controlled by TeamTNT to drop malicious Docker images.


Using compromised Docker Hub accounts makes the distribution points more reliable for the actors, as they are harder to map, report, and takedown.


The actors were spotted collecting Docker Hub credentials in a previous campaign analyzed by TrendMicro [in July](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/teamtnt-activities-probed) when credentials stealers were deployed in attacks.


"Our [July 2021 research](https://www.trendmicro.com/vinfo/tmr/?/us/security/news/cybercrime-and-digital-threats/teamtnt-activities-probed) into TeamTNT showed that the group previously used credential stealers that would rake in credentials from configuration files. This could be how TeamTNT gained the information it used for the compromised sites in this attack," explains [TrendMicro's research](http://www.trendmicro.com/en_us/research/21/k/compromised-docker-hub-accounts-abused-for-cryptomining-linked-t.html) published today.


As such, TeamTNT demonstrates a high level of operational planning, being organized and purposeful in their goals.


Permanent threat to Docker systems
----------------------------------


TeamTNT is a sophisticated actor that constantly evolves its techniques, shifts short-term targeting focus but remains a constant threat to vulnerable Docker systems.


They first created a worm to [exploit Docker and Kubernetes](https://www.bleepingcomputer.com/news/security/cryptojacking-worm-steals-aws-credentials-from-docker-systems/) en masse back in August 2020.


In October 2020, the actors [added Monero mining](https://www.bleepingcomputer.com/news/security/crypto-mining-malware-adds-linux-password-stealing-capability/) and credential-stealing capabilities, targeting Docker instances.


In January 2021, TeamTNT upgraded its miners with [sophisticated detection evasion tricks](https://www.bleepingcomputer.com/news/security/linux-malware-uses-open-source-tool-to-evade-detection/) while still harvesting user credentials from the compromised servers.


Docker provides some "mandatory" tips that can be used lock down Docker's REST API and prevent these types of attacks.


"Therefore it is *mandatory* to secure API endpoints with [HTTPS and certificates](https://docs.docker.com/engine/security/protect-access/). It is also recommended to ensure that it is reachable only from a trusted network or VPN," explains Docker's [security guide](https://docs.docker.com/engine/security/).




#### Tags:
[[TeamTNT]] [[TrendMicro]] [[Bleeping Computer]]
