# Over nine million Android devices infected by info-stealing trojan
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/over-nine-million-android-devices-infected-by-info-stealing-trojan/)
+ Date: November 23, 2021
+ Author: Bill Toulas


## Article:
![Android](https://www.bleepstatic.com/content/hl-images/2021/10/21/Android.jpg)


A large-scale malware campaign on Huawei's AppGallery has led to approximately 9,300,000 installs of Android trojans masquerading as over 190 different apps. 


The trojan is detected by Dr.Web as 'Android.Cynos.7.origin' and is a modified version of the Cynos malware designed to collect sensitive user data.


The discovery and report come from researchers at Dr. Web AV, who notified Huawei and helped them remove the identified apps from their store.


However, those who installed the apps on their devices will still have to remove them from their Android devices manually.


### Trojan disguised as game apps


The threat actors hid their malware in Android apps pretending to be simulators, platformers, arcades, RTS strategy, and shooting games for Russian-speaking, Chinese, or international (English) users.


As they all offered the advertised functionality, users were unlikely to remove them if they enjoyed the game.


The list of the Cynos malware apps is too extensive to share here, but some notable examples that stand out due to having a large number of installations are listed below:


* 快点躲起来 (Hurry up and hide) – 2,000,000
* Cat adventures – 427,000
* Drive school simulator – 142,000



![One of the trojanized apps](https://www.bleepstatic.com/images/news/u/1220909/Android%20malware/cat_adventures.png)**One of the trojanized apps.**  
*Source: Dr. Web*
Since it's impractical to compare your list of installed apps to the [full list of 190 malicious apps](https://github.com/DoctorWebLtd/malware-iocs/blob/master/Android.Cynos/README.adoc), the more straightforward solution would be to run an AV tool that can detect Cynos trojans and their variants.


Powerful malware
----------------


The functionality of this Cynos trojan variant can perform various malicious activities, including spying on SMS texts and downloading and installing other payloads.


"The Android.Cynos.7.origin is one of the modifications of the Cynos program module. This module can be integrated into Android apps to monetize them. This platform has been known since at least 2014," explained Doctor Web malware analysts in [their report](https://news.drweb.com/show/?i=14360&lng=en).


"Some of its versions have quite aggressive functionality: they send premium SMS, intercept incoming SMS, download and launch extra modules, and download and install other apps."


"The main functionality of the version discovered by our malware analysts is collecting the information about users and their devices and displaying ads."


The aggressive nature of the trojan becomes apparent right from the installation phase when it asks for permission to perform activities that are not generally associated with a game, such as making phone calls or detecting users' locations.



![Risky permission request from a laced game](https://www.bleepstatic.com/images/news/u/1220909/Android%20malware/permission.png)**Risky permission request from a laced game**  
*Source: Dr. Web*
If the user grants the permission requests, the malware can exfiltrate the following data to a remote server:


* User mobile phone number
* Device location based on GPS coordinates or the mobile network and Wi-Fi access point data
* Various mobile network parameters, such as the network code and mobile country code; also, GSM cell ID and international GSM location area code
* Various technical specs of the device
* Various parameters from the trojanized app’s metadata


In addition to the above, Cynos trojans can potentially download and install extra modules or apps, send premium service SMS, and intercept incoming SMS.


As such, these apps can lead to unexpected charges from subscribing to premium services, and they can also drop even stealthier spyware payloads.




#### Tags:
[[malware]] [[apps]] [[Cynos]] [[Android]] [[Dr.]] [[SMS,]] [[Bleeping Computer]]
