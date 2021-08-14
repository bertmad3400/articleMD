# Ransomware Payments Explode Amid ‘Quadruple Extortion’
### Unit 42 puts the average payout at over half a million, while Barracuda has tracked a 64 percent year over year spike in the number of attacks. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168622)
+ Date: August 12, 2021  12:06 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/12114419/extortion-e1628783070711.jpeg)
Two reports slap hard figures on what’s already crystal clear: Ransomware attacks have skyrocketed, and ransomware payments are the comet trails that have followed them skyward.


The average ransomware payment spiked 82 percent year over year: It’s now over half a million dollars, according to the [first-half 2021 update](https://www.paloaltonetworks.com/blog/2021/08/ransomware-crisis/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+PaloAltoNetworks+%28Palo+Alto+Networks+Research+Center%29) report put out by Palo Alto Networks’ Unit 42. As far as the sheer multitude of attacks goes, Barracuda researchers on Thursday [reported](https://blog.barracuda.com/2021/08/12/threat-spotlight-ransomware-trends/) that they’ve identified and analyzed 121 ransomware incidents so far in 2021, a 64 percent increase in attacks, year-over-year.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


What’s helped to intensify extortion payments is the fact that cybercriminals have been pouring money into “highly profitable ransomware operations,” Unit 42 researchers wrote, including a new, disturbing trend: The rise of “quadruple extortion.”


Thumbscrews Have Quadrupled
---------------------------


[Double extortion](https://threatpost.com/double-extortion-ransomware-attacks-spike/154818/) has been around for more than a year: That’s when threat actors not only paralyze a victim’s systems and/or data but also threaten to leak compromised data or use it in future spam attacks if victims balk at paying extortion demands.


But during the first half of 2021, Unit 42 researchers observed ransomware groups commonly using as many as four techniques to turn the thumbscrews on victims, adding denial-of-service (DoS) attacks and harassment of a victim’s connections to the pain:


These “increasingly aggressive” tactics have fattened ransoms that were already increasingly engorged. Unit 42 reported last year that the average payment last year had surged 171 percent, to more than $312,000. During the first half of this year, that shot up to a record $570,000.


“While it’s rare for one organization to be the victim of all four techniques, this year we have increasingly seen ransomware gangs engage in additional approaches when victims don’t pay up after encryption and data theft,” Unit 42 reported.


“Among the dozens of cases that Unit 42 consultants reviewed in the first half of 2021, the average ransom demand was $5.3 million. That’s up 518 percent from the 2020 average of $847,000,” researchers observed.


More statistics include the highest ransom demand of a single victim spotted by Unit 42, which rose to $50 million in the first half of 2021, up from $30 million last year. So far this year, the largest payment confirmed by Unit 42 was the $11 million that [JBS SA disclosed](https://www.wsj.com/articles/jbs-paid-11-million-to-resolve-ransomware-attack-11623280781) after a [massive attack](https://threatpost.com/revil-ransomware-ground-down-jbs-sources/166597/) in June. Last year, the largest payment Unit 42 observed was $10 million.


Barracuda has also tracked a spike in ransom demands: In the attacks that it’s observed, the average ransom ask per incident was more than $10 million, with only 18 percent of the incidents involving a ransom demand of less than that. Meanwhile 30 percent of the incidents had greater than $30 million ransom asks.


But for its part, Barracuda traced the cause of spiked extortion demands to the wider adoption of cryptocurrency. It said that this increased prevalence of cryptocurrency has led to “a[correlation of increased ransomware attacks](https://blog.barracuda.com/2021/06/29/threat-spotlight-cryptocurrency-email-threats/) and higher ransom amounts. With increased crackdown on bitcoin and successful tracing of transactions, criminals are starting to provide alternative payments methods, such as the REvil ransomware gang asking for Monero instead of Bitcoin.”


REvil’s New Tactic: Dangling a Pricey Decryptor Key
---------------------------------------------------


Unit 42 researchers also alluded to a new tactic that REvil pulled out of its hat: After attacking Kaseya and its customers, REvil operators offered to sell a universal decryption key that would unlock all organizations affected by the attack, for $70 million – an asking price it quickly [dropped to $50 million](https://twitter.com/jackhcable/status/1411906687968161792).


That would have helped a lot of Kaseya’s customers, many of which were managed service providers (MSPs) that use the company’s VSA product. At least [60 customers in 22 countries](https://threatpost.com/kaseya-patches-zero-day-exploits/167548/) were hit in the spate of worldwide cyberattacks on July 2. Eventually, Kaseya did [get its hands on a decryptor.](https://threatpost.com/kaseya-universal-decryptor-revil-ransomware/168070/) 


081221 13:14 UPDATE: The original story misstated the facts around Kaseya’s possible payment for a decryptor. In fact, Kaseya published a statement on July 26 on its [VSA updates page,](https://www.kaseya.com/potential-attack-on-kaseya-vsa/) emphatically saying that it did not pay for the key: “Kaseya did not pay a ransom – either directly or indirectly through a third party – to obtain the decryptor.”


(A purported master key was [leaked online](https://threatpost.com/kaseyas-master-key-to-revil-attack-leaked-online/168565/) earlier this week, but researchers said that the decryptor is of little use to other companies hit in the attacks, which were unleashed before the notorious ransomware group [went dark](https://threatpost.com/ransomware-revil-sites-disappears/167745/).)


Barter Hard
-----------


The drop in asking price for REvil’s decryptor is mirrored by other instances of shrinking ransom demands. Barracuda pointed out several instances of ransomware gangs responding to negotiation tactics, including:


“The initial ransom ask may not be the final ask, so if they’re planning to pay, it is important for ransomware victims to exercise negotiation options,” according to Barracuda’s Fleming Shi. “The outcome can be savings in the millions.”


Who’s Getting Picked On
-----------------------


In his Thursday [post](https://blog.barracuda.com/2021/08/12/threat-spotlight-ransomware-trends/), Shi said that the ransomware thugs are picking on victims of all sizes. “The grim outlook for the future of ransomware leaves no one spared from financial damage or brand-crushing headlines,” Shi wrote. “Ransomware criminals are penetrating the foundation of our digital economy, from trusted software vendors to IT service providers.”


While ransomware gangs are still “heavily targeting” municipalities, healthcare and education, attacks on other businesses are “surging,” the researcher said. “Attacks on corporations, such as infrastructure, travel, financial services, and other businesses, made up 57 percent of all ransomware attacks between August 2020 and July 2021, up from just 18 percent in our 2020 study. Infrastructure-related businesses account for 10 percent of all the attacks we studied.”


After analyzing more than 120 incidents from August 2020 until July 2021, Barracuda’s research team found that ransomware attacks increased 64 percent year over year, and that REvil and DarkSide were responsible for 27 percent of those attacks.


A multiplier effect is brought into play, given that ransomware attacks are “quickly evolving to software supply-chain attacks, which reach more businesses in a single attempt,” Shi explained, with Kaseya being just one case in point. Others are the [airline industry](https://threatpost.com/supply-chain-attack-airlines-state-actor/166842/) and the JBS Foods attacks, the latter of which led to the meat supplier being forced to [shut down operations](https://threatpost.com/cyberattack-meat-producer-shut-down/166560/) in the U.S. and Australia.


While the U.S. is still in attackers’ crosshairs, Barracuda found that ransomware attacks are proliferating across the globe. “Just under half of the attacks in the past 12 months hit U.S organizations (44 percent). In comparison, 30 percent of the incidents happened in EMEA, 11 percent were in Asia Pacific countries, 10 percent were in South America, and 8 percent were in Canada and Mexico,” Shi said.


The Ransomware Crystal Ball
---------------------------


Unit 42 predicted that ransom demands will continue to spiral upwards, but that some gangs will continue to focus on smaller businesses that can’t afford to invest heavily in cybersecurity defenses.


“So far this year, we have observed groups, including NetWalker, SunCrypt and LockBit, demanding and taking in payments ranging from $10,000 to $50,000,” researchers noted. “While they may seem small compared to the largest ransoms we observed, payments that size can have a debilitating impact on a small organization.”


Unit 42 also expected to see more targeting of hypervisors, given that can lead to corruption of multiple virtual instances running on a single server. One example was seen last month, when researchers observed a [Linux Variant of REvil ransomware](https://threatpost.com/linux-variant-ransomware-vmwares-nas/167511/) targeting VMware’s ESXi virtual machine management software and network attached storage (NAS) devices that run on the Linux operating system (OS).


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[ransomware]] [[year,]] [[REvil]] [[attacks,]] [[Kaseya]] [[million.]] [[“The]] [[ThreatPost]]
