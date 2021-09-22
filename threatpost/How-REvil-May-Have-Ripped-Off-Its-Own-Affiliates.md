# How REvil May Have Ripped Off Its Own Affiliates
### A newly discovered backdoor and double chats could have enabled REvil ransomware-as-a-service operators to hijack victim cases and snatch affiliates’ cuts of ransom payments. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=174887)
+ Date: September 22, 2021  12:50 pm
+ Author: Lisa Vaas


## Article:
There’s no honor between thieves, but this is beyond rude: Malware specialists have found evidence of how REvil’s leadership may have screwed their own affiliates out of their cut of ransomware payouts.


Malware specialists researching newly available samples from [REvil](https://threatpost.com/kaseya-patches-zero-days-revil-attacks/167670/) – aka Sodinokibi, a [once-major](https://threatpost.com/jbs-paid-11m/166767/), now [sort-of reborn](https://threatpost.com/revil-back-coder-decryptor-key/169403/) ransomware-as-a-service (RaaS) player – have identified a backdoor that may have enabled the original gang to hijack chats with victims so as to scoop up affiliates’ cut of ransom payments.


Yelisey Boguslavskiy, head of research at the cyber risk prevention firm Advanced Intelligence, said in a [LinkedIn update](https://www.linkedin.com/feed/update/urn:li:activity:6845837344713519104/) on Monday that the backdoor also enabled REvil operators to decrypt workstations and files.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Backdoors and encryption are nothing new for a ransomware gang, but by using this backdoor, REvil could hijack cases while the victims actively negotiated with the RaaS’s affiliates. That would enable REvil operators to filch affiliates’ cut of the pie, which is 70 percent of ransom payments, Boguslavskiy told Threatpost on Wednesday.


How Much ‘Should’ REvil Affiliates Get
--------------------------------------


The way the payout is supposed to go is that when an affiliate compromises a network and digs in to secure its presence, REvil leadership hands the affiliate a payload of malware to infect that network, Boguslavskiy explained.


Next, if a victim pays the ransom, the affiliate is supposed to get 70 percent of it for doing all the dirty work of network compromise, data stealing and encryption. REvil leadership pockets the remaining 30 percent in exchange for providing the ransomware payload that the affiliates use to seize control of victims’ data and systems.


In REvil’s case, that payload has a history of major hits, including, most recently, [Kaseya](https://threatpost.com/kaseya-patches-zero-days-revil-attacks/167670/) with its many managed service provider (MSP) customers and the global meat supplier [JBS Foods](https://threatpost.com/jbs-paid-11m/166767/).


Then again, if leadership decides to scam the affiliate instead of paying out, they pocket the whole enchilada: the affiliates’ 70 percent cut plus REvil operators’ 30 percent cut = 100 percent and “so long, sucker.”


How to RE-ip Off Affiliates: Double Chats & a Backdoor
------------------------------------------------------


In recently acquired malware samples – taken from campaigns waged by both the original REvil operators and by the newcomer who started [running the show](https://threatpost.com/revil-back-coder-decryptor-key/169403/) after the [gang’s servers’ went bye-bye](https://threatpost.com/ransomware-revil-sites-disappears/167745/) in July, AdvIntel researchers identified the [backdoor](https://www.linkedin.com/feed/hashtag/?keywords=backdoor&highlightedUpdateUrns=urn%3Ali%3Aactivity%3A6845837344713519104) that could have enabled REvil leadership to decrypt workstations and files. “By using this backdoor, REvil can hijack victim cases during active negotiations with affiliates and obtain the 70% of ransom payments that are supposed to go to the affiliates,” Boguslavskiy explained.


AdvIntel had already been aware that REvil has been using double-chats: That’s when two identical chats are open with the victim, one by the affiliate and another by REvil leadership.


The threat intelligence firm doesn’t have direct evidence of REvil leadership having used the backdoor to shut down the affiliate chat, to then imitate a victim who’s decided to quit the negotiations without paying, and to then continue to negotiate with the victim to get the full income, but Boguslavskiy considers double chats and a backdoor to be “significant evidence of REvil’s practices as affiliate scammers.”


AdvIntel derived the evidence based on threat actor engagements. The only way to get more direct evidence than that would be to embed yourself in the ransomware gang’s leadership, Boguslavskiy noted: “To have the direct evidence, one would need to be within the REvil’s leadership, as they are the ones creating the double chats.”


Why the Backdoor?
-----------------


Besides the double-chat setup, the backdoor itself may serve the same purpose of affiliate case hijacking, Boguslavskiy said, as it enables secret decryption of files when negotiations are complete.


AdvIntel found an interesting twist in the latest samples, coming after REvil shut down its servers in July: The backdoor has since been erased.


“It seems that the new samples were reworked and the backdoor was cleaned out,” Boguslavskiy said: what might be evidence of the new operator’s desire to start out with a clean slate as far as reputation on the underground goes.


“This evidence correlates with the underground’s approach to REvil as a talkative and perpetually lying group that should not be trusted by the community or even by its own members,” Boguslavskiy commented.


The new coder, who’s using the handle “REvil,” likely reworked the samples “to prevent the use of the backdoor against new victims by REvil’s former members who have backdoor access,” he conjectured. “But most importantly this is done to prevent decryption of victims by security teams, as the underground community believes that Bitdefender was able to obtain the backdoor key.”


BitDefender released [a universal, free decryptor key](https://threatpost.com/revil-sodinokibi-ransomware-universal-decryptor/169498/) for REvil ransomware last week.


Public Keys, Both Pre- and Post-Rebirth
---------------------------------------


AdvIntel provided this public key from the actor’s post, which is likely pre-REvil rebirth:


FF5EEDCAEDEE6250D488F0F04EFA4C957B557BDBDC0BBCA2BA1BB7A64D043A3D


The intelligence firm also provided the following hashes and samples that are likely also pre-REvil comeback and hence still contain the backdoor:


hxxps://www.virustotal[.]com/gui/file/12d8bfa1aeb557c146b98f069f3456cc8392863a2f4ad938722cd7ca1a773b39


hxxps://www.virustotal[.]com/gui/file/ea1872b2835128e3cb49a0bc27e4727ca33c4e6eba1e80422db19b505f965bc4


AdvIntel also provided new samples after the backdoor had been cleaned out:


hxxps://www.virustotal[.]com/gui/file/ab0aa003d7238940cbdf7393677f968c4a252516de7f0699cd4654abd2e7ae83


“Interestingly enough, the backdoor was only for Windows,” Boguslavskiy noted.


**Rule #1 of Linux Security:** No cybersecurity solution is viable if you don’t have the basics down. [**JOIN**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the [**4 Golden Rules of Linux Security**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar). Your top takeaway will be a Linux roadmap to getting the basics right! [**REGISTER NOW**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.




#### Tags:
[[REvil]] [[Boguslavskiy]] [[AdvIntel]] [[REvil’s]] [[ransomware]] [[Linux]] [[affiliates’]] [[Threatpost]] [[ThreatPost]]
