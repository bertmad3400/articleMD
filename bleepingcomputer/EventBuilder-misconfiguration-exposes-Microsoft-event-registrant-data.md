# EventBuilder misconfiguration exposes Microsoft event registrant data
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/eventbuilder-misconfiguration-exposes-microsoft-event-registrant-data/)
+ Date: September 20, 2021
+ Author: Ionut Ilascu


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/08/24/database-header.jpg)


Personal details of registrants to virtual events available through the EventBuilder platform have stayed accessible over the public internet, open to indexing by various engines.


EventBuilder is a software solution for creating virtual events (webinars, training, online learning, conferences) using Microsoft technologies and integrates with Microsoft Teams and Teams Live Events extension.



The platform is a member of the Microsoft Supplier Program and is used by Microsoft to [host events](https://www.microsoft.com/en-us/us-partner-blog/location/online-3/) for external audiences.


### Microsoft event registrant's data


A report from security researcher Bob Diachenko in partnership with Clario Tech reveals that [EventBuilder](https://www.eventbuilder.rocks/) exposed more than one million CSV and JSON files with personal information belonging to registrants to events through Microsoft Teams.


Publicly exposed details included full names, email addresses, company names and registrant’s position, phone numbers, and questionnaire feedback. The data was discovered using the [Grayhat Warfare](https://buckets.grayhatwarfare.com/) search engine.


A "registrant summary" was also present in the leaked data, which revealed information about the event, such as its name, date, tags, and if the registrant participated or not.



![EventBuilder webinar registrant data leak](https://www.bleepstatic.com/images/news/u/1100723/2021/EventBuilderLeak04_ClarioTech.jpg)source: [Clario Tech](https://clario.co/blog/eventbuilder-data-exposure/)
Looking for details about "Supercharge key workflows with apps in Teams" event, we found it was part of the [Microsoft Teams Chalk Talks](https://docs.microsoft.com/en-us/MicrosoftTeams/chalk-talks-landing-page)  program and it was a [presentation from Abbie Sweeney](https://adoption.microsoft.com/virtual-hub/microsoft-teams-365-developer-platform/microsoft-teams-platform/supercharge-key-workflows-with-apps-in-teams/), Teams Program Manager.


Diachenko shared with BleepingComputer some screenshots showing the type of data exposed, redacted to protect the privacy of the registrants:



![EventBuilder webinar registrant data leak](https://www.bleepstatic.com/images/news/u/1100723/2021/EventBuilderLeak02_Diachenko.png)source: [Bob Diachenko](https://mobile.twitter.com/MayhemDayOne)
The data was discovered on June 10 and reported responsibly on the same day. EventBuilder acknowledged the report and fixed the issue but did not make a comment about it, Diachenko told BleepingComputer.


The total number of records leaked remains unknown but as seen from the screenshot below, the exposed CSV and JSON files are pretty large-sized.



![EventBuilder webinar registrant data leak](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)source: [Bob Diachenko](https://mobile.twitter.com/MayhemDayOne)
Based on this, Diachenko’s conservative estimation is that hundreds of thousands of participants are potentially impacted.


The exposed data was present on Microsoft Azure Blob Storage, which is Microsoft’s cloud-based object storage solution. In their report, Diachenko and Clario Tech say that the storage was meant to host recorded sessions and provide access to them via a link.


Only this data was supposed to be publicly available. However, the organizers of the webinar also included registrants’ information in the same blob, thus exposing sensitive details to anyone with the correct link.


Since EventBuilder is also used by Microsoft, Diachenko says that this data leak makes for “an interesting case study in how even the most advanced technology companies can expose themselves to data vulnerabilities.”




#### Tags:
[[Microsoft]] [[Diachenko]] [[EventBuilder]] [[Teams]] [[Clario]] [[source:]] [[Bleeping Computer]]
