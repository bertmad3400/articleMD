# Large-Scale Phishing-as-a-Service Operation Exposed
### Discovery of BulletProofLink—which provides phishing kits, email templates, hosting and other tools—sheds light on how wannabe cybercriminals can get into the business.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=174932)
+ Date: September 23, 2021  7:10 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/23070332/phishing-farm.jpg)
Microsoft uncovered a large-scale, well-organization and sophisticated phishing-as-a-service (PhaaS) operation. The turnkey platform allows users to customize campaigns and develop their own phishing ploys so they can then use the PhaaS platform to help with phishing kits, email templates and hosting services needed to launch attacks.


Microsoft researchers discovered the operation, marketed by criminals as BulletProofLink, when they found a high volume of newly created and unique subdomains—more than 300,000 in a single run, according to a [post](https://www.microsoft.com/security/blog/2021/09/21/catching-the-big-fish-analyzing-a-large-scale-phishing-as-a-service-operation/) published by the Microsoft 365 Defender Threat Intelligence Team.


“This investigation led us down a rabbit hole as we unearthed one of the operations that enabled the campaign,” researchers wrote.  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


With more than 100 available phishing templates that mimic known brands and services—including Microsoft itself–the BulletProofLink operation is responsible for many of the phishing campaigns that impact enterprises today, they said.


Phishing is a common way for cybercriminals to dupe people through [socially-engineered emails](https://threatpost.com/trump-biden-campaign-apt-phishing-emails/156319/) into giving up their credentials to online accounts that can store sensitive data. Phishers use these emails—which sometimes fool people by impersonating a trusted company, [application](https://threatpost.com/phishing-sharepoint-file-shares/168356/) or [institution](https://threatpost.com/attackers-impersonate-dot-phishing-scam/169484/)–to direct people to specially crafted phishing sites so they can enter credentials, thinking they are doing so for a legitimate reason


Phishing is often a gateway drug into other criminal activity; phishers sell credentials obtained through campaigns on the dark web, and they can be used by ransomware gangs as an entry point into networks to deliver [ransomware attacks](https://threatpost.com/phishing-costs-quadrupled/168716/), among other nefarious activity.


**Full-Scale Phishing Facilitator**
-----------------------------------


BulletProofLink—also known as BulletProftLink or Anthrax by its operators in various websites, ads and other promotional materials–provides a starting point for people without significant resources to get into the phishing business.


The group has been active since 2018 and maintains multiple sites under aliases. The group leverages services such as YouTube and Vimeo offering instructional videos, advertisements and promotional materials. It is known to hawk their wares on a plethora of underground forums, researchers said.


While previously, criminals who wanted to launch these attacks had to build phishing emails and brand-impersonating websites on their own, “the phishing landscape has evolved its own service-based economy,” researchers said. Now attackers can just purchase all the resources and other infrastructure they need to launch phishing attacks without investing a lot of time or effort, researchers said.


There are two key offerings that are available to criminals who want to get into the phishing business: phish kits and phishing-as-a-service.


The first are packaged files sold on a one-time basis that come with ready-to-use email phishing templates designed to evade detection and are often accompanied by a portal with which to access them, researchers explained. The kits—an example of which is the MIRCBOOT phish kit–allow people to set up the websites and purchase the domain names they need to launch phishing campaigns.


The second offering is similar to ransomware-as-a-service (RaaS), which also is a popular way cybercriminals can get into the game without making their own significant investment, researchers said.


PhaaS—the bread and butter of BulletProofLink’s operation–follows the software-as-a-service model, they said. Attackers pay an operator to develop turnkey phishing campaigns that include everything from false sign-in page development to website hosting to credential parsing and redistribution.


**Diving Deeper into PhaaS**
----------------------------


Researchers took a deeper dive into BulletProofLink’s PhaaS operation to uncover how the group has created a flourishing network of phishers.


Like any service provider, the group explains on an “About Us” page on its site the services it provides, including the sale of a “unique scam page” as well as a monthly hosted subscription service to set up a customer’s phishing operation. In fact, the group hosts multiple sites to serve its customers, including an online store where customers can register, sign in and advertise their hosted service for monthly subscriptions.


The monthly service costs as much as $800, while other services cost about $50 dollars for a one-time hosting link, researchers found, with Bitcoin being a common payment method on the BulletProofLink site. The organization even uses the typical service-provider tactic of offering a 10 percent welcome discount on customers’ orders when they subscribe to its newsletter.


An interesting point about the PhaaS working model BulletProofLink uses is that it follows the RaaS model’s method of double extortion—or in this case, “double theft,” as researchers describe.


In ransomware, this method generally involves attackers exfiltrating and posting data publicly in addition to encrypting them on compromised devices to put pressure on organizations to pay the ransom, they noted.


A similar workflow also is present in the economy of stolen credentials in BulletProofLink’s PhaaS model, researchers wrote. The group includes a secondary location in its phishing kit for credentials to be sent once acquired, they observed.


“In cases where the attackers using the service received credentials and logs at the end of a week instead of conducting campaigns themselves, the PhaaS operator maintained control of all credentials they resell,” researchers wrote.


In both RaaS and PhaaS, then, the operators supplying resources to facilitate attacks maximize monetization by assuring stolen data, access, and credentials are put to use in as many ways as possible. This also ensures that stolen credentials are likely to end up in the undergound economy, researchers observed.


***Rule #1 of Linux Security:****No cybersecurity solution is viable if you don’t have the basics down.* [**JOIN**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the [**4 Golden Rules of Linux Security**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar). Your top takeaway will be a Linux roadmap to getting the basics right! [**REGISTER NOW**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.




#### Tags:
[[phishing]] [[PhaaS]] [[said.]] [[Linux]] [[Microsoft]] [[wrote.]] [[BulletProofLink]] [[Phishing]] [[BulletProofLink’s]] [[ThreatPost]]
