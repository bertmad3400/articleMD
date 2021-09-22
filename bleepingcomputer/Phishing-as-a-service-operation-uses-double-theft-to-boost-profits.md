# Phishing-as-a-service operation uses double theft to boost profits
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/phishing-as-a-service-operation-uses-double-theft-to-boost-profits/)
+ Date: September 22, 2021
+ Author: Sergiu Gatlan


## Article:
![Phishing-as-a-service operation uses double theft to boost profits](https://www.bleepstatic.com/content/hl-images/2021/09/22/Hacker_threat_actor.jpg)


Microsoft says BulletProofLink, a large-scale phishing-as-a-service (PhaaS) operation it spotted while investigating recent phishing attacks, is the driving force behind many phishing campaigns that have targeted many corporate organizations lately.


The threat actor behind **BulletProofLink (also known as BulletProftLink and Anthrax)** provides cybercriminals with various services, ranging from selling phish kits and email templates to providing hosting and automated services under a single payment or monthly subscription-based business model.


"In researching phishing attacks, we came across a campaign that used a rather high volume of newly created and unique subdomains—over 300,000 in a single run," the Microsoft 365 Defender Threat Intelligence Team [said](https://www.microsoft.com/security/blog/2021/09/21/catching-the-big-fish-analyzing-a-large-scale-phishing-as-a-service-operation/).


"With over 100 available phishing templates that mimic known brands and services, the BulletProofLink operation is responsible for many of the phishing campaigns that impact enterprises today."


The BulletProofLink threat actor was first spotted in October 2020 by OSINT Fans, who published a three-part series [[1](https://osint.fans/bulletproftlink-phishing-service-p1), [2](https://osint.fans/bulletproftlink-phishing-service-p2), [3](https://osint.fans/bulletproftlink-phishing-service-p3)] exposing some of the inner workings of this PhaaS operation.


As they revealed, the Bulletproftlink ICQ group chat had 1,618 members last year, "all potential buyers of the stolen passwords and the Bulletproftlink phishing services."



![BPL PhaaS](https://www.bleepstatic.com/images/news/u/1109292/2021/BPL%20PhaaS.png)*Image: Microsoft*
Double theft used to boost profits
----------------------------------


Of note, the large-scale phishing campaigns enabled by BulletProofLink also use a "double theft," a method meant to boost the threat actor's profits much like the double extortion one used by ransomware gangs.


The double theft Microsoft refers to is a tactic where credentials stolen in phishing attacks are also sent to a secondary server controlled by PhaaS operators if the phish kits used in the campaign use their default configuration.


This way, the credentials harvested by BulletProofLink customers are also sent to the phishing-as-a-service operator if the cybercriminals using their services will not customize the phish kits to exfiltrate stolen data only to their own servers.


"In both ransomware and phishing, the operators supplying resources to facilitate attacks maximize monetization by assuring stolen data, access, and credentials are put to use in as many ways as possible," Microsoft added.


"This is true for the BulletProofLink phishing kit, and in cases where the attackers using the service received credentials and logs at the end of a week instead of conducting campaigns themselves, the PhaaS operator maintained control of all credentials they resell."


Using this tactic, the PhaaS operators boost their profits without much effort, further motivating them and funding their ongoing operation.



![Phishing attack chain of BulletProofLink-enabled campaigns](https://www.bleepstatic.com/images/news/u/1109292/2021/Phishing%20attack%20chain%20of%20BulletProofLink-enabled%20campaigns.png)*Phishing attack chain of BulletProofLink-enabled campaigns (Microsoft)*
Infinite subdomain abuse
------------------------


The threat actor has also observed using a technique Microsoft calls "infinite subdomain abuse," making it possible for attackers to assign unique URLs for each phishing recipient while only using a single domain, compromised or bought before the attacks.


This tactic is used when the attackers can compromise a website's DNS or when compromised sites are configured using a DNS allowing unlimited wildcard subdomains.


Infinite subdomain abuse is an increasingly popular tactic, given that it minimizes the effort put into a phishing campaign while maximizing the number of available unique domains ready to be deployed at any single time.


Furthermore, "the creation of unique URLs poses a challenge to mitigation and detection methods that rely solely on exact matching for domains and URLs."


"At the time of this report, BulletProofLink continues to operate active phishing campaigns, with large volumes of redirections to their password-processing links from legitimate web hosting providers," Microsoft concluded.




#### Tags:
[[phishing]] [[Microsoft]] [[BulletProofLink]] [[PhaaS]] [[phish]] [[subdomain]] [[Bleeping Computer]]
