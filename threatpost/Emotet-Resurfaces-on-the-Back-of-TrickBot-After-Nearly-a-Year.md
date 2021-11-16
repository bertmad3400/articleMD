# Emotet Resurfaces on the Back of TrickBot After Nearly a Year
### Researchers observed what looks like the Emotet botnet – the “world’s most dangerous malware” – reborn and distributed by the trojan it used to deliver.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176362)
+ Date: November 16, 2021  8:57 am
+ Author: Elizabeth Montalbano


## Article:
![Trojan malware](https://media.threatpost.com/wp-content/uploads/sites/103/2020/01/22100148/trojan-malware.jpg)
Emotet, one of the most prolific and disruptive botnet malware-delivery systems, appears to be making a comeback after [nearly a year](https://threatpost.com/emotet-returns-100k-mailboxes/162584/) of inactivity, researchers have found.


A team of researchers from [Cryptolaemus](https://twitter.com/Cryptolaemus1/status/1460302706954981385), [G DATA](https://cyber.wtf/2021/11/15/guess-whos-back/) and [AdvIntel](https://twitter.com/VK_Intel/status/1460308855129313281) recently observed the TrickBot trojan launching what appears to be a new loader for the notorious malware, they said [separately](https://twitter.com/Cryptolaemus1/status/1460302706954981385) on Twitter and in a blog post.


“We have reason to assume with high confidence that [#Emotet](https://twitter.com/hashtag/Emotet?src=hashtag_click) is active again and currently distributed via [#Trickbot](https://twitter.com/hashtag/Trickbot?src=hashtag_click),” [G DATA Advanced Analytics](https://www.gdata-advancedanalytics.de/) [posted](https://twitter.com/gdata_adan/status/1460298879090503681) on its [Twitter feed](https://twitter.com/gdata_adan).


“2021-11-14: The ‘[#Emotet](https://twitter.com/hashtag/Emotet?src=hashtag_click) partner ($) loader’ program appears resorcing [SIC] from existing [#TrickBot](https://twitter.com/hashtag/TrickBot?src=hashtag_click) infections,” [AdvIntel](https://www.advintel.io/) CEO [Vitali Kremez](https://twitter.com/VK_Intel) also confirmed [via Twitter](https://twitter.com/VK_Intel/status/1460308855129313281). “TrickBot launched what appears to be the newer Emotet loader.”


[A blog post](https://cyber.wtf/2021/11/15/guess-whos-back/) from researchers at G DATA has the most detailed information about what went down. It explains that on Sunday at around 9:26 UTC, researchers observed on several TrickBot trackers an attempt to download a DLL to the system, G DATA’s Luca Ebach wrote.


“According to internal processing, these DLLs have been identified as Emotet,” he wrote.


Because Emotet was largely dismantled earlier this year by an international law-enforcement effort, researchers said they were “suspicious about the findings” and conducted further verification of the activity. After doing so, they said with “high confidence” that “the samples indeed seem to be a re-incarnation of the infamous Emotet” but will be conducting further analysis, Ebach wrote.


**Evolution of a Cyberthreat**
------------------------------


Emotet started life as a banking trojan in 2014 and has continually evolved to become a full-service threat-delivery mechanism. It can install a collection of malware on victim machines, including information stealers, email harvesters, self-propagation mechanisms and ransomware, the last of which is at a [record high](https://threatpost.com/ransomware-volumes-record-highs-2021/168327/) in terms of volume and currently the cyber threat most worrying [international law enforcement](https://threatpost.com/feds-offer-10-million-bounty-on-darkside-info/176030/).


Emotet was last seen in volume [hitting 100,000 target mailboxes](https://threatpost.com/emotet-returns-100k-mailboxes/162584/) a day to deliver [TrickBot](https://threatpost.com/trickbot-cybercrime-elite-affiliates/175510/), Qakbot and Zloader in December 2020 ahead of the Christmas holidays. Before that in October it [targeted](https://threatpost.com/emotet-email-dnc-volunteers/159758/) volunteers for the Democratic National Committee (DNC); previously, it became [active in July](https://threatpost.com/emotet-returns-in-malspam-attacks-dropping-trickbot-qakbot/157604/) of that year after a five-month hiatus, dropping the TrickBot trojan.


Emotet appeared to be [put out of commission](https://threatpost.com/emotet-takedown-infrastructure-netwalker-offline/163389/) by an international law-enforcement collaborative takedown of a network of hundreds of botnet servers supporting the system in January 2021. The effort eliminated active infections on more than 1 million endpoints worldwide, they said.


Now it appears to have resurfaced using familiar partner-in-crime TrickBot, with the two having a [history of working together.](https://threatpost.com/un-weathers-emotet-trickbot-malware/151894/) Often, it was Emotet using its vast network to deliver TrickBot as a payload in [targeted email phishing campaigns](https://threatpost.com/un-weathers-emotet-trickbot-malware/151894/), though TrickBot also in the past has delivered Emotet samples – which appears to be the case once more.


Researchers detailed the similarities between previous samples of Emotet and the one they observed being dropped by TrickBot on Sunday. One hallmark is that the network traffic originating from the sample closely resembles what has been observed as Emotet behavior previously, as [described by Kaspersky Labs](https://securelist.com/the-chronicles-of-emotet/99660/), Ebach wrote.


“The URL contains a random resource path and the bot transfers the request payload in a cookie,” he wrote. “However, the encryption used to hide the data seems different from what has been observed in the past. Additionally, the sample now uses HTTPS with a self-signed server certificate to secure the network traffic.”


Another “notable characteristic” of Emotet was “the heavy use of control-flow flattening to obfuscate the code,” Ebach noted. The current sample also contains flattened control flows, he said.


**Phishing Onslaught Ahead?**
-----------------------------


The news is already sending shivers down the spines of security professionals, who, unsurprised by Emotet’s resurfacing, are well familiar with the disruption it can wreak when it’s at its full power.


“Emotet was once the ‘world’s most dangerous malware,'” noted James Shank, senior security evangelist and chief architect of community service at security firm [Team Cymru](https://team-cymru.com/), in an email to Threatpost. However, it will be a while before its latest version will be capable of a similar level of havoc-wreaking, he added.


Shank said it’s too soon to tell from the sample disclosed by researchers what this new version of Emotet will look like, though there does appear to be code overlap between the old version and the latest. “Old signatures written to detect the first version of Emotet also detect this variant, in some cases,” he said.


Fortunately, as the botnet will need some time to gain strength, organizations still have some breathing room to shore up defenses, noted another security professional.


“It will take some time to build up to its previous size,” Eric Kron, security awareness advocate at security firm [KnowBe4](http://www.knowbe4.com/), wrote in an email to Threatpost. “Unfortunately, we can expect to see these infected devices used to increase the spread of ransomware, which is already out of control.”


Organizations can already get ahead of the threat by focusing on training their workforces about the dangers of email threats as well as shoring up network monitoring, since Emotet spreads infections predominantly through phishing campaigns, Kron said.


“Wise organizations will engage users in security awareness training and simulated testing campaigns in an effort to help them hone their skills at spotting and reporting phishing emails,” he said. “In addition, tracking newly discovered command and control servers, alerting on and blocking traffic to them, can reduce the risk of infection greatly.”


***Want to win back control of the flimsy passwords standing between your network and the next cyberattack? Join Darren James, head of internal IT at Specops, and Roger Grimes, data-driven defense evangelist at KnowBe4, to find out how during a free, LIVE Threatpost event,*** [***“Password Reset: Claiming Control of Credentials to Stop Attacks,”***](https://bit.ly/3bBMX30) ***on Wed., Nov. 17 at 2 p.m. ET. Sponsored by Specops.***


[***Register NOW***](https://bit.ly/3bBMX30) ***for the LIVE event!***




#### Tags:
[[Emotet]] [[TrickBot]] [[wrote.]] [[said.]] [[Ebach]] [[botnet]] [[phishing]] [[ThreatPost]]
