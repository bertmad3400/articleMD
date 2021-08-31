# Top 3 APIs Vulnerabilities: Why Apps are Owned by Cyberattackers
### Jason Kent, hacker-in-residence at Cequence, talks about how cybercriminals target apps and how to thwart them.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169048)
+ Date: August 31, 2021  9:29 am
+ Author: Jason Kent


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/31092830/APIs-e1630416526184.gif)
Application programming interfaces (APIs) have become the glue that holds today’s apps together. There’s an API to turn on the kitchen lights while still in bed. There’s an API to change the song playing on your house speakers. Whether the app is on your mobile device, entertainment system or garage door, APIs are what developers use to make applications function.


There are three major vulnerability types that cyberattackers target in order to “own” apps. But first, some background on what makes APIs such a security concern.


APIs can operate much the same way that a URL might operate. Typing “www.example[.]com” into a web browser will elicit a response from example.com. Search for your favorite song and you will see the following in the URL bar: “www.example.com/search?{myfavoritesong}.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The page result is dynamically built to present you with your search findings. Your mobile banking app operates in the same manner, with the API grabbing your name, account number and account balance — and populating the fields in the pre-built pages accordingly. While APIs have similar characteristics to web applications, they are far more susceptible to attacks; they include the entire transaction, including any security checks, and are typically communicating directly to a back-end service.


Increased API Vulnerabilities: History Repeats Itself
-----------------------------------------------------


In the late 1990s folks figured out that you could often drop a single quote ” ‘ ” into a search box or login field and the application would respond with a database error. Understanding SQL database syntax means that a vulnerable application was simply a wide-open application that one could potentially have total control over. And once found, SQL vulnerabilities were often attacked.


This reflects the problems we have had in application security forever: Input validation. Without proper function and security testing, APIs can become a perfect point of attack. Trusted by the application, with high-speed, massive data exchanges possible, APIs are a cause for concern for any organization that is utilizing them or developing them for use.


Top 3 API Vulnerabilities
-------------------------


In my work with customers in the application-security market and my long-time involvement in the Open Web Application Security Project (OWASP) community, I commonly see API vulnerability exploits. Here are three of the most common types:


Fixing the Problem
------------------


2021 is already the year of the API security incident, and the year is not over. API flaws impact the entire business – not just dev, or security or the business groups. Finger-pointing has never fixed the problem. The fix begins with collaboration; development needs a full understanding from business groups on how the API should function. API coding is different, so a refresh on secure coding practices is warranted. And security needs to be involved upfront, to help uncover gaps before publication.


A great place to start is with the OWASP. It has published the [API Security Top 10](https://cloudsecurityalliance.org/blog/2021/05/11/understanding-the-owasp-api-security-top-10/) and recently published the [Completely Ridiculous API](https://github.com/OWASP/crAPI), which includes examples of bad APIs in an application. Organizations can use the Completely Ridiculous API online or in-house as an educational platform to train development and security on the errors to avoid when utilizing APIs.


Whether you are utilizing an “API-first approach” or just starting your journey into digital transformation aided by APIs, knowing the vulnerabilities that are out there and what might happen if something is missed, is crucial.


***Jason Kent is hacker-in-residence at Cequence Security.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[API]] [[ThreatPost]]
