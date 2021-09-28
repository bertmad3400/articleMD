# A cloud company asked security researchers to look over its development systems. Here's what they found
### With supply chain attacks increasingly common, cloud companies are looking to tighten their defences.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/a-cloud-company-asked-security-researchers-to-look-over-its-development-systems-heres-what-they-found/)
+ Date: September 28, 2021
+ Author: Danny Palmer


## Article:
Unknown

While [cloud computing services](https://www.zdnet.com/article/what-is-cloud-computing-everything-you-need-to-know-about-the-cloud/) are often touted as more secure than building applications and hosting them in-house, that doesn't mean those cloud services are without their own flaws. And with hackers increasingly looking to deploy their attacks through the software supply chain, cloud security is back in the spotlight.

Cybersecurity researchers found vulnerabilities in the infrastructure of a large software-as-a-service provider which if exploited by an attacker, could've been used by cyber criminals as part of a cloud-based supply chain attack. 

The unspecified SaaS provider [invited cybersecurity researchers at Palo Alto Networks](https://unit42.paloaltonetworks.com/cloud-threat-report-2h-2021/) to conduct a red team exercise on their development software pipeline in order to identify vulnerabilities in the supply chain.

"In just three days, a single Unit 42 researcher discovered critical software development flaws that left the customer vulnerable to an attack similar to those on SolarWinds and Kaseya VSA," the security company said.

At a time when so many businesses are reliant on [cloud services](https://www.zdnet.com/article/what-is-cloud-computing-everything-you-need-to-know-about-the-cloud/), it demonstrates how misconfigurations and vulnerabilities can have a huge impact if not managed properly because of the hundreds or even thousands of companies which are reliant on the infrastructure.

**SEE:**[**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/)**(ZDNet special report)**

Initially provided with the limited developer access a contractor would have, the researchers managed to elevate privileges to the extent they were able to gain administrator rights to the wider continuous integration (CI) cloud environment.  






Using this access, researchers examined all of the environment they could and were able to locate and gain access to 26 [Identity and Access Management](https://www.zdnet.com/article/best-enterprise-identity-access-management-software/) (IAM) keys. Some of these contained hard-coded credentials which provided unauthorised access to additional areas of the cloud environment, which could be exploited to gain administrator access – allowing what should have been an account with limited access gain privileges which open up the whole environment. 

While the company which had requested penetration testing was able to detect some of the activity researchers engaged in, it was only after administrator access had been gained that this was the case – in the event of a real attack, this would've been too late and attackers would have compromised the system.  

After the exercise, the researchers worked with the organization's security operations center, DevOps, and red and blue teams to develop a plan of action to tighten up security with a focus on the early identification of suspicious or malicious operations within their software development pipeline

The researchers knew what they were looking for so were able to easily identify misconfigurations and vulnerabilities to exploit. While this might involve advanced knowledge of these environments and how to exploit them, it's the sort of thing that specialised attack operations like [ransomware gangs or nation-state backed Advanced Persistent Threat Groups](https://www.zdnet.com/article/ransomware-attackers-targeted-this-company-then-defenders-discovered-something-curious/) (APTs) would also be familiar with - and will actively exploit if they can, as demonstrated by recent incidents. 

"Successful supply chain attacks are particularly devastating due to the widespread fallout of the attacks, for example potentially thousands of downstream customer environments being compromised. The risk of fallout conditions should mandate the increase of security mechanisms and procedures used to protect the supply chain", Nathaniel Quist, principal researcher at Unit 42 at Palo Alto Networks told ZDNet. 

**SEE:**[**Cloud security in 2021: A business guide to essential tools and best practices**](https://www.zdnet.com/article/cloud-security-in-2021-a-business-guide-to-essential-tools-and-best-practices/)

Part of the reason these environments can be exploited is because they're complex and can be difficult to secure – [it's understandably not a simple task](https://www.zdnet.com/article/unsecured-servers-and-cloud-services-how-remote-work-has-increased-the-attack-surface-that-hackers-can-target/) and vulnerabilities and misconfigurations can snowball to the extent that with patience and the right skills, attackers could exploit access to service providers and leave customers vulnerable to attacks. 

There are a number of things which can be done to help protect cloud environments from unauthorised access, including providing access to systems and services on a role-based basis. If developer staff don't need access to access management keys, then there's no reason they should be able to gain hold of them. 

"Role-Based Access Controls (RBAC) within the developer roles would have prevented the Unit 42 researchers from accessing all of the developer repositories. Had the client limited developer user accounts to only the repositories required to perform their job, it would have prevented the red team from identifying all of the 26 hardcoded IAM keys," said Quist. 

Organisations should also implement security checks and barriers as part of the development lifecycle. Because if this is implemented properly, it might be possible to determine that there's been unauthorised access to systems, something which could prevent an attack from being sent down the line to customers.

In this scenario, there's still a security issue to deal with, but dealing with it before hundreds or thousands of customers have been affected is a much better way to deal with it. 

**MORE ON CYBERSECURITY**

* [**Hackers are getting more hands-on with their attacks. That's not a good sign**](https://www.zdnet.com/article/hackers-are-getting-more-hands-on-with-their-attacks-thats-not-a-good-sign/)
* [**Half of businesses can't spot these signs of insider cybersecurity threats**](https://www.zdnet.com/article/half-of-businesses-cant-spot-these-signs-of-insider-cybersecurity-threats/)
* [**Best antivirus software for 2021**](https://www.cnet.com/tech/services-and-software/best-antivirus/)
* [**Supply chain attacks are getting worse, and you are not ready for them**](https://www.zdnet.com/article/supply-chain-attacks-are-getting-worse-and-you-are-not-ready-for-them/)
* [**Ransomware: Only half of organisations can effectively defend against attacks, warns report**](https://www.zdnet.com/article/ransomware-only-half-of-organisations-can-effectively-defend-against-attacks-warns-report/)





#### Tags:
[[cloud]] [[cybersecurity]] [[misconfigurations]] [[ZDNet]]
