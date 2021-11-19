# 6M Sky Routers Left Exposed to Attack for Nearly 1.5 Years
### Pen Test Partners didn’t disclose the vulnerability after 90 days because it knew ISPs were struggling with a pandemic-increased network load as work from home became the new norm. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176483)
+ Date: November 19, 2021  12:39 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/19123418/work_from_home-e1637343268627.jpg)
Sky, a U.K. broadband provider, left about 6 million customers’ underbellies exposed to attackers who could remotely sink their fangs into their home networks: a nice, soft attack surface left that way for nearly 18 months as the company tried to fix a DNS rebinding vulnerability in customers’ routers. 


Pen Test Partners reported the problem to Sky Broadband – a broadband service offered by Sky UK in the United Kingdom – on May 11, 2020 … and then chased Sky for a repeatedly postponed update, the security firm said in [a post](https://www.pentestpartners.com/security-blog/skyfail-6-million-routers-left-exposed/). 


The flaw could have affected customers who hadn’t changed the default admin password on their routers. As well, non-default credentials could have been [brute-forced](https://threatpost.com/kubernetes-brute-force-attacks-russia-apt28/167518/), according to Pen Test Partners. The vulnerability has now been fixed. 


These are the affected model numbers:


While the last two router models were also affected by the weakness, they come with a random admin password, making them tougher to attack but also leaving them prey to brute-forcing attacks. The BBC reports that another 1 percent of routers that Sky gives out aren’t made by the company itself, though customers who own such routers can ask for a free replacement. 


DNS Rebinding Vulnerability Explained
-------------------------------------


DNS rebinding is a technique that turns a victim’s browser into a proxy for attacking private networks. We’ve seen it used before, and at an even greater scale than this SkyFlop: It was used in a two-step proof-of-concept exploit researchers demonstrated in [January 2020](https://threatpost.com/cable-haunt-remote-code-execution/151756/), gaining remote access to a compromised spectrum analyzer. 


Multiple cable modems used by ISPs to provide broadband into homes were found to have the critical vulnerability in their underlying reference architecture – a vulnerability that would allow an attacker to get full remote control of the device. The footprint for the affected devices numbered in the hundreds of millions worldwide.


Pen Test Partners explained that the DNS rebinding technique allows an attacker to bypass the [“Same-origin” policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy): a defense in web browsers that permits scripts contained in a first web page to access data in a second web page, but only if both web pages have the same origin, thereby preventing web applications from interacting with different domains without the user’s consent.


The exploit, which would have allowed an attacker to reconfigure a victim’s home router, could have been triggered simply by directing a user, via a [phishing](https://threatpost.com/tools-defending-phishing-attacks/176463/) attack, to a malicious link. From there, the threat actor could “take over someone’s online life,” stealing passwords for banking and other sensitive sites, Pen Test Partner’s Ken Munro told BBC News.


The security firm posted a [proof-of-concept](https://www.youtube.com/watch?v=M7liKMFw8Uk&t=8s) video on Friday. 


Pen Test Partners hasn’t found evidence that the vulnerability has been exploited in the wild. 


Why the Foot Dragging?
----------------------


Sky didn’t immediately respond to Threatpost’s queries, but the company told [the BBC](https://www.bbc.com/news/technology-59332840) that updating so many routers took time and that it takes the safety and security of its customers “very seriously.”


The BBC quoted a Sky spokesperson: “After being alerted to the risk, we began work on finding a remedy for the problem and we can confirm that a fix has been delivered to all Sky-manufactured products.”


As for why Pen Test Partners didn’t disclose its findings for so long, the firm explained that the lag, at least initially, seemed to make sense, given work slowdowns caused by the Coronavirus, followed by a Christmas change freeze, followed next by a series of deadlines missed without explanation. Finally, in August, Pen Test asked the BBC to get in touch with Sky. On Oct. 22, Sky told the security firm that 99 percent of the vulnerable routers had been fixed. 


Pen Test Partners said they didn’t disclose the vulnerability after 90 days because “ISPs were dealing with challenges from vastly increased network loading as working from home became the new norm. We didn’t want to do anything to limit the ability of people to work from home.”


Munro told BBC News that the foot-dragging was “baffling:” “While the coronavirus pandemic put many internet service providers under pressure, as people moved to working from home, taking well over a year to fix an easily exploited security flaw simply isn’t acceptable,” he was quoted as saying.


The ‘Inexcusable’ Problem of Default Passwords
----------------------------------------------


The fact that so many routers are being shipped with default passwords exposed to the internet is “inexcusable in 2021,” John Bambenek, principal threat hunter at security firm Netenrich, told Threatpost via email on Friday.


“This isn’t a vulnerability or security flaw, it’s gross negligence and we should call it exactly that,” he wrote. “Knowing that they did this, it’s not surprising that it took 18 months to address.”


Sky got more sympathy out of Jake Williams, co-founder and CTO at incident response firm BreachQuest, who said that DNS rebinding vulnerabilities are tough to suss out, being “relatively complex” and often “difficult for developers to understand.” 


In an email to Threatpost on Friday Williams said he doesn’t find it surprising that Sky’s developers repeatedly missed their original timelines. 


But still … 18 months? That’s “far too long to address” a flaw, regardless of how technically tough it is to understand, he commented. 


“The good news is that while Pentest Partners, the firm that discovered the vulnerability, makes the exploitation look effortless, exploitation is actually a bit more complex than most vulnerabilities,” he observed. 


At any rate, he said, it could have been worse: “This isn’t the type of vulnerability we should be as worried about as something that truly offered full remote access to the device,” he said. That’s a stroke of luck, given that most home users don’t change default passwords on their routers, he noted. Still, the incident shows how important it is to change passwords, Williams said: “Even changing to a weak password like 123456 would prevent exploitation in this case.”


*Image courtesy of [Built in Boston](https://www.builtinboston.com/2020/03/19/boston-tech-companies-work-home-policies-covid-19).*


***Cybersecurity for multi-cloud environments is notoriously challenging. OSquery and CloudQuery is a solid answer. Join Uptycs and Threatpost for “***[***An Intro to OSquery and CloudQuery***](https://bit.ly/3wf2vTP)***,” an on-demand Town Hall with Eric Kaiser, Uptycs’ senior security engineer, and find out how this open-source tool can help tame security across your organization’s entire campus.***


[***Register NOW***](https://bit.ly/3wf2vTP) ***for the on-demand event!***




#### Tags:
[[BBC]] [[DNS]] [[didn’t]] [[isn’t]] [[Threatpost]] [[ThreatPost]]
