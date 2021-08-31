# Initial Access Broker use, stolen account sales spike in cloud service cyberattacks
### Current trends also include the abuse of Docker images.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/initial-access-broker-use-stolen-account-sales-spike-in-cloud-service-cyberattacks/)
+ Date: August 31, 2021 -- 12:00 GMT (13:00 BST)
+ Author: Charlie Osborne


## Article:
Unknown

There is rising demand for the services of Initial Access Brokers (IABs) and access credentials in cloud-based cyberattacks. 


On Tuesday, Lacework [published](https://www.lacework.com/resources/) its 2021 Cloud Threat Report vol.2, outlining how today's cybercriminals are attempting to cut out some of the legwork involved in campaigns against cloud service providers.  

Over this year, the cloud security firm's team has observed a number of trends of note in [the cloud space](https://www.zdnet.com/article/cloud-security-in-2021-a-business-guide-to-essential-tools-and-best-practices/), including increased demand for IABs.  

Initial Access Brokers, as documented [by KELA](https://www.zdnet.com/article/ransomware-operators-love-them-key-trends-in-the-initial-access-broker-space/), are individuals or groups which have managed to secure access to a target system. Access may have been obtained through weak, broken, or stolen credentials; an insider, or by way of a vulnerability. 

The average price of network access, as analyzed by the team, is currently $5,400, while the median price is $1,000, depending on the level of access obtained and the target organization.  

Ransomware groups have taken an interest in IABs, and alongside these groups, other threat actors focused on exploiting cloud services are also attempting to recruit IABs for their own ends.  

Lacework says that over the past few months, administrator credentials obtained by IABs appear to have become a popular resource for attackers. In addition, the scanning and probing of storage buckets, online databases, login platforms, and orchestration systems continue to increase.  






"What started as one-off marketplace postings continues to escalate as criminals begin to understand and operationalize the utility of access to cloud services above and beyond cryptocurrency mining," the team says.  

The report also explores the latest [TeamTNT](https://www.zdnet.com/article/a-crypto-mining-botnet-is-now-stealing-docker-and-aws-credentials/) criminal operation activities against cloud services. The TeamTNT botnet, first spotted back in 2020, is known to install cryptocurrency-mining malware on vulnerable containers. 

TeamTNT is hunting for exposed Docker APIs to deploy malicious Docker images, and in numerous cases, public Docker repositories are being taken over through compromised accounts to host malware. 

Another tactic of note is the exploitation of [canary tokens](https://www.lacework.com/blog/canarytokensandransomwareoperations/). The team suspects that the legitimate canarytokens.org service, used to alert users when a resource has been accessed, has also been abused to notify ransomware operators of malware execution on a victim's system.  

Additional points of interest include honeypot data collected by the firm, which suggests SSH, SQL, Docker, and Redis services are most commonly targeted. Tor is often employed when AWS environments are targeted; the zgrab scanner is employed to probe Docker APIs for weaknesses; and when it comes to Redis, the command line interface INFO command is most commonly used to harvest data concerning target systems.  

###  Previous and related coverage

* [Cloud security in 2021: A business guide to essential tools and best practices](https://www.zdnet.com/article/cloud-security-in-2021-a-business-guide-to-essential-tools-and-best-practices/)  

* [Cloud security: 'Suspicious superhumans' behind rise in attacks on online services](https://www.zdnet.com/article/cloud-security-suspicious-superhumans-behind-rise-in-attacks-on-online-services/)  

* [What is cloud computing? Everything you need to know about the cloud explained](https://www.zdnet.com/article/what-is-cloud-computing-everything-you-need-to-know-about-the-cloud/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[cloud]] [[Cloud]] [[TeamTNT]] [[ZDNet]]
