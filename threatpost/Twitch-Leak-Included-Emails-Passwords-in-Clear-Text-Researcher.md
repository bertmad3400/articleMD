# Twitch Leak Included Emails, Passwords in Clear Text: Researcher
### A researcher combed through the Twitch leak and found what they said was evidence of PayPal chargebacks with names and emails; employees’ emails; and more. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175390)
+ Date: October 7, 2021  4:25 pm
+ Author: Lisa Vaas


## Article:
Twitch users, if you haven’t changed your password yet, go. Now. Do it.


Your email and password may already have been leaked – unhashed, unencrypted, in cleartext.


Researchers have been squeezing the live-streaming service’s innards after 135 gigabytes of its internal data were [smeared all over 4chan](https://threatpost.com/twitch-source-code-leaked/175359/) by an anonymous poster on Tuesday.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


It’s a horrific leak that included the Amazon-owned service’s source code, comments dating back to the dawn of Twitch time, security tools, an unreleased Amazon Game Studios competitor to Steam (codenamed Vapor), a list of of the highest-paid channels plus [how much they were paid](https://www.businessinsider.com/how-much-your-favorite-twitch-creator-earnings-paid-2021-10) (FYI: A channel operated by voice actors took the top spot, making about $10 million in two years), and more.


Emails, Passwords in Plaintext
------------------------------


Since Tuesday, the “and more” has been unpacked to reveal what many experts predicted: Namely, this wasn’t just a direct attack on Twitch, in spite of the attacker calling the service a “disgusting toxic cesspool.”


Rather, it was also an attack on Twitch users, whose personal information was breached.


An independent security researcher who requested anonymity found streamers’ email addresses and passwords in plain text in one exposed datastore. The researcher shared the following Twitch screenshot with [PrivacySharks](https://www.privacysharks.com/), which subsequently shared it with Threatpost.


When Threatpost contacted Twitch, a representative sent this statement: “At this time, we have no indication that login credentials have been exposed. We are continuing to investigate. Additionally, full credit-card numbers are not stored by Twitch, so full credit-card numbers were not exposed.”


It Was a Misconfigured Switch
-----------------------------


On Wednesday, Twitch [disclosed](https://blog.twitch.tv/en/2021/10/06/updates-on-the-twitch-security-incident/) that “some data” was exposed to the internet due to “an error in a Twitch server configuration change that was subsequently accessed by a malicious third party.” It said that its teams were urgently investigating, but that it hadn’t found any evidence that login credentials had been exposed.


“We are continuing to investigate,” Twitch said.


On Thursday, the service reset all keys “​​out of an abundance of caution” and directed streamers to get new keys [here](https://dashboard.twitch.tv/settings/stream).


PayPal Chargebacks, Scraping Competitors’ Sites, Employee Data
--------------------------------------------------------------


In spite of Twitch’s failure to find any evidence of exposed user data, the independent researcher shared with PrivacySharks other datastores containing personal data, including a PayPal file containing details on more than 1,000 chargebacks made from Twitch to various platforms.


The records include full names, email addresses, buyer comments and amounts. The redacted screenshot below is an example of what the file contained:


The anonymous leaker called Tuesday’s 135 gigabytes data dump “part one” of the leak, but they didn’t say what else might be coming or when.


But so far, as the researcher told PrivacySharks, the leak has also included back-end employees’ names, email addresses and positions.


The researcher also discovered evidence that Twitch has allegedly been scraping competitors’ services for live channels and view counts. They shared this screen capture:


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/07155356/scraping_competitors-e1633636454969.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/07155356/scraping_competitors-e1633636454969.png)


Twitch Allegedly Has Anti-View-Botting Tech Up Its Sleeve
---------------------------------------------------------


Finally, the researcher also found screenshots that indicate that Twitch is allegedly ramping up its technology to detect and prevent view-botting on the platform. View-botting is when streamers artificially inflate their concurrent-view count by using “illegitimate scripts or tools,” [according to Twitch](https://help.twitch.tv/s/article/how-to-handle-view-follow-bots?language=en_US#viewbotting).


Bots aren’t all bad. Good bots help keep weather, sports and other news updated in real-time, and they can help find the best price on a product or track down stolen content. Bad bots, however, can dish out malware and can be used for hacking, spamming, spying, [spreading fake news](https://www.cits.ucsb.edu/fake-news/spread) and compromising websites of all sizes, as [Kaspersky](https://www.kaspersky.com/resource-center/definitions/what-are-bots) has explained.


When it comes to a service like Twitch, streamers use view-fraud bots “to boost their streams and get on the virtual leaderboard where they hope to attract legitimate followers and views,” according to [Fraud Blocker](https://fraudblocker.com/articles/what-is-a-viewbot). That’s similar to how other platforms work, by promoting popular channels more than new and unpopular channels.


Twitch is apparently, allegedly working on technology to kill those view-bots. The researcher who was looking over Twitch’s doxxed data claimed that Twitch uses what PrivacySharks described as “detection tactics involving broadcast statistics to see whether or not streamers are using view-bots.”


In a Thursday [blog post](https://www.privacysharks.com/twitch-leaked-files-confirm-active-viewbot-detection-for-partners/), PrivacySharks shared a screenshot, replicated below, that shared what allegedly look like Twitch’s botting-battle plans:


“This will compute partnerships-relevant information for each broadcast for which edge playlist requests were made (in other words, a broadcast that someone, somewhere cared about), including basic broadcast summary statistics, whether the broadcast was botted, roughly how many of the views were real, how concurrents numbers change if we factor out the botted views, and some information on chat activity. ”


Why Does View-Botting Matter?
-----------------------------


Twitch’s embrace of anti-view-bot technology shouldn’t surprise anyone: In April, Twitch announced that it was cracking down on the bots, leading many Twitch streamers to [hemorrhage](https://cogconnected.com/2021/04/twitch-anti-viewbot-measures/) followers.



As PrivacySharks’s Madeleine Hodson explained in Thursday’s blog post, amassing a large following is crucial to getting popular on Twitch, and when she says “crucial,” she’s talking dollar signs.


“Not only does this increase earnings on the platform from subscriptions and donations, but it can result in lucrative partnerships with third-party companies,” she wrote. “However, if companies are advertising products with Twitch creators that are streaming to a mostly fake audience, a lot of money is being spent to no avail.”


A Pound of Source-Code Flesh
----------------------------


But while view-bots matter to streamers and advertisers in the Twitch ecosystem, the source-code leak is what makes cybersecurity professionals perk up their ears.


Jon Murchinson, CEO of Blackpoint Cyber, told Threatpost that from an information security standpoint, “Source code and software development kits are the crown jewels that you want to protect at all cost.”


He and others predicted that the leak could result in adversaries uncovering critical vulnerabilities that could be weaponized for future use. “While details are still scarce, this highlights the difficulty with securing distributed cloud and on-prem infrastructure,” Murchinson commented.


June Werner, cyber-range engineer at Infosec Institute, agreed that the source-code leak “may make it easier for malicious actors to find exploits on Twitch’s platform in the future.”


To reiterate, Twitch hasn’t acknowledged the leak of personal data. But given the findings of PrivacySharks’ researcher contact, and just to stay on the safe side, Werner suggested that to protect themselves, Twitch users should enable two-factor authentication (2FA) and ensure that they’re not using their old Twitch password for any other accounts.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Twitch,]] [[Twitch’s]] [[Threatpost]] [[PrivacySharks]] [[ThreatPost]]
