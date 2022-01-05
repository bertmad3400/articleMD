# Uber Bug, Ignored for Years, Casts Doubt on Official Uber Emails
### A simple-to-exploit bug that allows bad actors to send emails from Uber's official system — skating past email security — went unaddressed despite multiple flagging by researchers.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177395
+ Date: 2022-01-05T20:49:37+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/05154612/uber.jpg)

A security vulnerability that would allow malicious attackers to send email from Uber’s network appears to be closed – but users could have been swindled already. The easy-to-find bug has been hanging around for years, ready to take Uber’s customers for a ride of a very different sort.


According to Seekurity security researcher and bug-hunter Seif Elsallamy, the HTML-injection issue made it possible to tap into an internet-facing internal Uber API endpoint in order to send out email directly from Uber’s email system (the company uses the SendGrid platform); since the emails would be coming from an authentic sender, they wouldn’t trigger normal email security filters [like DMARC](https://threatpost.com/dmarc-adoption-spikes-higher-ed-remains-behind/157413/) or DKIM.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Obviously, the bug opened a gaping opportunity for cyberattackers to send out social-engineering emails to the ride-sharing giant’s nearly 100 million users – perhaps a message asking them to “verify” their account info or “update” their credit-card information.


Elsallamy forwarded a [proof-of-concept example](https://www.bleepingcomputer.com/news/security/uber-ignores-vulnerability-that-lets-you-send-any-email-from-ubercom/) of a possible attack email to BleepingComputer:


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/05153451/Uber-email.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/05153451/Uber-email.png)The danger seems particularly pertinent given that Uber suffered a data breach in 2016 [that involved](https://threatpost.com/uber-reveals-breach-of-57-million-users-admits-to-covering-up-incident/128969/) the email addresses of 57 million of its users, the researcher pointed out:



> 
> heck this days with triage teams, they don't understand their own policies [@Uber](https://twitter.com/Uber?ref_src=twsrc%5Etfw) [@Uber\_Support](https://twitter.com/Uber_Support?ref_src=twsrc%5Etfw) [@Hacker0x01](https://twitter.com/Hacker0x01?ref_src=twsrc%5Etfw) [pic.twitter.com/kCQqwR3M3b](https://t.co/kCQqwR3M3b)
> 
> 
> — SAFE 😵 (@0x21SAFE) [December 31, 2021](https://twitter.com/0x21SAFE/status/1476991015395471364?ref_src=twsrc%5Etfw)
> 
> 



He also submitted a bug report via HackerOne to Uber, but the issue was rejected because the triage team mistakenly thought exploitation involved the social engineering of Uber employees:



> 
> Hi [@Uber](https://twitter.com/Uber?ref_src=twsrc%5Etfw) [@Uber\_Support](https://twitter.com/Uber_Support?ref_src=twsrc%5Etfw) bring your calc and tell me what would be the result if this vulnerability has been used with the 57 million email address that has been leaked from the last data breach?  
> If you know the result then tell your employees in the bug bounty triage team. [pic.twitter.com/f9yKIoCJ6O](https://t.co/f9yKIoCJ6O)
> 
> 
> — SAFE 😵 (@0x21SAFE) [December 31, 2021](https://twitter.com/0x21SAFE/status/1477003988792926210?ref_src=twsrc%5Etfw)
> 
> 



 


Making matters worse, he wasn’t the first to report it and be rebuffed; at least two other researchers filed the same issue, with the same result – one [as long ago as 2015](https://twitter.com/ShivaSMaharaj/status/1477670787792445444). That’s a lot of time for possible exploitation to have occurred.


“I don’t have evidence that this bug has been exploited in the wild, but since the report has been duplicated, that means at least one researcher has reported it before me,” Elsallamy told Threatpost. “So, it looks like that it is an easy-to-spot issue [and] I hope that it has not been exploited in the wild. The exploitation was not difficult, it only requires basic HTML and CSS knowledge.”



> 
> i reported this issue on [@Hacker0x01](https://twitter.com/Hacker0x01?ref_src=twsrc%5Etfw) last year and triager closed it as informative xD [pic.twitter.com/29yxgTV287](https://t.co/29yxgTV287)
> 
> 
> — ${jndi:ldap://mainteemoforfun} (@wld\_basha) [January 2, 2022](https://twitter.com/wld_basha/status/1477661440131710978?ref_src=twsrc%5Etfw)
> 
> 



“The researchers and Uber’s employees are just doing their job, and I understand that Uber receives a lot of false reports,” Elsallamy told Threatpost. “But they have at least to spend five minutes in the report that had taken me days to prepare. Uber’s customers are who will pay for our faults in the end.”


He noted that a fix would be simple: “The issue is not difficult to fix, I think it will be only one or two lines of code,” he said. “They should sanitize the users’ input through security encoding library, so any HTML appears as a normal text.”


Since the story was reported earlier this week, it appears that Uber has fixed the vulnerability – “because I am unable to reproduce the issue anymore,” Elsallamy said. However, because it’s unknown whether the vulnerability has been exploited in the years that it existed, customers who gave up personal information in response to an official Uber email should take action to change their passwords immediately.


Additionally, “I advise Uber customers to use unique passwords, use credit cards with a limited amount of money available online if they don’t want to hold cash, and to use two-factor authentication whenever possible to limit the damage if any of their data has been compromised,” he said.


Uber did not immediately return a request to comment on this story.


***Password******Reset: [On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):*** *Fortify 2022 with a password-security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the new password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken.****[Register & stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)****– sponsored by Specops Software.*


 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Uber]] [[Elsallamy]] [[Threatpost]] [[ThreatPost]]
#### urls
ldap://mainteemoforfun}

