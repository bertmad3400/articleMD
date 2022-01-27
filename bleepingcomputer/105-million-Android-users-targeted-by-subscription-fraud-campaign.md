# 105 million Android users targeted by subscription fraud campaign
### A premium services subscription scam for Android has been operating for close to two years. Called 'Dark Herring', the operation used 470 Google Play Store apps and affected over 100 million users worldwide, potentially causing hundreds of millions of USD in total losses.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/105-million-android-users-targeted-by-subscription-fraud-campaign/
+ Date: 2022-01-27T07:07:48-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/10/21/Android_headpic_red.jpg)

!['Dark Herring' premium service fraud impacts 105 million Android users](https://www.bleepstatic.com/content/hl-images/2021/10/21/Android_headpic_red.jpg)


A premium services subscription scam for Android has been operating for close to two years. Called ‘Dark Herring’, the operation used 470 Google Play Store apps and affected over 100 million users worldwide, potentially causing hundreds of millions of USD in total losses.


‘Dark Herring’ was present in 470 applications on the Google Play Store, Android’s official and most trustworthy source of apps, with the earliest submission dating to March 2020.


In total, the fraudulent apps were installed by 105 million users in 70 countries, subscribing them to premium services that charged $15 per month through Direct Carrier Billing (DCB).


DCB is a mobile payment option that lets people purchase digital content from the Play Store, charging it to their prepaid balance or postpaid bill.


The operators of ‘Dark Herring’ cashed the subscriptions while users realized the fraudulent charges much later, sometimes several months after the infection.


The discovery of ‘Dark Herring’ comes from [Zimperium zLabs](https://blog.zimperium.com/dark-herring-android-scamware-exceeds-100m-installations/), a Google partner and member of the Google App Defense Alliance, whose goal is to tackle the malware problem on the Play Store.


How the malware works
---------------------


The long-term success of the Dark Herring relied on AV anti-detection capabilities, propagation through a large number of apps, code obfuscation, and the use of proxies as first-stage URLs.


While none of the above is new or groundbreaking, seeing them combined into a single piece of software is rare for Android fraud.


Moreover, the actors used a sophisticated infrastructure that received communications from all users of the 470 applications but handled each separately based on a unique identifier.


The installed app doesn’t contain any malicious code but features a hard-coded encrypted string that points to a first-stage URL hosted on Amazon's CloudFront.


The response from the server contains links to additional JavaScript files hosted on AWS instances, which are downloaded onto the infected device.



![Response from the first-stage URL](https://www.bleepstatic.com/images/news/u/1220909/Android%20malware/http-response.jpg)**Response from the first-stage URL**  
*Source: Zimperium*
These scripts prepare the app to acquire its configuration in relation to the victim, generate the unique identifiers, fetch the language and country details and determine which DCB platform is applicable in each case.


Finally, the app serves a customized WebView page that prompts the victim to enter their phone number, supposedly receive a temporary OTP (one-time passcode) code to activate the account on the application.



![Requesting the victim's phone number via a customized page](https://www.bleepstatic.com/images/news/u/1220909/Android%20malware/phone-number.jpg)**Requesting the victim's phone number via a customized page**  
*Source: Zimperium*
Apps and targets
----------------


With 470 applications to distribute the malware, the targeted demographics was quite diverse. Most of these apps fell in the broader and more popular “Entertainment” category.


Other prevalent Dark Herring apps were photography tools, casual games, utilities, and productivity apps.


One key factor in the consequences of the Dark Herring operation is the absence of DCB consumer protection laws, so some countries were targeted more zestfully than others.


Those at greater risk were India, Pakistan, Saudi Arabia, Egypt, Greece, Finland, Sweden, Norway, Bulgaria, Iraq, and Tunisia.



![Victimization likelihood heatmap](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Victimization likelihood heatmap**  
*Source: Zimperium*
Even in countries where strict DCB protection rules apply, if the victims are late to realize the fraud, reverting the transactions may be impossible.


The most popular Dark Herring apps that each counts several million downloads are:


* Smashex
* Upgradem
* Stream HD
* Vidly Vibe
* Cast It
* My Translator Pro
* New Mobile Games
* StreamCast Pro
* Ultra Stream
* Photograph Labs Pro
* VideoProj Lab
* Drive Simulator
* Speedy Cars – Final Lap
* Football Legends
* Football HERO 2021
* Grand Mafia Auto
* Offroad Jeep Simulator
* Smashex Pro
* Racing City
* Connectool
* City Bus Simulator 2

To access the entire list of all 470 malicious Android applications, check out [this GitHub page](https://github.com/Zimperium/DarkHerring/blob/master/packagenames.md).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Derusbi]] [[action.malware.name=Elise]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Entertainment]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Egypt]] [[victim.continent.name=Africa]] [[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Tunisia]] [[victim.continent.name=Africa]] [[victim.city.name=Tunis]] [[victim.country.name=Tunisia]] [[victim.continent.name=Africa]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=Iraq]] [[victim.continent.name=Asia]] [[victim.country.name=Pakistan]] [[victim.continent.name=Asia]] [[victim.country.name=Saudi Arabia]] [[victim.continent.name=Asia]] [[victim.country.name=Bulgaria]] [[victim.continent.name=Europe]] [[victim.country.name=Finland]] [[victim.continent.name=Europe]] [[victim.country.name=Greece]] [[victim.continent.name=Europe]] [[victim.country.name=Norway]] [[victim.continent.name=Europe]] [[victim.country.name=Sweden]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Apps]] [[Android]] [[‘dark]] [[Google]] [[Zimperium]] [[Malware]] [[First-stage]] [[Bleeping Computer]]

