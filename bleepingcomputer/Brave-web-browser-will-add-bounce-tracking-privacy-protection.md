# Brave web browser will add bounce tracking privacy protection
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/software/brave-web-browser-will-add-bounce-tracking-privacy-protection/)
+ Date: October 15, 2021
+ Author: Bill Toulas


## Article:
![brave](https://www.bleepstatic.com/content/hl-images/2020/11/02/brave-glowing.jpg?rand=1540218075)


Brave, the privacy-conscious web browser, has announced plans to introduce additional privacy protections against 'bounce tracking,' a newer form of tracking that is not currently blocked by the browser.


The new system, which Brave’s team calls “debouncing”, addresses the bounce tracking method, which disregards users' privacy preferences such as the 'Do Not Track' setting and the blocking of third-party cookies.



![tracker settings](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/image%20(1).png)**User tracker settings on Brave**
Redirects used to track users
-----------------------------


Online advertisers and their partners are using a new trick to bypass user preferences while still operating within a legal context by redirecting users through a tracker site that redirects to the intended destination.


Thanks to this bounce, when a user attempts to visit a site, the tracker will be in a position to capture both the origin site and the destination URL.


This only happens for a brief moment, almost imperceptibly in most cases, and is called "bounce tracking".



![Diagram showing how bounce tracking works](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/tracker%20example.png)**Diagram showing how bounce tracking works**  

Source: Brave
If a user visits two or more sites that point to the same bounce tracking network, significant chunks of their browsing activity could be monitored.


Blocking trackers on these sites (origin and destination) doesn’t stop the bounce tracking from uncovering your online whereabouts, as the problem takes place on the navigational level.


Brave's solution
----------------


Brave’s debouncing works by actively monitoring which sites use bouncing trackers and replacing the injected intermediate tracking URL with the final URL that the user intends to visit. As such, the navigation becomes direct and the privacy of the user remains intact.


The same system will strip affiliate marketing links and send the user straight to the target site through a “clean” URL.


But Brave won’t rely solely on the dynamic detection of bounce tracking URLs. The project maintains a constantly updated [list of these intermediate URLs](https://github.com/brave/adblock-lists/blob/master/brave-lists/debounce.json), so a rapid check against them will take place too.


Right now, the new debouncing system is being tested on the “Nightly” version of Brave, and [the announcement](https://brave.com/privacy-updates-11/) promises a full roll out on desktop version 1.32.


The new feature will be enabled automatically in the web browser, but those who still want to go through bounce tracking domains will be given the option to disable it.


Navigational tracking remains a troubling problem for internet users, and the World Wide Web Consortium has [formed a working group](https://privacycg.github.io/nav-tracking-mitigations/#intro) to develop a standardized protection system against it.


Other browsers currently offering redirect tracking protection include Firefox and Safari.


Firefox follows a list-based approach to combat the problem, while Safari users algorithmic detection to detect and label sites that push users through unneeded bouncing patterns.




#### Tags:
[[Brave]] [[Bleeping Computer]]
