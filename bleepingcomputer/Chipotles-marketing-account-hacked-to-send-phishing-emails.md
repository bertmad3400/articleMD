# Chipotle’s marketing account hacked to send phishing emails
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/chipotle-s-marketing-account-hacked-to-send-phishing-emails/)
+ Date: July 29, 2021
+ Author: Ionut Ilascu


## Article:
![Hackers use Chipotle’s mail service to send out phishing messages](https://www.bleepstatic.com/content/hl-images/2020/11/27/Phishing.jpg)


Hackers have compromised an email marketing account belonging to the Chipotle food chain and used it to send out phishing emails, luring recipients to malicious links.


Most of the messages directed users to credential-harvesting sites impersonating services from a financial business and Microsoft. A very small number had malware attachments.


### Hacked Mailgun account


The campaign sent out in three days at least 120 malicious emails from a hacked Mailgun account used by Chipotle for email marketing purposes [mail.chipotle.com].


Using a legitimate email address increases the chances of a successful delivery, especially when there are automated security solutions in place that check if email addresses pass the DomainKeys Identified Mail (DKIM) and Sender Policy Framework authentication methods.


Almost all malicious emails impersonated Microsoft with the purpose of collecting login information. Email security company Inky says in a blog post today that they caught 105 such emails in this three-day campaign.



“Almost everyone has a Microsoft account, and logins there can lead to all kinds of interesting data, including other logins, trade secrets, financial details, and other intelligence” - [Inky](https://www.inky.com/blog/chipotle-mail-service-hack-delivers-a-steaming-plate-of-evil-to-email-recipients)



The emails appeared to come from “Microsoft 365 Message center” and alerted the recipient of emails that could not be delivered “due to low email storage” in the cloud.


Clicking on the button that allegedly “released messages to inbox” would take the user to a fake Microsoft login page that harvested the sensitive information.


![Chipotle-delivered phishing email impersonating Microsoft 365](https://www.bleepstatic.com/images/news/u/1100723/2021/microsoft_phish_email_Inky.jpg)


The hackers also impersonated the United Services Automobile Association ([USAA](https://www.usaa.com/)), a Fortune 500 diversified financial services group of companies, enticing the user to navigate to a well-crafted phishing site.


![USAA phishing email delivered from hacked Chipotle address](https://www.bleepstatic.com/images/news/u/1100723/2021/usaa_phish_site-Inky.png)


The rest of the fake emails, two of them, posed as voicemail notifications and carried malware attachments. While Inky does not say what type of threat was delivered, business email compromise (BEC) fraudsters often use phishing to deliver information stealers to collect information helpful for the social engineering part of the scam.


Hacking an email marketing platform for phishing attacks has been described earlier this year as an entry vector [used by Nobelium](https://www.bleepingcomputer.com/news/security/microsoft-russian-svr-hackers-target-govt-agencies-from-24-countries/), the state-sponsored threat actor blamed for the Solarwinds supply-chain attack.


However, Inky says that they found no evidence indicating that the recent email phishing campaign is the work of the same group of hackers.




#### Tags:
[[phishing]] [[emails]] [[Microsoft]] [[Bleeping Computer]]
