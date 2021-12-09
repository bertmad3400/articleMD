# Hundreds of thousands of MikroTik devices still vulnerable to botnets
### Approximately 300,000 MikroTik routers are vulnerable to critical vulnerabilities that malware botnets can exploit for cryptomining and DDoS attacks.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/hundreds-of-thousands-of-mikrotik-devices-still-vulnerable-to-botnets/
+ Date: 2021-12-09T06:00:00-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/08/mikrotik-datacenter.jpg)

![mikrotik](https://www.bleepstatic.com/content/hl-images/2021/12/08/mikrotik-datacenter.jpg)


Approximately 300,000 MikroTik routers are vulnerable to critical vulnerabilities that malware botnets can exploit for cryptomining and DDoS attacks.


MikroTik is a Latvian manufacturer of routers and wireless ISPs who has sold over 2,000,000 devices globally.


In August, the Mēris botnet exploited vulnerabilities in MikroTik routers to create an army of devices that performed a [record-breaking DDoS attack on Yandex](https://www.bleepingcomputer.com/news/security/new-m-ris-botnet-breaks-ddos-record-with-218-million-rps-attack/). MikroTik [explained](https://www.bleepingcomputer.com/news/security/mikrotik-shares-info-on-securing-routers-hit-by-massive-m-ris-botnet/) that the threat actors behind the attack exploited vulnerabilities fixed in 2018 and 2019, but users hadn't applied.


Researchers have found that far too many remain vulnerable to three critical remote code execution flaws that can lead to a complete device takeover despite all of these warnings and attacks.


As illustrated in a report published by [Eclypsium](https://eclypsium.com/2021/12/09/when-honey-bees-become-murder-hornets/) today, the situation remains highly problematic.


Potent router swarm up for grabs
--------------------------------


Researchers from Eclypsium scanned the Internet for MikroTik devices that are still vulnerable to the following four CVEs:


* [CVE-2019-3977](https://nvd.nist.gov/vuln/detail/CVE-2019-3977): Remote OS downgrade and system reset. CVSS v3 – 7.5
* [CVE-2019-3978](https://nvd.nist.gov/vuln/detail/CVE-2019-3978): Remote unauthenticated cache poisoning. CVSS v3 – 7.5
* [CVE-2018-14847](https://nvd.nist.gov/vuln/detail/cve-2018-14847): Remote unauthenticated arbitrary file access and write. CVSS v3 – 9.1
* [CVE-2018-7445](https://nvd.nist.gov/vuln/detail/CVE-2018-7445): Buffer overflow enabling remote access and code execution. CVSS v3 – 9.8

The devices need to run RouterOS version 6.45.6 or older to be eligible for exploitation and have their WinBox protocol exposed to the Internet.


After scanning the Internet, Eclypsium found approximately 300,000 IP addresses for MikroTik routers that meet the above criteria and are vulnerable to at least one of the vulnerabilities mentioned above.


These devices have considerable horsepower, making them enticing targets for cryptomining and distributed denial-of-service attacks.


"First of all, they are plentiful with more than 2,000,000 devices deployed worldwide, and also particularly powerful and feature-rich devices," explained the [Eclypsium](http://eclypsium.com/2021/12/09/when-honey-bees-become-murder-hornets/) researchers.


"In addition to serving SOHO environments, MikroTik routers and wireless systems are regularly used by local ISPs. The same horsepower that can make MikroTik enticing to an ISP, can also be enticing to an attacker."


Most of the discovered devices are in China, Brazil, Russia, and Italy, while the United States has a significant number of exploitable devices too.



![World heatmap showing the widespread deployment of MikroTik devices](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/victim_map.jpg)**World heatmap showing the widespread deployment of MikroTik devices**  
*Source: Eclypsium*
Interestingly, the researchers found that coin-miners had infected about 20,000 of these devices, with roughly half of them attempting to connect to the now-offline CoinHive.



![Coinminer infections on vulnerable MikroTik devices](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/coinminers.jpg)**Coinminer infections on vulnerable MikroTik devices**  
*Source: Eclypsium*
Address the flaws now
---------------------


Unfortunately, even with repeated warnings and 2-year-old security updates to resolve these vulnerabilities, too many routers are not updated to the latest software.


Furthermore, devices exploited before the security updates must be analyzed and passwords reset, as installing the updates will not resolve a prior compromise.


The [official MikroTik advice](https://blog.mikrotik.com/security/meris-botnet.html) towards all its customers can be summed in the following:


* Keep your MikroTik device up to date with regular upgrades.
* Do not open access to your device from the internet side to everyone. If you need remote access, only open a secure VPN service, like IPsec.
* Use a strong password, and even if you do, change it now!
* Don’t assume your local network can be trusted. Malware can attempt to connect to your router if you have a weak password or no password.
* Inspect your RouterOS configuration for unknown settings including: System -> Scheduler rules that execute a Fetch script. Remove these., IP -> Socks proxy. If you don’t use this feature or don’t know what it does, it must be disabled., L2TP client named “lvpn” or any L2TP client that you don’t recognize.
* Input firewall rule that allows access for port 5678.
* Block domains and tunnel endpoints associated with the Meris botnet.

In addition to these guidelines, Eclypsium has released a [free MikroTik assessment tool](https://github.com/eclypsium/mikrotik_meris_checker) that can check if a device is vulnerable to CVE-2018-14847 and if a scheduler script exists, an indication of Mēris compromise.



![MikroTik assessment tool](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**MikroTik assessment tool**
MikroTik owners must address the flaws on their devices, as the malware can harm the devices due to extensive cryptomining and make the device a physical part of malicious operations.


Bleeping Computer has reached out to MikroTik for a comment on the above, and got the following response:



> 
> Eclypsium report deals with the same old vulnerabilities we have mentioned in our previous security blogs. As far as we know - there are no new vulnerabilities in RouterOS. Furthermore, RouterOS has been recently independently audited by several third parties. They all arrived at the same conclusion.
> 
> 
> Unfortunately, closing the old vulnerability does not immediately protect the affected routers. We don’t have an illegal backdoor to change the user’s password and check their firewall or configuration. These steps must be done by the users themselves.
> 
> 
> We try our best to reach out to all users of RouterOS and remind them to do software upgrades, use secure passwords, check their firewall to restrict remote access to unfamiliar parties, and look for unusual scripts. Unfortunately, many users have never been in contact with MikroTik and are not actively monitoring their devices. We cooperate with various institutions worldwide to look for other solutions as well.
> 
> 
> Meanwhile, we want to stress the importance of keeping your RouterOS installation up to date once again. That is the essential step to avoid all kinds of vulnerabilities.
> 
> 
> 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.country.name=Latvia]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Brazil]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Mikrotik]] [[Eclypsium]] [[Routeros]] [[Cvss]] [[V3]] [[Cryptomining]] [[Bleeping Computer]]
#### CVE's
[[CVE-2019-3977]] [[CVE-2019-3978]] [[CVE-2018-14847]] [[CVE-2018-7445]]

