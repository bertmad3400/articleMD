# MikroTik shares info on securing routers hit by massive Mēris botnet
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/mikrotik-shares-info-on-securing-routers-hit-by-massive-m-ris-botnet/)
+ Date: September 15, 2021
+ Author: Sergiu Gatlan


## Article:
![MikroTik shares info on securing routers hit by massive Mēris botnet](https://www.bleepstatic.com/content/hl-images/2021/09/15/Meris-botnet.jpg)


Latvian network equipment manufacturer MikroTik has shared details on customers can secure and clean routers enslaved by the massive Mēris DDoS botnet over the summer.


"As far as we have seen, these attacks use the same routers that were [compromised in 2018](https://blog.mikrotik.com/security/winbox-vulnerability.html), when MikroTik RouterOS had a vulnerability, that was quickly patched," a MicroTik spokesperson told BleepingComputer.


"Unfortunately, closing the vulnerability does not immediately protect these routers. If somebody got your password in 2018, just an upgrade will not help.


"You must also change password, re-check your firewall if it does not allow remote access to unknown parties, and look for scripts that you did not create."


IoT botnet on steroids
----------------------


The [Mēris botnet](https://www.bleepingcomputer.com/tag/meris/) has been behind two record-breaking volumetric (aka application-layer) DDoS attacks this year.


The first one [mitigated by Cloudflare in August](https://blog.cloudflare.com/cloudflare-thwarts-17-2m-rps-ddos-attack-the-largest-ever-reported/) reached 17.2 million request-per-second (RPS). The second one peaked at an [unprecedented rate of 21.8 million RPS](https://www.bleepingcomputer.com/news/security/new-m-ris-botnet-breaks-ddos-record-with-218-million-rps-attack/) while hammering Russian internet giant Yandex servers earlier this month.


According to [Qrator Labs](https://qrator.net/en/) researchers who provided details on the Yandex attack, Mēris — a botnet derived from Mirai malware code — is now controlling roughly 250,000 devices, most of them MikroTik network gateways and routers.


The researchers also added that the hosts compromised by Mēris are "not your typical IoT blinker connected to WiFi" but highly capable devices connected to the Intenet via an Ethernet connection.


Mēris' history of attacks targeting Yandex's network started in early August with a 5.2 million RPS DDpS attack and kept increasing in size:


* 2021-08-07 - 5.2 million RPS
* 2021-08-09 - 6.5 million RPS
* 2021-08-29 - 9.6 million RPS
* 2021-08-31 - 10.9 million RPS
* 2021-09-05 - 21.8 million RPS


How to secure and clean your MikroTik router
--------------------------------------------


MikroTik also shared info on how to clean and secure gateways compromised by this botnet in [a blog post published today](https://blog.mikrotik.com/security/meris-botnet.html).


The network equipment vendor urges customers to choose strong passwords that should defend their devices from brute-force attacks and keep them up to date to block [CVE-2018-14847 Winbox exploits](https://blog.mikrotik.com/security/winbox-vulnerability.html) used by the Mēris botnet.


The company outlined the best course of action, which includes the following steps:


* Keep your MikroTik device up to date with regular upgrades.
* Do not open access to your device from the internet side to everyone, if you need remote access, only open a secure VPN service, like IPsec.
* Use a strong password and even if you do, change it now!
* Don't assume your local network can be trusted. Malware can attempt to connect to your router if you have a weak password or no password.
* Inspect your RouterOS configuration for unknown settings.


Settings the Mēris malware can set when reconfiguring compromised MicroTik routers include:


* System -> Scheduler rules that execute a Fetch script. Remove these.
* IP -> Socks proxy. If you don't use this feature or don't know what it does, it must be disabled.
* L2TP client named "lvpn" or any L2TP client that you don't recognize.
* Input firewall rule that allows access for port 5678.


"We have tried to reach all users of RouterOS about this, but many of them have never been in contact with MikroTik and are not actively monitoring their devices. We are working on other solutions too," MikroTik added.


"As far as we know right now - There are no new vulnerabilities in these devices. RouterOS has been recently independently audited by several contractors." 




#### Tags:
[[MikroTik]] [[Mēris]] [[botnet]] [[RouterOS]] [[Yandex]] [[Bleeping Computer]]
