# BrewDog exposed data of 200,000 shareholders for over a year
### The beer's on BrewDog, too.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/brewdog-exposed-data-of-200000-shareholders-for-over-a-year/)
+ Date: October 8, 2021
+ Author: Charlie Osborne


## Article:
Unknown

BrewDog exposed the personally identifiable information (PII) of roughly 200,000 shareholders for the best part of 18 months, researchers say. 


According [to PenTestPartners](https://www.pentestpartners.com/security-blog/free-brewdog-beer-with-a-side-order-of-shareholder-pii/), BrewDog "declined to inform their shareholders and asked not to be named" in the research revealing the security flaw. 

On October 8, the cybersecurity firm said that the Scottish brewery implemented a hard-coded Bearer authentication token associated with API endpoints designed for BrewDog's mobile applications.  

The tokens were returned, but rather than being triggered once a user has submitted their credentials -- therefore, allowing access to an endpoint -- as they were hardcoded, this verification step was missed.  

PenTestPartners members, who happened to be BrewDog shareholders, appended each other's customer IDs at the end of API endpoint URLs. During tests, they found they were able to access the PII of Equity for Punks shareholders without a suitable authentication challenge. 

Names, dates of birth, email addresses, genders, telephone numbers, previously used delivery addresses, shareholder numbers, shares held, referrals, and more were accessible. The customer IDs were not considered "sequential," however.  

"An attacker could brute force the customer IDs and download the entire database of customers," the researchers said. "Not only could this identify shareholders with the largest holdings along with their home address, it could also be used to generate a lifetimes supply of discount QR codes!" 






PenTestPartners noted that some of the PII exposed would fall under the GDPR protection banner, and hard-coding authentication tokens is a failure to meet these standards.  

Based on an analysis of older versions of the BrewDog app, the researchers say that the security issue was introduced in version 2.5.5, released in March 2020, and was not resolved for roughly 18 months.  

After PenTestPartners reached out with its findings, researcher Alan Monie tested a total of six different builds. It took four fix attempts before the issue was resolved in version 2.5.13, released on September 27.  

![screenshot-2021-10-08-at-12-45-45.png]()![screenshot-2021-10-08-at-12-45-45.png](https://www.zdnet.com/a/img/resize/2b6034fd916f2f981cffa160d4ea9d7a8c35ddb7/2021/10/08/72752236-e25b-4480-a097-a3b3c302f18f/screenshot-2021-10-08-at-12-45-45.png?width=370&fit=bounds&auto=webp)
 PenTestPartners
 However, the changelog for this version does not appear to mention the vulnerability fix.  

"The vulnerability is fixed," the researcher says. "As far as I know, BrewDog has not alerted their customers and shareholders that their personal details were left unprotected on the internet. I worked with BrewDog for a month and tested six different versions of their app for free. I'm left a bit disappointed by BrewDog both as a customer, a shareholder, and the way they responded to the security disclosure." 

Speaking to ZDNet, a BrewDog spokesperson provided the following statement: 

"We were recently informed of a vulnerability in one of our apps by a third party technical security services firm, following which we immediately took the app down and resolved the issue. We have not identified any other instances of access via this route or personal data having been impacted in any way. There was therefore no requirement to notify users. 

We are grateful to the third-party technical security services firm for alerting us to this vulnerability. We are totally committed to ensuring the security of our user's privacy. Our security protocols and vulnerability assessments are always under review and always being refined, in order that we can ensure that the risk of a cyber security incident is minimized." 

BrewDog also told us:

"BrewDog was notified of a vulnerability and the potential for data to be compromised. Investigations found no evidence that it was. Therefore there is no requirement to inform the ICO. An independent party documented the case as is required by the ICO."

###  Previous and related coverage

* [Enterprise data breach cost reached record high during COVID-19 pandemic](https://www.zdnet.com/article/enterprise-data-breach-cost-reached-record-high-during-covid-19-pandemic/)  

* [The biggest hacks, data breaches of 2020](https://www.zdnet.com/article/the-biggest-hacks-data-breaches-of-2020/)  

* [Twitch source code, business data, gamer payouts leaked in massive hack](https://www.zdnet.com/article/twitch-source-code-business-data-gamer-payouts-leaked-in-massive-hack/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[BrewDog]] [[PenTestPartners]] [[ZDNet]]
