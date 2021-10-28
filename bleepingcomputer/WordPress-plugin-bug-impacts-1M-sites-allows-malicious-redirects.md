# WordPress plugin bug impacts 1M sites, allows malicious redirects
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/wordpress-plugin-bug-impacts-1m-sites-allows-malicious-redirects/)
+ Date: October 28, 2021
+ Author: Bill Toulas


## Article:
![wordpress](https://www.bleepstatic.com/content/hl-images/2020/09/10/WordPress-war.jpg?rand=629131620)


The OptinMonster plugin is affected by a high-severity flaw that allows unauthorized API access and sensitive information disclosure on roughly a million WordPress sites.


Tracked as CVE-2021-39341, the flaw was discovered by researcher Chloe Chamberland on September 28, 2021, with a patch becoming available on October 7, 2021.


All users of the OptinMonster plugin are advised to upgrade to version 2.6.5 or later, as all earlier versions are affected.


API trouble
-----------


OptinMonster is one of the most popular WordPress plugins used to create beautiful opt-in forms that help site owners convert visitors to subscribers/customers.


It is essentially a lead generator and monetization tool, and thanks to its ease of use and abundance of features, it's deployed on approximately a million sites.


As Chamberland explains in her vulnerability [disclosure report](https://www.wordfence.com/blog/2021/10/1000000-sites-affected-by-optinmonster-vulnerabilities/), OptinMonster's power relies upon API endpoints that allow seamless integration and a streamlined design process.


However, the implementation of these endpoints isn’t always secure, and the most critical example concerns the ‘/wp-json/omapp/v1/support’ endpoint.


This endpoint can disclose data such as the site’s full path on the server, API keys used for requests on the site, and more.


An attacker holding the API key could make changes on the OptinMonster accounts or even plant malicious JavaScript snippets on the site.


The site would execute this code every time an OptinMonster element was activated by a visitor without anyone's knowledge.


To make matters worse, the attacker wouldn’t even have to authenticate on the targeted site to access the API endpoint, as an HTTP request would bypass security checks under certain, easy to meet conditions.



![A request to the vulnerable API endpoint](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/request.jpg)**A request to the vulnerable API endpoint**  

Source: Wordfence
While the case of the '/wp-json/omapp/v1/support' endpoint is the worse, it's not the only insecure REST-API endpoint vulnerable to exploitation.


After the researcher's report reached the OptinMonster team, the developers of the popular WordPress plugin realized that the entire API needed revisiting.


As such, you must install any OptinMonster updates that land on your WordPress dashboard over the following weeks, as these will likely address additional API flaws.


In the meantime, all API keys that could have been stolen were invalidated immediately, and site owners were forced to generate new keys.


This case highlights that even widely deployed and extremely popular WordPress plugins can carry multiple undiscovered flaws for extensive periods.


If you are a site owner, try to use the minimum number of plugins to cover the necessary functionality and usability and apply plugin updates as soon as possible.




#### Tags:
[[API]] [[OptinMonster]] [[WordPress]] [[plugin]] [[plugins]] [[Bleeping Computer]]
