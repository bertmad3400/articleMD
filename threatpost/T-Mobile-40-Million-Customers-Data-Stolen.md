# T-Mobile: >40 Million Customers’ Data Stolen
### Attackers stole tens of millions of current, former or prospective customers’ personal data, the company confirmed. It’s providing 2 years of free ID protection.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168778)
+ Date: August 18, 2021  1:54 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/18104053/data-theft-e1629297667514.jpeg)
T-Mobile has confirmed much of what a threat actor bragged about over the weekend: Personal details for tens of millions of current, former or prospective T-Mobile customers were stolen in a huge breach of its servers.


On Tuesday, it disclosed further details on the [data breach](https://threatpost.com/t-mobile-investigates-100m-records/168689/) in a [post](https://www.t-mobile.com/news/network/additional-information-regarding-2021-cyberattack-investigation) on its website, saying that the breach affects as many as 7.8 million postpaid subscribers, 850,000 prepaid customers and “just over” 40 million past or prospective customers who’ve applied for credit with T-Mobile.


Its investigation is ongoing, but so far, it doesn’t look like financial data, credit card information, debit or other payment information was in the stolen files, T-Mobile said. The wireless carrier said that it located and “immediately” closed the access point in its servers that it believes granted access to the attacker(s).


Forrester Analyst Allie Mellen told Threatpost on Wednesday that this attack wasn’t exactly rocket science.  “According to the attackers, this was a configuration issue on an access point T-Mobile used for testing,” he said via email. “The configuration issue made this access point publicly available on the Internet. This was not a sophisticated attack; this was not a zero day. T-Mobile left a gate left wide open for attackers – and attackers just had to find the gate.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


At least according to what the purported thief told cybersecurity intelligence firm Cyble, the threat actor made off with a collection of databases that total about 106GB of data, including T-Mobile’s Oracle customer relationship management (CRM) database.


Compromised payment data may not have shown up in T-Mobile’s investigation, but personal information did: As of 01:54 Wednesday morning, T-Mobile had ascertained that the ripped-off data included customers’ first and last names, date of birth, Social Security numbers, and driver’s license/ID information “for a subset of current and former postpay customers and prospective T-Mobile customers.”


The telecommunications bigwig said that it first learned late last week about claims, posted to an underground forum, that threat actor(s) had stolen over 100 million customer records and were offering 30 million for sale for the surprisingly cheap cost of 6 bitcoin (~$270,000), or about 1 cent per record.


According to preliminary analysis, about 7.8 million current T-Mobile postpaid customer accounts’ information were in the stolen files, plus over 40 million records of former or prospective customers who had previously applied for credit with T-Mobile.


Either the purported thief was lying about also getting at phone numbers, account numbers, security PINs, and passwords, or T-Mobile’s preliminary investigations haven’t yet revealed proof that they were. At any rate, the company said that none of those, nor financial information, were compromised in any of the purloined files of customers or prospective customers.


Over the weekend, the threat actor who was offering to sell the records on an underground forum told BleepingComputer and Motherboard that they’d also stolen physical addresses, unique IMEI numbers and IMSI numbers. The attacker told BleepingComputer that T-Mobile’s “entire IMEI history database going back to 2004 was stolen.” IMEI (International Mobile Equipment Identity) is a unique 15-digit code that precisely identifies a mobile device with the SIM card input, and an IMSI (International mobile subscriber identity) is a unique number that identifies every user of a cellular network.


No phone numbers, account numbers, PINs, passwords, or financial information were compromised in any of the stolen records pertaining to customers or prospective customers, Not so for prepaid customers, though: There were, in fact, security PINs for 850,000 prepaid customers involved, T-Mobile said in its update: “At this time, we have also been able to confirm approximately 850,000 active T-Mobile prepaid customer names, phone numbers and account PINs were also exposed.”


It’s reset all the PINs on the prepaid accounts and plans to notify customers “right away,” the company said. No Metro by T-Mobile, former Sprint prepaid, or Boost customers had their names or PINs exposed.


Finally, information from inactive prepaid accounts was compromised through prepaid billing files. There were no customer financial information, credit card information, debit or other payment information or Social Security numbers contained in the inactive file.


Free Two Years Identity Protection
----------------------------------


T-Mobile plans to contact customers “shortly” to let them know that it’s immediately offering two years of free identity protection services with McAfee’s ID Theft Protection Service. What else it plans to outline:


Stay tuned, the company said: The investigation continues, and T-Mobile “may learn additional facts through our investigation that cause the details above to change or evolve.”


Some observers aren’t exactly impressed by the standard-issue “security is super important to us” messaging and the offloading of responsibility to customers. “T-Mobile is offering two free years of identity protection for affected customers, but ultimately this is pushing the responsibility for the safety of the data onto the user,” Mellen told Threatpost. “Instead of addressing the security gaps that have plagued T-Mobile for years, they are offering their customers temporary identity protection when breaches happen, as if to say, ‘This is the best we can do.'”


Somebody’s Flunking at History
------------------------------


If this is the best T-Mobile can do, that’s a sad statement. This is at least the fifth time that T-Mobile has been attacked in recent years.


The roster of breaches:


**January 2021:** The wireless carrier disclosed that it detected and shut down “malicious, unauthorized access to some information” related to T-Mobile accounts. Specifically, that data consisted of [customer proprietary network information](https://threatpost.com/t-mobile-another-data-breach/162703/) (CPNI) – a data set that the [FCC calls](https://www.fcc.gov/document/customer-proprietary-network-information-cpni) “some of the most sensitive personal information that carriers and providers have about their customers.”


CPNI includes records of which phone numbers users called; the frequency, duration, and timing of such calls; and any services purchased by the consumer, such as call waiting. T-Mobile said that the thieves in this case lifted phone numbers, number of lines subscribed to on accounts, “and, in some cases, call-related information.”


**2018:** [2.3 million subscribers’ data](https://threatpost.com/t-mobile-alerts-2-3-million-customers-of-data-breach-tied-to-leaky-api/136896/) were exposed, including names, billing ZIP codes, phone numbers, email addresses, account numbers and account types (prepaid or postpaid).


**2019:** about 1.26 million of T-Mobile’s prepaid [were affected](https://www.t-mobile.com/customers/6305378822) by a breach that included names, billing addresses (if provided), phone numbers, account numbers and CPNI.


**2020:** An undetermined number of employees and customers were affected when attackers [accessed](https://www.complianceweek.com/cyber-security/t-mobile-data-breach-a-cautionary-tale-for-all-companies/28568.article) employee email accounts, some of which contained account information for T-Mobile customers, including names and addresses, phone numbers, account numbers and more.


While this is the fifth breach since 2018, it’s “by far” the biggest and the baddest, Mellen observed, meaning that somebody isn’t learning their cybersecurity lessons. “This is the fifth public data breach of T-Mobile in three or four years, and by far leaks the most sensitive data and exposes the most customers,” he said. “It seems T-Mobile has not learned from these previous breaches, especially considering they didn’t know about the attack until the attackers posted about it in an online forum.”


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[T-Mobile]] [[numbers,]] [[T-Mobile’s]] [[information,]] [[names,]] [[customers,]] [[said.]] [[Mellen]] [[cybersecurity]] [[addresses,]] [[ThreatPost]]
