# A Guide to Doing Cyberintelligence on a Restricted Budget
### Cybersecurity budget cuts are everywhere. Chad Anderson, senior security researcher at DomainTools, discusses alternatives to fancy tooling, and good human skills alignment.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175574)
+ Date: October 19, 2021  11:12 am
+ Author: Chad Anderson


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/19100940/checklist2-e1634652595388.jpg)
For those in the industry, it comes as no surprise that many cybersecurity programs have been impacted by loss of revenue during the pandemic. From cutting tooling and feed budgets to reduction in staff, it’s been challenging at best.


In a recent [SANS 2021 survey](https://www.domaintools.com/resources/survey-reports/sans-2021-threat-hunting-survey?utm_source=ThreatPost&utm_campaign=Byline), “Threat Hunting In Uncertain Times,” we were shown that 11 percent of organizations have had their threat-hunting and intelligence programs impacted by the pandemic, with 12 percent of the organizations polled stopping their hunting programs altogether. With ransomware affiliate actions on the rise and organizations constantly under the target of business email compromise (BEC) scams, this is a horrible time to be stuck with a shrinking budget.


In light of this, we’re going to go through some broad suggestions and checklists for how to do 80 percent of what you need to do on the cyberintelligence front, at just 20 percent of the typical cost for an enterprise program.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


**Wrap in Open-Source Resources**
---------------------------------


Luckily, as security vendors have matured the capability of enterprise products, so too has the maturity of community projects grown. Couple those free and open technologies with the dedicated time of an analyst or researcher, and you have a viable alternative for a low-budget team.


Stress must be placed on viable in this case, and it’s important to note that you should bring up with your leadership the fact that managing your own tooling comes with the price of human hours.


Many of the free and open-source tools are not as easy to work with or have poor integrations and therefore require the dedicated time of a more skilled member of your team to build some of that operational glue. That said, a lot can be learned, and skill sets matured, from not having your intelligence feeds handed to your team members on a silver platter.


 


With this in mind, there are a couple of guidelines that should be observed if you need to operate on a restricted budget.


Once you have fully fleshed out your budget and tooling needs, it’s then time to make decisions for the people power/resources to manage those tools.


**Aligning Human Resources and Skill Sets**
-------------------------------------------


Threat-intelligence teams are often composed of people from varying backgrounds. The skills required involve the networking fundamentals that would come with being a systems administrator, the research and writing methodologies of a journalist, the automation chops of a programmer, and the reverse engineering skills of a malware analyst. It’s rare to have someone on your team who does all of the above, so taking the strengths of each team member into account when deciding who manages what is crucial.


The harder piece to operate in all this will be your knowledge management, commonly referred to as threat intelligence platforms (TIPs). You can get away with spreadsheets to an extent, but your team will eventually have too much data to manage and require a dedicated tool.


Open-source tools like MISP, The Hive or OpenCTI have lots of moving parts with typically an application layer served up and backed by a database, coupled often with a document store as well. For these sorts of applications, you’ll want a team member with infrastructure management and operations experience — because there will likely be a need to tweak configuration values and appropriately size machines for your workload.


If there isn’t someone on your team with that skill set, then you may want to look to join a community MISP instance or one of the other open threat-sharing platforms with a free tier. Some of those will even have the next critical piece of enrichment included.


On the easier end to operate will be your enrichment capabilities. Indicator enrichment is one of the places where open-source tooling really shines, as tools like IntelOwl and Cortex have become increasingly mature; and companies are now producing their own plugins that allow enrichment.


Both of those tools run easily through Docker, and don’t require much in the way of a production level database. This is because once your enrichments have been moved into your knowledge store, there isn’t much of a reason to keep the enrichment job itself around. If this service goes down and comes back up missing jobs from a month ago this isn’t a large impact to your team.


These applications are a good spot for someone that wants to get programming and light infrastructure experience, because of their relative ease to set up. The harder portion will be connecting those enriched pieces into your TIP. There’s a number of ways to do this, depending on the tool with both of the aforementioned tools automatically feeding enrichments into multiple open-source TIPs.


Once you have divided up those two main tool sets amongst your team there are a few things you’ll want to keep in mind running your own infrastructure:


When it comes to running your infrastructure in-house there are a number of different tools that can get your team most of the way to enterprise-level products. While this venture will take a certain amount of human hours, taking away from time analysts could be researching threats, that cost tradeoff may be what your group needs to continue being effective under a constricted budget.


***Chad Anderson is a senior security researcher with DomainTools.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[it’s]] [[budget.]] [[open-source]] [[isn’t]] [[ThreatPost]]
