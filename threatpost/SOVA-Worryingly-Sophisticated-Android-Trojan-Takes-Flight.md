# SOVA, Worryingly Sophisticated Android Trojan, Takes Flight
### The malware appeared in August with an ambitious roadmap (think ransomware, DDoS) that could make it ‘the most feature-rich Android malware on the market.’

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169366)
+ Date: September 10, 2021  12:25 pm
+ Author: Tara Seals


## Article:
A new Android banking trojan named SOVA (“owl” in Russian) is under active development, researchers said, and it has big dreams even in its infancy stage. The malware is looking to incorporate distributed denial of service (DDoS), man in the middle (MiTM) and ransomware functionality into its arsenal – on top of existing banking overlay, notification manipulation and keylogging services.


According to researchers from ThreatFabric, the malware’s authors are shooting for the moon on this one.


“This malware is still in its infancy [first appearing in August, now only on version 2] and it is undergoing a testing phase…prospecting serious and worrying plans for the near future,” they said in a [Friday analysis](https://www.threatfabric.com/blogs/sova-new-trojan-with-fowl-intentions.html), noting that the malware’s roadmap is laid out in underground forum posts advertising its availability for testing.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“SOVA is…taking a page out of traditional desktop malware,” they added. “Including DDoS, man in the middle and ransomware to its arsenal could mean incredible damage to end users, in addition to the already very dangerous threat that overlay and keylogging attacks serve.”


The malware authors’ coding and development choices also speak to SOVA’s sophistication, the analysis showed.


“Regarding the development, SOVA also stands out for being fully developed in Kotlin, a coding language supported by Android and thought by many to be the future of Android development,” according to ThreatFabric. “If the author’s promises on future features are kept, SOVA could potentially be the most complete and advanced Android bot to be fully developed in Kotlin to this day.”


SOVA meanwhile relies on the legitimate open-source project known as RetroFit for its communication with the command-and-control (C2) server.


“Retrofit is a type-safe REST client for Android, Java and Kotlin developed by Square,” researchers said. “The library provides a powerful framework for authenticating and interacting with APIs and sending network requests with OkHttp.”


**Banking Trojan Features**
---------------------------


SOVA is first and foremost a banking trojan, and its authors are applying innovation to this portion of its development too, researchers noted. For instance, SOVA doesn’t skimp on the more traditional banking front of overlay attacks.


Overlay attacks are a common tactic used by banking trojans, in which the malware replaces the screen that users see when they log into mobile banking with a copycat screen – thus harvesting any credentials the victim puts in.


In SOVA’s case, the targets that it’s capable of imitating include banking applications, cryptocurrency wallets and shopping applications that require credit-card access to operate.


“According to the authors, there are already multiple overlays available for different banking institutions from the U.S. and Spain, but they offer the possibility of creating more in case of necessity from the buyer,” researchers noted. Also, version 2 contains functionality to target users of some Russian banks – drawing ire from other forum users, ThreatFabric reported.


To better gather the victim’s credentials and other personally identifiable information (PII), SOVA is banking (so to speak) on Android’s Accessibility Services – also a traditional functionality.


“When it is started for the first time, the malware hides its app icon and abuses the Accessibility Services to obtain all the necessary permissions to operate properly,” researchers explained. Some of those permissions allow it to intercept for SMS messages and notifications for instance, to better hide from the victim – and on the roadmap is also the ability to circumvent two-factor authentication.


SOVA already has one highly uncommon banking-trojan feature that stands out for Android malware, according to the analysis: The ability to steal session cookies, which allows the malware to piggyback on valid logged-in banking sessions, thus skirting the need to have banking credentials to access victim’s accounts.


“Cookies are a vital part of web functionality, which allow users to maintain open sessions on their browsers without having to re-input their credentials repeatedly,” researchers noted. “SOVA will create a WebView to open a legitimate web URL for the target application and steal the cookies once the victim successfully logs in…it is capable of stealing session cookies from major websites like Gmail or PayPal with ease.”


In the newer version of SOVA, the cybercrooks also added the option to create a list of applications for which to monitor for cookies automatically.


Another feature that version 2 offers is clipboard manipulation, i.e., the ability to alter the data in the system clipboard in an effort to steal cryptocurrency, ThreatFabric explained.


“The bot sets up an event listener, designed to notify the malware whenever some new data is saved in the clipboard,” researchers said. “If the string of data is potentially a cryptocurrency wallet address, S.O.V.A. substitutes it with a valid address for the corresponding cryptocurrency.”


The supported cryptocurrencies so far are Binance, Bitcoin, Ethereum and TRON.


Still ahead on the roadmap, SOVA’s authors said that they will soon add “automatic three-stage overlay injections.”


“It is not clear what the three stages imply, but it could mean more advances and realistic process, maybe implying download of additional software to the device,” researchers noted.


**SOVA: A Well-Thought-Out Development Roadmap**
------------------------------------------------


The authors of the malware clearly have plenty of ambitions regarding SOVA’s future, and it does have the potential to become a dangerous threat for the Android ecosystem, researchers concluded.


“The second set of features, added in the future developments, are very advanced and would push SOVA into a different realm for Android banking malware,” they said. “If the authors adhere to the roadmap, it will also be able to feature…DDoS capabilities, ransomware and advanced overlay attacks. These features would make SOVA the most feature-rich Android malware on the market and could become the ‘new norm’ for Android banking trojans targeting financial institutions.”


In some ways, SOVA could be following in the footsteps of TrickBot, a multiplatform malware that began life as a banking trojan before moving on to other types of cyberattacks and becoming one of the most popular and pervasive trojans used by bad actors across the globe. It now specializes in acting as a first-stage infection, delivering a range of follow-on ransomware and other malware.


Interestingly, TrickBot’s authors [lately instituted some code changes](https://threatpost.com/trickbot-banking-trojan-module/167521/) that could indicate that TrickBot is getting back into the bank-fraud game – specifically adding a man-in-the-browser (MitB) capability for stealing online banking credentials that derives from Zeus, the early banking trojan — potentially signaling a coming onslaught of fraud attacks.


**It’s time to evolve threat hunting into a pursuit of adversaries.**[**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**Threatpost and Cybersixgill for**[**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**and get a guided tour of the dark web and learn how to track threat actors before their next attack.**[**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with independent researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[SOVA]] [[malware]] [[Android]] [[ransomware]] [[SOVA’s]] [[noted.]] [[“If]] [[said.]] [[“The]] [[attacks.]] [[ThreatPost]]
