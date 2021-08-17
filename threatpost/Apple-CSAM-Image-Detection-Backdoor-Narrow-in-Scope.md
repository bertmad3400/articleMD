# Apple: CSAM Image-Detection Backdoor ‘Narrow’ in Scope
### Computing giant tries to reassure users that the tool won’t be used for mass surveillance.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168727)
+ Date: August 17, 2021  9:58 am
+ Author: Becky Bracken


## Article:
![apple](https://media.threatpost.com/wp-content/uploads/sites/103/2020/07/01143018/Mac-Malware.jpg)
Apple provided additional [design and security details](https://www.apple.com/child-safety/pdf/Security_Threat_Model_Review_of_Apple_Child_Safety_Features.pdf) this week about the planned rollout of a feature aimed at detecting child sexual abuse material (CSAM) images stored in iCloud Photos.


Privacy groups like the Electronic Frontier Foundation warned that the process of flagging CSAM images essentially [narrows the definition of end-to-end encryption](https://www.eff.org/deeplinks/2021/08/if-you-build-it-they-will-come-apple-has-opened-backdoor-increased-surveillance) to allow client-side access — which essentially means Apple is building a backdoor into its data storage, it said.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“Apple can explain at length how its technical implementation will preserve privacy and security in its proposed backdoor, but at the end of the day, even a thoroughly documented, carefully thought-out, and narrowly scoped backdoor is still a backdoor,” The EFF said in [reaction to the Apple announcement](https://www.eff.org/deeplinks/2021/08/apples-plan-think-different-about-encryption-opens-backdoor-your-private-life).


Apple’s new document explained that the tool is only available to child accounts set up in Family Sharing and the parent or guardian must opt-in. Then, a machine-learning classifier is deployed to the device in the messaging app, which will trigger a warning if the app detects explicit images being sent to or from the account. If the account is for a child under 13 years old, the parent or guardian will also receive a notification, according to Apple.  The image is not shared with the parent, only a notification, Apple added.


**Apple Explains How It Protects Privacy While Monitoring CSAM Content**
------------------------------------------------------------------------


“This feature does not reveal information to Apple,” the company said. “Specifically, it does not disclose the communications of the users, the actions of the child or the notifications to the parents. It does not compare images to any database, such as a database of CSAM material. It never generates any reports for Apple or law enforcement.”


The feature also detects collections of CSAM images uploaded to iCloud photos, Apple said. First it runs code on the device that compares any photo being uploaded to a known database of CSAM images.


“The iCloud photo servers can decrypt the safety vouchers corresponding to positive matches — if and only if that user’s iCloud Photos account exceeds a certain number of matches, called the match threshold,” Apple added.


After a certain number of images is detected, the images are sent to a human reviewer and if an issue is detected, the information is turned over to the National Center for Missing and Exploited Children who will notify law enforcement as necessary.


“The system is designed so that a user need not trust Apple, any other single entity, or even any set of possibly colluding entities from the same sovereign jurisdiction (that is, under the control of the same government) to be confident that the system is functioning as advertised,” Apple said.


First, Apple said it generated a CSAM device database by combining information from two separate child-safety agencies.


“Any perceptual hashes appearing in only one participating child-safety organization’s database, or only in databases from multiple agencies in a single sovereign jurisdiction, are discarded by this process, and not included in the encrypted CSAM database that Apple includes in the operating system,” Apple’s document explained. “This mechanism meets our source-image correctness requirement.”


The company added that the database is never updated or shared over the internet.


“Since no remote updates of the database are possible, and since Apple distributes the same signed operating system image to all users worldwide, it is not possible – inadvertently or through coercion – for Apple to provide targeted users with a different CSAM database,” the company explained. “This meets our database update transparency and database universality requirements.”


Apple added that it will publish a Knowledge Base article with a root hash of the encrypted database with each iOS update, to allow for independent third-party technical audits.


It’s unclear how any of these details will reassure critics of the move.


“While Apple aims at the scourge of child exploitation and abuse, the company has created an infrastructure that is all too easy to redirect to greater surveillance and censorship,” the EFF said in response. “The program will undermine Apple’s defense that it can’t comply with the broader demands.”


**Worried about where the next attack is coming from? We’ve got your back.**[**REGISTER NOW**](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**for our upcoming live webinar,**[**How to Think Like a Threat Actor**](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**, in partnership with Uptycs. Find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on Aug. 17 at 11AM EST for this**[**LIVE**](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**discussion.**


 




#### Tags:
[[CSAM]] [[iCloud]] [[said.]] [[Apple’s]] [[“This]] [[“The]] [[ThreatPost]]
