# Payment API Bungling Exposes Millions of Users’ Payment Data
### Misconfigured APIs make any app risky, but when you’re talking about financial apps, you’re talking about handing ne’er-do-wells the power to turn your pockets inside-out.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=174825)
+ Date: September 20, 2021  3:02 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/20144055/stealing-money-e1632163270893.jpeg)
App developers have once again been accused of having butterfingers when it comes to API keys, leaving millions of mobile app users at risk of exposing their personal and payment data.


CloudSEK, maker of artificial intelligence- (AI-) enabled digital threat protection, [reported](https://bevigil.com/blog/exposed-payment-integration-api-keys-imperil-millions-of-users-transaction-details-and-pii/) last week that the mobile ecosystem is reeking with hard-coded API keys: Keys that should never be exposed in endpoint apps.


Misconfigured APIs make any app risky, but when you’re talking about financial apps, it’s about handing ne’er-do-wells the power to turn victims’ pockets inside-out.


“While the rampant exposure of API keys is hazardous for any app, it is especially critical when it comes to apps that handle payment information such as bank details, credit card information and UPI transactions, in addition to user [personally identifiable information, or PII],” according to CloudSEK’s writeup.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


APIs – application programming interfaces – are the veins and arteries of the mobile ecosystem, enabling apps to communicate with multiple sources and to move data in and out of those apps. It’s an “integral” part of how an app works, CloudSEK said, which means that app developers need to handle them with kid gloves in order to avoid leaking customer data: “Any systematic mishandling of API keys among app developers can cause threat to the app’s business,” researchers maintained.


But like so much of cybersecurity, it’s a could-a, should-a situation: “CloudSEK has observed that a wide range of companies – both large and small – that cater to millions of users have mobile apps with API keys that are hardcoded in the app packages,” according to CloudSEK researchers Arshit Jain and Sai Ahladini Tripathy. “These keys could be easily discovered by malicious hackers or competitors who could use them to compromise user data and networks.


They added, “Hardcoded API keys are akin to locking your house but leaving the key in an envelope titled ‘do not open.'”


It’s Raining APIs
-----------------


CloudSEK pointed to recent high-profile attacks as examples of how API misconfigurations have led to compromised cloud infrastructure, including the [2019 breach](https://threatpost.com/imperva-data-breach-cloud-misconfiguration/149127/) of security vendor Imperva. The Imperva breach was triggered by the theft of an Amazon Web Services (AWS) administrative API key housed in a cloud instance that was left exposed to the public internet.


APIs use a combination of a key\_id and a key\_secret to make API requests to payment-service providers. CloudSEK’s investigation uncovered 10 apps that were exposing both halves of the equation.


Researchers focused on 13,000 apps currently uploaded to CloudSEK’s mobile app security search engine BeVigil, about 250 of which – roughly 5 percent – were using the Razorpay API to power financial transactions.


But the fact that CloudSEK only checked out Razorpay transactions to find those 10 leaky apps also means that “the actual number of apps exposing API keys could be higher,” CloudSEK suggested. That’s a likely scenario, given that millions of businesses use Razorpay as a payment gateway.


Mind you, there’s no flaw with the Razorpay financial payment gateway or other such payment integration services. No, this is all on developers, CloudSEK asserted, the API key exposures being “evidence of how API keys are mishandled by app developers.”


The report stressed that the onus is also on the companies where the keys are getting bungled: “It is up to individual companies to address the security concerns associated with payment gateways, AWS services, open Firebases, etc.”


Below is a redacted screen capture listing the package names identified in apps submitted to CloudSEK’s BeVigil search engine that are using Razorpay as a payment gateway:


Many of the apps exposing API keys – apps that include health and fitness, eCommerce, travel and hospitality, healthcare and pharma – have more than a million downloads. The apps are based in India, which is also where CloudSEK is based. A selection of the affected apps:


A Well-Known Issue
------------------


As CloudSEK pointed out, the fact that unauthorized access to API keys can allow threat actors to query sensitive information or access critical data is old news. For example, in 2019, North Carolina State University published a report ([PDF](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_04B-3_Meli_paper.pdf)) describing the discovery of more than 100,000 GitHub repositories whose API or cryptographic keys [had leaked](https://www.zdnet.com/article/over-100000-github-repos-have-leaked-api-or-cryptographic-keys/).


In fact, over the weekend, just a few days after CloudSEK published its report, penetration tester [Abdulrahman-Kamel](https://www.linkedin.com/in/abdulrahman-kamel/?originalSubdomain=eg) shared what happened after he created a Python script that searched through archived requests in the Wayback Machine: A project that archives the content of internet sites.


In a nutshell, the penetration tester found API leakage that would let an attacker access [more than 10,000 paid API keys](https://4bdoz.medium.com/access-more-than-10k-premium-api-keys-python-exploit-c728fdf5eae) and to use them to get free services or sensitive data.


Tsk, tsk, remarked Michael Isbitski, technical evangelist at Salt Security: “In this case, the impacted sites committed the worst form of offense where they relied on API keys submitted as parameters within a URL (i.e., a GET request),” he told Threatpost on Monday. “This implementation approach goes against security best practice, where no sensitive data should be submitted in a URL. Sensitive data in URLs is often logged and such data can often be harvested later by an insider threat or external attacker.”


In April, CloudSEC came across another leaking boat: Namely, AWS keys. Imperva is far from the the only business to misconfigure its AWS API, it found: in fact, 0.5 percent of [mobile apps expose their internal AWS keys](https://cloudsek.com/whitepapers_reports/mobile-apps-exposing-aws-keys-affect-100m-users-data/), affecting 100 million users’ data. “This highlights a pattern of systemic mishandling of API keys among app developers,” CloudSEK said last week.


Below is one example CloudSEK provided of an app containing the hardcoded API key\_id and key\_secret:


What Threat Actors Can Do With API Secrets
------------------------------------------


CloudSEK noted that attackers can extract query payment information via leaked APIs. They can also revoke unauthorized transactions and gain access to a user’s PII (including phone numbers and email addresses), transaction IDs, transaction amounts, order details and refund details.


With regards to the fraud threat actors can get up to with such sensitive data, they can initiate refunds by using the compromised translation ID, according to CloudSEK.


“An adversary can make bulk purchases and then initiate refunds,” according to the researchers. “Such refunds can also lead to significant losses for the company. For example: In one of the apps we found a transaction for an amount of INR 1,82,813 along with the payment\_id. And using just these two details an adversary could carry out a refund.”


They can also sell user data on the dark web or to a competitor: “A threat actor can either dump or sell the financial information, transaction details, user PII on cybercriminal forums and dark web marketplaces. They could also share the app’s consolidated data, proprietary research, and corporate financial records as competitor intelligence to other players in the sector,” the CloudSEK researchers wrote.


Threat actors can also wield the users’ PII in social engineering schemes, scams and identity theft.


Hardcoded API Keys Are a No-No
------------------------------


Salt Security’s Isbitski noted that API keys are the equivalent of static passwords that organizations frequently use as a sole means of authentication, with IT teams failing to rotate them frequently enough, “if at all,” while engineering teams “often rely on API keys as a means of system integration or automation.”


Attackers know this full well. They know that API keys can often be found embedded within mobile apps that are easy to reverse-engineer, Isbitski said. “API keys are often hardcoded within application source code or infrastructure code, both of which are often stashed within cloud-hosted code repositories like GitHub or general-purpose cloud storage like AWS S3,” he explained. “Obtaining an API key is the equivalent of obtaining a working credential. Attackers craft requests to API endpoints using harvested API keys to gain access to data or functionality.”


API security best practices including disallowing the embedding of API keys or secrets in applications or code, given how easily they can be harvested by attackers.


“API keys alone are not intended as a means of authentication,” he continued. “API keys must be paired with other authentication and authorization material to provide strong access control” – an issue that Salt Security tackled in its recently published [API Security Best Practices](https://content.salt.security/wp-api-security-best-practices.html).


Attackers regularly steal credentials or hijack authenticated sessions through a variety of techniques including social engineering, phishing, person-in-the-middle attacks and by reverse engineering code, he iterated. Thus, another aspect of API security best practices is strong access control, as well as runtime behavior analysis that can detect and stop events when authentication material is compromised and, in turn, used to abuse APIs.


***Rule #1 of Linux Security:** No cybersecurity solution is viable if you don’t have the basics down. [**JOIN**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the [**4 Golden Rules of Linux Security**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar). Your top takeaway will be a Linux roadmap to getting the basics right! [**REGISTER NOW**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.*




#### Tags:
[[API]] [[apps]] [[CloudSEK]] [[Razorpay]] [[AWS]] [[Linux]] [[CloudSEK’s]] [[data.]] [[hardcoded]] [[cloud]] [[ThreatPost]]
