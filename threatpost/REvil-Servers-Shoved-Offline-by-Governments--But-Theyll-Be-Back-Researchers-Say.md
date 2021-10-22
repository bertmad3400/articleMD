# REvil Servers Shoved Offline by Governments – But They’ll Be Back, Researchers Say
### A multi-country effort has given ransomware gang REvil a taste of its own medicine by pwning its backups and pushing its leak site and Tor payment site offline. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175675)
+ Date: October 22, 2021  1:01 pm
+ Author: Lisa Vaas


## Article:
The REvil ransomware gang is unhappy, with its Happy Blog leak site and Tor payment site pushed offline yet again, this time by a multi-country battering ram.


Relying on input from three private-sector cyber-experts working with the U.S. and one former official, [Reuters](https://www.reuters.com/technology/exclusive-governments-turn-tables-ransomware-gang-revil-by-pushing-it-offline-2021-10-21/) reported on Thursday that the ransomware-as-a-service (RaaS) gang has been given a taste of its own medicine: Specifically, the “hackers” who took out REvil’s servers did it by compromising its backups.


VMWare head of cybersecurity strategy Tom Kellermann told Reuters that those “hackers” were actually law enforcement and intelligence agencies from multiple countries: “The FBI, in conjunction with Cyber Command, the Secret Service and like-minded countries, have truly engaged in significant disruptive actions against these groups,” Kellermann, an adviser to the U.S. Secret Service on cybercrime investigations, said. “REvil was top of the list.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


REvil Didn’t Back Away From Its Own Backup
------------------------------------------


According to Reuters’ sources, last month, REvil operators restored operations from a backup that, it turns out, was under government control.


REvil operators – including a top leader called 0\_neday – restored the group’s websites from a backup last month, without realizing that law enforcement were controlling some of the gang’s internal systems.


Reuters quoted Oleg Skulkin, deputy head of the forensics lab at the Russian-led security company Group-IB: “The REvil ransomware gang restored the infrastructure from the backups under the assumption that they had not been compromised. Ironically, the gang’s own favorite tactic of compromising the backups was turned against them.”


It’s ironic, given that backups are seen as the [top way](https://threatpost.com/5-tips-to-prevent-and-mitigate-ransomware-attacks/166847/) to protect organizations from ransomware attacks. If an entity can just restore systems from backups, they don’t have to pay to get a [decryptor key](https://threatpost.com/revil-sodinokibi-ransomware-universal-decryptor/169498/) to unfreeze their seized systems, the thinking goes.


Ransomware attackers know that. Hence, they make a science out of [demolishing backups](https://threatpost.com/conti-ransomware-backups/175114/) to prevent their victims from shrugging off attacks and restoring operations from those backups in the wake of an attack.


There have been rumblings about REvil getting sucker-punched for a while: Last week, Flashpoint [reported](https://www.flashpoint-intel.com/blog/revil-disappears-again/) that on Oct. 17, a REvil operator announced that the ransomware group was shutting down its presence on the high-tier Russian language forum XSS after their domain had been “hijacked.”


The threat actor explained that an unidentified person had used the private Tor keys of the group’s former spokesperson, “Unknown,” to access the REvil domain.


REvil Recap
-----------


This is the second time in a few months that REvil’s servers have gone belly-up. [The first time](https://threatpost.com/ransomware-revil-sites-disappears/167745/) was on July 13.


After the July 2021 shutdown, REvil operators believed that Unknown had disappeared. Some believed that the spokesperson had died.


But then, somebody used Unknown’s keys. “The REvil operation stated that the REvil domain was accessed using Unknown’s keys, confirming their concerns that a third-party has backups with their service keys,” according to Flashpoint’s writeup.


‘Good Luck’
-----------


Over the weekend, 0\_neday posted a message on the XSS cybercrime forum, saying that REvil’s domain had been accessed with Unknown’s keys. In an XSS message captured and posted to Twitter by The Record’s [Dmitry Smilyanets](https://twitter.com/ddd1ms), 0\_neday said they were throwing in the towel:



> The server had been hacked, and they were on the lookout for me. They removed the route of my secret service from the torrc file and replaced it with their own, causing me to go there. I double-checked with others, and this was not the case. Good luck to everyone; I’m leaving now.” —0\_neday’s post to the XSS forum.
> 
> 



According to Flashpoint, a REvil operator confirmed that whoever had hijacked REvil’s sites had also deleted 0\_neday’s access to the gang’s hidden admin server.


So Much for REvil’s Reboot
--------------------------


REvil had recently begun to recruit new affiliates on the [RAMP forum](https://www.flashpoint-intel.com/blog/revil-continues-reemergence-on-ramp-forum/). Flashpoint pointed out that the group was offering unusually high commissions of 90 percent to attract [affiliates](https://www.flashpoint-intel.com/blog/interview-with-revil-affiliated-ransomware-contractor/).


It’s not surprising to hear that the rehashed, ragtag REvil reboot would feel the need to woo new affiliates with higher payouts. In September, news broke that REvil had [conned its own affiliates](https://threatpost.com/how-revil-may-have-ripped-off-its-own-affiliates/174887/) out of ransomware payments by using double chats and a backdoor that let REvil operators hijack ransom payments. A day later, those affiliates took to the top Russian-language hacking forum, Exploit, to renew their demands for REvil to fork over their [pilfered share of ransom payments](https://threatpost.com/revil-affiliates-leadership-cheated-ransom-payments/174972/).


Flashpoint noted that XSS users had been “generally incredulous” when REvil joined the RAMP forum. On Oct. 18, the XSS moderators closed the thread where REvil made its pitch for new affiliates and advised fellow users to block REvil accounts.


The underground is undoubtedly unsurprised by this new REvil takedown. They’ve interpreted it as proof that the gang’s [re-emergence in September](https://www.flashpoint-intel.com/blog/revil-is-back-on-exploit-and-trying-to-restore-its-reputation/) was “part of an elaborate FBI plot to catch REvil affiliates,” as Flashpoint described a LockBit representative’s take on the news.


“Several threat actors agreed with the Lockbit representative and added that they believed that REvil will re-emerge again under a totally new name, leaving behind [recent scandals](https://www.flashpoint-intel.com/blog/revils-cryptobackdoor-con-ransomware-groups-tactics-roil-affiliates-sparking-a-fallout/) without having to pay out old affiliates,” according to Flashpoint’s writeup.


REvil’s Roly-Poly Road
----------------------


The [REvil](https://threatpost.com/revil-apple-ransomware-pay-off/165570/) ransomware gang is notorious – or, rather, was notorious at one point and, since July, has been reshaped like a blob of Silly-Putty. Aka [Sodinokibi](https://threatpost.com/sodinokibi-ransomware-now-scans-networks-for-pos-systems/156855/), REvil’s victim list has included [Kaseya](https://threatpost.com/kaseya-patches-zero-days-revil-attacks/167670/) and its many managed service provider (MSP) customers, the global meat supplier [JBS Foods](https://threatpost.com/jbs-paid-11m/166767/), and even, audaciously enough, [Apple](https://threatpost.com/revil-apple-ransomware-pay-off/165570/).


According to Reuters’ sources, it’s also responsible for the [Colonial Pipeline](https://threatpost.com/colonial-pays-5m/166147/) attack. Unnamed officials told the outlet that the DarkSide encryption software used in the Colonial attack was actually developed by REvil associates, counteracting months-long reporting about a ransomware group named DarkSide being responsible for the attack.


After its servers went offline in July – a disappearance that some observers linked to its main operator taking off to avoid the heat generated by the Kaseya attack – REvil [reared its slimy head](https://threatpost.com/revil-back-coder-decryptor-key/169403/) again in September.


September was quite a month for REvil. Its servers came back online; a fresh victim was listed on its site; ransomware payments were allegedly back up and flowing; a new REvil operator offered an explanation for the gang’s [two-month hiatus](https://threatpost.com/ransomware-revil-sites-disappears/167745/); and it told a story about how one of its fat-fingered coders misclicked, generated and issued a [universal decryptor for Kaseya](https://threatpost.com/kaseyas-master-key-to-revil-attack-leaked-online/168565/).


But that’s just not how the ransomware business works. The underground scoffed, dubbing the reborn gang as likely some mediocre, lower-tier REvil lackeys milking the name so as to pull an exit scam.


The Importance of Multi-Country Coordination
--------------------------------------------


Steve Forbes, a government cyber security expert at Nominet, noted that the significance of a multi-country takedown like this one is “hard to overstate” in the ransomware battle and that this is the way to go as that battle rages on.


“Ransomware has increasingly taken centre stage this year, as it has disrupted global supply chains,” Forbes told Threatpost on Friday. “Despite not always being a very sophisticated attack method, it achieves notoriety because of its real-world impact. A combination of network analysis to identify the tell-tale signs of a ransomware attack, robust back-ups to aid recovery, and cross-country coordinated takedowns will be the key to stemming the flow of successful ransomware attacks in the future.”


They’ll Be Back
---------------


Multiple experts told Threatpost that nobody should assume that REvil’s affiliates have been neutralized. Rather, they’re still hungry for profits and they’ll likely be back.


“REvil affiliates regularly used double extortion, the exfiltration of data from victim networks with the threat of release, to compel payment,” Jake Williams, co-founder and CTO at BreachQuest, said via email. “These affiliates stay in line and don’t release data because doing so would remove them from future work with the core group, effectively their cash cow.


“As work from REvil is clearly drying up now, affiliates will need new sources of revenue. It won’t be surprising to see stolen [data] sold on the dark web. I anticipate that some organizations who believed their data was safe because they paid an REvil ransom are in for a rude awakening.”


Digital Shadows’ Photon Research Team agreed. In a statement sent to Threatpost, its analysts said that despite law enforcement operations, “it’s realistically possible that unscathed REvil affiliates will return as a rebranded ransomware group. This is a familiar tactic employed by cybercriminals who remain intent on continuing ransomware extortion operations.”


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[REvil]] [[ransomware]] [[REvil’s]] [[XSS]] [[gang’s]] [[Flashpoint]] [[Reuters]] [[“The]] [[0_neday]] [[attack.]] [[ThreatPost]]
