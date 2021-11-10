# Telnyx is the latest VoIP provider hit with DDoS attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/telnyx-is-the-latest-voip-provider-hit-with-ddos-attacks/)
+ Date: November 10, 2021
+ Author: Lawrence Abrams


## Article:
![DDoS](https://www.bleepstatic.com/content/hl-images/2021/01/23/ddos-header.jpg)


Telnyx is the latest VoIP telephony provider targeted with distributed denial-of-service (DDoS) attacks, causing worldwide outages since yesterday.


Telnyx is a voice over Internet Protocol (VoIP) company that provides worldwide telephony services over the Internet, including in the Americas, EMEA, APAC, and Australia regions.


Starting November 9th at approximately 11 PM EST, Telnyx was targeted with a DDoS attack causing all telephony services to fail or be delayed.


"Telnyx is currently experiencing a DDoS attack. Until we reach a resolution, you may be experiencing failed calls, API and portal latency/time outs, and/or delayed or failed messages," reported the Telnyx [status page](https://status.telnyx.com/).


After the DDoS attacks continued, Telnyx began migrating their services to [Cloudflare's Magic Transit service](https://www.cloudflare.com/magic-transit/), which provides DDoS protection for service providers.


"Magic Transit delivers its connectivity, security, and performance benefits by serving as the “front door” to your IP network. This means it accepts IP packets destined for your network, processes them, and then outputs them to your origin infrastructure," explains [documentation](https://developers.cloudflare.com/magic-transit/about) for the Magic Transit feature.


At this time, Telnyx has moved their EMEA and APAC services behind Cloudflare, with the company planning on migrating services for the Americas during off-peak hours.


VoIP providers under siege by DDoS attacks
------------------------------------------


This attack follows September DDoS attacks on VoIP.ms and Bandwidth that effectively took down the service provider's services for days.


When [VoIP.ms suffered their week-long DDoS attack](https://www.bleepingcomputer.com/news/security/voipms-phone-services-disrupted-by-ddos-extortion-attack/), they received a ransom demand by threat actors impersonating the ransomware group 'REvil.'


The threat actors [initially demanded a one bitcoin ransom](https://web.archive.org/web/20210918231028/https://pastebin.com/y207gbnR) (roughly ~$45,000) to halt the attacks but later increased it to 100 bitcoins, worth approximately $4.5 million at the time



![VoIP.ms ransom note](https://www.bleepstatic.com/images/news/security/attacks/d/ddos/bandwidth/voip-ms-ransom-note.jpg)**VoIP.ms ransom note**  
*Source: BleepingComputer*
Bandwidth remained silent about the cause of their outage for days but, eventually, [admitted to suffering a DDoS attack](https://www.bleepingcomputer.com/news/security/bandwidthcom-is-latest-victim-of-ddos-attacks-against-voip-providers/).


In a recent Q2 2021 earnings call, the Bandwidth CEO implied that the threat actors demanded a ransom in their attack but that the company did not give in to the demands.


"We did not pay a ransom and instead relied on innovative solutions and strategies to confront the threat, head on. To sum up, we believe, Bandwidth is now stronger than ever and we plan to leverage what we've learned to help make the ecosystem safer for enterprise communications," Bandwidth CEO David Morken said during the [earnings call](https://www.fool.com/earnings/call-transcripts/2021/11/09/bandwidth-inc-band-q2-2021-earnings-call-transcrip/).


To mitigate the DDoS attacks, both vendors migrated their infrastructure behind Cloudflare as well.


Morken went as far as to say that the attacks on their infrastructure taught Cloudflare how to mitigate attacks against VoIP providers.


"We rallied during this attack and used vendors like Cloudflare and taught them how to address this issue for the first time and collaborated with them in a way that they then were able to go to the whole industry and share," said Morken.


As VoIP services are commonly routed over the Internet and require servers and endpoints to be publicly accessible, they become prime targets for DDoS extortion attacks.


We should expect these attacks to continue and potentially bypass defenses at times as threat actors evolve their tactics.


BleepingComputer did not receive a response after reaching out to Telnyx to ask if they also received a ransom demand.




#### Tags:
[[DDoS]] [[Telnyx]] [[VoIP]] [[Cloudflare]] [[VoIP.ms]] [[Bleeping Computer]]
