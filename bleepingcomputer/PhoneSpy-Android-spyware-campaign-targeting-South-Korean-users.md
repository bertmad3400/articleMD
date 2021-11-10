# PhoneSpy: Android spyware campaign targeting South Korean users
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/phonespy-android-spyware-campaign-targeting-south-korean-users/)
+ Date: November 10, 2021
+ Author: Bill Toulas


## Article:
![Android malware](https://www.bleepstatic.com/content/hl-images/2021/09/29/Android.jpg)


An ongoing spyware campaign dubbed 'PhoneSpy' targets South Korean users via a range of lifestyle apps that nest in the device and silently exfiltrate data.


The campaign deploys a powerful Android malware capable of stealing sensitive information from the users and taking over the device's microphone and camera.


Researchers at [Zimperium](https://blog.zimperium.com/phonespy-the-app-based-cyberattack-snooping-south-korean-citizens/) who discovered the campaign reported their findings to the US and South Korean authorities, but the host that supports the C2 server is yet to be taken down.


Hidden in "harmless" apps
-------------------------


The 'PhoneSpy' spyware comes disguised as a Yoga companion app, the Kakao Talk messaging app, an image gallery browser, a photo editing tool, and more.


Zimperium identified 23 laced apps that appear as harmless lifestyle apps, but in the background, the apps run all the time, silently spying on the user.


To do that, the apps ask the victim to grant numerous permissions upon installation, which is the only stage where cautious users would notice signs of trouble.



![Permissions requested by the spyware-laced app](https://www.bleepstatic.com/images/news/u/1220909/Security/permissions.jpg)**Permissions requested by the spyware-laced app**  
*Source: Zimperium*
The spyware that is hiding inside the masqueraded apps can do the following on a compromised device:


* Fetch the complete list of the installed applications
* Uninstall any application on the device
* Install apps by downloading APKs from links provided by C2
* Steal credentials using phishing URLs sent by C2
* Steal images (from both internal and SD card memory)
* Monitoring the GPS location
* Steal SMS messages
* Steal phone contacts
* Steal call logs
* Record audio in real-time
* Record video in real-time using front & rear cameras
* Access camera to take photos using front & rear cameras
* Send SMS to attacker-controlled phone number with attacker-controlled text
* Exfiltrate device information (IMEI, Brand, device name, Android version)
* Conceal its presence by hiding the icon from the device's drawer/menu


The spectrum of the stolen data is wide enough to support almost any malicious activity, from spying on spouses and employees to conducting corporate cyber-espionage and blackmailing people.


Apart from the spyware functionality, some apps also actively try to steal people's credentials by displaying fake login pages for various sites.


Phishing templates used in the PhoneSpy campaign mimick Facebook, Instagram, Kakao, and Google account login portals.



![Phishing pages served directly by the C2](https://www.bleepstatic.com/images/news/u/1220909/Security/phishing%20pages.jpg)**Phishing pages served by PhoneSpy**  
*Source: Zimperium*
Distributing laced apps
-----------------------


The initial distribution channel for the laced apps is unknown, and the threat actors did not upload the apps to the Google Play Store.


It could be distributed through websites, obscure party APK stores, social media, forums, or even [webhards and torrents](https://www.bleepingcomputer.com/news/security/rat-malware-spreading-in-korea-through-webhards-and-torrents/).


A potential distribution method may be via SMS sent by the compromised device to its contact list since the malware is capable.


Using SMS texts increases the chances of the recipients tapping on the link that leads to downloading the laced apps as it comes from a person they know and trust.



![Icons of some of the laced apps](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Icons of some of the laced apps**  
*Source: Zimperium*
If you think you might have downloaded a risky app carrying spyware, delete it immediately and then run an AV scanner to clean your device of any remnants.


In cases where privacy and security are imperative, perform a factory reset on the device.




#### Tags:
[[apps]] [[Zimperium]] [[spyware]] [[SMS]] [[C2]] [[Bleeping Computer]]
