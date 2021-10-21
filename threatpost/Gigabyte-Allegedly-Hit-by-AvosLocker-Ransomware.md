# Gigabyte Allegedly Hit by AvosLocker Ransomware
### If AvosLocker stole Gigabyte’s master keys, threat actors could force hardware to download fake drivers or BIOS updates in a supply-chain attack a la SolarWinds. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175642)
+ Date: October 21, 2021  1:33 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/21125838/gigabyte-e1634835529945.jpg)
The AvosLocker ransomware gang is claiming that it breached tech giant Gigabyte, adding that it has leaked a sample of what it claims are files stolen from the Taiwanese company’s network. It’s offering to sell the rest.


On Wednesday, the gang posted a “press release” announcing that it had purportedly gutted the motherboard/server maker, though it didn’t say when or how. The leaked files, seen by PrivacySharks and by Threatpost, appear to contain confidential details regarding deals with third-party companies and identifiable information about employees.


PrivacySharks has reached out to AvosLocker for more information about the breach. Threatpost has reached out to Gigabyte but hasn’t heard back yet.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Below is a screen capture of AvosLocker’s announcement, which refers to a nondisclosure agreement (NDA) between Gigabyte and Barracuda Networks. The NDA, which Threatpost has viewed, is dated June 2007 and signed on behalf of Barracuda by “Drako” – which, if authentic, presumably refers to Barracuda co-founder Dean Drako.


“Gigabyte INC suffered a breach, and this is a sample of the files we’ve downloaded from their network. Barracuda NDA + full dir list leaked in sample,” according to AvosLocker’s statement.


What Was Leaked
---------------


In a [Thursday post](https://www.privacysharks.com/gigabyte-breached-by-ransomware-group-avoslocker-data-up-for-sale/), PrivacySharks said that an independent security researcher affiliated with the company has viewed the contents of a leaked 14.9MB file called “proof.zip” that was purportedly exfiltrated from Gigabyte.


The researcher said that it contains the following list of sensitive information:


Could Attack Set Off Supply-Chain Ripples?
------------------------------------------


Gigabyte designs and manufactures motherboards for both AMD and Intel platforms. It also produces graphics cards and notebooks in partnership with AMD and Nvidia, including Nvidia’s Turing chipsets and AMD’s Vega and Polaris chipsets. PrivacySharks suggested that if the leak turns out to include Gigabyte’s master keys – i.e., keys that identify hardware manufacturers as the original developer – threat actors could use them to  force hardware to download fake drivers, BIOS updates or more, as happened with [SolarWinds](https://threatpost.com/solarwinds-hack-seismic-shift/165758/).


At this point, PrivacySharks’ experts have only found two .KEY files and a few .CRT files, suggesting that “this breach contains no or very little data from the security/tech departments,” according to the writeup. “However, if Gigabyte revokes any keys in the near future, keep this possibility in mind,” PrivacySharks suggested.


Data Both Fresh and Stale?
--------------------------


If the leaked files turn out to be legitimate, some are from a fresh breach, with files dating as recently as May.


“This indicates that this is a fresh leak with new data,” according to PrivacySharks. “Not only this, but the date of the files means that some of the personally identifiable data (such as interviewees’ information, password and username credentials, etc.) could be up-to-date, and therefore, at risk of being compromised.”


Then again, they’re also old, as in, years old, which begs the question: Why are the files still kicking around?  Why, if these files are really Gigabyte’s data, did the company hang on to sensitive data for so long, instead of deleting it per rules such as the European Union’s General Data Protection Regulation ([GDPR](https://threatpost.com/gdpr-a-compliance-quagmire-for-now/132644/)), Privacy Sharks asked.


“Some of the leaked data calls into question how Gigabyte stores and uses data,” the writeup suggested. “For example, we were particularly surprised to find a vast amount of identifiable data about job applicants, including CVs and resumes, which normally include personal data like dates of birth, email addresses, and phone numbers.


“As a rule of thumb, companies should not hold onto candidates’ data after the hiring process is over, and the Gigabyte data leak demonstrates why, as this information can fall into the wrong hands. For this reason, the EU has a GDPR law that requires companies to delete data like this.”


AvosLocker and Its Auction Gimmick
----------------------------------


As [Cyble reported](https://blog.cyble.com/2021/07/15/avoslocker-under-the-lens-a-new-sophisticated-ransomware-group/) in July, AvosLocker is a new ransomware group that’s been infecting Windows machines with malware that’s primarily distributed via spam email campaigns or funky advertisements.


Earlier this month, the gang [reportedly](https://therecord.media/avoslocker-ransomware-gang-to-auction-the-data-of-victims-who-dont-pay/) revamped its site to create a way to auction off the data of recalcitrant victims who refuse to pay ransom. It’s not the first ransomware gang to pull this stunt, which is meant to add yet another thumbscrew to the [double-extortion](https://threatpost.com/double-extortion-ransomware-attacks-spike/154818/) gambit of not only freezing victims’ systems but also threatening to publish stolen data if they don’t pay up. In fact, other ransomware gangs cooked up the added pressure point in 2020, including the [REvil ransomware gang](https://threatpost.com/revil-ransomware-gang-auction-stolen-data/157006/).


But ransomware experts say that the threat of auction isn’t real and shouldn’t be taken seriously.


It’s just a form of victim intimidation, and a “very low-quality one” at that, according to Yelisey Boguslavskiy head of research at the cyber risk prevention firm Advanced Intelligence.


“This is simply a button on a website,” Boguslavskiy told Threatpost on Thursday.


“The underground auctions do exist – [the Exploit forum being] the most exemplary case,” he said. “However, in the years of the forum’s existence, there were never cases when actors came to Exploit with [offerings] similar to the ones which RaaS [ransomware as-a-service] groups make.”


To put it simply, “no one in the underground has offered stolen files, since this is not what the actors are willing to pay for,” Boguslavskiy said. “The auction button is completely fake. There is no chance anyone will use it simply because it is useless.”


Same Old Same Old
-----------------


Boguslavskiy said that cases like this are becoming “very typical for the post-2020/2021 ransomware.”


Such attacks are coming from smaller groups or groups with mediocre skills who “believe that they can extort ransom by simply stealing and publishing the data on shame blogs,” he said. “However, such blackmailing only works as a force multiplier or an integral component of a larger holistic ransomware operation built around maximizing the risks for victims if they don’t pay.”


AdvIntel used [Conti](https://threatpost.com/conti-ransomware-backups/175114/) as an example: While the RaaS group steals data and threatens to publish it, Conti integrates the methodology into a larger context, which Boguslavskiy described as locking and encrypting the networks, removing backups, investigating networks for weeks to identify the most critical information and performing smart negotiations.


“In other words, a ransomware group can definitely leverage data exfiltration to get paid, however, only if they do it in a very smart, strategic and sophisticated way,” he explained. “And this is not the case with AvosLocker and/or 80 percent RaaS on today’s landscape (a big difference from 2019/2020 when more groups were like Conti).”


It’s like heart surgery, he said: “Groups like AvosLocker, REvil, or LockBit are trying to perform a surgery without having skills and tools, and as a result, they don’t get paid the ransom.”


Simple Threats of Dumping Files Don’t Scare Victims
---------------------------------------------------


“They do believe that a simple threat of dumping a set of files on a blog will force the victim to pay,” Boguslavskiy said, but that’s mostly because the media has been on a two-year scare fest about ransomware that, in reality, doesn’t stand up to the smell test.


“[It’s] simply not true,” he said, and that’s evidenced by the fact that large amounts of unimportant data from hundreds of companies get dumped on shame blogs of ransomware groups such as SunCrypt or LockBit.


What else are the crooks going to do with it, after all?


“They dump it there because they are not being paid. These groups expect huge payments as after stealing some files they feel omnipotent, but in reality, for them, it all ends up not with a bang but a whimper (to put it more poetically), when they are left with $0 on their account and have nothing else to do than dump files on TOR,” Boguslavskiy commented.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[ransomware]] [[Boguslavskiy]] [[AvosLocker]] [[PrivacySharks]] [[It’s]] [[Threatpost]] [[that’s]] [[files,]] [[“However,]] [[don’t]] [[ThreatPost]]
