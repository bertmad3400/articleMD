# GriftHorse Money-Stealing Trojan Takes 10M Android Users for a Ride
### The mobile malware has fleeced hundreds of millions of dollars from victims globally, using sophisticated techniques.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175130)
+ Date: September 29, 2021  2:08 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/29134813/horseandmoney-e1632937726788.jpg)
More than 10 million Android users have been saddled with a malware called GriftHorse that’s trojanizing various applications and secretly subscribing victims to premium mobile services – a type of billing fraud that researchers categorize as “fleeceware.”


Zimperium uncovered more than 130 GriftHorse apps being distributed through both Google Play and third-party application stores, across all categories. Some of them have basic functionality, and some of them do nothing, researchers said. In either case, once installed, they lead to victims being billed for premium services – but phone-owners are usually none the wiser until they take a look at their mobile bills.


GriftHorse rode onto the scene in November of last year, and by now, “the total amount stolen could be well into the hundreds of millions of Euros,” according to Zimperium researchers, with each victim paying upwards of $40 per month.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Victims sprawl across 70 different countries, all packing sneaky extra charges that they may not be aware of. Google removed the flagged apps, but GriftHorse is far from corralled: There could be additional Play apps, installs could still be active on peoples’ phones, and the apps remain in many unofficial stores.


If users are unlucky enough to download one of the apps, they’ll find themselves “bombarded with alerts on the screen letting them know they had won a prize and need to claim it immediately,” according to Zimperium’s [Wednesday analysis](https://blog.zimperium.com/grifthorse-android-trojan-steals-millions-from-over-10-million-victims-globally/). “These pop ups reappear no less than five times per hour until the application user successfully accepts the offer.”


This is where it gets sneaky: Upon accepting the invitation for the prize, the malware serves victims selective pages, based on the geolocation of their IP addresses, using the local language and targeted verbiage. Those pages are also dynamically generated to avoid the blacklisting of strings by security solutions.


“These cybercriminals took great care not to get caught by malware researchers by avoiding hardcoding URLs or reusing the same domains, and filtering/serving the malicious payload based on the originating IP address’s geolocation,” according to the researchers. “This method allowed the attackers to target different countries in different ways. This check on the server-side evades dynamic analysis checking for network communication and behaviors.”


The redirect page asks targets to submit their phone numbers for “verification.” In reality, typing in the numbers merely subscribes them to a premium SMS service that charges $42 on average per month (€36), which will show up on their phone bills.


**Looking GriftHorse in the Mouth**
-----------------------------------


The creators of the apps have employed several novel techniques to help the apps stay off the radar of security vendors, the analysis found. In addition to the no-reuse policy for URLs mentioned above, the cybercriminals are also developing the apps using Apache Cordova.


Cordova allows developers to use standard web technologies – HTML5, CSS3 and JavaScript – for cross-platform mobile development – which in turn allows them to push out updates to apps without requiring user interaction.


“[This] technology can be abused to host the malicious code on the server and develop an application that executes this code in real-time,” according to Zimperium. “The application displays as a web page that references HTML, CSS, JavaScript and images.”


The campaign is also supported with a sophisticated architecture and plenty of encryption, which makes detection more difficult, according to the researchers.


For instance, when an app is launched, the encrypted files stored in the “assets/www” folder are decrypted using AES. After a bit more unpacking, the core functionality source code uses the GetData() function to establish communication between the application and a first-stage command-and-control (C2) server by encrypting an HTTP POST request.


The app then receives an encrypted response, which is decrypted using AES to collect a second-stage C2 URL. It also executes a GET request using Cordova’s “InAppBrowser” function to uncover a third-stage URL, and it starts pushing user notifications about the supposed “prize” once an hour, five times in a row, according to the analysis.


“The second-stage C2 domain is always the same irrespective of the application or the geolocation of the victim,” researchers explained. “The third-stage URL displays the final page asking for the victim’s phone number and subscribes to several paid services and premium subscriptions.”


JavaScript code embedded in the page is responsible for the malicious behavior of the application, researchers added: “The interaction between the WebPage and the in-app functions is facilitated by the JavaScript Interface, which allows JavaScript code inside a WebView to trigger actions in the native (application-level) code. This can include the collection of data about the device, including IMEI and IMSI among others.”


**Android Fleeceware Continues to Plague Users**
------------------------------------------------


GriftHorse is not the only malware that looks to defraud victims via trojanized apps. The well-documented [Joker malware](https://threatpost.com/updated-joker-malware-android-apps/167776/), for example, has been circulating since 2017, disguising itself within hundreds of common, legitimate apps like camera apps, games, messengers, photo editors, translators and wallpapers.


Once installed, Joker silently simulates clicks and intercepts SMS messages to – you guessed it – subscribe victims to unwanted, paid premium services controlled by the attackers. The apps also steal SMS messages, contact lists and device information.


GriftHorse takes a slightly different approach than Joker, but Zimperium warned that it’s just as virulent.


“The threat actors have exerted substantial effort to maximize their presence in the Android ecosystem through a large number of applications, developer accounts and domains,” they said. “The GriftHorse campaign is one of the most widespread campaigns the zLabs threat research team has witnessed in 2021. The cybercriminal group behind the GriftHorse campaign has built a stable cash flow of illicit funds from these victims, generating millions in recurring revenue each month with the total amount stolen potentially well into the hundreds of millions.”


**Detected GriftHorse Apps**
----------------------------


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[GriftHorse]] [[apps]] [[“The]] [[JavaScript]] [[malware]] [[apps,]] [[Android]] [[Zimperium]] [[SMS]] [[ThreatPost]]
