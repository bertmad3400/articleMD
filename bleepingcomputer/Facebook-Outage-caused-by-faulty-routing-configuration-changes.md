# Facebook: Outage caused by faulty routing configuration changes
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/technology/facebook-outage-caused-by-faulty-routing-configuration-changes/)
+ Date: October 5, 2021
+ Author: Sergiu Gatlan


## Article:
![Facebook: Outage caused by faulty routing configuration changes](https://www.bleepstatic.com/content/hl-images/2021/06/30/Facebook.jpg)


Facebook says that yesterday's worldwide outage was caused by faulty configuration changes made to its backbone routers that brought all its services to a halt.


"Our engineering teams have learned that configuration changes on the backbone routers that coordinate network traffic between our data centers caused issues that interrupted this communication," [said](https://engineering.fb.com/2021/10/04/networking-traffic/outage/) Santosh Janardhan, VP for Engineering and Infrastructure at Facebook.


"This disruption to network traffic had a cascading effect on the way our data centers communicate, bringing our services to a halt."


The configuration issues also impacted the company's internal systems and tools, making it harder to bring systems online and further hindered the recovery process.


"The underlying cause of this outage also impacted many of the internal tools and systems we use in our day-to-day operations, complicating our attempts to quickly diagnose and resolve the problem," Janardhan added.


He also said that there is no evidence that Facebook users' data was compromised due to this downtime, with the company pinning the root cause behind this incident on a faulty configuration change.




> 
> To the huge community of people and businesses around the world who depend on us: we're sorry. We’ve been working hard to restore access to our apps and services and are happy to report they are coming back online now. Thank you for bearing with us.
> 
> 
> — Facebook (@Facebook) [October 4, 2021](https://twitter.com/Facebook/status/1445155265360416773?ref_src=twsrc%5Etfw)


What happened?
--------------


Yesterday, Facebook, Instagram, and WhatsApp [started coming back online](https://www.bleepingcomputer.com/news/technology/facebook-instagram-and-whatsapp-back-online-after-bgp-fix/) after the fix of a BGP routing issue that led to over six hours of downtime.


At approximately 11:50 AM EST, [all three websites suddenly became unreachable](https://www.bleepingcomputer.com/news/technology/facebook-whatsapp-and-instagram-down-due-to-dns-outage/), with browsers and apps displaying DNS errors on connection attempts.


While Facebook didn't provide any details and the massive outage appeared to be DNS-related at first, it was later learned that the problem was far worse and a lot harder to fix.


Multiple Facebook routing prefixes suddenly disappeared from the Internet's BGP routing tables, which immediately made it impossible to connect to any services hosted on those IP addresses, as Giorgio Bonfiglio, a Principal Technical Account Manager at Amazon AWS, explained.


[BGP (Border Gateway Protocol](https://www.cloudflare.com/en-gb/learning/security/glossary/what-is-bgp/)) is a routing protocol that makes the Internet work and makes it possible for devices from one side of the world to devices on the other using routes (or prefixes.)


Since Facebook's domain registrar and DNS servers are hosted on the company's own routing prefix, when the BGP prefixes were removed from routing tables, no one could connect to their IP addresses or the services running on top of them.


"The BGP routes pointing traffic to Facebook's IP address space have been withdrawn. The Internet no longer knows where to find Facebook's IPs. One symptom is that DNS requests are failing," [said](https://isc.sans.edu/forums/diary/Facebook+Outage+Yes+its+DNS+sort+of+A+super+quick+analysis+of+what+is+going+on/27900/) Johannes B. Ullrich, Ph.D., Dean of Research at the SANS Technology Institute.


"But this is just the result of Facebook hosting its DNS servers inside its own network. Even with working DNS (for example if you still have cached results), the IPs are currently not reachable."


"To everyone who was affected by the outages on our platforms today: we're sorry," a Facebook spokesperson told BleepingComputer.


"We know billions of people and businesses around the world depend on our products and services to stay connected. We appreciate your patience as we come back online."




#### Tags:
[[Facebook]] [[BGP]] [[DNS]] [[IP]] [[Bleeping Computer]]
