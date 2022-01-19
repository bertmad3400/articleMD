# Cloned Dept. of Labor Site Hawks Fake Government Contracts
### A well-crafted but fake government procurement portal offers the opportunity to submit a bid for lucrative government projects — but harvests credentials instead.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177734
+ Date: 2022-01-19T11:00:12+00:00
+ Author: Becky Bracken


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2020/01/23124846/spear-phishing-.jpg)

A new phishing campaign is targeting aspiring government vendors with an invitation to bid on various fake federal projects with the U.S. Department of Labor.


Emails branded to look like legitimate communications from the DoL contain malicious links that, rather than leading to a government procurement portal, harvest the credentials of anyone who attempts to login, according to a new report from threat researchers at INKY.


“In this campaign, the majority of phishing attempts had sender email addresses spoofed to look as if they came from no-reply@dol[.]gov, which is the real DoL site,” the INKY team reported in a [Wednesday report](https://www.inky.com/blog/fresh-phish-phishers-lure-victims-with-fake-invites-to-bid-on-nonexistent-federal-projects). “A small subset were spoofed to look as if they came from no-reply@dol[.]com, which is, of course, not the real DoL domain.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The remainder were [sent by phishers](https://threatpost.com/phishers-ea-gamers/177575/) from lookalikes dol-gov[.]com, dol-gov[.]us and bids-dolgov[.]us.


The [phishing lure email](https://threatpost.com/gootloader-accounting-law-firms/177629/) texts claim that the DoL is soliciting bids for “ongoing government projects,” and included a .PDF file attached with government branding. The threat researchers said the efforts were “well-crafted.”


“Click on the button below to access our website to bid,” the phishing email instructs. Once clicked, the link takes victims to various domains impersonating the DoL.


**Copy & Paste Spoof of DoL Site**
----------------------------------


The malicious site was a copy-and-paste of the website styling code (both HTML and CSS) from the actual Department of Labor site, with the addition of a bright red link directing victims to a credential harvester asking for the login details of a Microsoft or other business account, the report added.


“When an INKY engineer made a first attempt at entering fake credentials, the site displayed a fake incorrect credentials error,” the researchers wrote. “But behind the scenes, those fake credentials had already been harvested (and either stored on the malicious site or emailed to the phisher).”


Following another attempt to sign in with fake login details, the researchers were redirected to the real Department of Labor site, they reported.


“This nuanced touch, borrowed from con artistry that well predates the digital era, is designed to confuse the victim and delay the moment when they realize that they were taken,” the researchers said.


Most of the emails were sent from compromised servers. But some of the lures were sent from domains created by the attackers to trick users into thinking they were from the Department of Labor, they added.


To avoid compromise, INKY suggests security teams remind end users that legitimate government domains end in .gov or .mil and that official federal procurement departments do not typically send out cold solicitations for bids.


In addition, users could probably use a reminder that its unusual to be asked for email credentials to view a document on an unrelated network, the INKY team recommended.


“For message administrators, it ought to be clear that SMTP servers should not be configured to accept and forward emails from non-local IP addresses to non-local mailboxes by unauthenticated and unauthorized users,” the report added.


***Password******Reset:***[**On-Demand Event**](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)***:****Fortify 2022 with a password-security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the new password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken.*[**Register & stream this FREE session today**](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/) *– sponsored by Specops Software.*





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=RTM]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Phishing]] [[ThreatPost]]

