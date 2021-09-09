# New Mēris botnet breaks DDoS record with 21.8 million RPS attack
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-m-ris-botnet-breaks-ddos-record-with-218-million-rps-attack/)
+ Date: September 9, 2021
+ Author: Ionut Ilascu


## Article:
![New Mēris botnet breaks DDoS record with 21.8 million RPS attack](https://www.bleepstatic.com/content/hl-images/2021/09/09/Meris_Botnet.jpg)


A new distributed denial-of-service (DDoS) botnet that kept growing over the summer has been hammering Russian internet giant Yandex for the past month, the attack peaking at the unprecedented rate of 21.8 million requests per second.


The botnet received the name Mēris, and it gets its power from tens of thousands of compromised devices that researchers believe to be primarily powerful networking equipment.


### Large and powerful botnet


News about a [massive DDoS attack hitting Yandex](https://www.bleepingcomputer.com/news/security/yandex-is-battling-the-largest-ddos-in-russian-internet-history/) broke this week in the Russian media, which described it as being the largest in the history of the Russian internet, the so-called RuNet.


Details have emerged today in joint research from Yandex and its partner in providing DDoS protection services, [Qrator Labs](https://qrator.net/en/).


Information collected separately from several attacks deployed by the new Mēris (Latvian for ‘plague’) botnet, showed a striking force of more than 30,000 devices.


From the data that Yandex observed, assaults on its servers relied on about 56,000 attacking hosts. However, the researchers have seen indications that the number of compromised devices may be closer to 250,000.



“Yandex' security team members managed to establish a clear view of the botnet's internal structure. L2TP tunnels are used for internetwork communications. The number of infected devices, according to the botnet internals we’ve seen, reaches 250 000” - Qrator Labs



The difference between the attacking force and the total number of infected hosts forming Mēris is explained by the fact that the administrators do not want to parade the full power of their botnet, [Qrator Labs says](https://habr.com/en/company/yandex/blog/577040/) in a blog post today.


The researchers note that the compromised hosts in Mēris are “not your typical IoT blinker connected to WiFi” but highly capable devices that require an Ethernet connection.


Mēris is the same botnet responsible for generating the [largest volume of attack traffic](http://enter%20urlhttps//www.bleepingcomputer.com/news/security/http-ddos-attacks-reach-unprecedented-17-million-requests-per-second/) that Cloudflare recorded and mitigated to date, as it peaked at 17.2 million requests per second (RPS).


However, Mēris botnet broke that record when hitting Yandex, as its flux on September 5 reached a force of 21.8 million RPS.



![DDoS attack from Meris botnet peaks at 21.8 million requests per second](https://www.bleepstatic.com/images/news/u/1100723/Botnets/Meris/MerisBot_Yandex.png)source: Qrator Labs
The botnet’s history of attacks on Yandex begins in early August with a strike of 5.2 million RPS and kept increasing in strength:


* 2021-08-07 - 5.2 million RPS
* 2021-08-09 - 6.5 million RPS
* 2021-08-29 - 9.6 million RPS
* 2021-08-31 - 10.9 million RPS
* 2021-09-05 - 21.8 million RPS


### Technical data points to MikroTik devices


To deploy an attack, the researchers say that Mēris relies on the SOCKS4 proxy at the compromised device, uses the [HTTP pipelining](http://enter%20urlhttps//en.wikipedia.org/wiki/HTTP_pipelining) DDoS technique, and port 5678.


As for the compromised devices used, the researchers say that they are related to MikroTik, the Latvian maker of networking equipment for businesses of all sizes.


Most of the attacking devices had open ports 2000 and 5678. The latter points to MikroTik equipment, which uses it for the neighbor discovery feature (MikroTik Neighbor Discovery Protocol).


Qrator Labs found that while MikroTik provides its standard service through the User Datagram Protocol (UDP), compromised devices also have an open Transmission Control Protocol (TCP).


This kind of disguise might be one of the reasons devices got hacked unnoticed by their owners,” Qrator Labs researchers believe.


When searching the public internet for open TCP port 5678, more than 328,000 hosts responded. The number is not all MikroTik devices, though, as [LinkSys equipment](https://www.speedguide.net/port.php?port=5678) also uses TCP on the same port.



![Devices with open port 5678](https://www.bleepstatic.com/images/news/u/1100723/Botnets/Meris/Port5678_Qrator.png)source: Qrator Labs
Port 2000 is for "Bandwidth test server," the researchers say. When open, it replies to the incoming connection with a signature that belongs to MikroTik’s RouterOS protocol.


MikroTik has been informed of these findings. The vendor [told](https://www.vedomosti.ru/technology/articles/2021/09/07/885664-yandeks-ddos-atake) Russian publication Vedomosti that it is not aware of a new vulnerability to compromise its products.


The network equipment maker also said that many of its devices continue to run old firmware, vulnerable to a [massively exploited](http://enter%20urlhttps//www.bleepingcomputer.com/news/security/massive-coinhive-cryptojacking-campaign-touches-over-200-000-mikrotik-routers/) security issue tracked as CVE-2018-14847 and [patched in April 2018](https://www.bleepingcomputer.com/news/security/mikrotik-patches-zero-day-flaw-under-attack-in-record-time/).


However, the range of RouterOS versions that Yandex and Qrator Labs observed in attacks from Mēris botnet varies greatly and includes devices running newer firmware versions, such as the current stable one (6.48.4) and its predecessor, 6.48.3.



![RouterOS versions seen in Meris DDoS botnet](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)source: Qrator Labs
 




#### Tags:
[[Qrator]] [[botnet]] [[Mēris]] [[Yandex]] [[MikroTik]] [[DDoS]] [[However,]] [[source:]] [[Bleeping Computer]]
