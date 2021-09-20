# Bring Your APIs Out of the Shadows to Protect Your Business
### APIs are immensely more complex to secure. Shadow APIs—those unknown or forgotten API endpoints that escape the attention and protection of IT¬—present a real risk to your business. Learn how to identify shadow APIs and take control of them before attackers do.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169334)
+ Date: September 20, 2021  9:00 am
+ Author: Unknown


## Article:
![API Shadow](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/16081604/API-Shadow.jpeg)
*[![Pankaj Gupta](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/16081324/Pankaj-Gupta-1-214x300.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/16081324/Pankaj-Gupta-1.jpg)*


*Pankaj Gupta, Senior Director, Citrix*


 


APIs are immensely more complex to secure. What was previously one request to one server has become dozens or hundreds of requests to dozens or hundreds of entities. In the past, you defended one large application with a single front door. Now you must defend applications with many doors and windows. This is made immeasurably harder when new windows open without your knowing.


 


The unknown is very dangerous
-----------------------------


Shadow APIs—those unknown or forgotten API endpoints that escape the attention and protection of IT­—present a real risk to your business.


Shadow APIs often exist as the result of third-party applications used by individual departments without central IT’s knowledge and outside their jurisdiction. Shadow APIs can also be present when applications are not properly decommissioned, leaving APIs accessible and vulnerable to attack. And even applications that are in use and actively managed by IT can be susceptible to attack when APIs have been incorrectly documented or added without telling IT.


In each case, because IT is not aware of an API’s existence, they cannot secure it, which increases the risk that the application—or the data it exposes—will be compromised.


Discover your APIs, protect your business
-----------------------------------------


Because you can’t protect what you can’t see, it is imperative that you discover, catalog, and bring your shadow APIs under governance before they are discovered by bad actors and exploited.


The first step is to identify *every* API endpoint in use within your organization. While this might be easy for APIs you know about, the bigger challenge is to [discover every unknown API](https://www.citrix.com/blogs/2021/04/14/api-protection-made-simple-with-api-discovery/). This means monitoring traffic to every server and application. You should use your API gateway or application delivery controller ([ADC](https://www.citrix.com/products/citrix-adc/)) to check every API calls traffic, compare it against a list of known APIs, and mark any that are not recognized as rogue.


Discovering APIs being actively used is simpler as ADC have visibility and intelligence to discover API traffic. But APIs not in active use or lack the documentation could be very challnaging as they still pose significant resucity risk. To discover API’s not in use and without documentaion, you have to reply on code analysis tools. Legacy or apps developed long time back are great candidates to start code scans.


Also identify all the teams who are developing APIs and ask them to documenting and creating the inventory of all their APIs.


Indications of a problematic API could be an API call to an IP address for which no APIs are registered. It might be a call to a URL that is not intended to be exposed. Or perhaps a call to a known API that uses a different communication method than is expected (GET instead of POST, for example). These situations are all indicative of uncontrolled APIs that attackers could use to get access to and expose your corporate data.


Your northstar is to discover *every* API endpoint.


You must catalog all your APIs. Ideally, your inventory will be created automatically on discovery by your API gateway or ADC. Don’t rely on manual methods like a spreadsheet because it will soon become unwieldy. Automate everything with APIs! Once you discover previously unknown APIs that could pose a security risk, you need to ensure that they are investigated.


Unfortunately, like all security processes, this is not a “one and done” task. You need to keep the inventory up to date, which effectively means continuous scanning and analyzing changes over time. API security is a journey, not a destination.


Once you become aware of a previously unknown API, you need to bring it into line with your API governance strategy to secure it.  Create a centralised point where all API govereance policies are defined and enforced consistently including standardizing API design.


Find the owner of each API and decide whether or not it’s actually required. If you can disable an unused API, you don’t have to worry about securing it. However, this is easier said than done when you must track down partners to find out if they are still using a specific API.


When you secure a particular API, make sure it is well documented and that you know the schema for the requests and responses so that you can lock it down more effectively and identify attacks against it. Also make sure that the API is versioned so that you know when there are updates and whether you need to adjust your security policies.


Most importantly, establish and enforce a well-defined API introduction and deprecation strategy.


If APIs cannot be put into production without IT’s knowledge, then you can better control and secure them. And if IT is consulted when APIs are removed from service, you can ensure that there are no orphaned APIs giving up their data freely. This will dramatically reduce the risk of accidentally exposing sensitive data.


Take control of your APIs before attackers take control of your business
------------------------------------------------------------------------


There is nothing more frustrating than locking all the windows and bolting all the doors only for someone to open new entryways and not tell you. Shadow APIs are a serious security problem, and the situation is only going to get worse as multiple departments and developers continue to institute new APIs without following a defined API security governance process.


IT needs to take control of *all* APIs—including the shadow APIs—and put the right governance in place to secure them before attackers exploit them. Shadow APIs are aptly named: If they are not identified and properly secured, they will cast a dark shadow on your security posture and business.




#### Tags:
[[API]] [[API,]] [[it.]] [[ThreatPost]]
