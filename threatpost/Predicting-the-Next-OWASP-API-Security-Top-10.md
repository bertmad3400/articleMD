# Predicting the Next OWASP API Security Top 10
### API security risk has dramatically evolved in the last two years. Jason Kent, Hacker-in-Residence at Cequence Security, discusses the top API security concerns today and how to address them.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175961)
+ Date: November 3, 2021  1:05 pm
+ Author: Jason Kent


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/31092830/APIs-e1630416526184.gif)
As a long-time OWASP member and application security practitioner, I wanted to share my thoughts on how the newly released OWASP Web App Top 10 might impact or influence the updates to the API Security Top 10, last released back in December 2019.


These lists cover the most common causes for security events. Web App Top 10 was recently updated to reflect the ever-changing application and threat landscape. You can read more about the categories that were added, changed or expanded in scope [here](https://owasp.org/Top10/).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


In its current form, the API Security Top 10 has roughly a 60 percent overlap with the 2017 Web App Top 10. This made sense at the time, given that application programming interface (API) usage was just beginning to explode and there was a definite need for guidance on how best to address the security requirements for APIs.


Since the release of the API Top 10, both API usage and related security concerns have changed. Even so, many parallels can be drawn from the API Top Ten and the new Web App Top 10:


![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/03095853/API-Security-1.png)


In the next API Security Top 10 list, I expect the nomenclature to align, though I don’t expect similar positioning because of the (obvious) differences between APIs and web apps. I expect that there will be some overlap with the new Web App list, but with a smattering of API-specific threats—perhaps something like this:


![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/03100002/API-Security-2.png)


Let’s go through the predictions for that future list.


The Next OWASP API Security Top 10
----------------------------------


API authentication and authorization error-related security incidents are nearly as common as security misconfigurations, justifying the placement at the top of the list (and calling into question the No. 5 placement for misconfigurations). Organizations need to pay closer attention to the way that they design and implement APIs, perhaps using security specifications that can watch for missing endpoint authentication, authorization and administrative functions.


Cryptographic failures have always plagued web applications. In the early days, developers were resistant to make changes that might require a user upgrade. As a result, making strong encryption an app (or API) requirement was frowned upon — but not anymore. Forcing an upgrade that improves data protection and possibly prevents a credit breach is now (and should be) the norm, not the exception. A developer might lose one or two customers but it won’t be worried about making the news on a credit-card breach from leaky data exchanges and poor encryption. Similarly, applications utilizing APIs can now contain certificates and robust encryption algorithms.


This threat ranks higher on the list because APIs make it easier for both legitimate or malicious traffic spikes to occur. We have seen 30X more malicious traffic spikes against APIs this year. If rate limiting weren’t applied, this would be a disaster. Organizations need to be more diligent about implementing rate limiting on APIs as it not only helps fend off malicious attacks, but also helps control infrastructure-cost overruns.


APIs with misconfigured security is a common error we see within our customer base, and based on what we see in the news, it’s a common error for many organizations. Unexpected endpoints, or those without authentication or authorization flags, are just a few examples of errors we see. The reason for the frequency is that API security misconfigurations are something that most organizations aren’t instrumented to look for. To get this one off the list, organizations need to understand and test their API functionality — and not just pen tests, but true functionality tests.


Once viewed as an oddity, the role of the Application Security Architect has rapidly evolved with the widespread adoption of “[shift left](https://devopedia.org/shift-left)” and DevSecOps. As APIs have become more foundational, understanding the architecture and specifically the security of each part of the API is critical. When an application consumes or emits data internally, externally, or to/from a third party, all instances where that data will be accessed or moved requires secure design. This is just a small example of the idea that when architecture is needed, considerations for login, session management, authorization and other aspects need to be included as well.


Injection is low on this list and high on the new AppSec Top Ten because web applications are viewed through a web browser and require JavaScript to render parts of the page. This can lead to cross-site scripting (XSS), which is usually followed by SQL injection against the backend database. APIs typically don’t require a browser, so injections are possible but less likely. API injection usually only occurs when someone has a deep understanding of the application and is trying to break another mechanism.


API asset management starts with a good inventory that is updated as elements are added and removed. Most organizations struggle with their application inventory, and very few have an accurate picture of the number of APIs they have and all of their associated components. API visibility and asset management should be a cornerstone of all API security initiatives.


Whenever the main security question of “what happened?” is asked, invariably the answer can only be derived by finding out what logs are available. Without logs, the root cause is difficult to determine. And without monitoring, it is quite possible no one will ever ask “what happened?” because the breach will still be happening. Logging and monitoring are inexpensive, simple to implement and often needed for troubleshooting. I would love to see this one fall off the list in the next round.


This ends up being a bit of a catch-all for anything that revolves around data integrity in the API. This could be a third-party library or some other dependency with a flaw in it. It could be an issue with the continuous integration and delivery (CI/CD) pipeline not confirming sources or adding sources that are vulnerable in some way. These types of failures are becoming more prominent, but the concept of code integrity has become increasingly important. We have an opportunity to reverse this trend.


This API Top 10 list is what I feel is going to be reflected in the official OWASP list revision in the near future. Most of this comes from dealing with APIs being attacked by automated adversaries and those that wish to gain a foothold within an organization. Hopefully this list is heavily modified in its final form as we have fixed many of these categories — but alas, hope is all we have.


***Jason Kent is Hacker-in-Residence at Cequence Security.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[API]] [[OWASP]] [[list,]] [[ThreatPost]]
