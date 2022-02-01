# Fending off ransomware attacks using AI-powered tools | ZDNet
### Why Cohesity believes zero-trust security by itself isn't enough to stop an increasing number of sophisticated ransomware attacks.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/fending-off-ransomware-attacks-using-ai-powered-tools/
+ Date: 2022-02-01 22:16:32
+ Author: Chris Preimesberger


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/f4efb40bab7f08bb3eee21abb7879d429caf491e/2022/02/01/55eea121-ad46-4a83-a47f-e07b861332eb/cohesity-sign.jpg?width=770&height=578&fit=crop&auto=webp)

Zero trust-type security, which no self-respecting security software provider doesn't now provide, is a good leap forward in the never-ending battle against the bad hacker actors of the world. But it's turning out not to be the complete answer to storing corporate data securely for an enterprise and its users.

Zero trust enables enterprises to restrict access controls to networks, applications, and environments without sacrificing performance and causing user ire. A zero-trust approach trusts no one, no matter how high on a security clearance ladder he or she may be. Multiple entry codes will always be needed. But ZT still needs assistance in order to provide the 24/7 security and airtight access processes required by many enterprises, and AI is providing that help.

This is where next-gen data protection providers such as [Fortinet](https://fortinet.com), [Dell Technologies](https://delltechnologies.com), [Forcepoint](https://forcepoint.com), and [Cohesity](https://cohesity.com) come into the picture, because they all bring multiple weapons to this problem. Many of those tools use AI to identify intruders and stop exploits faster than had been available previously.

Cohesity is the latest to produce new capabilities augmenting ZT and aimed squarely at solving the rampant ransomware problem that so many organizations – both for-profit and nonprofit – have suffered in the last few years. 

Early on, cybercriminals focused only on encrypting a victim's production data. Cohesity, among others, countered by enabling users to rapidly restore from backup data. Then, criminals started to destroy or encrypt backup volumes themselves. Cohesity countered with immutability. Now, bad actors are exfiltrating the data and threatening to post it on the dark web. 

To help its users address the latest threats, Cohesity unveiled at its [Cohesity Connect](https://www.cohesity.com/connect/) conference the following SaaS offerings, which are now included in the company's [Data Management as a Service](https://www.cohesity.com/products/saas/) platform: 

* **Cohesity DataGovern:** A data security and governance service that uses AI/ML to automate the discovery of sensitive data and detect anomalous access and usage patterns that could indicate a cyberattack in play -- the key to thwarting bad actors trying to exfiltrate data.
* **Project Fort Knox:** A service that allows users to maintain an isolated copy of their data in a Cohesity-managed vault to improve data resiliency in the face of ransomware attacks. In addition to immutability, the company said, this gives users another way to thwart attackers trying to encrypt data.

### The four pillars of next-gen data management

Cohesity CEO Mohit Aron told ZDNet that any provider describing its platform as "next-gen data management" must include the following four characteristics: 

* **Must be intuitive and simple to use at scale:** Enterprise line-of-business employees should be able to use the platform at will to manage all their data optimally as needed.
* **Must include zero-trust security:** Specific ransomware protection is built into this.
* **Must be AI-powered:** "The platform needs to be smart, so when something goes down, it can auto-heal itself. It must have AI-based detection of ransomware. So the whole platform must be AI-powered," Aron said.  Cohesity's AI/ML-based classification software is used to identify sensitive data -- including personally identifiable information (PII) -- in backup and production data, and determine who has access to it, helping to harden environments before attacks occur.
* **Must have third-party extensibility:** "Users shouldn't just be able to take benefit of the products that we build, but on this platform, they should be able to extend the power of this platform by third-party applications and integrations," Aron said.






"Relying on legacy backup as an insurance policy no longer is sufficient," Cohesity Head of Product Matt Waxman said. "Users need next-gen technology that makes it easy to identify sensitive data, detect anomalies, isolate data, and stay ahead of modern threats. That's what we're focused on in our Threat Defense architecture."  

### How the AI is implemented

In order for technologists, data architects, and software developers to learn more about how to utilize AI, ZDNet asked the following questions of Aron, who offered these details:

**ZDnet:** What AI and ML tools are you using specifically? 

**Aron:** Applications of AI/ML are spread across multiple areas of our product, both on the SaaS side and on-premises. One set of use cases is the use of time series (looking at data over time) anomaly detection techniques that identify potential data security threats, such as a ransomware attack, and provide alerts and guidance to the administrator.   Another category is the use of a combination of supervised/semi-supervised models for security analytics and data governance. For proactive performance optimization use cases, we use a variety of time-series regression models. 

**ZDnet:** **Are you using models and algorithms out of a box, such as DataRobot or other sources?**

**Aron:** For simpler use cases, we use off-the-shelf models with minimal tuning. For more complex ones, we integrate a set of off-the-shelf models to achieve better accuracy. 

**ZDnet:** **What cloud services are you using?**

**Aron:** Our Data Management as a Service portfolio of SaaS offerings runs on AWS. Our data management platform also runs on Microsoft Azure and Google Cloud. 

**ZDnet:** **Are you using the AI workflow tools that come with that cloud?**

**Aron:** We leverage SageMaker workflows where applicable; however, we do build our own workflows deployed on Kubernetes to support a variety of deployment models.

**ZDnet: How are you labeling data for the ML and AI workflows?**

**Aron:** For labeling data for supervised learning use cases, we leverage pre-labeled data collected from our wide customer base in combination with our own data labeling inference workflows for augmentation. 

**ZDnet:** **Can you give us a ballpark estimate on how much data you are processing?**

**Aron:** We estimate that we process hundreds of millions of events on a daily basis for a variety of ML-enabled use cases.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Bern]] [[victim.country.name=Switzerland]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Aron]] [[Cohesity]] [[Ransomware]] [[Next-gen]] [[Zdnet]] [[Saas]] [[Workflows]] [[ZDNet]]

