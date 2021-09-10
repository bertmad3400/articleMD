# Yandex Pummeled by Potent Meris DDoS Botnet
### Record-breaking distributed denial of service attack targets Russia’s version of Google – Yandex.   

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169368)
+ Date: September 10, 2021  12:31 pm
+ Author: Tom Spring


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/10120505/DDoS.jpg)
Technical details tied to a record-breaking distributed-denial-of-service (DDoS) attack against Russian internet behemoth Yandex are surfacing as the digital dust settles. A massive botnet, dubbed Mēris, is believed responsible, flooding Yandex with millions of HTTP requests for webpages at the same time.


This DDoS technique is called HTTP pipelining, where a browser requests a connection to a server and, without waiting for a response, sends multiple more requests. Those requests reportedly originated from networking gear made by MikroTik. Attackers, according to Qrator Labs, exploited a 2018 bug unpatched in more than 56,000 MikroTik hosts involved in the DDoS attack.


According to Qrator, the Mēris botnet delivered the largest attack against Yandex it has ever spotted (by traffic volume) – peaking at 21.8 million requests per second (RPS). By comparison, infrastructure and website security firm Cloudflare reported that the “[largest ever](https://blog.cloudflare.com/cloudflare-thwarts-17-2m-rps-ddos-attack-the-largest-ever-reported/)” DDoS attack occurred on August 19, with 17.2 million RPS.


The Looming Mēris Monster
-------------------------


Researchers have linked Mēris to the August 19 DDoS attack tracked by Cloudflare. The Yandex attacks occurred between August 29 through September 5 – when the 28.1 million RPS attack occurred. Both are believed to be smaller precursor attacks by threat actors behind the Mēris botnet, which have yet to utilize the enormous firepower.  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“Yandex’ security team members managed to establish a clear view of the botnet’s internal structure. L2TP [Layer 2 Tunneling Protocol] tunnels are used for internetwork communications. The number of infected devices, according to the botnet internals we’ve seen, reaches 250,000,” [wrote Qrator in a Thursday blog post](https://blog.qrator.net/en/meris-botnet-climbing-to-the-record_142/).


L2TP is a protocol used to manage virtual private networks and deliver internet services. Tunneling facilitates the transfer of data between two private networks across the public internet.


Yandex and Qrato launched an investigation into the attack and believe the Mēris to be highly sophisticated.


“Moreover, all those [compromised MikroTik hosts are] highly capable devices, not your typical IoT blinker connected to Wi-Fi – here we speak of a botnet consisting of, with the highest probability, devices connected through the Ethernet connection – network devices, primarily,” researchers wrote.


Early Warnings Ignored?
-----------------------


The technical attack specifics include the exploitation of [CVE-2018-14847](https://threatpost.com/poc-attack-escalates-mikrotik-router-bug-to-as-bad-as-it-gets/138076/). Tenable Research [warned at the time](https://threatpost.com/poc-attack-escalates-mikrotik-router-bug-to-as-bad-as-it-gets/138076/) of its disclosure that the bug needed to be taken extremely seriously, because a newly found hack technique allowed for remote code execution on MikroTik edge and consumer routers.


“We are now able to show how an attacker can use it to get root shell on a system. It uses CVE-2018-14847 to leak the admin credentials first and then an authenticated code path gives us a back door,” Tenable told Threatpost in 2018.


While MikroTik patched CVE-2018-14847 back then, Tenable has now revealed that only approximately 30 percent of vulnerable modems have been patched, which leaves approximately 200,000 routers vulnerable to attack. MikroTik’s RouterOS powers its business-grade RouterBOARD brand, as well as ISP/carrier-grade gear from the vendor.


Qrato recent analysis of the DDoS attack revealed that the compromised hosts each had open ports 2000 (Bandwidth test server) and 5678 (Mikrotik Neighbor Discovery Protocol). Researchers reported 328,723 active hosts on the internet replying to the TCP probe on port 5678.


Mitigating a Monster
--------------------


While patching MikroTik devices is the most ideal mitigation to combat future Mēris attacks, researchers also recommended blacklisting.


“Since those [Mēris] attacks are not spoofed, every victim sees the attack origin as it is. Blocking it for a while should be enough to thwart the attack and not disturb the possible end user,” wrote researchers.


“[It’s] unclear how the…owners for the Mēris botnet would act in the future – they could be taking advantage of the compromised devices, taking 100 percent of its capacity (both bandwidth and processor-wise) into their hands. In this case, there is no other way other than blocking every consecutive request after the first one, preventing answering the pipelined requests.”


**It’s time to evolve threat hunting into a pursuit of adversaries.** [**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **Threatpost and Cybersixgill for** [**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **and get a guided tour of the dark web and learn how to track threat actors before their next attack.** [**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **for the LIVE discussion on September 22 at 2 PM EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[Mēris]] [[Yandex]] [[DDoS]] [[MikroTik]] [[botnet]] [[devices,]] [[attack.]] [[Threatpost]] [[ThreatPost]]
