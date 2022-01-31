# Microsoft: Here's how we stopped the biggest ever DDoS attack | ZDNet
### Microsoft details how Azure helped mitigate a 3.47 terabytes per second distributed denial of service (DDoS) attack.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/microsoft-heres-how-we-stopped-the-biggest-ever-ddos-attack/
+ Date: 2022-01-31 12:12:22
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/76ecb1de544bfb69c0eed4f609957885cbbf20d7/2021/10/14/31150cff-22bb-4487-b7c2-004fb0db8459/shutterstock-574000213.jpg?width=770&height=578&fit=crop&auto=webp)

Microsoft has revealed that it stopped what it described as the largest distributed denial of service (DDoS) attack ever reported in history in November, which at 3.47 terabytes (Tbps) per second outsized a [mega 2.4 Tbps DDoS it thwarted last year](https://www.zdnet.com/article/microsoft-azure-fends-off-huge-ddos-attack/) that was then thought to be the largest DDoS in history. 

DDoS attacks harness the connectivity of many compromised devices and direct packets of data at a specific target, such as a website or internet service, with the aim of knocking it offline.  


Massive DDoS attacks measured in Tbps are becoming more common. According to Alethea Toh, a product manager on the Microsoft Azure networking team, Microsoft stopped two other DDoS attacks that exceeded 2.5 Tbps in December. 

**SEE:** [**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/#link=%7B%22role%22:%22standard%22,%22href%22:%22http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/%22,%22target%22:%22_blank%22,%22absolute%22:%22%22,%22linkText%22:%22%3Cstrong%3EA%20winning%20strategy%20for%20cybersecurity%3C/strong%3E%22%7D) **(ZDNet special report)**

The record-breaking 3.47 Tbps DDoS attack originated from approximately 10,000 sources from connected devices in the United States, China, South Korea, Russia, Thailand, India, Vietnam, Iran, Indonesia, and Taiwan. "We believe this to be the largest attack ever reported in history," said Toh.

The largest attacks last year used the User Datagram Protocol (UDP), while attacks focusing on gaming servers were carried out using variants of the Mirai DDoS botnet malware, which [relies on compromised PCs and Internet of Things (IoT) devices](https://www.zdnet.com/article/mirai-splinter-botnets-dominate-iot-attack-scene/). 

Like last year's huge DDoS attack, the attack vector in the 3.47 Tbps DDoS attack was a UDP "reflection attack", where UDP request and response packets are reflected within a local network using a source Internet Protocol (IP) address that's been spoofed by the attacker. 






An attacker abuses UDP by creating a valid UDP request that falsely lists a target's IP address as the UDP source IP address. The attacker sends the spoofed UDP request to a middleman server, which sends a larger number of UDP response packets to the target's IP address rather than to the attacker's actual IP address. The technique amplifies the size of a DDoS attack, but UDP is just one of several internet protocols that can be abused for amplification, including Domain Name System (DNS), and Network Time Protocol (NTP), and memcached. 

The 3.47 Tbps UDP reflection attack lasted only 15 minutes, [Toh explains in a blogpost](https://azure.microsoft.com/en-us/blog/azure-ddos-protection-2021-q3-and-q4-ddos-attack-trends/). The two other attacks that surpassed 2.5 Tbps were were also short bursts targeting servers in Asia. UDP was used in all three cases. The protocol has proved popular for these attacks because online-gaming servers can't withstand high-volume attacks, even in short bursts. Also, UDP is commonly used in gaming and streaming applications. 

"The majority of attacks on the gaming industry have been mutations of the Mirai botnet and low-volume UDP protocol attacks. An overwhelming majority were UDP spoof floods, while a small portion were UDP reflection and amplification attacks, mostly SSDP, Memcached, and NTP," notes Toh.

"Workloads that are highly sensitive to latency, such as multiplayer game servers, cannot tolerate such short burst UDP attacks. Outages of just a couple seconds can impact competitive matches, and outages lasting more than 10 seconds typically will end a match," Toh explains. 

**SEE: [DDoS attacks that come combined with extortion demands are on the rise](https://www.zdnet.com/article/ddos-attacks-that-come-combined-with-extortion-demands-are-on-the-rise)**

The gaming industry has been hit with multiple DDoS attacks this year affecting Titanfall, Escape from Tarkov, Dead by Daylight, and Final Fantasy, Microsoft notes. Voice over IP (VoIP) service providers were another heavily targeted group for DDoS attacks. 

The two other December attacks exceeding 2.5 Tbps were UDP attacks. One was a UDP attack on port 80 and 443 in Asia that lasted 15 minutes with four main peaks, at 3.25 Tbps, 2.54 Tbps, and 0.59 Tbps, and a final peak at 1.25 Tbps. The other attack lasted just five minutes and was a 2.55 Tbps UDP flood on port 443 with one single peak, Toh notes. 

Some 55% of DDoS attacks relied on UDP spoofing in 2021 and it became the main vector in the second half of 2021. 

The US was the target of 54% of DDoS attacks, followed by 23% of attacks targeting India. DDoS activity in Europe, however, dropped from 19% in the first half of 2021 to just 6% in the second half, putting it behind East Asia, which was the target of 8% of DDoS attacks. Last year's 2.4 Tbps attack was aimed at European Azure cloud users. Again, gaming adoption in East Asia made it a popular target. 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Location:
[[victim.continent.name=Asia]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=Indonesia]] [[victim.continent.name=Asia]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=South Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Thailand]] [[victim.continent.name=Asia]] [[victim.country.name=Taiwan]] [[victim.continent.name=Asia]] [[victim.country.name=Vietnam]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Udp]] [[Ddos]] [[Tbps]] [[Ip]] [[Microsoft]] [[Toh]] [[ZDNet]]

