# Millions of Android users targeted in subscription fraud campaign
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/millions-of-android-users-targeted-in-subscription-fraud-campaign/)
+ Date: October 25, 2021
+ Author: Bill Toulas


## Article:
![Malicious Android app](https://www.bleepstatic.com/content/hl-images/2021/09/29/Android.jpg)


A massive fraud campaign utilizing 151 Android apps with 10.5 million downloads was used to subscribe users to premium subscription services without their knowledge.


Researchers at Avast discovered the campaign, naming it 'UltimaSMS,' and reported 80 associated apps that they found on the Google Play Store.


While Google quickly removed the apps, the fraudsters likely ammassed millions of dollars in fraudulent subscription charges.


It starts with a phone number
-----------------------------


The threat actors conducted the UltimateSMS campaign through 151 Android apps that pretended to be discount apps, games, custom keyboards, QR code scanners, video and photo editors, spam call blockers, camera filters, and more.


When launching one of these apps for the first time, use data from the smartphone, like the location and IMEI, to change its language to match the country.


The app would then prompt the user to enter their mobile phone number and email address to access the program's features.



![First screen on some of the scam apps.](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/first%20screen.png)**First screen on some of the scam apps.**  
*Source: Avast*
Having the phone number and the required permissions, the app then subscribes the victim to a $40 per month SMS service from which the scammers get a cut as an affiliate partner.


[Avast's analysis](https://blog.avast.com/premium-sms-scam-apps-on-play-store-avast) reveals that the authors of these apps have implemented a system that charges the victim the maximum possible amount based on their location.


Although most of these apps don't offer the advertised functionality, and despite the numerous bad reviews they had on the Play Store, their creators are still finding success through the sheer volume of submissions.


By using such a large number of apps for the 'UltimaSMS' campaign, the scammers maintained a constant influx of victims and preserved their presence on the Play Store despite the constant reporting and take-down action by Google.


According to Sensor Tower, the most affected countries are Egypt, Saudi Arabia, Pakistan, and the UAE, all counting over a million victimized users. In the U.S., the number of infected devices is 170,000.



![Countries most affected by the campaign](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/list%20of%20countries.png)**Countries most affected by the campaign**
What should UltimateSMS victims do?
-----------------------------------


While uninstalling the app will prevent new subscriptions from being made, it will not prevent the existing subscription from being charged again. To avoid future charges, you need to contact your carrier and ask for a cancellation of all SMS subscriptions.


You can review [this list on GitHub](http://github.com/avast/ioc/blob/master/UltimaSMS/UltimaSMS_IOC_19-10-2021.pdf) for a complete list of the apps you should remove immediately from your device.


To avoid falling victim to scams of this kind, ask your carrier to disable the premium SMS option for your account and avoid entering your phone number on apps that would not need this information.


It is also strongly advised that you read reviews before installing an app, and if there is repeated negative feedback, avoid the app altogether.




#### Tags:
[[apps]] [[SMS]] [[Bleeping Computer]]
