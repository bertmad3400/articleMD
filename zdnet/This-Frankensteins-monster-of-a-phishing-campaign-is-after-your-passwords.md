# This Frankenstein's monster of a phishing campaign is after your passwords
### TodayZoo phishing campaign sends links to spoofed Microsoft 365 login pages.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/this-frankensteins-monster-of-a-phishing-campaign-is-after-your-passwords/)
+ Date: October 22, 2021
+ Author: Liam Tung


## Article:
Unknown

Microsoft has detailed an unusual phishing campaign aimed at stealing passwords that uses a phishing kit built using pieces of code copied from other hackers' work.

A "phishing kit" is the various software or services designed to facilitate phishing attacks. In this case, the kit has been called ZooToday by Microsoft after some text used by the kit. Microsoft also described it as a 'Franken-Phish' because it is made up of different elements, some available for sale through publicly accessible scam sellers or reused and repackaged by other kit resellers.


Microsoft said TodayZoo is using the WorkMail domain AwsApps[.]com to pump out email with links to phishing pages mimicking the Microsoft 365 login page.

**SEE:** [**Ransomware: Looking for weaknesses in your own network is key to stopping attacks**](https://www.zdnet.com/article/ransomware-looking-for-weaknesses-in-your-own-network-is-key-to-stopping-attacks/)

Microsoft says the attackers have been creating malicious AWS WorkMail accounts "at scale" but are just using randomly generated domain names instead of names that would represent a legitimate company. In other words, it's a crude phishing product likely made on a thin budget, but large enough to be noticeable. 

It caught Microsoft's attention because it impersonated Microsoft's brand and used a technique called "[zero-point font obfuscation](https://www.microsoft.com/security/blog/2021/08/18/trend-spotting-email-techniques-how-modern-phishing-emails-hide-in-plain-sight/)" – HTML text with a zero font size in an email – to dodge human detection. Microsoft detected an [uptick in zero-font attacks in July.](https://www.microsoft.com/security/blog/2021/08/18/trend-spotting-email-techniques-how-modern-phishing-emails-hide-in-plain-sight/)  

TodayZoo campaigns in April and May of this year typically impersonated Microsoft 365 login pages and a password-reset request. However. Microsoft found that campaigns in August used Xerox-branded fax and scanner notifications to dupe workers into giving up credentials. 






Microsoft's threat researchers have found that most of the phishing landing pages were hosted within cloud provider DigitalOcean. Those pages were identical to the Microsoft 365 signin page.

Another unusual trait was that after harvesting credentials, the stolen information was not forwarded to other email accounts but stored on the site itself. This behaviour was a trait of the TodayZoo phishing kit, which has previously focussed on phishing credentials from Zoom video-meeting accounts.

**SEE:** [**These stealthy hackers avoid Windows but target Linux as they look to steal phone data**](https://www.zdnet.com/article/these-hackers-dodge-windows-and-target-linux-as-they-look-to-steal-phone-data/)

But Microsoft researchers believe this phishing group is a single operation rather than a network of agents. 

"While many phishing kits are attributed to a wide variety of email campaign patterns and, conversely, many email campaign patterns are associated with many phishing kits, TodayZoo-based pages exclusively utilized the same email campaign patterns, and any of those subsequent email campaigns only surfaced TodayZoo kits. These lead us to believe that the actors behind this specific TodayZoo implementation are operating on their own," Microsoft said. 

Microsoft says it informed Amazon about the TodayZoo phishing campaign and that AWS "promptly took action". 





#### Tags:
[[Microsoft]] [[phishing]] [[TodayZoo]] [[ZDNet]]
