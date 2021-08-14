# WordPress Sites Abused in Aggah Spear-Phishing Campaign
### The Pakistan-linked threat group’s campaign uses compromised WordPress sites to deliver the Warzone RAT to manufacturing companies in Taiwan and South Korea.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168657)
+ Date: August 13, 2021  9:31 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2020/04/02113430/Phishing-Lure-Fishing-Lure.jpg)
Threat actors are using compromised WordPress websites to target manufacturers across Asia with a new spear-phishing campaign that delivers the Warzone RAT, a commodity infostealer available widely for purchase on criminal forums, researchers have found.


The threat group Aggah, believed to be affiliated with Pakistan and first identified in March 2019, is delivering the RAT in a campaign aimed at spreading malware to manufacturing companies in Taiwan and South Korea, according to new research from threat detection and response security firm [Anomali](https://www.anomali.com/).


The campaign, which began in early July, uses spoofed email addresses appearing to originate with legitimate customers of the manufacturers, signaling that it was the work of Aggah, researchers noted.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

“Spoofed business-to-business (B2B) email addresses against the targeted industry is activity consistent with Aggah,” Tara Gould and Rory Gould from Anomali Threat Research wrote in [a report](https://www.anomali.com/blog/aggah-using-compromised-websites-to-target-businesses-across-asia-including-taiwan-manufacturing-industry) on the campaign published Thursday.


Researchers from [Palo Alto Network’s Unit 42](https://unit42.paloaltonetworks.com/) [first discovered](https://unit42.paloaltonetworks.com/aggah-campaign-bit-ly-blogspot-and-pastebin-used-for-c2-in-large-scale-campaign/) Aggah in March 2019 in a campaign targeting entities in the United Arab Emirates that later was identified as a global phishing campaign designed to deliver RevengeRAT, researchers said.


The group, which typically aims to steal data from targets, was first thought to be associated with Gorgon Group: a Pakistani group known for targeting Western governments. This association has not been proven, but researchers tend to agree that the Urdu-speaking group originated in Pakistan, according to Anomali.


Among the targets of Aggah’s latest campaign were Fon-star International Technology, a Taiwan-based manufacturing company; FomoTech, a Taiwanese engineering company; and Hyundai Electric, a Korean power company.


Threat actors often target global manufacturers and other suppliers not only to target them, but also as a way to infiltrate some of their more high-profile customers. An example of this was seen in April when the now-defunct REvil gang successfully deployed ransomware against Quanta, a Taiwanese supplier of Apple Computer, just ahead of a big Apple product launch event.


REvil [stole files from Quanta](https://threatpost.com/revil-apple-ransomware-pay-off/165570/) that included blueprints for some of Apple’s new products. The operators threatened to release more and to spill the beans on new products in order to pressure the company to pay up ahead of Apple’s Spring Loaded event.


**Exploiting Compromised WordPress Sites**
------------------------------------------


The latest Aggah spear-phishing campaign begins with a custom email masquerading as “FoodHub.co.uk,” an online food delivery service based in the United Kingdom, researchers said.


The email body includes order and shipping information as well as an attached PowerPoint file named “Purchase order 4500061977,pdf.ppam” that contains obfuscated macros that use mshta.exe to execute JavaScript from a known compromised website, mail.hoteloscar.in/images/5[.]html, researchers explained.


“Hoteloscar.in is the legitimate website for a hotel in India that has been compromised to host malicious scripts,” they said. “Throughout this campaign, we observed legitimate websites being used to host the malicious scripts, most of which appeared to be WordPress sites, indicating the group may have exploited a WordPress vulnerability.”


The JavaScript uses anti-debugging techniques such as setInterval to detect the use of a debugger based on the execution time, researchers noted. This sends setInterval into an infinite loop if a debugger is detected. After the debugging checks, the script returned http://dlsc.af/wp-admin/buy/5[.]html, another compromised website for a food distributor based in Afghanistan.


Eventually, the Javascript uses PowerShell to load hex-encoded payloads, with the ultimate payload being the Warzone RAT, a C++-based malware available for purchase on the dark web, researchers said.


“Warzone is a commodity malware, with cracked versions hosted on GitHub,” they wrote. “The RAT reuses code from the Ave Maria stealer.” Capabilities of the Warzone RAT include privilege escalation, keylogging; remote shell, downloading and executing files, file manager, and persistence on the network, researchers noted.


“To bypass User Account Control (UAC), the Windows Defender path was added to a PowerShell command to exclude it,” they explained. “Privilege escalation in Warzone was carried out using sdclt.exe, a Windows backup utility in Windows 10.”


The Anomali team noted a number of tactics used in the campaign that are evidence of Aggah’s handiwork. These include the use of malicious documents and malicious PowerPoint files containing macros; obfuscated payloads in a PowerShell file, typically hex-encoded; use of scripts embedded in websites; themes of order and payment information; and the aforementioned use of spoofed B2B email addresses within the target industry.


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[WordPress]] [[Warzone]] [[said.]] [[noted.]] [[PowerShell]] [[Windows]] [[ThreatPost]]
