# 96% of third-party container applications deployed in cloud infrastructure contain known vulnerabilities: Unit 42
### Unit 42 found that 63% of third-party code used in building cloud infrastructure contained insecure configurations.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/96-of-third-party-container-applications-deployed-in-cloud-infrastructure-contain-known-vulnerabilities-unit-42/)
+ Date: September 29, 2021
+ Author: Jonathan Greig


## Article:
Unknown

A [new report](https://unit42.paloaltonetworks.com/cloud-threat-report-2h-2021/) from Palo Alto Networks' Unit 42 outlined the ways that the supply chain has become an emerging cloud security threat. 

Unit 42 conducted a red team exercise with a large SaaS provider that is a Palo Alto Networks customer and within three days, the team was able to discover critical software development flaws that could have exposed the organization to an attack similar to [SolarWinds](https://www.zdnet.com/article/solarwinds-the-more-we-learn-the-worse-it-looks/) and [Kaseya](https://www.zdnet.com/article/updated-kaseya-ransomware-attack-faq-what-we-know-now/). 

Unit 42 found that 63% of third-party code used in building cloud infrastructure contained insecure configurations. If an attacker compromises third-party developers, it's possible to infiltrate thousands of organizations' cloud infrastructures, according to the report.

The organization analyzed data from a variety of public data sources around the world in order to draw conclusions about the growing threats organizations face today in their software supply chains. 

They found that 96% of third-party container applications deployed in cloud infrastructure contain known vulnerabilities. 

In the report, Unit 42 researchers discovered that even for a customer who had what most would consider a "mature" cloud security posture, there were several critical misconfigurations and vulnerabilities that allowed the Unit 42 team to take over the customer's cloud infrastructure in a matter of days.

"In most supply chain attacks, an attacker compromises a vendor and inserts malicious code in software used by customers. Cloud infrastructure can fall prey to a similar approach in which unvetted third-party code could introduce security flaws and give attackers access to sensitive data in the cloud environment. Additionally, unless organizations verify sources, third-party code can come from anyone, including an Advanced Persistent Threat," Unit 42 wrote. 






"Teams continue to neglect DevOps security, due in part to lack of attention to supply chain threats. Cloud native applications have a long chain of dependencies, and those dependencies have dependences of their own. DevOps and security teams need to gain visibility into the bill of materials in every cloud workload in order to evaluate risk at every stage of the dependency chain and establish guardrails."

![word-image-66.png]()![word-image-66.png](https://www.zdnet.com/a/img/resize/ee8c7549027a6b49fe0a7bac4550a50ceb369604/2021/09/29/d066774a-a80b-47a5-a0c2-135fd7f1714a/word-image-66.png?width=470&fit=bounds&auto=webp)
 Unit 42
 BreachQuest CTO Jake Williams called the research "significant" and said it replaces anecdotes of incident responders with actual data on how common it is to find configuration issues and unpatched vulnerabilities in the public software supply chain. 

"At BreachQuest, we are used to working incidents where code and apps are built from Docker Hub images with pre-built security issues. While these are usually missing patches, it's not uncommon to find security misconfigurations in these images either," Williams said. 

"This is a problem the security community has dealt with since the dawn of the public cloud. Previous research found that the vast majority of publicly available Amazon Machine Images contained missing patches and/or configuration issues."

Other experts, like Valtix CTO Vishal Jain, noted that for more than a year now, spend on the cloud vastly exceeded spend on data centers. 

Jain added that attacks typically go where the money is, so the big, open security front for enterprises is now the cloud. 

He suggested organizations focus on security at build time -- scanning of IaC templates used in building cloud infrastructure -- and security at run time. 

"It is not either/or, it needs to be both. More importantly, with dynamic infrastructure and app sprawl in the public cloud, there is a new set of security problems that need to be addressed in the cloud," Jain said. 

Others said code was almost impossible to secure against fast-moving functional requirements and threat models. Mohit Tiwari, CEO at Symmetry Systems, told ZDNet it is more efficient to harden the infrastructure than chase application-level bugs in hundreds of millions of lines of code. 

Tiwari explained that first-party code is as likely as third-party code to have exploitable bugs -- like authorization errors -- and these bugs expose customer data that is managed by business logic. 

"Blaming third party code is a red-herring -- software like Linux, Postgres, Django/Rails etc…comprise most of any applications, so nearly 100% of applications have third party code with known vulnerabilities," Tiwari said. 

"Organizations in practice are instead moving to get infrastructure -- cloud IAM, service meshes, etc… -- in order while relying on code-analysis for targeted use cases (such as the trusted code base that provides security for the bulk of application code)."





#### Tags:
[[cloud]] [[third-party]] [[said.]] [[ZDNet]]
