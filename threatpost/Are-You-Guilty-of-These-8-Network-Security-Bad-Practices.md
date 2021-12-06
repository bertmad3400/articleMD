# Are You Guilty of These 8 Network-Security Bad Practices?
### Tony Lauro, director of Security Technology & Strategy at Akamai, discusses VPNs, RDP, flat networks, BYOD and other network-security bugbears.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176798
+ Date: 2021-12-06T21:47:45+00:00
+ Author: Tony Lauro


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/06162635/Bad-business-practice-e1638826008203.jpg)

They say the first step in addressing a serious issue is admitting you have a problem. And so it is with network security. 


The ongoing explosion of ransomware events and breaches (many of which the public never hears about) is elevating network security to a top corporate priority. Employees are constantly reminded to change their passwords frequently, watch out for phishing attacks and comply with strict security policies. But companies are also failing to address the everyday practices and mindsets that undermine traditional safeguards and increase the risk of a breach.


To help refocus the thinking, let’s skip the network-security best practices; instead, let’s go over to the dark side and consider some *B**ad Practices*. Remember, these aren’t recommendations — they’re caution signs.



> **We want to know what your biggest cloud security concerns and challenges are, and how your company is dealing with them. Weigh in with our exclusive, anonymous [Threatpost Poll](https://threatpost.com/cloud-security-challenges-poll/176702/)!**
> 
> 


The first category of Bad Practices springs from the rise of work-at-home and work-from-anywhere models. Already in progress before the COVID-19 pandemic, decentralized work styles have really taken off in the past 18 months. And so have some risky practices.


**Bad Practice 1:**
-------------------


### ***“Business email, personal email…what’s the difference?”***


With many people still working from home, the lines between work life and personal life have become blurred. Sometimes, it’s just easier to use a personal email account or computer for communicating with colleagues. But this can dramatically increase the risk of a phishing attack aimed at credential harvesting or malware distribution, which can turn your home computer or business laptop into a vector for malware infecting many other users—including work colleagues. Once in your company’s email server, it’s free to access critical data assets.


**Bad Practice 2:**
-------------------


### ***“Go ahead, use my business laptop for web surfing!”***


Security-conscious companies wisely limit access to websites via the corporate network. But when working from home, all bets are off. So, your child might borrow your company laptop to visit a gaming or education site with weak security—or, worse yet, a malicious site that appears legitimate — potentially delivering malicious JavaScript which gains entry to your corporate network the next time you log in. The loosely collected cybercrime syndicate [known as Magecart](https://threatpost.com/magecart-server-side-itactics-changeup/166242/) has elevated malicious JavaScript to an art, skimming credit-card information and login credentials from websites. So, while the cybercriminals may not be targeting your company specifically, gaining opportunistic access to your corporate network will make their day.


**Bad Practice 3:**
-------------------


### ***“Relax, I’m using a VPN.”***


With cybercrime tactics continually evolving, using outdated technologies to secure remote access may provide a false sense of security. Virtual private networks (VPNs) are intended to provide a secure connection between two trusted points. But what if one of those points is infected with malware? If that point is your company laptop (see Bad Practice 2), you could serve as a vector for delivering it to your corporate network, and then it can spread laterally from system to system.  




Similar risks may exist when accessing your corporate network using remote desktop protocol (RDP) without encryption, or web applications without appropriate authentication or authorization for any connectivity model. All of these approaches to remote-access security should be considered way past their freshness date.


**Bad Practice 4:**
-------------------


### ***“In MFA we trust.”***


Remember when multi-factor authentication (MFA) was considered the gold standard for web-access security? Those days are over. There is now a cottage industry of bad actors focused on defeating MFA, most particularly two-factor authentication (2FA), where the push notifications used for delivering security codes can be circumvented by attackers. 


Last year, researchers from the Global Threat Intelligence Team at WMC [disclosed that they were tracking a threat actor who goes by the alias “Kr3pto”](https://www.wmcglobal.com/blog/kr3pto-puppeteer-kits-dynamic-phishing-kit-targeting-uk-banking-customers) selling phishing kits designed to acquire real-time security codes and 2FA data targeting U.K. financial institutions. And he or she is not alone. So, while MFA is better than nothing, it is not the rock-solid security savior many believe it to be.


All of these Bad Practices are important cautions in today’s work-from-anywhere world. But those responsible for managing corporate networks have their own Bad Practices to watch out for. Consider the following.


**Bad Practice 5:**
-------------------


### ***“A flat network is a simple network.”***


No one likes complexity. So, it’s not surprising that many network admins opt for the simplicity of a flat network. It’s just so much easier to manage than a network that is properly segmented. But in today’s world, it’s almost impossible to completely prevent intrusion by malware and ransomware. Intelligent network segmentation isolates mission-critical applications and data, preventing access to them by malicious code and limiting the scope of the inevitable infection. The more sophisticated your segmentation — through a micro-segmentation strategy — the more secure your network will be.


**Bad Practice 6:**
-------------------


### ***“BYOD means** **any** **device, right?”***


With many people working from home, “bring your own device” (BYOD) has taken on expanded meaning. Suddenly, your spouse’s tablet may seem like a viable option for accessing the monthly sales report. But does that device meet your company’s minimum-security standards? While iOS devices have traditionally offered better security safeguards than some other mobile operating systems, no personal device is completely secure.


**Bad Practice 7:**
-------------------


### ***“Always assume your corporate network is secure.”***


Sure, you’ve deployed tools to keep your network secure. But the increased use of cloud services, software-as-a-service (SaaS) applications, mobile and remote work models, and the internet of things (IoT) has dramatically increased the potential attack surface. To counter the threat, you need continuous monitoring of network activity. For example, inspecting passive DNS traffic can provide great insight into the health and activity of your environment for website acceptable use policy (AUP) compliance, malicious website blockage and malware protection. This can also be used to identify if there is any leakage of confidential information going out hidden in plain sight within these seemingly innocuous DNS requests. 


**Bad Practice 8:**
-------------------


### ***“Our network is our castle.”***


Not anymore. Digital transformation has changed that paradigm. Increasingly, your applications, data and users are outside the castle walls. Application workloads are running in the cloud and your users are accessing them from home or on the road. Today, your network is wherever your users are. Traditional perimeter security is not enough, and you need to rethink your security model to follow your users. That includes implementing a Secure Web Gateway (SWG) that provides a variety of critical security functions, including URL filtering, intelligent malware scanning, AUP enforcement, payload analysis and user authentication strategies that go beyond 2FA.


**New World, New Frameworks**
-----------------------------


In case you missed it, it’s a new world. In today’s decentralized, work-from-anywhere business environment, traditional network security strategies are not sufficient. Worse, they may provide a false sense of security that actually increases your risk. You need to think about new security frameworks designed to meet the challenges of this world without walls. This includes frameworks like zero-trust network architectures that provide modern access protections and micro-segmentation, and secure access service edge (SASE) to deliver effective security controls at the network edge, close to end users.


The solutions for securing your environment exist. The first step is admitting you have a problem. So, take a good, hard look at your organization: Do any of these Bad Practices sound familiar? 


***Tony Lauro is director of Security Technology & Strategy at [Akamai Technologies](http://www.akamai.com).***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Tunis]] [[victim.country.name=Tunisia]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Malware]] [[Phishing]] [[Cloud]] [[Work-from-anywhere]] [[Mfa]] [[ThreatPost]]

