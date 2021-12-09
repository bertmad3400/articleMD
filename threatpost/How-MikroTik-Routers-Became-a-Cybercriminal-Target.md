# How MikroTik Routers Became a Cybercriminal Target
### The powerful devices leveraged by the Meris botnet have weaknesses that make them easy to exploit, yet complex for organizations to track and secure, researchers said.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176894
+ Date: 2021-12-09T15:56:16+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2018/03/10101223/Router_Target_Privacy.jpg)

The routers leveraged by the Mēris botnet in a [massive distributed denial-of-service (DDoS) attack](https://threatpost.com/yandex-meris-botnet/169368/) against Russia’s internet giant Yandex have also been the unwitting platform for numerous cyberattacks, researchers have found. This is due to a persistent vulnerable state that’s difficult for organizations to wrangle, but easy for threat actors to exploit, they said.


Researchers from Eclypsium took a deep dive into the feature-rich small office/home office (SOHO) and internet-of-things (IoT) devices [from Latvia-based company](https://threatpost.com/thousands-of-mikrotik-routers-hijacked-for-eavesdropping/137165/) MikroTik, which number some 2 million in deployments.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Due to the sheer number of devices in use, their high power and numerous known [vulnerabilities](https://threatpost.com/poc-attack-escalates-mikrotik-router-bug-to-as-bad-as-it-gets/138076/) within them, threat actors have been using MikroTik devices for years as the command center from which to launch numerous attacks, researchers said.


**The MikroTik Attack Surface**
-------------------------------


Eclypsium researchers began exploring the how and why of the weaponization of MikroTik devices in September, based on previous research into how TrickBot threat actors used compromised routers as command-and-control (C2) infrastructure. Eclypsium analysts found that TrickBot also was able to fall back on MikroTik infrastructure after U.S. Cyber Command successfully [disrupted](https://threatpost.com/trickbot-takedown-crimeware-apparatus/160018/) its main infrastructure.


“This made us want to better understand the MikroTik attack surface and how attackers might use them once compromised,” they wrote.


In addition to their power, one of the chief reasons MikroTik devices are so popular with attackers is that they are, like many SOHO and IoT devices, vulnerable out of the box. They often come with default credentials of admin/empty password, and even devices that are intended for corporate environments come without default settings for the WAN port, researchers wrote.


Additionally, MikroTik devices often miss out on important firmware patches because their auto-upgrade feature is rarely turned on, “meaning that many devices are simply never updated,” according to Eclypsium.


This has allowed CVEs dating back to 2018 and 2019 — one of which was used by in the Yandex attack — to remain unpatched on many devices and ripe for exploitation, researchers said. The bugs tracked as [CVE-2019-3977](https://nvd.nist.gov/vuln/detail/CVE-2019-3977), [CVE-2019-3978](https://nvd.nist.gov/vuln/detail/CVE-2019-3978), [CVE-2018-14847](https://nvd.nist.gov/vuln/detail/CVE-2018-14847) and [CVE-2018-7445](https://nvd.nist.gov/vuln/detail/CVE-2018-7445) can all lead to pre-authenticated remote code execution (RCE) — and a complete takeover of a device.


MikroTik devices also have “an incredibly complex configuration interface” that invites easy mistakes from those setting them up, which allows attackers to easily discover and abuse them over the internet, researchers said.


**Multiple Cyberattack Scenarios**
----------------------------------


“The capabilities demonstrated in these attacks should be a red flag for enterprise security teams,” researchers wrote in [a report](https://eclypsium.com/2021/12/09/when-honey-bees-become-murder-hornets/) published Thursday. “The ability for compromised routers to inject malicious content, tunnel, copy or reroute traffic can be used in a variety of highly damaging ways.”


These include the use of DNS poisoning to redirect a remote worker’s connection to a malicious website or introduce a machine-in-the-middle attack; the use of well-known techniques and tools to  

potentially capture sensitive information or steal two-factor authentication (2FA) credentials; the tunneling of enterprise traffic to another location; or the injection of malicious content into valid traffic, researchers said.


Then there was the Mēris botnet attack — which happened soon after Eclypsium began its research. Requests used in the DDoS HTTP-pipelining attack on Russia’s internet giant Yandex in September originated from MikroTik networking gear, with attackers exploiting a 2018 bug unpatched in the more than 56,000 MikroTik hosts involved in the incident.


And, Eclypsium also found approximately 20,000 devices with proxies open, which were injecting different crypto-mining scripts into web pages.


“These devices are both powerful, and as our research shows, often highly vulnerable,” they noted, adding that MikroTik devices, in addition to serving SOHO environments, are regularly used by local Wi-Fi networks, which also attracts attention from attackers, they wrote.


Threatpost has reached out to MikroTik for comment on the researchers’ findings and conclusions.


**Tool to Mitigate Risk**
-------------------------


Researchers used Shodan queries to build a dataset of 300 000 IP addresses vulnerable to at least one of the aforementioned RCE exploits and also tracked geographically where the devices were located, finding that they are “particularly widespread,” they wrote. Researchers found that China, Brazil, Russia, Italy and Indonesia had the most total vulnerable devices, with the United States coming in at eight on the list.


Eclypsium has created a [freely available tool](https://github.com/eclypsium/mikrotik_meris_checker) that could allow network administrators to test their devices’ vulnerability, in three ways: Identify MikroTik devices with CVEs that would allow the device to be taken over; attempt to log in with a given list of default credentials; and check for indicators of compromise of the Mēris botnet.


The tool works across SSH, WinBox and HTTP API protocols, all of which the Mēris malware uses, researchers said. Eclypsium recommended that enterprises using the tool only attempt to log into the MikroTik devices that they own and to take liability for their actions.


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** ***[REGISTER TODAY](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)*** ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This [LIVE, interactive Threatpost Town Hall](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article), sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***for the LIVE event!***


 


 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=Tor]] [[action.malware.name=TrickBot]]

#### Industry:
[[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=Indonesia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.country.name=Latvia]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Brazil]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Mikrotik]] [[Eclypsium]] [[Mēris]] [[Botnet]] [[Yandex]] [[Threatpost]] [[ThreatPost]]
#### CVE's
[[CVE-2019-3977]] [[CVE-2019-3978]] [[CVE-2018-14847]] [[CVE-2018-7445]]

