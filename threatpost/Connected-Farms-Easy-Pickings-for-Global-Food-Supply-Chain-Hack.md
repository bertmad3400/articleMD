# Connected Farms Easy Pickings for Global Food Supply-Chain Hack
### John Deere security bugs could allow cyberattackers to damage crops, surrounding property or even people; impact harvests; or destroy farmland for years.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168547)
+ Date: August 10, 2021  5:21 pm
+ Author: Becky Bracken


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/10171830/john-deere-1-e1628630327291.jpg)
A group of hackers made an unnerving DEF CON 29 presentation showing how the sprawling growth of digital and automated farming has left the world’s food supply chain vulnerable to cyberattack.


A video for [DEF CON 29 hacker conference](https://threatpost.com/punkspider-def-con-debate/168223/) this week put out by the group Sick Codes explained that modern farming is a high-tech, data-driven business like any other, trying to innovate its way to wider margins.


Farms are connected by Wi-Fi, 5G, radio sensors and more, and increasingly, every operation on the farm is being monitored and its data collected for analysis. Sick Code’s narrator, who goes by the handle Good Hackerman, used the John Deere 7450 Self-Propelled Forage Harvesters as a prime example.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/)


The monster tractor is fully automated, has GPS, has autonomous capabilities, and can even be controlled remotely by a John Deere customer service rep to help customers through issues.


Fears of a threat actor taking over the function of these machines to damage crops, surrounding property or even harm people, are real, Goodman said, adding that [denial-of-service (DoS) attacks](https://threatpost.com/auth-bypass-bug-routers-exploited/168491/) could have an enormous impact on harvests, and over-spraying of chemicals could destroy farmland for years.


All that needs to happen is for a hacker to upload “a firmware update that inserts an offset into the GPS locations used by the target,” the group said. “The target navigates itself into a highway, into a river, through a fence, over a cliff, or whatever. Target is destroyed.”


**Global Farm Data Unprotected**
--------------------------------


Locking down the world’s biggest farms’ data also might be worth a bit more consideration.


According to [John Deere](https://www.global-equipment.com/pub/media/wysiwyg/download/John%20Deere%207250-7350-7450-7550-7750-7950%20brochure%20USA.pdf), current tractors being sold are connected to a moisture sensor monitor called HarvestLab, and an overall monitoring software system called Harvest Monitor, which displays real-time productivity measurements on a monitor. There’s also HarvestDoc software, which reads crop data like yield and GPS location, which can later be sent to the Apex Farm Management Software for analysis.


There’s also something called AutoLOC, a function which takes the HarvestLab moisture readings and makes adjustments to how long the tractor cuts the crop for the best outcomes.


It’s easy to see how this seamless, constant data collection and analysis could be handy for farmers, however the security of holding all that data on the world’s modern farms in one single platform begs consideration, Hackerman points out.


Indeed, with some additional time, Sick Codes was able to breach the John Deere platform to make changes to supply networks, equipment reservations and even the contact details of those who received “demo units” from John Deere.


Sick Codes was also able to find a misconfiguration of John Deere’s Pega Chat Access Group Portal (CVE-2021-27653) that defaults to admin credentials, giving access over to anyone on the platform. From there the team was able to find additional credentials, the original signature password and even the encryption certificate.


“We could literally do whatever heck we wanted with anything we wanted on the John Deere operations center — period,” Goodman said. “That’s where we pretty much stopped because we pretty much had the whole organization.”


John Deere’s major competitor, Case, similarly has gaping security holes, the team added — including unprotected servers, personally identifiable information IP addresses and more.


**Sick Codes Grabs Ag Industry’s Attention**
--------------------------------------------


Because John Deere wasn’t immediately responsive to Sick Codes’reports, Goodman said they got the U.S. Cybersecurity Infrastructure and Security Agency (CISA) involved to help get mitigations in place. Case was just as unresponsive, the report added.


A John Deere spokeswoman told Threatpost that members of the company’s security team have been in contact with Sick Codes since April, adding that it has taken the vulnerabilities seriously, “and appreciated the opportunity to mitigate the issues brought to our attention.”


John Deere added that the security team, “verified that none of the vulnerabilities identified enabled access to customer accounts, agronomic data, dealer accounts or sensitive personal information – nor did they provide anyone the ability to remotely operate equipment. ”


To improve security at John Deere, the company said it has increased annual security investment by 750 percent and partnered with HackerOne for a bug-bounty program.


“We recognize this is a journey,” John Deere’s spokesperson told Threatpost. “We have been fiercely committed to growing our own security team and to work with third party security professionals to further test and improve our security systems. ”


The DEF CON 29 presentation explained that Sick Codes was assembled in consultation with a farmer and grandson of a John Deere board member, Willie Cade; a farmer and engineer out of Nebraska, Kevin Kenny; as well as Paul Roberts from Security Ledger who first mentioned to Goodman that [John Deere didn’t have any CVEs](https://securityledger.com/2021/08/def-con-security-holes-in-deere-case-ih-shine-spotlight-on-agriculture-cyber-risk/).


“Why did we start looking at agriculture?” Goodman said in the video. “Because nobody else was.”


**Worried about where the next attack is coming from? We’ve got your back.****[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)****for our upcoming live webinar,****[How to Think Like a Threat Actor](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)****, in partnership with Uptycs. Find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on Aug. 17 at 11AM EST for this****[LIVE](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)****discussion.**


 




#### Tags:
[[Deere]] [[world’s]] [[Deere’s]] [[“We]] [[ThreatPost]]
