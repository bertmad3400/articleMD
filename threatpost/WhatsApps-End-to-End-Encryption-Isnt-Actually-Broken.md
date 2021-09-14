# WhatsApp’s End-to-End Encryption Isn’t Actually Broken
### WhatsApp’s moderators sent messages flagged by intended recipients. Researchers say this isn’t concerning — yet.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169399)
+ Date: September 13, 2021  2:41 pm
+ Author: Becky Bracken


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2019/11/18125720/whatsapp-flaw.jpg)
End-to-end encryption isn’t designed to secure messages against the intended recipients.


New revelations about WhatsApp’s moderator access to messages last week might seem like they run counter to the company’s privacy-forward brand, but a closer look shows the messaging service’s privacy protections remain in place and are operating as intended.


First, some background: A report from non-profit investigative journalism organization ProPublica reported that users can flag messages as abusive — and those messages will be sent to a moderator. The report positions the option for [moderators to review messages as a security flaw](https://www.propublica.org/article/how-facebook-undermines-privacy-protections-for-its-2-billion-whatsapp-users), but data-security experts disagree with that characterization, explaining the distinction is that the intended user must initiate the review.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


This isn’t a violation of the promises of end-to-end encryption, experts explained to Threatpost, which [WhatsApp has had in place since 2016](https://threatpost.com/whatsapp-encryption-a-good-start-but-far-from-a-security-cure-all/117230/). The platform has more than [2 billion users worldwide](https://www.statista.com/statistics/260819/number-of-monthly-active-whatsapp-users/).


Chris Hauk, who is a consumer privacy champion with Pixel Privacy, explained to Threatpost that this practice isn’t something he has a “problem” with, adding that once a user receives a message, “all bets are off as to sharing of the message.”


Taylor Gulley with nVisium told Threatpost that he too agrees WhatsApp isn’t violating user privacy with its reporting feature.


**Trusted Sources Can Flag Messages for Moderation**
----------------------------------------------------


“Yes, WhatsApp is reviewing a lot of unencrypted messages, but it’s at the behest of a trusted party in that conversation,” Gulley said. “As with any communication, it’s important to realize that even when the method is thought to be secure, the next weakest link is the people involved in that conversation.”


Gulley explained that once a report of abuse is made, the platform automatically submits five messages for moderation: the offending message and four previous messages in the conversation to add context.


“These messages are then reviewed manually and by artificial intelligence (AI) to check for abuse or terms-of-service violations,” he said.


WhatsApp and its parent company Facebook are generally viewed skeptically by privacy advocates.  ProPublica’s report explained that in countries where communications are limited and tightly controlled, WhatsApp functions as a crucial lifeline for dissidents and whistleblowers around the world who need to communicate without government surveillance. However, it added that in 2016, WhatsApp [began sharing critical user metadata](https://threatpost.com/whatsapp-blasted-by-eu-data-protection-group-over-facebook-sharing/121656/) with Facebook to try and turn a profit. And the following year the company was sued by regulators in both the European Union and the U.S.  for failing to protect user privacy.


Facebook founder Mark Zuckerberg has made public commitments to protecting user data, ProPublica highlighted.


“We don’t see any of the content in WhatsApp,” Zuckerberg said during Senate testimony in 2018.


While ProPublica’s reporting on the moderation function shows this statement isn’t exactly 100 percent true in all cases, security pros argue this is hardly a user privacy violation, and that the report, while unflattering, doesn’t prove that WhatsApp is abusing user messages.


Chris Clements, researcher at Cerberus, compares this moderation function to someone sharing a screen capture of a sensitive conversation they’re part of online.


“The user that the message is sent to by definition has access to the decrypted information,” Clements commented by email. “It’s not a situation encryption is designed to protect against. Further, a message is displayed that clearly indicates to the reporting user that a specific number of messages will be shared with the moderation team when they choose to report.”


**Potential Abuse a Real Concern**
----------------------------------


End-to-end technicalities aside, Erich Kron, security awareness advocate at KnowBe4 added that these new revelations will nonetheless likely have some effect on the platform’s brand — and may be useful to cybercriminals.


“While specific things need to happen, specifically one of the parties in a conversation must report it, this does not shine a good light on the privacy that WhatsApp is saying it offers,” Kron told Threatpost.


He explained the moderation process itself could be abused by threat actors interested in getting information about message content.


“If they can see those messages, it means there is a way that the organization could view all of them, and odds are, surveillance groups and possibly even some cybercriminals have now made this process that allows decrypting the messages when being reported a target,” Kron said. “With encryption, it is not usually the encryption itself that is broken, but rather the process used to perform the encryption. It is often in how the encryption keys are handled that makes the difference, and you can bet this will be a prime target now with WhatsApp.”


**Law Enforcement Wants WhatsApp Meta Data**
--------------------------------------------


Another criticism of WhatsApp in the ProPublica report is its ongoing cooperation with law enforcement. ProPublica found that WhatsApp reported 400,000 instances of possible exploitive images of children in 2020, ten times more than 2019.


WhatsApp only has access to metadata, rather than the messages themselves, but that metadata can be incredibly valuable to law enforcement.


“In terms of handing over information to law enforcement, well, what also wasn’t talked about enough, or perhaps tactically left out, was the amount of metadata we know is being collected and stored,” Caitlin Johanson with Coalfire explained to Threatpost. “Facebook sure knows what it needs to have ready in a CYA moment.”


Facebook and WhatsApp are hardly the only messaging platforms to come under sharp criticism from privacy groups.


Apple recently announced it would delay its plans to [deploy a CSAM image-detection](https://www.cnbc.com/2021/09/03/apple-delays-controversial-plan-to-scan-iphones-for-child-exploitation-images.html) backdoor to identify child sexual materials after outcry from privacy advocates. And video platform Zoom was just hit with a $85 million class-action lawsuit fine over its lax [security and lack of end-to-end encryption](https://threatpost.com/zoom-settlement-85m-security-investment/168445/).


But it appears in the case of WhatsApp, it’s up to users to share confidential messages only with those they trust.


“It’s the Wild West when it comes to invading one’s privacy,” Johanson cautioned. “One’s feature is another’s backdoor.”


**It’s time to evolve threat hunting into a pursuit of adversaries.**[**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**Threatpost and Cybersixgill for**[**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**and get a guided tour of the dark web and learn how to track threat actors before their next attack.**[**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with independent researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[WhatsApp]] [[isn’t]] [[ProPublica]] [[Threatpost]] [[Facebook]] [[it’s]] [[said.]] [[metadata]] [[ThreatPost]]
