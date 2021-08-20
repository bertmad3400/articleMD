# Cloudflare says it mitigated a record-breaking 17.2M rps DDoS attack
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/cloudflare-says-it-mitigated-a-record-breaking-17-2m-rps-ddos-attack/)
+ Date: August 19, 2021
+ Author: Catalin Cimpanu


## Article:
![Cloudflare says it mitigated a record-breaking 17.2M rps DDoS attack](https://therecord.media/wp-content/uploads/2021/08/Cloudflare-DDoS.png)

Internet infrastructure company [Cloudflare disclosed today](https://blog.cloudflare.com/cloudflare-thwarts-17-2m-rps-ddos-attack-the-largest-ever-reported/) that it mitigated the largest volumetric distributed denial of service (DDoS) attack that was recorded to date.


The attack, which took place last month, targeted one of Cloudflare’s customers in the financial industry.


Cloudflare said that a threat actor used a botnet of more than 20,000 infected devices to flung HTTP requests at the customer’s network in order to consume and crash server resources.


Called a volumetric DDoS, these are different from classic bandwidth DDoS attacks where threat actors try to exhaust and clog up the victim’s internet connection bandwidth. Instead, attackers focus on sending as many junk HTTP requests to a victim’s server in order to take up precious server CPU and RAM and prevent legitimate users from using targeted sites.


Cloudflare said this attack peaked at **17.2 million HTTP requests/second (rps)**, a figure that the company described as **almost three times larger** than any previous volumetric DDoS attack that was ever reported in the public domain.





Cloudflare said that while the attack peaked at 17.2 million rps, the threat actor kept its botnet aimed against its customer for hours, during which time it had to absorb more than 330 million junk HTTP requests.


But the botnet operator did not stop after this initial attack. Cloudflare said the same botnet also carried out two other large-scale attacks in the subsequent weeks, including another that peaked at 8 million rps, aimed at a web hosting provider.


Cloudflare said it’s currently tracking the botnet’s evolution, which appears to have been built using a modified version of the well-known [Mirai](https://malpedia.caad.fkie.fraunhofer.de/details/elf.mirai) IoT malware.


Based on the infected device’s (bots) IP addresses, Cloudflare said that 15% of the attacker’s traffic came from Indonesia, while another 17% of the malicious traffic came from India and Brazil combined.


![Cloudflare-DDoS-source](https://www-therecord.recfut.com/wp-content/uploads/2021/08/Cloudflare-DDoS-source.png)Image: Cloudflare
At 17.2 million rps, the attack also accounted for 68% of the legitimate HTTP traffic the company processed during Q2 2021, estimated at 25 million rps.


The biggest bandwidth DDoS attack ever recorded comes at [2.3 terabytes per second (Tbps)](https://twitter.com/campuscodi/status/1273285258583121922), recorded by Amazon Web Services in February 2020.





#### Tags:
[[Cloudflare]] [[HTTP]] [[botnet]] [[DDoS]] [[rps,]] [[The Record]]
