# 100m T-Mobile Customer Records Purportedly Up for Sale
### The seller claims to have sucker-punched U.S. infrastructure out of retaliation. The offer: 30m records for ~1 penny each, with the rest being sold privately. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168689)
+ Date: August 16, 2021  11:12 am
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/16104546/computer-system-security-breach-picture-id486481278-1-e1629125159886.jpeg)
A threat actor is selling what they claim to be 30 million T-Mobile customers’ Social Security and driver license numbers on an underground web forum. The collection is a subset of the purported 100 million records contained in stolen databases.


The seller told Motherboard – which first reported the news – that for now, they’re privately selling the rest.


The seller also told [Alon Gal](https://twitter.com/UnderTheBreach/status/1426923538099970050), CTO of cybercrime intelligence firm [Hudson Rock](https://www.hudsonrock.com/), that this sucker-punch to US infrastructure was done in retaliation, as Gal [tweeted](https://twitter.com/UnderTheBreach/status/1426923538099970050) on Sunday: “This breach was done to retaliate against the US for the kidnapping and torture of John Erin Binns (CIA Raven-1) in Germany by CIA and Turkish intelligence agents in 2019,” the threat actor told Gal. “We did it to harm US infrastructure.”



> 
> I spoke to the hackers, they claim they did it to harm US infrastructure and to retaliate against alleged US actions. <https://t.co/F7mcmrmgxn> [pic.twitter.com/0Kwn4Xl89D](https://t.co/0Kwn4Xl89D)
> 
> 
> — Alon Gal (Under the Breach) 🦇🔊 (@UnderTheBreach) [August 15, 2021](https://twitter.com/UnderTheBreach/status/1426923538099970050?ref_src=twsrc%5Etfw)
> 
> 



Binns is a US citizen who lives in Turkey and who [sued](https://casetext.com/case/binns-v-cent-intelligence-agency) the FBI, CIA and Department of Justice in 2020, alleging that he was tortured and harassed by the US and Turkish governments and is seeking to compel the USA to release documents regarding these activities under the Freedom of Information Act.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The seller’s offer doesn’t mention T-Mobile, but the seller told [Motherboard](https://www.vice.com/en/article/akg8wg/tmobile-investigating-customer-data-breach-100-million) and [BleepingComputer](https://www.bleepingcomputer.com/news/security/hacker-claims-to-steal-data-of-100-million-t-mobile-customers/) that the source is in fact the telecommunication kingpin’s servers. Specifically, they claim to have penetrated T-Mobile’s production, staging, and development servers two weeks ago, including an Oracle database server that held the customer data, according to what they told BleepingComputer.


As proof of the theft, the threat actor shared with BleepingComputer a screenshot of an SSH connection to a production server running Oracle.


T-Mobile told news outlets that it’s investigating the alleged data breach, which first came to light on an underground forum over the weekend. Its statement: “We are aware of claims made in an underground forum and have been actively investigating their validity. We do not have any additional information to share at this time.”


Threatpost has reached out to T-Mobile to ask about the scale of the breach, whether the company has contacted law enforcement and what plans are for informing affected customers but hadn’t heard back by the time this article was posted.


Even if T-Mobile hasn’t yet confirmed the breach, T-Mobile customers would be wise to change their security PINs, given that laundry list of details that were purportedly exposed. The seller told BleepingComputer that the records contain:


The attacker told BleepingComputer that T-Mobile’s “entire IMEI history database going back to 2004 was stolen.” IMEI (International Mobile Equipment Identity) is a unique 15-digit code that precisely identifies a mobile device with the SIM card input, and an IMSI (International mobile subscriber identity) is a unique number that identifies every user of a cellular network.


Fresh Baked, and Such a Bargain
-------------------------------


The asking price for the 30m records is six bitcoin, which was worth about $280,000 as of Monday morning East Coast time.


BleepingComputer posted a screenshot of the forum post, which claimed that the records are “Freshly dumped and NEVER sold before!” It added that “SERIOUS BUYERS ONLY!” should inquire.


Motherboard’s Joseph Cox has seen samples of the data and confirmed that it’s accurate information belonging to T-Mobile customers. In short, the records contain “Full customer info” for T-Mobile USA customers, the threat actor told Motherboard in an online chat.


T-Mobile has apparently responded by turning off the leaky faucet(s): The seller told Motherboard that they’ve “lost access to the backdoored servers.”


No matter, the purported thief said: They already made backups “in multiple places.”


Cybersecurity intelligence firm Cyble told BleepingComputer that the threat actor claims that they obtained several databases, totaling approximately 106GB of data, including T-Mobile’s customer relationship management (CRM) database.


A Penny Per Person
------------------


The asking price is crazy cheap, one expert told Threatpost: It comes out to about a penny per purported victim. That’s quite a bargain for cybercrooks, given that the records are rich in data that can be used to conduct ” targeted mobile attacks, social engineering, sophisticated phishing campaigns or financial fraud.”


Ilia Kolochenko, founder of the Swiss app sec firm ImmuniWeb and a member of the Europol Data Protection Experts Network, told Threatpost that what’s even worse is that the records reportedly encompass data from 2004 to 2021 and “can cause extreme invasion of privacy or be used for blackmailing of wealthy victims.


“Given that the offer seems to be new and unique, the price is very cheap: just 1 cent per victim. The records, which allegedly contain such extremely sensitive data as social security numbers and full histories of mobile phone usage, can be exploited to conduct targeted mobile attacks, social engineering, sophisticated phishing campaigns or financial fraud,” Kolochenko said via email.


Kolochenko thinks it’s “pretty likely” that one of T-Mobile’s suppliers could have unwittingly facilitated or caused the data breach, “Based on the available technical information.”


“If so, it will be another grim reminder about the importance of Third-Party Risk Management (TPRM) programs and risk-based vendor vetting,” he noted.


T-Mobile could be in for a world of legal hurt if the breach is confirmed, Kolochenko predicted. “T-Mobile may face an avalanche of individual and class action lawsuits from the victims, as well as protracted investigations and serious monetary penalties from the states where the victims are based.


Nonetheless, it’s too early to freak out, Kolochenko advised: “It would be premature to make conclusions before T-Mobile makes an official statement on the quantity and nature of the stolen data. The potential victims should refrain from panic and contact T-Mobile asking what type of intermediary support and compensation may be provided while the investigation is in progress. Some remediate actions, such as changing your driving license, may be time-consuming and costly, and I’d not precipitate here unless T-Mobile undertakes to cover the costs or confirm that the information was actually stolen.”


One of the Year’s Biggest Breaches
----------------------------------


If T-Mobile was in fact breached, and if 100 million customers’ data was in fact involved, it won’t be the biggest breach so far this year. It’s outdone by the [LinkedIn breach](https://threatpost.com/data-700m-linkedin-users-cyber-underground/167362/) in June, in which 700 million users’ data was posted for sale on the underground.


Still, it’s up there.


Jack Chapman, vice president of threat intelligence at Egress, told Threatpost on Monday that the threat to T-Mobile is high. “The data leaked in this breach is reported as being already accessible to cybercriminals, who could now weaponize it to formulate sophisticated phishing attacks targeting the victims,” Chapman said in an email.


He advised affected customers to be wary of “any unexpected communications they might now receive, whether that’s over email, text messages or phone calls. Follow-up attacks may utilize the information accessed through this data breach to trick people into sharing more personal data that can be used for identity and financial fraud.”


Chapman added that the incident “highlights the need for organizations such as T-Mobile to put in place the right technology to secure their sensitive data and defend their employees and their company from targeted attacks by cybercriminals. It’s time for organizations to take responsibility and ensure they’re keeping their customers’ data out of the hands of cybercriminals.”


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[T-Mobile]] [[BleepingComputer]] [[it’s]] [[T-Mobile’s]] [[breach,]] [[Kolochenko]] [[customers’]] [[Threatpost]] [[phishing]] [[ThreatPost]]
