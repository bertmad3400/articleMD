# Cloudflare report highlights devastating DDoS attacks on VoIP services and several 'record-setting HTTP attacks'
### In Q3, Cloudflare researchers said they stopped "one of the largest recorded HTTP attacks​."

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/cloudflare-report-highlights-devastating-ddos-attacks-on-voip-services-and-several-record-setting-http-attacks/)
+ Date: November 5, 2021
+ Author: Jonathan Greig


## Article:
Unknown

Cloudflare [released](https://blog.cloudflare.com/ddos-attack-trends-for-2021-q3/) its Q3 DDoS Attack Trends report this week, capping a record-setting quarter that saw a number of [devastating attacks on VoIP services](https://www.bandwidth.com/blog/a-message-to-our-customers-and-partners/). 

Cloudflare researchers said they saw the several "record-setting HTTP DDoS attacks, terabit-strong network-layer attacks and one of the largest botnets ever deployed (Meris)," noting the emergence of ransom DDoS attacks on voice over IP (VoIP) service providers. The [attack on Bandwidth.com](https://www.zdnet.com/article/bandwidth-ceo-confirms-outages-caused-by-ddos-attack/) left dozens of companies scrambling to deal with outages. 


The US topped the list for the second quarter in a row of countries with the most targeted companies. But Cloudflare noted that companies in the UK and Canada also shot up the list. 

Computer software, gaming, gambling, IT and Internet companies saw an average increase in attacks of 573% compared to the previous quarter.

Overall, DDoS attacks across the world increased by 44%, according to Cloudflare's research, while the Middle East and Africa led the way with average attack increases of 80%. 

"Morocco recorded the highest DDoS activity in the third quarter globally -- three out of every 100 packets were part of a DDoS attack. While SYN and RST attacks remain the dominant attack method used by attackers, Cloudflare observed a surge in DTLS amplification attacks -- recording a 3,549% increase QoQ. Attackers targeted (and continue to target going into the fourth quarter this year) VoIP service providers with massive DDoS attack campaigns in attempts to bring SIP infrastructure down," the researchers said. 

Cloudflare data showed that most DDoS attacks originated from devices and servers in China, the US and India, but the number of attacks from China decreased 30% throughout the quarter. 

![screen-shot-2021-11-05-at-12-23-17-pm.png]()![screen-shot-2021-11-05-at-12-23-17-pm.png](https://www.zdnet.com/a/img/resize/3dd40b5533ec48bd22509803139de728fb15f5b9/2021/11/05/4a6248f6-44df-48da-9055-752c48316c42/screen-shot-2021-11-05-at-12-23-17-pm.png?width=470&fit=bounds&auto=webp)
 Cloudflare
 




The report also takes time to discuss the [Meris botnet](https://www.zdnet.com/article/meris-botnet-assaults-krebsonsecurity/), which is powered by Internet of Things (IoT) devices. IoT products, PCs, home gadgets -- including cameras, VCRs, TVs, and routers -- that are hijacked and become slave nodes in a botnet's network are typically used in DDoS attacks.

Cloudflare said Meris was "one of the most powerful botnets deployed to launch some of the largest HTTP DDoS attacks in history," adding that in Q3 they saw "[one of the largest recorded HTTP attacks](https://www.zdnet.com/article/cloudflare-says-it-stopped-the-largest-ddos-attack-ever-reported/) -- 17.2M rps (requests per second) -- targeting a customer in the financial services industry."

Meris has been [used to target networks and organizations](https://www.zdnet.com/article/meris-botnet-assaults-krebsonsecurity/) around the world, including news sites like KrebsOnSecurity.

"The Meris botnet infected routers and other networking equipment manufactured by the Latvian company MikroTik. According to MikroTik's blog, a vulnerability in the MikroTik RouterOS (that was patched after its detection back in 2018) was exploited in still unpatched devices to build a botnet and launch coordinated DDoS attacks by bad actors," Cloudflare stated, comparing it to the 2016 Mirai botnet.

"While Mirai infected IoT devices with low computational power such as smart cameras, Meris is a growing swarm of networking infrastructure (such as routers and switches) with significantly higher processing power and data transfer capabilities than IoT devices — making them much more potent in causing harm at a larger scale." 


Despite its power, Meris did not actually cause significant damage or outages, according to Cloudflare. 

The company noted that its customers on the Magic Transit and Spectrum services were targeted with network-layer attacks by a Mirai-variant botnet that "launched over a dozen UDP- and TCP-based DDoS attacks that peaked multiple times above 1 Tbps, with a max peak of approximately 1.2 Tbps."

The report notes that the number of attacks peaked in September but throughout the quarter, the number of large attacks increased, both in volume of traffic delivered and in the number of packets delivered. 

"QoQ data shows that the number of attacks of sizes ranging from 500 Mbps to 10 Gbps saw massive increases of 126% to 289% compared to the previous quarter. Attacks over 100 Gbps decreased by nearly 14%. The number of larger bitrate attacks increased QoQ (with the one exception being attacks over 100 Gbps, which decreased by nearly 14% QoQ). In particular, attacks ranging from 500 Mbps to 1 Gbps saw a surge of 289% QoQ and those ranging from 1 Gbps to 100 Gbps surged by 126%. This trend once again illustrates that, while (in general) a majority of the attacks are indeed smaller, the number of 'larger' attacks is increasing. This suggests that more attackers are garnering more resources to launch larger attacks," the report found. 

"Most attacks remain under one hour in duration, reiterating the need for automated always-on DDoS mitigation solutions. As in previous quarters, most of the attacks are short-lived. To be specific, 94.4% of all DDoS attacks lasted less than an hour. On the other end of the axis, attacks over 6 hours accounted for less than 0.4% in Q3 '21, and we did see a QoQ increase of 165% in attacks ranging 1-2 hours. Be that as it may, a longer attack does not necessarily mean a more dangerous one."

Cybercriminals typically use SYN floods as their method of attack but there was a 3,549% QoQ increase in attacks over DTLS. 

Vishal Jain, CTO at Valtix, told ZDNet that it's not surprising to learn DDoS attacks are breaking records. For years, the cybersecurity community has been talking about how IoT devices will lead to larger botnets capable of stronger DDoS attacks, Jain said, adding that as the volume of vulnerable, compromised, and misconfigured IoT devices continue to grow -- cloud service providers will be challenged to protect their customer's services. 

"Organizations need to have an incident response plan in place that involves a DDoS mitigation service," Jain said. 

"Being alerted to a possible DDoS attack and identifying what is impacted allows security teams to take a proactive approach instead of reacting to downed services. Businesses should use edge-based, volumetric L4 DDoS protections complementing L7 DDoS protections close to internet facing applications."

Digital Shadows cyber threat intelligence analyst Stefano De Blasi said that while DDoS attacks are commonly associated with technically unsophisticated attackers, recent events are a reminder that highly skilled adversaries can mount high-intensity operations that may result in severe consequences for their targets. 

In the past two years, De Blasi noted that Digital Shadows has frequently observed attackers combining DDoS attacks with cyber extortion tactics, potentially offering a glimpse into how the future of this cyber threat will look. 

"With the introduction of extortion, leading to a higher likelihood of financial gain, financially motivated threat actors likely see DDoS attacks as viable options, especially with success experienced by ransomware operators. In the coming years, cybercriminals will likely begin leveraging DDoS attacks to conduct financially motivated campaigns, while hacktivist groups will continue to use DDoS attacks for disruption purposes," De Blasi said. 

"Nation-state groups primarily conduct attacks to gather competitive intelligence, which is more attainable through unauthorized network access through phishing, vulnerability exploitation, and ransomware deployment when coupled with data exfiltration."





#### Tags:
[[DDoS]] [[Cloudflare]] [[Meris]] [[IoT]] [[Gbps]] [[botnet]] [[QoQ]] [[Q3]] [[services.]] [[HTTP]] [[ZDNet]]
