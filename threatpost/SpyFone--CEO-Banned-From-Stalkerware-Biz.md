# SpyFone & CEO Banned From Stalkerware Biz
### The FTC’s first spyware ban nixes a company whose “slipshod” security practices led to exposure of thousands of victims’ illegally collected personal data. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169165)
+ Date: September 2, 2021  4:12 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/02153256/stalkerware.jpeg)
The Federal Trade Commission (FTC) has kicked spyware maker SpyFone out of the surveillance business.


The same goes for its CEO, Scott Zuckerman, and Support King LLC, the company behind the stalkerware.


In a Wednesday [announcement](https://www.ftc.gov/news-events/press-releases/2021/09/ftc-bans-spyfone-and-ceo-from-surveillance-business), the FTC slammed SpyFone, calling it a stalkerware app that sold real-time access to “stalkers and domestic abusers to stealthily track the potential targets of their violence.” It added that SpyFone also failed to provide even basic security, exposing device owners “to hackers, identity thieves, and other cyber threats.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The FTC also ordered SpyFone to delete its illegally harvested information and to notify owners that somebody had secretly slipped the app onto their devices.


The FTC’s statement quoted Samuel Levine, Acting Director of the FTC’s Bureau of Consumer Protection, who called SpyFone “a brazen brand name for a surveillance business that helped stalkers steal private information.


“The stalkerware was hidden from device owners, but was fully exposed to hackers who exploited the company’s slipshod security,” Levine said.


The FTC described SpyFone as “a stalkerware app that allowed purchasers to surreptitiously monitor photos, text messages, web histories, GPS locations, and other personal information of the phone on which the app was installed without the device owner’s knowledge.”


SpyFone Stalkers Have to Root Victims’ Phones
---------------------------------------------


In its complaint ([PDF](https://www.ftc.gov/system/files/documents/cases/192_3003_spyfone_complaint.pdf)), the FTC explained that in order to enable certain SpyFone functions, such as monitoring of email on targets’ Android devices, buyers of the SpyFone app had to root the phones, which could void warranties and expose the devices to security risks. The company provided instructions on how to hide the app so surveillance targets couldn’t sniff out the monitoring, the FTC alleged.


Ray Kelly, principal security engineer at app security provider NTT Application Security, observed to Threatpost on Thursday that, while rooting a device is common for Android users who want to sideload apps to avoid the Google Play store, once a phone’s rooted, “all bets are off as far as security goes for the user.”


SpyFone’s Slimy History
-----------------------


This creature has been fattening itself on victims and their stalkers’ money for quite a while: SpyFone first [crawled out of the muck](https://threatpost.com/spyphone-iphone-app-can-harvest-personal-data-120409/73211/) in 2009, released by a Swiss iPhone developer and capable of harvesting huge amounts of personal data from iPhones, including geolocation data, passwords, address book entries and email account information, all via nothing but the public API.


SpyFone sells various products. One is a basic Android version that – as is typical for stalkerware – has marketed itself as a way to (legally) monitor children or employees. As The Electronic Frontier Foundation (EFF) [explains,](https://www.eff.org/deeplinks/2020/07/coalition-against-stalkerware-expands-membership#breadcrumb) stalkerware apps are sold commercially, sometimes blatantly marketed as tools to “catch a cheating spouse” and sometimes posing as tools to track children’s or employees’ devices: both of which are legal. But what really defines stalkerware is that it’s designed to operate covertly, so the victim doesn’t know they’re being monitored.


SpyFone was sold on a subscription basis for $99.95/year and can capture and log, among other things, SMS messages; call history; GPS location and live location; web history; contacts; pictures; calendar; files downloaded on the device; and notifications.


According to the FTC’s complaint, it also gave buyers the ability to block apps, receive an app usage report, and also claimed it could spoof text messages so that the purchaser can send text messages that appear to be coming from the victim’s monitored device.


The premium version of SpyFone for Android, which costs $199.95 for a year subscription, added the ability to capture victims’ emails; video chats; and activity on or through apps, including posts made on social media, contents of messages sent and received, pictures shared on photo apps, and information exchanged on online dating apps. The SpyFone for Android Xtreme – marketed as the most popular product – added a keylogger and live screen viewing.


For $299.95/year, the Android Xtreme product also included the ability to remotely take pictures, record audio by turning on the device’s microphone, record calls, and send the mobile device commands through SMS, such as commands to vibrate or ring.


Until at least spring 2019, SpyFone was also selling a device that came preinstalled with a one-year subscription for Android Xtreme, starting at $495 – all the better to pass off as a (boobytrapped) “gift” without stalkers needing to get their hands on victims’ phones. Given that stalkerware isn’t allowed on Google Play store, buyers would need to download the stalkerware onto the target’s device, would have to strip the phones of safeguards that keep people from downloading apps from unknown sources, would need to give themselves admin control, and would have to disable notifications that would give the phone’s owner a heads-up that something wasn’t right on their devices – among other things.


Hank Schless, senior manager of security solutions at endpoint-to-cloud security company Lookout, observed to Threatpost that stalkerware like SpyFone demonstrates why we all need a security solution on our mobile devices, particularly given how much we trust them. “We assume these devices will act in our best interests, but in reality they’re even more vulnerable to cyberattacks and stalking than our computers,” he said via email on Thursday. “We all run security tools on our laptops and desktops, so why should our smartphones and tablets be any different? They store and have access to far more sensitive data than our computers, and in addition attackers have countless avenues to execute their malicious campaigns across countless mobile apps and vulnerabilities that exist.”


What Could Possibly Go Wrong?
-----------------------------


In August 2018 – the same year that SpyFone emerged – the company’s sadsack security led to terabytes worth of victims’ unencrypted camera photos [being exposed](https://www.vice.com/en/article/9kmj4v/spyware-company-spyfone-terabytes-data-exposed-online-leak). The security researcher who found the data – and who opted to remain anonymous at the time, due to fear of legal repercussions – discovered it on an unsecured Amazon S3 bucket belonging to SpyFone.


Besides personal photos, the researcher also found “at least 2,208 current ‘customers’ and hundreds or thousands of photos and audio in each folder,” he told Motherboard at the time: data belonging to what he said were 3,666 tracked phones.


NTT’s Kelly noted that the breach was a “double whammy”: it occurred “when SpyFone was breached to steal the information that they, themselves, were stealing from users,” he said in an email.


After the incident hit the headlines, SpyFone promised customers that it would work with an outside data security firm and law enforcement to investigate the incident – a promise that it failed to follow through on, the FTC alleged.


Specifically, the FTC alleged that, among the “reasonable precautions to safeguard” the information it illegally harvested, SpyFone’s security lapses included, among others, this list:


This is the second case the FTC has brought against stalkerware apps but the first in which it managed to get a ban.


Good Riddance to Bad Rubbish
----------------------------


One stalkerware app gone, so many still slithering around.


In February, Kaspersky researchers reported that the U.S. had earned the dubious honor of having moved into third place on the list of countries [most infected with stalkerware](https://threatpost.com/stalkerware-volumes-high-bans/164325/).


That means that thousands of mobile users were infected with stalkerware last year.


It could have been even worse, if not for COVID-19 putting a damper on installations, researchers found.


According to Kaspersky’s “The State of Stalkerware 2020” report, there were 53,870 mobile users within its telemetry who were affected by stalkerware during the year. That’s a drop from the year before, when [67,500 mobile users were affected](https://threatpost.com/stalkerware-attacks-increased-50-percent/153248/), but still up from the 40,386 instances detected among Kaspersky’s client base in 2018.


Thumbs-up From the EFF
----------------------


The EFF praised the FTC’s order. “With the FTC now turning its focus to this industry, victims of stalkerware can begin to find solace in the fact that regulators are beginning to take their concerns seriously,” EFF Senior Staff Technologist William Budington and Director of Cybersecurity Eva Galperin wrote in [a blog post](https://www.eff.org/deeplinks/2021/09/victory-federal-trade-commission-bans-stalkerware-company-conducting-business).


The FTC board voted 5-0 to accept the consent order with the company.


Support King, a Puerto Rico LLC doing business as SpyFone, has neither admitted nor denied the FTC’s allegations, according to the consent order agreement ([PDF](https://www.ftc.gov/system/files/documents/cases/192_3003_spyfone_agreement_and_order_without_signatures_0.pdf)). Commissioner Rohit Chopra issued a separate [statement](https://www.ftc.gov/public-statements/2021/09/statement-commissioner-rohit-chopra-matter-spyfone) ([PDF](https://www.ftc.gov/system/files/documents/public_statements/1595161/updated_date_final_chopra_statement_on_spyfone_.pdf)) saying the proposed order “in no way releases or absolves” the company or the CEO from potential criminal liability.


“We must be clear eyed about the variety of threats that surveillance businesses pose,” FTC Chair Lina Khan [said](https://twitter.com/linakhanFTC/status/1433435158913355778) in a tweet stream. “The @FTC will be vigilant in its data security and privacy enforcement and will seek to vigorously protect the public from these dangers.”



**It’s time to evolve threat hunting into a pursuit of adversaries.** [**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **Threatpost and Cybersixgill for** [**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **and get a guided tour of the dark web and learn how to track threat actors before their next attack.** [**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[SpyFone]] [[stalkerware]] [[FTC]] [[Android]] [[FTC’s]] [[apps]] [[Threatpost]] [[“The]] [[apps,]] [[victims’]] [[ThreatPost]]
