# These researchers wanted to test cloud security. They were shocked by what they found
### Cybersecurity researchers set up a tempting cloud honeypot to examine how cyber attackers work.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/these-researchers-wanted-to-test-cloud-security-they-were-shocked-by-what-they-found/)
+ Date: December 1, 2021
+ Author: Danny Palmer


## Article:
Unknown

Insecure cloud-computing services can be a huge risk for organisations because they're a regular target for cyber criminals. Researchers have demonstrated how [vulnerable or misconfigured cloud services](https://www.zdnet.com/article/cloud-security-in-2021-a-business-guide-to-essential-tools-and-best-practices/) can be, after deploying hundreds of honeypots designed to look like insecure infrastructure, some of which lasted just minutes before being compromised by hackers.

[Cybersecurity researchers at Palo Alto Networks](https://unit42.paloaltonetworks.com/exposed-services-public-clouds/) set up a honeypot compromised of 320 nodes around the world, made up of multiple misconfigured instances of common cloud services, including remote desktop protocol (RDP), secure shell protocol (SSH), server message block (SMB) and Postgres databases. 


The honeypot also included [accounts configured to have default or weak passwords](https://www.zdnet.com/article/these-are-the-terrible-passwords-that-people-are-still-using-heres-how-to-do-better/) -- exactly the sort of things that cyber criminals are looking for when trying to breach networks. 

**SEE**: [**Cloud security in 2021: A business guide to essential tools and best practices**](https://www.zdnet.com/article/cloud-security-in-2021-a-business-guide-to-essential-tools-and-best-practices/)

And it wasn't long before cyber criminals discovered the honeypot and looked to exploit it -- some of the sites were compromised in minutes while 80% of the 320 honeypots were compromised within 24 hours. All of them had been compromised within a week. 

The most attacked application was secure shell, which is a network communication protocol that enables two machines to communicate. Each SSH honeypot was compromised 26 times a day on average. The most attacked honeypot was compromised a total of 169 times in just a single day. 

Meanwhile, one attacker compromised 96% of the 80 Postgres honeypots within a single 90-second period. 






"The speed of vulnerability management is usually measured in days or months. The fact that attackers could find and compromise our honeypots in minutes was shocking. This research demonstrates the risk of insecurely exposed services," said Jay Chen, principal cloud security researcher at Palo Alto Networks. 

Exposed or poorly configured cloud services like those deployed in the honeypot make tempting targets for cyber criminals of all kinds.  

Several notorious [ransomware](https://www.zdnet.com/article/have-we-reached-peak-ransomware-how-the-internets-biggest-security-problem-has-grown-and-what-happens-next/) operations are known to [exploit exposed cloud services](https://www.zdnet.com/article/ransomware-vs-wfh-how-remote-working-is-making-cyberattacks-easier-to-pull-off/) to gain initial access to the victim's network in order to eventually encrypt as much as possible and demand a multi-million dollar ransom in exchange for the decryption key. 

Meanwhile, [nation state-backed hacking groups are also known to target vulnerabilities in cloud services](https://www.zdnet.com/article/microsoft-office-365-is-becoming-the-core-of-many-businesses-and-hackers-have-noticed/) as stealthy means of entering networks in order to conduct espionage, steal data, or deploy malware without detection. 

**SEE:**[**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/)**(ZDNet special report)**

And as the research demonstrates, it doesn't take long for cyber criminals to find exposed internet-facing systems. 

"When a vulnerable service is exposed to the internet, opportunistic attackers can find and attack it in just a few minutes. As most of these internet-facing services are connected to some other cloud workloads, any breached service can potentially lead to the compromise of the entire cloud environment," said Chen.  

When it comes to securing accounts used to access cloud services, organisations should avoid using default passwords and users should be provided with [multi-factor authentication](https://www.zdnet.com/article/multi-factor-authentication-use-it-for-all-the-people-that-access-your-network-all-the-time/) to create an extra barrier to prevent leaked credentials being exploited.  

It's also vital for organisations to apply security patches when they're available in order to prevent cyber criminals from taking advantage of known exploits -- [and it's a strategy that applies to cloud applications, too](https://www.zdnet.com/article/many-organisations-dont-know-how-to-manage-vpn-security-properly-and-cyber-criminals-are-taking-advantage/).  

"The outcome [of the research] reiterates the importance of mitigating and patching security issues quickly. When a misconfigured or vulnerable service is exposed to the internet, it takes attackers just a few minutes to discover and compromise the service. There is no margin of error when it comes to the timing of security fixes," said Chen. 

### **MORE ON CYBERSECURITY**

* [**Two-thirds of cloud attacks could be stopped by checking configurations, research finds**](https://www.zdnet.com/article/two-thirds-of-cloud-attacks-could-be-stopped-by-checking-configurations-research-finds/)
* [**A cloud company asked security researchers to look over its systems. Here's what they found**](https://www.zdnet.com/article/a-cloud-company-asked-security-researchers-to-look-over-its-development-systems-heres-what-they-found/)
* **[Unsecured servers and cloud services: How remote work has increased the attack surface that hackers can target](https://www.zdnet.com/article/unsecured-servers-and-cloud-services-how-remote-work-has-increased-the-attack-surface-that-hackers-can-target/)**
* [**Don't want to get hacked? Then avoid these three 'exceptionally dangerous' cybersecurity mistakes**](https://www.zdnet.com/article/dont-want-to-get-hacked-then-avoid-these-three-exceptionally-dangerous-cybersecurity-mistakes/)
* **[**Critical security alert: If you haven't patched this old VPN vulnerability, assume your network is compromised**](https://www.zdnet.com/article/critical-security-alert-if-you-havent-patched-this-two-year-old-vpn-vulnerability-assume-your-network-is-compromised/)**





#### Tags:
[[cloud]] [[honeypots]] [[organisations]] [[misconfigured]] [[ZDNet]]
