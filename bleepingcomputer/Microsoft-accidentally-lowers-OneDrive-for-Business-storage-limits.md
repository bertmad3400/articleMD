# Microsoft accidentally lowers OneDrive for Business storage limits
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-accidentally-lowers-onedrive-for-business-storage-limits/)
+ Date: August 26, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft accidentally lowers OneDrive for Business storage limits](https://www.bleepstatic.com/content/hl-images/2021/05/19/OneDrive.jpg)


Microsoft is investigating an ongoing issue impacting OneDrive for Business customers and causing their storage space to shrink down to the default setting or switching them to read-only mode, forcing some [to delete files](https://twitter.com/CleanthisCon/status/1430864574299975682) to free up space to work on their projects.


[OneDrive for Business](https://www.microsoft.com/en-ww/microsoft-365/onedrive/onedrive-for-business) is a cloud storage and file sharing service for enterprise customers (part of Office 365 or SharePoint Server) that allows users to access, share, and collaborate on personal and shared work files across Microsoft 365.


According to Microsoft, more than 85 percent of all Fortune 500 companies use the OneDrive for Business file storage and sharing platform.


Storage limits accidentally lowered
-----------------------------------


"We’re investigating an issue in which users' OneDrive for Business storage limits are lower than expected," the company [shared](https://twitter.com/MSFT365Status/status/1430862920863322114) via its Microsoft 365 Status Twitter account. "Additional information will be provided in the admin center under OD280960."


From diagnostic logs gathered to isolate the root cause of the incident, Microsoft found that "an exception is not recognizing user licenses and reverting the storage quota limit to the default settings of 1TB."


According to the incident ticket, some users' accounts may have also been switched to read-only mode, preventing them from making changes to their files.


"For any content which exceeds the 1TB storage quota, users may only be able to see their content in read-only mode," the company explained.


The company's engineers are working on changing how the storage quota is being calculated to mitigate this ongoing issue.


As a workaround, admins can set individual quotas for all impacted users in their environment using the steps detailed [here](https://docs.microsoft.com/en-us/onedrive/change-user-storage).


In the last published update, Microsoft said its engineers are analyzing tenants' change log per tenant, aligning the users' quotas to the users' licenses, and reverting each affected users' quotas to their previously set states.




> 
> We’re investigating an issue in which users' OneDrive for Business storage limits are lower than expected. Additional information will be provided in the admin center under OD280960.
> 
> 
> — Microsoft 365 Status (@MSFT365Status) [August 26, 2021](https://twitter.com/MSFT365Status/status/1430862920863322114?ref_src=twsrc%5Etfw)


Microsoft has recently announced [price increases](https://www.microsoft.com/en-us/microsoft-365/blog/2021/08/19/new-pricing-for-microsoft-365/) for Office 365 and Microsoft 365 plans, after a decade since Office 365 was launched, and has grown to more than 300 million commercial paid seats.


"This updated pricing reflects the increased value we have delivered to our customers over the past 10 years," said Jared Spataro, Corporate Vice President for Microsoft 365, one week ago.


*This is a developing story ...*




#### Tags:
[[Microsoft]] [[OneDrive]] [[read-only]] [[Bleeping Computer]]
