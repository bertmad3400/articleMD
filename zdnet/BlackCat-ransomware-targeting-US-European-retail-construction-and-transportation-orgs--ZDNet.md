# BlackCat ransomware targeting US, European retail, construction and transportation orgs | ZDNet
### Palo Alto said that as of December 2021, BlackCat has the 7th largest number of victims listed on their leak site among ransomware groups that Unit 42 tracks.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/blackcat-ransomware-targeting-us-european-retail-construction-and-transportation-orgs/
+ Date: 2022-01-28 12:30:00
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/ac23f5475eb67f67e44c9bb5e0b41e3d9a8919da/2021/12/15/5d6836ac-a637-410c-9381-0ff8754dd00f/shutterstock-2023392170.jpg?width=770&height=578&fit=crop&auto=webp)

Palo Alto Networks' Unit 42 [released](https://unit42.paloaltonetworks.com/blackcat-ransomware/) a deep-dive into the BlackCat ransomware, which emerged in mid-November 2021 as an innovative ransomware-as-a-service (RaaS) group leveraging the Rust programming language and offering affiliates 80-90% of ransom payments.


In December, the ransomware family, also known as ALPHV, racked up at least 10 victims, giving it the seventh-largest number of victims listed on their leak site among ransomware groups tracked by Unit 42. 

Doel Santos, threat intelligence analyst with Unit 42, told *ZDNet* the group has already attacked a wide range of industries, including construction and engineering, retail, transportation, commercial services, insurance, machinery, professional services, telecommunication, auto components and pharmaceuticals. 

Last week, Italian fashion brand Moncler was [revealed](https://www.bleepingcomputer.com/news/security/fashion-giant-moncler-confirms-data-breach-after-ransomware-attack/) to be a BlackCat victim [from December](https://s3.documentcloud.org/documents/21181299/moncler-press-release-malware.pdf). 

In addition to being written in Russian and coded in the Rust programming language, the malware stood out to Santos for a number of other reasons.

"What makes Blackcat standout is the use of their private access-key token. Most of the groups we have looked at in the past include a direct link and the keys embedded in the samples, which makes it easy to look at and confirm the ransomware victims," Santos said.

**Also: [White House, EPA release 100-day cybersecurity plan for water utility operators](https://www.zdnet.com/article/white-house-epa-release-100-day-cybersecurity-plan-for-water-utility-operators/)** 






"Blackcat ransomware samples don't include the keys. Instead, they need to be submitted by the operator. Without it, there is no way for an external entity to get access to their negotiation site or identify the victim unless they have an exact copy of a ransom note with the exact key used for executing the ransomware."

Unit 42 noted that the affiliates of the group have "taken an aggressive approach to naming and shaming victims, listing more than a dozen on their leak site in a little over a month." 

"The largest number of the group's victims so far are US organizations, but BlackCat and its affiliates have also attacked organizations in Europe, the Philippines and other locations," the report noted. 

![screen-shot-2022-01-27-at-6-52-14-pm.png]()![screen-shot-2022-01-27-at-6-52-14-pm.png](https://www.zdnet.com/a/img/resize/bef071fc07d6c1096c2060b8b8f89ce2a8503017/2022/01/27/2ef9b35e-aa97-4dc0-9959-1cafe1967b21/screen-shot-2022-01-27-at-6-52-14-pm.png?width=370&fit=bounds&auto=webp)
 Unit 42
 "Use of BlackCat ransomware has grown quickly for a variety of reasons (for comparison, [AvosLocker](https://unit42.paloaltonetworks.com/emerging-ransomware-groups/) had only listed a handful of victims publicly within two months of becoming known). Effective marketing to affiliates is a likely factor. In addition to offering an enticing share of ransom payments, the group has solicited affiliates by posting ads on forums such as Ransomware Anonymous Market Place (RAMP)," the report added. 

"Though this is not the first piece of malware to use Rust, it is one of the first, if not the first, piece of ransomware to use it. By leveraging this programming language, the malware authors can easily compile it against various operating system architectures. Given its numerous native options, Rust is highly customizable, which facilitates the ability to pivot and individualize attacks."

**Also: [QNAP warns NAS users of DeadBolt ransomware, urges customers to update](https://www.zdnet.com/article/qnap-warns-nas-users-of-deadbolt-ransomware-urges-customers-to-update/)**

The group also extorts victims by stealing their data before deploying the ransomware, threatening to leak the data and launch distributed denial-of-service (DDoS) attacks.

BlackCat has been seen targeting both Windows and Linux systems, according to Unit 42, which added that it has observed affiliates asking for ransom amounts of up to $14 million. In some instances, affiliates have offered discounts of $9 million if the ransom is paid before the established time. They allow ransom to be paid in Bitcoin and Monero.

"In some cases, BlackCat operators use the chat to threaten the victim, claiming they will perform a DDoS attack on the victims' infrastructure if the ransom is not paid. When it appears in addition to the use of a leak site, this practice is known as triple extortion, a tactic that was observed being used by groups like [Avaddon](https://unit42.paloaltonetworks.com/ransomware-threat-report-highlights/) and [Suncrypt](https://unit42.paloaltonetworks.com/ransomware-threat-report-highlights/) in the past," Unit 42 explained. 

"One unique feature of BlackCat ransomware is that negotiation chats can only be accessed by those holding an access token key or ransom note -- the group has made efforts to avoid third-party snooping."

Recorded Future ransomware expert Allan Liska said that based on a couple of factors, including the use of the Rust programming language, Black Cat/ALPHV appears to be a well-sourced group. 

Liska said the fact that the group started with ransomware variants targeting Windows, Linux and ESXi systems "shows a level of sophistication."

"They have quickly become one of the top tier ransomware groups. This is credited, in part, to the fact that their RaaS offering is very aggressive, offering affiliates the ability 80%-90% of ransom paid, an unusually high percentage. Despite some early success, not every affiliate has been impressed, as this very negative review shows," Liska said, sharing a screenshot of an affiliate who complained about being banned by BlackCat for targeting an organization in Turkmenistan.

While Turkmenistan is not in CIS, it does have close ties to Russia.




> A prolific [#ransomware](https://twitter.com/hashtag/ransomware?src=hash&ref_src=twsrc%5Etfw) operator known as FishEye aka bassterlord has come out of deep waters after a month off and posted a very negative review of the [#ALPHA](https://twitter.com/hashtag/ALPHA?src=hash&ref_src=twsrc%5Etfw) ([#BlackCat](https://twitter.com/hashtag/BlackCat?src=hash&ref_src=twsrc%5Etfw)) ransomware. 1/5 [pic.twitter.com/k1Wl1liljO](https://t.co/k1Wl1liljO)
> 
> — Azim Khodjibaev (@AShukuhi) [January 19, 2022](https://twitter.com/AShukuhi/status/1483661973162188800?ref_src=twsrc%5Etfw)




 window.ZdnetFunctions.logWithLabel('%c One Trust ', "Service loaded: script\_twitterwidgets with class optanon-category-5");
 
"Their public targets have been larger organizations, and they appear to be very aggressive when dealing with negotiators and their affiliates (e.g. a ban from the affiliate program after 2 weeks of inactivity). We'll see whether their penchant for being overbearing outweighs the attractive percentages they are offering," Liska added. 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Avaddon]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Construction]] [[victim.industry.name=Professional]] [[victim.industry.name=Retail]]

#### Location:
[[victim.country.name=Philippines]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Turkmenistan]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.city.name=Oslo]] [[victim.country.name=Norway]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=Paris]] [[victim.country.name=France]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Blackcat]] [[Liska]] [[Malware]] [[ZDNet]]

