# FreakOut botnet now attacks vulnerable video DVR devices
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/freakout-botnet-now-attacks-vulnerable-video-dvr-devices/)
+ Date: October 12, 2021
+ Author: Bill Toulas


## Article:
![malware botnet](https://www.bleepstatic.com/content/hl-images/2021/02/02/Malware-scanner.jpg?rand=755812512)


A new update to the FreakOut (aka Necro, N3Cr0m0rPh) Python botnet has added a recently published PoC exploit for Visual Tools DVR in its arsenal to further aid in breaching systems.


Mining Monero on a DVR
----------------------


Researchers at [Juniper Threat Labs](https://blogs.juniper.net/en-us/threat-research/necro-python-botnet-goes-after-vulnerable-visualtools-dvr) have analyzed a recent sample of the malware, and warn that Visual Tools DVR VX16 4.2.28.0 from visual-tools.com is being targeted with an exploit for a CVE-less flaw.


The targeted device is a digital video recorder used in professional-grade surveillance video equipment installations, supporting up to 16 cameras and live video transmission to two monitors.


Compromising a DVR device could allow the threat actors to spread laterally in an internal corporate network that the DVR resides on. Additionally, the device could be incorporated into the botnet’s DDoS swarm.



![HTTP request attacking Visual Tools DVR](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/attack%20DVR.png)**HTTP request attacking Visual Tools DVR**  

Source: Juniper Labs
In this case, the actors are largely interested in abusing the compromised hardware resources for mining cryptocurrency.


The PoC (proof of concept) for the new exploit, which is an unauthenticated command injection, was [published on July 6, 2021](https://www.exploit-db.com/exploits/50098), and is incorporated on top of numerous other exploits such as those given below:


* CVE-2020-15568 – TerraMaster TOS before 4.1.29
* CVE-2021-2900 – Genexis PLATINUM 4410 2.1 P4410-V2-1.28
* CVE-2020-25494 – Xinuos (formerly SCO) OpenServer v5 and v6
* CVE-2020-28188 – TerraMaster TOS
* CVE-2019-12725 – Zeroshell 3.9.0


When the FreakOut botnet's scans detect a vulnerable system, they will use the exploit to gain access, and install an XMRig Monero miner on the device.


The functions still seen in the latest versions of the FreakOut malware include brute-force spreading and network sniffing, so depending on the interest of the actor or the value of the compromised entity, the attacks could grow into more a more advanced compromise.


New tricks
----------


Another interesting aspect of the botnet’s functionality is the domain generation algorithm (DGA) used for both its command and control and the download servers.


The malware appears to be using a different seed in each campaign, to generate up to 253 unique pseudo-random domains to be used in the operations. The idea is to evade domain flagging and take-downs that reduce its effectiveness.



![Using fresh DGA domains on new campaigns](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/DGA.png)**Using fresh DGA domains on new campaigns**  

Source: Juniper Labs
Some important differences compared to FreakOut samples analyzed in previous months are:


* The SMB scanner has been removed
* The script injection URL has changed from being hardcoded to a DGA one
* The DDoS-supporting TOR Socks proxies have been replaced with new ones


To get an idea of how active the development of FreakOut is, the malware had two notable upgrades this year. [One in January](https://www.bleepingcomputer.com/news/security/freakout-malware-exploits-critical-bugs-to-infect-linux-hosts/) when it added Linux-targeting exploits in its arsenal, and [one in June](https://www.bleepingcomputer.com/news/security/freakout-malware-worms-its-way-into-vulnerable-vmware-servers/) when it was upgraded to target vulnerable VMWare servers.


Botnets are always on the look for unpatched systems, and although they add new exploits, they are commonly not zero-days. If you follow proper patching practices and monitor your networks for suspicious activity, you should be safe from this threat. 




#### Tags:
[[DVR]] [[malware]] [[Bleeping Computer]]
