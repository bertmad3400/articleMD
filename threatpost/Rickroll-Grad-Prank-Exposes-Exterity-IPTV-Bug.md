# Rickroll Grad Prank Exposes Exterity IPTV Bug
### IPTV and IP video security is increasingly under scrutiny, even by high school kids.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175491)
+ Date: October 14, 2021  4:38 pm
+ Author: Becky Bracken


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/14162918/rickroll-e1634243370645.jpg)
When Township High School District 214 in Illinois got rickrolled all at once across its six different schools just before graduation, it was more than a meticulously executed senior prank.


Cybersecurity star-in-the-making and recent high-school graduate Minh Duong found, and was able to exploit, a zero-day bug in the district’s [Exterity IPTV system](https://whitehoodhacker.net/posts/2021-10-04-the-big-rick). The goof was received in good humor by school administrators, luckily for Minh and his cohorts, and the bug was reported to Exterity.


But so far, the company hasn’t responded to Minh’s disclosure or said anything about possible mitigations, he said.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“If I don’t end up hearing back from them in my next few attempts at contact, I will publish the exploit that I used,” he told Threatpost. “CVE-2021-42109 has been reserved for the Exterity IPTV privesc vulnerabilities, with my blog post being listed as a reference.”


“The Big Rick,” as the prank was called, came off beautifully — hijacking every TV, projector and monitor on the district’s IPTV system to play Rick Astley’s classic video for “Never Gonna Give You Up.”


Projectors and TVs across the Township district are all connected, and can be controlled through a blue box with three Exterity tools: The AvediaPlayer receiver, the AvediaStream encoder and the AvediaServer for management.


“These receivers include both a web interface and an SSH server to execute the serial commands,” he wrote. “Additionally, they run embedded Linux with BusyBox tools, and use some obscure CPU architecture designed for IoT [internet of things] devices called ARC (Argonaut RISC Core).”


The monitors can be centrally controlled to broadcast and receive things like morning announcements; with his exploit, Minh had full access and control.


“Since freshman year, I had complete access to the IPTV system,” he said. “I only messed around with it a few times and had plans for a senior prank, but it moved to the back of my mind and eventually went forgotten.”


Until he had the idea for “the Big Rick.” There’s even a video to document the moment:


“This is where I state the disclaimer again: never access other systems in an unauthorized manner without permission,” he wrote.


So far, there’s no indication that Threatpost could uncover that the bugs have [been fixed](https://www.exterity.com/about/news/vitec-acquires-exterity-to-create-global-iptv-and-digital-signage-powerhouse?utm_source=Social%20Media&utm_medium=LinkedIn&utm_campaign=Vitec%20announcement) by Exterity, which was recently acquired in April by IP video-tech company VITEC. Neither company responded to Threatpost’s inquiries by press time. According to its [company site,](https://www.exterity.com/about/whoweare) Exterity is used across the world to deliver broadcast-quality television over IP networks.


The news comes as IP video vendors are increasingly under attack by threat actors.


For instance, three bugs were found in [IP video surveillance systems](https://threatpost.com/ip-surveillance-bugs-axis-rce-data-theft/175350/) from Axis communications earlier this month (CVE-2021-31986, CVE-2021-31987, CVE-2021-31988), which researchers said impacted every device run on the company’s embedded operating system.


Last summer, the Cybersecurity and Infrastructure Security Agency (CISA) issued a warning about a [supply-chain flaw](https://threatpost.com/millions-connected-cameras-eavesdropping/166950/) in ThroughTek security cameras that left them open to unauthorized access.


As for Minh, he’s studying at University of Illinois at Urbana-Champaign this semester, and said he’s interested in pursuing a career in infosec.


***Check out our free***[***upcoming live and on-demand online***](https://threatpost.com/category/webinars/) ***town halls*** ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Exterity]] [[IPTV]] [[IP]] [[Minh]] [[ThreatPost]]
