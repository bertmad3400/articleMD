# Google's new tool helps you find abandoned cloud projects and delete them
### Google's Unattended Project Reminder helps identify and eliminate unattended cloud projects that could become a security risk.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/googles-new-tool-helps-you-find-abandoned-cloud-projects-and-delete-them/)
+ Date: August 9, 2021 -- 09:45 GMT (10:45 BST)
+ Author: Liam Tung


## Article:
Unknown

Google's Unattended Project Reminder feature has moved to a public preview and aims to improve cloud utilization, and address security issues caused by forgotten old cloud-computing projects that shouldn't be around anymore. 

Unattended Project Reminder, a part of Google Cloud's [Active Assist](https://cloud.google.com/solutions/active-assist), could be useful in reducing security risks by finding those old initiatives, such as a prototyping project, that no longer require network access, cloud resources, or supported APIs. 


Google has developed the feature through 2021 as part of a prototype aimed at cleaning up internal projects that were unattended. 

**SEE:** [**Google's new cloud computing tool helps you pick the greenest data centers**](https://www.zdnet.com/article/googles-new-cloud-computing-tool-helps-you-pick-the-greenest-data-centers/)

Google's internal security team had the issue of unattended projects on the radar for some time, according to Google Cloud, so the two units started searching for unattended cloud projects within the "[google.com](http://google.com)" organization.    

Despite being a good idea, Google ran into detection problems because it was difficult to use signals – such as API, network and user activity – to tell the difference between an actually unattended project and a project that intentionally has a low level of activity. 

Risks here include correctly identifying unattended projects, and accidentally deleting a component that was essential to a production workload, thus inadvertently causing permanent data loss. But benefits include reducing cloud bills for unnecessary resources and reducing configuration issues, such as open firewalls or privileged service account keys that attackers can exploit to get a hold of your cloud resources for cryptocurrency mining or to steal data.






"These security risks tend to grow over time because the latest best practices and patches are usually not applied to unattended projects," Googe said.

To address these issues, it worked with customers using real-life data to find thousands of unattended projects.

Key signals that Unattended Project Reminder uses include API activity (such as service accounts with authentication activity and API calls consumed), networking activity, billing activity, user activity, and cloud services usage (such as active VMs, BigQuery jobs, and storage requests). 

"Based on these signals, it can generate recommendations to clean up projects that have low usage activity (where "low usage" is defined using a machine learning model that ranks projects in your organization by level of usage), or recommendations to reclaim projects that have high usage activity but no active project owners," [explain Google Cloud product managers, Dima Melnyk and Bakh Inamov](https://cloud.google.com/blog/products/identity-security/google-cloud-launches-unattended-project-recommender). 

**SEE:** [**Attacks on critical infrastructure are dangerous. Soon they could turn deadly, warn analysts**](https://www.zdnet.com/article/attacks-on-critical-infrastructure-are-dangerous-soon-they-could-turn-deadly-warns-analyst/)

Insights and recommendations can be sent automatically via email or chat messages to project owners.  

Admins have a recovery option for accidentally removed projects: the recovery period is 30 days. However, Google notes some resources, such as Cloud Storage or Pub/Sub resources, are deleted before the 30-day period ends, and may not be fully recoverable.

French sporting goods retail giant Decathlon used the feature to delete 775 projects. "And no one complained," said Adeline Villette, Decathlon's cloud security officer. 

French utility [Veolia](https://www.veolia.com/) and US file storage firm Box trialed the technology to reduce the number of unattended projects they were respectively supporting.





#### Tags:
[[Google]] [[cloud]] [[Cloud]] [[resources,]] [[activity,]] [[ZDNet]]
