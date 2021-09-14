# REvil’s Back; Coder Fat-Fingered Away Its Decryptor Key?
### How did Kaseya get a universal decryptor after a mind-bogglingly big ransomware attack? A REvil coder misclicked, generated & issued it, and “That’s how we sh*t ourselves.”

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169403)
+ Date: September 13, 2021  2:59 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/13145703/baby-hand-fingers-skin-e1631559437454.jpeg)
UPDATE


The REvil ransomware gang’s tentacles shot out yet again last week, with the ransomware gang’s servers back online, a fresh victim listed on its site, ransomware payments back up and flowing, and an explanation of why it took [a two-month hiatus.](https://threatpost.com/ransomware-revil-sites-disappears/167745/)


A purported REvil representative also addressed a slew of questions, including:


***Q:** How did Kaseya, an IT solutions developer for managed service providers (MSPs), get its hands on a [universal decryptor key](https://threatpost.com/kaseyas-master-key-to-revil-attack-leaked-online/168565/) that was leaked online after REvil launched one of the [biggest ransomware sprees](https://threatpost.com/kaseyas-master-key-to-revil-attack-leaked-online/168565/) in history against it and 60 of its MSP clients on July 2?*


***A:**  The short answer: A REvil coder screwed up.*


As [Flashpoint](https://threatpost.com/kaseyas-master-key-to-revil-attack-leaked-online/168565/) has reported, REvil posted twice on the Exploit underground forum on Friday, Sept. 10, to clarify what happened during that Kaseya-related key generation process and how a coder fat-fingered the generation and leaking of the universal key. 


Flashpoint provided this lightly edited translation: “One of our coders misclicked and generated a universal key, and issued the universal decryptor key along with a bunch of keys for one machine. That’s how we sh*t ourselves.”


REvil’s alleged new rep, operating under the alias “REvil,” explained that the criminal organization’s encryption process allows for generation of either a universal decryptor key or individual keys for each of a victim’s encrypted machines. In the process of generating the keys for Kaseya and its victimized MSPs, REvil had to generate between 20 and 500 decryption keys for each individual victim, because the victims in that attack all had networks of different sizes. 


The fat-fingered claim is suspect at best, according to underground sources speaking to Advanced Intelligence.


“All actors [including LockBit representatives and the administrator of the XSS Dark web market] agree that the explanation provided by the ‘new; representative regarding the misclick generation of the decryption key is absolutely ridiculous and doesn’t make any sense in the context of how contemporary ransomware operations work,” Yelisey Boguslavskiy, head of research at Advanced Intelligence, told Threatpost.


He noted that REvil has a reputation for making outlandish claims.


“They are perceived as pathological liars who are not as merely capable as what they state about themselves,” he said. “UNKN’s allegation that REvil has access to US military infrastructure turned into a meme and has been actively referenced during these discussions as a way to illustrate how ridiculously flamboyant and ungrounded anything coming from REvil can be.”


REvil Used Backups to Crawl Back
--------------------------------


The new representative explained that REvil managed to come back online using the criminal affiliation’s backups. 


According to Flashpoint analysts, this is apparently the first time that REvil has appeared on the Russian-language underground forum Exploit since its servers slipped offline without an explanation in July: A disappearance that followed fast on the heels of the high-profile Kaseya attack. 


After that attack, the gang’s Tor servers and infrastructure powered down, and the security researcher known as  [@Pancak3](https://threatpost.com/kaseyas-master-key-to-revil-attack-leaked-online/168565/) discovered the master decryption key had been leaked to an underground forum. The researcher posted a screenshot to the key on [Twitter](https://threatpost.com/kaseyas-master-key-to-revil-attack-leaked-online/168565/) and [GitHub](https://threatpost.com/kaseyas-master-key-to-revil-attack-leaked-online/168565/)


It was a Kaseya attack-specific key, and it worked to untangle the victims of that attack. Nobody at the time was quite sure how Kaseya may have gotten the key, but the company has maintained that it came from a “trusted third party.”


REvil Back Up
-------------


The screenshot below, captured by Flashpoint, depicts REvil’s new registration on Exploit. It was taken at approximately 10:00 a.m. EST last Thursday, Sept. 9. 


Two days earlier, on Tuesday, Sept. 7, REvil’s leak site – known as Happy Blog – was back up, and it’s now “fully operational,” according to Flashpoint: “For all intents and purposes, it appears that REvil is fully operational after its hiatus,” Flashpoint researchers wrote. 


On that same day, REvil’s Tor payment/negotiation site also suddenly sprang back to life. By Thursday, victims could once again log in and negotiate with the group. As it was, those victims had been [left high and dry](https://threatpost.com/kaseyas-master-key-to-revil-attack-leaked-online/168565/) after REvil’s disappearance on July 13, which left them with no decryption key and no ability to negotiate the ransom so they could get one. 


As BleepingComputer reported, prior victims have had their ransom-payment timers reset.


At this point, there’s evidence of active development, too. On Thursday, Sept. 9, a new REvil ransomware sample, compiled on Sept. 4, was uploaded to VirusTotal.


Also, on Saturday, the gang published screenshots of stolen data for the new victim on its data leak site as further proof that REvil is, in fact, back in action. 


However, Advanced Intel’s Boguslavskiy is skeptical of the claims that the group is back at full force.


“UNKN who was the core developer has disappeared. It is very unlikely that even if other REvil members indeed allied to re-establish the gang, they will be able to successfully develop the ransomware without UNKN,” he told Threatpost.


He added, “Moreover, considering the recent development concerning [BlackMatter](https://threatpost.com/ransomware-gangs-haron-blackmatter/168212/) and its evolution, it is very likely that other elite REvil developers have merged with this new group. This leaves the ‘new’ REvil with mostly mediocre specialists. Most likely, the low-tier REvil affiliates simply united to exploit the brand and obtained the widely available source code as well as the Happy log hosting (the same situation was seen with Babuk ransomware).”


Why REvil Shut Up Shop in the First Place
-----------------------------------------


On Thursday, the new rep – REvil – explained in posts to criminal forums that the group had briefly yanked its servers offline because they thought that the former rep – Unk/Unknown – had been arrested and that REvil’s servers were compromised.


[Advanced Intel captured and translated some of the new REvil rep’s posts, which the cybercrime and adversarial disruption firm shared with](https://threatpost.com/kaseyas-master-key-to-revil-attack-leaked-online/168565/) [BleepingComputer](https://threatpost.com/kaseyas-master-key-to-revil-attack-leaked-online/168565/). They’re shown below: 


Advanced Intel’s translation: 


*As Unknown (aka 8800) disappeared, we (the coders) backed up and turned off all the servers. Thought that he was arrested. We tried to search, but to no avail. We waited – he did not show up and we restored everything from backups.*


*After UNKN disappeared, the hoster informed us that the Clearnet servers were compromised and they deleted them at once. We shut down the main server with the keys right afterward.*


*Kaseya decryptor, which was allegedly leaked by the law enforcement, in fact, was leaked by one of our operators during the generation of the decryptor. – REvil*


Law enforcement getting their hands on the decryptor and shutting down the servers was one possibility that was floated after REvil’s servers went dark. However, multiple sources have told BleepingComputer, REvil’s disappearance “surprised law enforcement as much as everyone else.”


Making Nice With Unhappy Affiliates
-----------------------------------


Besides re-emerging, in whatever form it has, REvil is apparently looking to re-establish its cred. It looks like the reborn REvil – which is a ransomware-as-a-service (RaaS) player that rents out its ransomware gear to affiliates – is trying to patch things up with disgruntled affiliates who grumbled about missing payouts after the group’s disappearance. 


When Happy Blog popped back up, some threat actors opened arbitration cases against REvil on underground forums. 


Flashpoint analysts observed one threat actor, “boriselcin,” who opened an arbitration case against REvil spokesperson UNKN, aka [Unknown](https://threatpost.com/kaseyas-master-key-to-revil-attack-leaked-online/168565/), on the Russian-language forum XSS. The actor claimed that UNKN owed them money and wanted to be compensated now that the group is back up and running. 


But by Thursday, Sept. 8, the squall had blown over, as boriselcin closed the claim saying it had been resolved. 


Flashpoint predicted that more former affiliates may file similar cases, however. 


***This story was updated at 5:00 p.m. ET on September 13, 2021, to include comments from Advanced Intel’s Boguslavskiy.***


 


**It’s time to evolve threat hunting into a pursuit of adversaries.**[**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**Threatpost and Cybersixgill for**[**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**and get a guided tour of the dark web and learn how to track threat actors before their next attack.**[**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with independent researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[REvil]] [[ransomware]] [[REvil’s]] [[Sept.]] [[Flashpoint]] [[Kaseya]] [[Thursday,]] [[decryptor]] [[gang’s]] [[key,]] [[ThreatPost]]
