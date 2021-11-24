# 9.3M+ Androids Running ‘Malicious’ Games from Huawei AppGallery
### A new trojan called Android.Cynos.7.origin, designed to collect Android users’ device data and phone numbers, was found in 190 games installed on over 9M Android devices. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176581)
+ Date: November 24, 2021  12:28 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/24121603/android-e1637774177513.jpg)
Why would a game about a cat’s “cute diary” need permission to make phone calls or suss out your location?


It doesn’t: “Cat cute diary” is one of 190 trojanized games that Doctor Web malware analysts have found on AppGallery, the official app store for Huawei Android.


They’re littering the Android landscape. In a [report](https://news.drweb.com/show/?i=14360&lng=en) published on Tuesday, Doctor Web estimated that more than 9,300,000 Android device owners have installed the dangerous games.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


According to researchers, the main purpose of the slew of malware-laced apps – which includes loads of kid-enticing entries, including games, simulators, platformers, arcades, strategies and shooters – isn’t to satisfy users’ cute-kitty and shoot-the-bad-guys lust.


Rather, they’re rigged with a new Android trojan, tracked by the analysts as Android.Cynos.7.origin, the main purpose of which is to lap up users’ phone numbers and device data and to make money by milking the data to inflict ads, according researchers.


Fun and Games and Data Exfiltration
-----------------------------------


Doctor Web provided a few examples of the trojan-containing games, some of which are targeting Russian-speaking users and which have Russian titles and descriptions, and some of which target Chinese or international audiences.


One of them – the “快点躲起来” game – which, according to Google Translator, means “Hurry up and hide” in English – has been downloaded over 2,000,000 times, according to the research.


Here’s the [full list](https://github.com/DoctorWebLtd/malware-iocs/blob/master/Android.Cynos/README.adoc) of the 190 apps the researchers are identifying as malicious.


What the Apps Do With Those Permissions
---------------------------------------


Doctor Web said that the Android.Cynos.7.origin trojan is one of the modifications of the Cynos malware platform – a module that can be integrated into Android apps so as to squeeze money out of devices. Malware analysts have known about Cynos since at least 2014, the analysts said.


When the malicious apps are downloaded, they ask for permission to make and manage phone calls, as shown in the screen capture below.


“That allows the trojan to gain access to certain data,” the analysts explained. Namely, after a user grants those permissions, the trojans collects and exfiltrates all of the following information to a remote server:


For what it’s worth, some of the Cynos versions are even more aggressive that creep into the realm of spyware or more, according to Doctor Web: “They send premium SMS, intercept incoming SMS, download and launch extra modules, and download and install other apps.”


However, the 190 apps its analysts found are mainly designed to collect the above-mentioned list of information about users and their devices and to display ads.


Still, son’t shrug these off, Doctor Web analysts cautioned. These games are designed to be used by kids, which makes them plenty dangerous: “At first glance, a mobile phone number leak may seem like an insignificant problem. Yet in reality, it can seriously harm users, especially given the fact that children are the games’ main target audience.


“Even if the mobile phone number is registered to an adult, downloading a child’s game may highly likely indicate that the child is the one who [is] actually using the mobile phone. It is very doubtful that parents would want the above data about the phone to be transferred not only to unknown foreign servers, but to anyone else in general.”


Huawei Yanked the Bad Apps
--------------------------


This isn’t the first time that Huawei’s AppGallery has been infused with malware. In April, Doctor Web [reported](https://news.drweb.com/show/?i=14182&lng=en&c=5) that it had found the app store infested with apps that contained the [Joker](https://threatpost.com/updated-joker-malware-android-apps/167776/) trojan: apps that were downloaded by unwitting users to more than 538,000 devices.


Doctor Web notified Huawei about the Cynos-infested malicious apps in its Android gallery. Huawei subsequently removed them all. The company hadn’t responded to Threatpost’s request for comment by the time this article was published, but it did send this statement to [BleepingComputer](https://www.bleepingcomputer.com/news/security/over-nine-million-android-devices-infected-by-info-stealing-trojan/):


“AppGallery’s built-in security system swiftly identified the potential risk within these apps. We are now actively working with affected developers to troubleshoot their apps. Once we can confirm that the apps are all clear, they will be re-listed on AppGallery so consumers can download their favorite apps again and continue enjoying them.


“Protecting network security and user privacy is Huawei’s priority. We welcome all third-party oversight and feedback to ensure we deliver on this commitment. We will continue to collaborate closely with our partners, and at the same time, employ the most advanced and innovative technologies to safeguard our users’ privacy.”


*Image credit: [MaxPixel.](https://www.maxpixel.net/photo-604356)*


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** [***REGISTER TODAY***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article) ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This*** [***LIVE, interactive Threatpost Town Hall***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***, sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***




#### Tags:
[[apps]] [[Android]] [[Huawei]] [[users’]] [[Cynos]] [[ThreatPost]]
