# Microsoft mitigated a record 3.47 Tbps DDoS attack on Azure users
### Microsoft says its Azure DDoS protection platform mitigated a massive 3.47 terabits per second (Tbps) distributed denial of service (DDoS) attack targeting an Azure customer from Asia in November.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/microsoft-mitigated-a-record-347-tbps-ddos-attack-on-azure-users/
+ Date: 2022-01-27T08:12:43-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/09/27/ddos-header-image.jpg)

![DDoS attack](https://www.bleepstatic.com/content/hl-images/2021/09/27/ddos-header-image.jpg)


Microsoft says its Azure DDoS protection platform mitigated a massive 3.47 terabits per second (Tbps) distributed denial of service (DDoS) attack targeting an Azure customer from Asia in November.


Two more large size attacks followed this in December, also targeting Asian Azure customers, a 3.25 Tbps UDP attack on ports 80 and 443 and a 2.55 Tbps UDP flood on port 443.


"In November, Microsoft mitigated a DDoS attack with a throughput of 3.47 Tbps and a packet rate of 340 million packets per second (pps), targeting an Azure customer in Asia. We believe this to be the largest attack ever reported in history," said Alethea Toh, an Azure Networking Product Manager.


"This was a distributed attack originating from approximately 10,000 sources and from multiple countries across the globe, including the United States, China, South Korea, Russia, Thailand, India, Vietnam, Iran, Indonesia, and Taiwan."


The 15 minutes attack used multiple attack vectors for UDP reflection on port 80, including:


* Simple Service Discovery Protocol (SSDP),
* Connection-less Lightweight Directory Access Protocol (CLDAP),
* Domain Name System (DNS),
* and Network Time Protocol (NTP)

Previous record-breaking publicly reported DDoS attacks were a [21.8 million requests per second (rrps) application layer assault](https://www.bleepingcomputer.com/news/security/http-ddos-attacks-reach-unprecedented-17-million-requests-per-second/) that hit the Russian internet giant Yandex in August and a [2.3 Tbps volumetric strike detected by Amazon Web Services Shield](https://aws-shield-tlr.s3.amazonaws.com/2020-Q1_AWS_Shield_TLR.pdf) during Q1 2020.


Google Security Reliability Engineer Damian Menscher also revealed two years ago that Google mitigated [a 2.54 Tbps DDoS](http://cloud.google.com/blog/products/identity-security/identifying-and-protecting-against-the-largest-ddos-attacks)in 2017.


 



![3.47 Tbps attack](https://www.bleepstatic.com/images/news/u/1109292/2022/3_47%20Tbps%20attack.png)*3.47 Tbps Azure DDoS attack (Microsoft)*
"Largest attack ever reported in history"
-----------------------------------------


The November 3.47 Tbps attack was the largest one the company had to face to date (and likely ever recorded), after previously reporting that it [mitigated another record 2.4 Tbps attack](https://www.bleepingcomputer.com/news/security/microsoft-azure-customer-hit-by-record-ddos-attack-in-august/) targeting a European Azure customer during late August.


Microsoft saw a rise in attacks that lasted longer than an hour in the second half of 2021, while multi-vector attacks such as the record one mitigated in November were prevalent.


These more prolonged DDoS attacks usually come as a sequence of short-lived, repeated burst attacks quickly ramping up (in seconds) to terabit volumes.


"Gaming continues to be the hardest hit industry. The gaming industry has always been rife with DDoS attacks because players often go to great lengths to win," Toh added.


"The concentration of attacks in Asia can be largely explained by the huge gaming footprint10, especially in China, Japan, South Korea, Hong Kong, and India, which will continue to grow as the increasing smartphone penetration drives the popularity of mobile gaming in Asia."


Microsoft also defended customers against new TCP PUSH-ACK flood attacks (dominant in the East Asia region) during the 2021 holiday season.


"We observed a new TCP option manipulation technique used by attackers to dump large payloads, whereby in this attack variation, the TCP option length is longer than the option header itself," Toh [said](https://azure.microsoft.com/en-us/blog/azure-ddos-protection-2021-q3-and-q4-ddos-attack-trends/).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.continent.name=Asia]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=Indonesia]] [[victim.continent.name=Asia]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.country.name=Japan]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=South Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Thailand]] [[victim.continent.name=Asia]] [[victim.country.name=Taiwan]] [[victim.continent.name=Asia]] [[victim.country.name=Vietnam]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Tbps]] [[Ddos]] [[Microsoft]] [[Udp]] [[Toh]] [[Tcp]] [[Bleeping Computer]]

