# Exchange/Outlook Autodiscover Bug Spills $100K+ Email Passwords
### Hundreds of thousands of email credentials, many of which double as Active Directory domain credentials, came through to credential-trapping domains in clear text. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175004)
+ Date: September 24, 2021  2:46 pm
+ Author: Lisa Vaas


## Article:
Guardicore security researcher Amit Serper has discovered a severe design bug in MIcrosoft Exchange’s [autodiscover](https://docs.microsoft.com/en-us/exchange/architecture/client-access/autodiscover?view=exchserver-2019) – a protocol that lets users easily configure applications such as Microsoft Outlook with just email addresses and passwords.


The flaw has caused the Autodiscover service to leak nearly 100,000 unique login names and passwords for Windows domains worldwide, Serper [said in a technical report](https://www.guardicore.com/labs/autodiscovering-the-great-leak/) released this week.


“This is a severe security issue, since if an attacker can control such domains or has the ability to ‘sniff’ traffic in the same network, they can capture domain credentials in plain text (HTTP basic authentication) that are being transferred over the wire,” he said.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“Moreover, if the attacker has DNS-poisoning capabilities on a large scale (such as a nation-state attacker), they could systematically syphon out leaky passwords through a large-scale DNS poisoning campaign based on these Autodiscover TLDs [top-level domains],” Serpa wrote.


The design flaw causes the protocol to leak web requests to Autodiscover domains outside of the user’s own domain if they’re in the same TLD – i.e., Autodiscover.com. Guardicore picked up a slew of those domains and found that researchers could set them up to intercept clear-text account credentials for hapless users experiencing network difficulties or whose admins goofed on configuring DNS.


Domain-buying Spree
-------------------


Guardicore Labs picked up 11 Autodiscover domains with TLD suffixes that spanned the globe and which are listed below. Between April 16 and Aug. 25, 2021, researchers set up these domains to connect with a web server Guardicore controlled, thus configuring the domains to serve as proof-of-concept credential traps.


Those credential traps opened the floodgate to “a massive” leak of valid Windows domain credentials, according to Serper’s writeup. Over that four-month period, Guardicore captured 372,072 Windows domain credentials and 96,671 unique credentials leaked out of applications including Microsoft Outlook, mobile email clients and other apps that interface with Microsoft’s Exchange server.


To top it all off, Guardicore developed an attack that downgrades a client’s authentication scheme, elbowing it off of a secure one such as OAuth or HTLM and replacing it with HTTP Basic authentication, which sends credentials in clear text.


Thus, those hundreds of thousands of email credentials, many of which double as Active Directory domain credentials, came through to the credential-trapping domains in clear text.


The Problem: A POX Upon Your Protocol
-------------------------------------


The weakness Guardicore discovered has to do with a specific implementation of Autodiscover based on the POX (aka “plain old XML”) XML protocol, through which applications exchange raw XML documents using standard transfer protocols such as HTTP, SMTP and FTP, or by using proprietary protocols, such as message-oriented middleware.


After adding a new Microsoft Exchange account to Outlook via its auto account setup, a prompt requests a user’s username and password. After the user obliges, Outlook tries to use Autodiscover to configure the client.


Autodiscover attempts to put together a URL to fetch configuration data baked on the email domain in any of these formats that combine email domain, subdomain and a path string:


Falling that, it starts a “back-off” procedure, and therein lies the rub.


As Serper explained, this back-off mechanism “is the culprit of this leak because it is always trying to resolve the Autodiscover portion of the domain and it will always try to ‘fail up,’ so to speak.”


On its next attempt to build an Autodiscover URL, the procedure would concoct “[http://Autodiscover.com/Autodiscover/Autodiscover.xml](http://autodiscover.com/Autodiscover/Autodiscover.xml),” meaning that all of the requests that can’t reach the original domain fall into the lap of whoever owns Autodiscover.com.


After the HTTP GET requests to its purchased domains started to arrive, Guardicore was surprised to discover that many requested the relative path of /Autodiscover/Autodiscover.xml with the Authorization header pre-populated with credentials.


“The interesting issue with a large amount of the requests that we received was that there was no attempt on the client’s side to check if the resource is available, or even exists on the server, before sending an authenticated request,” Serper commented. “Usually, the way to implement such a scenario would be to first check if the resource that the client is requesting is valid, since it could be non existent (which will trigger an HTTP 404 error) or it may be password protected (which will trigger an HTTP 401 error code).”


He continued, “Between Apr 16, 2021 to Aug 25, 2021 we have captured a large number of credentials this way, needless to say, without sending a single packet other than what’s required to establish an HTTP/HTTPS session between our server and the miscellaneous clients.”


The requests – and their leaked credentials – came in from a wide range of sources: publicly traded Chinese companies. Investment banks, food manufacturers, power plants, power delivery, real estate, shipping and logistics, and jewelry companies.


Given that Microsoft Exchange is part of Microsoft’s “domain suite” of products, the fact that anybody who has credentials to log in to Exchange inboxes of such businesses – and, in most cases, also to their domain credentials – sets the stage for a world of cybersecurity hurt. “The implications of a domain credential leak in such scale are massive, and can put organizations in peril” Serber stressed. “Especially in today’s ransomware-attacks ravaged-world – the easiest way for an attacker to gain entry into an organization is to use legitimate and valid credentials.”


Guardicore sees a bit of irony in all this: Attackers try hard to weasel credentials out of users, be it through social engineering, phishing or whatever have you. This credentials leakage is like pennies from heaven for threat actors, though, coming as it does due to a design flaw in protocol meant to streamline IT operations when it comes to email client configuration. It “emphasises the importance of proper segmentation and Zero trust,” Serper wrote.


A Design Flaw That’s Been Known About for Years
-----------------------------------------------


As of Thursday, the flaw hadn’t been patched, and Microsoft Senior Director Jeff Jones told [Ars Technica](https://arstechnica.com/information-technology/2021/09/exchange-outlook-autodiscover-bug-exposed-100000-email-passwords/) that Guardicore disclosed the flaw publicly prior to reporting it to the company. But as a Guardicore spokesperson told Threatpost on Friday, it’s not the first time that the flaw has been publicly reported.


“We did not notify Microsoft initially because the protocol flaw isn’t new,” the Guardicore representative said via email. “We were just able to exploit it at a massive scale.”


In fact, as Guardicore’s paper outlined, the flaw was discovered in 2017 by Shape Security and described in [a paper](https://www.blackhat.com/docs/asia-17/materials/asia-17-Nesterov-All-Your-Emails-Belong-To-Us-Exploiting-Vulnerable-Email-Clients-Via-Domain-Name-Collision-wp.pdf) that detailed how the leak can be caused by Autodiscover implementations on email clients on mobile phones, such as Samsung’s email client on Android and Apple Mail on iOS (CVE-2016-9940, CVE-2017-2414).


Here we are, four years later, and the situation has just gotten worse, Guardicore said in the report:


The vulnerabilities disclosed by Shape Security were patched, yet, here we are in 2021 with a significantly larger threat landscape, dealing with the exact same problem only with more third-party applications outside of email clients. These applications are exposing their users to the same risks. We have initiated responsible disclosure processes with some of the vendors affected.


In a Thursday [Tweet stream](https://twitter.com/0xAmit/status/1441094788632043532), Serper called out Microsoft for lagging – for years – in a response to this known flaw. “Microsoft had plenty of time to fix or address this issue, either by patching products [or] just buying all of the autodiscover TLDs (which they are doing right now),” he wrote.


The researcher pointed to this flaw’s history of research papers (such as Shape Security’s paper), Black Hat conference talks (there was one such last month: It covered how [Autodiscover formed a part](https://threatpost.com/exchange-servers-attack-proxyshell/168661/) of the ProxyShell vulnerabilities and attacks) and news articles “proving that these issues were known.”



> 
> 1/n Thread: Last thing about the whole Microsoft conundrum because I actually have more pressing issues to deal with: Microsoft's attempt via their PR guy and the MVPs that have been dogpiling on me here and on LinkedIn are missing a point. This issue was known for years
> 
> 
> — Amit Serper (@0xAmit) [September 23, 2021](https://twitter.com/0xAmit/status/1441094788632043532?ref_src=twsrc%5Etfw)
> 
> 



Microsoft hadn’t responded to Threatpost’s request for comment by the time this article was published. Guardicore is planning to release more details as a followup to the paper it released this week.


How to Plug the Leaks
---------------------


Unfortunately, the news isn’t great for the general public: After all, Autodiscover was designed to spare them from sinking up to their elbows in the guts of email client configuration, and mitigation requires rolling up shirtsleeves. But for users who don’t mind plunging in, Guardicore did offer these protective measures:


For developers and vendors, the company offered this tip:


The Buck Stops With Microsoft
-----------------------------


Saryu Nayyar, CEO of risk-analytics provider [Gurucul](https://u7061146.ct.sendgrid.net/ls/click?upn=4tNED-2FM8iDZJQyQ53jATUSAYJveNocwbnPSKJDlL0AUsCrCneWc9pTSMEJ7OrGFoL6ih_q07lK5GAAVvAnbc-2Fr-2FBDhAPhoMvwzp-2Bdh4wgfTcF0AUhu01ZMXdKNJrsN0iCyDU7ehW0N22Ype9yCK1TM6XYzQ9CpkZyf7pccI4YxuRF0BJuYEbml5ScFK0-2F-2FZqd-2FdTf2lurjfGACG78buFm8U2vQgZEOYl5CKkQCVO6sFp8WJeINFZmyUBerTtEHoxSBMBMyNzf3aV-2FW0Yt1zGOoFVMJM-2FAQBOVLQn-2BDR94CY1D5LtmbW-2FKh5OWhBwWG9V7vvM9YN0Ov4KYhuqHiXW5lTMB-2Fzkpt5OqTeYcLBns7u4b9W6BuKDIH7QNUJF7D3-2BaAOv9jChPUWy3Ei0E881XOzXrnbDwqGuEx5cXg3Q1ZrxoCBM-3D), told Threatpost that we can all thank our lucky stars that the credentials were grabbed by Guardicore – the “good guys,” as she called them.


“That doesn’t mean that we can rest easy, however,” she cautioned. “If researchers understand the nature of the vulnerability and know how to exploit it, it’s a short link to attackers exploiting it. Those organizations using detailed security analytics can easily determine if a login or access request is legitimate and investigate and remediate if necessary. This is a clear and severe weakness, but one that organizations can detect and respond to.”


Alicia Townsend, technology evangelist at identity and access management firm [OneLogin](https://www.onelogin.com/), told Threatpost that it seems “incredible” that a product would send a user’s username and password to an untrusted endpoint.


“The fact that this is happening with an incredibly popular Microsoft product such as Exchange is even more disheartening,” she noted. “But maybe the answer lies in the fact that it is happening in a product that has been around for so long.”


Townsend pointed out it’s not clear how long this design flaw has been around, given that the Exchange Autodiscover feature was introduced in Exchange 2007. Either way, it doesn’t shine a good light on Microsoft. “Whether the oversight was on the part of early developers or was introduced by more recent developers, it is clear that Security First was not their primary objective,” she said.


Still, the buck stops in Redmond, Townsend said. “It is the responsibility of all software manufacturers both on prem and in the cloud to ensure that their developers are educated on how to create and test for secure code. We need to be continually evaluating our products for possible security risks. We need to evaluate not just new functionality but existing functionality, because as we can see with the Exchange Autodiscover feature, something could have been designed into the feature years ago and no one has been aware of it. Customers put their trust in us and we need to be ever vigilant.”


**Rule #1 of Linux Security:** No cybersecurity solution is viable if you don’t have the basics down. [**JOIN**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the [**4 Golden Rules of Linux Security**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar). Your top takeaway will be a Linux roadmap to getting the basics right! [**REGISTER NOW**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.




#### Tags:
[[Guardicore]] [[Autodiscover]] [[Microsoft]] [[Serper]] [[Threatpost]] [[Linux]] [[HTTP]] [[Windows]] [[said.]] [[wrote.]] [[ThreatPost]]
