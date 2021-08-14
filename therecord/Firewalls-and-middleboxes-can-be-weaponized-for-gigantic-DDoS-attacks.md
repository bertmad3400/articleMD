# Firewalls and middleboxes can be weaponized for gigantic DDoS attacks
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/firewalls-and-middleboxes-can-be-weaponized-for-gigantic-ddos-attacks/)
+ Date: August 13, 2021
+ Author: Catalin Cimpanu


## Article:
![Firewalls and middleboxes can be weaponized for gigantic DDoS attacks](https://therecord.media/wp-content/uploads/2021/08/DDoS-globe.png)

* Academics discover novel DDoS attack vector abusing the TCP protocol.
* Middleboxes like firewalls and DPI boxes can be abused to launch this new form of DDoS attack.
* The new DDoS technique can be used to launch attacks with amplification factors in the realm of 1000x and more.


In an award-winning paper today, academics said they discovered a way to abuse the TCP protocol, firewalls, and other network middleboxes to launch giant distributed denial of service (DDoS) attacks against any target on the internet.


Authored by computer scientists from the University of Maryland and the University of Colorado Boulder, the research is the first of its kind to describe a method to carry out DDoS reflective amplification attacks via the TCP protocol, previously thought to be unusable for such operations.


Making matters worse, researchers said the amplification factor for these TCP-based attacks is also far larger than UDP protocols, making TCP protocol abuse one of the most dangerous forms of carrying out a DDoS attack known to date and very likely to be abused in the future.


#### How DDoS reflective amplification attacks work


But to understand the importance of this research, a short intro to DDoS attacks is also needed. First documented in the early 2000s, DDoS attacks were initially carried out by hijacking home computers to launch requests to websites, all at the same time, in order to overwhelm a victim’s hosting infrastructure.


As the years went by, methods to carry out DDoS attacks also diversified. One of the most dangerous of these methods was the so-called “*DDoS reflective amplification attack*.”


This happens when an attacker sends network packets to a third-party server on the internet, the server processes and creates a much larger response packet, which it then sends to a victim instead of the attacker (thanks to a technique known as IP spoofing).


The technique effectively allows attackers to reflect/bounce and amplify traffic towards a victim via an intermediary point.


Historically, the best DDoS reflective amplification vectors were servers running [UDP-based protocols](https://github.com/Phenomite/AMP-Research), such as SNMP, DNS, NetBIOS, CoAP, and NTP.


The reason was that the UDP protocol uses a simple two-stage request and response process that can be easily abused and weaponized by DDoS botnet operators.


![TCP-DDoS-amp-factor-UDP](https://www-therecord.recfut.com/wp-content/uploads/2021/08/TCP-DDoS-amp-factor-UDP.png)
On the other hand, TCP connections always began with a three-way handshake where attackers couldn’t use the IP spoofing technique as they couldn’t complete the handshake, and servers would drop connections before the attacker could amplify and reflect its payload.


![TCP-DDoS-amp-factor-TCP](https://www-therecord.recfut.com/wp-content/uploads/2021/08/TCP-DDoS-amp-factor-TCP.png)
But in research published today, researchers said that they found a way to abuse the TCP protocol for reflective amplified DDoS attacks for the first time, and with very dangerous consequences.


#### TCP-based reflective amplified DDoS attack vector discovered


The flaw they found was in the design of middleboxes, which are equipment installed inside large organizations that inspect network traffic.


Middleboxes usually include the likes of firewalls, network address translators (NATs), load balancers, and deep packet inspection (DPI) systems.


The research team said they found that instead of trying to replicate the entire three-way handshake in a TCP connection, they could send a combination of non-standard packet sequences to the middlebox that would trick it into thinking the TCP handshake has finished and allow it to process the connection.


![TCP-DDoS-amp-factor-packtes](https://www-therecord.recfut.com/wp-content/uploads/2021/08/TCP-DDoS-amp-factor-packtes.png)
Under normal circumstances, this wouldn’t be an issue, but if the attacker tried to access a forbidden website, then the middlebox would respond with a “block page,” which would typically be much larger than the initial packet—hence an amplification effect.


Following extensive experiments that began last year, the research team said that the best TCP DDoS vectors appeared to be websites typically blocked by nation-state censorship systems or by enterprise policies.


Attackers would send a malformed sequence of TCP packets to a middlebox (firewall, DPI box, etc.) that tried to connect to pornography or gambling sites, and the middlebox would reply with an HTML block page that it would send to victims that wouldn’t even reside on their internal networks—thanks to IP spoofing.


![TCP-DDoS-amp-factor-scheme](https://www-therecord.recfut.com/wp-content/uploads/2021/08/TCP-DDoS-amp-factor-scheme.png)
While the research team tested various universally forbidden websites, they found that five domains, in particular, tended to get responses from most middleboxes on the internet and would be a reliable “trigger” for these attacks:


* **www.youporn.com** (pornography)
* **www.roxypalace.com** (gambling)
* **plus.google.com** (social media)
* **www.bittorrent.com** (file sharing)
* **www.survive.org.uk** (sexual health/education)


![TCP-DDoS-amp-factor-websites](https://www-therecord.recfut.com/wp-content/uploads/2021/08/TCP-DDoS-amp-factor-websites.png)
#### Middleboxes provide huge DDoS amplification factors


But the research team says that not all middleboxes responded to their tests in the same way. Some amplified traffic more than others, while some did not even respond.


In an interview this week, Kevin Bock, a researcher at the University of Maryland, told *The Record* that amplification factors varied based on middlebox device type, vendor, configurations, and network setup.


Bock said the research team scanned the entire IPv4 internet address space 35 different times to discover and index middleboxes that would amplify TCP DDoS attacks.


In total, the team said they found 200 million IPv4 addresses corresponding to networking middleboxes that could be abused for attacks.


Most UDP protocols typically have an amplification factor of between 2 and 10, with very few protocols sometimes reaching 100 or more.


“We found hundreds of thousands of IP addresses that offer [TCP] amplification factors greater than 100×,” Bock and his team said, highlighting how a very large number of networking middleboxes could be abused for DDoS attacks far larger than the UDP protocols with the best amplification factors known to date.


Furthermore, the research team also found thousands of IP addresses that had amplification factors in the range of thousands and even up to 100,000,000, a number thought to be inconceivable for such attacks.


![TCP-DDoS-amp-factor-chart](https://www-therecord.recfut.com/wp-content/uploads/2021/08/TCP-DDoS-amp-factor-chart.png)
While some of these devices are installed inside corporate and government networks, researchers said that many are also part of state-wide censorship apparatuses, like the ones in China, Saudi Arabia, Russia, and the UK.


Many of these systems work with huge traffic loads and are sometimes misconfigured with traffic loops that send the same malformed TCP packet multiple times through the same or other middleboxes, effectively allowing for infinite-loop DDoS attacks. Researchers said such situations were common in the censorship systems employed by China and Russia.


#### Tool to test networks made available


Although this research and attack vector was discovered last year, the research was made public today because the team has been in the midst of a broad disclosure process for the past year.





Bock told *The Record* they contacted several country-level Computer Emergency Readiness Teams (CERT) to coordinate the disclosure of their findings, including CERT teams in China, Egypt, India, Iran, Oman, Qatar, Russia, Saudi Arabia, South Korea, the United Arab Emirates, and the United States, where most censorship systems or middlebox vendors are based.


The team also notified companies in the DDoS mitigation field, which are most likely to see and have to deal with these attacks in the immediate future.


“We also reached out to several middlebox vendors and manufacturers, including Check Point, Cisco, F5, Fortinet, Juniper, Netscout, Palo Alto, SonicWall, and Sucuri,” the team said.


Because of the broad nature of this research and its findings, dealing with this attack vector requires more than firmware patches and also includes deploying configuration updates to the networks on which these middleboxes are installed.


Some of these countermeasures and mitigations are included in the team’s research paper, linked at the bottom of this article.


To aid in this complex process, the research team also plans to release scripts and tools that network administrators can use to test their firewalls, DPI boxes, and other middleboxes and see if their devices are contributing to this problem. These tools will be available later today via this [GitHub repository](https://github.com/breakerspace/weaponizing-censors).


However, there are still several reasons why this attack vector won’t be patched in time or at all.


First is that patching censorship systems for this attack vector also weakens their traffic filtering and censorship capabilities, a solution that oppressive regimes would certainly not consider.


Second, correcting middlebox configurations requires extensive tests, something that some companies or system administrators wouldn’t have the time or technical skills to achieve.


Third, the research team says that weaponizing this attack is relatively simple. While they have not released any proof-of-concept code, the research team told *The Record* that threat actors could create their own with the details from their paper.


With the promise of unheard-of DDoS amplification factors, TCP-based DDoS attacks via (nation-wide or enterprise) firewalls and other middleboxes are a threat looming on the horizon.


Additional technical details are available in a research paper titled “***Weaponizing Middleboxes for TCP Reflected Amplification***” [[PDF](https://www.usenix.org/system/files/sec21fall-bock.pdf)]. The paper was presented today [at the USENIX security conference](https://www.usenix.org/conference/usenixsecurity21/presentation/bock), where it also received the Distinguished Paper Award.





#### Tags:
[[DDoS]] [[TCP]] [[middleboxes]] [[middlebox]] [[IP]] [[Middleboxes]] [[UDP]] [[attacks.]] [[DPI]] [[firewalls,]] [[The Record]]
