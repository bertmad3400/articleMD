# Free Discord Nitro Offer Used to Steal Steam Credentials
### A fake Steam pop-up prompts users to ‘link’ Discord account for free Nitro subs.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176011)
+ Date: November 4, 2021  12:18 pm
+ Author: Becky Bracken


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2018/08/01084854/Steam-logo.jpg)
There’s a new scam making the rounds on Discord, through which cybercriminals can harvest Steam account information and make off with any value it contains.


Gamer-aimed Discord scams are [just about everywhere](https://threatpost.com/various-malware-lurking-in-discord-app-to-target-gamers/163867/). But researchers flagged a new approach as noteworthy because it crosses over between Discord and the Stream gaming platform, with crooks offering a purported free subscription to Nitro (a Discord [add-on](https://discord.com/nitro) that enables avatars, custom emoji, profile badges, bigger uploads, server boosts and so on), in exchange for “linking” the two accounts.


Researchers at Malwarebytes Labs released a report detailing the new [Discord Nitro tactic](https://blog.malwarebytes.com/malwarebytes-news/2021/11/this-steam-phish-baits-you-with-free-discord-nitro/), explaining that the target is first served a malicious direct message on Discord with the fake offer:


“Just link your Steam account and enjoy,” the message says, and it includes a link purportedly to do just that. The malicious link takes users to a spoofed Discord page with a button that reads, “Get Nitro.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


There are several malicious domains associated with the spoofed page, analysts noted:


The button initiates a fake pop-up window that appears to send targets off to Steam — but in fact, it keeps them on the same malicious page.


**Fake Pop-Up Ads**
-------------------


As Malwarebytes Labs explained in the report, once a victim clicks on the button, the site appears to serve a Steam pop-up ad, but researchers explained the ad is still part of the same malicious site. The gambit is intended to fool users into thinking they’re being taken to the Steam platform to enter in their login information — supposedly to fulfil the request to “link” the Steam account with Discord for the free Nitro subscription.


“When Discord users key in their Steam credentials in the fake pop-up, it will show them the error message saying, ‘The account name or password that you have entered is incorrect,'” the report said. “Behind the scenes, though, their Steam credentials have already been stored into the scam website.”


Stolen [gamer accounts](https://threatpost.com/gamers-malware-steam-epic-ea-origin-accounts/175081/) can fetch around $14 per 1,000 accounts in underground criminal forums, according to a report from Sept. from Kaspersky Labs — so it’s no wonder that they’ve become common targets for phishing, malware and more.


**Gaming Security Woes**
------------------------


Attacks on the gaming industry skyrocketed during the first year of the pandemic, with attacks on web applications shooting up 340 percent in 2020, [according to Akamai](https://threatpost.com/attackers-gaming-industry/167183/).


Discord, which is popular for hosting gaming servers, has been grappling with a malware problem for many months. A report from Sophos last summer showed [malware on Discord](https://threatpost.com/discord-malware-researchers/168096/) is up 140 percent over 2020.


Steam has been abused in the past as well. Accounts and in-game payment information was recently targeted by a [trojan called BloodyStealer;](https://threatpost.com/gamers-malware-steam-epic-ea-origin-accounts/175081/) and last summer, a [bug in Steam’s code](https://threatpost.com/valve-bug-unlimited-funds/168710/) let gamers trick the platform’s Smart2Pay system to fill their digital wallets with unlimited funds. It’s also been used as a [malware host](https://threatpost.com/steam-gaming-delivering-malware/166784/) in a campaign called “SteamHide.”


And, fake “Among Us” and Steam offerings [are circulating on](https://threatpost.com/tiktok-gamer-targets-among-us-steam/175546/) TikTok, with the goal of spreading malware.


As cybercriminals continue to prey on gamers with new attacks, Malwarebytes Labs latest report implored players to stay aware of threats, adding the simple, yet effective, advice: “Please don’t just click links that come out of the blue.”


***Want to win back control of the flimsy passwords standing between your network and the next cyberattack? Join Darren James, head of internal IT at Specops, and Roger Grimes, data-driven defense evangelist at KnowBe4, to find out how during a free, LIVE Threatpost event,*** ***[“Password Reset: Claiming Control of Credentials to Stop Attacks,”](https://bit.ly/3bBMX30)*** ***on Wed., Nov. 17 at 2 p.m. ET. Sponsored by Specops.***


***[Register NOW](https://bit.ly/3bBMX30)*** ***for the LIVE event and submit questions ahead of time to Threatpost’s Becky Bracken at [becky.bracken@threatpost.com](mailto:becky.bracken@threatpost.com).***




#### Tags:
[[malware]] [[Malwarebytes]] [[ThreatPost]]
