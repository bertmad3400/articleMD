# Artwork Archive cloud storage misconfiguration exposed user data, revenue records
### An unsecured bucket exposed PII and sales information.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/artwork-archive-cloud-storage-misconfiguration-exposed-user-data-revenue-records/)
+ Date: July 16, 2021 -- 13:00 GMT (14:00 BST)
+ Author: Charlie Osborne


## Article:
Unknown

A platform used to connect artists and potential buyers leaked the personally identifiable information (PII) of users, researchers say. 


On Friday, the WizCase team, led by Ata Hakçıl, said that misconfigurations in an Amazon S3 bucket belonging to Artwork Archive exposed over 200,000 files. 

Based in Denver, Colorado, Artwork Archive is marketed as a platform to "give artists, collectors, and organizations a better way to manage their art." Software solutions are offered on a subscription basis to manage both the purchase and sale of artwork. 

The security researchers [discovered the bucket](https://www.wizcase.com/blog/artworkarchive-breach-report), which did not require any authentication to access, on May 23.

In total, 421GB of data was exposed. Dating back to August 2015, the records related to over 7,000 artists, collectors, and galleries, and "potentially their customers, too," according to WizCase. Data available to view included full names, physical addresses, and email addresses.  

Purchase details, too, were exposed. WizCase found approximately 9,000 invoices, as shown below, including the price of artwork and sales agreements, alongside revenue reports. 

![screenshot-2021-07-15-at-10-48-59.png]()![screenshot-2021-07-15-at-10-48-59.png](https://www.zdnet.com/a/hub/i/r/2021/07/15/e3dd47e4-86a8-46ae-8fe6-2faab0064456/resize/470xauto/b9456c6f5f56e68dc60df2ee152d2262/screenshot-2021-07-15-at-10-48-59.png)
 WizCase
 ![screenshot-2021-07-16-at-08-36-22.png]()![screenshot-2021-07-16-at-08-36-22.png](https://www.zdnet.com/a/hub/i/2021/07/16/c9c0888c-e39b-4f18-97b7-3a5c26ba5bd0/screenshot-2021-07-16-at-08-36-22.png)
 WizCase
 In addition, "exported contacts" were stored in the bucket, containing full names, phone numbers, email addresses, city and country, and company affiliations of individuals.






"These were usually contacts an artist added to Artwork Archive via their contact management feature and included art institutions, individual artists, art collectors, friends, and family," the researchers say.  

Finally, WizCase discovered inventory reports which listed artwork owned by "specific artists, buyers, and galleries."  

Artwork Archive was made aware of the security issue on May 23 and secured the storage system three days later, on May 26.  

ZDNet has reached out to Artwork Archive and we will update when we hear back.  

###  Previous and related coverage

* [Guess announces breach of employee SSNs and financial data after DarkSide ransomware attack](https://www.zdnet.com/article/guess-announces-breach-of-employee-ssns-and-financial-data-after-darkside-attack/)  

* [Oil giant Shell discloses data breach linked to Accellion FTA vulnerability](https://www.zdnet.com/article/oil-giant-shell-discloses-data-breach-linked-to-accellion-fta-vulnerability/)  

* [T-Mobile discloses its fourth data breach in three years](https://www.zdnet.com/article/t-mobile-discloses-its-fourth-data-breach-in-three-years/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[WizCase]] [[000]] [[ZDNet]]
