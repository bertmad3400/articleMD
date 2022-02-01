# The Account Takeover Cat-and-Mouse Game
### ATO attacks are evolving. Jason Kent, hacker-in-residence at Cequence Security, discusses what new-style cyberattacks look like in the wild.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178128
+ Date: 2022-02-01T20:59:53+00:00
+ Author: Jason Kent


## Article:
![Article Image](https://khub-media.s3.eu-west-1.amazonaws.com/wp-content/uploads/sites/103/2022/01/01155844/cat-and-mouse-scaled-e1643749142516.jpeg)

In an analysis of more than 21 billion application transactions analyzed by the Cequence Security Threat Research Team between June and December of last year, API-based account login and registration transactions increased by 92 percent to more than 850 million. Highlighting the fact that attackers love APIs just as much as developers, that same dataset showed account takeover (ATO) attacks on login APIs increased by 62 percent.


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/31154135/Cequence.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/31154135/Cequence.png)


The initial impact of an ATO on an end user is to panic – they often get a message like, “you have received a password reset notification from your favorite retailer/social media/financial institution because your account has been compromised.”


Being a victim of account takeover isn’t very fun and causes one to want to stop doing business with the organization the account is for. The impact on the business is not only the potential loss of customers, but the impacts can be felt directly on the bottom line due to lost sales, infrastructure cost overruns and damage to the brand.


![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)


The Evolution of ATO Attack Techniques
--------------------------------------


ATO techniques have expanded beyond the commonly used hot-and-heavy, high-volume [credential stuffing](https://www.cequence.ai/blog/tales-from-the-front-lines-attackers-target-apis-with-get-based-atos/), to include methodical low-and-slow attacks using specific usernames and passwords.


These patterns are best exemplified in attacks on companies and individuals with a significant social presence (i.e., reviews, recommendations, etc.). For them, account takeovers are a persistent problem where the goal is to not necessarily steal from the compromised account, but to use it to amplify positive or negative information.


Between mid-July and late September 2021, one organization we examined experienced four distinct attack-defend cycles, outlined below.


[![Four ATO attack-defend cycles](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/31155223/IMG_4010-1024x569.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/31155223/IMG_4010.jpg)


* Phase 1: ATO mitigation was enabled during the first week of July, resulting in an immediate impact. Bots disappeared – but only for about a week.
* Phase 2: Bots returned with a vengeance beginning in late July, continuing for nearly two months with pedal to the metal, high-volume attacks consuming up to 80 percent of all login traffic. In this phase, the attackers continuously retooled their efforts every other day – looking for weaknesses in the defense. They also used hundreds of thousands of clean residential proxy IPs to distribute their actions and mask their identity and location.
* Phase 3: In yet another attempt to hide in plain sight, during this phase, attackers shifted from high-volume to low-and-slow, mixing their evasive techniques. Attackers were seen reverse engineering good browser fingerprints and farming legitimate cookie profiles (both site-specific and common web tools like Google Analytics). For a period of more than three weeks, bot activity never exceeded 20 percent of overall traffic.
* Phase 4: Bot activity has dropped to nearly an all-time low.


The patterns observed here have been seen previously in one form or another in other customer environments. Bots go quiet for a time period and they return with a vengeance. Monitoring bot forums confirms that botters often collaborate by sharing ideas, probing for unprotected vectors (like a deprecated API), all in preparation for the next attack. A successful defense requires continued vigilance, monitoring all types of endpoints – web, API and mobile, and collaboration between your peers and with your protection provider.


ATO is a problem that more and more organizations are facing as threat actors want to steal gift cards, access one-click purchasing and dominate [hype-sales to buy and resell](https://threatpost.com/pandemic-grinchbots-surge-activity/176898/) the inventory. As we have seen through this analysis, the pace and vigor are on the rise. All organizations that have an authenticated application should consider monitoring for ATO, and build mitigations to ensure their customer satisfaction remains high.


***Jason Kent*** ***is* *Hacker-in-Residence at [Cequence Security](https://www.cequence.ai/)**.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by visiting our [microsite](https://threatpost.com/microsite/infosec-insiders-community/]).***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Expand]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Agriculture]] [[victim.industry.name=Retail]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ato]] [[High-volume]] [[ThreatPost]]

