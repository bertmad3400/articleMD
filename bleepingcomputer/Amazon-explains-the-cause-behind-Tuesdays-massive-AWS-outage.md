# Amazon explains the cause behind Tuesday’s massive AWS outage
### Amazon has published a post-event summary to shed some light on the root cause behind this week's massive AWS outage that took down a long list of high-profile sites and online services, including Ring, Netflix, Amazon Prime Video, and Roku.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/technology/amazon-explains-the-cause-behind-tuesday-s-massive-aws-outage/
+ Date: 2021-12-11T10:00:00-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/04/09/AWS.jpg)

![Amazon explains the cause behind Tuesday’s massive AWS outage](https://www.bleepstatic.com/content/hl-images/2021/04/09/AWS.jpg)


Amazon has published a post-event summary to shed some light on the root cause behind this week's massive AWS outage that took down a long list of high-profile sites and online services, including Ring, Netflix, Amazon Prime Video, and Roku.


[The outage](https://www.bleepingcomputer.com/news/technology/aws-outage-impacts-ring-netflix-and-amazon-deliveries/) started at roughly 10:30 AM EST on Tuesday. It affected the US-EAST-1 AWS region, which ensures connectivity for people and companies in the northeastern part of the United States.


As a result, streaming through Netflix, Amazon Prime, and Roku was immediately impacted together with Ring devices, brought down and unreachable, according to users reporting that they couldn't connect to their cameras.


Around the same time, Amazon delivery employees began sharing on Reddit that they could no longer access internal apps required to scan packages, access delivery routes, or see upcoming schedules.


"At 7:30 AM PST, an automated activity to scale capacity of one of the AWS services hosted in the main AWS network triggered an unexpected behavior from a large number of clients inside the internal network," [Amazon explained](https://aws.amazon.com/message/12721/) in a summary of this incident.


"This resulted in a large surge of connection activity that overwhelmed the networking devices between the internal network and the main AWS network, resulting in delays for communication between these networks.


"These delays increased latency and errors for services communicating between these networks, resulting in even more connection attempts and retries. This led to persistent congestion and performance issues on the devices connecting the two networks."



> 
> Our Support Contact Center also relies on the internal AWS network, so the ability to create support cases was impacted from 7:33 AM until 2:25 PM PST. We expect to release a new version of our Service Health Dashboard early next year that will make it easier to understand service impact and a new support system architecture that actively runs across multiple AWS regions to ensure we do not have delays in communicating with customers. - Amazon
> 
> 
> 


The Tuesday AWS outage is definitely not unique as it follows [multiple other similar events](https://aws.amazon.com/premiumsupport/technology/pes/) since 2011, including a large-scale incident that affected the same region in November 2020.


When it happened, it also brought down a large number of sites and online platforms after Amazon's Kinesis service for real-time processing of streaming data [began experiencing issues](https://aws.amazon.com/message/11201/).


One year prior, during September 2019, a power outage that hit the AWS US-EAST-1 data center in North Virginia [caused data loss for all Amazon customers](https://www.bleepingcomputer.com/news/technology/amazon-aws-outage-shows-data-in-the-cloud-is-not-always-safe/) lacking working backups to restore their files.


In February 2017, an [Amazon's S3 (Simple Storage Service) outage](https://www.bleepingcomputer.com/news/hardware/aws-goes-down-and-so-do-millions-of-websites-apps-and-other-services/) took down millions of small and high-profile sites and online platforms, including Adobe's apps and services, Docker, Mailchimp, Medium, Signal, Slack, Trello, Twilio, IFTTT, and Twitch.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Aws]] [[Bleeping Computer]]

