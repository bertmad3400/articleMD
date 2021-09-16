# REvil/Sodinokibi Ransomware Universal Decryptor Key Is Out
### Bitdefender worked with law enforcement to create a key to unlock victims  encrypted in ransomware attacks before REvil’s servers went belly-up on July 13.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169498)
+ Date: September 16, 2021  9:00 am
+ Author: Lisa Vaas


## Article:
REvil victims, your prayers have been answered: There’s a universal decryptor key waiting to free you.


Bitdefender is releasing a free, universal decryptor key to unlock data of victimized organizations that were encrypted by REvil/Sodinokibi ransomware attacks before the gang’s [servers went belly-up](https://threatpost.com/ransomware-revil-sites-disappears/167745/) on July 13.


The firm announced that it’s giving away the universal key on Thursday morning, mere days after REvil [reared its slimy head](https://threatpost.com/revil-back-coder-decryptor-key/169403/) again (though the underground considers it to probably be some mediocre, lower-tier REvil lackeys milking the name so as to pull an exit scam).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


This is the real deal, Bitdefender said, not the letdown of last month, when REvil victim Kaseya [got its hands on a master key](https://threatpost.com/kaseyas-master-key-to-revil-attack-leaked-online/168565/). At that time, it was first thought that the key could unlock all of the REvil attacks that occurred at the same time as the Kaseya one. Unfortunately, it soon became clear to researchers that the decryptor was only for the files locked in the Kaseya attack.


Bitdefender, a Romania-based cybersecurity firm, didn’t share details on how it developed the key, beyond saying that it was created “in collaboration with a trusted law enforcement partner” and that it will help those entities that were attacked before parts of REvil’s infrastructure blinked off on July 13.


“​Please note this is an ongoing investigation and we can’t comment on details related to this case until authorized by the lead investigating law enforcement partner,” Bitdefender said in a press release. “Both parties believe it is important to release the universal decryptor before the investigation is completed to help as many victims as possible.”


When REvil shut down, it left infected victims [high and dry](https://threatpost.com/whats-next-revil-victims/167926/), unable to continue with negotiations that were abruptly snipped and, hence, unable to get a decryptor key. The decryption tool that Bitdefender is offering should help those victims to take back control of their data and assets.


How to Get the Key
------------------


UPDATE: Victims of REvil ransomware can download the new decryption tool for free to recover their data: See [Bitdefender’s post, here.](https://www.bitdefender.com/blog/labs/bitdefender-offers-free-universal-decryptor-for-revil-sodinokibi-ransomware/)


A step-by-step tutorial on how to use the REvil decryption tool [is available here](https://www.nomoreransom.org/uploads/REvil_documentation.pdf).


Who is REvil/Sodinokibi?
------------------------


REvil is a ransomware-as-a-service (RaaS) operator likely based in a [Commonwealth of Independent States](http://www.cisstat.com/eng/cis.htm#:~:text=At%20present%20the%20CIS%20unites,%2C%20Turkmenistan%2C%20Uzbekistan%20and%20Ukraine.) (CIS) country. It emerged in 2019 as a [successor](https://threatpost.com/gandcrab-operators-resurface-revile-malware/148631/) of the now-defunct GandCrab ransomware. REvil/Sodinokibi is one of the most prolific ransomwares on the Dark Web: Affiliates have targeted thousands of technology companies, MSPs and retailers around the world.


After successfully encrypting a business’s data, REvil affiliates demand big ransoms – up to $70 million – in exchange for a decryption key and promises that the gang won’t publish the data it stole during the attack.


Its biggest caper before it disappeared was the Kaseya attack: A blitz that ensnared thousands of managed service providerd (MSPs).


Starting July 2, the REvil gang [launched](https://threatpost.com/kaseya-patches-zero-day-exploits/167548/) what would amount to more than 5,000 attacks in 22 countries against the Kaseya Virtual System/Server Administrator (VSA) platform. Those attacks hit not only Kaseya’s MSP customer base but also, given that many of them use VSA to manage the networks of other businesses, the customers of those MSPs.


REvil’s Key Hierarchy
---------------------


When it comes to decryption keys, REvil, as well as other RaaS groups, uses a key hierarchy.


Yelisey Boguslavskiy, head of research at Advanced Intelligence, explained that each RaaS affiliate can get their own key to unlock the victim – if the victim pays. But that key will only work for that specific victim: That’s why the key that Kaseya got hold of wouldn’t work to unlock other REvil victims.


There’s also a universal key owned by the core team for a set of victims like Kaseya. That universal key can cover multiple networks and workstations, Boguslavskiy told Threatpost on Wednesday.


“This was the key released after the Kaseya attack,” he said, referring to the story told by the purported new representative for the [purportedly reborn REvil](https://threatpost.com/revil-back-coder-decryptor-key/169403/) about a coder misclicking and accidentally generating and issuing a key.


Then too, there’s an “operator’s key” or a “master key” used by top RaaS leadership such as UNKN – the REvil representative who was active before the July 13 server shutdown.


The master key can unlock any victim, but the one that Kaseya obtained wasn’t the master key. In fact, Advanced Intelligence has “never seen this key before,” Boguslavskiy said. Below is a screenshot that Advanced Intel took of a Dark-Web forum conversation on the topic of decryption keys:


This master key is the one that Bitdefender is now offering.


While Bitdefender isn’t able to share details about the key, given the fact that the firm mentioned a “trusted law enforcement partner,” Boguslavskiy conjectured that Bitdefender likely “conducted an advanced operation on REvil’s core servers and infrastructures with or for European law enforcement and was somehow able to reconstruct or obtain the master key.”


Using the key in a decryptor will unlock any victim, he said, “unless REvil redesigned their entire malware set.”


But even if the reborn REvil did redesign the original malware set, the key will still be able to unlock victims that were attacked prior to July 13, Boguslavskiy said.


Advanced Intel monitors the top actors across all underground discussions, including on XSS, ​​a Russian-language forum created to share knowledge about exploits, vulnerabilities, malware and network penetration. So far, the intelligence firm hasn’t spotted any substantive discussion about the universal key on these underground forums. Boguslavskiy did note, however, that the administrator of XSS has been trying to shut down discussion threads, since they “don’t see any use in the gossip.”


However Bitdefender got the universal decryptor, releasing it is “obviously a game-changer,” Boguslavskiy said, given how hard it is to get or build one and the fact that “ransomware groups make sure that only the most important people in their gang have access to it.”


Deus Ex Machina
---------------


Dirk Schrader, global vice president of security research at NNT, noted that these decryptors are “the last hope of victims, and as such the cyber security representation of the ‘deus ex machina’ known in ancient Greek drama.”


But while they’re good to have as a last resort, entities can’t count on getting one as a central line of defense against threats. “Such a decryptor might be able to help unlock files and restore access to data, but it will not address questions like ‘why did we become a ransomware victim in first place?’ or ‘what else has been done by the attackers?'” Schrader noted to Threatpost.


“Security teams are constrained in resources and boards might think that – using a weird argument of easing the workload – universal decryptors are the way to go in addressing ransomware,” he continued. He thinks it’s likely that REvil – whatever that name constitutes these days, be they low-skilled leftovers or the actual pros who coded the initial, highly successful ransomware in the first place – will change code and cryptography, rendering an existing decryptor useless.


“There is one aspect that will be missed again,” Schrader predicted: “a pro-active, cyber-resilient approach to information security that is not focused on point-in-time solutions, dissolving the existing security silos for infrastructure, identity, and data.”


REvil Reborn: Clowns or Pros?
-----------------------------


Bitdefender thinks that new REvil attacks are “imminent,” given that the ransomware gang’s servers and supporting infrastructure recently came back online after a two-month hiatus. “We urge organizations to be on high alert and to take necessary precautions,” the firm said in its press release.


But the criminal RaaS underground, for its part, isn’t all that impressed by the REvil redo. Take the story about the purported fat-fingered REvil coder’s misclick leading to a key generation and issuance: It’s just not how ransomware works, and the underground knows that full well, Boguslavskiy told Threatpost.


Rather, top-tier groups such as REvil use advanced admin panels that are complicated, developed process management systems that look and operate similar to legitimate software platforms like JIRA.


“A ransomware attack from the eyes of the operator looks more like a business process,” Boguslavskiy explained. “Affiliates obtain access and validate it with the core developer team. This is often done via a ticket system which enables the management to moderate and assess prospective targets. Only when the ticketing process is complete, the affiliate may begin advancing with the attack by receiving the payload from the management. The negotiations and the data release are often done the same way in which a ticket is created, and the management will provide the decryption key generated for this specific victim.”


He continued, “This is a highly customized, well-operated system that was managed by close observation from UNKN. And as the underground community argues, the explanation that within this system there was a misclick leading to release of master key and subsequent loss of $50-70 million which REvil demanded from Kaseya victims looks very dubious. Other hackers argue that it is very hard to imagine that such misclicks never happened in REvil’s history but suddenly occurred during their biggest attack.”


Representatives of all underground actors – including LockBit – agree that the explanation provided by the “new” REvil representative regarding the misclick generation of the decryption key is “absolutely ridiculous and doesn’t make any sense in the context of how contemporary RaaS operations work,” Boguslavskiy said.


A more realistic scenario: The decryption key was released because REvil’s management, specifically UNKN, received some sort of payment and decided to not share it with affiliates and instead quit, he suggested.


“The new REvil is most likely one of the low-level members who were among those scammed with the Kaseya ransom,” Boguslavskiy said via email. “They won’t admit this, however, because they are trying to rebuild the group’s already poor reputation.”


But what about the victim that appeared – briefly – on the reborn REvil’s shame site?


That U.S. company was actually deleted from REvil’s Happy Blog after a short stint, perhaps suggesting that it was an older victim who was extorted prior to REvil’s shutdown and whose data was used “in order to emulate the resurgence activity,” Boguslavskiy hypothesized.


“Overall the community agrees that the re-emergence is a form of scam or a policy operation,” he said. “If REvil has indeed re-emerged, the main challenge with the group would be the absence of long-term prospects. UNKN who was the core developer has disappeared. It is very unlikely that even if other REvil members indeed allied to re-establish the gang, they will be able to successfully develop the ransomware without UNKN.”


Here’s hoping that the reborn REvil is, in fact, just a boogeyman set up to milk all the FUD that this gang gives off like a nasty miasma – and that Bitdefender’s universal key helps victims to wake up out of their ransomware nightmare.


091621 09:11 UPDATE: Added links to Bitdefender’s decryptor and guide on how to use it.




#### Tags:
[[REvil]] [[Boguslavskiy]] [[Kaseya]] [[decryptor]] [[Bitdefender]] [[ransomware]] [[REvil’s]] [[RaaS]] [[said,]] [[key.]] [[ThreatPost]]
