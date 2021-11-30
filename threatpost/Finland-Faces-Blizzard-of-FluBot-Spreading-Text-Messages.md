# Finland Faces Blizzard of FluBot-Spreading Text Messages
### Millions of texts leading to the Flubot spyware/banking trojan are targeting everyone who uses Androids in the country, in an “exceptional” attack.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176649)
+ Date: November 30, 2021  1:11 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/30105841/nature-outdoor-snow-cold-winter-people-1213447-pxhere.com_.jpg)
The Flubot banking trojan is blanketing Finland, spreading via Android phones that are sending millions of malicious text messages.


On Friday, the National Cyber Security Centre (NCSC-FI) at the Finnish Transport and Communications Agency posted [a “severe” alert](https://www.kyberturvallisuuskeskus.fi/en/news/ncsc-fi-issued-severe-alert-malware-being-spread-sms) about the malware blizzard, which it said was spreading via dozens of message variants that are sneezing out [Flubot](https://threatpost.com/flubot-malware-targets-androids-with-fake-security-updates/175276/) like mad.


Once installed, Flubot sets about gaining permissions, stealing banking information and credentials, lifting passwords stored on the device and squirreling away various pieces of personal information. It also sends out additional text messages to the infected device’s contact list, which allows it to “go viral” — like the flu.


“An Android malware called Flubot is being spread by SMS. According to our current estimate, tens of thousands of messages have been sent to people in Finland during one day. We expect the amount to increase in the coming days and weeks,” said Aino-Maria Väyrynen, information security adviser at the NCSC-FI, in the alert.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


It Started Not-Slow & Continued to Grow-Grow-Grow
-------------------------------------------------


The campaign did indeed get far more virulent, just as Väyrynen predicted: In an article published early Tuesday morning, Väyrynen was quoted by [Bloomberg](https://www.bloomberg.com/news/articles/2021-11-30/finland-battles-exceptional-malware-attack-spread-by-phones) as saying that the daily messages now number in the millions.


The country’s biggest telecom companies told the news outlet that they’ve intercepted hundreds of thousands of messages. Teemu Makela, CISO at Elisa Oyj, called the attack “extremely exceptional and very worrying.”


When Androids, iPhones, Etc. Attack
-----------------------------------


The NCSC-FI’s advisory said that the malware is targeting “everyone using an Android device and a mobile subscription,” while iPhones and other devices “are directed to other fraudulent material on the website.”


The malicious text messages are using come-ons that tell targets that they’ve received a voicemail or a message from their mobile operator. All of the variant messages ask the recipient to open a malicious link.


The link doesn’t install the malware right off the bat: Rather, targets are prompted to grant voicemail permissions, which is actually a front for malware installation. Then, once installed, the malware steals data from the device and sends malware-spreading scam messages in the background.


There are telltale red flags: The messages “are often written without Scandinavian letters (å, ä and ö) and may contain the characters +, /, &, % and @ in random and illogical places in the text,” the advisory explained.


Finnish authorities shared examples of the messages, as well as the malware’s installation request, both of which are shown below.


 


No Immunity Gained After Earlier Flubot Campaign
------------------------------------------------


This is the second time that Flubot has buffeted Finland. A Flubot mobile malware campaign was unleashed in Finland [in June 2021](https://www.kyberturvallisuuskeskus.fi/en/android-malware-spread-sms) and persisted into August, sending messages written in Finnish to thousands of Finns. In that earlier campaign, the malicious messages said that there was a package in delivery and included a tracking link that tried to lure targets to a scam website that tried to install Flubot.


That time, thanks to cooperation between the authorities and telecoms, the NCSC-FI said that the country managed to eliminate Flubot “almost completely.”


Antti Turunen, fraud manager at Swedish telco Telia (which operates in Finland) told Bloomberg that this time it’s worse — a sentiment shared by the NCSC-FI. The new wave shows that the Flubot operators have mutated their malware to hook its tentacles into victims regardless of the control measures put in place to eradicate the summer Flubot campaign, the security center said.


Flubot often switches up tactics: In October for instance, the banking trojan was seen using a [fake security warning](https://threatpost.com/flubot-malware-targets-androids-with-fake-security-updates/175276/) to try to trick Android users into thinking that they’d already been infected … with Flubot.


It was a lie, but it became a reality for recipients of the text message who clicked on the “install security update” button.


**Threat Intel Is ‘King’ to Protect Against These Attacks**
-----------------------------------------------------------


Hank Schless, senior manager of security solutions at Lookout, told Threatpost via email on Tuesday that Finland’s plight is an example of “the problems that the malware-as-a-service (MaaS) market creates for consumers and enterprises alike.” 


This market has made malware and phishing kits “incredibly accessible for even the least skilled threat actors,” he said. “Usually, for a very small price, someone can go online and find one of these kits fully built and ready to be used. Once they acquire the kit, all the attacker needs to do is host it on a web domain then build a delivery mechanism. Most frequently, this mechanism is some form of message targeting mobile users because of the number of ways you can deliver a message to these devices via SMS, email, social media platforms, third party messaging apps, gaming and even dating apps.” 


The only difference between Finland’s earlier Flubot campaign and this one are the different social-engineering hooks, he noted – a sign of how “socially engineered phishing attacks can continue to be effective over time.”


[Phishing](https://threatpost.com/tools-defending-phishing-attacks/176463/) has become “the most concerning issue for every enterprise,” Schless observed. “Threat actors not only use it to steal login credentials, but deliver malware to devices and infrastructure as well. Lookout data shows that threat actors heavily target users through mobile channels such as SMS, social media platforms, third party messaging apps, gaming and even dating apps.” 


He pointed to Lookout data showing that there was an average quarterly exposure rate to phishing attacks of 15.35 percent over the first three quarters of 2021: A jump from the 10.25 percent exposure rate the firm tracked in the first three quarters of 2020. 


“Phishing is clearly a growing issue for every organization,” he said.


While this Flubot campaign targets consumers, the same tactics are used to target enterprise organizations, Schless said: For example, the attacker’s bait message could say that a target’s Outlook or Salesforce login were compromised, luring them to a fake login page with the goal of stealing their corporate login credentials. 


“Once the attacker has those compromised credentials, they’re free to log in to any corporate app and move laterally through the infrastructure,” Schless continued. “This could lead to them exfiltrating or encrypting data for an eventual ransomware attack.”


He concluded by calling threat intel “king” when it comes to protecting against attacks like this. “Solutions backed by datasets with enough threat telemetry are the only way to detect and protect against these attacks before they can even reach the end user,” he said. “Since these campaigns typically run for a short amount of time, traditional security solutions will be too slow on the uptake. Pushing automated coverage against attacks like this as the malicious page when it’s being built, is the only way to mitigate the gap in protection.”


What to Do If You’ve Been Flubotted
-----------------------------------


The NCSC-FI offered [guidance](https://www.kyberturvallisuuskeskus.fi/en/be-aware-malware-spread-sms) on what to do if your device has been infected with Flubot. Caution: The medicine is bitter.


The easiest way to remedy the ailment is to perform a factory reset as soon as possible, the security center said. When restoring from backup, make sure to use a backup that dates back to pre-infection, the advisory recommended.


It gave these additional instructions, meant to keep the Flubot banking trojan from rampaging through financial accounts:


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** [***REGISTER TODAY***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article) ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This*** [***LIVE, interactive Threatpost Town Hall***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***, sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***  

[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article) ***for the LIVE event!***




#### Tags:
[[Flubot]] [[malware]] [[said.]] [[Android]] [[credentials,]] [[Flubot.]] [[Threatpost]] [[phishing]] [[Schless]] [[ThreatPost]]
