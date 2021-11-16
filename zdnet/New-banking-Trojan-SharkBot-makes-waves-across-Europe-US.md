# New banking Trojan SharkBot makes waves across Europe, US
### The malware specializes in infiltrating Android handsets.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/new-banking-trojan-sharkbot-makes-waves-across-europe/)
+ Date: November 16, 2021
+ Author: Charlie Osborne


## Article:
Unknown

A new Android banking Trojan has been discovered that is able to circumvent multi-factor authentication controls through the abuse of ATS. 


At the end of October, cybersecurity researchers from Cleafy found the malware, which does not appear to belong to any known family. 

Now [dubbed SharkBot](https://www.cleafy.com/cleafy-labs/sharkbot-a-new-generation-of-android-trojan-is-targeting-banks-in-europe), the Android malware has been traced in attacks focused on stealing funds from vulnerable handsets running on the Google Android operating system.  

So far, infections have been found in the UK, Italy, and the United States.  

It is believed that SharkBot is likely a private botnet and is still in the early stages of development. 

SharkBot is modular malware that the researchers say belongs to the next generation of mobile malware able to perform attacks based on the Automatic Transfer System (ATS) system.  

ATS allows attackers to automatically fill in fields on an infected device with minimal human input. In the same way as the Gustuff banking Trojan, the autofill service is launched to facilitate fraudulent money transfers through legitimate financial service apps -- a general trend in malware development and a pivot from older theft techniques on mobile handsets, such as the use of phishing domains.  






Cleafy suggests that SharkBot utilizes this technique in an attempt to bypass behavioral analytics, biometric checks, and multi-factor authentication (MFA) -- as no new device would need to be enrolled. However, in order to do so, the malware must first compromise Android Accessibility Services.  

Once executed on an Android handset, SharkBot will immediately request accessibility permissions -- and will plague the victim with pop-ups until this is granted.  

No installation icon is displayed. Now armed with all of the handset permissions it needs, SharkBot will then quietly perform standard window overlay attacks to steal credentials and credit card information, theft based on ATS, and is also able to key log and both intercept or hide incoming SMS messages.  

The researchers say the banking Trojan is also capable of performing "gestures" on the victim's behalf.  

Apps provided by international banks and cryptocurrency services are being targeted.  

One silver lining is that no samples have been found in the official Android app repository, the Google Play Store. Instead, the malware has to be loaded from an external source through side-loading -- a practice that the vendor has warned can be dangerous, as this allows malicious apps to circumvent Google Play security controls.  

At the time of writing, SharkBot has low detection rates by antivirus solutions.  

"With the discovery of SharkBot we have shown new evidence about how mobile malware [is] quickly finding new ways to perform fraud, trying to bypass behavioral detection countermeasures put in place by multiple banks and financial services during the last years," Cleafy says. "Like the evolution of workstation malware occurred in the past years, in the mobile field, we are seeing a rapid evolution towards more sophisticated patterns like ATS attacks." 

###  Previous and related coverage

* [Meris botnet assaults KrebsOnSecurity](https://www.zdnet.com/article/meris-botnet-assaults-krebsonsecurity/)
* [This malware botnet gang has stolen millions with a surprisingly simple trick](https://www.zdnet.com/article/this-relentless-malware-botnet-has-made-millions-with-a-surprisingly-simple-trick/)
* [This ransomware-spreading malware botnet just won't go away](https://www.zdnet.com/article/this-ransomware-spreading-malware-botnet-just-wont-go-away/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[malware]] [[SharkBot]] [[Android]] [[botnet]] [[Cleafy]] [[Google]] [[ZDNet]]
