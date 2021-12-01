# Widespread ‘Smishing’ Campaign Defrauds Iranian Android Users
### Attackers use socially engineered SMS messages and malware to compromise tens of thousands of devices and drain user bank accounts.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176679)
+ Date: December 1, 2021  7:15 am
+ Author: Elizabeth Montalbano


## Article:
![emotet Smishing](https://media.threatpost.com/wp-content/uploads/sites/103/2020/02/19101804/smishing.png)
Attackers are impersonating the Iranian government in a widespread SMS phishing campaign that is defrauding thousands of Android users by installing malware on their devices that can steal their credit card data and siphon money from financial accounts.


Researchers from Check Point Research estimate that the campaign, which sends so called “smishing” messages that entice victims to visit a malicious website, has already compromised tens of thousands of devices. This has resulted in the theft of billions of Iranian rial (or hundreds of thousands of US dollars), they said in [a report](https://research.checkpoint.com/2021/smishing-botnets-going-viral-in-iran) published Wednesday.


The campaign is first delivered as a standard [smishing](https://threatpost.com/smishing-text-phishing-ciso-radar/165634/) attack, using socially engineered SMS messages sent to a potential victim’s device to lure them to a malicious website, researchers said. There they are asked to enter account info while Android malware silently installs a backdoor on devices.  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


What’s been impressive about the campaign is its ability of attackers to defraud so many people of so much money, researchers said.


“What is noteworthy about these current campaigns is the sheer scale of the attack,” they wrote in the report, adding that “an unprecedented number of victims” have shared similar stories on social networks about how their bank accounts were drained by the cybercriminals.


**Backdoor Capabilities**
-------------------------


The malware delivered to targets via the malicious site has a number of backdoor capabilities that allow attackers to steal money from people’s accounts, maintain persistence on their devices, and allow attackers to take over device functionality, researchers reported.


The malware immediately steals all of the victim’s SMS messages to a command-and-control (C2) server; with this type of data access, attackers can then bypass two-factor authentication (2FA) on financial accounts and make unauthorized account withdrawals, researchers said.


The app also hides its icon on the device, making it difficult for people to remove or control the app. The backdoor can then maintain persistence and use its botnet capabilities, communicating with the C2 server via Firebase Cloud Messaging to allow attackers to execute additional commands on the victim’s device. This can include stealing contacts and sending SMS messages, researchers said.


The malware also has a wormable component to it. It can expand the campaign’s attack surface by sending SMS messages to a list of potential victims using a custom message and a list of phone numbers retrieved from the C2 server, researchers said. This allows attackers to bypass any existing blocks on “malicious” numbers by telecom companies because the smishing messages are delivered from the phone numbers of recognized users, they said.


**Attack Sequence**
-------------------


The attack typically begins with an SMS message from an electronic judicial notification system that notifies the victim that a new complaint was opened against them—which in Iran, is not something to be ignored, researchers said.


“The seriousness of such an issue might explain why the campaign has gone viral,” they observed in the report. “When official government messages are involved, most citizens do not think twice before clicking the links.”


The link directs a target to what looks like an official government site, ostensibly to read the full complaint. There the user is asked to enter personal identification information to proceed to an electronic system to do so, using current COVID restrictions as a reason this must be done electronically.


Once this is done, the campaign redirects the victim to a page to download a malicious .apk file that, once installed, shows a fake login page for the Iranian electronic judicial notification system authentication service.


The page, which appears authentic, asks the victim to enter his or her mobile phone and national identity numbers as well as also notifies the victim that a small fee–—typically 20,000, or sometimes 50,000 Iranian rials, the equivalent of US$1–is required to proceed. The trivial amount alleviates any suspicious and makes the transaction appear legitimate, researchers noted.


Once the details are entered, the target is redirected to a payment page that shows a “payment error” message once the person carries through with the transaction—a signal that attackers already have taken the money and the person’s payment info. The malware payload of the campaign also has been installed on a person’s device at this point, allowing the attacker to proceed with further theft and other malicious activity.


***There’s a sea of unstructured data on the internet relating to the latest security threats.***[***REGISTER TODAY***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This***[***LIVE, interactive Threatpost Town Hall***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***, sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)**for the LIVE event!**




#### Tags:
[[said.]] [[SMS]] [[malware]] [[victim’s]] [[ThreatPost]]
