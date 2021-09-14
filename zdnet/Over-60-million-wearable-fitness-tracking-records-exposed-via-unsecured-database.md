# Over 60 million wearable, fitness tracking records exposed via unsecured database
### Data sources included Apple's HealthKit and Fitbit.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/over-60-million-records-exposed-in-wearable-fitness-tracking-data-breach-via-unsecured-database/)
+ Date: September 13, 2021 -- 16:06 GMT (17:06 BST)
+ Author: Charlie Osborne


## Article:
Unknown

An unsecured database containing over 61 million records related to wearable technology and fitness services was left exposed online. 


On Monday, WebsitePlanet, together with cybersecurity researcher Jeremiah Fowler, [said the database](https://www.websiteplanet.com/blog/gethealth-leak-report/) belonged to GetHealth.  

Based in New York, GetHealth describes itself as a "unified solution to access health and wellness data from hundreds of wearables, medical devices, and apps." The firm's platform is able to pull health-related data from sources including Fitbit, Misfit Wearables, Microsoft Band, Strava, and Google Fit.  

On June 30, 2021, the team discovered a database online that was not password protected.  

The researchers said that over 61 million records were contained in the data repository, including vast swathes of user information -- some of which could be considered sensitive -- such as their names, dates of birth, weight, height, gender, and GPS logs, among other datasets.  

While sampling a set of approximately 20,000 records to verify the data, the team found that the majority of data sources were from Fitbit and Apple's HealthKit. 

![screenshot-2021-09-13-at-17-02-11.png]()![screenshot-2021-09-13-at-17-02-11.png](https://www.zdnet.com/a/hub/i/r/2021/09/13/2502605f-f01a-4c0b-aefc-e59b585bea7b/resize/1200xauto/e9b3d01cacdbd1ca27db6019f23b1709/screenshot-2021-09-13-at-17-02-11.png)
 WebsitePlanet
 "This information was in plain text while there was an ID that appeared to be encrypted," the researchers said. "The geo location was structured as in "America/New\_York," "Europe/Dublin" and revealed that users were located all over the world." 

![screenshot-2021-09-08-at-15-18-57.png]()![screenshot-2021-09-08-at-15-18-57.png](https://www.zdnet.com/a/hub/i/r/2021/09/08/eaa5f48a-cf2f-4982-b1ec-7b5133fe0423/resize/1200xauto/f42d13862bff6bd4aa0685db2644a739/screenshot-2021-09-08-at-15-18-57.png)
 WebsitePlanet
 




"The files also show where data is stored and a blueprint of how the network operates from the backend and was configured," the team added. 

References to GetHealth in the 16.71 GB database indicated the company was the potential owner, and once the data had been validated on the day of discovery, Fowler privately notified the company of his findings. GetHealth responded rapidly and the system was secured within a matter of hours. On the same day, the firm's CTO reached out, informed him that the security issue was now resolved, and thanked the researcher.  

"It is unclear how long these records were exposed or who else may have had access to the dataset," WebsitePlanet said. "[...] We are not implying any wrongdoing by GetHealth, their customers, or partners. Nor, are we implying that any customer or user data was at risk. We were unable to determine the exact number of affected individuals before the database was restricted from public access." 

ZDNet has reached out to GetHealth with additional queries and we will update when we hear back. 


###  Previous and related coverage

* [Chinese developers expose data belonging to Android gamers](https://www.zdnet.com/article/chinese-developers-expose-data-belonging-to-android-gamers/)  

* [Unsecured servers and cloud services: How remote work has increased the attack surface that hackers can target](https://www.zdnet.com/article/unsecured-servers-and-cloud-services-how-remote-work-has-increased-the-attack-surface-that-hackers-can-target/)  

* [23,600 hacked databases have leaked from a defunct 'data breach index' site](https://www.zdnet.com/article/23600-hacked-databases-have-leaked-from-a-defunct-data-breach-index-site/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0 



---





#### Tags:
[[GetHealth]] [[WebsitePlanet]] [[ZDNet]]
