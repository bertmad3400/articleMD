# Google Play Sign-Ins Allow Covert Location-Tracking
### A design flaw involving Google Timeline could allow someone to track another device without installing a stalkerware app.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169151)
+ Date: September 2, 2021  12:03 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/02115807/Google-Timeline-e1630598317516.jpg)
It’s possible to track someone’s user location via Google Play sign-ins, a researcher has discovered – a potential stalker avenue that, so far, the internet behemoth has yet to address.


“With the aid of Google I was able to ‘spy’ on my wife’s whereabouts without having to install anything on her phone,” said Malwarebytes Labs researcher Pieter Arntz, in a [Wednesday posting](https://blog.malwarebytes.com/awareness/2021/09/google-play-sign-ins-can-be-abused-to-track-another-persons-movements/). “In my defense, this whole episode happened on an operating system that I am far from an expert on (Android), and I was trying to be helpful. But what happened was unexpected.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


In short: Arntz logged into his Google Play account from his wife’s phone, in order to pay for an app that that she wanted to install. Then he handed the phone back to her, forgetting to log out. And that’s when the weirdness started.


**Google Timeline for Good and Evil(ish)**
------------------------------------------


“I was investigating how much information the Google Maps Timeline feature was gathering about me,” Arntz explained. “The timeline is an often-overlooked Google feature that ‘shows an estimate of places you may have been and routes you may have taken based on your Location History.’ I was curious to see what Google records about me, even though I never actively check in or review places.”


In the course of looking at the timeline, he started noticing that Google was marking him down at places he hadn’t visited that day. After wondering if it was a glitch, one update came through showing a location that he knew his wife had been to.


“Suddenly, it dawned on me: I was actually receiving location updates from my wife’s phone, as well as mine,” he said.


Thinking that logging out of Google Play on his wife’s phone would resolve the issue, Arntz was surprised to see that Google automatically added his account to his wife’s phone.


“After some digging I learned that my Google account was added to my wife’s phone’s accounts when I logged in on the Play Store, but was not removed when I logged out after noticing the tracking issue,” he said – forcing the need to manually remove his account from settings.


Making matters even worse, it’s almost unnoticeable if this situation is in play, he added – there’s no indication other than a barely noticeable icon when Google Play is opened:


“The only thing that might have alerted my wife to this unintentional surveillance—but never did—was my initial in a small circle at the top right corner of her phone, when she used the Google Play app,” he explained. “You have to touch the icon to see the full details of the account that is logged in.”


Bottom line? Google will record the location of whatever phone a person has logged into. So, it’s not even necessary for someone to install one of the insidious stalkerware apps that have [flooded the marketplace](https://threatpost.com/stalkerware-volumes-high-bans/164325/) in order to keep tabs on where someone has been, making covert surveillance by, say, a controlling partner or estranged spouse all the easier to carry out.


“This really is a low-effort method of spying on someone’s whereabouts,” Arntz nutshelled. “Plus, you do not need to install anything and there is only a minimal chance of being found out.”


One more potential concern, the researcher added, and it’s an ominous one:


“While this post talks about Google Maps location information, I’m pretty sure there will be other apps that are linked to your account rather than to your phone,” he said. “Those apps could be queried for information by people other than the owner of the phone if they are logged into Google Play.”


**Feature or Bug? Potential Fixes for Google**
----------------------------------------------


Arntz said that he submitted a bug report to Google, but he’s not hopeful it will address the potential for misuse.


“I’m afraid they will tell me that it is a feature and not a bug,” he said. “[But] there are a few things that Google could improve here.”


That includes ensuring that Timeline gathers data only on the phones it’s actually enabled on.


“Google timeline was enabled on my phone, not on my wife’s, so I feel I should not have received the locations visited by her phone,” Arntz said.


Another easy fix would be to send an alert to the user that the phone’s location is being shared to a different phone with Timeline enabled – or, at the very least, that someone else logged into Google Play from one’s device.


“When I logged in under my account on her Google Play, I got a ‘logged in from another device’ warning,” the researcher said. “I feel there should have been something similar sent to her phone. Something along the lines of ‘someone else logged into Google Play on your phone.'”


**Tech Abuse on the Rise**
--------------------------


While the situation doesn’t represent a by-design attempt to work around a user’s consent, it’s still a design and user-experience flaw, Arntz noted.


“We should be very clear here…this situation is not a form of stalkerware,” he explained. “However, it is still a flaw that can and should be called out, because the end result can still provide location tracking of another person’s device.”


The potential abusive misuse of legitimate technology should be [of concern](https://threatpost.com/google-bans-stalkerware-ads-with-a-loophole/157365/) for Google and any other app provider, according to Eva Galperin, director of cybersecurity for Electronic Frontier Foundation (EFF).


The flaw “does highlight the importance of quality assurance and user testing that takes domestic abuse situations into account and takes the leakage of location data seriously,” Galperin said. “One of the most dangerous times in a domestic abuse situation is the time when the survivor is trying to disentangle their digital life from their abusers’. That is a time when the survivors’ data is particularly vulnerable to this kind of misconfiguration problem and the potential consequences are very serious.”


Google did not immediately return a request for comment.


Arntz added, “Of course, a cynic might say that the fundamental obstacle here is that if your business model demands that you hoover up as much information about somebody as possible, the opportunities for this kind of unintentional, tech-enabled abuse are likely to increase.”


**How to Prevent Google-based Surveillance**
--------------------------------------------


The only way for users to make sure they’re not being tracked from another phone via Timeline (or any other location-sharing app) is to check which accounts have been added to one’s phone.


This can be done by going to Settings > Accounts and Backups > Manage Accounts. There will be a list of Google accounts linked to the phone, and users can click on the accounts they want to remove.


“After removing my account from there on my wife’s phone the tracking issue was finally resolved,” Arntz noted.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





#### Tags:
[[Google]] [[Arntz]] [[wife’s]] [[said.]] [[phone,]] [[Timeline]] [[it’s]] [[phone.]] [[phone,”]] [[explained.]] [[ThreatPost]]
