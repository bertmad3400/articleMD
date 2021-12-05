# Convincing Microsoft phishing uses fake Office 365 spam alerts
### A persuasive and ongoing series of phishing attacks are using fake Office 365 notifications asking the recipients to review blocked spam messages, with the end goal of stealing their Microsoft credentials.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/convincing-microsoft-phishing-uses-fake-office-365-spam-alerts/
+ Date: 2021-12-05T11:07:37-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2020/11/03/Office-365--phishing.jpg)

![Convincing Microsoft phishing uses fake Office 365 spam alerts](https://www.bleepstatic.com/content/hl-images/2020/11/03/Office-365--phishing.jpg)


A persuasive and ongoing series of phishing attacks are using fake Office 365 notifications asking the recipients to review blocked spam messages, with the end goal of stealing their Microsoft credentials.


What makes these phishing emails especially convincing is the use of quarantine[at]messaging.microsoft.com to send them to potential targets and the display name matching the recipients' domains.


Additionally, the attackers have embedded the official Office 365 logo and included links to Microsoft's privacy statement and acceptable use policy at the end of the email.


Luckily, the phishing messages come with text formatting issues and out-of-place extra spaces that would allow spotting these emails' malicious nature on closer inspection.


"The email subject is 'Spam Notification: 1 New Messages,' alluding to the body of the email that informs the recipient that a spam message has been blocked and is being held in quarantine for them to review," cloud email security provider MailGuard who spotted this campaign [said](https://www.mailguard.com.au/blog/scammers-mimic-microsoft-with-spam-notification-phishing-email). 


"Details of the 'Prevented spam message' are provided, with scammers personalizing the subject heading as '[company domain] Adjustment: Transaction Expenses Q3 UPDATE' to create a sense of urgency and using a finance-related message."



![Office 365 spam alert phishing sample](https://www.bleepstatic.com/images/news/u/1109292/2021/Office%20365%20spam%20alert%20phishing%20sample.png)*Office 365 spam alert phishing sample (MailGuard)*
The targets are given 30 days to review the quarantined messages by going to Microsoft's Security and Compliance Center by clicking on an embedded link.


However, instead of reaching the Office 365 portal when clicking the 'Review' button, they are sent to a phishing landing page that will ask them to enter their Microsoft credentials to access the quarantined spam messages.


After entering their credentials in the malicious form displayed on the phishing page, their accounts' details get sent to attacker-controlled servers.


If they fall victim to these tricks, the victims' Microsoft credentials will later be used by the cybercriminals to take control of their accounts and gain access to all their information.


"Providing your Microsoft account details to cybercriminals means that they have unauthorised access to your sensitive data, such as contact information, calendars, email communications, and more," MailGuard added.


Appealing target for phishing attacks
-------------------------------------


Office 365 users are continuously targeted in phishing campaigns attempting to harvest their credentials and use them in fraudulent schemes.


Microsoft revealed in August that a [highly evasive spear-phishing campaign targeted Office 365 customers](https://www.bleepingcomputer.com/news/microsoft/microsoft-evasive-office-365-phishing-campaign-active-since-july-2020/) in multiple waves of attacks beginning with July 2020.


In March, the company also warned of a phishing operation that [stole roughly 400,000 OWA and Office 365 credentials](https://www.bleepingcomputer.com/news/security/microsoft-warns-of-phishing-attacks-bypassing-email-gateways/) since December 2020 and later expanded to abuse new legitimate services to circumvent secure email gateways (SEGs) protections.


In late January, Redmond further notified [Microsoft Defender ATP subscribers](https://www.bleepingcomputer.com/news/security/microsoft-warns-of-increasing-oauth-office-365-phishing-attacks/) of an increasing number of OAuth phishing (consent phishing) attacks targeting remote workers.


If successful, the impact of phishing attacks ranges from identity theft and fraud schemes including but not limited to Business Email Compromise (BEC) attacks.


For instance, since last year, the FBI has warned of BEC scammers abusing popular cloud email services, including Microsoft Office 365 and Google G Suite, in Private Industry Notifications issued in [March](https://www.bleepingcomputer.com/news/security/fbi-warns-of-bec-attacks-abusing-microsoft-office-365-google-g-suite/) and [April](https://www.bleepingcomputer.com/news/security/fbi-warns-again-of-bec-scammers-exploiting-cloud-email-services/) 2020.


The US Federal Trade Commission (FTC) has also revealed that [the number of identity theft reports doubled last year](https://www.bleepingcomputer.com/news/security/us-govt-number-of-identity-theft-reports-doubled-last-year/) compared to 2019, reaching a record of 1.4 million reports within a single year.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=CALENDAR]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Expand]]

#### Industry:
[[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Phishing]] [[Microsoft]] [[Bleeping Computer]]

