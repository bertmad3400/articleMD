# Russian security firm sinkholes part of the dangerous Meris DDoS botnet
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/russian-security-firm-sinkholes-part-of-the-dangerous-meris-ddos-botnet/)
+ Date: September 21, 2021
+ Author: Catalin Cimpanu


## Article:
![Russian security firm sinkholes part of the dangerous Meris DDoS botnet](https://therecord.media/wp-content/uploads/2021/09/Meris.png)

Rostelecom-Solar, the cybersecurity division of Russian telecom giant Rostelecom, said on Monday that it sinkholed a part of the Meris DDoS botnet after identifying a mistake from the malware’s creators.


First spotted earlier this year, the Meris botnet is [currently the largest DDoS botnet on the internet](https://therecord.media/meet-meris-the-new-250000-strong-ddos-botnet-terrorizing-the-internet/), with an estimated size of around 250,000 infected systems.


For the past few months, the botnet has been abused by a threat actor that has engaged in DDoS extortion attacks against internet service providers and financial entities across several countries, such as [Russia](https://www.kommersant.ru/doc/4974831), [the UK](https://www.ispreview.co.uk/index.php/2021/09/ddos-attack-disrupts-voip-and-internet-services-at-voipfone-uk.html), [the US](https://blog.cloudflare.com/cloudflare-thwarts-17-2m-rps-ddos-attack-the-largest-ever-reported/), and [New Zealand](https://www.zdnet.com/article/anz-new-zealand-back-online-after-outage-from-ddos-attack/).


The attacks have been brutal, with companies often going offline overwhelmed by the botnet’s sheer power. As part of this ferocious campaign, Meris broke the record for the largest volumetric DDoS attack twice this year, once in [June](https://blog.cloudflare.com/cloudflare-thwarts-17-2m-rps-ddos-attack-the-largest-ever-reported/) and then again in [September](https://blog.qrator.net/en/meris-botnet-climbing-to-the-record_142/).


Internet infrastructure firms like Cloudflare and Qrator Labs have analyzed the botnet following attacks on their customers and found that the vast majority of infected systems have been MikroTik networking equipment like routers, switches, and access points.


In a [blog post](https://blog.mikrotik.com/security/meris-botnet.html) last week, MikroTik said the attackers abused an old vulnerability (CVE-2018-14847) in its RouterOS to assemble their botnet using devices that haven’t been updated by their owners.


### Meris botnet operators make a mistake


But in [research](https://rt-solar.ru/events/news/2343/) published on Monday, Rostelecom-Solar said that during routine analysis of this new threat, which has also been attacking some of its customers, its engineers found that some infected routers were reaching out and asking for new instructions from an unregistered domain at **cosmosentry[.]com**.


Seizing the operator’s mistake, Rostelecom-Solar engineers said they registered this domain and converted it into a “[sinkhole](https://en.wikipedia.org/wiki/DNS_sinkhole).”


After days of tracking, researchers said they received pings from around 45,000 infected MikroTik devices, a number estimated to be around a fifth of the botnet’s entire size.


“Unfortunately, we cannot take any active actions with devices under our control (we do not have the authority to do this),” the company said this week.


“At the moment, about 45,000 MikroTik devices turn to us as a sinkhole domain.”


![Meris-sinkhole](https://www-therecord.recfut.com/wp-content/uploads/2021/09/Meris-sinkhole.png)Image: The Record
In case MikroTik router owners detect these suspicious connections to the cosmosentry[.]com, Rostelecom-Solar said they’ve set up a placeholder message informing them of who owns the domain and why their router is making the connection.


### The Glupteba connection


Furthermore, researchers said they also identified clues in the Meris malware code that also provided an insight into how this botnet had been assembled.


Per the Rostelecom-Solar team, the Meris botnet appears to have been assembled via **Glupteba**, a malware strain targeting Windows computers, typically used as a loader for various other malware strains.


Researchers pointed to two 2020 reports from cyber-security firms [Sophos [PDF]](https://news.sophos.com/wp-content/uploads/2020/06/glupteba_final-1.pdf) and [Trend Micro](https://www.trendmicro.com/en_us/research/19/i/glupteba-campaign-hits-network-routers-and-updates-cc-servers-with-data-from-bitcoin-transactions.html), both of which documented a new Glupteba module at the time that was specialized in attacking MikroTik routers found on companies’ internal networks via the CVE-2018-14847 vulnerability.


Similarities in the Meris code and the fact that many routers which pinged Rostelecom’s sinkhole using internal IPs confirmed the company’s theory that Meris was fully or partially assembled via the Glupteba malware.


However, it is currently unclear if the Glupteba gang built the Meris botnet themselves or if another group rented access to Glupteba-infected hosts to deploy the MikroTik module that eventually led to Meris’ creation.


Rostelecom-Solar said it notified authorities about their findings. The report was shared with the National Coordination Center for Computer Incidents (NKTsKI), a CERT-like organization created by the Russian Federal Security Service (FSB) in 2018.





#### Tags:
[[botnet]] [[Meris]] [[MikroTik]] [[Rostelecom-Solar]] [[DDoS]] [[Glupteba]] [[malware]] [[The Record]]
