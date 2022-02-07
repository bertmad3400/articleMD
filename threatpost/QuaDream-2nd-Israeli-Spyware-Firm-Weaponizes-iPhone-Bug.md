# QuaDream, 2nd Israeli Spyware Firm, Weaponizes iPhone Bug
### The now-patched flaw that led to the ForcedEntry exploit of iPhones was exploited by both NSO Group and a different, newly detailed surveillance vendor.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178252
+ Date: 2022-02-07T18:49:59+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/25125341/Spyware-scaled.jpg)

ForcedEntry – the exploit of a zero-click iMessage zero day that [circumvented](https://threatpost.com/pegasus-spyware-uses-iphone-zero-click-imessage-zero-day/168899/) Apple’s then-brand-new BlastDoor security feature starting a year ago – was picked apart not just by NSO Group with its Pegasus spyware but also by a newly uncovered, smaller smartphone-hacking toolmaker named QuaDream.


Reuters [published](https://www.reuters.com/technology/exclusive-iphone-flaw-exploited-by-second-israeli-spy-firm-sources-2022-02-03/) details on QuaDream last week. The outlet relied on input from five sources familiar with the matter, plus a look at two QuaDream product brochures dating from 2019 and 2020 that its reporters got their hands on.


Three people familiar with the matter told Reuters that QuaDream and NSO Group have shared employees over the years. Two sources also said that QuaDream and NSO Group came up with the iPhone exploit techniques on their own, separately — as opposed to collaborating.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


In September, Citizen Lab [published details about having captured](https://citizenlab.ca/2021/09/forcedentry-nso-group-imessage-zero-click-exploit-captured-in-the-wild/) NSO Group’s ForcedEntry exploit in the wild, though its security researchers believe that it was first used in February 2021. Apple had just introduced BlastDoor, a structural improvement in iOS 14 meant to block message-based, zero-click exploits – a month prior to when NSO Group is believed to have started using it.


Months earlier, in August, the privacy watchdog identified nine Bahraini activists whose iPhones were hacked with NSO Group’s Pegasus spyware between June 2020 and last February. Some of the activists were attacked with what Citizen Lab came to call the 2021 ForcedEntry exploit, while others’ devices were remotely exploited and infected with spyware by [the 2020 KISMET exploit](https://threatpost.com/zero-click-apple-zero-day-pegasus-spy-attack/162515/): another zero-click iMessage exploit.


BlastDoor was supposed to prevent this type of attack by acting as what Google Project Zero’s Samuel Groß called at the time a “tightly sandboxed” service responsible for “almost all” of the parsing of untrusted data in iMessages. The ForcedEntry exploit managed to circumvent BlastDoor by targeting Apple’s image rendering library: a sophisticated attack that was effective against Apple iOS, MacOS and WatchOS devices.


QuaDream Got in on the Fun
--------------------------


QuaDream was allegedly in on the Bahraini malware infections, it turns out, including an attack on one living in London at the time.


According to Reuters, the firm was founded in 2016 by Ilan Dabelstein, a former Israeli military official, and by two former NSO employees, Guy Geva and Nimrod Reznik. Reuters’ sources for QuaDream’s background were Israeli corporate records and two people familiar with the business.


Its 2016 founding means that QuaDream has spent more than five years hacking iPhones and other iGadgets, prying them open so as to monitor calls and get access to users’ microphones and cameras in real time. This type of powerful spyware gives its users access to their targets’ email, photos, texts, contacts and instant messages, even in spite of what should be the end-to-end encryption promised by services such as WhatsApp, Telegram or Signal.


There’s So Much Talent Out There, Unfortunately
-----------------------------------------------


Citizen Lab security researcher Bill Marczak, who’s been studying both companies’ tools, told Reuters that the zero-click capability of QuaDream’s flagship product – called REIGN – seems “on par” with NSO’s Pegasus spyware.


As Reuters noted, security researchers at Google’s Project Zero have called ForcedEntry [“one of the most technically sophisticated exploits”](https://googleprojectzero.blogspot.com/2021/12/a-deep-dive-into-nso-zero-click.html) they’ve ever captured: an estimation confirmed by Citizen Lab director Ronald Deibert.


On Monday, he pointed to Project Zero’s “very thorough” analysis of ForcedEntry as having demonstrated the level of engineering talent available to companies like NSO Group and others in the mercenary spyware marketplace.


“That spyware can be engineered with such sophistication and stealth, and then abused widely to target broad cross sections of civil society, should give everyone serious pause,” he told Threatpost via email.


Israeli Police Linked to Widespread Pegasus Spying
--------------------------------------------------


A related piece of news emerged on Monday. According to a new [report](https://www.calcalistech.com/ctech/articles/0,7340,L-3928830,00.html) from the Israeli newspaper Calcalist, dozens of prominent Israelis have been hacked with Pegasus, including a son of former premier Benjamin Netanyahu, activists and senior government officials.


“CEOs of government ministries, journalists, tycoons, corporate executives, mayors, social activists and even the Prime Minister’s relatives, all were police targets, having their phones hacked by NSO’s spyware, prior to any investigation even opening and without any judicial authorization,” Calcalist reported.


Pegasus was also recently found on the devices of Finland’s diplomatic corps serving outside the country as part of a wide-ranging espionage campaign, Finnish officials [claimed](https://threatpost.com/nso-group-pegasus-spyware-finnish-diplomats/178113/). In December, Pegasus was also [reportedly](https://threatpost.com/pegasus-spyware-state-department-iphones/176779/) planted on the iPhones of at least nine U.S. State Department employees.


QuaDream: Less Known But Just as Powerful
-----------------------------------------


According to QuaDream’s brochures for the REIGN “Premium Collection,” its malware tools offer similar capabilities as Pegasus, including “real-time call recordings,” “camera activation – front and back,” and “microphone activation,” as Reuters reported.


The outlet’s sources said that QuaDream and NSO Group share several buyers, including Saudi Arabia and Mexico, both of which are among the many governmental Pegasus buyers that have been accused of illegally using spyware to target political opponents. QuaDream’s first clients also allegedly include the Singaporean government. As well, the firm apparently made a pitch to the Indonesian government, though Reuters couldn’t determine whether Indonesia ponied up.


Its prices appear to vary. According to the 2019 brochure, one offering that gave customers the ability to infect 50 devices per year was priced at $2.2 million, “exclusive of maintenance costs,” though two people familiar with REIGN’s sales told Reuters that the price for REIGN “was typically higher.”


How Vast *Is* the Spyware Market?
---------------------------------


Kudos to Reuters for digging up details on QuaDream: not an easy task, given how murky the company is. It reportedly has no website, and employees have reportedly been told to stay mum about the company on their social-media posts.


John Bambenek, principal threat hunter at digital IT and security operations company Netenrich, told Threatpost on Monday that discretion is the hallmark of spyware sellers. “Every intelligence agency worth their salt (or more accurately their budgets) are developing these kinds of exploits in house or via closely-associated companies who do not do business with many other countries,” he said via email. “China, for instance, has done great work in mobile exploitation that seems to have been government performed effort. For every player we know about, there are dozens that are much more secretive.”


The fact that there are more spyware-makers than just NSO Group is no shocker.


That was made clear in December by Meta, Facebook’s parent company, which kicked six alleged spy-for-hire “cyber-mercenaries” [to the curb](https://threatpost.com/facebook-bans-spy-hire/177149/), along with a mysterious Chinese law-enforcement supplier. Meta accused the entities of collectively targeting about 50,000 people for surveillance, issued cease-and-desist warnings to six of the groups, and undertook the task of warning targeted people in more than 100 countries.


Mike Parkin, engineer at SaaS enterprise cyber-risk remediation firm Vulcan Cyber, told Threatpost that bleeding-edge attacks will continue to appear, given “an entire Dark-Web economy built around discovering exploits and selling them to the highest bidder, and state/state-sponsored actors having access to extraordinary financial and technical resources.”


There are “almost certainly” exploits similar to ForcedEntry already being used in the wild, Parkin said: ones that haven’t yet come to light “because they are used sparingly and only against high-value targets.”


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Derusbi]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=RTM]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Bahrain]] [[victim.continent.name=Asia]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=Indonesia]] [[victim.continent.name=Asia]] [[victim.country.name=Israel]] [[victim.continent.name=Asia]] [[victim.country.name=Saudi Arabia]] [[victim.continent.name=Asia]] [[victim.country.name=Singapore]] [[victim.continent.name=Asia]] [[victim.city.name=Singapore]] [[victim.country.name=Singapore]] [[victim.continent.name=Asia]] [[victim.country.name=Finland]] [[victim.continent.name=Europe]] [[victim.city.name=London]] [[victim.country.name=United Kingdom]] [[victim.continent.name=Europe]] [[victim.country.name=Mexico]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Quadream]] [[Nso]] [[Spyware]] [[Reuters]] [[Forcedentry]] [[Zero-click]] [[Blastdoor]] [[Threatpost]] [[Iphones]] [[ThreatPost]]

