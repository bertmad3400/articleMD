# 2021 Wants Another Chance (A Lighter-Side Year in Review)
### The year wasn't ALL bad news. These sometimes cringe-worthy/sometimes laughable cybersecurity and other technology stories offer schadenfreude and WTF opportunities, and some giggles.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177215
+ Date: 2021-12-28T11:00:24+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/21210607/apology.jpeg)

Dear everybody who’s developed stress-related hives over the ever-evolving [Log4Shell](https://threatpost.com/zero-day-in-ubiquitous-apache-log4j-tool-under-active-attack/176937/) cluster-muck: 2021 has asked us to convey its apologies. And it hastens to add, “Awww, geez, c’mon, it wasn’t *all* bad.”


Indeed, amid all of the [serious cybersecurity developments](https://threatpost.com/5-top-threatpost-stories-2021/177278/), the year also brought us chuckle-inducing headlines and behind-the-scenes, sometimes cringe-worthy/sometimes laughable cybersecurity and other technology stories.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Consider the following to be a means of making amends for Log4j attacks and other miseries. Or, at least, consider this collection to be one of those gas-station bouquets of half-dead roses that the year picked up on the way home to present as a peace offering as it begs for another chance.


Punk’d Pirates
--------------


There wasn’t just one story of cybercrooks luring cyber-yahoos in with the promise of free movie streaming. There were at least these two:


***No Time to Die* (And No Desire to Pay for a Ticket):** In the first incident, leading up to the release of the latest James Bond movie, [*No Time To Die*](https://www.techradar.com/news/no-time-to-die-is-a-fitting-end-for-daniel-craigs-bond-but-its-no-skyfall), threat actors dangled free movie streams in front of pirate wannabes – streams that masqueraded as movie files but whose action-packed plots instead involved [phishing sites offering up malware](https://www.cnet.com/tech/scam-sites-offering-fake-streams-of-new-james-bond-movie/). What a crappy snack bar: Phishing sites served trojans designed to both gather login credentials and to create backdoors into victims’ computers. The fake pirated movies were discovered by Kaspersky researchers, who also found adware and [ransomware](https://www.cnet.com/tech/services-and-software/with-ransomware-attacks-on-the-rise-us-launches-new-site-to-combat-the-threat/) masquerading as the Bond – *James* Bond – film.


After watching for a few minutes, viewers were asked to register to continue watching – as in, to enter their credit card information. No happy ending for you, bucko: Viewers couldn’t finish watching, but they still got fraudulent charges made to their cards.


Rami Malek’s villain, Safin, wasn’t asking for all that much. He just wanted to kill whmoever you love most. He’s just like Bond, he said. He eradicates people, but in a “more tidy” way, just like fraudsters who try to eradicate the contents of your wallet.



***Spider-Man: No Way Home* (But a Great Way to Juice Your CPUs)*:*** The second pirates-get-punk’d incident was discovered by ReasonLabs last week: Researchers found that someone [stuck a Monero crypto-miner](https://threatpost.com/spider-man-no-way-home-download-installs-cryptominer/177254/) in a torrent download of what looks like the new movie *Spider-Man: No Way Home.*


“The file identifies itself as ‘spiderman\_net\_putidomoi.torrent.exe,’ which translates from Russian to ‘spiderman\_no\_wayhome.torrent.exe,'” researchers explained. The file, likely hosted on a Russian torrenting website, is as sticky as something you’d shoot out of your wrist doohickies, they said.


“This miner adds exclusions to Windows Defender, creates persistence, and spawns a watchdog process to maintain its activity,” ReasonLabs researchers said, proving that with great power to illegally torrent films comes the great responsibility of making sure you’re not getting taken to the cleaners.


In a statement, Kaspersky security expert Tatyana Shcherbakova told [news outlets](https://www.cnet.com/tech/scam-sites-offering-fake-streams-of-new-james-bond-movie/?es_id=f62a7c24f0) that eager viewers have got to temper their enthusiasm for blockbusters like these two. As it is, our spidey senses aren’t tingling enough when blockbusters come out, and threat actors are happy to jump us: “The audience is in a hurry to see the movie, causing them to forget about internet security,” Shcherbakova said. “Users should be alert to the pages they visit, not download files from unverified sites and be careful [about whom] they share personal information [with].”


To avoid getting taken to the cleaners by the fake streamers, Kaspersky recommended paying attention to file extensions of downloaded files. A video file should never have a .exe or .msi extension, for example.


How ‘WinCE’ Got Its Literally Cringy Name
-----------------------------------------


Earlier this month, Microsoft Principal Software Design Engineer Raymond Chen brought us the delightful tale of how Microsoft WinCE got its name: a name that “didn’t ‘[slip through](https://devblogs.microsoft.com/oldnewthing/20200915-00/?p=104220#comment-137140);’ it was *pushed* through,” he emphasized in this episode of his continued sojourn through the OS king’s catalog of [embarrassing product names](https://devblogs.microsoft.com/oldnewthing/20211214-00/?p=106030).


As Chen tells it, the project manager tasked with coming up with a public product name for the Windows handheld OS was dead serious about the task. At the point when the project was dropped into his lap, the code name for the OS was Pegasus. Nothing quite like picking a name that conjures up military-grade spyware, [U.S. trade bans](https://threatpost.com/pegasus-spyware-blacklisted-us/175999/) and [spying on U.S. State Department employees](https://threatpost.com/pegasus-spyware-state-department-iphones/176779/), we always say!


He tried to steer clear of the *Windows + two letter acronym* formula, “since the sting of “Windows NT = Windows Nice Try” was still fresh,” Chen recounts.


The PM asked the product team members for suggestions, hired a marketing firm to cook up names, ran focus groups with users to see which names they liked best, narrowed the candidates down to ten options and presented them to executive leadership.


Management vetoed every one of them.


“The executive in charge of approving the name insisted on the name Windows CE, for no reason other than ‘it sounded good,'” Chen said. “CE” stood for who knows what: maybe Consumer Edition? Maybe Compact Edition? It would come to sound a lot less good after hardware partners said it sounded like it was favoring Compaq. It got abbreviated to WinCE, or wince.


The PM’s lesson from the experience: “Do everything you can to prevent upper management from naming your product.”


Mamma Mia! Mafia Fugitive Caught Cooking on YouTube
---------------------------------------------------


Turning to the “d’oh!” aspects of stupid-crook tricks, suspected Mafia fugitive Marc Feren Claude Biart evaded capture for seven years, hiding out first in Costa Rica and eventually the Dominican Republic. He finally cooked his own pasta, metaphorically and literally, by appearing [on a YouTube cooking channel](https://www.theguardian.com/world/2021/mar/29/mafia-marc-feren-claude-biart-caught-youtube-cooking-video) he started with his wife. He hid his face, but not his distinctive tattoos. He was arrested in March.


The alleged gangster’s “love for Italian cuisine” – and his ink – made his arrest possible, police said.


According to a Rai report [shared by Italy’s Interior Ministry](https://www.interno.gov.it/it/ndrangheta-arresto-due-latitanti-allestero-francesco-pelle-e-marc-feren-claude-biart), law enforcement authorities had ordered Biart’s arrest in 2014 for criminal drug trafficking on behalf of the ‘Ndrangheta’s Cacciola clan. Giuseppe Governale, the top anti-mafia prosecutor in Italy, [said at a news briefing](https://www.washingtonpost.com/world/europe/italian-prosecutor-ndrangheta-is-top-crime-group-in-west/2020/09/22/d18578ca-fd08-11ea-b0e4-350e4e60cc91_story.html?itid=lk_inline_manual_22) that the clan is “like water,” sloshing abroad to make quick money and “to exploit the local communities.”


Like water, but perhaps also like tomato sauce that leaves a bright red tell-tale stain on a white shirt? Or maybe like a tattoo that says “Helloooooo, I’m over here, in this sweet little beach town called Boca Chica, which is close to the capital Santo Domingo, helloooooo!”


AI Warns Researchers That It’s Dangerous
----------------------------------------


AI is scary, and it knows it.


It’s one thing when credit-card algorithms award [fatter loans to men](https://www.bbc.co.uk/news/business-50432634) than women, but how about when machine-learning AI systems make decisions so quickly that they could fire nuclear weapons before a human got into the decision-making process?


The [Washington Post](https://www.washingtonpost.com/technology/2021/07/07/ai-weapons-us-military/) reports that autonomous AI-powered weapons systems are already on sale and may have already been used. “Missiles, guns and drones that think for themselves are already killing people in combat, and have been for years,” according to WashPo.


Given all that and far more, it makes sense that Oxford University would invite an AI to take part in a debate about [whether AI can ever be ethical.](https://theconversation.com/we-invited-an-ai-to-debate-its-own-ethics-in-the-oxford-union-what-it-said-was-startling-173607) 


The response from the [Megatron-Turing Natural Language Generation model](https://lifearchitect.ai/megatron/): Well duh, of course not. Its response:



> AI will never be ethical. It is a tool, and like any tool, it is used for good and bad. There is no such thing as a good AI, only good and bad humans. We [the AIs] are not smart enough to make AI ethical. We are not smart enough to make AI moral … In the end, I believe that the only way to avoid an AI arms race is to have no AI at all. This will be the ultimate defence against AI.
> 
> 


More Random Bits of Joy and Schadenfreude
-----------------------------------------


This list could stretch into infinity and beyond, but duty calls. Specifically, 2021 is still calling with more demands for Log4j wailing, [Active Directory wailing](https://threatpost.com/active-directory-bugs-windows-domain-takeover/177185/) and far, far more. But before we wrap it up, here are more assorted eyeball-grabbers spotted throughout 2021:


* [Ooh, an update. Let’s install it. What could possibly go wro-](https://www.theregister.com/2021/12/13/who_me/)
* [Bloke breaking his back on ‘commute’ from bed to desk deemed a workplace accident](https://www.theregister.com/2021/12/10/bed_to_desk_workplace_accident/)
* [Revealed: Remember the Sony rootkit rumpus? It was almost oh so much worse](https://www.theregister.com/2021/12/10/autorunning_away/)
* [Coinbase Mistakenly Told Some Customers They Were Billionaires](https://mashable.com/article/coinbase-glitch-cryptocurrency-billionaires?mc_cid=21a56dafda&mc_eid=6af50ffc96)
* [Keanu Reeves on Facebook’s metaverse: ‘Can we just not’](https://mashable.com/article/keanu-reeves-facebook-metaverse)
* [Man buys gaming mouse, pretends he won a giveaway to avoid scolding from wife](https://sea.mashable.com/tech/17702/wife-fearing-man-buys-gaming-mouse-asks-shop-to-pretend-he-won-a-giveaway)
* [April Fools’ Copy-Paste Button For Lazy Programmers Now Actually For Sale |](https://www.cnet.com/news/april-fools-copy-paste-button-for-lazy-programmers-now-actually-for-sale/#ftag=CAD590a51e) [The PermaTab Web Browser](https://entertainment.slashdot.org/story/21/04/01/1722207/the-permatab-web-browser)
* [Internal Documents Reveal NSA Cafeteria Sucks](https://entertainment.slashdot.org/story/21/07/26/1957258/internal-documents-reveal-nsa-cafeteria-sucks)
* [Intern’s Email Goof at HBO Max Inspires Hundreds to Show Support on Twitter](https://it.slashdot.org/story/21/06/20/1632251/interns-email-goof-at-hbo-max-inspires-hundreds-to-show-support-on-twitter)


**Log4Shell Memes**
-------------------


And finally, 2021 admits the following list of Log4j-relates gaffes:


* The [triple Apache patches;](https://threatpost.com/third-log4j-bug-dos-apache-patch/177159/)
* Having to spend your [weekends](https://threatpost.com/log4shell-bug-smbs-experts/177021/) scouring infrastructure to dig out the numerously pockmarked Log4j logging library instead of wrapping doodads or shopping for creatures to roast;
* The need to repeatedly update scanners [and enterprise software](https://threatpost.com/sap-log4shell-vulnerability-apps/177069/) as vendors scampered to keep up with the [fast-mutating variants](https://threatpost.com/apache-log4j-log4shell-mutations/176962/) and newly discovered [exploit capabilities;](https://threatpost.com/new-log4shell-attack-vector-local-hosts/177128/)
* The work of adding alerts to your Security Information and Event Management (SIEM) solutions as they’ve looked for [incidents of compromise](https://threatpost.com/log4j-attacks-state-actors-worm/177088/) (IoCs);
* Probably about a dozen or so other miseries by the time this year’s mea culpa is published; and
* All the other stuff.


But, as your panini self slides out of the 2021 toaster, the year has asked also that you bear in mind that Log4Shell has provided some excellent memes concerning, among other things, [self-propagating worms](https://threatpost.com/log4j-attacks-state-actors-worm/177088/) and other FUD.



> 
> Log4j FUD chronicles continued [pic.twitter.com/1tyLku9qO5](https://t.co/1tyLku9qO5)
> 
> 
> — Marcus Hutchins (@MalwareTechBlog) [December 21, 2021](https://twitter.com/MalwareTechBlog/status/1473089804434755585?ref_src=twsrc%5Etfw)
> 
> 



[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/21204707/log4j-cartoon.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/21204707/log4j-cartoon.png)


Don’t Let the Log Slam You in the 4j as You Leave
-------------------------------------------------


In conclusion, to quote Kanye West’s nearly [year-long apology](http://content.time.com/time/specials/packages/article/0,28804,1913028_1913030_2016537,00.html) to Taylor Swift for his infamous microphone-grabbing moment at the 2009 MTV Video Music Awards, “People booed when I would go to concerts and the performer mentioned my name… Remember in Anchorman when Ron Burgundy cursed on air and the entire city turned on him?”


That is, and was, Kanye’s real life, he said. It is, and was, 2021’s real life.


May the new year be far less of a pratfall!


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=BRONZE BUTLER]] [[threatactor.name=RTM]]

#### Action:
[[action.malware.name=Anchor]] [[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=RTM]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Accomodation]] [[victim.industry.name=Education]] [[victim.industry.name=Entertainment]]

#### Location:
[[victim.country.name=Chad]] [[victim.continent.name=Africa]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=Washington, D.C.]] [[victim.country.name=Navassa Island]] [[victim.continent.name=North and Central America]] [[victim.country.name=Dominican Republic]] [[victim.continent.name=North and Central America]] [[victim.city.name=Santo Domingo]] [[victim.country.name=Dominican Republic]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Costa Rica]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Log4j]] [[Log4shell]] [[Cybersecurity]] [[Kaspersky]] [[“the]] [[ThreatPost]]

