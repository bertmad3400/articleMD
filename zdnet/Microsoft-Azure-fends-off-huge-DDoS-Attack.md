# Microsoft Azure fends off huge DDoS Attack
### Microsoft successfully blocked a 2.4 Tbps Distributed Denial of Service (DDoS) attack on one of its European Azure cloud customers.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/microsoft-azure-fends-off-huge-ddos-attack/)
+ Date: October 12, 2021
+ Author: Steven J. Vaughan-Nichols


## Article:
Unknown

[Distributed Denial of Service (DDoS)](https://www.zdnet.com/article/what-is-a-ddos-attack-everything-you-need-to-know-about-ddos-attacks-and-how-to-protect-against-them/) [attacks are happening ever more often and growing ever bigger](https://www.zdnet.com/article/ddos-attacks-are-becoming-more-prolific-and-more-powerful-warn-cybersecurity-researchers/). At 2.4 terabits per second (Tbps), the DDoS attack [Microsoft just successfully defended European Azure cloud users](https://azure.microsoft.com/en-us/blog/business-as-usual-for-azure-customers-despite-24-tbps-ddos-attack/) against could be the biggest one to date.

What we know for certain is it's the biggest DDoS attack on an Azure cloud customer. It was bigger than the previous high, [2020's Azure 1 Tbps attack](https://azure.microsoft.com/en-us/blog/azure-ddos-protection-2020-year-in-review/), and Microsoft reported it was "higher than any network volumetric event previously detected on Azure." 


Who was targeted? We don't know. Microsoft isn't talking. 

The attack itself came from over 70,000 sources. It was orchestrated from multiple Asia-Pacific countries such as Malaysia, Vietnam, Taiwan, Japan, and China, and from the United States. 

The attack vector was a User Datagram Protocol (UDP) reflection attack. The attack lasted over 10 minutes with very short-lived bursts. Each of these bursts ramped up in seconds to terabit volumes. In total, Microsoft saw three main peaks, the first at 2.4 Tbps, the second at 0.55 Tbps, and the third at 1.7 Tbps.

In a UDP reflection attack, the attacker exploits the fact that UDP is a stateless protocol. That means the attackers can create a valid UDP request packet listing the attack target's IP address as the UDP source IP address. It looks as if the attack is being reflected back and forth within the local network, hence the name. This relies on the UDP request packet's source Internet Protocol (IP) being spoofed, i.e. falsified. The UDP packet contains the spoofed source IP and is sent by the attacker to a middleman server. The server is tricked into sending its UDP response packets to the targeted victim IP rather than back to the attacker. The middleman machine helps strengthen the attack by generating network traffic that is several times larger than the request packet, thus amplifying the attack traffic.

How big the amplification can get depends on the attack protocol being abused. Such common internet protocols as DNS, NTP, [memcached](https://memcached.org/), CharGen, or QOTD can all be turned into network DDoS attack dogs. The nastiest of these is memcached. [Memcached is an open-source, high-performance, distributed, object-caching system](http://practical-tech.com/infrastructure/thanks-for-the-memcached/7333/). It's commonly used by social networks such as Facebook and its creator [LiveJournal](https://www.livejournal.com/) as an in-memory key-value store for small chunks of arbitrary data. There it's very useful. When abused, however, [Cloudflare](https://www.cloudflare.com/), the web performance and security company, has found [15 bytes of request can cause 750KB of attack traffic](https://blog.cloudflare.com/memcrashed-major-amplification-attacks-from-port-11211/) -- that's a 51,200x amplification! That's bad. 






Microsoft isn't saying which was used in this case but it did mention DNS. Attacks exploiting DNS can produce 28 to 54 times the original number of bytes. So, if an attacker sends a request payload of 64 bytes to a DNS server, they can generate over 3,400 bytes of unwanted traffic to an attack target. 

While Microsoft also didn't go into detail about how it blocked the attack, the company said Azure's DDoS protection platform, built on distributed DDoS detection and mitigation pipelines, can absorb tens of terabits of DDoS attacks: "This aggregated, distributed mitigation capacity can massively scale to absorb the highest volume of DDoS threats, providing our customers the protection they need."

Generally speaking this works by Azure's DDoS control plane logic kicking in when it detects a DDoS storm building up. "This cuts through normal detection steps, needed for lower-volume floods, to immediately kick-in mitigation. This ensures the fastest time-to-mitigation and prevents collateral damage from such large attacks."

Some DDoS protection is provided for all of Azure's users. For better, more comprehensive protection, Microsoft recommends you subscribe to [Azure DDoS Protection Standard](https://azure.microsoft.com/en-us/services/ddos-protection/). Besides blocking DDoS attacks, it also offers cost protection. This provides data transfer and application scale-out service credit for resource costs incurred because of documented DDoS attacks.

**Related Stories:**

* [DDoS attacks are becoming more prolific and more powerful, warn cybersecurity researchers](https://www.zdnet.com/article/ddos-attacks-are-becoming-more-prolific-and-more-powerful-warn-cybersecurity-researchers/)
* [Bandwidth CEO confirms outages caused by DDoS attack](https://www.zdnet.com/article/bandwidth-ceo-confirms-outages-caused-by-ddos-attack/)
* [This massive DDoS attack took large sections of a country's internet offline](https://www.zdnet.com/article/this-massive-ddos-attack-took-large-sections-of-a-countrys-internet-offline/)





#### Tags:
[[DDoS]] [[Microsoft]] [[UDP]] [[IP]] [[attack,]] [[ZDNet]]
