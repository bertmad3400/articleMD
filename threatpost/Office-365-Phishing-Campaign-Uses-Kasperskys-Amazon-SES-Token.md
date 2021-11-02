# Office 365 Phishing Campaign Uses Kaspersky’s Amazon SES Token
### It’s a legitimate access token, stolen from a third-party contractor, that lets the attackers send phishing emails from kaspersky.com email addresses. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175915)
+ Date: November 1, 2021  8:29 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/21134528/phishing-1-e1632246346826.jpg)
A surge in spearphishing emails designed to steal Office 365 credentials were rigged to look like they came from a Kaspersky email address.


In spite of coming from sender addresses such as noreply@sm.kaspersky.com, nobody at Kaspersky sent the phishing emails, the security company said in an [advisory](https://support.kaspersky.com/general/vulnerability.aspx?el=12430#01112021_phishing) issued on Monday. Rather, the emails were sent with Kasperskyi’s legitimate, albeit stolen, Amazon Simple Email Service (SES) token.


[Amazon SES](https://aws.amazon.com/ses/) is a scalable email service that lets developers send mail from any app, including in marketing or mass email communications.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“This access token was issued to a third party contractor during the testing of the website 2050.earth,” according to Kaspersky’s advisory. The [2050.earth](https://2050.earth/) site is a Kaspersky project that features an interactive map illustrating what futurologists and others think will happen to the planet in coming decades.


Kaspersky said that the site is hosted on Amazon infrastructure.


After spotting what it called “a huge uptick” in recent Office 365 credential spearphishing attacks – attacks that may be coming from multiple threat actors – the SES token was immediately revoked, Kaspersky said.


The theft caused no damage, according to the advisory: “No server compromise, unauthorized database access or any other malicious activity was found at 2050.earth and associated services,” it said.


The Lure: Phony Faxes
---------------------


Phishing is a common way for cybercriminals to dupe people through [socially engineered emails](https://threatpost.com/trump-biden-campaign-apt-phishing-emails/156319/) into giving up their credentials to online accounts that can store sensitive data. Phishers use these emails – which sometimes fool people by impersonating a trusted company (like Kaspersky), [application](https://threatpost.com/phishing-sharepoint-file-shares/168356/) or [institution](https://threatpost.com/attackers-impersonate-dot-phishing-scam/169484/) – to direct people to specially crafted phishing sites so they can enter credentials, thinking they’re doing so for a legitimate reason.


Office 365 credentials are a common target for phishing attacks. In March, for example, a [phishing scam targeted executives](https://threatpost.com/phishing-as-a-service-exposed/174932/) in the insurance and financial services industries with the aim of harvesting their Microsoft 365 credentials and launching [business email compromise](https://threatpost.com/cybercriminal-enterprise-ringleaders-stole-55m-via-covid-19-fraud-romance-scams/164086/) (BEC) attacks.


The cybercrooks who came up with the Kaspersky-themed scheme didn’t try to impersonate Kaspersky employees. Instead, the phishing emails typically purport to be “fax notifications” that lure targets to fake websites that harvest credentials for Microsoft’s online services. It’s hardly the first time the old “fax alert” song and dance has been used: In December 2020, Office 365 credentials were likewise [under attack](https://threatpost.com/microsoft-office-365-credentials-attack-fax/162232/) by a campaign that used the same email con.


The Kaspersky phishing emails were sent from various supposed Kaspersky addresses, and they’re coming from multiple websites, including Amazon Web Services infrastructure.


Kaspersky provided the sample phishing email below.


Analysis showed that the phishing campaigns are relying on a phishing kit that Kaspersky researchers have named “Iamtheboss,” used in conjunction with another phishing kit known as “MIRCBOOT.”


MIRCBOOT Served Up By Turnkey Phishing Platform BulletProofLink
---------------------------------------------------------------


If the name MIRCBOOT sounds familiar, it might be because it was one of the phishing kits that Microsoft recently found when it uncovered a large-scale, well-organized, sophisticated phishing-as-a-service (PhaaS) operation that the criminals called [BulletProofLink](https://threatpost.com/phishing-as-a-service-exposed/174932/).


BulletProofLink, a turnkey platform, provides phishing kits, email templates, hosting and other tools that let users customize campaigns and develop their own phishing ploys. They then use the PhaaS platform to help with phishing kits, email templates and the hosting services needed to launch attacks.


MIRCBOOT and the other phishing kits available on BulletProofLink allow cybercriminal wannabes to set up the websites and purchase the domain names they need to launch phishing campaigns, pretending to be, say, employees of a security firm, as in this case.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[phishing]] [[Kaspersky]] [[emails]] [[attacks.]] [[MIRCBOOT]] [[ThreatPost]]
