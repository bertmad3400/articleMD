# Cybercrooks Frame Targets by Planting Incriminating Evidence
### The ‘ModifiedElephant’ threat actors are technically unimpressive, but they’ve evaded detection for a decade, hacking human rights advocates' systems with dusty old keyloggers and off-the-shelf RATs.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178384
+ Date: 2022-02-11T19:57:34+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/02/11143537/elephant-scaled-e1644608152556.jpeg)

Threat actors are hijacking the devices of India’s human rights lawyers, activists and defenders, planting incriminating evidence to set them up for arrest, researchers warn.


The actor, dubbed ModifiedElephant, has been at it for at least 10 years, and it’s still active. It’s been shafting targets since 2012, if not sooner, going after hundreds of groups and individuals – some repeatedly – according to SentinelLabs researchers.


The operators aren’t what you’d call technical prodigies, but that doesn’t matter. Tom Hegel, threat researcher at SentinelOne, said in a Wednesday [post](https://www.sentinelone.com/labs/modifiedelephant-apt-and-a-decade-of-fabricating-evidence/) that the advanced persistent threat (APT) group – which may be tied to the [commercial surveillance](https://threatpost.com/quadream-israeli-spyware-weaponized-iphone-bug/178252/) industry – has been muddling along just fine using rudimentary hacking tools such as commercially available remote-access trojans (RATs).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The APT is snaring victims with spearphishing, delivering malware via rigged documents.


The group’s preferred malwares include [NetWire](https://threatpost.com/netwire-rat-back-stealing-payment-card-data/122156/), [DarkComet](https://threatpost.com/darkcomet-rat-flames-out-070912/76777/) and simple keyloggers “with infrastructure overlaps that allow us to connect long periods of previously unattributed malicious activity,” Hegel wrote.


The DarkComet RAT, for one, has been used in politically motivated attacks for at least as long as ModifiedElephant has been doing its dirty work. In 2012, its author [threw in](https://threatpost.com/darkcomet-rat-flames-out-070912/76777/) the towel on development and sales after finding out that [DarkComet was used by the Syrian government](https://threatpost.com/syrian-government-using-skype-spyware-monitor-rebels-050412/) in attacks against anti-government activists.


Frumpy Old Tools
----------------


“There’s something to be said about how mundane the mechanisms of this operation are,” said Juan Andrés Guerrero-Saade, threat researcher at SentinelOne and adjunct professor at Johns Hopkins SAIS, [via Twitter](https://twitter.com/juanandres_gs/status/1491784707008122885?s=20). “The malware is either custom garbage [or] commodity garbage. There’s nothing *technically* impressive about this threat actor, instead we marvel at their audacity.”


In fact, ModifiedElephant uses old Visual Basic keyloggers that “are not the least bit technically impressive,” Hegel wrote, noting that the overall keylogger structure resembles code that was freely available on [Italian hacking forums](https://italianhack.forumfree.it/?t=63131534) back in 2012. The loggers don’t even work anymore, he said, given that they’re built “in such a brittle fashion.”


ModifiedElephant is also sending a commodity Android trojan payload, delivered as an APK file (0330921c85d582deb2b77a4dc53c78b3), along with the NetWire trojan. The Android trojan tries to trick recipients into installing the malware themselves, by posing as a news app or a safe messaging tool.


Below is an example of ModifiedElephant’s phishing emails, which include attachments for the NetWire and Android trojan variants.


The Android trojan appears to have been designed as a multi-purpose hacking tool for broader cybercrime, researchers said. But the fact that it’s delivered at the same time as NetWire means that the same attacker was trying to target victims across the spectrum, getting them both from the endpoint and on mobile.


The trojan enables attackers to intercept and manage SMS and call data, wipe or unlock the device, perform network requests, and perform remote administration, according to SentinelLabs: In other words, it’s a basic, ideal, low-cost mobile surveillance toolkit.


Evidence Tampering
------------------


An example of the incriminating files planted by ModifiedElephant is a file, Ltr\_1804\_to\_cc.pdf, that detailed an assassination plot against India Prime Minister Narendra Modi. Arsenal Consulting’s digital analysis shows that the file – one of the more [incriminating pieces](https://web.archive.org/web/20210917152050/https://scroll.in/article/991095/why-isnt-the-government-looking-for-the-source-of-modi-assassination-malware-on-rona-wilsons-pc) of data seized by police – was one of many files delivered via a NetWire RAT remote session associated with ModifiedElephant.


“Further analysis showed how ModifiedElephant was performing nearly identical evidence creation and organization across multiple unrelated victim systems within roughly fifteen minutes of each other,” according to SentinelLabs’ detailed [report](https://www.sentinelone.com/labs/modifiedelephant-apt-and-a-decade-of-fabricating-evidence/).


If the notion of a threat actor tampering with evidence sounds familiar, it might be because ModifiedElephant’s tactics have precedence, Guerrero-Saade [tweeted](https://twitter.com/juanandres_gs/status/1491784711110234126).


A few months back, SentinelOne [reported](https://www.sentinelone.com/labs/egomaniac-an-unscrupulous-turkish-nexus-threat-actor/) on EGoManiac, a Turkish nexus (as in, its malware contained Turkish language, its lures were written in Turkish, and its victims are Turkish and related to local politics) threat actor that was doing similar with the Octopus Brain campaign.


In that campaign, Arsenal Consulting’s digital forensics revealed that the threat actor [planted](https://otx.alienvault.com/pulse/5859cea0a759501d3b140f5b) incriminating files on the systems of journalists working at the Turkish online news portal OdaTV immediately before Turkish National Police seized their machines. The fabricated files were later used as evidence of terrorism and justification for jailing journalists.


“A threat actor willing to frame and incarcerate vulnerable opponents is a critically underreported dimension of the cyber threat landscape that brings up uncomfortable questions about the integrity of devices introduced as evidence,” SentinelOne’s Hegel pointed out in Wednesday’s post.


Analyzing EGoManiac’s intrusions revealed the decade’s worth of malicious activity that SentinelLab now attributes to a previously unknown threat actor – namely, ModifiedElephant.


“This actor has operated for years, evading research attention and detection due to their limited scope of operations, the mundane nature of their tools, and their regionally-specific targeting,” Hegel said. What’s more, it’s still actively targeting victims.


Victimology
-----------


ModifiedElephant’s goal is long-term surveillance, sometimes leading up to the delivery of cooked-up “evidence” that supposedly connects the target to specific crimes right before what Hegel referred to as “conveniently coordinated arrests,” like the files planted on the devices used by OdaTV journalists Barış Pehlivan and Müyesser Yıldız.


Researchers have identified hundreds of groups and individuals targeted by ModifiedElephant phishing campaigns: predominantly, they’re activists, human rights defenders, journalists, academics and law professionals in India.


The APT primarily uses weaponized Microsoft Office files to deliver whichever malware the operators currently favor – a preference that’s changed over time and depending on the target.


Here’s how the group has evolved over the years, researchers said:


* Mid-2013: the actor used phishing emails containing executable file attachments with fake double extensions (filename.pdf.exe).
* Post-2015: the actor moved on to less obvious files containing publicly available exploits, such as .doc, .pps, .docx, .rar, and password protected .rar files. These attempts involved legitimate lure documents in .pdf, .docx, and .mht formats to captivate the target’s attention while also executing malware.
* 2019: ModifiedElephant operators employed phishing campaigns that dangled links to files hosted externally for manual download and execution by the target.
* 2020: As Amnesty International and Citizen Lab [documented](https://www.amnesty.org/en/latest/research/2020/06/india-human-rights-defenders-targeted-by-a-coordinated-spyware-operation/), the operators also made use of large .rar archives (up to 300MB), potentially in an attempt to bypass detection, in a coordinated spyware attack that illegally targeted nine human rights defenders.


SentinelLabs found that the lure documents they analyzed repeatedly made use of exploits of vulnerabilities that have been used plenty of times over the years – [CVE-2012-0158](https://threatpost.com/extensible-attack-platform-has-familiar-feel/103021/), [CVE-2014-1761](https://threatpost.com/plugx-go-to-malware-for-targeted-attacks-more-prominent-than-ever/110936/), [CVE-2013-3906](https://threatpost.com/attacks-on-new-microsoft-zero-day-using-multi-stage-malware/102833/) and [CVE-2015-1641](https://threatpost.com/apt-targeting-tibetans-packs-four-vulnerabilities-in-one-compromise/117493/) – to drop and execute malware. The spearphishing emails and lures use titles and themes around topics relevant to the target, Hegel said, “such as activism news and groups, global and local events on climate change, politics, and public service.”


Below is another phishing example:


Critics of Authoritarian Governments, Beware
--------------------------------------------


SentinelOne cautions that it only took a look at “a small subset” of the total list of ModifiedElephant’s potential targets, the actor’s techniques and its objectives.


More work needs to be done, and many questions remain to be answered. But one thing’s clear, researchers said: “Critics of authoritarian governments around the world must carefully understand the technical capabilities of those who would seek to silence them.”


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=Silence]]

#### Action:
[[action.malware.name=Arp]] [[action.malware.name=Arp]] [[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=DarkComet]] [[action.malware.name=Net]] [[action.malware.name=NETWIRE]] [[action.malware.name=njRAT]] [[action.malware.name=Octopus]] [[action.malware.name=Reg]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=Oman]] [[victim.continent.name=Asia]] [[victim.country.name=Syria]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Modifiedelephant]] [[Hegel]] [[Malware]] [[Sentinelone]] [[Netwire]] [[Phishing]] [[Sentinellabs]] [[Android]] [[Darkcomet]] [[Emails]] [[ThreatPost]]
#### CVE's
[[CVE-2012-0158]] [[CVE-2014-1761]] [[CVE-2013-3906]] [[CVE-2015-1641]]
#### MD5-hash
0330921c85d582deb2b77a4dc53c78b3

