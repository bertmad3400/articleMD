# Apple Issues Emergency Fix for NSO Zero-Click Zero Day
### Citizen Lab urges Apple users to update immediately. The new zero-click zero-day ForcedEntry flaw affects all things Apple: iPhones, iPads, Macs and Watches.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169416)
+ Date: September 13, 2021  6:10 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/20141444/white-pegasus-e1626804896117.jpg)
Apple users should immediately update all their devices – iPhones, iPads, Macs and Apple Watches – to install an emergency patch for a zero-click zero-day exploited by NSO Group to install spyware.


The [security updates](https://support.apple.com/en-us/HT201222), pushed out by Apple on Monday, include [iOS 14.8](https://support.apple.com/en-us/HT212807) for iPhones and iPads, as well as new updates for Apple Watch and macOS. The patches will fix at least one vulnerability that the tech behemoth said “may have been actively exploited.”


Citizen Lab first [discovered](https://threatpost.com/pegasus-spyware-uses-iphone-zero-click-imessage-zero-day/168899/) the never-before-seen, zero-click exploit, which it detected targeting iMessaging, last month. It’s allegedly been used to illegally spy on Bahraini activists with NSO Group’s Pegasus spyware, according to the cybersecurity watchdog.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The digital researchers dubbed the new iMessaging exploit ForcedEntry.


Citizen Group said in August that they had identified nine Bahraini activists whose iPhones were inflicted with Pegasus spyware between June 2020 and February 2021. Some of the activists’ phones suffered zero-click iMessage attacks that, besides ForcedEntry, also included [the 2020 KISMET exploit](https://threatpost.com/zero-click-apple-zero-day-pegasus-spy-attack/162515/).


The activists included three members of [Waad](https://www.aldemokrati.org/) (a secular Bahraini political society), three members of the [Bahrain Center for Human Rights](https://bahrainrights.net/), two exiled Bahraini dissidents, and one member of [Al Wefaq](https://en.wikipedia.org/wiki/Al_Wefaq) (a Shiite Bahraini political society), Citizen Lab wrote.


The ForcedEntry exploit was particularly notable in that it was successfully deployed against the latest iOS versions – 14.4 & 14.6 – blowing past Apple’s new BlastDoor sandboxing feature to install spyware on the iPhones of the Bahraini activists.


Citizen Lab first observed NSO Group deploying ForcedEntry in February 2021. Apple had just [introduced BlastDoor](https://threatpost.com/apple-ios-imessage-blastdoor/163479/), a structural improvement in iOS 14 meant to block message-based, zero-click exploits like these NSO Group-associated attacks – the month before. BlastDoor was supposed to prevent this type of Pegasus attack by acting as what Google Project Zero’s Samuel Groß [called](https://googleprojectzero.blogspot.com/2021/01/a-look-at-imessage-in-ios-14.html) a “tightly sandboxed” service responsible for “almost all” of the parsing of untrusted data in iMessages.


In a [post](https://citizenlab.ca/2021/09/forcedentry-nso-group-imessage-zero-click-exploit-captured-in-the-wild/) on Monday, Citizen Lab researchers said that in March 2021, they had examined the phone of a Saudi activist who requested anonymity and determined that the phone had been infected with NSO Group’s Pegasus spyware. Last Tuesday, Sept. 7, Citizen Lab forwarded artifacts from two types of crashes on another phone that had been infected with Pegasus, suspecting that both infections showed parts of the ForcedEntry exploit chain.


Citizen Lab forwarded the artifacts to Apple on Tuesday, Sept. 7. On Monday, Sept. 13, Apple confirmed that the files included a zero-day exploit against iOS and MacOS. Apple has designated the ForcedEntry exploit CVE-2021-30860: an as-yet-unrated flaw that Apple describes as “processing a maliciously crafted PDF may lead to arbitrary code execution.”


Sniffing out NSO Group’s Tracks
-------------------------------


Citizen Lab described several distinct elements that gives researchers high confidence that the exploit can be tied to the secretive Israeli spyware maker [NSO Group](https://threatpost.com/nso-group-data-pegasus/167897/), including a forensic artifact called CascadeFail.


CascadeFail is a bug whereby “evidence is incompletely deleted from the phone’s DataUsage.sqlite file,” according to Citizen Lab. In CascadeFail, “an entry from the file’s ZPROCESS table is deleted, but not entries in the ZLIVEUSAGE table that refer to the deleted ZPROCESS entry,” they described.


That has NSO Group’s fingerprints, they said: “We have only ever seen this type of incomplete deletion associated with NSO Group’s Pegasus spyware, and we believe that the bug is distinctive enough to point back to NSO.”


Another telltale sign: multiple process names installed by the ForcedEntry exploit, including the name “setframed”. That process name was used in an attack with NSO Group’s Pegasus spyware on an [Al Jazeera journalist](https://threatpost.com/zero-click-apple-zero-day-pegasus-spy-attack/162515/) in July 2020, according to Citizen Lab: a detail that the watchdog didn’t reveal at the time.


Zero click remote exploits such as the novel method used by Pegasus spyware to invisibly infect an Apple device without the victim’s knowledge or the need for the victim to click on anything at all were used to infect one victim for as long as six months. They’re pure gold to governments, mercenaries and criminals who want to secretly surveil targets’ devices without being detected.


Pegasus is a powerful spyware: it can turn on a target’s camera and microphone so as to record messages, texts, emails, and calls, even if they’re sent via encrypted messaging apps such as [Signal](https://threatpost.com/google-research-pinpoints-security-soft-spot-in-multiple-chat-platforms/163175/).


Pegasus’s Threadbare Narrative
------------------------------


NSO has long maintained that it only sells its spyware to a handful of intelligence communities within countries that have been thoroughly vetted for human rights violations. The company has repeatedly tried to keep up that narrative, taking the tactic of questioning Citizen Lab’s methods and motives.


But, as pointed out by Hank Schless, Senior Manager of security solutions at endpoint-to-cloud security company Lookout, the narrative is now pretty threadbare. “The recent exposure of 50,000 phone numbers linked to targets of NSO Group customers was all people needed to see right through what NSO claims,” he told Threatpost on Monday.


“Since Lookout and The Citizen Lab first discovered Pegasus back in 2016, it has continued to evolve and take on new capabilities,” he elaborated. “It can now be deployed as a zero-click exploit, which means that the target user doesn’t even have to tap a malicious link for the surveillanceware to be installed.


While the malware has adjusted its delivery methods, the basic exploit chain remains the same, Schless continued. “Pegasus is delivered via a malicious link that’s been socially engineered to the target, the vulnerability is exploited and the device is compromised, then the malware communicated back to a command-and-control (C2) server that gives the attacker free reign over the device. Many apps will automatically create a preview or cache of links in order to improve the user experience. Pegasus takes advantage of this functionality to silently infect the device.”


Schless said that this is an example of how important it is for both individuals and enterprise organizations to have visibility into the risks their mobile devices present, Pegasus being just onei “extreme, but easily understandable example.


“There are countless pieces of malware out there that can easily exploit known device and software vulnerabilities to gain access to your most sensitive data,” he continued. “From an enterprise perspective, leaving mobile devices out of the greater security strategy can represent a major gap in the ability to protect the entire infrastructure from malicious actors. Once the attacker has control of a mobile device or even compromises the user’s credentials, they have free access to your entire infrastructure. Once they enter your cloud or on-prem apps, they can move laterally and identify sensitive assets to encrypt for a ransomware attack or exfiltrate to sell to the highest bidder.”


Kevin Dunne, president at unified access orchestration provider Pathlock, noted that the Pegasus infections point to the need for businesses to look beyond securing servers and workstations as primary targets for cyberattacks and espionage. “Mobile devices are now used broadly and contain sensitive information that needs to be protected,” he explained.


To protect themselves against spyware, businesses should look at their mobile device security strategy, Dunne said – particularly when threats come in forms that are far more insidious than suspicious SMS messages or phishy links that security teams can train users to avoid.


“Spyware attackers have now engineered zero click attacks which are able to get full access to a phone’s data and microphone/camera by using vulnerabilities in third party apps or even built-in applications,” Dunne said. “Organizations need to make sure they have control over what applications users download on to their phones, and can ensure they are up to date so any vulnerabilities are patched.”


**It’s time to evolve threat hunting into a pursuit of adversaries.** [**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **Threatpost and Cybersixgill for** [**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **and get a guided tour of the dark web and learn how to track threat actors before their next attack.** [**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar) **for the LIVE discussion on September 22 at 2 PM EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[NSO]] [[Bahraini]] [[Group’s]] [[spyware]] [[zero-click]] [[ForcedEntry]] [[Monday,]] [[iPhones]] [[exploit,]] [[spyware,]] [[ThreatPost]]
