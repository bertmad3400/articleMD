# Telegram bots are trying to steal your one-time passwords
### The tokens can be used to shred second-stage account verification.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/telegram-bots-are-trying-to-steal-your-one-time-passwords/)
+ Date: September 29, 2021
+ Author: Charlie Osborne


## Article:
Unknown

Telegram-powered bots are being utilized to steal the one-time passwords required in two-factor authentication (2FA) security. 


On Wednesday, researchers from Intel 471 said that they have seen an "uptick" in the number of these services provided in the web's underground, and over the past few months, it appears the variety of 2FA circumvention solutions is expanding -- with bots becoming a firm favorite.  

Two-factor authentication (2FA) can take the form of one-time password (OTP) tokens, codes, links, biometric markers, or by tapping a physical dongle to confirm an account owner's identity. Most often, 2FA tokens are sent through a text message to a handset or an email address.  

While 2FA can improve upon the use of passwords alone to protect our accounts, threat actors were quick to develop methods to intercept OTP, such as through malware or social engineering.  

According to Intel 471, since June, a number of 2FA-circumventing services are abusing the Telegram messaging service. Telegram is either being used to create and manage bots or as a 'customer support' channel host for cybercriminals running these types of operations.  

"In these support channels, users often share their success while using the bot, often walking away with thousands of dollars from victim accounts," the researchers say.  

The Telegram bots are being used to automatically call would-be victims in phishing attempts, to send messages claiming to be from a bank, and to otherwise try and lure victims into handing over OTP codes. Other bots are targeting social media users in phishing and [SIM-swap](https://www.zdnet.com/article/europol-tackles-massive-sim-swap-hacking-rings/) attack attempts.  






In order to create a bot, there is a basic level of programming required -- but nothing in comparison to developing custom malware, for example. What makes matters worse is that in the same way as traditional botnets, the Telegram bots can be leased out -- and once the phone number of an intended victim is submitted, attacks can begin with only a few clicks.  

The researchers cited two particular bots of interest; SMSRanger and BloodOTPbot.  

SMSRanger's interface and command setup are similar to the Slack collaboration platform and it can be used to target particular services including PayPal, Apple Pay, and Google Play. BloodOTPbot is an SMS-based bot that can also be used to generate automatic calls that impersonate bank staff.  

![screenshot-2021-09-27-at-14-07-40.png]()![screenshot-2021-09-27-at-14-07-40.png](https://www.zdnet.com/a/img/resize/8f885b74afa832969dae7d178b27008b3e052ed2/2021/09/27/3361be4a-84e3-466e-8117-522a4c02b376/screenshot-2021-09-27-at-14-07-40.png?width=470&fit=bounds&auto=webp)
 Intel 471
 "The bots show that some forms of two-factor authentication can have their own security risks," Intel 471 commented. "While SMS- and phone-call-based OTP services are better than nothing, criminals have found ways to socially engineer their way around the safeguards."

In April, Check Point Research disclosed the existence of a Remote Access Trojan (RAT) [dubbed ToxicEye](https://www.zdnet.com/article/toxiceye-trojan-abuses-telegram-platform-to-steal-your-data/) that abuses the Telegram platform, leveraging the communications service within its command-and-control (C2) infrastructure.  

###  Previous and related coverage

* [WhatsApp vs. Signal vs. Telegram vs. Facebook: What data do they have about you?](https://www.zdnet.com/article/whatsapp-vs-signal-vs-telegram-vs-facebook-what-data-do-they-have-about-you/)  

* [Telegram now lets you bring across chat history from WhatsApp](https://www.zdnet.com/article/telegram-now-lets-you-bring-across-chat-history-from-whatsapp/)  

* [ToxicEye: Trojan abuses Telegram platform to steal your data](https://www.zdnet.com/article/toxiceye-trojan-abuses-telegram-platform-to-steal-your-data/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[2FA]] [[WhatsApp]] [[vs.]] [[ZDNet]]
