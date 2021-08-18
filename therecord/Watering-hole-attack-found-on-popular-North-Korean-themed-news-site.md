# Watering hole attack found on popular North Korean-themed news site
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/watering-hole-attack-found-on-popular-north-korean-themed-news-site/)
+ Date: August 18, 2021
+ Author: Catalin Cimpanu


## Article:
![Watering hole attack found on popular North Korean-themed news site](https://therecord.media/wp-content/uploads/2021/08/Kim-Jong-un.jpg)

A North Korean cyber-espionage group has breached one of the most popular North Korean-themed news sites on the internet in order to carry out a watering hole attack and infect some of the site’s visitors with malware.


The [watering hole attack](https://en.wikipedia.org/wiki/Watering_hole_attack) lasted from at least late March 2021 until early June 2021, security firm Volexity said in a [report](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/) yesterday.


The attack kit consisted of two browser exploits, loaded on the site using a JavaScript file, which would infect users’ systems visiting the [Daily NK](https://en.wikipedia.org/wiki/Daily_NK) website using old Internet Explorer and legacy Edge browsers.


According to Volexity, the attackers leveraged [CVE-2020-1380](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2020-1380), a vulnerability in the old IE, and [CVE-2021-26411](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26411), a newer exploit in the IE and legacy Edge browsers. For both vulnerabilities, the threat actor used public proof-of-concept code posted online in previous months[[1](https://www.trendmicro.com/en_us/research/20/h/cve-2020-1380-analysis-of-recently-fixed-ie-zero-day.html), [2](https://enki.co.kr/blog/2021/02/04/ie_0day.html)], the Volexity team said.


The final payloads of these attacks differed across time but included a Cobalt Strike backdoor beacon, which could be used to deploy other malware, or a new malware strain called **BlueLight**, which could be used to download and execute shellcode or other apps or search through local files.


The breadth of the attack and how many users were infected are currently unknown.


The Daily NK website is one of the Top 50,000 most popular websites on the internet, according to the Tranco unified traffic ranking. The website, operated out of South Korea and published in English, is known for its coverage of North Korean topics and is considered a top source and subject matter experts on North Korean politics.


Volexity pinned the intrusion into Daily NK’s servers on a North Korean cyber-espionage group known in the cyber-security community under codenames such as [APT37](https://malpedia.caad.fkie.fraunhofer.de/actor/apt37), ScarCruft, Ricochet Chollima, and InkySquid.


A spokesperson for the Daily NK did not return a request for comment sent by The Record yesterday.





#### Tags:
[[Volexity]] [[NK]] [[The Record]]
