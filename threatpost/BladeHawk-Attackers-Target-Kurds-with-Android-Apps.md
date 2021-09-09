# BladeHawk Attackers Target Kurds with Android Apps
### Pro-Kurd Facebook profiles deliver ‘888 RAT’ and ‘SpyNote’ trojans, masked as legitimate apps, to perform mobile espionage.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169300)
+ Date: September 9, 2021  7:26 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/09072544/kurds-e1631186756340.jpg)
Attackers have been targeting the Kurdish ethic group for more than a year through an Facebook-based spyware campaign that disguises backdoors in legitimate Android apps, researchers have found.


A group called BladeHawk is behind the campaign, discovered by researchers from cybersecurity firm ESET and active since at least March 2020, according to [a report](https://www.welivesecurity.com/2021/09/07/bladehawk-android-espionage-kurdish/?web_view=true) published this week. The campaign disguises the 888 RAT in Android apps using dedicated Facebook profiles, researchers aid.


“These profiles appeared to be providing Android news in Kurdish, and news for the Kurds’ supporters,” ESET malware researcher Lukas Stefanko wrote in the report, published Wednesday. “Some of the profiles deliberately spread additional spying apps to Facebook public groups with pro-Kurd content.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


All in all, researchers identified six profiles as part of the BladeHawk campaign, which have been sharing the Android spying apps and targeted about 11,000 followers through 28 unique posts. The profiles have been reported to Facebook and since disabled, Stefanko said.


Each of these posts in the campaign contained fake app descriptions and links to download an app, according to the post. Researches downloaded 17 unique Android application packages (APKs) from these links, some of which pointed directly to the malicious apps.


“Two of the profiles were aimed at tech users, while the other four posed as Kurd supporters,” he wrote. “All these profiles were created in 2020 and shortly after creation they started posting these fake apps. These accounts, except for one, have not posted any other content besides Android RATs masquerading as legitimate apps.”


Other links pointed to the third-party upload service top4top.io, which tracks the number of file downloads. Data from that service shows that there have been at least 1,481 downloads of the malicious apps from URLs promoted in just a few Facebook posts between July 20, 2020 and June 28 of this year, researchers found.


Attackers also shared espionage apps to public Facebook groups, most of which support of Masoud Barzani, the former president of the Kurdistan Region, Stefanko said.


**Payload Activity**
--------------------


The key payload of the campaign is the multiplatform 888 RAT, which previously was used in two other organized campaigns—one [targeting TikTok users](https://www.zscaler.com/blogs/security-research/tiktok-spyware) with [TikTok Pro spyware](https://threatpost.com/spyware-labeled-tiktok-pro-exploits-fears-of-us-ban/159050/) and another by the [Kasablanka group](https://blog.talosintelligence.com/2021/02/kasablanka-lodarat.html), according to ESET. In one instance, the campaign spread the SpyNote trojan, which is an [older and well-known](https://threatpost.com/new-trojan-spynote-installs-backdoor-on-android-devices/119560/) commercial spy tool that has a history of masquerading as legitimate apps, [including Netflix](https://threatpost.com/spynote-rat-now-disguised-as-netflix-app/123311/).


888 RAT originally only was published for the Windows ecosystem and sold on the Dark Web for $80. In June 2018, a Pro version of the RAT costing $150 extended its capability for Android, while an Extreme version released later and sold for $200 could create Linux-based payloads as well.


The 888 RAT used in the BladeHawk campaign includes the ability to: Steal and delete files from a device; take screenshots; get device location; get a list of installed apps; steal user photos; take photos; record surrounding audio and phone calls; make calls; steal SMS messages; steal the device’s contact list; and send text messages.


The RAT also can phish Facebook credentials by deploying activity that appears to be coming from the legitimate Facebook app, Stefanko wrote.


“When the user taps on the recent apps button, this activity will seem legitimate,” he wrote. “However, after a long press on this app’s icon, as in Figure 8, the true app name responsible for the Facebook login request is disclosed.”


ESET has published a list of file names, Facebook profiles and groups, and distribution and phishing links associated with the BladeHawk campaign in the post.


**It’s time to evolve threat hunting into a pursuit of adversaries.**[**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**Threatpost and Cybersixgill for**[**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**and get a guided tour of the dark web and learn how to track threat actors before their next attack.**[**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with independent researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**


 




#### Tags:
[[Facebook]] [[Android]] [[apps]] [[BladeHawk]] [[Stefanko]] [[ESET]] [[wrote.]] [[ThreatPost]]
