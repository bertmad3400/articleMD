# Microsoft uncovers giant Phishing-as-a-Service operation
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/microsoft-uncovers-giant-phishing-as-a-service-operation/)
+ Date: September 21, 2021
+ Author: Catalin Cimpanu


## Article:
![Microsoft uncovers giant Phishing-as-a-Service operation](https://therecord.media/wp-content/uploads/2021/09/BulletProofLink.jpg)

* BulletProofLink works as a Phishing-as-a-Service portal for the cybercrime underground.
* BulletProofLink operators provide phishing kits and out-of-the-box hosting for phishing campaigns.
* The BulletProofLink store provides "customers" with access to more than 120 phishing templates.


**Microsoft’s security team said today that it uncovered a massive operation that provides phishing services to cybercrime gangs using a hosting-like infrastructure that the OS maker likened to a Phishing-as-a-Service (PHaaS) model.**


Known as **BulletProofLink, BulletProftLink, or Anthrax**, the service is currently advertised on underground cybercrime forums.


The service is an evolution on “phishing kits,” which are collections of phishing pages and templates imitating the login forms of known companies.


![BulletProofLink-features](https://www-therecord.recfut.com/wp-content/uploads/2021/09/BulletProofLink-features.png)Image: Microsoft
BulletProofLink takes this to a whole new level by providing built-in hosting and email-sending services as well.


Customers register on the BulletProofLink portal by paying a fee of $800, and the BulletProofLink operators handle everything else for them. These services include setting up a web page to host the phishing site, installing the phishing template itself, configuring domain (URLs) for the phishing sites, sending the actual phishing emails to desired victims, collecting credentials from attacks, and then delivering the stolen logins to “paying customers” at the end of the week.


If criminal groups want to vary their phishing templates, the BulletProofLink gang also runs a separate store where threat actors can buy new templates to use in their attacks, with prices ranging from $80 to $100 per each new template.


Roughly 120 different phishing templates are available on the BulletProofLink store, as seen by *The Record* today. In addition, the site also hosts tutorials to help customers use the service.


![BulletProofLink-shop](https://www-therecord.recfut.com/wp-content/uploads/2021/09/BulletProofLink-shop-1024x787.png)Image: The Record
But Microsoft researchers said they also found that the service has also been stealing from its own customers by keeping copies of all the collected credentials, which the group is believed to monetize at a later point by selling the credentials on underground markets.


![BulletProofLink-scheme](https://www-therecord.recfut.com/wp-content/uploads/2021/09/BulletProofLink-scheme.png)Image: Microsoft
Microsoft described the entire operation as technically advanced, with the group often using hacked sites to host its phishing pages.


In some scenarios, the BulletProofLink gang was observed compromising the hacked sites’ DNS records in order to generate subdomains on trusted sites to host phishing pages.


“In researching phishing attacks, we came across a campaign that used a rather high volume of newly created and unique subdomains—over 300,000 in a single run,” Microsoft said today, putting the huge scale of the BulletProofLink PHaaS in perspective.


Additional insights, indicators of compromise, and technical details into BulletProofLink are available in [Microsoft’s report](https://www.microsoft.com/security/blog/2021/09/21/catching-the-big-fish-analyzing-a-large-scale-phishing-as-a-service-operation/) and in a [blog post](https://osint.fans/bulletproftlink-phishing-service-p1) from OSINT Fans from October 2020, when the service was first spotted and linked to a threat actor possibly operating out of Ukraine.





#### Tags:
[[phishing]] [[BulletProofLink]] [[Microsoft]] [[cybercrime]] [[Image:]] [[attacks,]] [[The Record]]
