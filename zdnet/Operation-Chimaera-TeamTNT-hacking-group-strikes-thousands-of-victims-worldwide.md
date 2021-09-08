# Operation Chimaera: TeamTNT hacking group strikes thousands of victims worldwide
### The cybercriminals are now indiscriminate in the operating systems they attack.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/operation-chimaera-teamtnt-hacking-group-strikes-thousands-of-victims-worldwide/)
+ Date: September 8, 2021 -- 11:31 GMT (12:31 BST)
+ Author: Charlie Osborne


## Article:
Unknown

The TeamTNT hacking group has upped its game with a set of tools allowing it to indiscriminately target multiple operating systems. 


On Wednesday, cybersecurity researchers from AT&T Alien Labs [published a report](https://cybersecurity.att.com/blogs/labs-research/teamtnt-with-new-campaign-aka-chimaera) on a new campaign, dubbed Chimaera, that is thought to have begun on July 25, 2021 -- based on command-and-control (C2) server logs -- and one that has revealed an increased reliance on open source tools by the threat group.  

TeamTNT was first spotted [last year](https://www.zdnet.com/article/a-crypto-mining-botnet-is-now-stealing-docker-and-aws-credentials/) and was connected to the installation of cryptocurrency mining malware on vulnerable Docker containers. [Trend Micro](https://www.trendmicro.com/vinfo/hk-en/security/news/virtualization-and-cloud/coinminer-ddos-bot-attack-docker-daemon-ports) has also found that the group attempts to steal [AWS credentials](https://www.zdnet.com/article/a-crypto-mining-botnet-is-now-stealing-docker-and-aws-credentials/) to propagate on more servers, and Cado Security contributed the more recent discovery of TeamTNT targeting Kubernetes installations. 

Now, Alien Labs says the group is targeting Windows, AWS, Docker, Kubernetes, and various Linux installations, including Alpine. Despite the short time period, the latest campaign is responsible for "thousands of infections globally," the researchers say.

TeamTNT's portfolio of open source tools includes the port scanner Masscan, libprocesshider software for executing the TeamTNT bot from memory, 7z for file decompression, the b374k shell php panel for system control, and Lazagne. 

Lazagne is an open source project that lists browsers including Chrome and Firefox, as well as Wi-Fi, OpenSSH, and various database programs as supported for password retrieval and credential storage. 

[Palo Alto Networks](https://unit42.paloaltonetworks.com/teamtnt-operations-cloud-environments/) has also discovered that the group is using Peirates, a cloud penetration testing toolset to target cloud-based apps. 






"The use of open-source tools like Lazagne allows TeamTNT to stay below the radar for a while, making it more difficult for antivirus companies to detect," the company says. 

While now self-armed with the kit necessary to strike a wide variety of operating systems, TeamTNT still focuses on [cryptocurrency mining](https://www.zdnet.com/article/crypto-mining-worm-steal-aws-credentials/).  

Windows systems, for example, are targeted with the Xmrig miner. A service is created and a batch file is added to the startup folder to maintain persistence -- whereas a root payload component is used on vulnerable Kubernetes systems.  

Alien Labs says that as of August 30, a number of malware samples still have [low detection](https://www.virustotal.com/gui/file/caeb6eb1ee40fc4ac1da020a9a7542cffe55d29339306f6adf2d1e20e638538a/detection) rates.  

###  Previous and related coverage

* [Initial Access Broker use, stolen account sales spike in cloud service cyberattacks](https://www.zdnet.com/article/initial-access-broker-use-stolen-account-sales-spike-in-cloud-service-cyberattacks/)  

* [A crypto-mining botnet is now stealing Docker and AWS credentials](https://www.zdnet.com/article/a-crypto-mining-botnet-is-now-stealing-docker-and-aws-credentials/)  

* [Crypto-mining worm steals AWS credentials](https://www.zdnet.com/article/crypto-mining-worm-steal-aws-credentials/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[TeamTNT]] [[AWS]] [[ZDNet]]
