# McDonald’s Email Blast Includes Password to Monopoly Game Database
### Usernames, passwords for database sent in prize redemption emails. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169346)
+ Date: September 9, 2021  4:38 pm
+ Author: Becky Bracken


## Article:
![mcdonalds](https://media.threatpost.com/wp-content/uploads/sites/103/2019/11/19145328/mcdonalds.jpeg)
McDonald’s UK Monopoly VIP game kicked off at the end of August, and a recent round of emails sent to winners of the game’s various prizes included more than a coupon for free fries. The franchise accidentally inserted passwords for a McDonald’s server that hosted information tied to the UK Monopoly VIP game.


In the wrong hands, these credentials could have been abused to rip off players or cheat the game on a massive scale, according to experts. The gaff was spotted by researcher Troy Hunt, along with some tech-savvy winners who realized what they had.


McDonald’s said it quickly changed the server passwords when it the error was brought to its attention.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)Human error, warn cybersecurity experts, is nearly impossible to mitigate against, Mohit Tiwari, CEO of Symmetry Systems told Threatpost. He said the incident should serve as a public example to firms to identify and lock down large deposits of customer data and employ zero-trust solutions.


“Modern data-store security products bring zero-trust principles to data, ensuring that there is no one point of failure and that risk-based controls monitor every access to crown-jewel data,” Tiwari said.


**McDonald’s Monopoly Server Credential Email Blast**
-----------------------------------------------------


[McDonald’s Monopoly VIP promotion dates back to 1987](https://www.businessinsider.com/mcdonalds-monopoly-game-has-a-surprisingly-wild-history-2016-4) and is a long-standing tradition among customers who buy menu items, collect tickets with codes and enter those codes on the McDonald’s site to redeem cash and prizes.


This year’s McDonald’s Monopoly game in the U.K. runs through Oct. 19.


“Collect and complete property sets to win prizes! Once you’ve completed a set, visit the website address printed on the winning game piece and enter all the property codes to claim your prize,” the company’s [Monopoly VIP game site](https://monopoly.mcdonalds.co.uk/how-to-play) said. Make sure to keep your game pieces safe!”


But on Sept. 6, Australia-based Hunt Tweeted out a screencap of an email sent to a winner with the database passwords included in plain text.


Hunt captioned the image, “Never trust a clown to secure your connection strings.”



> 
> Never trust a clown to secure your connection strings 🤡 [pic.twitter.com/BWJ70TqNnw](https://t.co/BWJ70TqNnw)
> 
> 
> — Troy Hunt (@troyhunt) [September 6, 2021](https://twitter.com/troyhunt/status/1435015619045257222?ref_src=twsrc%5Etfw)
> 
> 



On TikTok another [McDonald’s Monopoly VIP winner](https://www.tiktok.com/@creatorsphereco/video/7004526492055014661) with the handle, “cretorsphereco” posted a video titled, “I don’t want these, Please answer emails McD” where he explained the credential leak and asked someone to let the fast [f]ood conglomerate know.


“Currently I have the keys to the kingdom,” he said. “And I don’t want them.”


Eventually, McDonald’s got the message because Hunt tweeted on Sept. 6 the [passwords had been changed](https://threatpost.com/5-password-security-rules-employees-ignoring/165686/).



> 
> They've been notified and passwords (well, the same password on both production and development / staging…) have already been changed. As to how you end up publishing *both* your connection strings into a mass email remains a mystery…
> 
> 
> — Troy Hunt (@troyhunt) [September 6, 2021](https://twitter.com/troyhunt/status/1435016373650935808?ref_src=twsrc%5Etfw)
> 
> 



“As to how you end up publishing *both*your connection strings into a mass email remains a mystery,” Hunt added.


McDonald’s hasn’t responded to Threatpost’s request for comment but acknowledged the leak in a Sept. 7 [statement to Bleeping Computer](https://www.bleepingcomputer.com/news/security/mcdonalds-leaks-password-for-monopoly-vip-database-to-winners/).


“Due to an administrative error, a small number of customers received details for a staging website by email.” McDonald’s told Bleeping Computer. “No personal details were compromised or shared with other parties. Those affected will be contacted to reassure them that this was a human error and that their information remains safe. We take data privacy very seriously and apologize for any undue concern this error has caused.”


**Human Error and Locking Down Data First**
-------------------------------------------


These types of human-related [security incidents](https://threatpost.com/incident-response-risk-preparedness/169211/) are a real threat to organizations of all sizes, according to Javvad Malik, security awareness advocate for KnowBe4 said.


“McDonalds stated that this leak was due to human error — which is a far more common occurrence than one may think,” Malik said. “It’s why it’s important that all organizations take steps to reduce the risk posed by human error. This includes having processes that involve checks so that no service goes live, or no changes are made without security assurance such as penetration testing.”


He adds all this helps generate an overall culture of security awareness.


Besides user training cybersecurity pros should first look to lock down large deposits of customer data, which are juicy targets for threat actors, Mohit Tiwari, CEO of Symmetry Systems told Threatpost.


“The knee-jerk response to such errors is to double down on application security — but perfectly securing hundreds of millions of lines of code is an impossible ask and doing surface level code scans (‘AppSec’) or asking for software bill of materials (SBOM) are extremely low-leverage activities,” Tiwari said. “In this case, protections around data can ensure that even if attackers know the database location/IP, username, and password, they are unable to use these — since data store access is confined to specific application-roles, IAM and cloud-network perimeters, etc.”


Data security tools can go deeper to monitor how applications access data, he added.


**It’s time to evolve threat hunting into a pursuit of adversaries.**[**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**Threatpost and Cybersixgill for**[**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**and get a guided tour of the dark web and learn how to track threat actors before their next attack.**[**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with independent researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[McDonald’s]] [[said.]] [[Sept.]] [[data,]] [[ThreatPost]]
