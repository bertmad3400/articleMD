# The Overlooked Security Risks of The Cloud
### Nate Warfield, CTO of Prevaliion, discusses the top security concerns for those embracing virtual machines, public cloud storage and cloud strategies for remote working.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168754)
+ Date: August 17, 2021  2:56 pm
+ Author: Nate Warfield


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/17145342/cloud-e1629226435519.jpg)
Cloud networking has done more to change computing as we know it than any other innovation in the last 15 years. It’s enabled small companies to quickly deploy an online presence, large companies to scale as demand ebbs and flows, and in a post-COVID world, it provides the foundation for a remote workforce.


This convenience however hasn’t come without its own set of challenges, and the race to “move to the cloud” has frequently left organizations and their users with an entirely new set of security challenges and data-privacy issues.


Cloud marketplaces are rife with pre-built virtual machine (VM) images containing unpatched vulnerabilities, overly permissive firewall settings and even malware and coin miners. Cloud providers don’t take a proactive stance towards breach/compromise monitoring and, in many cases, won’t even pass on notifications to their customers which they have received from external researchers.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Cloud deployments are also [a huge source](https://threatpost.com/google-cloud-buckets-exposed-misconfiguration/159429/) of data leaks (S3 buckets, open databases/NoSQL servers), and third-party data providers running in the cloud continue to be a source of data leaks from otherwise secure organizations.


 


Security is paramount for the companies who build and maintain the major clouds like Azure, AWS, Google Cloud Platform (GCP) and others – Microsoft for example has an extremely well-developed process to secure its hypervisor layer. But, due to the nature of providing infrastructure/platform/software as-a-service (IaaS/PaaS/SaaS) solutions, a large amount of the work is left to the customer.


**The Problem with Pre-Built and Pre-Installed VMs**
----------------------------------------------------


Cloud marketplaces or galleries are the repositories of pre-built VMs available for customers to deploy. While cloud providers offer methods for customers to upload their own VM images for easy deployment and auto-scaling, many people prefer the convenience of using a pre-built image.


While convenient, these images are frequently outdated or deployed with overly permissive firewall settings which may open the VM up for attack immediately after it boots up. Another troubling trend has been the introduction of VM images which are pre-installed with malware or crypto-currency miners – [as was seen with](https://threatpost.com/malicious-docker-cryptomining-images/165120/) Docker Hub.


While dangerous, these attacks are only the tip of the iceberg in terms of malicious potential. A properly motivated attacker could, in theory, develop a VM image which, after a pre-determined amount of time, phones home to the malware operators and establishes a command-and-control (C2) connection.


The major clouds like AWS and Azure automatically provision internal IPs to be only accessible to the virtual machines which provide details of the subscription the VM runs under. However, this information could be collected by the malware or discovered by malicious operators [on the machine itself](https://threatpost.com/windows-containers-malware-targets-kubernetes/166692/).


Furthermore, with the rise in hybrid-cloud deployments and point-to-point VPNs connecting cloud environments to a customer’s on-premises network, a beachhead on a cloud VM could easily become a pathway to the heart of an organization’s network.


These are non-trivial problems for cloud providers to solve. While providers do scan VM images for malware before making them available, as seen with antivirus solutions, these types of scans only catch known malicious code and aren’t a comprehensive defense. A simple *cron* job on a Linux VM or scheduled task in Windows could easily download secondary payloads days or weeks after provisioning.


Compounding this risk are clouds like AWS, which allow any user to share a VM image in the marketplace. Using these types of VMs is akin to the risk posed by mobile app stores, but with enterprise consequences.


**Lack of Protection and Customer Notification**
------------------------------------------------


A key problem today is that cloud providers aren’t taking a proactive stance towards breach/compromise monitoring and, in many cases, do not pass on notifications to their customers which arrive from external researchers.


While it’s true that cloud providers cannot be responsible for all security decisions made by their customers, their approach is primarily focused on selling additional security tooling — and reports of breached VMs discovered by external security researchers (and even employees of the cloud provider) are frequently dismissed as unactionable.


This leads to situations where hundreds, sometimes thousands of VMs become compromised in coordinated attack campaigns and remain breached for weeks or longer if the customer doesn’t immediately notice.


A good example of this is a continued attack campaign against improperly secured NoSQL databases, which started in late 2016 and continues to this day.


Research I performed against this attack trend showed that many customers were put at risk due to overly permissive default firewall settings on the VM, coupled with NoSQL being enabled on internet-facing network interfaces and a default lack of authentication. I found nearly 8,000 VMs in Microsoft’s Azure cloud between 2016-2019 which were compromised.


In most cases, the customers weren’t aware they’d even been exposed to the internet or that a compromise had taken place – and those were only in the limited instances where customer notifications were sent out. The attacks weren’t limited to Azure, of course, and globally there were more than 100,000 VMs affected by attacks against  CassandraDB, [Elasticsearch](https://threatpost.com/cloud-leak-320m-dating-site-records/159225/), MongoDB and Redis.


**Data Leak Risks**
-------------------


Beyond the risk of compromise, unsecured NoSQL databases have been the source of countless data leaks and privacy problems. Microsoft accidentally exposed 250 million customer records through an improperly secured Elasticsearch instance in late 2019, and these problems continue to occur across the globe at a regular cadence.


Amazon’s S3 buckets were so commonly left insecure that search engines have been developed to allow bug-bounty hunters (and, inadvertently, malicious actors) to search exposed S3 instances for valuable data, personally identifiable information (PII), financial records, database backups, credentials and credit-card records. Healthcare information is another commonly exposed dataset, as are social-media accounts and advertising data collected by data-warehouse companies.


Third-party data aggregators and advertising companies are also frequently the cause of data leaks from organizations who themselves may have strict policies about data security, encryption-at-rest, privileged access and restricted internet exposure to sensitive files. In 2020 alone, [36 billion records were exposed](https://cisomag.eccouncil.org/2020-is-the-worst-year-on-record-in-terms-of-data-breaches-survey/) in the first three quarters.


**Better Security Is Essential**
--------------------------------


All of this isn’t to say that cloud networking is inherently insecure, but as the world shifts to a cloud-centric and hybrid cloud environment, particularly for remote workforces, organizations need to recognize that their cloud-security strategy, policies, controls and processes must be as robust as in a classic on-premises environment. They cannot assume that because a Seattle, Redmond or Bay Area tech giant runs their cloud, that any additional security is baked in.


Cloud providers should also be taking a far more aggressive and proactive approach to securing their customers, notifying them of breaches and isolating virtual machines inside subscriptions when compromise is detected.


There are third-party monitoring services which offer real-time detection of automated scanning occurring on the internet, and others who offer real-time detection of malware beacons emitting from clouds, which providers are resistant to utilize. Some recent data on four of the larger cloud providers (Azure, AWS, Rackspace and Oracle Cloud) shows massive numbers of malware beacons being emitted over a 180-day period. Microsoft’s Azure cloud was the worst with 1.4 billion beacons, followed by AWS with 793 million, Rackspace with 598 million and Oracle seemingly much better with “only” 1.4 million beacons.


Whether the large delta is a result of vastly different customer sizes or significant differences in the security posture is impossible to determine, but it serves to underline the fact that cloud customers are being compromised in massive numbers, and these infections are going unaddressed.


By leveraging external systems against their internal subscriber-to-IP address databases, cloud providers could be delivering notifications to customers within minutes or hours of compromise, giving organizations much needed time to respond, detect and evict attackers before it’s too late.


***Nate Warfield is CTO of Prevailion, co-founder of the CTI League and a former senior security researcher for Microsoft Defender for Endpoints.***


***Enjoy additional insights from Threatpost’s InfoSec Insider community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***


 




#### Tags:
[[cloud]] [[VM]] [[Cloud]] [[malware]] [[VMs]] [[pre-built]] [[cases,]] [[AWS,]] [[Microsoft]] [[NoSQL]] [[ThreatPost]]
