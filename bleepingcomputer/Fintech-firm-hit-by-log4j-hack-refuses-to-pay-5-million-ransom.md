# Fintech firm hit by log4j hack refuses to pay $5 million ransom
### One of the largest Vietnamese crypto trading platforms, ONUS, recently suffered a cyber attack on its payment system running a vulnerable Log4j version. Soon enough, threat actors approached ONUS to extort $5 million and threatened to publish the customer data should ONUS refuse to comply.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/fintech-firm-hit-by-log4j-hack-refuses-to-pay-5-million-ransom/
+ Date: 2021-12-29T07:07:07-05:00
+ Author: Ax Sharma


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j.jpg)

![log4j fire](https://www.bleepstatic.com/content/hl-images/2021/12/13/Log4j.jpg)


One of the largest Vietnamese crypto trading platforms, ONUS, recently suffered a cyber attack on its payment system running a vulnerable Log4j version.


Soon enough, threat actors approached ONUS to extort a $5 million sum and threatened to publish the customer data should ONUS refuse to comply.


After the company's refusal to pay the ransom, threat actors put up data of nearly 2 million ONUS customers for sale on forums.


Payment software ran a vulnerable log4j version
-----------------------------------------------


On December 9th, the [PoC exploit](http://web.archive.org/web/20211210193908/https://github.com/tangxiaofeng7/apache-log4j-poc) for the notorious [Log4Shell](https://www.bleepingcomputer.com/news/security/new-zero-day-exploit-for-log4j-java-library-is-an-enterprise-nightmare/) vulnerability (CVE-2021-44228) leaked on GitHub. And, that got the attention of opportunistic attackers who began [mass-scanning](https://twitter.com/bad_packets/status/1469225135504650240) the internet for vulnerable servers.


Between December 11th and 13th, threat actors successfully exploited the Log4Shell vulnerability on a Cyclos server of ONUS and planted backdoors for sustained access.


Cyclos provides a range of point-of-sale (POS) and payment software solutions, and like most vendors, was using a vulnerable log4j version in their software.


Although Cyclos did issue an [advisory](https://forum.cyclos.org/viewtopic.php?p=12374&sid=c8f5ff3a23e64a7bd6d042cb76ed387f#%20p12374) on the 13th and reportedly informed ONUS to patch their systems, it was too late.


Despite ONUS having patched their Cyclos instance, the exposure window allowed sufficient time for threat actors to exfiltrate sensitive databases.


These databases contained nearly 2 million customer records including E-KYC (Know Your Customer) data, personal information, and hashed passwords.


E-KYC workflows used by banks and FinTech companies typically involve procuring some form of identification documents and proofs from the customers, along with a 'video selfie' for automated verification.


Interestingly, the Log4Shell vulnerability existed on a sandbox server used "for programming purposes only" but allowed attackers further access into sensitive data storage locations (Amazon S3 buckets) with production data, due to a system misconfiguration. 


ONUS was then reportedly slapped with a $5 million extortion demand that they declined to meet. Instead, the company chose to disclose the attack to their customers via a private Facebook group.


"As a company that puts safety first, we are committed to providing our customers with transparency and integrity in business operations," stated ONUS CEO Chien Tran.


"That is why, after careful consideration, the right thing we need to do now is to inform the entire ONUS community about this incident."


A copy of the disclosure has been obtained by BleepingComputer, along with a rough English translation appended:



Misconfigured Amazon S3 buckets
-------------------------------


The hack itself is a little more than just a Log4j problem alone. Log4j exploit may have been the entry point for attackers, but improper access control on ONUS' Amazon S3 buckets allowed attackers undue access.


"The hacker took advantage of a vulnerability in a set of libraries on the ONUS system to get into the sandbox server (for programming purposes only)," explains ONUS.


"However, due to a configuration problem, this server contains information that gave bad guys access to our data storage system (Amazon S3) and stole some essential data. This leads to the risk of leaking the personal information of a large number of users."


The customer information retrieved by threat actors includes:



* Name
* Email and Phone number
* Address
* KYC information
* Encrypted password
* Transaction history
* And some other encrypted information

Cybersecurity firm CyStack, which provided services to ONUS, has conducted a thorough investigation and [released their findings](https://cystack.net/research/the-attack-on-onus-a-real-life-case-of-the-log4shell-vulnerability) on the attack mechanics and the backdoor planted by the attackers.


Nearly 2 million customer records put up for sale
-------------------------------------------------


By December 25th, after failing to secure the extortion amount from ONUS, threat actors put up the customer data for sale on a data breach marketplace, as seen by BleepingComputer:



![ONUS customer data put up for sale](https://www.bleepstatic.com/images/news/u/1164866/2021/Dec-2021/onus-log4j-hack/onus-data-forum.jpg)**Data of nearly 2 million ONUS customers put up for sale on a forum**(BleepingComputer)
The threat actors claim to have copies of 395 ONUS database tables with customers' personal information and hashed passwords in their possession.


Samples of such data were published by the threat actor in the forum post seen by BleepingComputer.


The samples also included images of customers' ID cards, passports, and customer-submitted video selfie clips procured during the KYC process.



![customer data hashed passwords](https://www.bleepstatic.com/images/news/u/1164866/2021/Dec-2021/onus-log4j-hack/customer-data-passwords.jpg)**Excerpts of customer data that the threat actor claims to have**(BleepingComputer)
"We sincerely apologize and hope for your understanding," [states](https://goonus.io/en/the-impact-of-a-cyber-attack-on-data-security/) ONUS.


"This is also an opportunity for us to review ourselves, upgrade and further perfect the system to assure the safety of our users, especially during the transition from [VNDC to ONUS](https://blog.vndc.io/en/announcement-onus-whitepaper-and-smart-contract/)."


CyStack's recommendations to ONUS included patching the Log4Shell vulnerability in Cyclos–as instructed by the vendor, deactivating leaked AWS credentials, properly configuring AWS access permissions, blocking public access to all sensitive S3 buckets, and imposing additional restrictions.


By now log4j vulnerabilities have been exploited by all kinds of threat actors from [state-backed hackers](https://www.bleepingcomputer.com/news/security/log4j-vulnerability-now-used-by-state-backed-hackers-access-brokers/) to [ransomware gangs](https://www.bleepingcomputer.com/news/security/new-ransomware-now-being-deployed-in-log4shell-attacks/) and a few others to [inject crypto miners](https://www.bleepingcomputer.com/news/security/log4j-attackers-switch-to-injecting-monero-miners-via-rmi/) on vulnerable systems.


The Conti ransomware gang has also been seen eying [vulnerable VMWare vCenter servers](https://www.bleepingcomputer.com/news/security/conti-ransomware-uses-log4j-bug-to-hack-vmware-vcenter-servers/) for exploitation.


Log4j users should immediately upgrade to the latest version 2.17.1 (for Java 8) [released yesterday](https://www.bleepingcomputer.com/news/security/log4j-2171-out-now-fixes-new-remote-code-execution-bug/). Backported versions 2.12.4 (Java 7) and 2.3.2 (Java 6) containing the fix are expected to be released shortly.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]]

#### Location:
[[victim.city.name=Tunis]] [[victim.country.name=Tunisia]] [[victim.continent.name=Africa]] [[victim.country.name=Vietnam]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Log4shell]] [[S3]] [[Log4j]] [[Bleepingcomputer]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-44228]]

