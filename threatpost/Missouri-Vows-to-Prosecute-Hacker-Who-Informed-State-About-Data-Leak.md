# Missouri Vows to Prosecute ‘Hacker’ Who Informed State About Data Leak
### Missouri Gov. Mike Parson launched a criminal investigation of a reporter who flagged a state website that exposed 100K+ Social-Security numbers for teachers and other state employees.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175501)
+ Date: October 15, 2021  1:44 pm
+ Author: Lisa Vaas


## Article:
![](https://threatpost.com/files/2021/10/screenshot-from-press-conference.bmp)
The St. Louis Post-Dispatch newspaper recently found a huge security blunder: The Missouri educational agency’s site was displaying 100,000+ clearly visible Social-Security numbers for school teachers, administrators and counselors in its HTML source code.


The newspaper verified its findings with a cybersecurity professor and then informed the agency responsible for the leaking site – the Department of Elementary and Secondary Education (DESE) – on Tuesday. On the same day, the DESE took down the affected pages. Then, on Wednesday, having waited to disclose the vulnerability until after the pages came down, the outlet [published its story](https://www.stltoday.com/news/local/education/missouri-teachers-social-security-numbers-at-risk-on-state-agencys-website/article_f3339700-ece0-54a1-9a45-f300321b7c82.html).


The next day, on Thursday morning, a naked emperor shot the messenger, as Missouri Gov. Mike Parson threatened legal action against whoever found the vulnerability and whoever may have helped them.



> 
> Through a multi-step process, an individual took the records of at least three educators, decoded the HTML source code, and viewed the SSN of those specific educators.
> 
> 
> We notified the Cole County prosecutor and the Highway Patrol’s Digital Forensic Unit will investigate. [pic.twitter.com/2hkZNI1wXE](https://t.co/2hkZNI1wXE)
> 
> 
> — Governor Mike Parson (@GovParsonMO) [October 14, 2021](https://twitter.com/GovParsonMO/status/1448697768311132160?ref_src=twsrc%5Etfw)
> 
> 



He called the unnamed journalist a “hacker,” vowed to sic the courts on the individual and said the state would try to recoup incident-response costs that might cost taxpayers “as much as $50 million.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


A Quick Tutorial in How to Become a Source-Code-Sniffing ‘Hacker’
-----------------------------------------------------------------


“Through a multistep process,” Parson gravely said, “an individual took the records of at least three educators, decoded the HTML source code and viewed the Social-Security numbers of those specific educators.”


That surely sounds nefarious to those who aren’t familiar with how the magic of the internet works, but the truth is that HTML source code is only “encoded” as it travels from a website to a browser, which automatically “decodes” the HTML because that’s what browsers do: They interpret HTML instructions.


Jake Williams, co-founder and CTO at incident-response provider BreachQuest, told Threatpost on Friday that the journalist’s means of discovering the flaw “is certainly not hacking in any sense of the word.”


He continued: “It appears that the reporter used a publicly available web application intended to facilitate searching for teacher certifications. When the results were displayed, the reporter simply viewed the source code of the web page and found the social security numbers. While Governor Parson said the reporter ‘decoded the HTML source code’ in reality they simply used the feature built into every web browser since the dawn of the internet.”


Williams explained that because HTTP is stateless, many web applications store their status in hidden form fields so they can be passed from the browser back to the server with every request. “It seems likely that these hidden form fields included the Social-Security number of the teacher,” he suggested.


The Post-Dispatch reported that it had found the Social-Security numbers in the HTML source code of the website’s pages, exposed due to a vulnerability in a web app that allowed the public to search teacher certifications and credentials. No other private information was clearly visible.


That means that it was publicly available to anyone with a web browser who decided to examine the site’s public code.


As Williams suggested, doing so is simple as pie. Every major browser allows you to [view HTML source code](https://www.computerhope.com/issues/ch000746.htm) of any web page by using the browser’s developer tools. For example, in Chrome, to view a page’s source code, choose the three dots in the upper right, select More Tools, then click on Developer Tools, as depicted below.


Even easier is to press Ctrl+U on your keyboard or Opt+Command+U on a Mac keyboard. Presto: A page’s source code is displayed. An example of what source code looks like for those who’ve never scrutinized this easily accessed data is given below:


Verifying What They Saw
-----------------------


The Post-Dispatch reached out to Shaji Khan, a cybersecurity professor at the University of Missouri at St. Louis, to verify what it had found. He confirmed that it was “a serious flaw” and that it was “mind-boggling” to find this type of vulnerability in the DESE web app.


The professor urged the state to audit its apps to ensure that similar vulnerabilities get weeded out. DESE reportedly kicked off an audit on Tuesday that was still ongoing as of Wednesday but hadn’t yet uncovered other instances of the flaw.


At any rate, it’s not the first entity to commit source-code sins. For example, in 2019, data scientist David Stier reported that for months, the source code for Instagram’s website was showing some user profiles that [displayed phone numbers and emails](https://www.cnet.com/tech/services-and-software/instagram-website-leaked-phone-numbers-and-emails-for-months-researcher-says/): data that wasn’t available on public-facing pages.


It’s not clear how long the Social-Security numbers were accessible on DESE’s site, nor if the data was accessed by anyone with ill intent.


An ‘Attempt to Embarrass the State and Sell Headlines’
------------------------------------------------------


Regardless of how easy it reportedly was to get at the sensitive information, the Post-Dispatch journalist who discovered it was denounced as a criminal “hacker,” first in a statement issued by the educational agency and then by the governor.


“Nothing on DESE’s [the Department of Elementary and Secondary Education’s] website gave permission or authorization for this individual to access teacher data,” the governor claimed during his Thursday press briefing, suggesting that the journalist just wanted to “sell headlines.”


“This individual is not a victim,” Parson proclaimed. “They were acting against the state agency to compromise teachers’ personal information in an attempt to embarrass the state and sell headlines for the news outlet. We will not let this crime against Missouri teachers go unpunished. And we refuse to let them be a pawn in the news outlets’ political vendetta.”


Parson added that his administration “is standing up against any and all perpetrators who attempt to steal personal information and harm Missourians. It is unlawful to access encoded data and systems in order to examine other peoples’ personal information.”


The governor notified the Cole County Prosecutor about the matter, along with the Missouri State Highway Patrol’s digital forensic unit, which he said will also be conducting “an investigation of all of those involved.”


Below is the governor’s full press conference.


How About Focusing on the Flaw Instead of Lashing Out?
------------------------------------------------------


Tim Wade, technical director and CTO team at AI cybersecurity company Vectra, said that the brouhaha underscores the need to protect security researchers who operate in the public good. He suggested that a wise path would be to redirect the spleen that’s directed toward bug-finders and to instead focus that energy on “the root causes of why these security failures continue to occur.”


Legally, he just doesn’t see merit in the saber-rattling. “Courts recognize limits to protections from unlawful search when activities occur clearly in a public context,” Wade observed. “It’s hard to imagine that the low technical sophistication of the behaviors described, with a tool as common as a web browser, constitutes anything but the digital equivalent of observations made in a public context.”


Other security practitioners agreed. Williams said that rather than focus on this so-called “hacking,” Parson “should be worried about the security of the state’s applications, particularly those that are available for public use.”


Frankly, the state should be embarrassed to find a flaw like this in 2021, Williams said. But it’s not the first time that “a politician has fired on all cylinders, claiming that accessing publicly available information was hacking,” he noted, referring to a 2017 incident in which then-Georgia Secretary of State Brian Kemp alleged that voter records taken from an open directory on a Kennesaw State web server also constituted “hacking.”


“That hasn’t exactly aged well, and no charges were ever filed,” Williams said via email.


Just Put on Some Pants Already
------------------------------


But hey, it’s all true to form for politicians, as pointed out by John Bambenek, principal threat hunter at digital IT and security operations firm Netenrich. “Throughout human history, emperors have responded to those telling them they were wearing no clothes by lashing out in anger at the audacity of those who’d dare say such a thing,” he told Threatpost.


“Life would be better if they, you know, just put on pants,” Bambenek said. “Government leaders should be thanking people who notify government of problems, not threatening them. I’m sure every actual criminal hacker on the planet noticed this tirade and you can bet they’re adjusting their targeting accordingly.”


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[HTML]] [[Social-Security]] [[Post-Dispatch]] [[cybersecurity]] [[DESE]] [[website]] [[it’s]] [[ThreatPost]]
