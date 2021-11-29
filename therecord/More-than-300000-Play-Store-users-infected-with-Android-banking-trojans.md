# More than 300,000 Play Store users infected with Android banking trojans
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/more-than-300000-play-store-users-infected-with-android-banking-trojans/)
+ Date: November 29, 2021
+ Author: Catalin Cimpanu


## Article:
![More than 300,000 Play Store users infected with Android banking trojans](https://therecord.media/wp-content/uploads/2021/11/play-store.png)

More than 300,000 Android users were infected with banking trojans after installing apps from the official Google Play Store over the past few months, mobile security firm ThreatFabric said today.


The malicious code was hidden inside fully functional apps that operated as QR code scanners, PDF scanners, security tools, fitness apps, and two-factor authenticators.


But besides the legitimate functionality they offered, these apps also included a special module called a “loader.”


#### Loaders are still the best way to deploy malware on the Play Store


In the cybersecurity field, loaders are small pieces of malware that are hidden inside an app. They typically contain very little and very benign functionality, such as the ability to connect to a remote server to download and run additional code.


This lightweight design allows them to bypass checks performed by security software. However, while loaders contain the same functionality of any in-app update module, they are typically used to connect to an attacker’s remote server and download and run a more potent payload, which might not get scrutinized as much as the initial app install.


Due to this clever design, loaders have been an old and reliable payload distribution mechanism for desktop malware since the late 2000s, and today, some of the world’s largest botnets, such as Dridex, Emotet, and Trickbot, are designed around a loader component that acts as an initial point of infection before more complex modules are deployed on infected systems.


In the mobile market, malware groups [began using loaders in 2017 and 2018](https://www.bleepingcomputer.com/news/security/droppers-is-how-android-malware-keeps-sneaking-into-the-play-store/) after a series of updates to Google’s Play Store security scans made it more difficult to hide actual malware inside an app during the app submission process.


Loaders allowed Android malware groups to place a benign-looking component inside legitimate-looking apps, submit the app for scanning, get listed on the Play Store, and deploy the actual malware after the app was installed on user devices.


Initial designs for Android loaders used environment scans to detect Android OS emulators as a way to detect when an app/loader was scanned inside Bouncer—Google’s Play Store app scanning system.


Later designs also started incorporation delayed execution timers in order to prevent the loader from running while being tested inside Bouncer.


Today, Google’s Bouncer checks include a multitude of various types of scans, with [the latest one](https://support.google.com/googleplay/android-developer/answer/10964491) being added last month, in October 2021, when Google decided to restrict the category of apps that can gain access to permissions that Google has classified as “dangerous” due to their repeated abuse by malware gangs.


#### Loaders bypass latest Play Store checks


But in a [blog post](https://threatfabric.com/blogs/deceive-the-heavens-to-cross-the-sea.html) today, ThreatFabric says that this new update does not appear to have slowed down the operators of Loader-as-a-Service systems at all.


ThreatFabric says that malware gangs have responded to Google’s latest change by submitting clean apps to Google’s Bouncer checks and then incrementally adding the malicious code throughout one or more app updates.


Once the entire loader code is present inside an app, the malware gangs can then move to ask users for access to dangerous permissions and deploy their final payloads on the infected devices.


In other cases, some gangs only deployed their second-stage payloads in one geographical area at a time—to make sure their final payloads only reach real users and not Google security sandboxes.


Furthermore, some malware gangs also created fake websites for their apps, where they hosted the loader’s command and control server, so any malicious code looked like a legitimate component from an app’s official website.


ThreatFabric says it has already seen four different Android banking trojans using these updated delivery tactics in real-world campaigns. The list includes banking trojans like Anatsa, Ermac, Hydra, and Alien.


Once the loaders install any of these four, these banking trojans can steal credentials for social media, instant messaging, mobile banking, and cryptocurrency apps. Some of them also have the ability to bypass SMS-based two-factor authentication and automate the theft of user funds.


According to ThreatFabric, the following Play Store apps contained novel loaders that led to a banking trojan infection, even after Google’s latest updates. All apps were reported to the Play Store security team and removed from the store.




| App name | Package name |
| --- | --- |
| Two Factor Authenticator | com.flowdivison |
| Protection Guard | com.protectionguard.app |
| QR CreatorScanner | com.ready.qrscanner.mix |
| Master Scanner Live | com.multifuction.combine.qr |
| QR Scanner 2021 | com.qr.code.generate |
| QR Scanner | com.qr.barqr.scangen |
| PDF Document Scanner – Scan to PDF | com.xaviermuches.docscannerpro2 |
| PDF Document Scanner | com.docscanverifier.mobile |
| PDF Document Scanner Free | com.doscanner.mobile |
| CryptoTracker | cryptolistapp.app.com.cryptotracker |
| Gym and Fitness Trainer | com.gym.trainer.jeux |





#### Tags:
[[malware]] [[apps]] [[Android]] [[Google’s]] [[Google]] [[ThreatFabric]] [[apps,]] [[The Record]]
