# Terrorist Watchlist Exposed Online with Nearly 1.9M Records
### A researcher discovered a data cache from the FBI’s Terrorist Screening Center left online without a password or authentication requirement.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168737)
+ Date: August 17, 2021  10:46 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/01/05170820/cloud_web_app.jpg)
A researcher has revealed the discovery of a federal terrorist watchlist that includes 1.9 million records, which were available online without any security protections. The data remained exposed for three more weeks even after the Department of Homeland Security (DHS) was informed about it.


Volodymyr Diachenko, who goes colloquially as “Bob” and is head of security research at Comparitech, found the records “without a password or any other authentication required to access it” on July 19, he revealed [in a post on LinkedIn](https://www.linkedin.com/pulse/americas-secret-terrorist-watchlist-exposed-web-report-diachenko/).


“The watchlist came from the Terrorist Screening Center, a multi-agency group administered by the FBI,” he wrote in the post. “The TSC maintains the country’s no-fly list, which is a subset of the larger watchlist.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The no-fly list is a list of individuals that the federal government considers dangerous or capable of terrorist activity who should not be allowed to board a commercial airliner.


“A typical record” in the list discovered by Diachenko included the full name, citizenship, gender, date of birth, passport number, no-fly indicator and more information of the suspected terrorist, he said. Diachenko posted [a screenshot](https://twitter.com/MayhemDayOne/status/1417174479323680775) with information redacted from the list, on his Twitter feed.



> 
> Apparently, this is the TSC (Terrorist Screening Centre) dataset publicly exposed (tsc\_id is the only clue), with 1.9M+ records. In any case, any thoughts as of where to responsibly report? [pic.twitter.com/e31pSrHnoM](https://t.co/e31pSrHnoM)
> 
> 
> — Bob Diachenko (@MayhemDayOne) [July 19, 2021](https://twitter.com/MayhemDayOne/status/1417174479323680775?ref_src=twsrc%5Etfw)
> 
> 



“The exposed Elasticsearch cluster contained 1.9 million records,” he said. “I do not know how much of the full TSC Watchlist it stored, but it seems plausible that the entire list was exposed.”


Diachenko said he immediately reported the exposed database — which was found on a Bahrain IP address, not a U.S. one — to DHS officials, who appeared somewhat dismissive, he said.


Officials “acknowledged the incident and thanked me for my work” without providing “further official comment,” Diachenko wrote in his post.


**Exposure of Sensitive Data**
------------------------------


The TSC, created after 9/11, is a multi-agency center managed by the FBI. The center is meant to be the U.S. government’s “consolidated counterterrorism watchlisting component,” according to [its website](https://www.fbi.gov/about/leadership-and-structure/national-security-branch/tsc).


The center manages and operates the Terrorist Screening Database, commonly known as “the watchlist,” which is “a single database that contains sensitive national-security and law-enforcement information” aimed at keeping track of all the individuals the feds have targeted for potential terrorist activity, according to the site.


“The TSC uses the watchlist to support front-line screening agencies in positively identifying known or suspected terrorists who are attempting to obtain visas, enter the country, board an aircraft or engage in other activities,” according to the TSC website.


The exposed server that hosted the watchlist was indexed by search engines Censys and ZoomEye, Diachenko said. After discovering it on July 19, he reported it to the DHS on the same day. However, the exposed server wasn’t taken down until about three weeks later, on Aug. 9, he said.


“It’s not clear why it took so long, and I don’t know for sure whether any unauthorized parties accessed it,” Diachenko said.


**Potentially Harmful Scenario**
--------------------------------


Indeed, access by an unauthorized person or persons could be potentially detrimental for those on the list, who are suspected of terrorism but “have not necessarily been charged with any crime,” he noted.


“In the wrong hands, this list could be used to oppress, harass or persecute people on the list and their families,” Diachenko wrote. “It could cause any number of personal and professional problems for innocent people whose names are included in the list.”


Indeed, with the recent headlines about organizations and governments [using](https://threatpost.com/nso-group-data-pegasus/167897/) Israeli firm NSO Group’s Pegasus spyware to target activists, journalists, business executives and [politicians](https://threatpost.com/french-launch-nso-probe-after-macron-believed-spyware-targe/167986/) on a widespread level, it’s not unusual to imagine that people targeted on the watchlist who may well be innocent could also be caught up in similar campaigns.


The exposure also once again highlights the importance of ensuring any information stored on the cloud or a public-facing internet server be configured and secured properly to avoid inadvertent data leaks and nefarious campaigns that leverage that data, said Saumitra Das, CTO and co-founder of cloud security firm Blue Hexagon.


“Exposure of records through misconfiguration is a major issue whether we are talking about public cloud misconfigurations or of any service exposed to the internet,” he said in an email to Threatpost. “Organizations needs to continuously monitor all resources deployed in their enterprise to minimize risks of such exposure. Such records can be sold on the dark web or used for further attacks especially if credentials are involved.”


**Worried about where the next attack is coming from? We’ve got your back.**[**REGISTER NOW**](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**for our upcoming live webinar,**[**How to Think Like a Threat Actor**](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**, in partnership with Uptycs. Find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on Aug. 17 at 11AM EST for this**[**LIVE**](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**discussion.**


 




#### Tags:
[[Diachenko]] [[said.]] [[watchlist]] [[TSC]] [[“The]] [[no-fly]] [[list,]] [[cloud]] [[ThreatPost]]
