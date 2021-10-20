# VPN Exposes Data for 1M Users, Leading to Researcher Questioning
### Experts warn that virtual private networks are increasingly vulnerable to leaks and attack.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175612)
+ Date: October 20, 2021  1:53 pm
+ Author: Becky Bracken


## Article:
![Forcepoint vpn patch](https://media.threatpost.com/wp-content/uploads/sites/103/2019/09/20105955/forcepoint-vpn.jpeg)
Free virtual private network (VPN) service Quickfox, which provides access to Chinese websites from outside the country, exposed the personally identifiable information (PII) of more than a million users in just the latest high-profile VPN security failure.


The incident has some security practitioners questioning whether VPNs are an outdated technology.


Researchers at WizCase discovered [Quickfox misconfigured the VPN](https://www.wizcase.com/blog/quickfox-breach-report/) service’s Elasticsearch, Logstash and Kibana (ELK) stack security. The trio of programs helps manage searches, the report explained.


“Quickfox had set up access restrictions from Kibana but had not set up the same security measures for their Elasticsearch server,” according to the report. “This means that anyone with a browser and an internet connection could access Quickfox logs and extract sensitive information on Quickfox users.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Quickfox users in China, Indonesia, Japan, Kazakhstan and the U.S. were affected, the researchers found, adding that a total of 500 million records and 100GB of data were exposed.


The leaked data fell into one of two categories, the report said — PII like emails and phone numbers — but also information about software on the devices of around 300,000 Quickfox users.


“Data from the leak exposes the names of other software installed on the users’ devices, as well as the file location, install date, and version number. It’s unclear why the VPN was collecting this data, as it is unnecessary for its process, and it is not standard practice seen with other VPN services,” the researchers said in the report.


**VPNs Vulnerable, But Zero-Trust is A Hassle**
-----------------------------------------------


Since the pandemic, VPN use by organizations has exploded to help remote workers access the systems necessary to perform their jobs. Archie Agarwal, CEO of ThreatModeler, told Threatpost that his most recent search identified more than a million VPNs online in the U.S. alone.


But following spectacular VPN security failures like the [Colonial Pipeline breach,](https://threatpost.com/darkside-pwned-colonial-with-old-vpn-password/166743/) and the leak of thousands of [Fortinet VPN account credentials,](https://threatpost.com/thousands-of-fortinet-vpn-account-credentials-leaked/169348/) the U.S. government decided to weigh in and issue guidance on [hardening VPNs,](https://threatpost.com/vpns-nsa-cisa-guidance/175150/) including looking for a service with strong encryption and access management. A service that actively patches known vulnerabilities is also a plus.


Adopting a zero-trust security model is one solution to reliance on VPNs, but that’s are both expensive and hard to implement, Chris Morgan, analyst with Digital Shadows, told Threatpost.


“While zero-trust models may indeed be a more secure solution, its adoption will result in a greater logistical and financial cost,” Morgan said. “Many companies will likely find continued use of a VPN a more pragmatic short-term solution.”


But Agarwal argues VPNs need to go entirely.


“These are the doorways to private sensitive internal networks and are sitting there exposed to the world for any miscreant to try to break through,” Agarwal told Threatpost. “These represent the old perimeter paradigm and have failed to protect the inner castle over and again. If credentials are leaked or stolen, or new vulnerabilities discovered, the game is over and the castle falls. New zero-trust approaches being advocated by the United States government and NIST takes this public doorway offline and throws an invisible cloak over the entire network.”


**User Behavior a Huge Driver**
-------------------------------


Employee user behavior is another big consideration, Heather Paunet, senior vice president at Untangle, explained to Threatpost.


“Moving forward, we must take the human element into consideration,” Paunet said. “IT professionals are challenged with getting employees to effectively use the technology. If the VPN is too difficult to use, or slows down systems, the employee is likely to turn it off. The challenge for IT professionals is to find a VPN solution that is fast and reliable so that employees turn it on once and forget about it.”


Paunet added that VPN solutions are continuing to improve both in ease of use and security.


However, Timur Kovalev told Threatpost that it’s time for IT administrators to require employees to up their cybersecurity game, regardless of how annoying it is.


“To combat employees not always using VPN connections, and provide another layer of security, administrators looked to requiring 2FA [two-factor authentication] for more systems than they had before,” he said. “This means they can also choose whether to use 2FA for every login, which is more ‘annoying’ for employees yet more secure, or to use 2FA periodically, or after a device is trusted, which is easier for employees yet not quite as secure.”


Kovalev suggested to Threatpost the stakes are too high to ignore user behavior.


“With the recent ransomware attacks and high-profile breaches, such as SolarWinds, JBS, Pulse Secure and Kaseya VSA, IT administrators should be considering using the more secure options,” Kovalev added. “This will also involve training their employees how to navigate the less easy to use tools as well as explaining to employees why these measures are necessary and what they can do to not fall victim themselves to any type of security breach.”


Troublingly, Tyler Shields with JupiterOne predicts more VPN attacks to come.


“Discovery of exploits tend to cluster over time,” Shields told Threatpost. “Moving forward, I would expect additional network technology-based exploits to be disclosed as hackers continue to target those types of devices.”


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[VPN]] [[Quickfox]] [[VPNs]] [[Threatpost]] [[Threatpost.]] [[“This]] [[U.S.]] [[zero-trust]] [[said.]] [[Kovalev]] [[ThreatPost]]
