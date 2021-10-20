# Google Crushes YouTube Cookie-Stealing Channel Hijackers
### Google has caught and brushed off a bunch of cookie-stealing YouTube channel hijackers who were running cryptocurrency scams on, or auctioning off, ripped-off channels. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175617)
+ Date: October 20, 2021  3:45 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/20143313/cookie-monster-e1634754805919.jpeg)
Google has caught and brushed off a bunch of cookie-stealing YouTube channel hijackers who were running cryptocurrency scams on the ripped-off channels.


In a [Wednesday post](https://blog.google/threat-analysis-group/phishing-campaign-targets-youtube-creators-cookie-theft-malware/), Ashley Shen, with Google’s Threat Analysis Group (TAG), said that TAG attributes the assaults to a group of attackers recruited from a Russian-speaking forum. Since late 2019, they’ve been luring targets with fake collaboration come-ons, including requests to purchase ads on their targets’ channels.


(The collaboration pitch is similar to how [now-shuttered] Twitter accounts have been used to [catfish security researchers](https://threatpost.com/twitter-suspends-security-researchers/175524/) by setting their traps with zero days and collaboration invitations.]


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

The YouTube channel hijackers are financially motivated, Shen said, looking to either auction off the stolen channels or use them to broadcast cryptocurrency scams.


Cookie Monsters
---------------


In order to elbow rightful channel owners out of the way, the attackers have been targeting YouTubers with [cookie theft](https://threatpost.com/apple-fixes-cookie-theft-bug-in-ios-9-2-1/115970/) malware.


Cookie theft, which is also called [session hijacking](https://cwatch.comodo.com/blog/website-security/what-is-session-hijacking/) or pass-the-cookie attack, involves a crook inserting themself between a computer and a server in order to steal what’s known as a [magic cookie](https://en.wikipedia.org/wiki/Magic_cookie): a session that authenticates a user to a remote server. After stealing the cookie, an intruder can monitor and potentially capture everything from the account and can take full control of the connection.


Cookie thieves can, for example, change existing codes, modify server settings or install new programs in order to steal data, set up a back-door entry for attackers, and lock legitimate users out of their own accounts.


As Shen noted in her post, the attack has been around since nearly the dawn of HTTP itself, and it’s recently resurged: “While the technique has been around for decades, its resurgence as a top security risk could be due to a wider adoption of multi-factor authentication (MFA) making it difficult to conduct abuse, and shifting attacker focus to social engineering tactics,” she suggested.


Google’s Recipe for Phish Stew
------------------------------


Google’s got some bragging rights when it comes to sticking a spoke into these wheels, of which there have been quite a few: Since May 2021, the company has blocked 1.6M phishing messages sent to targets, displayed around 62K Safe Browsing phishing page warnings, blocked 2.4K files and successfully clawed back about 4K hijacked accounts.


The cookie-stealing, cryptocurrency-scam running channel hijackers are still out there, but they’ve shifted from Gmail to other email providers: “mostly email.cz, seznam.cz, post.cz and aol.com,” Shen wrote. Google has also given details to the FBI so that the bureau can investigate further.


Fake Ad-Buying Pitches From Fake AV Company
-------------------------------------------


Among other tactics, the attackers have been socially engineering their targets by waving ad-buying dollars under their noses. They send emails posing as an existing company that’s interested in collaborating on a video ad placed on the target’s channel.


Here’s one example of the type of channel-flattering suck-up-ery in the phishing emails:


Next up for anybody who falls for it is the malware landing page, disguised as a software-download URL sent via email or as a PDF on Google Drive or, in a few cases, tucked as a phishing link into a Google document.


Shen said that Google identified about 15,000 accounts behind the phishing emails, most of which were specifically created for this campaign.


So far, Google’s identified at least 1,011 domains created just for this campaign. They’re flaunting big names of legitimate sites run by brands such as Luminar, Cisco VPN and Steam games.


The attackers also posed as a company offering a “Covid19 news software,” as shown in the screen capture below, which depicts a malware landing page and its lure message:


Google also came across a fake Instagram page, shown below, that copied content from a real cloud gaming platform and replaced its URL with one leading to a cookie-theft malware download.


Smash-and-Grab Before Detection Catches Up
------------------------------------------


After a target falls for a lure and runs the fake software, the cookie-stealing malware executes. The malware steals browser cookies and uploads them to the attackers’ command-and-control (C2) servers.


It’s a quick turn-around operation, according to Google TAG: “Although this type of malware can be configured to be persistent on the victim’s machine, these actors are running all malware in non-persistent mode as a smash-and-grab technique,” Shen explained.


That’s a good way to escape detection, she said: “If the malicious file is not detected when executed, there are less artifacts on an infected host and therefore security products fail to notify the user of a past compromise,” she wrote.


Selling Hijacked Channels, Cryptocurrency Scams
-----------------------------------------------


Many of the hijacked channels were rebranded for cryptocurrency scam live-streaming. “The channel name, profile picture and content were all replaced with cryptocurrency branding to impersonate large tech or cryptocurrency exchange firms,” according to the writeup. “The attacker live-streamed videos promising cryptocurrency giveaways in exchange for an initial contribution.”


If they’re not being used to hawk cryptocurrency scams, the channels are selling on account-trading markets at between $3 and $4,000 USD, depending on how many subscribers they have.


Google traced the campaigns to “hack-for-hire” attackers recruited on Russian-language forums via the job description shown below:


Protecting Your Channel
-----------------------


Google’s taken a number of steps to ward off these attacks, including:


The company also passed along these tips for users:


In fact, pass-the-cookie attacks are “a testament to the importance of enabling MFA on sensitive accounts,” according to Stefano De Blasi, Cyber Threat Intelligence Analyst at Digital Shadows.


“Due to the extra layer of security granted by MFA, the attackers most likely had to increase the sophistication of their operation (targeted phishing emails and ad-hoc fraudulent domains) to breach these YouTube accounts” he noted in an email to Threatpost on Wednesday. “Ultimately, despite the emergence of attack methods such as Pass-the-Cookie, MFA currently remains the best defense against cybercriminals interested in stealing employees’ credentials, as it prevents other account takeover tactics such as credential reuse and brute-forcing.”


More Tips
---------


John Bambenek, Principal Threat Hunter at Netenrich, told Threatpost on Wednesday that on the upside, these types of attacks tend to only be partial account takeovers. “Cookie theft, by itself, is usually not enough to allow someone to change [a] password, remove 2FA, or otherwise seize the account,” he said via email.


But creators who are making real money might want to take a few more precautions, Bambenek advised: “They may wish to subscribe to their own channels via their smart phone (using a different account than what they publish with) so they can get notices when new content is uploaded,” he suggested. “They may also wish to use dedicated hardware for streaming and publishing that is the only place they log into with their creator account, which will greatly mitigate any impact malware may have. The more money that their channel involves, the more protection they should think about.”


As far as mitigating these attacks goes, it’s complex, De Blasi said, given that they’re not exactly rocket science: They don’t require “an in-depth knowledge of the original user or any particular administrator rights,” he said.


Still, security teams “can establish tighter measures on how authentication cookies are stored and how frequently they are deleted,” he continued. “Additionally, aligning this authentication method with other security best practices like digital footprint tracking and behavior monitoring is the best way to mitigate against credential-based attacks.”


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Google]] [[malware]] [[phishing]] [[Google’s]] [[YouTube]] [[Threatpost]] [[ThreatPost]]
