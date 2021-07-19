# Leaked NSO Group Data Hints at Widespread Pegasus Spyware Infections
### Report, based on secretive Israeli firm, suggests that activists, journalists, business executives and politicians were possible targets of iPhone and Android hacking.    

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167897)
+ Date: July 19, 2021  11:56 am
+ Author: Tom Spring


## Article:
Israeli-based NSO Group is being blasted in a groundbreaking report that alleges that the company’s controversial Pegasus malware is being used to target activists, journalists, business executives and politicians on a widespread level, using a variety of exploits — including a zero-click zero-day in iOS.


A consortium of journalists leveled the allegations in a report called Pegasus Project, which was published Sunday. It examined leaked data from the NSO Group, which revealed a cache of more than 50,000 mobile phone numbers worldwide that the firm was storing, according to the report [published by the Guardian newspaper](https://www.theguardian.com/world/2021/jul/18/revealed-leak-uncovers-global-abuse-of-cyber-surveillance-weapon-nso-group-pegasus).


The report accuses NSO Group of selling its spy tool, Pegasus, to unidentified third-parties, including governments, who then use it to infect the phones of dissidents and other people who may be critical of a given regime. The malware can secretly take remote control of the phone to monitor activity, enabling “customers” to even read encrypted messages of their targets sent via Signal and Telegram.



“The leak contains a list of more than 50,000 phone numbers that, it is believed, have been identified as those of people of interest by clients of NSO since 2016,” according to the Guardian report.


The Guardian, along with 16 additional media organizations, concluded that the NSO Group’s Pegasus malware is in widespread use and used to target more than just criminals and terrorists, as the company insists are the primary and only targets of its spyware.


In a statement issued by the NSO Group, it denies claims made in the Guardian report and those made by the Pegasus Project. It countered the report’s conclusions are based on “uncorroborated theories” that are “based on misleading interpretation of leaked data.”


Amnesty International found in its report that the spyware is under active development, consistently adding zero-day exploits into the mix, including in iPhone attacks observed as recently as this month. Those attacks have been effective against the latest version of iOS, and are “zero-click,” meaning that no user interaction or action is required to deliver an infection, according to [the report](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/).


“On the iPhone of a French human rights lawyer (CODE FRHRL2), we observed a lookup of a suspicious iMessage account unknown to the victim, followed by an HTTP request performed by the ‘com.apple.coretelephony’ process,” according to Amnesty International. “This is a component of iOS involved in all telephony-related tasks and likely among those exploited in this attack. We found traces of this HTTP request in a cache file stored on disk at */private/var/wireless/Library/Caches/com.apple.coretelephony/Cache.db,* containing metadata on the request and the response. The phone sent information on the device including the model 9,1 (iPhone 7) and iOS build number 18C66 (version 14.3) to a service fronted by Amazon CloudFront, suggesting NSO Group has switched to using AWS services in recent months. At the time of this attack, the newer iOS version 14.4 had only been released for a couple of weeks.”


The report added that zero-click attacks have been observed since May 2018; the most recent attack was observed exploiting multiple zero-days to attack a fully patched iPhone 12 running iOS 14.6 in July.


Reported Pegasus Victims
------------------------


The Paris-based Forbidden Stories and Amnesty International were initially given access to the leaked list of 50,000 phone numbers. The Pegasus Project is careful to point out that the list of phone numbers does not indicate that all of those phones were targeted with an attack.


“The presence of a phone number in the data does not reveal whether a device was infected with Pegasus or subject to an attempted hack. However, the consortium believes the data is indicative of the potential targets [that] NSO’s government clients identified in advance of possible surveillance attempts,” according to the report.


Reporters worked with researchers at Amnesty’s Security Lab to examine 67 phones believed to be targeted with the Pegasus malware. It found that more than half (37) had “traces of Pegasus activity” on them. Also, forensic analysis of leaked NSO Group data “suggested” the Pegasus spyware was used by Saudi Arabia and UAE to target phones of people close to murdered Washington Post journalist Jamal Khashoggi in the months after his death.


NSO in the Headlines
--------------------


In October 2019, [Facebook subsidiary WhatsApp sued NSO Group](https://threatpost.com/facebook-sues-nso-whatsapp-hack/149661/) for creating tools allegedly used by its clients for reading the protected WhatsApp messages of journalists and human rights workers.


NSO Group [maintains](https://threatpost.com/nso-group-president-defends-controversial-tactics/150694/) to this day that its spy tools are meant to help law enforcement fight crime and terror. It has often asserted it is not complicit in any government’s misuse of its technology.


Meanwhile, a separate report by Citizen Lab published last week [revealed that](https://threatpost.com/windows-zero-days-israeli-spyware-dissidents/167865/) a private company, called variously Candiru, Grindavik, Saito Tech and Taveta (and dubbed “Sourgum” by Microsoft), is hawking a malware dubbed DemonTongue that’s being used for surveillance of dissidents by repressive regimes, even though it says itself that it sells its wares exclusively to governments to combat terror, similar to the NSO Group.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[NSO]] [[malware]] [[iPhone]] [[zero-click]] [[000]] [[spyware]] [[ThreatPost]]
