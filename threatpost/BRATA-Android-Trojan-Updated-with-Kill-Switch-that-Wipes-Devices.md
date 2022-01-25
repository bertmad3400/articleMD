# BRATA Android Trojan Updated with ‘Kill Switch’ that Wipes Devices
### Researchers identify three new versions of the banking trojan that include various new features, including GPS tracking and novel obfuscation techniques.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177921
+ Date: 2022-01-25T13:56:19+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/24121603/android-e1637774177513.jpg)

New variants of the BRATA banking trojan have been targeting global Android devices since November with advanced features, including the ability to wipe devices after stealing user data, tracking devices via GPS, and novel obfuscation techniques, researchers have found.


The remote access trojan (RAT), which targets banks and financial institutions, is now being distributed through a downloader to avoid being detected by antivirus (AV) solutions, researchers from fraud-management firm Cleafy wrote in [a report](https://www.cleafy.com/cleafy-labs/how-brata-is-monitoring-your-bank-account) published Monday. The malware is currently targeting banks and financial institutions in Italy, Latin America, Poland and the United Kingdom, they said.


Researchers from Kaspersky [discovered BRATA](https://securelist.com/spying-android-rat-from-brazil-brata/92775/) in January 2019, proliferating via the Google Play store and initially targeting users in Brazil. The RAT featured the [unique capability](https://threatpost.com/brata-android-rat-steals-banking-info/148003/) of collecting and relaying banking info to its operators in real time.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Since then, the actors behind the RAT have continued to target financial institutions and add new capabilities to the malware. The Cleafy team has identified three new variants of BRATA that have been delivered via two new waves of samples in the last few months, researchers reported.


“The first wave started in November 2021, and the second around mid-December 2021,” researchers wrote. “During the second wave, [threat actors] began to deliver a few new tailored variants of BRATA in different countries.”


**New Variants, Wiper Capabilities**
------------------------------------


The most prevalent of the variants observed by researchers is BRATA.A, which has two key new features, researchers reported. One is GPS tracking of victim devices, a capability that “appears to be still under development,” researchers wrote. The RAT requests permission to use GPS at installation, but does not appear to actually use it during execution, they said.


“For this reason, we could just guess that malware developers are requesting this permission for future development, most likely to target people that belong to specific countries or to enable other cash-out mechanisms (e.g. cardless ATMs),” they wrote.


BRATA.A also features a “kill switch” that serves to perform a factory reset of the device in two scenarios, researchers said.


The first is after a bank fraud has been completed successfully, they said. “In this way, the victim is going to lose even more time before understanding that a malicious action happened,” researchers wrote.


The second case in which BRATA wipes a device is when the application is installed in a virtual environment, as the RAT “tries to prevent dynamic analysis through the execution of this feature,” researchers wrote.


The second new variant observed by the team, BRATA.B, is nearly identical to the A variant except for “particular obfuscation of the code and the use of tailored overlay pages used to steal the security number (or PIN) of the targeted banking application, according to Cleafy.


**Avoiding Detection**
----------------------


BRATA.C is the third new variant and shows evolution in the method its operators use to avoid the RAT being detected upon installation by users.


The variant uses an initial dropper to download and execute the “real” malicious app later, demonstrating a unique way that deviates from how other Android banking trojans actors try to evade detection by AV solutions, researchers wrote.


“Although the majority of Android banking trojans try to obfuscate/encrypt the malware core in an external file (eg. *.*DEX or .JAR), BRATA uses a minimal app to download in a second step the core BRATA app (*.*APK),” they explained in the post.


After the victim installs the downloader app, it requires the acceptance of just one permission to download and install the malicious application from an untrusted source, researchers said.


“When the victim clicks on the install button, the downloader app sends a GET request to the command-and-control (C2) server to download the malicious .APK,” they explained. “At this point, the victim has two malicious apps installed on their device.”


Overall, Cleafy’s latest findings demonstrate that BRATA operators aim to expand their regional scope of targets as well as plan to evolve the malware further, with little sign of letting up in the near future, researchers said.


“We can expect BRATA to keep staying undetected and to keep developing new features,” they wrote.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Expand]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]] [[action.malware.name=Wiper]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Finance]] [[victim.industry.name=Manufacturing]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.country.name=Poland]] [[victim.continent.name=Europe]] [[victim.country.name=United Kingdom]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Brazil]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Brata]] [[Malware]] [[Cleafy]] [[Android]] [[Downloader]] [[ThreatPost]]

