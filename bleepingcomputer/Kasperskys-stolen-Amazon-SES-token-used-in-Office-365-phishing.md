# Kaspersky's stolen Amazon SES token used in Office 365 phishing
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/kasperskys-stolen-amazon-ses-token-used-in-office-365-phishing/)
+ Date: November 1, 2021
+ Author: Sergiu Gatlan


## Article:
![Kaspersky's stolen Amazon SES token used in Office 365 phishing](https://www.bleepstatic.com/content/hl-images/2020/11/03/Office-365--phishing.jpg)


Kaspersky said today that a legitimate Amazon Simple Email Service (SES) token issued to a third-party contractor was recently used by threat actors behind a spear-phishing campaign targeting Office 365 users.


[Amazon SES](https://aws.amazon.com/ses/) is a scalable email service designed to allow developers to send emails from any app for various use cases, including marketing and mass email communications.


Kaspersky security experts linked the phishing attempts to multiple cybercriminals who used two phishing kits in this campaign, one known as *Iamtheboss* and another named *MIRCBOOT*.


No servers compromised
----------------------


"This access token was issued to a third party contractor during the testing of the website 2050.earth," Kaspersky explained in an advisory issued today, the first of its kind issued by the Russian cybersecurity firm in the last six years.


"The site is also hosted in Amazon infrastructure. Upon discovery of these phishing attacks, the SES token was immediately revoked.


"No server compromise, unauthorized database access or any other malicious activity was found at 2050.earth and associated services."


The threat actors did not attempt to impersonate Kaspersky and decided to camouflage their phishing messages as missed fax notifications, redirecting potential victims to phishing landing pages designed to harvest their Microsoft credentials.


However, they used an official Kaspersky email and sent the emails from Amazon Web Services infrastructure, which likely helped them reach their targets mailboxes by easily evading most Secure Email Gateway (SEGs) protections.


"The phishing e-mails are usually arriving in the form of 'Fax notifications' and lure users to fake websites collecting credentials for Microsoft online services," Kaspersky [added](https://support.kaspersky.com/general/vulnerability.aspx?el=12430#01112021_phishing).


"These emails have various sender addresses, including but not limited to noreply@sm.kaspersky.com."



![Kaspersky phishing attacks](https://www.bleepstatic.com/images/news/u/1109292/2021/Kaspersky_phishing_attacks.png)*Phishing email sample (Kaspersky)*
Users warned to be cautious
---------------------------


Kaspersky encourages users and those targeted in these spear-phishing attacks to be cautious and remain vigilant even when asked for their credentials or other sensitive information, even if the messages asking for such info seem to come from familiar brands or email addresses


You can find detailed information on checking the sender's identity using the email headers on [Kaspersky's blog](https://www.kaspersky.com/blog/analyzing-mail-header/42665/).


In related news, Microsoft also warned in August of a [highly evasive spear-phishing campaign targeting Office 365 customers](https://www.bleepingcomputer.com/news/microsoft/microsoft-evasive-office-365-phishing-campaign-active-since-july-2020/) in multiple waves since July 2020.


The company also said in March that attackers behind a large-scale phishing operation [stole roughly 400,000 OWA and Office 365 credentials](https://www.bleepingcomputer.com/news/security/microsoft-warns-of-phishing-attacks-bypassing-email-gateways/) since December 2020.


[Microsoft Defender ATP subscribers were also alerted in](https://www.bleepingcomputer.com/news/security/microsoft-warns-of-increasing-oauth-office-365-phishing-attacks/) late January of an increasing number of consent phishing (aka OAuth phishing) attacks targeting remote workers.




#### Tags:
[[Kaspersky]] [[phishing]] [[Microsoft]] [[spear-phishing]] [[emails]] [[Bleeping Computer]]
