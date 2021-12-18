# Malicious Joker App Scores Half-Million Downloads on Google Play
### Joker malware was found lurking in the Color Message app, ready to fleece unsuspecting users with premium SMS charges.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177139
+ Date: 2021-12-17T19:23:09+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/17141527/joker3-e1639768541455.jpg)

The Joker malware is back again on Google Play, this time spotted in a mobile application called Color Message. The app was downloaded more than 500,000 times before its removal from the store.


Users should immediately delete Color Message from their devices to avoid being defrauded, researchers at Pradeo Security warned.


Joker is a persistent threat that’s been kicking around since 2017, hiding itself within legitimate-seeming, common application types like games, messengers, photo editors, translators and wallpapers, many of them aimed at children. But once installed, Joker apps subscribe victims to unwanted, paid premium services controlled by the attackers – a type of billing fraud that researchers [categorize as “fleeceware.”](https://threatpost.com/fleeceware-apps-from-google-play/151927/) Often, the victim is none the wiser until the mobile bill arrives.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


In the worst cases, the apps also exfiltrate contact lists and device information and can hide their icons from the home screen – which is the case with Color Message, Pradeo researchers said, adding that the application appeared to be making connections to Russian servers.


Color Message purported to offer the ability to jazz up messaging with a range of fun emojis and screen overlays.


“It makes texting easy, fun and beautiful,” according to its Google Play listing, captured by Pradeo before the takedown. “Customize the theme quickly. The Color Message application has unique technology that can help you personalize your default SMS messenger.”


Interestingly, it also had 1,800+ reviews, with an average rating of four stars – though the more recent reviews tended towards the scathing, such as “misleading ad and worst app ever.”


“The application’s very concise terms and conditions are hosted on an unbranded one-page blog and do not disclose the extent of the actions the app can perform on users’ devices,” according to the Pradeo [writeup](https://blog.pradeo.com/pradeo-identifies-app-joker-malware-google-play). “One of the victims has even tried reaching out to the application’s developer through the comment section of the legal page, other users are directly complaining about the fraud in the comment section of the app on the store.”


**Joker, an Evergreen Malware Threat**
--------------------------------------


Malicious Joker apps are commonly found outside of the official Google Play store, but they’ve continued to [skirt Google Play’s protections](https://threatpost.com/joker-androids-malware-ramps-volume/151785/). One of the ways Joker does this is through lightweight development and constant code tinkering.


“By using as little code as possible and thoroughly hiding it, Joker generates a very discreet footprint that can be tricky to detect,” according to Pradeo.


The most recent version of the malware also takes advantage of a legitimate developer tool called Flutter to evade both device-based security and app-store protections, Zimperium recently found. Flutter is an open-source app development kit designed by Google that allows developers to craft native apps for mobile, web and desktop from a single codebase. The use of Flutter to code mobile applications is a common approach, and one that traditional scanners see as benign, researchers said.


“Due to the commonality of Flutter, even malicious application code will look legitimate and clean, whereas many scanners are looking for disjointed code with errors or improper assemblies,” explained Zimperium researchers in [an analysis](https://threatpost.com/updated-joker-malware-android-apps/167776/) published in July.


As a result of all the trickery, there have been [periodic reinfestations](https://threatpost.com/joker-androids-malware-ramps-volume/151785/) of Joker inside the official store, including two [massive onslaughts](https://threatpost.com/joker-trojans-android/159595/) last year. According to researchers at Zimperium, more than 1,800 Android applications infected with Joker have been removed from the Google Play store in the last four years.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Bread]] [[action.malware.name=Conti]] [[action.malware.name=Derusbi]] [[action.malware.name=Elise]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Google]] [[Pradeo]] [[Apps]] [[Zimperium]] [[ThreatPost]]

