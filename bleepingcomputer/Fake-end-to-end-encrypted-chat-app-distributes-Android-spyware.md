# Fake end-to-end encrypted chat app distributes Android spyware
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/fake-end-to-end-encrypted-chat-app-distributes-android-spyware/)
+ Date: November 13, 2021
+ Author: Bill Toulas


## Article:
![Spyware](https://www.bleepstatic.com/content/hl-images/2021/05/13/spyware.jpg)


The GravityRAT remote access trojan is being distributed in the wild again, this time under the guise of an end-to-end encrypted chat application called SoSafe Chat.


This particular RAT (remote access trojan) targets predominately Indian users, being distributed by Pakistani actors.


The telemetry data on the most recent campaign shows that the targeting scope hasn’t changed, and Gravity is still targeting high-profile individuals in India, like officers of the Armed Forces.


Disguised as a secure chat app
------------------------------


In 2020, the malware was targeting people via an Android app named ‘[Travel Mate Pro](https://www.bleepingcomputer.com/news/security/windows-gravityrat-malware-now-also-targets-android-macos/),’ but since the pandemic has slowed down traveling, the actors moved to a new guise.


The app is now called ‘SoSafe Chat’ and is promoted as a secure messaging application that features end-to-end encryption.



![The SoSafe Chat website](https://www.bleepstatic.com/images/news/u/1220909/Website%20snaps/website.jpg)**The SoSafe Chat website**
The website that likely played a role in the distribution of the app (sosafe.co[.]in) remains online today, but the download link and the registration form are no longer working.


The channel and method of distribution remain unknown, but it was likely by driving traffic to the site through malvertising, social media posts, and instant messages to targets.


Extensive spying abilities
--------------------------


Once installed on a target’s device, the spyware can perform a wide range of malicious behavior, allowing the threat actors to exfiltrate data, spy on the victim, and track their location.


The complete list of malicious behavior includes


* Read SMS, Call Logs, and Contacts data
* Change or modify system settings
* Read current cellular network information, the phone number and the serial number of the victim’s phone, the status of any ongoing calls, and a list of any Phone Accounts registered on the device
* Read or write the files on the device’s external storage
* Record audio
* Gets connected network information
* Get the device’s location


According to [researchers at Cyble](http://blog.cyble.com/2021/11/11/gravity-rat-malware-returns-as-a-chat-application/), the list of permissions that the malware requests for this functionality is naturally quite extensive, but it can still appear justified for an IM app.



![Permissions requested by SoSafe upon installation](https://www.bleepstatic.com/images/news/u/1220909/Security/permissions(1).jpg)**Permissions requested by SoSafe**  
*Source: Cyble*
Compared to the 2020 version, GravityRAT has added the ability to record audio and added mobile-specific features like location fetching and cellular network data exfiltration.



![SMS exflitration function](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**SMS exflitration function**  
*Source: Cyble*
Before the 2020 version, GravityRAT would [exclusively target Windows](https://timesofindia.indiatimes.com/city/lucknow/pakistan-spy-lured-98-targets-with-bots/articleshow/69867201.cms) machines, not having the ability to infect mobile devices.


As such, the reemergence of the malware in the wild in targeting mobile devices indicates that its authors are actively developing it.




#### Tags:
[[GravityRAT]] [[malware]] [[Bleeping Computer]]
