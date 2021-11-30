# EwDoor botnet targets AT&T network edge devices at US firms
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/ewdoor-botnet-targets-atandt-network-edge-devices-at-us-firms/)
+ Date: November 30, 2021
+ Author: Sergiu Gatlan


## Article:
![New EwDoor botnet targets AT&T network edge devices at US firms](https://www.bleepstatic.com/content/hl-images/2021/11/30/ATT_botnet.jpg)


A recently discovered botnet is attacking unpatched AT&T enterprise network edge devices using exploits for a four-year-old critical severity Blind Command Injection security flaw.


The botnet, dubbed **EwDoor** by researchers at Qihoo 360's Network Security Research Lab (360 Netlab), targets AT&T customers using EdgeMarc Enterprise Session Border Controller (ESBC) edge devices.


EdgeMarc appliances support high-capacity VoIP and data environments, bridging the gap between enterprise networks and their service providers, in this case, the AT&T carrier.


However, this also requires the devices to be publicly exposed to the Internet, increasing their exposure to remote attacks.


360 Netlab spotted the botnet on October 27 when the first attacks targeting Internet-exposed Edgewater Networks' devices unpatched against the critical CVE-2017-6079 vulnerability started.


Almost 6,000 compromised devices spotted in three hours
-------------------------------------------------------


The researchers were able to take a quick look at the botnet's size by registering one of its backup command-and-control (C2) domains and monitoring the requests made from infected devices.


During the three hours they had before the botnet's operators switched to a different C2 network communication model, 360 Netlab could spot roughly 5,700 infected devices.


"We confirmed that the attacked devices were EdgeMarc Enterprise Session Border Controller, belonging to the telecom company AT&T, and that all 5.7k active victims that we saw during the short time window were all geographically located in the US," the researchers [said in a report published today](https://blog.netlab.360.com/warning-ewdoor-botnet-is-attacking-att-customers/).


"By back-checking the SSl certificates used by these devices, we found that there were about 100k IPs using the same SSl certificate. We are not sure how many devices corresponding to these IPs could be infected, but we can speculate that as they belong to the same class of devices the possible impact is real."




> 
> Our latest blog is about EwDoor Botnet, all its infected devices are located in US, we saw around 6k compromised ips in a short 3 hours time window <https://t.co/1YHZZYqR3c>
> 
> 
> — 360 Netlab (@360Netlab) [November 30, 2021](https://twitter.com/360Netlab/status/1465682853820350464?ref_src=twsrc%5Etfw)


Backdoor with DDoS attack capabilities
--------------------------------------


After analyzing the versions captured since they discovered EwDoor, 360 Netlab says the botnet is likely used to launch distributed denial-of-service (DDoS) attacks and as a backdoor to gain access to the targets' networks.


It currently has six major features: self-updating, port scanning, file management, DDoS attack, reverse shell, and execution of arbitrary commands on compromised servers.


"So far, the EwDoor in our view has undergone 3 versions of updates, and its main functions can be summarized into 2 main categories of DDoS attacks and Backdoor," 360 Netlab added.


"Based on the attacked devices are telephone communication related, we presume that its main purpose is DDoS attacks, and gathering of sensitive information, such as call logs."



![EwDoor botnet](https://www.bleepstatic.com/images/news/u/1109292/2021/EwDoor_botnet.png)*EwDoor botnet (360 Netlab)*
EwDoor uses TLS encryption to block network traffic interception attempts and encrypts resources to block malware analysis.


Additional technical details on the EwDoor botnet and indicators of compromise (IOCs), including C2 domains and malware sample hashes, can be found in [360 Netlab's report](https://blog.netlab.360.com/warning-ewdoor-botnet-is-attacking-att-customers/).




#### Tags:
[[botnet]] [[EwDoor]] [[Netlab]] [[DDoS]] [[AT&T]] [[EdgeMarc]] [[devices.]] [[Bleeping Computer]]
