# Threat Actors Weaponize Telegram Bots to Compromise PayPal Accounts
### A campaign is stealing one-time password tokens to gain access to PayPal, Apple Pay and Google Pay, among others.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175099)
+ Date: September 29, 2021  9:55 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2018/03/20144222/Telegram_Messagees.jpg)
Cybercriminals are using Telegram bots to steal one-time password tokens (OTPs) and defraud people through banks and online payment systems, including PayPal, Apple Pay and Google Pay, new research has found.


Researchers from Intel 471 discovered the campaign, which has been operational since June, they said in a report published Wednesday.


“Two-factor authentication is one of the easiest ways for people to protect any online account,” researchers noted in [the post](https://intel471.com/blog/otp-password-bots-telegram). “So, of course criminals are trying to circumvent that protection.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

Threat actors are using Telegram bots and channels and a range of tactics to gain account information, including calling victims, and impersonating banks and legitimate services, researchers said.


Through social engineering, threat actors also deceive people into giving them an OTP or other verification code via a mobile device, which the crooks then use to defraud accounts of money, they said.


“The ease by which attackers can use these bots can not be understated,” they wrote in the report. “While there’s some programming ability needed to create the bots, a bot user only needs to spend money to access the bot, obtain a phone number for a target, and then click a few buttons.”


Indeed, Telegram bots have become a popular tool for cybercriminals, which have used them in various ways as part of user scams. A similar campaign discovered in January, dubbed [Classiscam](https://threatpost.com/telegram-bots-classiscam-scam/163061/), where bots were sold as-a-service by Russian-speaking cybercriminals for the purpose of stealing money and payment data from European victims. Other threat actors have been found using Telegram bots in a rather unique way as [command-and-control for spyware](https://threatpost.com/masad-spyware-telegram-bots/148759/).


In this case, Intel 471 researchers observed and analyzed the campaign’s activity in regard to three bots—dubbed SMSRanger, BloodOTPbot and SMS Buster.


**Easy-to-Use Bot as-a-Service**
--------------------------------


Researchers characterized SMSRanger as “easy to use,” according to the post. Actors pay to access the bot and then can use it by entering commands, in a similar fashion to how bots are used on the widely used workforce collaboration platform Slack, they explained.


“A simple slash command allows a user to enable various ‘modes’ — scripts aimed as various services — that can target specific banks, as well as PayPal, Apple Pay, Google Pay or a wireless carrier,” researchers wrote.


SMSRanger sends a potential victim a text message requesting his or her phone number, researchers said. Once a target’s phone number has been entered in a chat message, the bot takes over from there, “ultimately granting [cybercriminals] access to whatever account has been targeted,” they wrote.


About 80 percent of users who are targeted by SMSRanger will end up providing their full and accurate information to threat actors, allowing them to defraud these victims, researchers added.


**Impersonating Trusted Companies**
-----------------------------------


Meanwhile, BloodTPbot also uses the ability to send users a fraudulent OTP code via SMS, researchers noted. However, this bot requires an attacker to spoof the victim’s phone number and impersonate a bank or company representative.


The bot attempts to call victims and uses social-engineering techniques to obtain a verification code from the person targeted. An attacker will receive a notification from the bot during the call specifying when to request the OTP during the authentication process, researchers explained. The bot then texts the code to the operator once the victim receives the OTP and enters it on the phone’s keyboard.


BloodTPbot goes for a monthly fee of $300; users also can pay between $20 to $100 more to access live phishing panels that target accounts on social-media networks, including Facebook, Instagram and Snapchat; financial services like PayPal and Venmo; the investment app Robinhood; and cryptocurrency marketplace Coinbase, researchers said.


**Masquerading as Banks**
-------------------------


The third bot observed by researchers, SMS Buster, requires a bit more effort than the others for a threat actor to gain access to someone’s account information, they said.


The bot provides options so an attacker can disguise a call made from any phone number to make it appear as a legitimate contact from a specific bank, researchers said. Upon calling a potential victim, an attackers follows a script to try to fool the target into providing info such as an ATM card PIN, credit card verification value (CVV) or OTP.


Researchers observed threat actors using SMS Buster against Canadian victims and their bank accounts, using both English and French to target people, they said. At the time the post was written, Intel 471 researchers had witnessed attackers illegally accessing accounts at eight different Canadian-based banks using SMS Buster.


“Overall, the bots show that some forms of two-factor authentication can have their own security risks,” researchers concluded. “While SMS- and phone-call-based OTP services are better than nothing, criminals have found ways to socially engineer their way around the safeguards.”


***Rule #1 of Linux Security:****No cybersecurity solution is viable if you don’t have the basics down.*[***JOIN***](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)*Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the*[***4 Golden Rules of Linux Security***](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)*. Your top takeaway will be a Linux roadmap to getting the basics right!*[***REGISTER NOW***](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)*and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.*




#### Tags:
[[said.]] [[OTP]] [[Linux]] [[SMS]] [[SMSRanger]] [[ThreatPost]]
