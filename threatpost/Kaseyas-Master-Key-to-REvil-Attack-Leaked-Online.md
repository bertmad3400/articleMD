# Kaseya’s ‘Master Key’ to REvil Attack Leaked Online
### The decryptor is of little use to other companies hit in the spate of attacks unleashed before the notorious ransomware group went dark, researchers said.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168565)
+ Date: August 11, 2021  11:34 am
+ Author: Elizabeth Montalbano


## Article:
Someone has leaked the master decryption key that [Kaseya used](https://threatpost.com/kaseya-universal-decryptor-revil-ransomware/168070/) to unlock the files encrypted by a REvil ransomware attack on the company that affected customers across 22 countries last month.


However, while the key may be interesting to security researchers, it’s not likely to be of use to any of the other companies REvil hit in the spate of attacks that occurred on July 2.


A security researcher who goes by the handle [@Pancak3](https://twitter.com/pancak3lullz) on Twitter found what was purported to be the key on a hacking forum and [tweeted](https://twitter.com/pancak3lullz/status/1425221181058306050) about it, posting a screenshot to the key on Twitter and also [GitHub](https://github.com/Fr3akaLmaTT3r/decryptor/blob/main/screenshot.png).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/)  

While it was first thought that the key could unlock all of the REvil attacks that occurred at the same time as the Kaseya one, it soon became clear to researchers that the decryptor – which appeared to some to be genuine – was only for the files locked in the Kaseya attack.


“Initial tests indicate this might be legit but do not cite me you’ll need own verification,” tweeted @SOS, or SwiftonSecurity, a systems security researcher who writes the [Decent Security blog](https://decentsecurity.com/).


Oregon-based ethical hacker [@Jeff McJunkin](https://twitter.com/jeffmcjunkin) also tweeted that the master decryption key appears legitimate. “If you were affected, it’s definitely worth taking a look (in an isolated lab environment at first, naturally),” he [wrote on Twitter](https://twitter.com/jeffmcjunkin/status/1425229927197011969).


Researchers at Flashpoint said they patched the decryptor binary with the annotated key from the thread and successfully decrypted a sandbox infected with the new REvil test sample “upon changing the file extensions to “universal\_tool\_xxx\_yyy” as seen in the screenshot,” according to [a blog post](https://www.flashpoint-intel.com/blog/possible-universal-revil-master-key-posted-to-xss/) published Tuesday.


“The files were properly decrypted once the file extensions were renamed,” researchers reported.


Kaseya was one of the victims attacked in a global ransomware spree REvil went on July 2 not long before [the group disappeared](https://threatpost.com/ransomware-revil-sites-disappears/167745/). The attacks on Kaseya [exploited](https://threatpost.com/zero-days-kaseya-unitrends-backup-servers/168180/) [now-patched zero-days](https://threatpost.com/kaseya-patches-zero-days-revil-attacks/167670/) in the Kaseya Virtual System/Server Administrator (VSA) platform and affected 60 customers using the on-premises version of the platform.


Many of those hit were managed service providers (MSPs) that use VSA to manage the networks of other businesses. In addition to the direct customers, about 1,500 downstream customers of those MSPs were also affected.


Late on July 22, Kaseya said it had obtained the master decryptor “through a third party,” making it unclear if the company paid the $70 million in ransom REvil demanded for the attack. The company worked with security firm Emsisoft to help customers affected by the attack; the key was used to unlock systems that REvil had encrypted.


**Key Limited to Kaseya Attack**
--------------------------------


Though Emsisoft would not comment at the time about its work to help Kaseya customers decrypt their files after the REvil attack, CTO Fabian Wosar did step forward on Twitter Tuesday to verify that the Kaseya master key published on the dark web was not for all the REvil attacks that happened concurrently.


“The REvil hardcoded operator public key is 79CD20FCE73EE1B81A433812C156281A04C92255E0D708BB9F0B1F1CB9130635,” Wosar, who also is a ransomware expert, [tweeted](https://twitter.com/fwosar/status/1425275409533476868). “The leaked key generates public key F7F020C8BBD612F8966EFB9AC91DA4D10D78D1EF4B649E61C2B9ADA3FCC2C853. Therefore, the leaked key is not the operator private key.”


At this point it’s still unclear how the key made its way to an online forum, although some on Twitter are speculating that one of Kaseya’s customers who used the key may be responsible.


“My bet is it’s a [SIC] NDA violation that someone is trying to divert attention from,” [tweeted](https://twitter.com/Jeremy_Kirk/status/1425319100562087936) security reporter [Jeremy Kirk](https://twitter.com/Jeremy_Kirk) of Information Security Media Group. “Doesn’t look like the key is going to be that useful to anyone at this point, though.”


He may be right, as some have reported on Twitter that the key did not perform as expected in tests they are running to prove its legitimacy.


“Still waiting on additional tests, but some have failed,” [tweeted](https://twitter.com/campuscodi/status/1425252654977069058) [Catalin Cimpanu](https://twitter.com/campuscodi), a cybersecurity reporter at The Register. “Maybe there’s certain steps people are missing. We’ll find out.”


One of the reasons this failure occurred could be because the [decryption](https://twitter.com/campuscodi) key posted by @Pancak3 is actually out of date, according to another researcher.


“Kindly note that REvil decrypter version 2.1 / 2.2 was used from more than a year ago,” [tweeted](https://twitter.com/ahmedm0hamed101/status/1425397385228861443) offensive security researcher [Ahmed Mohamed](https://twitter.com/ahmedm0hamed101). “But the version on that screenshot is 2.0. So we can’t guarantee it will be work, but you can try.”


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[REvil]] [[Kaseya]] [[it’s]] [[ransomware]] [[decryptor]] [[“The]] [[ThreatPost]]
