# T-Mobile’s Security Is ‘Awful,’ Says Purported Thief
### John Binns, claiming to be behind the massive T-Mobile theft of >50m customer records, dissed the security measures of the US’s No. 2 wireless biggest carrier. T-Mobile is “humbled,” it said, announcing new partnerships with security heavyweights on Friday.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169011)
+ Date: August 28, 2021  12:58 pm
+ Author: Lisa Vaas


## Article:
On Thursday, a 21-year-old US citizen claiming to be the attacker who stole data on more than 50 million T-Mobile customers called the telecom’s security “awful.”


On Friday, a “humbled” T-Mobile CEO Mike Sievert wiped the egg from his face and [apologized](https://www.t-mobile.com/news/network/cyberattack-against-tmobile-and-our-customers) for the debacle, the repercussions of which have affected a total of more than 50 million customers at this point. As of Aug. 18, T-Mobile had estimated the total number of ripped-off records to be [~40 million](https://threatpost.com/t-mobile-40-million-customers-data-stolen/168778/): a number that [rose to ~50 million](https://www.t-mobile.com/news/network/additional-information-regarding-2021-cyberattack-investigation) on Aug. 20 and could double if the purported thief is true to his word.


When [the breach](https://threatpost.com/t-mobile-investigates-100m-records/168689/) was widely reported 11 days ago, the purported thief was offering to sell 30 million records for ~1 penny each on an underground forum: what he claimed was a subset of 100 million customer records. He alleged that he was going to sell the other 50 million privately. As of Thursday, he hadn’t acknowledged having sold any of the records.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The [Wall Street Journal](https://www.wsj.com/articles/t-mobile-hacker-who-stole-data-on-50-million-customers-their-security-is-awful-11629985105?mod=article_relatedinline) has been chatting with the purported attacker via Telegram for a while. The news outlet has confirmed that his name is John Binns: a 21-year-old US citizen of Turkish descent who moved to Turkey a few years ago. Binns reportedly discussed details about the breach before they were widely known.


The WSJ noted that T-Mobile was initially notified of the breach by a cybersecurity company called [Unit221B LLC](https://unit221b.com/), which said that the telecom’s customer data was being peddled on the dark web.


Who is John Binns?
------------------


Binns told the WSJ that he conducted the attack from his home in Izmir, Turkey, where he lives with his mother. His father, who died when he was two, was American, while his mother is Turkish. They moved back to Turkey when Binns was 18.


If the name rings a bell, it’s because the seller told Alon Gal, CTO of cybercrime intelligence firm [Hudson Rock](https://www.hudsonrock.com/), that this sucker-punch to US infrastructure was done in retaliation against the US for the kidnapping and torture of John Binns at the hands of CIA and Turkish intelligence agents in 2019, as Gal tweeted at the time (from an account that has since been suspended).



> This breach was done to retaliate against the US for the kidnapping and torture of John Erin Binns (CIA Raven-1) in Germany by CIA and Turkish intelligence agents in 2019. We did it to harm US infrastructure. —Attacker’s alleged statement to Gal
> 
> 


It’s not clear who “we” refers to, but Binns said he needed help. In his conversation with the WSJ, Binns described the attack as a “collaborative effort to find the login credentials needed to crack T-Mobile’s internal databases,” and that another online actor offered, in online forums, to sell some of the stolen T-Mobile data.


Binns [sued](https://casetext.com/case/binns-v-cent-intelligence-agency) the FBI, CIA and Department of Justice in 2020, alleging that he was tortured and harassed by the US and Turkish governments and is seeking to compel the US to release documents regarding these activities under the Freedom of Information Act. He told the WSJ that the kidnapping story is legitimate – why would he lie?:



> I have no reason to make up a fake kidnapping story and I’m hoping that someone within the FBI leaks information about that. —John Binns, as quoted by the WSJ
> 
> 


Binns reportedly uses the online handles IRDev and v0rtex, among others. He’s apparently got a track record that includes “peripheral involvement” in the creation of a [massive botnet](https://www.wsj.com/articles/web-attack-stemmed-from-game-tactics-1477256958?mod=article_inline) of compromised devices that was used for online attacks four years ago, having been in cahoots with the gamers who infected devices around the world.


These botnets are often used by gamers to knock people and websites offline in distributed denial-of-service (DDoS) attacks. The [pandemic caused a surge](https://threatpost.com/ddos-attacks-skyrocket-pandemic/159301/) in such attacks: As of September 2020, more people were online during lockdowns and work-from-home shifts, making for lucrative pickings for DDoS-ers.


T-Mobile’s ‘Awful’ Security
---------------------------


Binns told the WSJ that he penetrated T-Mobile’s defenses in July after scanning the company’s known internet addresses, looking for weak spots and using what the publication called “a simple tool available to the public.” (That tool well might have been Shodan: a search engine used to uncover servers connected to the internet that’s often used by threat actors and researchers to find vulnerabilities.)


He found an unprotected, exposed router last month, he told the Journal. From there, Binns said he managed to break into T-Mobile’s data center outside East Wenatchee, Wash., where he reportedly accessed more than 100 servers that contained the personal data of millions. By Aug. 4, he had stolen millions of files thanks to what he told the Journal was the mobile phone seller’s pathetic security:



> I was panicking because I had access to something big. Their security is awful. —John Binns, as quoted by the WSJ
> 
> 


 


Cybersecurity experts have been nodding vigorously, albeit in more diplomatic terms than “awful.” The Journal spoke with Glenn Gerstell, a former general counsel for the National Security Agency, who said that the fact that the theft included records stolen from prospective clients or former, long-gone customers shows that somebody or somebodies at T-Mobile isn’t practicing good data management hygiene: “That to me does not sound like good data management practices,” he was quoted as saying.


Granted, that work gets harder all the time. Randy Watkins, chief technology officer at cybersecurity consulting and managed detection and response (MDR) services company CRITICALSTART, told Threatpost on Friday that the attack shows how difficult it is to secure growing perimeters and how tough it is to monitor attack surfaces.


Watkins warned that alerts set off by an intruder’s activity – including initial compromise, subsequent lateral movement and data exfiltration– are dismissed at an organization’s peril: “Even if this generated alerts, they would likely be low-priority, and something that would be disregarded as a likely false-positive,” he said via email. “As attackers take advantage of these less-obvious tactics, it is becoming more critical to resolve every alert generated by detection toolsets.”


Something’s Wrong in Magenta Land
---------------------------------


By some accounts, this is the sixth time that T-Mobile has been attacked in recent years.


The US Federal Communications Commission (FCC) said last week that it’s [investigating this most recent breach](https://www.reuters.com/technology/hackers-steal-some-personal-data-about-78-mln-t-mobile-customers-2021-08-18/). T-Mobile is also facing at least two [class-action lawsuits](https://www.q13fox.com/news/t-mobile-hit-with-class-action-lawsuits-over-data-breach) accusing the company, the second-largest US wireless carrier, of failing to protect customer data.


T-Mobile was [attacked](https://www.engadget.com/t-mobile-data-breach-security-phone-number-hack-2020-172117333.html) [twice](https://www.complianceweek.com/cyber-security/t-mobile-data-breach-a-cautionary-tale-for-all-companies/28568.article) last year, and in 2018, about 2.5 million customers had their data exposed in a network breach. That attack also became part of a federal class-action lawsuit.


The most recent theft involved the records of more than 13 million current customers, more than 40 million prospective customers who had applied for credit with the company, and 667,000 former customers, T-Mobile said last week. An additional 902,000 prepaid customers also had some data exposed.


Some records contained Social Security numbers, phone numbers, names, security PINs, physical addresses, unique IMEI numbers, IMSI numbers, driver license numbers and dates of birth: in short, all the ingredients necessary for [identity theft](https://threatpost.com/identity-theft-spikes-covid-19-relief/163577/).


A source familiar with the investigation told the WSJ that the Seattle office of the FBI is investigating.


The Latest From T-Mobile
------------------------


On Friday, T-Mobile’s CEO, Mike Sievert, announced that the company has sought help on the cybersecurity front. He said in a [statement](https://www.t-mobile.com/news/network/cyberattack-against-tmobile-and-our-customers) that the company has entered into long-term partnerships with Mandiant and with consulting firm KPMG LLP.


“We know we need additional expertise to take our cybersecurity efforts to the next level – and we’ve brought in the help,” Sievert said. “These arrangements are part of a substantial multi-year investment to adopt best-in-class practices and transform our approach. This is all about assembling the firepower we need to improve our ability to fight back against criminals and building a future-forward strategy to protect T-Mobile and our customers.”


With regards to details behind the attack, Sievert painted this as the work of an erudite threat actor. “What we can share is that, in simplest terms, the bad actor leveraged their knowledge of technical systems, along with specialized tools and capabilities, to gain access to our testing environments and then used brute force attacks and other methods to make their way into other IT servers that included customer data,” he was quoted as saying in Friday’s statement.


Security experts weren’t too sure about T-Mobile’s characterization of this as a fancy attack.


Well, Good Luck With All That
-----------------------------


Some security experts said that the move to pull in the security big guns is a good step, but T-Mobile’s got a lot of gunk to scrape out, and it won’t happen overnight. Ian McShane, Field CTO of security firm Arctic Wolf and former Gartner analyst, told Threatpost that, given how many breaches T-Mobile has suffered over the last few years, he’s already skeptical about the company’s claims that the breach was a “highly sophisticated” attack. “I’m sure many others in our industry will be just as keen as I am to understand the cause and the lessons learned, especially as it seems the internal investigation was only sparked by posts from a Twitter account with what appeared to be inside knowledge,” he said.


Mark Manglicmot, vice president of security services at Arctic Wolf, told Threatpost that one of the poor practices brought to light by the breach is storing Social Security numbers in plain text. “Encryption of this data is a mandatory part of the security equation,” he pointed out.


Moreover, since this is T-Mobile’s sixth such breach in a few years, it’s apparent “they haven’t taken security seriously enough,” Manglicmot continued. “Their IT asset management and patching of systems is poor. The combination of poor defenses and a lack of capable real-time detection and response is a recipe for this type of data theft disaster. Once a data rich company like T-Mobile experiences a breach, the flood-gates open to other attackers to find additional cracks. Reports are stating their security is a mess. It’s a good step that they are bringing in reputable help to investigate and bolster defenses, but it’s going to take T-Mobile years to fully get their security program on par with their responsibility to customers.”


Then too, there’s that throbbing sore thumb: namely, the exposed router. Agio founder and CEO Bart McDonough pointed out to Threatpost that the unsecured router that Binns claimed to have exploited “appears to have had a different configuration than other routers. The hacker exploited the weakness in this non-standard configuration.” T-Mobile should have had an AI-based anomaly detection system in place, he said: one that might have caught the aberrant login and resulting data exfiltration, “allowing T-Mobile to perhaps minimize the damage from this attack.”


Many businesses aren’t as complex as T-Mobile; nor do they get targeted with such intensity. Still, there are lessons to be learned for other businesses, McDonough observed. “All businesses could benefit from enhancing their cybersecurity fundamentals. Specifically, deploying device configuration management, access management, and AI-based detection of anomalous and suspicious network activity.”


As it is, many, if not most, organizations only have a static awareness of their “surface”, e.g. internal systems exposed to the Internet, he continued. “When an administrator makes a change (or mistake) the new exposure point should set off alarms and someone should be asking the question ‘is that system, router, etc. presenting what we are intending?'”


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[T-Mobile]] [[Binns]] [[T-Mobile’s]] [[WSJ]] [[cybersecurity]] [[Threatpost]] [[it’s]] [[numbers,]] [[Sievert]] [[Aug.]] [[ThreatPost]]
