# TA505 Gang Is Back With Newly Polished FlawedGrace RAT
### TA505 – cybercrime trailblazers with ever-evolving TTPs – have returned to mass-volume email attacks, flashing retooled malware and exotic scripting languages. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175559)
+ Date: October 19, 2021  5:00 am
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/18181519/rat-standing-rodent-cute-e1634595333580.jpg)
The TA505 cybercrime group is whirring its financial rip-off machinery back up, pelting malware at a range of industries in what was initially low-volume waves that researchers saw spiral up late last month.


They do bad things, but they’re so tricky that tracking them is a ton of fun, said Sherrod DeGrippo, vice president, Threat Research and Detection at Proofpoint.


“Tracking TA505 is one of life’s guilty little pleasures,” she admitted. “They are a trailblazer in the world of cybercrime, regularly changing up their [tactics, techniques and procedures, or TTPs].”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


TA505, aka Hive0065, is a gang of cybercrooks involved in both financial swindles and state-sponsored actions. Proofpoint researchers describe the group as being “[one of the more prolific actors](https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta505-dridex-globeimposter)” that they track.


It’s behind the biggest spam campaigns the firm has ever seen: namely, distribution of the [Dridex banking trojan](https://threatpost.com/covid-19-relief-checks-dridex-malware/164853/). Proofpoint has also tracked the gang distributing Locky and Jaff ransomwares, the [Trick banking trojan](https://threatpost.com/trickbot-banking-trojan-module/167521/), and others “in very high volumes,” Proofpoint says.


TA505, which actively targets a slew of industries – including finance, retail and restaurants – has been active since at least 2014. It’s known for frequent malware switchups and for driving global trends in criminal malware distribution.


The most recent bout of campaigns is reminiscent of TA505’s activity from 2019 and 2020, but “it doesn’t lack for some intriguing, new elements,” DeGrippo said, including spiffed-up tools and exotic languages. “In addition to updating [the FlawedGrace remote-access trojan, or RAT], they also overhauled their intermediate loader stages, replacing trusty Get2 with several new downloaders that are coded in unusual scripting languages,” she noted.


Retooling to Re-Attack
----------------------


True to form, the gang’s latest campaigns are distributed across a wide range of industries. They’re also showing up with new gear, including an upgraded KiXtart loader, the MirrorBlast loader that downloads [Rebol script stagers](http://www.rebol.com/rebolintro.html), the retooled [FlawedGrace](https://attack.mitre.org/software/S0383/) RAT, and updated malicious Excel attachments.


In an [analysis](https://www.proofpoint.com/us/blog/threat-insight/whatta-ta-ta505-ramps-activity-delivers-new-flawedgrace-variant) published on Tuesday, Proofpoint said that its researchers have been tracking renewed malware campaigns from TA505 that started out slowly at the beginning of September – with only several thousand emails per wave, distributing malicious Excel attachments – and then pumped up the volume later in the month, resulting in tens to hundreds of thousands of emails by the end of September.


Many of the campaigns – particularly the heftier ones – “strongly resemble” what the gang was up to between 2019 and 2020, including similar domain naming conventions, email lures, Excel file lures, and the delivery of the FlawedGrace RAT, according to the writeup. In the early September waves of email attacks, TA505 used more specific lures that didn’t affect as many industries as the more recent October 2021 campaigns Proofpoint researchers said.


“Example lures included legal, media release, situation report, and health claim themes,” according to the analysis.


By the time that the campaigns ramped up in late September/early October, TA505 was targeting more industries, and the gang began to use both URL- and attachment-based email campaigns.


TA505 also began to branch out: The crooks were initially targeting predominantly North American targets such as the U.S. and Canada but eventually began to go after German-speaking countries, including Germany and Austria, as the campaigns gained momentum.


Noteworthy new developments include the updated version of the FlawedGrace RAT, along with retooled intermediate loader stages scripted in Rebol and KiXtart – which. researchers said, the gang is using instead of the previously popular Get2 downloader. “The new downloaders perform similar functionality of reconnaissance and pulling in the next stages,” Proofpoint researchers noted.


The firm provided a screen capture, shown below, of one of the emails from a more recent (Sept. 28) campaign.


“The emails contained an Excel attachment that, when opened and macros enabled, would lead to the download and running of an MSI file,” Proofpoint said. [MSI files](https://isc.sans.edu/forums/diary/Malware+Delivered+via+Windows+Installer+Files/23349/#:~:text=MSI%20files%20are%20Windows%20installer,%7Cvbs%7C%E2%80%A6)%E2%80%9D.) are used to install software on a Windows system. “The MSI file in turn would execute an embedded Rebol loader, dubbed by Proofpoint as MirrorBlast.”


Proofpoint also offered a screen capture of an insurance claim Excel attachment, shown below, that was also part of the Sept. 28 campaign.


In a more recent campaign – one from Oct. 13 – the gang began to abuse Microsoft and OneDrive branding on their landing page.


New TTP: Intermediate Loaders in Exotic Languages
-------------------------------------------------


Researchers noted that TA505 is now using multiple intermediate loaders before the delivery of the FlawedGrace RAT, and they’re coded in uncommon scripting languages – Rebol and KiXtart.


The more things change, the more they stay the same, though: The intermediate loaders appear to serve the same purpose as Get2—a downloader that TA505 has been using since 2019 to deliver a variety of secondary payloads, researchers said.


“The loaders perform minimal reconnaissance of an infected machine, such as collecting user domain and username information, and download further payloads,” according to the writeup.


Malware Morphs, But Traces Linger
---------------------------------


Proofpoint picked up on similarities between current and older TA505 campaigns. For one, the Excel sheet lure spoofing Microsoft logos remained identical from a Sept. 2, 2020 campaign to the one used in an Oct. 6, 2021 campaign, as shown in the figure below.


Other parallels involve domain-naming conventions and code reuse that Proofpoint researchers found in parts of the delivery chain, such as in multiple parts of the landing page.


Macros for the Win
------------------


Unwitting victims have to enable macros after opening the malicious Excel files in order for the malware writers to win the day. “The code responsible for downloading the next stage MSI file was typically lightly obfuscated with filler characters, string reversing or similar simple functions and hidden in the document Comments, Title, in a Cell or other locations,” the analysis noted.


Expect More of the Same
-----------------------


Given that TA505 changes TTPs and that they’re “considered trendsetters in the world of cybercrime,” Proofpoint doesn’t expect them to go away anytime soon. “This threat actor does not limit its target set, and is, in fact, an equal opportunist with the geographies and verticals it chooses to attack” analysts noted. “This combined with TA505’s ability to be flexible, focusing on what is the most lucrative and shifting its TTPs as necessary, make the actor a continued threat.”


They predicted that the future probably holds yet more novelty from the ever-shifting tricksters, Proofpoint researchers said: “[We] expect TA505 to continue to adjust its operations and methods always with an eye to financial gain. Using intermediate loaders in its attack chain is also likely to become a longer-term technique employed by the threat actor.”  

***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Proofpoint]] [[TA505]] [[malware]] [[FlawedGrace]] [[“The]] [[noted.]] [[Rebol]] [[RAT,]] [[emails]] [[MSI]] [[ThreatPost]]
