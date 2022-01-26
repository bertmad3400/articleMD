# Threat Actors Blanket Androids with Flubot, Teabot Campaigns
### Attackers are getting creative, using smishing & a malicious Google Play QR reader to plant banking trojans on the phones of victims across the globe.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177991
+ Date: 2022-01-26T14:02:07+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/01112340/androids-e1633101831352.jpeg)

Researchers have discovered a raft of active campaigns delivering the Flubot and Teabot trojans through a variety of delivery methods, with threat actors using smishing and malicious Google Play apps to target victims with fly-by attacks in various regions across the globe.


Researchers from Bitdefender Labs said they have intercepted more than 100,000 malicious SMS messages trying to distribute Flubot malware since the beginning of December, according to a [report](https://www.bitdefender.com/blog/labs/new-flubot-and-teabot-global-malware-campaigns-discovered) published Wednesday.


During their observation of Flubot, the team also discovered a QR code-reader app that’s been downloaded more than 100,000 times from the Google Play store and which has delivered 17 different Teabot variants, they said.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

Flubot and Teabot emerged on the scene last year as relatively straightforward banking trojans that steal banking, contact, SMS and other types of private data from infected devices. However, the operators behind them have unique methods for spreading the malware, making them particularly nasty and far-reaching.


**Changing It Up**
------------------


Flubot was first [discovered in April](https://threatpost.com/flubot-spyware-android-devices/165607/) targeting Android users in the United Kingdom and Europe using malicious SMS messages that prompted recipients to install a “missed package delivery” app, demonstrating a feature of the malware that lets attackers use command-and-control (C2) to send messages to victims.


This feature allows operators to quickly change targets and other malware features on the fly, widening their attack surface to a global scale without needing complex infrastructure. Indeed, campaigns later in the year targeted Android users in [New Zealand](https://threatpost.com/flubot-malware-targets-androids-with-fake-security-updates/175276/) and [Finland](https://threatpost.com/finland-flubot-text-messages/176649/).


“These threats survive because they come in waves with different messages and in different time zones,” Bitdefender researchers wrote in the report. “While the malware itself remains pretty static, the message used to carry it, the domains that host the droppers, and everything else is constantly changing.”


This global fly-by aspect of the threat actors behind the trojans is evident in the most recent Flubot campaigns researchers observed, they said, with operators targeting different geographic zones for short periods of time – sometimes just for a few days, they wrote.


“For example, in the month between Dec. 1 of last year and Jan. 2 of this year, the malware was highly active in Australia, Germany, Spain, Italy and a few other European countries,” researchers wrote.


Campaigns between Jan. 15 and Jan. 18 then shifted to other parts of the globe, including Romania, Poland, the Netherlands, Spain and even Thailand, they found.


**Same Malware, Some New Tricks**
---------------------------------


Attackers also branched out beyond trying to trick users into thinking they missed a package delivery – what Bitdefender dubbed “fake courier messages” – to distribute Flubot.


Though this tactic was present in nearly 52 percent of campaigns researchers observed, they also used a scam dubbed “is this you in this video” that is a take-off of a credential-stealing campaign that’s been circulating relentlessly on social media in about 25 percent of observed campaigns, researchers wrote.


The original “is this you” video scam has been distributed mainly on Facebook Messenger for a couple of years, with users receiving a message from a friend in their list with a question, “Is this you in this video?” or some variation, along with a link, they explained.


“When the victim clicks on the link, it usually redirects them to a fake Facebook login that gives attackers direct access to credentials,” researchers explained.


Flubot operators have picked up on this trick and are using a variation of it in one of the smishing campaigns observed, with users receiving an SMS message that asks, “Is this you in this video?” researchers wrote.


But the goal of the campaign is the same: to somehow mislead users into installing the software under some pretext, they wrote. However, in the Flubot version, the message tells them that Flash or some Android component actually needs an upgrade after they’ve opened the link informing them they could be in a video, they explained.


“This new vector for banking trojans shows that attackers are looking to expand past the regular malicious SMS messages,” researchers noted.


Among other lures, Flubot operators also used SMS messages employing fake browser updates and fake voicemail notifications in about 8 percent of observed campaigns, respectively, researchers said.


**QR Reader Drops Teabot Variants**
-----------------------------------


While investigating Flubot, researchers also discovered a Teabot variant being installed on devices without a malicious SMS being sent, they said. Further investigation revealed a dropper application in Google Play Store named the “QR Code Reader – Scanner App” that’s been distributing 17 different Teabot variants for a little over a month, researchers said.


The application itself is not malicious, and the malicious code within the app has a minimal footprint, they observed. However, the app follows a rather curious path after installation in how it executes Teabot on a device that gives operators an unusual range of control over the payload, researchers said.


“When the user starts the Android app, it also starts a background service that checks the country code of the current registered operator (or the cell nearby),” they wrote. “If the country starts with a ‘U’ or is unavailable, the app skips executing the malicious code, which means that countries like Ukraine, Uzbekistan, Uruguay and the U.S. are skipped.”


If the app passes the check, it retrieves the context of a settings file from a GitHub address that includes a different github repository file link pointing to the actual payload to download.


“This settings file, from the QR Code Reader repository, has the URL changed whenever a different payload URL is needed or even removed if the authors wish to deactivate the malicious behavior temporarily,” researchers explained.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Agriculture]] [[victim.industry.name=Finance]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Oman]] [[victim.continent.name=Asia]] [[victim.country.name=Thailand]] [[victim.continent.name=Asia]] [[victim.country.name=Uzbekistan]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=Finland]] [[victim.continent.name=Europe]] [[victim.country.name=Germany]] [[victim.continent.name=Europe]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.country.name=Netherlands]] [[victim.continent.name=Europe]] [[victim.country.name=Poland]] [[victim.continent.name=Europe]] [[victim.country.name=Romania]] [[victim.continent.name=Europe]] [[victim.country.name=Spain]] [[victim.continent.name=Europe]] [[victim.country.name=Ukraine]] [[victim.continent.name=Europe]] [[victim.country.name=United Kingdom]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Uruguay]] [[victim.continent.name=South America]] [[victim.country.name=Australia]] [[victim.continent.name=Oceania]] [[victim.country.name=New Zealand]] [[victim.continent.name=Oceania]] [[victim.country.name=Australia]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Flubot]] [[Teabot]] [[Sms]] [[Malware]] [[Android]] [[Google]] [[Bitdefender]] [[ThreatPost]]

