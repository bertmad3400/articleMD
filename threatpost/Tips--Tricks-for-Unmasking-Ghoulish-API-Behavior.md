# Tips & Tricks for Unmasking Ghoulish API Behavior
### Jason Kent, hacker-in-residence at Cequence Security, discusses how to track user-agent connections to mobile and desktop APIs, to spot malicious activity.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175253)
+ Date: September 30, 2021  1:56 pm
+ Author: Jason Kent


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/30134206/unmask-1.jpg)
I was analyzing one of my customer’s API traffic the other day and I noticed something odd about the devices that were using the mobile application API. I found standard browsers like Firefox and Chrome hitting API endpoints that should only be touched by their mobile-application communication.


In the application development world, we call browsers “user agents (UA)” or “user-agent strings.” For example, when an analyst looks at a batch of web logs, they would see the user agent for Chrome appearing as “Mozilla/5.0 (Macintosh; Intel Mac OS X 11\_5\_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36.” This is a user sitting in front of a laptop or desktop with Chrome open, browsing the web.


On a mobile application, the development staff will create a user agent for their application. It can be something like “CoolAppV1-iPhone,” or anything else they want to use. The iPhone and Android user agents are often different, but they are almost always a hand-coded string that means something to the developers.


In this way you can track what kind of devices are hitting the APIs. Which is helpful, because I recommend that the API endpoints that the mobile applications and the web applications be completely different.


**Separate Mobile and Web Domains**
-----------------------------------


That’s because using generic terms that only your team knows in order to separate mobile and web domains makes it easier for you to spot malicious behavior.


For instance, iPhone or Android apps might communicate with app.example.com, while the website is www.example.com. This separation of subdomains and application flow allows us to see where the UA outliers might be.


For instance, if I see Chrome browser activity on a laptop showing up on app.example.com, I know something is up. It could be a developer testing their work, but this is unlikely in production. It could be a fluke, but flukes are rare in security. Most likely, someone has taken the app communication apart and is poking around.


Similarly, if you have a web application that is typically used via a web browser, analyzing the types of browsers that land on your page is important. Threat actors will commonly try to hide in plain sight by manipulating, or rotating through a high number of UAs. Lately we are seeing browsers that look like “Ruby” or “HTTP” but they are not actual user-agent strings.


**Beware of Crawlers**
----------------------


UAs are also common targets for known “crawlers” like Facebook (facebookexternalhit/1.1 (+http://www.facebook.com/externalhit\_uatext.php)), which crawl various places on a website but should rarely be seen in your mobile app flow.


The only communication that should be touching your mobile application are the mobile applications installed on your user’s phones. If you are seeing crawlers on your mobile application, you might have a problem elsewhere. It could be that somehow the endpoints are being learned by the Facebook crawler as it indiscriminately finds and tests URIs.


If you see suspicious activity on your UAs, you should look for possible errors like comments with URIs in them, advertised routes, or code repos publicly exposed or within your application paths. A public crawler on your application fabric is commonly a precursor to traffic from threat actors.


**Check for Suspicious Patterns in Your Application Logs**
----------------------------------------------------------


As a simple first step, analyze the UAs most prevalent in your application logs. If you are seeing odd or extremely old user-agent strings, you might have a threat actor poking around. Periodic log reviews are critical in discovering potentially malicious patterns. Having a systematic way to review these items and raise alarms, if needed, can effectively minimize the malicious traffic on your web and mobile applications.


Bottom line: Security often boils down to analysis of everyday things in order to notice patterns and put mitigations in place that keep the environment safe.


***Jason Kent is hacker-in-residence at Cequence Security.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[API]] [[ThreatPost]]
