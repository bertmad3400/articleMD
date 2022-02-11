# Amazon steps in to close exposed FlexBooker bucket after December data breach | ZDNet
### vpnMentor said FlexBooker's AWS S3 bucket held information about COVID-19 tests, babysitters and pet euthanizations.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/amazon-steps-in-to-close-exposed-flexbooker-bucket-after-december-data-breach/
+ Date: 2022-02-11 15:37:46
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/3ee8fc6b7bbeb64052de803cfdf568492eb0e045/2020/02/28/9d07c878-7f1a-4287-997c-1e8c522a108f/istock-1159096313.jpg?width=770&height=578&fit=crop&auto=webp)

Digital scheduling platform FlexBooker [has been accused](https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.vpnmentor.com%2Fblog%2Freport-flexbooker-leak%2F&data=04%7C01%7Cjonathan.greig%40zdnet.com%7Ca07996598afd4a10d9fd08d9ed67858c%7C4289d6102cfd46218c9644a1518ddb0a%7C0%7C0%7C637801852900868016%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=zzdixrn%2FFIQhhZ871bb0KNFdX%2BFq24067cIb6MT0zsU%3D&reserved=0) of exposing the sensitive data of millions of customers, according to security researchers at vpnMentor.

The researchers said the Ohio-based tech company was using an AWS S3 bucket to store data but did not implement any security measures, leaving the contents totally exposed and easily accessible to anyone with a web browser.

The 19 million exposed files included full names, email addresses, phone numbers and appointment details. 

FlexBooker did not respond to requests for comment from *ZDNet* but vpnMentor said they contacted the company and Amazon about the issue.

"We did contact them in January, to which they sent what seemed to be an automatic reply about the leak that affected them in December. We tried to explain it was a new breach, but didn't hear back," a vpnMentor spokesperson said. "Which is why we decided to contact AWS directly (as Flexbooker wrote on their site they were working together with Amazon), and soon after the bucket was secured (Amazon probably informed Flexbooker, as Amazon isn't supposed to do it themselves)."

In January, FlexBooker [apologized for a data breach](https://www.zdnet.com/article/flexbooker-apologizes-for-breach-of-3-7-million-user-records-credit-card-information/) that involved the sensitive information of 3.7 million users. At the time, the company told *ZDNet*a portion of its customer database had been breached after its AWS servers were compromised on December 23. FlexBooker said their "system data storage was also accessed and downloaded" as part of the attack. 

They [added](https://www.flexbooker.com/data-breach) they worked with Amazon to restore a backup and they were able to bring operations back in about 12 hours. 






"We sent a notification to all affected parties and have worked with Amazon Web Services, our hosting provider, to ensure that our accounts are re-secured," a spokesperson said. "We deeply apologize for the inconvenience caused by this issue."

Researchers at vpnMentor said they were not aware of this data breach as they scanned the internet for potential vulnerabilities in December. By January 23, vpnMentor confirmed the latest issue and contacted FlexBooker on January 25. Amazon was contacted the same day and by January 26, Amazon had resolved the issue. 

"Flexbooker's misconfigured AWS account contained over 19 million HTML files which exposed what seemed to be automated emails sent via FlexBooker's platform to users. This means potentially up to 19 million people were exposed, depending on how many people made multiple bookings on a website using Flexbooker," the researchers said in the report. 

"Each email appeared to be a confirmation message for bookings made via the platform, and exposed both the FlexBooker account holder and the person(s) who made a booking. For example, a plumbing supply company was using FlexBooker to schedule consultations between employees and customers. In this instance, PII data for both people were exposed."

![screen-shot-2022-02-11-at-10-22-31-am.png]()![screen-shot-2022-02-11-at-10-22-31-am.png](https://www.zdnet.com/a/img/resize/edaba745ae76981d11c8bb68ea6ef8d99927e6ed/2022/02/11/c0c55304-26b4-4ce4-a8c3-bf1d6c6bbac4/screen-shot-2022-02-11-at-10-22-31-am.png?width=470&fit=bounds&format=pjpg&auto=webp)One of the appointments exposed by FlexBookers platform. 


 vpnMentor
 The leaks are alarming because they included links with unique codes that could be used to create cancellation links, edit links, and view the appointment details that were hidden in the emails.

The S3 bucket was also live when vpnMentor discovered it, meaning it was constantly being updated with new information, exposing more and more people every day. 

vpnMentor included screenshots of the appointments, which ranged from COVID-19 tests to pet euthanizations and babysitting appointments. The babysitting emails exposed the sensitive information of children as well. 

"A few days after the breach was secured, we observed hackers on the dark web once again selling private data apparently owned by Flexbooker. It's not clear if this was from the previous breach, the one our team discovered, or a mix of both. However, it shows the risk for companies who don't adequately secure their users' data and how quickly hackers can get stolen data out into the open," the researchers explained. 

In January, Australian security expert Troy Hunt, who runs the [Have I Been Pwned](https://haveibeenpwned.com/) site that tracks breached information, [said](https://twitter.com/haveibeenpwned/status/1478980347631001602) the first trove of stolen data included password hashes and partial credit card information for some accounts. Hunt added that the data "was found being actively traded on a popular hacking forum."

A FlexBooker spokesperson confirmed Hunt's report, telling *ZDNet*that the last 3 digits of card numbers were included in the breach but not the full card information, expiration date, or CVV. 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Australia]] [[victim.continent.name=Oceania]] [[victim.country.name=Australia]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Flexbooker]] [[Vpnmentor]] [[Aws]] [[Flexbooker]] [[Zdnet]] [[ZDNet]]

