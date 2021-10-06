# Facebook outage leads to massive user exodus to Telegram, Signal
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/technology/facebook-outage-leads-to-massive-user-exodus-to-telegram-signal/)
+ Date: October 6, 2021
+ Author: Sergiu Gatlan


## Article:
![Facebook outage leads to massive user exodus to Telegram, Signal](https://www.bleepstatic.com/content/hl-images/2021/10/06/Facebook.jpg)


*Image: [Thought Catalog](https://unsplash.com/@thoughtcatalog)*


Facebook has finally confirmed that a BGP routing blunder caused the worldwide outage affecting its social media platforms and apps.


This comes after competitors like Signal and Telegram shared info on a massive exodus of Facebook users joining or switching to other platforms following the 6-hour-long downtime that impacted Facebook, Instagram, and WhatsApp.


Signal and Telegram also began experiencing in the wake of Facebook's global outage after millions of Facebook users were joining their platforms.


"Signups are way up on Signal (welcome everyone!)," Signal's social media team [tweeted](https://twitter.com/signalapp/status/1445062426739855366) while Facebook was dealing with the outage on Monday.


"Millions of new people have joined Signal today and our messaging and calling have been up and running but some people aren't seeing all of their contacts appear on Signal. We're working hard to fix this up."


70 million Facebook refugees joined Telegram in one day
-------------------------------------------------------


Pavel Durov, Telegram's CEO and founder, also added that more than 70 million users joined in a single day, following Facebook's downtime.


He also added that this massive deluge of millions of new users led to performance issues as they were all trying to sign up on the messaging platform simultaneously.


"The daily growth rate of Telegram exceeded the norm by an order of magnitude, and we welcomed over 70 million refugees from other platforms in one day," Durov said.


"I am proud of how our team handled the unprecedented growth because Telegram continued to work flawlessly for the vast majority of our users."


Facebook's CEO, Mark Zuckerberg, tried to downplay the impact of this user exodus, saying that Facebook isn't concerned with people's decision to switch to competitors or the money lost due to such outages.


"The SEV (site event) that took down all our services yesterday was the worst outage we've had in years. We've spent the past 24 hours debriefing how we can strengthen our systems against this kind of failure. This was also a reminder of how much our work matters to people," Facebook's CEO Mark Zuckerberg [said](https://www.facebook.com/4/posts/10113961365418581/?d=n).


"The deeper concern with an outage like this isn't how many people switch to competitive services or how much money we lose, but what it means for the people who rely on our services to communicate with loved ones, run their businesses, or support their communities."


BGP routing issue behind the outage
-----------------------------------


On October 4, at roughly11:50 AM EST, [all three platforms suddenly became unreachable](https://www.bleepingcomputer.com/news/technology/facebook-whatsapp-and-instagram-down-due-to-dns-outage/), with users reporting that web browsers and apps were displaying DNS errors on connection attempts.


While Facebook didn't immediately provide details on what happened, it was later discovered that multiple Facebook [BGP (Border Gateway Protocol)](https://www.cloudflare.com/en-gb/learning/security/glossary/what-is-bgp/) routing prefixes suddenly disappeared, making it impossible to connect to any of the services hosted on those IP addresses.


"The BGP routes pointing traffic to Facebook's IP address space have been withdrawn. The Internet no longer knows where to find Facebook's IPs. One symptom is that DNS requests are failing," [said](https://isc.sans.edu/forums/diary/Facebook+Outage+Yes+its+DNS+sort+of+A+super+quick+analysis+of+what+is+going+on/27900/) Johannes B. Ullrich, Ph.D., Dean of Research at the SANS Technology Institute.


Yesterday, the company confirmed a faulty backbone router configuration change was behind the outage but didn't link it to a BGP routing issue.


However, in [an update posted later in the day](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/), Facebook revealed that its DNS servers disabled all BGP advertisements after a command was sent to assess the availability of its global backbone network during a routine maintenance job, taking down its data centers worldwide in the process.




> 
> To the huge community of people and businesses around the world who depend on us: we're sorry. We’ve been working hard to restore access to our apps and services and are happy to report they are coming back online now. Thank you for bearing with us.
> 
> 
> — Facebook (@Facebook) [October 4, 2021](https://twitter.com/Facebook/status/1445155265360416773?ref_src=twsrc%5Etfw)


"During one of these routine maintenance jobs, a command was issued with the intention to assess the availability of global backbone capacity, which unintentionally took down all the connections in our backbone network, effectively disconnecting Facebook data centers globally," [said](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/) Santosh Janardhan, VP for Engineering and Infrastructure at Facebook.


"Our systems are designed to audit commands like these to prevent mistakes like this, but a bug in that audit tool didn't properly stop the command."




#### Tags:
[[Facebook]] [[BGP]] [["The]] [[DNS]] [[Bleeping Computer]]
