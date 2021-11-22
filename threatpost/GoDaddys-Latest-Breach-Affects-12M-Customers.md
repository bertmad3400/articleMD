# GoDaddy’s Latest Breach Affects 1.2M Customers
### The kingpin domain registrar has logged its fifth cyber-incident since 2018, after an attacker with a compromised password stole email addresses, SSH keys and database logins.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176530)
+ Date: November 22, 2021  5:03 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/22164808/GoDaddy-e1637617704303.jpg)
Web-hosting giant GoDaddy has confirmed another data breach, this time affecting at least 1.2 million of its customers.


On Monday, the world’s largest domain registrar said in a public filing to the SEC that an “unauthorized third party” managed to infiltrate its systems on Sept. 6 – and that the person(s) had continued access for almost two and a half months before GoDaddy noticed the breach on Nov. 17.


“We identified suspicious activity in our Managed WordPress hosting environment and immediately began an investigation with the help of an IT forensics firm and contacted law enforcement,” Demetrius Comes, GoDaddy CISO, said in [the website notice](https://www.sec.gov/Archives/edgar/data/1609711/000160971121000122/gddyblogpostnov222021.htm).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Specifically, the attackers compromised GoDaddy’s Managed WordPress hosting environment – a site-building service that allows companies and individuals to use the popular WordPress content management system (CMS) in a hosted environment, without having to manage and update it themselves.


“Using a compromised password, an unauthorized third party accessed the provisioning system in our legacy code base for Managed WordPress,” according to Comes.


The information the lurking cybercriminal(s) was/were able to purloin is a mixed bag. The Scottsdale, Ariz.-based firm said that it included:


It didn’t attach numbers as to how many customers are affected by the database log-in or certificate compromises.


“Our investigation is ongoing, and we are contacting all impacted customers directly with specific details,” Comes concluded. “We will learn from this incident and are already taking steps to strengthen our provisioning system with additional layers of protection.”


Questions also remain as to how the account itself was protected: Was a strong password in use, or multi-factor authentication (MFA)?


“The key question is, ‘was multifactor in use?’ With this breach being caused by a compromised credential, I wouldn’t imagine the login was protected by multi-factor authentication, which is an element that could have caused this breach,” Randy Watkins, CTO at Critical Start, said via email. “Moving forward, key and password management is crucial. Applying least-privilege where applicable can lessen the impact of a compromised credential, but it’s still best to protect every login with MFA and monitor service accounts that don’t support MFA.”


**GoDaddy Customers in Cybercriminals’ Sights**
-----------------------------------------------


When it comes to the ramifications for those affected, follow-on phishing is the obvious thing to watch out for, as flagged by GoDaddy in its announcement. But other issues should also be considered, researchers said.


“This breach could mean a few things for users,” said Watkins. “There is a chance that keys or credentials could be used to gain access or impersonate customer sites. Either of these scenarios could lead to a compromise of those organizations’ [customers’] data as well. While this breach will just be an inconvenience for most, others may have serious brand damage from impersonated sites or an actual breach. ”


According to Murali Palanisamy, chief solutions officer for AppViewX, compromised SSL private keys and certificates could also allow hackers to hijack a domain name and use it to extort ransom for its return.


“They can also redirect users to what appears as an identical website and deploy malware or collect user credentials and credit-card information and much more,” he said via email. “All of these threats are extinction-level events.”


He added that while GoDaddy is working to update the SSL certificates, it will take time to accomplish this, so customers might want to take matters into their own hands.


“To mitigate current vulnerabilities, customers of GoDaddy need to check that the certificates are updated and change the passwords for sFTP access to new and unique numbers, letters and symbols,” he said. “I’d also recommend incorporating a cryptographic agility capability, which will enable a quick rollover of certifications and keys.”


Long-term, users could also incorporate short-lived automated certificates.


“This way, if the keys are compromised, they are not used by attackers, and the window of opportunity for such sophisticated attacks are reduced,” he said. “Customers of GoDaddy should monitor for unusual activity and report any red flags to the government/FTC as soon as possible.”


**GoDaddy’s Cyber-Incident History**
------------------------------------


This is only the company’s latest data incident. Last year, GoDaddy made headlines with three separate incidents.


The first came to light in March 2020, when [an attacker phished an employee](https://krebsonsecurity.com/2020/03/phish-of-godaddy-employee-jeopardized-escrow-com-among-others/) to gain access to GoDaddy’s internal support system and went on to change at least five customers’ domain name entries.


Then, in May 2020, the company [said that](https://threatpost.com/godaddy-hack-breaches-hosting-account-credentials/155475/) cybercriminals had stolen customers’ web-hosting account credentials (SSH usernames and passwords), after having access to its systems from October 2019 to April 2020. In that incident, 28,000 of the company’s 19 million active users were affected by the attack.


And last November, a social-engineering “vishing” attack on GoDaddy employees [temporarily handed over](https://threatpost.com/godaddy-employees-tricked-compromise-cryptocurrency/161520/) control of cryptocurrency service sites NiceHash and Liquid to fraudsters, exposing personal information of users.


Before that, GoDaddy also exposed high-level configuration information for tens of thousands of systems (and competitively sensitive pricing options for running those systems) in Amazon AWS [back in 2018](https://threatpost.com/godaddy-leaks-map-of-the-internet-via-amazon-s3-cloud-bucket-misconfig/135009/), thanks to a cloud storage misconfiguration.


“Due to its history with cyber-incidents, GoDaddy has become an easy target,” said Nick Tausek, security solutions architect at Swimlane. “It operates 35,000 servers hosting more than five million websites, with millions of people relying on its services for the day-to-day operations of their businesses and hobbies. Because of the level of user dependency, repercussions can be severe when a situation like this presents itself.”


Threatpost reached out to GoDaddy for a statement, but the company did not immediately return a request for comment.


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** ***[REGISTER TODAY](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)*** ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This [LIVE, interactive Threatpost Town Hall](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article), sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***




#### Tags:
[[GoDaddy]] [[WordPress]] [[GoDaddy’s]] [[said.]] [[Threatpost]] [[ThreatPost]]
