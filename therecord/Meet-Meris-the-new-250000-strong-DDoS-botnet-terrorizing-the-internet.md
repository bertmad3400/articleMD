# Meet Meris, the new 250,000-strong DDoS botnet terrorizing the internet
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/meet-meris-the-new-250000-strong-ddos-botnet-terrorizing-the-internet/)
+ Date: September 9, 2021
+ Author: Catalin Cimpanu


## Article:
![Meet Meris, the new 250,000-strong DDoS botnet terrorizing the internet](https://therecord.media/wp-content/uploads/2021/09/Meris.png)

* Russian security firm Qrator Labs discover Meris, a new massive IoT botnet abused for DDoS attacks.
* Qrator estimates the size of the botnet at around 250,000 infected devices, most from Latvian vendor MikroTik.
* The Meris botnet broke the record for the largest volumetric DDoS attack twice this summer.
* Its most recent attack peaked at 21.8 million RPS and was aimed at a Russian bank hosting infrastructure on Yandex servers.


A new botnet consisting of an estimated 250,000 malware-infected devices has been behind some of the biggest DDoS attacks over the summer, breaking the record for the largest volumetric DDoS attack twice, once in June and again this month.


Named **Mēris**, the Latvian word for “plague,” the botnet has been primarily used as part of a DDoS extortion campaign against internet service providers and financial entities across several countries, such as [Russia](https://www.kommersant.ru/doc/4974831), [the UK](https://www.ispreview.co.uk/index.php/2021/09/ddos-attack-disrupts-voip-and-internet-services-at-voipfone-uk.html), [the US](https://blog.cloudflare.com/cloudflare-thwarts-17-2m-rps-ddos-attack-the-largest-ever-reported/), and [New Zealand](https://www.zdnet.com/article/anz-new-zealand-back-online-after-outage-from-ddos-attack/).


The group behind the botnet typically sends menacing emails to large companies asking for a ransom payment. The emails, which target companies with extensive online infrastructure and which can’t afford any downtime, contain threats to take down crucial servers if the group is not paid a certain amount of cryptocurrency by a deadline.


If victims don’t pay, the hackers unleash their botnet in smaller attacks at the beginning that substantially grow in size with time in order to put pressure on the victims.


### Meris – “a botnet of a new kind”


Qrator Labs, a Russian DDoS mitigation service, described Meris as “a botnet of a new kind” in a [blog post](https://blog.qrator.net/en/meris-botnet-climbing-to-the-record_142/) published earlier today, following a series of attacks against Russian companies.


“In the last couple of weeks, we have seen devastating attacks towards New Zealand, United States and Russia, which we all attribute to this botnet species,” the company researchers said today.


“[Meris] can overwhelm almost any infrastructure, including some highly robust networks. All this is due to the enormous RPS power that it brings along,” the company said, where RPS stands for requests per second, one of the two ways to measure the size of DDoS attacks [the other being Gbps, gigabytes per second].


The reason why Qrator Labs calls Meris one of a kind is that prior to this summer, most RPS-based DDoS attacks have been very rare and haven’t been seen at this scale for the past five years.


Most botnets are typically configured to sling as much junk traffic at a target as possible in classic “bandwidth attacks,” which are measured in Gbps.


Called volumetric or application-layer DDoS attacks, RPS attacks are different because attackers focus on send requests to a target server in order to overwhelm its CPU and memory. Instead of clogging its bandwidth with junk traffic, volumetric attacks focus on occupying servers’ resources and eventually crashing them.


“For the last five years, there have virtually been almost no global-scale application-layer attacks,” Qrator said today.


### Botnet breaks DDoS records twice


But things changed this summer with the emergence of Meris, which was built on a modified version of the old Mirai DDoS malware, according to internet infrastructure company Cloudflare, which also had to deal with some of its attacks.


But instead of focusing on bandwidth attacks, like most Mirai variants, Meris focused on modules specialized in launching volumetric attacks, and, apparently, they found a sweet spot.


In the aftermath of its recent spree of attacks, Meris broke the record for the largest volumetric DDoS attack twice. It did it the first time earlier this summer, in June, when it was behind a large [17.2 million RPS DDoS attack](https://therecord.media/cloudflare-says-it-mitigated-a-record-breaking-17-2m-rps-ddos-attack/) that hit a US financial company, according to Cloudflare, which had the unpleasant task of mitigating this particular attack.


Today, Qrator Labs said Meris outdid itself again during an attack that took place this Sunday, September 5, which hit even a bigger milestone at **21.8 million RPS**.


![Yandex-graph](https://www-therecord.recfut.com/wp-content/uploads/2021/09/Yandex-graph.png)Image: Qrator Labs
Qrator said it worked with Yandex to mitigate the attack, which was apparently hitting Yandex servers. But, a source involved in the incident told *The Record* that the target of the attack was actually a Russian bank that was keeping its e-banking portal on Yandex’s cloud hosting service.


### Botnet mostly consists of compromised MikroTik devices


Qrator says that after analyzing the source of most of the attack traffic, most of it led back to devices from [MikroTik](https://mikrotik.com/), a small Latvian company that sells networking gear such as routers, IoT gateways, WiFi access points, switches, and mobile network equipment.


The company said it wasn’t able to determine if the attacker found and weaponized a zero-day in MikroTik’s software or if they’re just living past exploits.


Nonetheless, a zero-day appears to be in play, just by the large number of MikroTik devices that appear to have been enslaved in Mesir’s gigantic 250,000-strong mesh.


A MikroTik spokesperson did not return a request for comment regarding Qrator’s report.


But besides bringing back volumetric (application layer) DDoS attacks, Meris also stands out due to its size. In recent years, DDoS botnets have rarely reached 50,000 infected devices.


This was because the code of several DDoS malware strains had been published online years ago, including Mirai, and this code was massively exploited to create numerous botnets that ended up fighting with each other over the limited number of devices they could infect, with very few botnets reaching even small figures of 15,000 over the past few years, let alone a 250,000 figure, unseen since late 2018.


All in all, what the Meris operators have achieved over the past few months can be considered impressive from a technical standpoint, but we’re also talking about a cybercrime gang here, so expect a long list of technical outages in the coming months as the Meris operators continue to use their new toy for extortion and DDoS attacks.





#### Tags:
[[DDoS]] [[botnet]] [[Meris]] [[Qrator]] [[attacks,]] [[botnets]] [[attacks.]] [[Yandex]] [[summer,]] [[years,]] [[The Record]]
