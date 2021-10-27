# Android spyware apps target Israel in three-year-long campaign
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/android-spyware-apps-target-israel-in-three-year-long-campaign/)
+ Date: October 27, 2021
+ Author: Bill Toulas


## Article:
![hacker](https://www.bleepstatic.com/content/hl-images/2021/06/30/hacker.jpg)


A set of seemingly innocuous Android apps have been infecting Israeli users with spyware since 2018, and the campaign continues to this day.


The spyware-laden apps were discovered by researchers at Qihoo 360 who found various apps disguised as social applications, Threema, Al-Aqsa Radio, Al-Aqsa Mosque, Jerusalem Guide, PDF viewer, Wire, and other applications.


The most abused app is one pretending to be Threema, an end-to-end encrypted instant messaging application.



![Laced apps used for spyware distribution](https://www.bleepstatic.com/images/news/u/1220909/Security/apps.png)**Laced apps used for spyware distribution**  

Source: Qihoo 360
The researchers believe the initial vector for these apps is a Facebook post or WhatsApp message that points victims to a website that hosts the APK and offers it for download.


In some cases, the messages contain a Google Drive link to a supposedly important classified PDF document.



![PDF used as lure to download laced PDF reader](https://www.bleepstatic.com/images/news/u/1220909/Security/pdf.png)**PDF used as a lure to download laced PDF reader**  

Source: Qihoo 360
The target is then urged to download an APK that pretends to be the mobile version of Adobe Reader, but which is actually spyware.


Extensive spyware set
---------------------


The researchers [analyzed](https://blogs.360.cn/post/Three_years_of_attacks_on_Israel_and_Palestine_are_revealed.html) various samples and found that the attackers use a wide range of different commodity malware for these attacks, including SpyNote, Mobihok, WH-RAT, and 888RAT.



![888RAT control panel](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**888RAT control panel**  
*Source: Qihoo 360*
These are all commercial spyware with powerful functionality, including:


* file exfiltration
* call recording
* location tracking
* keylogging
* photo and video capturing
* real-time recording
* clipboard management
* phishing
* shell command execution


In fewer cases, Metasploit and EsecretRAT were found in the APKs. On both occasions, the actors had implemented additional custom code on top of the open-source tools. 


EsecretRAT is based on ChatApp and is a novel spyware tool capable of exfiltrating contact lists, SMS, IMEI, location info, IP address, and all photos stored in the device. 


Signs of Hamas hackers
----------------------


Qihoo 360 believes that ‘APT-C-23’, a Hamas-backed group, is behind the attacks and has been repeatedly linked with past Israel-targeting campaigns.


In October 2020, they were uncovered for using Android spyware [disguised as Threema](https://www.bleepingcomputer.com/news/security/fake-threema-telegram-apps-hide-spyware-for-targeted-attacks/) and Telegram against devices in Israel.


A few months earlier, they baited Israeli soldiers through custom spyware apps made to appear as legit [dating apps](https://www.bleepingcomputer.com/news/security/hacker-group-catfishes-israeli-soldiers-into-installing-mobile-rat/).


For this campaign, which has been going on for three years, the researchers note that the attribution may be thin, but the similarities with previous APT-C-23 campaigns are strong.


If you have downloaded Threema, Telegram, PDF viewer, Al-Aqsa Radio, Al-Aqsa Mosque, and Jerusalem Guide from any site other than the Google Play Store, it is advised that you remove the app immediately and scan your device with an antivirus program.




#### Tags:
[[spyware]] [[apps]] [[Qihoo]] [[PDF]] [[Al-Aqsa]] [[Threema,]] [[Bleeping Computer]]
