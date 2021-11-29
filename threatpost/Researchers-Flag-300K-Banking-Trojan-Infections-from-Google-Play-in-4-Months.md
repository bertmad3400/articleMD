# Researchers Flag 300K Banking Trojan Infections from Google Play in 4 Months
### Attackers are honing Google Play dropper campaigns, overcoming app store restrictions.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176630)
+ Date: November 29, 2021  4:15 pm
+ Author: Becky Bracken


## Article:
![google play bug bounty](https://media.threatpost.com/wp-content/uploads/sites/103/2019/08/29094752/google-play.jpeg)
Overcoming Google Play app restrictions, attackers have successfully racked up more than 300,000 banking trojan installations over just the past four months in the official Android app marketplace.


Researchers from Threat Fabric reported that these threat groups have [honed their ability to use Google Play](https://www.threatfabric.com/blogs/deceive-the-heavens-to-cross-the-sea.html) to propagate banking trojans by shrinking the footprint of their dropper apps, eliminating the number of permissions they ask for, boosting the overall quality of the attack with better code and standing up convincing companion websites.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Droppers are apps that act as first-stage implants, whose job it is to fetch and install other, final payloads — in this case, banking trojans. The report offered the example of cyberattackers’ ingenuity in sneaking these onto Google Play: A dropper app disguised as a fitness service with an actual functioning back-end site to match.


“To make themselves even more difficult to detect, the actors behind these dropper apps only manually activate the installation of the banking trojan on an infected device in case they desire more victims in a specific region of the world,” the Threat Fabric researchers added. “This makes automated detection a much harder strategy to adopt by any organization.”


All 300,000 [banking-trojan](https://threatpost.com/mekotio-banking-trojan-campaign/175981/) dropper installations came from four malware families, according to the report: Anatsa (200,000+ installs); Alien (95,000+) and Hydra/Ermac (15,000+).


**Anasta Installs**
-------------------


Anasta threat actors were first observed by Threat Fabric using [Google Play malware dropper apps](https://threatpost.com/google-play-malware-spy-trojans/164601/) in Jan. 2021, the report said. The Anasta banking trojan does it all — credential theft, keylogging and even captures what’s shown on a user’s screen. The analysts found six separate droppers in Google Play that lead to Anasta infections, including scam QR code scammers, PDF scanners and cryptocurrency apps, collectively reaching more than 100,000 installations, they reported.


Once the app is downloaded and installed from Google Play, to continue, the user must allow an update, which is instead the Anatsa malware.


“Actors behind it took care in making their apps look legitimate and useful,” the analysts said. “There are large numbers of positive reviews for the apps. The number of installations and presence of reviews may convince Android users to install the app. Moreover, these apps indeed possess the claimed functionality, after installation they do operate normally and further convince victim in their legitimacy.”


**Hydra, Ermac and Alien Installs**
-----------------------------------


Threat group Brunhilda was observed using a fake QR-code app to distribute both Hydra and Ermac malware families, the report added.


And, a dropper app called “GymDrop” used “exercise update” messages to trick victims into downloading the Alien banking trojan.


“The Alien samples of this campaign connect to the same C2 as samples from previously described campaign powered by Brunhilda dropper,” the report said.


As these groups evolve, they’ve been able to develop an effective work around automated and machine learning detection, the report explained.


As [Google Play](https://threatpost.com/google-play-covert-location-tracking/169151/) continues to be reactive in its approach to weeding out these malicious actors, there’s a limit to the amount of protection that can be provided to users, John Bambenek, principal threat hunter at Netenrich told Threatpost.


“There is only so much protection you can have when app stores are inherently reactive in detecting abusive apps,” Bambenek said. “The same benefit application developers have in choosing the Android ecosystem are the same benefits criminals are going to use.”


***There’s a sea of unstructured data on the internet relating to the latest security threats.***[***REGISTER TODAY***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This***[***LIVE, interactive Threatpost Town Hall***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***, sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)**for the LIVE event!**


 


 




#### Tags:
[[Google]] [[apps]] [[Anasta]] [[said.]] [[Android]] [[malware]] [[ThreatPost]]
