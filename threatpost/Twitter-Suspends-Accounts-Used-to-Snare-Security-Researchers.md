# Twitter Suspends Accounts Used to Snare Security Researchers
### The accounts were used to catfish security researchers into downloading malware in a long-running cyber-espionage campaign attributed to North Korea.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175524)
+ Date: October 18, 2021  12:23 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/18120437/catfish-e1634573090547.jpg)
Twitter has shuttered two accounts – @lagal1990 and @shiftrows13 – specifically used to trick security researchers into downloading malware in a long-running cyber-espionage campaign attributed to North Korea.


The campaign was [first discovered](https://blog.google/threat-analysis-group/new-campaign-targeting-security-researchers/) by the Google Threat Analysis Group (TAG) in January and is ongoing.


On Friday, Google TAG analyst Adam Weidermann confirmed that Twitter suspended the accounts as part of the operation. This is the second time that Twitter has taken action against accounts linked to the Democratic People’s Republic of Korea (DPRK), having suspended another account connected to the espionage campaign [in August](https://twitter.com/digivector/status/1449036246446010369).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“We (TAG) confirmed these are directly related to the cluster of accounts we blogged about earlier this year,” Weidermann said. “In the case of @lagal1990, they renamed a GitHub account previously owned by another of their Twitter profiles that was shutdown in Aug, @mavillon1.”



> 
> We (TAG) confirmed these are directly related to the cluster of accounts we blogged about earlier this year. In the case of lagal1990, they renamed a github account previously owned by another of their twitter profiles that was shutdown in Aug, mavillon1 [pic.twitter.com/FXQ0w57tyE](https://t.co/FXQ0w57tyE)
> 
> 
> — Adam (@digivector) [October 15, 2021](https://twitter.com/digivector/status/1449036246446010369?ref_src=twsrc%5Etfw)
> 
> 



The Sweet Smell of Bugs and Bug-Hunting
---------------------------------------


As Weidermann detailed in his [January analysis](https://blog.google/threat-analysis-group/new-campaign-targeting-security-researchers/), the threat actors set up a “research” blog and used the Twitter profiles to disseminate links to it in order to pull in potential targets. They also used the accounts to post videos of purported exploits and to amplify and retweet posts from other accounts that they control.


The ongoing [campaign targets security researchers](https://threatpost.com/north-korea-security-researchers-0-day/163333/) using lures near and dear to their hearts: Bugs and research. Weidermann explained that both of the Twitter accounts had posed as security researchers, “leaning on the hype of 0 days to gain followers and build credibility.”


Google TAG, which traced the actors behind the campaign to a government entity based in North Korea, has also identified what analysts call a “novel” social-engineering tactic that the threat actors are using to target specific security researchers: Namely, collaboration.


“After establishing initial communications, the actors would ask the targeted researcher if they wanted to collaborate on vulnerability research together, and then provide the researcher with a Visual Studio Project,” Weidermann explained.


The project is poisoned, however: “Within the Visual Studio Project would be source code for exploiting the vulnerability, as well as an additional DLL that would be executed through Visual Studio Build Events,” Weidermann continued. “The DLL is custom malware that would immediately begin communicating with actor-controlled [command-and-control, or C2] domains.”


Google TAG provided the screen capture below, which shows an example of the VS Build Event.


In January, several unsuspecting researchers who fell for it and agreed to collaborate described what happened next. Below is one example:



The threat actors appear to be credible researchers in their own right, having posted videos of exploits they’ve worked on, including faking the success of a working exploit for what was, as of January, an existing and recently patched [Windows Defender vulnerability](https://threatpost.com/critical-microsoft-defender-bug-exploited/162992/), [CVE-2021-1647](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-1647), on YouTube.


The vulnerability received notoriety as one that was exploited for three months and leveraged by hackers as part of the massive [SolarWinds attack](https://threatpost.com/solarwinds-hack-linked-turla-apt/162918/).


“In the video, they purported to show a successful working exploit that spawns a cmd.exe shell, but a careful review of the video shows the exploit is fake,” Weidermann explained at the time.


Besides social engineering, the actors running the campaign also managed to compromise researchers who visited the purported research blog. “In each of these cases, the researchers have followed a link on Twitter to a write-up hosted on blog.br0vvnn[.]io, and shortly thereafter, a malicious service was installed on the researcher’s system and an in-memory backdoor would begin beaconing to an actor-owned command and control server,” according to the January writeup.


Attacks Worked Against Fully Patched, Up-to-Date Systems
--------------------------------------------------------


The security researchers who’ve been victimized weren’t running pockmarked systems. Rather, “at the time of these visits, the victim systems were running fully patched and up-to-date Windows 10 and Chrome browser versions,” Weidermann said in January.


That means that the threat actors were using zero days.


After Google TAG initially uncovered the campaign in January, South Korean [security researchers identified](https://enki.co.kr/blog/2021/02/04/ie_0day.html) that the actors were exploiting an Internet Explorer zero day: specifically, what researchers from ENKI said was a [double-free](https://cwe.mitre.org/data/definitions/415.html) bug that occurred in the attribute value release part of the DOM object.


This type of bug enables a malicious website or malicious ad to trigger an exploit for the IE zero-day bug, opening the door for data theft and code execution. In February, 0patch analysts gave details about [where the bug exists](https://threatpost.com/exploit-details-unpatched-microsoft-bug/164083/) and how it could be triggered in real-world attacks – notably, by just visiting a website.


Fake Security Company
---------------------


On March 17, Google TAG saw the same threat actors set up a new site, with associated social-media profiles, for a fake, Turkey-based security company called “SecuriElite” that was offering pen tests, software security assessments and exploits.


“Like previous websites we’ve seen set up by this actor, this website has a link to their PGP public key at the bottom of the page. In January, targeted researchers reported that the PGP key hosted on the attacker’s blog acted as the lure to visit the site where a browser exploit was waiting to be triggered,” Weidermann said in a [March 31 update](https://blog.google/threat-analysis-group/update-campaign-targeting-security-researchers/).


As of January, Google TAG had only seen the threat actors going after Windows campaigns. Besides Twitter, they used a variety of other platforms – including LinkedIn, Telegram, Discord, Keybase and email – to reach out to potential targets in the security research community.


According to [The Record](https://therecord.media/twitter-suspends-two-accounts-used-by-dprk-hackers-to-catfish-security-researchers/), neither of the two most recently closed accounts in the campaign – @lagal1990 and @shiftrows13 – had more than 1,000 followers. Google TAG hasn’t yet published analysis to indicate whether the accounts had started to reach out to researchers before they were closed or whether they were still building up their reputations.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Weidermann]] [[Google]] [[January,]] [[(TAG)]] [[“In]] [[Windows]] [[ThreatPost]]
