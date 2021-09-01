# This is why the Mozi botnet will linger on
### The botnet continues to haunt IoT devices, and likely will for some time to come.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/this-is-why-the-mozi-botnet-will-linger-on/)
+ Date: September 1, 2021 -- 11:53 GMT (12:53 BST)
+ Author: Charlie Osborne


## Article:
Unknown

It has been two years since the emergency of Mozi, and despite the arrest of its alleged author, the botnet continues to spread. 


Mozi was discovered in 2019 [by 360 Netlab](https://blog.netlab.360.com/mozi-another-botnet-using-dht/), and in the two years since, has grown from a small operation to a botnet that "accounted for an extremely high percentage of [Internet of Things] IoT traffic at its peak." 

According to Netlab ([translated](https://mp.weixin.qq.com/s/Su0-uU5JaUrAh8ptTzTCsA)), Mozi has accounted for over 1.5 million infected nodes, of which the majority -- 830,000 -- originate from China.  

Mozi is a P2P botnet that uses the DHT protocol. In order to spread, the botnet abuses weak Telnet passwords and known exploits to target networking devices, IoT, and video recorders, among other internet-connected products.  

The botnet is able to enslave devices to launch Distributed Denial-of-Service (DDoS) attacks, launch payloads, steal data, and execute system commands. If routers are infected, this could lead to Man-in-The-Middle (MITM) attacks. 

Earlier this month, Microsoft IoT security researchers said that Mozi [has evolved to](https://www.microsoft.com/security/blog/2021/08/19/how-to-proactively-defend-against-mozi-iot-botnet/) "achieve persistence on network gateways manufactured by Netgear, Huawei, and ZTE" by adapting its persistence mechanisms depending on each device's architecture. 

In July, Netlab claimed that the cybersecurity firm had [assisted law enforcement](https://twitter.com/360Netlab/status/1420390398825058313) to arrest the alleged developer of Mozi, and therefore, "we don't think it will continue to be updated for quite some time to come."  






However, the botnet lives on, and on Tuesday, the company has [provided its opinion](https://blog.netlab.360.com/the-mostly-dead-mozi-and-its-lingering-bots/) on why.  

"We know that Mozi uses a P2P network structure, and one of the "advantages" of a P2P network is that it is robust, so even if some of the nodes go down, the whole network will carry on, and the remaining nodes will still infect other vulnerable devices," Netlab says. "That is why we can still see Mozi spreading." 

According to the team, alongside the main Mozi\_ftp protocol, the discovery of malware using the same P2P setup -- Mozi\_ssh -- suggests that the botnet is also being used to cash in on illegal cryptocurrency mining. In addition, users are harnessing Mozi's DHT configuration module and creating new, functional nodes for it, which the team says allows them to "quickly develop the programs needed for new functional nodes, which is very convenient." 

"This convenience is one of the reasons for the rapid expansion of the Mozi botnet," Netlab added.  

The team also said that in a sample of the botnet dubbed v2s, captured last year, suggests that updates to Mozi have been focused on separating control nodes from "mozi\_bot" nodes, as well as improving efficiency. It may be that these changes were made by the authors to lease the network to other threat actors. 

"The Mozi botnet samples have stopped updating for quite some time, but this does not mean that the threat posed by Mozi has ended," the researchers say. "Since the parts of the network that are already spread across the internet have the ability to continue to be infected, new devices are infected every day." 

Netlab predicts that that week-by-week, the size of the botnet will gradually decrease, but it is likely that the impact of Mozi will be felt for some time to come.  

###  Previous and related coverage

* [This botnet is abusing Bitcoin blockchains to stay in the shadows](https://www.zdnet.com/article/this-botnet-is-abusing-bitcoin-blockchains-to-stay-in-the-shadows/)  

* [This ransomware-spreading malware botnet just won't go away](https://www.zdnet.com/article/this-ransomware-spreading-malware-botnet-just-wont-go-away/)  

* [Now this botnet is hunting for unpatched Microsoft Exchange servers](https://www.zdnet.com/article/now-this-botnet-is-hunting-for-unpatched-microsoft-exchange-servers/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[botnet]] [[Mozi]] [[Netlab]] [[P2P]] [[nodes,]] [[ZDNet]]
