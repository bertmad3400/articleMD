# Twitch Gets Gutted: All Source Code Leaked
### An anonymous user posted a link to a 125GB torrent to 4chan yesterday, containing all of Twitch’s source code, comments going back to its inception and more. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175359)
+ Date: October 6, 2021  11:26 am
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/06111339/gamer-e1633533232320.jpeg)
An attacker claims to have ransacked Twitch for everything it’s got, including all of its source code and user-payout information.


According to [Video Games Chronicle](https://www.videogameschronicle.com/news/the-entirety-of-twitch-has-reportedly-been-leaked/) (VGC), which first reported the assault on the interactive live-streaming service, an anonymous user posted a link to a 125GB torrent to 4chan on Wednesday.


Whoever’s responsible for gutting the service that’s near and dear to gamers’ hearts rationalized it by saying that the Twitch community needs to have the wind knocked out of its lungs. They called the leak a means to “foster more disruption and competition in the online-video streaming space,” because “their community is a disgusting toxic cesspool.”


S/he’s not all wrong, by Twitch’s own admission.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

In August, Twitch responded to what it described as “botting, hate raids and other forms of harassment targeting marginalized creators.”



> 
> We’ve seen a lot of conversation about botting, hate raids, and other forms of harassment targeting marginalized creators. You’re asking us to do better, and we know we need to do more to address these issues. That includes an open and ongoing dialogue about creator safety.
> 
> 
> — Twitch (@Twitch) [August 11, 2021](https://twitter.com/Twitch/status/1425550620887375876?ref_src=twsrc%5Etfw)
> 
> 



Twitch said that it had identified and patched a vulnerability in its “proactive” filters that should help it to better detect hate speech in chat. It also said at the time that it was planning to launch channel-level ban-evasion detection and account-verification improvements later this year.


Twitch’s announcement came days after Black and LGBTQ Twitch streamers, fed up with torrents of racist and transphobic hate, boycotted the service for 24 hours in the #[ADayOffTwitch](https://twitter.com/hashtag/ADayOffTwitch?src=hashtag_click) protest. [Venture Beat](https://venturebeat.com/2021/09/03/a-day-off-twitch-gave-the-platform-its-lowest-viewer-hours-of-2021/) reported that the boycott led to the platform’s worst day so far this year, in terms of viewer hours.


The protest followed repeated “hate raids” – streams in which dozens of identical racist slurs appear in a live chat. One user who goes by “Raven” and uses the pronouns she and they, [told CNN](https://www.cnn.com/2021/09/02/tech/twitch-day-off-boycott-racism-cec/index.html) that the hate raids have only intensified since she started to tweet videos with the hashtag #TwitchDoBetter.


The Files Are Legit
-------------------


Multiple outlets, including VGC and [The Verge](https://www.theverge.com/2021/10/6/22712250/twitch-hack-leak-data-streamer-revenue-steam-competitor), as well as one of VGC’s anonymous company sources, have verified that the data thief got away with the real deal: All the files mentioned on 4chan are legitimate and are publicly available to download.


That includes the source code for Twitch, which is owned by Amazon.


VGC provided this list of what’s in the data dump:


Twitch reportedly hasn’t yet disclosed the breach to its users. Threatpost has reached out to the streaming service for comment.


Change Your Password Now: Password Hashes Also Leaked
-----------------------------------------------------


One Twitch user has also claimed that the data dump includes includes encrypted passwords — something that Jarno Niemela, principal researcher for F-Secure, told Threatpost on Thursday morning was true.


“From what we currently know…password hashes have leaked, all users should obviously change their passwords, and use 2FA [two-factor authentication] if they are not doing so already,” he said via email.


“This leak is very serious for Twitch, but the question is what effects this will have for the regular Twitch user,” Niemela said.


No User Data Affected – Yet
---------------------------


At first glance, this looks like a direct attack against Twitch only, rather than its users. Still, it’s “almost guaranteed” that user information will have been swept up in this breach, according to Archie Agarwal, founder and CEO at the threat-modeling provider ThreatModeler.


“That means that users will have to take the usual precautions of changing their account credentials and making sure they don’t use the same combination of credentials to access other services online,” he told Threatpost via email.


That’s particularly true given that this breach, as nasty and sprawling as it is, is apparently just the start. The 4chan leak was labeled as “part 1,” suggesting that there’s more to come.


For instance, user data apparently wasn’t included in the archive, but that may be in the offing, according to James Chappell, co-founder and chief innovation officer at digital-risk solution provider Digital Shadows.


“As the attacker indicated that they have not yet released all the information they have, anyone who has been a Twitch user should review all information they have given to Twitch, and see if there are any precautions they need to make so that further private information isn’t leaked,” Chappell advised. “And while it won’t help in this case, as data has already leaked, users should always be cautious on what kind of information they provide to any social-media platform.”


The Worst Possible Breach
-------------------------


Agarwal told Threatpost that breaches don’t get any worse than this one.


“Reading of a data breach that includes the entire source code, including unreleased software, SDKs, financial reports and internal red-teaming tools will send a shudder down [the spine of] any hardened infosec professional,” he said. “This is as bad as it could possibly be.”


If zero alarms went off, that clearly means that something’s not right with Twitch’s security setup, Agarwal suggested.


“The first question on everyone’s mind has to be: How on earth did someone exfiltrate 125GB of the most sensitive data imaginable without tripping a single alarm?” he asked. “There’s going to be some very hard questions asked internally.”


How Did It Happen?
------------------


Chappell told Threatpost that the 128GB torrent appears to have been acquired from one of Twitch’s internal GitHub repositories. The leaked data was then made available through torrents shared as magnet links, Chappell said.


“There appears to be evidence that the original files came from an internal GitHub server, git-aws.internal.justin.tv,” he added, noting that Justin.tv was the name of the company that eventually [became Twitch](https://en.wikipedia.org/wiki/Justin.tv#:~:text=Justin.tv%20moved%20its%20gaming,company%20could%20focus%20on%20Twitch.).


“It rebranded as Twitch in 2011 — so this looks like a long-standing piece of infrastructure,” Chappell speculated.


If the leak does get tracked back to GitHub, Twitch will find itself in good company: Microsoft’s GitHub account was [ransacked](https://threatpost.com/report-microsofts-github-account-gets-hacked/155587/) back in 2020.


Beware of Phishing
------------------


Javvad Malik, security awareness advocate at KnowBe4, told Threatpost that beyond changing passwords, Twitch streamers should also keep an eye out for future phishing attempts that build on whatever data has been leaked or will be leaked.


“Changing passwords, especially if the same password has been used on other systems, is a good first step for affected users,” he commented. “But it’s also worth bearing in mind that not all attacks based on information on these leaks will come immediately.”


He added, “Criminals can use the data within the leak to formulate convincing phishing attacks over weeks or months. So it’s important for Twitch users to remain vigilant of emails, text messages, physical letters or even phone calls claiming to be from Twitch, or a related service.”


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Threatpost]] [[it’s]] [[Twitch’s]] [[Twitch,]] [[Chappell]] [[4chan]] [[passwords,]] [[said.]] [[GitHub]] [[ThreatPost]]
