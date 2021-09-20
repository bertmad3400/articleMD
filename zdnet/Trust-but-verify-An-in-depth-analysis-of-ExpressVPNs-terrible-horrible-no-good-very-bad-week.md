# Trust, but verify: An in-depth analysis of ExpressVPN's terrible, horrible, no good, very bad week
### In light of ExpressVPN's double-whammy of troubling news, we take a deep dive into the facts, and whether you can feel safe or suspicious about using one of the world's most popular VPNs.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/trust-but-verify-an-in-depth-analysis-of-expressvpns-terrible-horrible-no-good-very-bad-week/)
+ Date: September 20, 2021 -- 13:38 GMT (14:38 BST)
+ Author: David Gewirtz


## Article:
Unknown

ExpressVPN has been all over the news for the past week, and not in a good way. Because we recommend ExpressVPN here at ZDNet as one of the [top VPNs](https://www.zdnet.com/article/best-vpn/) out there, I've gotten a flood of reader questions asking for an objective read on the news. In this article, I'll do my best. 

 Sitrep
-------

Let's start with a [sitrep](https://en.wikipedia.org/wiki/Command_center#Military_and_government) (situation report). There are two key items which are tangentially related. 


The first item is that [Kape Technologies has announced plans to acquire ExpressVPN](https://www.zdnet.com/article/expressvpn-sells-to-kape-technologies-for-936-million/) for $986 million. I do have concerns about this because Kape was once considered a malware provider. I'll talk more about this in a bit. 

The second item is a report in Reuters indicating that ExpressVPN CIO Daniel Gericke is among three men fined $1.6 million by the US Department of Justice for hacking and spying on US citizens on behalf of the government of the UAE (United Arab Emirates).

I'll discuss each of these reports individually, and then share with you some thoughts about how these situations might impact your decision to use (or not use) ExpressVPN. 

 Kape Technologies
------------------

Kape Technologies has had quite a convoluted history. According to [a report in *Forbes*](https://www.forbes.com/sites/thomasbrewster/2015/06/09/from-israel-unit-8200-to-ad-men), a company called Crossrider was formed in 2011 by "billionaire Teddy Sagi, a serial entrepreneur and ex-con who was jailed for insider trading in the 1990s. His biggest money maker to date is gambling software developer Playtech," and Koby Menachemi. 

Menachemi was a developer for [Unit 8200](https://en.wikipedia.org/wiki/Unit_8200), an Israeli signals intelligence unit responsible for hacking and collecting data (think of it as part CIA, part NSA, and part high school, because the unit hires and trains teenagers in hacking and coding skills). 






Crossrider's business was ad injection. Remember back in the day when companies like Yahoo tried to convince you to download their browser extension with their search bar? Crossrider's business was creating tools that allowed them to inject ads into other companies' web pages, sometimes overriding even ads that were paid to run on the sites that were being compromised. 

Ad injection skirted the line between just being scummy and being malware. *Forbes* reported that Symantec's anti-malware identified software based on Crossrider's product as malware, in part because the product effectively stole the ad revenue from the sites its users visited, and in part because it collected whatever data it could find in the process. 

According to [Publift](https://www.publift.com/blog/what-you-need-to-know-about-ad-injection), an ad partnering service founded by ex-Googlers, the ad injection business is still out there. But Google has been fighting it for about five years now, meaning it's not nearly as lucrative a business as it once was. 

According to [a 2018 report](https://en.globes.co.il/en/article-crossrider-renamed-kape-after-switching-to-cybersecurity-1001227178) in the Israeli business daily *Globes*, Kape Technologies was a rebranding effort on the part of then relatively new Crossrider CEO Ido Erlichman. Crossrider's share price had fallen to a low of £0.27 on the London Stock Exchange and the company was seeking a new strategy. 

What better strategy for a company dedicated to siphoning users' data and eyeballs than to branch out into the one area of cybersecurity where users are obsessed with anonymity and information security? 

You can cut the irony with a knife. 

In any case, the newly renamed Kape Technologies set out on an acquisition binge. The company [started buying](https://www.crunchbase.com/acquisition/crossrider-acquires-cyberghost-srl--6d40ffd8) in 2017, [acquiring CyberGhost VPN for about $9 million](https://en.globes.co.il/en/article-crossrider-buys-german-cyber-security-co-cyberghost-1001180764). Next, in 2018, came Mac antivirus company [Intego for $16 million](https://www.calcalistech.com/ctech/articles/0,7340,L-3742992,00.html). A few months later, Kape gobbled up another VPN provider, [ZenMate, for about $5 million](https://www.crunchbase.com/acquisition/crossrider-acquires-zenmate--f07be86a). A year later, in 2019, [Kape spent $95 million for Private Internet Access](https://www.techradar.com/news/cyberghost-owner-buys-pia-for-dollar955m-to-create-vpn-giant), one of the best known VPN providers at the time. 

After a 2020 IPO on the London Stock Exchange ([which raised $115 million](https://en.globes.co.il/en/article-kape-technologies-raises-115m-in-london-offering-1001347631)), and [a year of record earnings](https://www.calcalistech.com/ctech/articles/0,7340,L-3888751,00.html) where the pandemic and [work-from-home cybersecurity concerns](https://www.zdnet.com/article/working-from-home-trend-causes-surge-in-cybersecurity-costs-security-breaches/) drove VPN demand, Kape was riding high. Back in March of this year, the company bought Webselenese for $149 million. This is worthy of further discussion. 

At first glance, it's tough to pin down what Webselenese does. The company describes itself as "an online platform specialising in consumer-focused privacy and security content." What does this mean? According to investment site *The Twenties Trader*, [Webselense owns two very high profile review sites](https://www.thetwentiestrader.com/post/be-wary-of-kapes-webselenese-acquisition), VPNMentor and Wizcase. According to Alexa (Amazon's traffic monitoring service, not Amazon's voice assistant -- I know, it's confusing), [VPNMentor has a rank of 5,807](https://www.alexa.com/siteinfo/vpnmentor.com). Wizcase has a rank of 7,280. 


Are you seeing where this is going? Adware provider pivots to become a provider of VPN services, then that company buys up two of the largest VPN review sites on the internet. Does anyone think those reviews will remain unbiased? [According to site RestorePrivacy.com](https://restoreprivacy.com/vpn-review-websites-owned-by-vpns/) (which itself traffics in VPN reviews), VPN rankings on both VPNMentor and Wizcase changed in Kape Technologies' favor just as soon as Kape bought Webselenese. 

Can you spell "conflict of intererest?" Sure. I knew you could. 

And then, last week, [Kape siphoned up ExpressVPN for $936 million](https://www.zdnet.com/article/expressvpn-sells-to-kape-technologies-for-936-million/), its biggest deal to date. With Kape's somewhat sordid history, you can see the concern. I'll mention one other issue about Kape, and then we'll move on. 

Last year, my CNET colleague Rae Hodge did [an extensive analysis of Kape Technologies](https://www.cnet.com/tech/services-and-software/what-is-kape-technologies-what-you-need-to-know-about-the-parent-company-of-cyberghost-vpn/). At the time, she was looking at Kape as it pertained to its ownership of CyberGhost. But one thing she pointed out should be a concern. She pointed out that even after the change from Crossrider to Kape, "Kape still operated the infamous scareware Reimage -- a potentially unwanted program that positions itself as a computer performance enhancer but which has been known to signal false positives on security threats in order to persuade you to pay for its premium service." She also pointed out that as recently as 2019, "new Crossrider-Kape mutations have been cropping up on the web." 

So, there's that. Now let's get to know Daniel Gericke a little better. 

 ExpressVPN CIO Daniel Gericke
------------------------------

Last week, as a completely separate story from Kape's acquisition of ExpressVPN, [*Reuters* reported](https://www.reuters.com/world/us/american-hacker-mercenaries-face-us-charges-work-uae-2021-09-14/) that, "Three former U.S. intelligence operatives who worked as cyber spies for the United Arab Emirates admitted to violating U.S. hacking laws and prohibitions on selling sensitive military technology." 

They were Marc Baier, Ryan Adams, and...Daniel Gericke. Gericke, as it turns out, is also ExpressVPN's CIO. 

Baier, Adams, and Gericke were not good boys. They were hired guns for a special intelligence unit set up by the United Arab Emirates (UAE) to gather intelligence on journalists, activists, dissidents, and rival governments. According to some [excellent in-depth reporting](https://www.reuters.com/investigates/special-report/usa-spying-raven) by *Reuters*, Raven was a substantial project, using money from Arab royalty to hire at least a dozen former NSA and CIA operatives to hack into networks in the US and other countries on behalf of their clients. 

Remember Project Raven. We'll come back to that in a bit, with even more irony. 

Unfortunately, Gericke doesn't have a profile on LinkedIn. There is a profile for a Daniel Gericke listing his sole position as "IT Director at Professional Corporation," so if that's our Daniel, it's not much to go on. The most we know is in [the 1,563-word statement issued by ExpressVPN regarding Mr. Gericke](https://www.expressvpn.com/blog/daniel-gericke-expressvpn/). ExpressVPN said it hired him in 2019. It did not say whether he was still doing work for Project Raven or the UAE at that time. 


If you're deeply interested in this, the best thing to do is read [ExpressVPN's statement](https://www.expressvpn.com/blog/daniel-gericke-expressvpn/). It's a bit of a marvel. It goes on to say that the company knew Gericke was involved in spy stuff, but did not know about anything illegal, immoral, or fattening. The company explains that it's necessary to hire someone "steeped and seasoned in offense" in order to build the best defenses. Then it goes on to state how it protected its services from corruption from within and have subsequently hardened its services from external attack. 

As of September 17, the company reaffirmed its support of Gericke and did not indicate any plans to terminate him. 

 Edward Snowden and his glass house
-----------------------------------

Y'all remember Edward Snowden? Back in 2013 and 2014, Snowden used up [a lot of my column inches](https://www.google.com/search?q=site:www.zdnet.com+gewirtz+snowden). For those of you doomed to forget history, Edward Joseph Snowden was a former NSA employee and CIA contractor [who stole and then leaked](https://en.wikipedia.org/wiki/Edward_Snowden#Size_and_scope_of_disclosures) [more than a million top secret documents](https://www.bloomberg.com/news/articles/2014-01-09/pentagon-finds-snowden-took-1-7-million-files-rogers-says) from the governments of the United States, Australia, and Great Britain. 

After the leak, he ran from the US to Hong Kong, and then from Hong Kong to Russia, where he received asylum after living in the Sheremetyevo Alexander S. Pushkin International Airport for about 40 days and 40 nights. In 2020, Snowden [applied for and was granted permanent residency in Russia](https://www.theguardian.com/us-news/2020/nov/02/edward-snowden-applies-for-russian-citizenship-for-sake-of-future-son). He then went on to apply for dual Russian-American citizenship in December of that year. 

In his years subsequent to his theft and escape to Russia, Snowden has made quite the name for himself. A movie was based on his exploits. And he makes a living doing remote speaking engagements for willing and credulous audiences. 

So how did Mr. Snowden wind up in our story? As it turns out, he weighed in on ExpressVPN and Daniel Gericke when the news broke last week. On September 15, [he tweeted](https://twitter.com/Snowden/status/1438291654239215619), "If you're an ExpressVPN customer, you shouldn't be." This came out the day after the *Reuters* report on Gericke and ExpressVPN and was picked up by media sources across the internet. 

You've probably heard the phrase, "people who live in glass houses shouldn't throw stones." Well, here's Snowden's glass house. According to [*Reuters*' in-depth report on Project Raven](https://www.reuters.com/investigates/special-report/usa-spying-raven), two months before Snowden's fateful theft of US government top secret information, he was recommended for work at military contractor Booz Allen Hamilton (which then subcontracted him out to the three letter agencies) by Lori Stroud, who herself was later recruited to Project Raven by Marc Baier. Baier worked at NSA Hawaii along with Snowden. Baier was also one of the three men indicted by the Justice Department along with ExpressVPN's Gericke. 

So, as we wade deeper in irony, we have a former NSA operative who stole millions of documents from the US Government and ran to Russia, who is complaining about the employer of a former colleague of a former colleague, both of whom were involved in shady activities, but nothing as vastly criminal as his own actions. 

 What now?
----------

Okay, so now you're up to date. You know about the company that just acquired ExpressVPN and its somewhat shady past and, at the very least unethical [juking of the stats](https://medium.com/@roshanrevankar/juking-the-stats-5926eaf5464) when it comes to VPN reviews. You know about the  background of ExpressVPN's CIO. 

But what of ExpressVPN itself? The key question is, should you use it or skip it? 

 What I use
-----------

One of the most frequently asked questions I get is which VPN service I use. This week, it's been all about whether I'm going to stop using ExpressVPN as my VPN service. 

Here's the hard truth: I don't use a commercial VPN service. I don't like the idea of my data going through any of the VPN players' servers. But I'm a bit of an outlier. I've long run my own bare-metal Linux VPN server network located across a few cloud infrastructure providers. I've been hacking my own Linux kernel mods for years, and I'm just as comfortable spinning up a series of servers that bounce traffic as I am making a cup of coffee in the morning. 

I do test all the VPN services I review, but only for a limited time, and only on dedicated test machines. Any that I have concerns about have been documented in my reviews. So far, at least among the top players, I haven't found anything much worse than a VPN connection indicating that the connection is routing through a VPN. 

But it's important to note that I personally only use a VPN for communication security at airports, hotels, and coffee shops -- which I'm visiting a whole lot less these days. I don't have any need to obfuscate my location in order to illegally route around sports viewing restrictions, or to cheap out and not pay for new episodes of *Star Trek Discovery* or *Picard*. 

I am also not a dissident, or someone running from an abusive relationship. I don't do financial transactions online when away from my home network. As such, I don't need all the services and all the clients offered by many of the VPN service providers I've profiled. 

None of the VPN services I recommend are bad -- I just don't need them in my day-to-day life because I built my own. 

 But what about ExpressVPN?
---------------------------

What about ExpressVPN? Do these revelations change anything? To answer that for yourself, you'll need to ask yourself three questions. 

###  How good is ExpressVPN for my needs?

[When I looked at ExpressVPN](https://www.zdnet.com/article/expressvpn-review/), I called it "an easy-to-use VPN with middle-of-the-road everything." I did find that an ExpressVPN connection routed through Security Firewall Ltd, a firm with a surprisingly high Google fraud rating. ExpressVPN reached out to say that Security Firewall is just one of many companies it leases infrastructure from, and its network is secure. You can read the company's statement in my review.

**Also:**[**ExpressVPN review: A fine VPN service, but is it worth the price?**](https://www.zdnet.com/article/expressvpn-review/) 


Overall, I didn't find that ExpressVPN was the fastest or the cheapest VPN, but it did have great documentation, support for a whole lot of clients, a nice user interface, and was easy to setup. So, from a functional point of view, it's fine. Not great, but generally good enough. 

###  Will the Kape acquisition change things?

Kape has genuinely been going hard after acquiring cybersecurity companies. I'd be comfortable with its pivot (we all did things in the past we regret) if it weren't for the Webselenese acquisition this year. Acquiring those review sites for $149 million just has terrible optics. I reviewed both CyberGhost and Private Internet Access well after their acquisition by Kape, and both products were good. 

**Also:** 

* [CyberGhost VPN review: More than just VPN, an all-in-one security kit](https://www.zdnet.com/article/cyberghost-vpn-review-more-than-just-vpn-an-all-in-one-security-kit/)
* [Private Internet Access review: A cheap, powerful VPN](https://www.zdnet.com/article/private-internet-access-review/)

Kape has had a past that's at odds with the mission of a VPN provider. Kape, back when it was Crossrider, liked to hoover up users' data, probably to sell to advertisers. Will it continue to do so? I don't know, but it'd be really foolish if it did. The VPN market is a vastly more profitable business than ad informatics, and Kape's VPN brands are now its golden geese. It'd be insane to risk those cash cows (I know, the mixed metaphor hurts), in favor of selling out its users' data. 

###  What about keeping Gericke on staff?

The [company's blog post](https://www.expressvpn.com/blog/daniel-gericke-expressvpn/) went to great lengths to show how it is restricting Gericke's access so he won't do *baaaad* things. But I agree with the premise that you need some offensive warriors when you're at war. I'm not sure Gericke should stay as the company's CIO with any infrastructure responsibility, but keeping a stable of folks who know and understand the enemy is important in this business. 

 So what's the bottom line?
---------------------------

One thing I'm asked regularly is whether or not ExpressVPN (or any other VPN) is going to share information with the FBI (or name your favorite intelligence agency). The prevailing wisdom is that VPN vendors located outside the [various "Eyes" intelligence sharing treaties](https://en.wikipedia.org/wiki/UKUSA_Agreement) are somehow safer for those hiding information from government access. This is generally not true. As I discussed in [my analysis of NordVPN](https://www.zdnet.com/article/meet-nordsec-the-company-behind-nordvpn-wants-to-be-your-one-stop-privacy-suite/), most VPN providers have enough of a footprint in [MLAT treaty](https://2009-2017.state.gov/j/inl/rls/nrcrpt/2014/vol2/222469.htm) countries that if a three-letter agency wants your information, it'll get it. 

So, unless you're a very serious dissident (or, I guess, a criminal) on the run from the government, the whole issue of jurisdiction is merely VPN theatre for the benefit of good marketing hype. And if you are relying on a VPN service to protect your life and freedom, why are you relying on something you read online for your truth? I just showed you that the biggest VPN review sites are owned by a VPN conglomerate. You need to do some very serious investigation and testing on your own, if you want to be truly safe. 

If you're currently using ExpressVPN for general-purpose safe computing (like checking your mail at the local coffee shop) and you like it, I wouldn't say you should give it up. If you're relying on any of the Kape brands for a life and death situation, I'd say it's probably not worth the risk. 

If you're shopping for a VPN, read all the reviews and try them out. Most give you thirty days, so see how they actually work for you. Again, I wouldn't necessarily dismiss ExpressVPN out of hand because of these reports, but it's up to you to gauge your risk level. 

In the mid-1980s, US president Ronald Wilson Reagan was preparing for a summit with Soviet president Mikhail Sergeyevich Gorbachev and wanted to bond with his Soviet counterpart. When Reagan spoke with Russian history scholar Susanne Massie, an American, she introduced him to the phrase *doveryai, no proveryai*. In English, that's [trust, but verify](https://en.wikipedia.org/wiki/Trust,_but_verify). Reagan apparently liked the phrase so much, [he overused it](https://www.rbth.com/lifestyle/330521-reagan-trust-but-verify-chernobyl), much to the annoyance of Gorbachev. 

In any case, that's how I recommend approaching ExpressVPN: trust, but verify. We'll keep an eye on how the company behaves. Does Kape do anything else that indicates their moral compass is askew? Does Gericke's access become more limited or does he leave the company? Does data secured by ExpressVPN turn out to be less secure? 

I don't believe we need to pillory ExpressVPN just yet. All the bad news is tangential to its operations. But I'd advise the company to walk very carefully, to hold its new masters at Kape accountable, and to both know where the line is and stay firmly on the angels' side of that line. 



---

*You can follow my day-to-day project updates on social media. Be sure to follow me on Twitter at [@DavidGewirtz](https://twitter.com/davidgewirtz), on Facebook at [Facebook.com/DavidGewirtz](https://www.facebook.com/davidgewirtz), on Instagram at [Instagram.com/DavidGewirtz](https://www.instagram.com/DavidGewirtz/), and on YouTube at [YouTube.com/DavidGewirtzTV](https://www.youtube.com/user/DavidGewirtzTV).* 





#### Tags:
[[VPN]] [[ExpressVPN]] [[Kape]] [[Gericke]] [[Snowden]] [[Crossrider]] [[million.]] [[week,]] [[Reuters]] [[Kape,]] [[ZDNet]]
