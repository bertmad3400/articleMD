# Amazon Kindle Vulnerable to Malicious EBooks
### Prior to a patch, a serious bug could have allowed attackers to take over Kindles and steal personal data.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168454)
+ Date: August 6, 2021  2:54 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2019/11/07120424/kindle-e1573146276447.jpg)
A security flaw in Amazon’s Kindle e-reader made it vulnerable to malicious eBooks, opening the door to turning the devices into bots, compromising personal information and more.


That’s according to Check Point researcher Slava Makkaeveev, who released the findings Friday. Check Point disclosed the bug to Amazon in February, and it was fixed in April; Amazon released patched firmware to be automatically installed on every Kindle connected to the internet. It’s unclear if the bug was exploited prior to the patch, but crisis appears to have been averted: Any serious attack could have affected tens of millions of Kindle users across the globe.


The Check Point research demonstrates how easily an eBook can be used to deliver malware.



“Antivirus [protections] do not have signatures for eBooks,” Makkaeveev wrote in . “A malicious eBook can be published and made available for free access in any virtual library, including the Kindle Store, via the ‘self-publishing’ service, or sent directly to the end-user device via the Amazon ‘send to Kindle’ service.”


**Anatomy of a Malicious EBook**
--------------------------------


The Check Point team was able to create a proof-of-concept malicious eBook that, once it was opened on a Kindle, would have executed a hidden code with root rights, t[he report explained](https://research.checkpoint.com/2021/i-can-take-over-your-kindle/).


“From this moment on, you can assume that you have lost control of your e-reader,” Makkaeveev warned.


If a victim clicked on the [malicious eBook,](https://www.youtube.com/watch?v=BtpGVa7FaXo) it connected to a remote server and locked the user’s screen, Check Point explained. The [malware](https://threatpost.com/malware-makers-using-exotic-programming-languages/168117/) developed by Check Point then gained root access, giving the attacker total control of the Kindle, including access to the user’s Amazon account, cookies and the device’s private keys.


Worse yet, the Kindle bug allowed threat actors to target victims by specific regions, languages and more.


**Specific Demographics Easily Targeted**
-----------------------------------------


“In this case, what alarmed us the most was the degree of victim specificity that the exploitation could have [used],” Yaniv Balmas, head of cyber-research at Check Point, said.


Balmas offered the example of a threat actor interested in targeting Romanians: Simply re-printing a popular title translated into Romanian would be an easy way to gain access to victims.


“That degree of specificity in offensive attack capabilities is very sought-after in the cybercrime and cyber-espionage world,” Balmas told Threatpost. “In the wrong hands, those offensive capabilities could do some serious damage, which concerned us immensely.”


Earlier this year, Amazon paid threat-hunter Yogev Bar-On $18,000 as part of its bug-bounty program, for discovering KindleDrip. That vulnerability allowed attackers to email a [malicious eBook](https://threatpost.com/amazon-kindle-attack-email/163282/) to a victim Kindle device to gain root access to the device and steal money.


The Check Point research shows reinforces what a malicious eBook attack might look like: i.e., easy to execute. Balmas added the sheer ubiquity of Kindles in the market demand that its security be closely scrutinized.


“Kindle, like other internet of things (IoT) devices, are often thought of as innocuous and disregarded as security risks,” Balmas said. “Everyone should be aware of the cyber-risks in using anything connected to the computer, especially something as ubiquitous as Amazon’s Kindle.”


**Worried about where the next attack is coming from? We’ve got your back.**[**REGISTER NOW**](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**for our upcoming live webinar,**[**How to Think Like a Threat Actor**](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**, in partnership with Uptycs. Find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on Aug. 17 at 11AM EST for this**[**LIVE**](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**discussion.**




#### Tags:
[[eBook]] [[Balmas]] [[ThreatPost]]
