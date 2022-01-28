# Google Play app dropped Vultur banking Trojan on Android handsets | ZDNet
### The app was installed thousands of times before it was removed.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/google-play-app-dropped-vultur-banking-trojan-on-android-handsets/
+ Date: 2022-01-28 09:46:43
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/c453bc6faf80858af6fa9cd3c208c1baa47c6545/2021/05/20/632cb058-b115-4737-8be3-24a70059e7b6/android-mascot-in-cloud.jpg?width=770&height=578&fit=crop&auto=webp)

A Trojanized 2FA authenticator app has been removed from the Google Play Store. 


The app, 2FA Authenticator, was discovered by the [Pradeo](https://blog.pradeo.com/vultur-malware-dropper-google-play) security team. 

According to a [cached version](https://web.archive.org/web/20220121164214/https://play.google.com/store/apps/details?id=com.privacy.account.safetyapp) of the app's page on Google Play, the developer said the software provided a "secure authenticator for your online services, while also including some features missing in existing authenticator apps, like proper encryption and backups."

In addition, the app claimed to support HOTP and TOTP, and was marketed as a way to import other authenticator protocols – including Authy, Google Authenticator, Microsoft Authenticator, and Steam – and host them in one place.  

![screenshot-2022-01-28-at-08-50-22.png]()![screenshot-2022-01-28-at-08-50-22.png](https://www.zdnet.com/a/img/resize/64cc14019f25becd9fd1e56c800a8db07813723c/2022/01/28/8971951a-4592-422d-ac5f-0bb881c2119b/screenshot-2022-01-28-at-08-50-22.png?width=1200&fit=bounds&auto=webp)
 Pradeo
 During its time on Google Play, the app was downloaded and installed over 10,000 times.  

However, the app was less about protecting your data and more about stealing it. According to Pradeo, upon installation, the app would act as a dropper for malware designed to steal financial information.  

"It has been developed to look legitimate and provide a real service," the researchers say. "To do so, its developers used the open-source code of the official [Aegis](https://getaegis.app/) authentication application to which they injected malicious code. As a result, the application is successfully disguised as an authentication tool which ensures it maintains a low profile." 






In the first stage of the attack, 2FA Authenticator requests a range of permissions from the handset owner including camera and biometric access, the ability to tamper with system alerts, package querying, and the ability to disable keylock.  

The permissions allow the malware to perform actions including collecting localized data for targeted attacks; disabling keylock and password security, downloading external apps, and creating overlay windows over other mobile application windows.  

Once these permissions have been granted, the dropper then installs Vultur.  

According to [Threat Fabric](https://www.threatfabric.com/blogs/vultur-v-for-vnc.html), Vulture is a Remote Access Trojan (RAT) that is a relatively new entrant to the malware landscape. Vultur uses screen recording and keylogging to capture bank account and financial service credentials rather than traditional overlay functions – a slower method, but potentially one that is less likely to be detected.  

Vultur tends to target European banking institutions as well as a range of cryptocurrency wallet platforms. The dropper used to execute the RAT is a framework called Brunhilda, previously linked to Android malware distribution through fake utility and 2FA apps on Google Play.  

In an update, the Pradeo team said the malicious app was removed after being available on the Google Play Store for 15 days. If you try to access the [2FA Authenticator](https://play.google.com/store/apps/details?id=com.privacy.account.safetyapp) page, you are met with an error display.  

Users of the app are advised to delete the software from their handsets. 

ZDNet has reached out to Google and we will update when we hear back.

###  Previous and related coverage

* [New banking Trojan SharkBot makes waves across Europe, US](https://www.zdnet.com/article/new-banking-trojan-sharkbot-makes-waves-across-europe/)
* [Over 300,000 Android users have downloaded these banking trojan malware apps, say security researchers](https://www.zdnet.com/article/over-300000-android-users-have-downloaded-these-banking-trojan-malware-apps-say-security-researchers/)
* [This cruel Android malware wipes phones after stealing money](https://www.zdnet.com/article/this-cruel-android-malware-wipes-phones-after-stealing-money/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Finance]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Google]] [[Malware]] [[2fa]] [[Pradeo]] [[Apps]] [[Android]] [[ZDNet]]

