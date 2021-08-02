# Chipotle Emails Serve Up Phishing Lures
### Mass email distribution service compromise mirrors earlier Nobelium attacks. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168279)
+ Date: August 2, 2021  3:15 pm
+ Author: Becky Bracken


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/02150734/Chipotle.jpg)
Customers who signed up for emails from fast-food chain Chipotle Mexican Grill were recently faced with bigger challenges than queso versus sour cream. A breach of the restaurant’s email marketing service last month lead to customers being served phishing lures and malicious links that redirected to credential harvesting sites.


Researchers at Inky reported that Chipotle’s [email vendor Mailgun was breached](https://www.inky.com/blog/chipotle-mail-service-hack-delivers-a-steaming-plate-of-evil-to-email-recipients), allowing threat actors to commandeer the company’s email marketing efforts.


Mailgun has not responded to Threatpost’s request for comment.



The Inky report, posted Friday, found 121 phishing emails sent from the compromised Chipotle Mailgun account sent between July 13 and July 16. Those attacks included two vishing attacks (using malicious voicemail message attachments), 14 impersonated USAA bank to harvest financial data and the remaining 105 emails attempted to redirect users to a spoofed Microsoft site that attempted to steal credentials.


**TTPs Eerily Similar to Nobelium**
-----------------------------------


The attacks leveraging Chipotle’s breached Mailgun account are similar to Nobelium’s attack on email marketing service in May 2021. That’s when the group [breached Constant Contact](https://threatpost.com/solarwinds-nobelium-phishing-attack-usaid/166531/)‘s systems and took over the account of USAID, an international development agency.


“Inky has no evidence to suggest the same actors are involved in these attacks, it appears to be a case of copying a successful attack vector used by Nobelium,” the report said. “Inky continues to investigate these attacks.”


Nobelium has been credited with the SolarWinds attack on the U.S. government.


By late June Nobelium was reported by the Microsoft Threat Intelligence Center to be behind [brute force and password-spray attacks](https://threatpost.com/russian-attackers-breach-microsoft/167340/) on Microsoft corporate networks as part of ongoing efforts to gain a foothold in U.S. tech and government agencies.


In fact, 45 percent of all phishing attacks in 2020 were aimed at swiping Microsoft credentials, according to a report released early this year by Cofense.


Microsoft continues to be a prime target for phishing attacks because the credentials are highly valuable, Inky explained.


“Almost everyone has a Microsoft account, and logins there can lead to all kinds of interesting data, including other logins, trade secrets, financial details, and other intelligence,” Inky said. “Thus, it is not surprising that INKY identified 105 phishing emails during that three-day stretch all of which had mail.company[.]com links that redirected the recipient to a malicious Microsoft credential-harvesting site. ”


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[Microsoft]] [[phishing]] [[emails]] [[Mailgun]] [[ThreatPost]]
