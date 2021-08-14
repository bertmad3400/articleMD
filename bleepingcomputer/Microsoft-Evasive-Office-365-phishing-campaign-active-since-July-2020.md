# Microsoft: Evasive Office 365 phishing campaign active since July 2020
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-evasive-office-365-phishing-campaign-active-since-july-2020/)
+ Date: August 12, 2021
+ Author: Sergiu Gatlan


## Article:
![](https://www.bleepstatic.com/content/hl-images/2020/11/06/Office-365.jpg)


Microsoft says that a year-long and highly evasive spear-phishing campaign has targeted Office 365 customers in multiple waves of attacks starting with July 2020.


The ongoing phishing campaign lures targets into handing over their Office 365 credentials using invoice-themed XLS.HTML attachments and various information about the potential victims, such as email addresses and company logos.



This suggests that the threat actors collect data on their targets in a reconnaissance stage of the attack, increasing the campaign's effectiveness through social engineering.


"This campaign’s primary goal is to harvest usernames, passwords, and—in its more recent iteration—other information like IP address and location, which attackers use as the initial entry point for later infiltration attempts," the Microsoft 365 Defender Threat Intelligence Team [explained](https://www.microsoft.com/security/blog/2021/08/12/attackers-use-morse-code-other-encryption-methods-in-evasive-phishing-campaign/).


Continuously evolving evasion tactics
-------------------------------------


However, this series of attacks stand out from others through the attackers' continuous efforts to obfuscate their phishing emails to circumvent email security solutions.


"In the case of this phishing campaign, these attempts include using multilayer obfuscation and encryption mechanisms for known existing file types, such as JavaScript. Multilayer obfuscation in HTML can likewise evade browser security solutions," Microsoft added.


The xls.HTML or xslx.HTML attachments bundled with these phishing emails are divided into multiple segments encoded using different methods to appear harmless and bypass email security controls.



![Encoding methods tmeline](https://www.bleepstatic.com/images/news/u/1109292/2021/Encoding-methods-timeline.png)*Encoding methods timeline (Microsoft)*
As Microsoft revealed, the segments delivered to the targets' inboxes with the spear-phishing emails include:


* Segment 1 – Email address of the target
* Segment 2 – Logo of the targeted user’s organization from logo[.]clearbit[.]com, i[.]gyazo[.]com, or api[.]statvoo[.]com; if the logo is not available, this segment loads the Microsoft Office 365 logo instead.
* Segment 3 – A script that loads an image of a blurred document, indicating that sign-in has supposedly timed out.
* Segment 4 – A script that prompts the user to enter their password, submits the entered password to a remote phishing kit, and displays a fake page with an error message to the user.


Throughout the campaign, the attackers have changed the encoding mechanisms to keep evading detection, using different methods for each segment and switching between plaintext HTML code, escaping, Base64, ASCII chars, and even Morse code. 


BleepingComputer shared more details on the [Morse code obfuscation](https://www.bleepingcomputer.com/news/security/new-phishing-attack-uses-morse-code-to-hide-malicious-urls/) in February, when the phishing campaign started using this new technique.


If the targets get tricked into launching the malicious attachment, it will display a fake Office 365 login dialog over a blurred Excel document in the victim's default web browser.


This login box, which also features the targets' email addresses and their company's logo, asks them to re-enter their passwords to access the blurred document because their login session has supposedly timed out.


If the target enters their password, a script will immediately display an alert saying that the submitted password is incorrect and send the password and other harvested user data to the attacker's phishing kit.



![Office 365 credentials phishing dialog](https://www.bleepstatic.com/images/news/u/1109292/2021/Phishing-credentials-dialog-box.png)*Office 365 credentials phishing dialog (Microsoft)*
"During our year-long investigation of [this] targeted, invoice-themed XLS.HTML phishing campaign, attackers changed obfuscation and encryption mechanisms every 37 days on average, demonstrating high motivation and skill to constantly evade detection and keep the credential theft operation running," Microsoft added.


"This phishing campaign exemplifies the modern email threat: sophisticated, evasive, and relentlessly evolving."


Microsoft alo warned in March of phishing operation that [stole an estimated 400,000 OWA and Office 365 credentials](https://www.bleepingcomputer.com/news/security/microsoft-warns-of-phishing-attacks-bypassing-email-gateways/) since December 2020 and expanded to abuse new legitimate services to bypass secure email gateways (SEGs).


The company also [alerted Microsoft Defender ATP subscribers in late-January](https://www.bleepingcomputer.com/news/security/microsoft-warns-of-increasing-oauth-office-365-phishing-attacks/) of an increasing number of consent phishing (aka OAuth phishing) attacks targeting remote workers.




#### Tags:
[[phishing]] [[Microsoft]] [[emails]] [[campaign,]] [[Bleeping Computer]]
