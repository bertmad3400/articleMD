# Brute-Force Attacks Target Inboxes for Gift Card Data
### Cybercriminal enterprise is mass testing millions of usernames and passwords per day in a hunt for loyalty card data.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169187)
+ Date: September 3, 2021  7:31 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/03072406/loyalty-card.jpg)
Threat actors are compromising up to 100,000 inboxes daily in a campaign that targets gift card and customer-loyalty program data in hopes of reselling it or cashing in on freebies, a security researcher has found.


The actors behind the scam—outlined in a [post](https://krebsonsecurity.com/2021/09/gift-card-gang-extracts-cash-from-100k-inboxes-daily/) by Brian Krebs on Krebs on Security—have been “mass-testing millions of usernames and passwords against the world’s major email providers each day” for the past three years, according to the post.


“Some of the most successful and lucrative online scams employ a ‘low-and-slow’ approach — avoiding detection or interference from researchers and law enforcement agencies by stealing small bits of cash from many people over an extended period,” Krebs noted in the post.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Citing an anonymous source Krebs calls “Bill,” the group tries to authenticate between five to 10 million email username/password combos daily, with only about a .1 percent strike rate—which still means the actor “comes away with anywhere from 50,000 to 100,000 of working inbox credentials,” he wrote.


While one might think that “whoever is behind such a sprawling crime machine would use their access to [blast out spam](https://threatpost.com/spam-icedid-banking-trojan-variant/167250/), or conduct targeted [phishing attacks](https://threatpost.com/phishing-sharepoint-file-shares/168356/) against each victim’s contacts,” that’s not what’s happening, Krebs wrote.


“Based on interactions that Bill has had with several large email providers so far, this crime gang merely uses custom, automated scripts that periodically log in and search each inbox for digital items of value that can easily be resold,” he said.


Moreover, their primary focus seems to be to steal the “low-hanging fruit” of gift-card data, which amounts to “cash in your inbox,” Bill told Krebs.


“Whether it’s related to hotel or airline rewards or just Amazon gift cards, after they successfully log in to the account their scripts start pilfering inboxes looking for things that could be of value,” the researcher told Krebs, according to the post.


**Loyalty-Card Data: Growing Target for Hackers**
-------------------------------------------------


The campaign appears similar to [one identified in 2018](https://threatpost.com/rewards-points-targeted-by-teens-in-hack-of-500k-accounts/133194/), where two teens were arrested for using dictionary-attacks against millions of inboxes in an effort to crack them open and steal rewards points to make purchases and sell account credentials on illicit markets.


The exploitation of rewards-points programs is a growing criminal enterprise, especially those accounts associated with travel, according to a [Flashpoint 2018 analysis](https://threatpost.com/boutique-shops-offering-rewards-points-pop-up-on-the-dark-web/131636/). As [previously reported](https://threatpost.com/boutique-shops-offering-rewards-points-pop-up-on-the-dark-web/131636/), researchers have been tracking a number of small specialty shops in the Russian-language underground specializing in rewards-point abuse


Most of these stores are advertising access to the login credentials of customer accounts for travel and hospitality rewards programs. Flashpoint said there is a relatively high demand for these kinds of logins.


**Theft Methods**
-----------------


According to the Krebs report on the most recent incident, the anonymous source Bill observed that in about half of the cases of stolen credentials in the current campaign leveraged the email standard internet messaging access protocol (IMAP) to crack accounts open. IMAP is the email standard used by email software clients like Mozilla’s Thunderbird and Microsoft Outlook—checks the email credentials to see if they are legitimate.


The threat actors use automated systems to log in to each inbox and search for a variety of domains and other terms related to companies that maintain loyalty and points programs, issue gift cards and handle their fulfillment.


These reward programs are attractive because the accounts can be cleaned out and deposited onto a gift card number that can be resold quickly online for 80 percent of its value, Bill told Krebs, according to the post.


“These guys want that hard digital asset — the cash that is sitting there in your inbox,” Bill said. “You literally just pull cash out of peoples’ inboxes, and then you have all these secondary markets where you can sell this stuff.”


Threat actors even will use the credentials to seek new gift card benefits on behalf of victims, if that option is available, he said.


Victims of the scam were found on “nearly all major email networks,” with several large ISPs in Germany and France being targeted in particular, according to the post.


**Trends Influencing the Scam**
-------------------------------


While the scam may seem a bit strange, one security expert said it’s the natural culmination of several trends.


As security solutions and protections to combat payment fraud improve, cybercriminals have to find sneakier ways to make money from online scams, said Uriel Maimon, senior director of emerging technologies at web-app security provider [PerimeterX](http://www.perimeterx.com/).


Finding approaches that are several steps away from the initial point of exploitation also helps them cover their tracks and exploit trusted relationships between online commercial partners, he said.


“As IT ecosystems get more connected, people are using their social and email providers to log into other sites, and sites are ‘trusting’ email addresses as ‘safe,'” Maimon said in an email to Threatpost. “The fraud can be at the end of the funnel — that is, the exploitation happens elsewhere — in this case the email provider – but the damage is done on an unrelated site where the gift card is redeemed.”


The gift-card scam “underscores the fact that everything is connected in security,” and that organizations should think beyond merely monitoring for payment fraud to ensure online transactions are secure, he added.


**It’s time to evolve threat hunting into a pursuit of adversaries.** [**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **Threatpost and Cybersixgill for** [**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **and get a guided tour of the dark web and learn how to track threat actors before their next attack.** [**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with independent researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[post.]] [[said.]] [[inboxes]] [[inbox]] [[ThreatPost]]
