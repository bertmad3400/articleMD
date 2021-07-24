# Kaseya Obtains Universal Decryptor for REvil Ransomware
### The vendor will work with customers affected by the early July spate of ransomware attacks to unlock files; it’s unclear if the ransom was paid.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168070)
+ Date: July 23, 2021  8:21 am
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2020/04/30081507/Ransomware-Key.jpg)
Kaseya has obtained a master decryptor key for the REvil ransomware that locked up the systems of at least 60 of its customers in a spate of worldwide cyberattacks on July 2.


The attacks, which exploited [now-patched zero-days](https://threatpost.com/kaseya-patches-zero-days-revil-attacks/167670/) in the Kaseya Virtual System/Server Administrator (VSA) platform, affected Kaseya customers [in 22 countries](https://threatpost.com/kaseya-patches-zero-day-exploits/167548/) using the on-premises version of the platform – many of which are managed service providers (MSPs) who use VSA to manage the networks of other businesses. In addition to the 60 direct customers, around 1,500 downstream customers of those MSPs were also affected.


The VSA software is used by Kaseya customers to remotely monitor and manage software and network infrastructure.



In the wake of the attacks, the REvil gang (aka Sodinokibi) demanded $70 million for a universal public decryption key that will remediate all impacted victims – a price that [one researcher said](https://twitter.com/jackhcable/status/1411906687968161792) was eventually lowered to $50 million.


Late on Thursday afternoon, the vendor announced via its [rolling advisory](https://helpdesk.kaseya.com/hc/en-gb/articles/4403440684689-Important-Notice-July-21st-2021) on the incident that it had obtained the decryptor “through a third party.” It’s unclear if the ransom was indeed paid.


“We can confirm that Kaseya obtained the tool from a third party and have teams actively helping customers affected by the ransomware to restore their environments, with no reports of any problem or issues associated with the decryptor,” it said. “Kaseya is working with Emsisoft to support our customer engagement efforts, and Emsisoft has confirmed the key is effective at unlocking victims…Customers who have been impacted by the ransomware will be contacted by Kaseya representatives.”


Deepening the mystery is the fact that REvil as a criminal organization [went dark July 13](https://threatpost.com/ransomware-revil-sites-disappears/167745/), when its sites vanished and representatives were banned on prominent underground forums.


Emsisoft isn’t releasing further details: “We are working with Kaseya to support their customer engagement efforts,” Emsisoft said in a statement given to Threatpost. “We have confirmed the key is effective at unlocking victims and will continue to provide support to Kaseya and its customers.”


Threatpost has reached out to Kaseya as well and will update this post with any additional information.


“The sudden appearance of this universal key suggests that it is possible that this ransom may have been paid, although it is likely that the ransom would have been negotiate to a lower price,” Ivan Righi, cyber-threat intelligence analyst at Digital Shadows, said via email.


**Despite Decryption, the Nightmare Isn’t Over**
------------------------------------------------


Even though the master decryption key has been acquired, the attack should not be considered to be over, researchers warned. For one thing, REvil is known for its double-extortion attacks, where company data is stolen in addition to being hit with ransomware.


“The group may still have copies of data stolen from victims,” Righi said. “The group could use this data to extort victims or auction off the data, as it has done in the past on its website Happy Blog.”


Erich Kron, security awareness advocate at KnowBe4, noted that remediation will take more than simply applying the unlocking mechanism to files.


“Significant damage has been done already in the way of downtime and recovery costs, both currently and in the future,” he noted via email. “Even with the data decrypted, there are significant costs associated with restoring devices and data. Simply decrypting the data does not resolve issues that remain, such as potentially installed back doors the attackers could use at a later date. This means there is still a lot of work ahead.”


Tim Wade, technical director on the CTO team at Vectra, said that there could be other nasty surprises for victims to watch out for following the attacks.


“From a distance, the emergence of a master key may appear more comforting than it should,” he warned. “The value of accelerating the restoration of data and services shouldn’t be trivialized, but it won’t exactly erase the already extensive cost of these attacks. And this is a cost carried both in terms of the historic disruption, but also given the proclivity of these criminal operators to leave lingering backdoors, the ongoing need to rebuild compromised infrastructure into a clean, trustworthy state. So yes, sidestepping how this key may have been acquired, it may have some positive outcomes but as they say – it isn’t over ’til it’s over.”


**Supply-Chain Attacks on MSPs Snowball**
-----------------------------------------


While this particular attack was far-reaching and significant, it’s not the first cyberattack to affect MSPs and their downstream customers this year. The Clop ransomware gang for instance went after the Accellion legacy FTA software for file transfers in February; multiple [Accellion FTA customers](https://threatpost.com/accellion-zero-day-attacks-clop-ransomware-fin11/164150/), including the Jones Day Law Firm, Kroger, Shell and Singtel were all affected.


The incidents point at a lesson for organizations of all sizes, researchers noted, when it comes to the MSP biz.


“Whenever an organization trusts external entities with the keys to their kingdom, they are undertaking a serious risk,” Kron said. “Likewise, when MSPs are given this access, it is imperative that they aggressively protect their customers. For organizations that have been taken down by ransomware due to the lack of backups, or if their backups were encrypted, leaving them vulnerable, this is a great time to have some hard discussions with their service providers in an effort to eliminate the threat in the future.”


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Kaseya]] [[ransomware]] [[MSPs]] [[REvil]] [[Emsisoft]] [[decryptor]] [[VSA]] [[Threatpost]] [[ThreatPost]]
