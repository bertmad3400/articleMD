# MacOS Being Picked Apart by $49 XLoader Data Stealer
### Cheap, easy & prolific, the new version of the old FormBook form-stealer and keylogger has added Mac users to its hit list, and it’s selling like hotcakes. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167971)
+ Date: July 21, 2021  6:00 am
+ Author: Lisa Vaas


## Article:
There’s a new version of the old [FormBook](https://threatpost.com/new-formbook-dropper-harbors-persistence/145614/) form-stealer and keylogger that’s added Mac users to its hit list, and it’s selling like hotcakes on the darknet for as low as $49.


It’s not only cheap; it’s easy. The data stealer is distributed in the form of malware-as-a-service ([MaaS](https://encyclopedia.kaspersky.com/glossary/malware-as-a-service-maas/)) and stands out from competing malware by being drop-dead simple to use, outfitting even code dummies with a multipurpose malware tool.


In a [report](https://research.checkpoint.com/2021/top-prevalent-malware-with-a-thousand-campaigns-migrates-to-macos) posted on Wednesday, analysts at Check Point Research (CPR) said that the new strain of FormBook – which mainly targeted Windows users when it first popped up on hacking forums in 2016 – is named XLoader. According to the report, FormBook disappeared from malware markets in 2018, then rebranded to XLoader in 2020.



Over the past six months, XLoader’s been a busy beaver, prolifically targeting Window users but also gnawing on its newfound love: namely, “to CPR’s surprise,” Mac users.


XLoader licenses start at $49: a price that will get even the most inexperienced and poorly funded cyberattackers a tool that they can use to harvest log-in credentials, collect screenshots, log keystrokes and execute malicious files.


CPR has tracked XLoader requests flooding in from eager attackers in 69 countries. Most of the targets – 53 percent – are in the U.S., including both Mac and Windows users.


The breakdown of victims by country is presented in the bar graph below:


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/20191027/CPR-Formbook-victims-figure-1.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/20191027/CPR-Formbook-victims-figure-1.png)


Victims are tricked into downloading XLoader via spoofed emails that contain malicious Microsoft Office documents.


From Humble Keylogger to Red-Hot Malware
----------------------------------------


As of December, as CPR [reported](https://www.checkpoint.com/press/2021/december-2020s-most-wanted-malware-emotet-returns-as-top-malware-threat/) at the time, FormBook was the third most prevalent malware family. It was outpaced only by Emotet at No. 1 (the servers for which were globally [dismantled](https://threatpost.com/emotet-takedown-infrastructure-netwalker-offline/163389/) in January) and the [TrickBot](https://threatpost.com/trickbot-banking-trojan-module/167521/) banking trojan/ransomware malware, which ranked No. 2.


[AnyRun Malware Trends Tracker](https://any.run/malware-trends/) backs that up: As of Tuesday evening, FormBook was ranked third most-spotted sample out of millions in the preceding week, and it was climbing in popularity. Between June 2020 and June 2021, AnyRun ranked FormBook as the fourth most prevalent malware family.


This isn’t what the malware author had in mind. At first, it was just supposed to be a keylogger – a cheap one, at that. At least back in 2016, attackers could rent FormBook MaaS for as little as $29/week.


But customers quickly spotted its potential to be used in broad spam campaigns for use across the world, CPR researchers explained. As the potential became reality, the author – “ng-Coder,” whom CPR researchers decided is a “he” – stopped selling FormBook. The author hadn’t wanted the tool to be used in email campaigns and had, in fact, banned customers from using it for spam. Ng-Coder made a final post in May 2018, and then the malware maker’s FormBook activity stopped.


Or, at least, his activity went dark. CPR researchers theorize that ng-Coder might have had his own plans for his creation, given analysis of domains linked to his email address, ng2coder [at] gmail.com. Sixteen unique command-and-control (C2) domains linked to that address were used in FormBook campaigns.


FormBook activity kept coming, but it had a bun in the oven. On Feb. 6, 2020, the rebranded XLoader offshoot was listed for sale in an underground forum – the same one that FormBook was sold on – under a new avatar. (CPR notes that XLoader malware for PCs and Mac shouldn’t be confused with [XLoader malware for Android](https://threatpost.com/roaming-mantis-swarms-globally-spawning-ios-phishing-cryptomining/132149/) [aka Roaming or MoqHao], a backdoor trojan and Android malware that uses Domain Name System (DNS) spoofing to distribute infected Android apps.)


CPR researchers were intrigued by XLoader’s ability to operate in macOS, which was “one of the most exciting things about the new malware,” they enthused. “With approximately 100 million users operating macOS in 2018 ([as reported by Apple](https://appleinsider.com/articles/18/10/30/apple-passes-100m-active-mac-milestone-thanks-to-high-numbers-of-new-users)), this was definitely a promising new market for the malware to enter.”


Enter it did, obviously, given how it’s shot up in malware rankings.


Standard-Issue CYA Instructions
-------------------------------


CPR recommends that we can all stop feeding XLoader’s success rate by following some standard-issue precautions for both Mac and Windows users:


As far as detection and removal goes, this malware is notoriously tough to detect, though AnyRun does offer the following video for instructions on detecting FormBook. For what it’s worth, the XLoader offspring does share the same code base as its FormBook progenitor.


Then again, you should maybe just leave it up to the pros, CPR analysts suggested. “Since this malware is [stealthy] in nature, it is likely difficult for a ‘non-technical’ eye to recognize whether they have been infected,” they opined. “Therefore, if you suspect you have been infected it would be wise to consult with a security professional or use third-party tools and protections designed to identify, block and even remove this threat from your computer.”


For more technical details to assist in detection and removal, CPR recommended using the AutoRun feature of Windows Explorer to:


Yaniv Balmas, CPR head of cyber research, called XLoader “far more mature and sophisticated than its predecessors,” given that it’s made itself at home on MacOS computers: an environment that historically hasn’t been cozy for malware.


“MacOS malware hasn’t been that common,” Balmas said in a statement. “They usually fall into the category of ‘spyware’, not causing too much damage.”


But XLoader is just the latest example of how the gap has steadily been closing when it comes to prevalence of PC vs. macOS malware, Balmas continued. “The truth is that MacOS malware is becoming bigger and more dangerous,” he said. “Our recent findings are a perfect example and confirm this growing trend.”


People love their Macs. Hence, the malware situation is bound to get worse, Balmas predicted. “With the increasing popularity of MacOS platforms, it makes sense for cyber criminals to show more interest in this domain, and I personally anticipate seeing more cyber threats following the FormBook malware family. I would think twice before opening up any attachments from emails I get from senders I don’t know.”


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[malware]] [[FormBook]] [[XLoader]] [[CPR]] [[Windows]] [[Balmas]] [[MacOS]] [[AnyRun]] [[Android]] [[macOS]] [[ThreatPost]]
