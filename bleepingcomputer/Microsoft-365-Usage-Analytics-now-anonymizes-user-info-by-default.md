# Microsoft 365 Usage Analytics now anonymizes user info by default
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-365-usage-analytics-now-anonymizes-user-info-by-default/)
+ Date: August 31, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft 365 Usage Analytics now anonymizes user info by default](https://www.bleepstatic.com/content/hl-images/2021/08/31/Microsoft-365.jpg)


Microsoft has announced today that it will start anonymizing user-level info by default Microsoft 365 Usage Analytics beginning with September 1, 2021.


"At Microsoft, we're committed to both data-driven insights and user privacy," said James Bell, Senior Product Marketing Manager for Microsoft 365 Product Marketing & Growth Strategy.


"As part of that commitment, we're making a change to Microsoft 365 usage analytics on September 1st to pseudonymize user-level information by default."


As Bell explained, Redmond will anonymize the users' data through a pseudonymization de-identification procedure where identifiable record fields are replaced with artificial data to remove identifying details.


Pseudonymization is a data management process recommended by the European Union's General Data Protection Regulation (GDPR) to enhance users' privacy.


[Microsoft 365 Usage Analytics](http://docs.microsoft.com/en-us/microsoft-365/admin/usage-analytics/usage-analytics) provides a dashboard with pre-built usage insights reports that can be used to keep track of adoption trends of Microsoft 365 services and apps within your organization.


These incoming changes will impact user info across multiple products and APIs, including: 


* [Microsoft 365 Reports in the Microsoft 365 admin center](https://docs.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports?view=o365-worldwide)
* [Microsoft 365 usage reports in Microsoft Graph](https://docs.microsoft.com/en-us/graph/api/resources/report?view=graph-rest-1.0)
* [Microsoft Teams analytics and reporting](https://docs.microsoft.com/en-us/microsoftteams/teams-analytics-and-reports/teams-reporting-reference) in the Microsoft Teams admin center
* The reportRoot: getSharePointSiteUsageDetail API ([1.0](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fgraph%2Fapi%2Freportroot-getsharepointsiteusagedetail%3Fview%3Dgraph-rest-1.0&data=04%7C01%7CJames.Bell%40microsoft.com%7C0c64cee0adba420dcca808d96862aaed%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637655595288810795%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=hr46pIM4MKBLwQuPtx4VdjrVEvpoVn6i36EpYrunpFU%3D&reserved=0) and [beta](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fgraph%2Fapi%2Freportroot-getsharepointsiteusagedetail%3Fview%3Dgraph-rest-beta&data=04%7C01%7CJames.Bell%40microsoft.com%7C0c64cee0adba420dcca808d96862aaed%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637655595288820748%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=rFxEpGKknq7e0k5tjEh%2FFexHkA3iDkT1sc%2BM7Z6jhtM%3D&reserved=0)) for SharePoint site detail


While enabled by default starting tomorrow in all tenants, global admins can show identifiable user information if their organization's privacy practices allow it.


This can be done by going into the Microsoft 365 admin center to Settings > Org Settings > Services > Reports and selecting 'Show identifiable user information in reports' under 'Choose how to show user information.'


"When user identification is enabled, administrative roles and the report reader role will be able to see identifiable user level information. Global reader and Usage Summary Reports Reader roles will not have access to identifiable user information, regardless of the setting chosen.," [Bell added](https://techcommunity.microsoft.com/t5/microsoft-365-blog/privacy-changes-to-microsoft-365-usage-analytics/ba-p/2694137).


"These changes to the product will bolster privacy for users while still enabling IT professionals to measure adoption trends, track license allocation and determine license renewal in Microsoft 365."




#### Tags:
[[Microsoft]] [[Bleeping Computer]]
