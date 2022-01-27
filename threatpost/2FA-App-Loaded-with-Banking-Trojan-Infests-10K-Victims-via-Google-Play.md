# 2FA App Loaded with Banking Trojan Infests 10K Victims via Google Play
### The Vultur trojan steals bank credentials but asks for permissions to do far more damage down the line.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178077
+ Date: 2022-01-27T20:59:53+00:00
+ Author: Becky Bracken


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/27155626/turkey-vulture-scaled-e1643317009313.jpeg)

After remaining available for more than two weeks, a malicious two-factor authentication (2FA) application has been removed from Google Play — but not before it was downloaded more than 10,000 times. The app, which is fully functional as a 2FA authenticator, comes loaded with the Vultur stealer malware that targets and swoops down on financial data.


Users with the malicious application, straightforwardly called “2FA Authenticator,” are advised by researchers at Pradeo to delete it from their device immediately since they still remain at risk — both from banking-login theft and other attacks made possible by the app’s extensive overpermissions.


The threat actors developed an operational and convincing application to disguise the [malware dropper,](https://blog.pradeo.com/vultur-malware-dropper-google-play) using open-source Aegis authentication code injected with malicious add-ons. That helped it spread via Google Play undetected, according to a Pradeo report released on Thursday.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“As a result, the application is successfully disguised as an authentication tool, which ensures it maintains a low profile,” the report added.


**Vultur Banking Trojan Gobbles Down Permissions**
--------------------------------------------------


Once downloaded, the app installs Vultur [banking trojan](https://threatpost.com/shipment-delivery-scams-a-fav-way-to-spread-malware/178050/), which steals financial and banking data on the compromised device — but can do much more.


First detected by analysts at ThreatFabric last March, the [Vultur remote access trojan (RAT) malware](https://www.threatfabric.com/blogs/vultur-v-for-vnc.html) was the first of its kind found to use keylogging and screen recording as its primary tactic for banking-data theft, enabling the group to automate the process of harvesting credentials and scale.


“The actors chose to steer away from the common HTML overlay strategy we usually see in other Android banking trojans: this approach usually requires more time and effort from the actors in order to steal relevant information from the user. Instead, they chose to simply record what is shown on the screen, effectively obtaining the same end result,” ThreatFabric said at the time.


The scam 2FA authenticator also asks for device permissions beyond what was disclosed in the Google Play profile, the Pradeo team said.


Those sneaky, elevated privileges allow the attackers to perform various functions beyond the standard banking-trojan fare, such as: Accessing user location data, so attacks can be targeted at specific regions; disabling the device lock and password security; downloading third-party applications; and taking over control of the device, even if the app is shut down, the report explained.


Pradeo uncovered another dirty trick the malicious 2FA pulled by grabbing the SYSTEM\_ALERT\_WINDOW permission, which gives the app the ability to change other mobile apps’ interfaces. As Google itself explained, “Very few apps should use this permission; these windows are intended for system-level interaction with the user.”


Once the device is fully compromised, the app installs Vultur, “an advanced and relatively new kind of malware that mostly targets online banking interface to steal users’ credentials and other critical financial information,” the report said.


The team at Pradeo reported that while the researchers submitted their disclosure to Google Play, nevertheless the malicious 2FA Authenticator app loaded with the [banking trojan](https://threatpost.com/brata-android-trojan-kill-switch-wipes/177921/) remained available for 15 days.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Google]] [[Pradeo]] [[2fa]] [[Malware]] [[ThreatPost]]

