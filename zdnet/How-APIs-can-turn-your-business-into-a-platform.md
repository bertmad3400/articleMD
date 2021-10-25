# How APIs can turn your business into a platform
### APIs are the new normal. They offer a lot of potential, drive innovation, save cost, and allow developers to self-serve their needs.  But there's a lot more to building great APIs than simply coding.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/how-apis-can-turn-your-business-into-a-platform/)
+ Date: October 25, 2021
+ Author: Anton Kravchenko


## Article:
Unknown

Market, technology, and legislative trends have created needs across all industry verticals to create and consume APIs. The mandate of an API economy is clear -- the question that IT leaders must answer is not "if", but "how?"


Having been around for decades, APIs today define the new normal. They decompose software monoliths and transform businesses by bridging the gap between new and old applications. More companies are funding digital transformational programs with APIs at the core of their strategy. IDC predicts that overall spending on these projects will reach a historic high totaling [$6.8 trillion between 2020 and 2023](https://www.idc.com/getdoc.jsp?containerId=prMETA47037520). 

It is worth pointing out that this trend not only touches software companies but also applies to all industry verticals as well. In industries where API-led regulations are now standard, such as Europe's PSD2 open banking standard in financial services or FHIR for the exchange of patient information in healthcare, the digital transformation trend is accelerating. "Every company needs to become a software company" [according](https://online.sxsw.com/event/sxsw-online/planning/UGxhbm5pbmdfMzM1NTg0) to Twilio CEO Jeff Lawson. 

The API boom is here and it is happening now. With [over 24,000 APIs](http://www.programmableweb.com/apis/directory) offered by firms today according to *Programmableweb.com*, it is important to carefully consider what is entailed in a successful API strategy. In the next section, we will summarize the keys to success in the API economy, distilling key trends into lessons that integration professionals and CIOs should think about before implementing an API.

**Keys to a Successful API Strategy**
-------------------------------------

As it turns out, there is a lot more to building great APIs than simply coding. Teams must also wear a product management hat throughout the API lifecycle. 

When treating your APIs as products, the API strategy is derived from business value, customer needs, and core technology. Let's get into each of these areas in detail.

### 1. Know the Business Value

![ap-circle.png]()![ap-circle.png](https://www.zdnet.com/a/img/resize/75c17fe2110093f9aaadcadb409799fc2845ecce/2021/10/21/80982399-0e28-4907-b392-394a3011b4d8/ap-circle.png?width=370&fit=bounds&auto=webp)"The most important thing, the very first piece is to figure out what your business value is. If you don't know why you have an API, it's not likely to succeed," says Kristien Hunter, author of Irresistible APIs. 






To start, let's take a look at API business models and what kind of value they create:

* **Internal API:** private, used only by your team or by your company. This API results in indirect revenue or cost savings, for example, a team that can self-service their needs in large organizations.
* **Partner/customer API:**private, shared only with integration partners. This API creates shared or marketed revenue so other technologies in the space can complement each other.
* **External API:** public, available openly on the web. This type of API often generates direct revenue with multiple monetization strategies. For example, if it's a transactional API, the API provider may take a percentage cut of the transaction. Or, if it's a utility API, the API provider may look to a "coin-operated" model that charges a fixed rate depending on the number of API transactions.

In the [2020 State of the API report](https://www.postman.com/state-of-api/api-strategies/#api-strategies), API-first companies indicate that they allocate on average 56.96% of their APIs to address internal use-cases. According to this data, it is important to prioritize value-add over monetization, especially towards the beginning of building an API strategy. Many businesses start with internal APIs first and later make parts of their APIs publicly available, and in some cases, these external APIs become a huge revenue generator for the business. For example, *Harvard Business Review* points out [how Expedia.com generates 90%](https://hbr.org/2015/01/the-strategic-value-of-apis) of its revenue from APIs.

It is also worth pointing out that APIs enable new business models to evolve. Multiple companies are now pioneering the new [Business to Developer (B2D)](https://snipcart.com/blog/b2d-marketing-selling-to-developers) model which creates pluggable value to other companies by focusing on developers first. When starting a new business, founders might want to consider this model.

### 2. Know Your Customer

The second key to success is knowing your customer. Companies must study current and potential users to see what they need and want. A common mindset while building an API is that once you build it, your users will follow. There is, however, a better approach that involves building an API with your users, involving them as design partners. 

Early design partnerships help your team identify key use-cases, understand the skills of your API users, and most importantly, validate that your API is delivering value to your customers. Engaging your API consumers early enables your team to refine API design based on the feedback from beta testers. 

Based on the [2021 The State of API Economy Report](https://www.mulesoft.com/lp/reports/connectivity-benchmark-2021#form-section) conducted by Google, APIs enable organizations to speed up new application development (58%), connect internal applications (53%), and create a developer ecosystem (47%). These are top examples of value creation for your API customers, whether they come from an internal team seeking self-service or outside developers who innovate on top of your public API.

Knowing the skills of your users is another critical area as it provides your API consumers with the most relevant tools. Postman's [2020 State of the API report](https://www.postman.com/state-of-api/who-works-with-apis/#who-works-with-apis) indicates that full-stack developers are the most common API consumer, accounting for nearly 29% of all survey responses. However, with the advent of low-code and no-code tools, there is also an increasing number of less technical job functions starting to consume APIs, such as directors, managers, product managers, support, and UX designers. In organizations where this is happening, APIs are essentially the key to democratizing innovation and taking some of the burdens off of IT. Depending on who your users are, consider complementing your API documentation with pre-packaged SDKs or native iPaaS connectors, which can be embedded into familiar integrated development environments (IDEs) to help your users get started quickly. 

Finally, regardless of where your API consumers come from, carefully design zero trust architectures and create API gateways that manage access to your most valuable data. [Security magazine](https://www.securitymagazine.com/articles/94509-of-organizations-had-api-security-incident-last-year) reports that 91% of organizations had an API security incident last year while leading analyst Gartner, predicts that [APIs will be the most common attack vector by 2022](https://www.gartner.com/en/webinars/4002323/api-security-protect-your-apis-from-attacks-and-data-breaches#:~:text=Gartner%20predicts%20that%20by%202022,a%20wide%20range%20of%20organizations.).

### 3. Treat Your API as a Product

Once you know the business value and the customers you are serving, it is time to build your API. Start by applying a product mindset while offering the best-in-class API to your users. 

**Top-notch API Documentation:**According to the [2020 State of the API Report](https://www.postman.com/state-of-api/#key-findings), one of the most important factors individuals consider before integration with an API is documentation (70.3%). 

When crafting your API documentation, take advantage of standard API description formats such as [the OpenAPI Specification (OAS)](https://www.openapis.org/) and tools that automatically generate API documentation from these formats. Instead of creating a laundry list of API operations and technical information, embed real-world API use cases into the API portal that developers use to not only onboard themselves to your APIs, but to make their first API call. This helps developers get started quickly and helps business managers see what kind of products can be built around your API. 

**Sandboxes:**Create sandbox environments that allow your API users to kick the tires of your APIs in non-production environments. With sandboxes, developers can start experimenting within minutes of arriving at your API portal without a need to engage with outside teams. 

"I saw an example literally last week with a customer that was 40 minutes into their welcome meeting with us, where the engineer was already developing and coding in a sandbox against the API," [says Bryson Koehler](https://searchcio.techtarget.com/feature/Inside-look-at-Equifaxs-15B-digital-transformation-journey) who joined Equifax as CTO to lead $1.5 billion digital transformation efforts.

**API Launch:**Just like any product launch, carefully design a marketing strategy segmenting your audience and target those segments with the most relevant content. Create advocates and recruit top developers from across the developer community to evangelize the benefits of your APIs. 

According to [HackerEarth's study](https://www.hackerearth.com/blog/developers/drive-api-adoption-through-hackathons/), hackathons can be one of the most effective methods to acquire and engage developers for your external APIs. A well-marketed and well-executed hackathon can attract between 1500 to 3000+ developers. 

**Support:**Consider overhead that goes along with supporting an API. For example, can developers contact a human for support or should they engage in the developer community to seek answers? Internally, the feedback cycles and the information exchange are quick. But when serving outside developers, creating an incentivized community of developers is key. 

Start by establishing channels that allow API users to point out mistakes and ask questions. Some practices include direct feedback links in API documentation where developers can contribute to your API instead of reporting a new bug. 

**Measure success**Finally, every product manager sets key performance indicators (KPIs), which help your team monitor API health and connect its adoption with the value it generates for the business. Below are the minimum set of metrics each API owner should keep in mind:

1. Revenue metrics, such as ROI and customer lifetime value (CLTV) per developer.
2. Operational metrics, such as uptime and errors.
3. Developer metrics, such as net promoter score (NPS) for measuring loyalty. Also, through your web analytics, community, and documentation engagement.

**Successful API-first Stories**
--------------------------------

Now that we know what it takes to build a successful API, let's take a look at a few best-in-class API-led examples. 

### Twilio

**API model:** External API with a coin-operated business model (eg: $0.0075 to send or receive an SMS text message to a mobile phone that's provisioned by any carrier)

Twilio is a great example of a company that pioneered the API economy. During [his pitch](https://avc.com/2016/06/best-seed-pitch-ever/) in 2008, Jeff Lawson, the CEO of Twilio, said "We have taken the entire messy and complex world of telephony and reduced it to five API calls." Since that year, Twilio reached a market cap of $57.7 billion. 

Before starting Twilio, Lawson was a technical product manager at Amazon where he saw how APIs transformed the Amazon business by launching AWS as another critical business. What makes Twilio APIs unique is the full page of real-world examples on how to use the API with complete SDKs that are pluggable into a variety of popular programming languages, such as Java and Node.js.

### Stripe

**API model:** External API with transaction fee e.g. 2.9% + $0.3 per credit card charge

Stripe is a suite of payment APIs that powers commerce for online businesses. The company was founded in 2010 and is currently valued at $95 billion. When sharing the success story and key strategies, Patrick Collison, co-founder of Stripe, [says](https://startupclass.samaltman.com/courses/lec11/) "Every single API request that generated an error, went to all of our inboxes and phoned all of us."

What made Stripe so successful is a more flexible and robust payments platform. Instead of building payment transaction infrastructure in-house, companies now can integrate with Stripe's platform via an API. "Because Stripe handles all of our transaction flows, we didn't have to create an infrastructure for it or hire the people to do that. So that saved us in headcount, and it got us to market faster. We built our platform with at most three engineers working on it at one time." reported one of Stripe's customers in the [IDC report](https://stripe.com/files/payments/IDC_Business_Value_of_Stripe_Platform_Full%20Study.pdf).

### Human API

**API model:** Customer APIs with multiple pricing tiers (e.g. Clinical API, Enterprise API)

API success stories emerge in other industries too. Once COVID-19 unfolded, the healthcare institutions needed to quickly reinvent themselves, and Human API illustrated the best API-first approach to healthcare. According to [the announcement](https://www.cleared4.org/post/cleared4-partners-with-human-api-to-deliver-real-time-covid-19-test-results-that-support-safe-workpl), CLEARED4 & Human API teams partnered to deliver real-time test data to organizations that can access their employee's COVID-19 data in real-time from over 5,000 labs including Quest Diagnostics, Lab Corps and CVS.

"We knew accessing COVID-19 test results in real-time would be critical to a safe reopening of workplaces and venues across the country," said Ashley John Heather, President & COO of CLEARED4. The "library of healthcare APIs" enabled Ashley's team to seamlessly and quickly integrate COVID-19 test results into their return-to-work platform.

**Conclusion**
--------------

APIs are the new normal. They offer a lot of potential, drive innovation, save cost, and allow developers to self-serve their needs. A successful API strategy is the key to creating business value and turning a business into a platform. The strategy starts with a product mindset that sits at the intersection of business, customers, and technology. Figuring this out early fosters your business, delights customers, recruits partners, and enables your teams to quickly respond to emerging needs. 





#### Tags:
[[API]] [[API,]] [[APIs.]] [[example,]] [[API.]] [[COVID-19]] [[strategy.]] [[Twilio]] [[API:]] [[API-first]] [[ZDNet]]
