# That Toy You Got for Christmas Could Be Spying on You
### Security flaws in the recently released Fisher-Price Chatter Bluetooth telephone can allow nearby attackers to spy on calls or communicate with children using the device.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177288
+ Date: 2021-12-28T16:31:41+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/28111824/chatter-e1640708531855.jpeg)

Many adults found it charming when Mattel [upgraded](https://www.amazon.com/Fisher-Price-Chatter-Phone-Bluetooth-Grownups/dp/B09MFY7GJ2) its classic Fisher-Price Chatter telephone for its 60th anniversary in October with actual Bluetooth capabilities, so grownups, too, can use it — and for actual mobile phone calls.


But flaws in the way [the toy](https://www.mattel.com/en-shop/products/fisher-price-chatter-telephone-fgw66) pairs with Bluetooth means that other people with nefarious intentions can potentially be listening in on private conversations, researchers have found.


A team at Pen Test Partners [revealed](https://www.pentestpartners.com/security-blog/audio-bugging-with-the-fisher-price-chatter-bluetooth-telephone/) earlier this month that the implementation of Bluetooth used in the device has no secure pairing process, allowing for audio bugging by anyone nearby when someone is using Chatter to talk on the phone, they said.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“When powered on, it just connects to any Bluetooth device in range that requests to pair,” allowing for “audio bugging of both children and adults” in some cases, researchers wrote.


The idea is that someone nearby — i.e., a neighbor living in a nearby house or apartment, or even someone on the street outside — could connect his or her own Bluetooth audio device to Chatter and spy on someone.


And even though the Bluetooth version of the toy was marketed for adults, researchers theorized that parents might pass it on to kids when they tire of it, researchers said. This means that someone with bad intentions could make contact with a child inside his or her own home, paving the way for child predator scenarios.


**Similar Flaw in Another Toy**
-------------------------------


The bug in Fisher-Price Chatter with Bluetooth is similar to [a problem with a children’s toy called My Friend Cayla](https://www.pentestpartners.com/security-blog/making-childrens-toys-swear/) — which is both a child’s doll and a Bluetooth headset — that a researchers from Pen Test Partners also identified.


In Cayla, [a vulnerability](https://threatpost.com/serious-security-flaws-found-in-childrens-connected-toys/151020/) in the Bluetooth implementation allowed an attacker within Bluetooth range to connect a Bluetooth audio device (e.g., a smartphone) and listen to the doll’s microphone, or speak through its speaker to a child playing with the doll.


Chatter’s Bluetooth issue makes it a bit more difficult for an attacker to access in that the audio is not enabled until someone lifts the handset or presses the speakerphone button, researchers said. However, they “do not think this sufficiently mitigates the problem” for two reasons, according to the post.


One is that if the Chatter telephone is powered on but the handset is left knocked off — as is quite possible if a child has played with it — the Chatter phone will auto-answer any incoming phone call to the connected smartphone, researchers said. This results in the phone becoming an audio bug with no interaction from child or parent.


The other is that the Chatter telephone will ring if the attached smartphone rings. This means that an attacker can simply use two phones–one to pair with the Chatter phone and a second to call the first phone—to establish two-way audio if a child answers the Chatter phone, researchers said.


“We don’t think this is acceptable,” researchers wrote, especially since the previously identified problem in the Cayla doll led to widespread concern from consumer protection groups such as the Norwegian Consumer Council (Forbrukerrådet) and product bans across several countries led by Germany’s Federal Network Agency (Bundesnetzagentur), they said.


Pen Test Partners are calling for Mattel — which so far has not commented on Chatter’s security issue — to fix the problem. The company did not immediately respond to request for comment by Threatpost on Tuesday.


“How have Fisher-Price not learned from similar security issues exposed in children’s toys several years ago?” researchers wrote. “An improved pairing process might involve an additional button press to force the device into a mode that allows pairing.”


**How to Prevent Chatter Telephone Spying**
-------------------------------------------


Researchers outlined in the post how people can test to see if their particular Chatter phone is vulnerable to the issue. They also provided mitigations for any parent concerned with potential use of the Chatter phone for spying on them or communicating with their children.


People who have the Bluetooth version of Chatter should ensure it is powered off when not explicitly in use, and parents should supervise their child’s use of the phone.


Since only one Bluetooth phone can connect to the Chatter telephone at a time, an attacker can’t connect a rogue phone if a legitimate phone is connected. Therefore, people should not leave the Chatter telephone powered on if they leave their home with the smartphone that is connected to the Chatter telephone, researchers advised.


Also, because the audio functions of the Chatter telephone will only allow bugging if the handset is picked up or knocked off, or the speakerphone button is pressed, adults should ensure that the handset is always replaced and the phone is turned off, according to Pen Test Partners.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=RTM]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Germany]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Bluetooth]] [[Fisher-price]] [[Cayla]] [[Smartphone]] [[ThreatPost]]

