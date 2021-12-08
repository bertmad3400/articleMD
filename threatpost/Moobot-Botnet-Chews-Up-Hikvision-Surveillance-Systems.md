# Moobot Botnet Chews Up Hikvision Surveillance Systems
### Attackers are milking unpatched Hikvision video systems to drop a DDoS botnet, researchers warned.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176879
+ Date: 2021-12-08T20:13:18+00:00
+ Author: Becky Bracken


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/08151148/cow-e1638994326421.png)

Although a patch was released in September, any still-vulnerable Hikvision IP Network Video Recorder (NVR) products are being actively targeted by the Mirai-based botnet [known](https://threatpost.com/mootbot-fiber-routers-zero-days/154962/) as Moobot.


FortiGuard Labs has released a report detailing how the Moobot botnet is leveraging a known [remote code execution (RCE) vulnerability](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36260) in Hikvision products (CVE-2021-36260) to spread a Moobot, which carries out distributed denial of service (DDoS) attacks.


The attack surface could be significant: China-based Hikvision touted itself as the “world’s leading [video-surveillance products supplier](https://us.hikvision.com/en/about/hikvision-global)” on the company site.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Once the attacker finds a vulnerable system, a downloader drops the malware, which FortiGuard identified as Moobot, a variant of Mirai with traces of Satori code. Sartori is another [Mirai-based botnet](https://threatpost.com/mirai-botnet-sees-big-2019-growth-shifts-focus-to-enterprises/146547/) and one of dozens that have been spun off the original source code.


“Its most obvious feature is that it contains the data string “w5q6he3dbrsgmclkiu4to18npavj702f”, which is used in the “rand\_alphastr” function,” the researchers found in analyzing the binary. “It is used to create random alphanumeric strings with different purposes, such as for a setup process name or to generate data for attacking.”


Once it makes a connection with the command-and-control server (C2), it launches the DDoS attack, the report added, which looks like this:


**Tracked to DDoS Service Provider**
------------------------------------


The analysts were able to track the code to a DDoS service provider’s Telegram channel called “tianrian,” which has been operating since August, they added.


“From the chatting channel we can see that the service is still updating,” FortiGuard’s report cautioned. “Users should always look out for DDoS attacks and apply patches to vulnerable devices.”


During Q3, threat researchers at Kaspersky found that the number of [DDoS attacks shattered records](https://threatpost.com/ddos-attacks-records-q3/176082/), often topping thousands per day.


Linux-based Mirai was first identified in September of 2016 when it was used in a DDoS attack [against Krebs on Security](https://krebsonsecurity.com/2016/09/krebsonsecurity-hit-with-record-ddos/). A month later it took out a vast swath of the internet with [a hit on Dyn](https://threatpost.com/dyn-ddos-could-have-topped-1-tbps/121609/). And despite its source code [being released](https://threatpost.com/source-code-released-for-mirai-ddos-malware/121039/) in October 2016, it has since become one of the most [powerful internet of things botnets](https://threatpost.com/mirai-variant-sonicwall-d-link-iot/164811/), infecting products and gadgets from brands including D-Link, SonicWall and Netgear, and other connected devices.


Fortinet listed [Mirai as the top botnet threat](https://threatpost.com/attackers-will-flock-to-crypto-wallets-linux-in-2022-podcast/176546/) in its analysis of the first half of 2021. The report’s author Derek Manky, Fortiguard Labs’ chief of security insights and global threat alliances doesn’t expect Mirai, or its related threat variants, to go away anytime soon.


“We’re going to fully expect to see more of [Mirai],” Manky said. “More Linux-based botnets. A lot of these targets, we’re not talking about Windows, but MacOS, we’ve already seen more and more … code written for Linux itself, and that is a majority of the [internet of things, or IoT] space.”


Any organizations running unpatched Hikvision systems are urged to get the [firmware update](https://www.hikvision.com/en/support/cybersecurity/security-advisory/security-notification-command-injection-vulnerability-in-some-hikvision-products/) provided by the company.


***There’s a sea of unstructured data on the internet relating to the latest security threats.***[***REGISTER TODAY***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This***[***LIVE, interactive Threatpost Town Hall***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***, sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***  

[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)**for the LIVE event!**





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Location:
[[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ddos]] [[Hikvision]] [[Botnet]] [[Moobot]] [[Mirai]] [[Fortiguard]] [[ThreatPost]]
#### CVE's
[[CVE-2021-36260]]

