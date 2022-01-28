# Conti, DeadBolt Target Delta, QNAP
### QNAP had to push out an unexpected (and not entirely welcome) NAS device update, and Delta Electronics' network has been crippled.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178083
+ Date: 2022-01-28T14:15:47+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/03083226/shutdown-ransomware.jpg)

Two Taiwanese companies were affected by separate ransomware incidents this week, forcing one to scramble to restore crippled systems and another to push out an emergency update to mitigate attacks on its customers.


Delta Electronics, an electronics company that provides products for Apple, Tesla, HP and Dell, disclosed Friday that “non-critical systems” were attacked by “overseas hackers” – an attack that’s been [attributed](https://www.bleepingcomputer.com/news/security/taiwanese-apple-and-tesla-contractor-hit-by-conti-ransomware/) to the [Conti Group](https://threatpost.com/conti-gang-ransomware-attack-mcmenamins/177119/).


Meanwhile, Taiwanese storage and networking equipment provider [QNAP Systems](https://www.qnap.com/en?ref=header_logo) forced out an update to its customers’ network attached storage (NAS) devices after [warning them](https://www.qnap.com/en/security-news/2022/take-immediate-actions-to-stop-your-nas-from-exposing-to-the-internet-and-fight-against-ransomware-together) earlier this week that the DeadBolt ransomware was in offensive mode against them.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“DeadBolt has been widely targeting all NAS exposed to the Internet without any protection and encrypting users’ data for Bitcoin ransom,” the company said in a statement.


**More Disruptive Attacks**
---------------------------


Indeed, ransomware, the volumes of [which hit record highs](https://threatpost.com/ransomware-volumes-record-highs-2021/168327/) in 2021, shows no signs of slowing in 2022. In fact, attackers appear to be taking aim at companies in a way that can cause even more disruption by creating a ripple effect across their ecosystem of customers and technology partners, hitting numerous industries at once and forcing victims to respond quickly, observed one security professional.


“Cybercriminals continue to target organizations that provide a service or product to larger organizations with the expectation that they cannot suffer downtime due to a ransomware attack and will be inclined to pay up faster,” James McQuiggan, security awareness advocate at security firm [KnowBe4](http://www.knowbe4.com/), said in an email to Threatpost.


Indeed, Conti’s attack on Delta Electronics – which occurred last Friday – has the potential to affect the high-profile customers to whom it supplies products in the United States if it’s not contained.


Delta officials said in their statement that the company reacted quickly to the attack, which has had “no significant impact on operations.” Delta is working with Trend Micro and Microsoft as well as the appropriate authorities to investigate the attack and restore the systems affected, according to reports.


However, the Taiwanese news outlet CTWANT [painted](https://www.ctwant.com/article/165246) a far more dire picture, claiming that attackers – identified as the [Conti Group](https://threatpost.com/conti-ransomware-backups/175114/) – encrypted more than 1,500 servers and more than 12,000 of the company’s 65,000 computers and is demanding a ransom of $15 million to decrypt the data.


Further, [a report](https://therecord.media/conti-ransomware-hits-apple-tesla-supplier/) in Recorded Future’s The Record said that the company still has not restored most of its systems, using [an alternative web server](https://www.deltapowersolutions.com/en/index.php) to communicate with customers while its [official website](https://www.deltaww.com/) remains offline for “system maintenance,” according to a message on its homepage.


**Targeted Assault on QNAP NAS**
--------------------------------


While Delta grapples with the aftermath of the Conti attack, fellow Taiwanese company QNAP had to do a clean-up of its own after customers this week began reporting on QNAP message boards and Twitter that the DeadBolt ransomware screen was coming up when they logged into their QNAP NAS devices.


“I just got hacked,” tweeted one of the victims, MIT research scientist and podcast host [Lex Fridman](https://twitter.com/lexfridman) on Thursday. “Ransomware named DeadBolt found an exploit in [@QNAP\_nas](https://twitter.com/QNAP_nas) storage devices, encrypting all files.”



> 
> I just got hacked. Ransomware named DeadBolt found an exploit in [@QNAP\_nas](https://twitter.com/QNAP_nas?ref_src=twsrc%5Etfw) storage devices, encrypting all files. They ask $1,000 from individuals or $1.8 million from QNAP. I have 50tb of data there, none of it essential or sensitive, but it hurts a lot. Time for a fresh start. [pic.twitter.com/E8ZkyIbdfp](https://t.co/E8ZkyIbdfp)
> 
> 
> — Lex Fridman (@lexfridman) [January 27, 2022](https://twitter.com/lexfridman/status/1486609372176429057?ref_src=twsrc%5Etfw)
> 
> 



As of Friday morning, a [search on Censys](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=100&virtual_hosts=EXCLUDE&q=services.http.response.body%3A+%22All+your+files+have+been+locked+by+DeadBolt%22) showed that DeadBolt had already encrypted 3,687 of the NAS devices. The ransomware [reportedly](https://www.bleepingcomputer.com/news/security/qnap-force-installs-update-after-deadbolt-ransomware-hits-3-600-devices/) adds the .deadboltextension to file names to lock customers out.


The ransomware also replaces the device’s regular HTML login page with a ransom note demanding 0.03 bitcoins, or about $1,100, to receive a decryption key and recover data.


Indeed, Fridman said attackers were asking $1,000 from individuals or $1.8 million from QNAP for a decryption key. “I have 50tb of data there, none of it essential or sensitive, but it hurts a lot,” he tweeted. “Time for a fresh start.”


**Ransomware-Inspired Update**
------------------------------


QNAP responded to the reports first by asking all of its NAS customers to immediately update their QNAP NAS devices to the latest version of the firmware, [version 5.0.0.1891](https://www.qnap.com/en-us/release-notes/qts/5.0.0.1891/20211221), released on Dec. 23. However, overnight on Thursday, the company began forcing the update out to all affected QNAP NAS devices.


Though the company appeared to have its customers’ best interests in mind with the move, not all of them were happy by the unexpected update.


“You do realize that for those who have deployed QNAPs in production environments, when you as a vendor force an update that your customer ISN’T EXPECTING, it can cause an outage at potentially bad times,” grumbled one user called [EvilMastermindG](https://www.reddit.com/user/EvilMastermindG/) on a [Reddit QNAP message board](https://www.reddit.com/r/qnap/comments/sdz7e5/you_want_to_know_why_your_qnap_updated_last_night/huhlp5t/). “Worse, an update can break or remove functionality that the customer was relying on.”


Rather than force its hand, QNAP should have exercised transparency and told customers exactly what security vulnerabilities were present in the devices, regardless of how it might reflect on the company, the user said.


“What you SHOULD do as a company is to effectively communicate specifically what the security vulnerabilities are, even if they’re stupid enough to make you guys look bad, and then let them make their own decisions as far as mitigation,” EvilMastermindG said.


Those potential mitigation tactics include opening the Security Counselor on QNAP NAS devices and checking to see if they are exposed to the internet, which means they’re “at high risk” of attack by threat actors, according to QNAP.


The company also said that customers with exposed NAS devices can disable both the Port Forwarding function of the router as well as the Universal Plug and Play function of the device to protect the devices against attack.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Taiwan]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Qnap]] [[Nas]] [[Ransomware]] [[Deadbolt]] [[Conti]] [[Fridman]] [[ThreatPost]]

