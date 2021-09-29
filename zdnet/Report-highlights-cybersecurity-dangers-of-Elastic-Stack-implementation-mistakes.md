# Report highlights cybersecurity dangers of Elastic Stack implementation mistakes
### Researchers from cybersecurity firm Salt Security discovered widespread mistakes that allowed them to launch attacks where any user could extract sensitive customer and system data.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/security-report-highlights-cybersecurity-dangers-of-elastic-stack-implementation-mistakes/)
+ Date: September 29, 2021
+ Author: Jonathan Greig


## Article:
Unknown

A [new report](https://salt.security/blog/api-threat-research-elastic-vuln) has identified significant vulnerabilities resulting from the mis-implementation of Elastic Stack, a group of open-source products that use APIs for critical data aggregation, search, and analytics capabilities.

Researchers from cybersecurity firm Salt Security discovered issues that allowed them to not only launch attacks where any user could extract sensitive customer and system data but also allowed any user to create a denial of service condition that would render the system unavailable. 

The researchers said they first discovered the vulnerability while protecting one of their customers, a large online business-to-consumer platform that provides API-based mobile applications and software as a service to millions of global users.

Once they discovered the vulnerability, they checked other customers using Elastic Stack and found that almost every enterprise with it was affected by the vulnerability — which exposed users to injection attacks and more. 

Salt Security officials were quick to note that this is not a vulnerability with Elastic Stack itself but instead a problem with how it is being implemented. Salt Security technical evangelist Michael Isbitski said the vulnerability is not connected to any issue with Elastic's software but is related to "a common risky implementation setup by users."

He noted that Elastic [provides guidance](https://www.elastic.co/guide/en/elasticsearch/reference/7.15/secure-cluster.html) about how to implement Elastic Stack instances securely but noted that the responsibility falls on practitioners to make use of the guidance. 

"The lack of awareness around potential misconfigurations, mis-implementations, and cluster exposures is largely a community issue that can be solved only through research and education," Isbitski told ZDNet. 






"Elastic Stack is far from the only example of this type of implementation issue, but the company can help educate its users just as Salt Security has been working with CISOs, security architects, and other application security practitioners to alert them to this and other API vulnerabilities and provide mitigation best practices."

The vulnerability would allow a threat actor to abuse the lack of authorization between front-end and back-end services as a way to get a working user account with basic permission levels. 

From there, a cyberattacker could then exfiltrate sensitive user and system data by making "educated guesses about the schema of back-end data stores and query for data they aren't authorized to access," according to the report. 

Salt Security CEO Roey Eliyahu said that while Elastic Stack is widely used and secure, the same architectural design mistakes were seen in almost every environment that uses it.

"The Elastic Stack API vulnerability can lead to the exposure of sensitive data that can be used to perpetuate serious fraud and abuse, creating substantial business risk," Eliyahu said. 

Exploits that take advantage of this Elastic Stack vulnerability can create "a cascade of API threats," according to Salt Security researchers, who also showed that the Elastic Stack design implementation flaws worsen significantly when an attacker chains together multiple exploits.

The problem has been something security researchers [have long highlighted](https://blog.shodan.io/elastic-data-exposure-grows-to-3-2-pb/) with a number of similar products like MongoDB and HDFS.

"The specific queries submitted to the Elastic back-end services used to exploit this vulnerability are difficult to test for. This case shows why architecture matters for any API security solution you put in place -- you need the ability to capture substantial context about API usage over time," Isbitski said.

"It also shows how critical it is to architect application environments correctly. Every organization should evaluate the API integrations between its systems and applications, since they directly impact the company's security posture."

Researchers from the company said they were able to gain access to sensitive data like account numbers, transaction confirmation numbers and other information that would violate GDPR regulations. 

The report details other actions that could be taken through the vulnerability including the ability to perpetrate a variety of fraudulent activities, extort funds, steal identities and take over accounts. 

Jon Gaines, senior application security consultant at nVisium, said the Elastic Stack is "notorious for excessive data exposure" and added that a few years ago -- and by default -- data was exposed publicly. Since then the defaults have changed but he noted that this doesn't mean that older versions aren't grandfathered in or that minor configuration changes can't lead to both of these newly unearthed vulnerabilities. 

"There are -- and have been -- multiple open source tools that lead to the discovery of these vulnerabilities that I've used previously and continue to use. Unfortunately, the technical barrier of these vulnerabilities is extremely low. As a result, the risk of a bad guy discovering and exploiting these vulnerabilities is high," Gaines said. 

"From the outside looking in, these vulnerabilities are common sense for security professionals, authorization, rate limitations, invalidation, parameterized queries, and so forth. However, as a data custodian, administrator, or even developer, oftentimes you aren't taught to develop or maintain with security in mind."

Vulcan Cyber CEO Yaniv Bar-Dayan added that the most-common cloud vulnerability is caused by human error and misconfigurations, and APIs are not immune.

"We've all seen exposed customer data and denial of service attacks do significant material damage to hacked targets. Exploitation of this vulnerability is avoidable but must be remediated quickly," Bar-Dayan said. 

"Other users of Elastic Stack should check their own implementations for this misconfiguration and not repeat the same mistake."





#### Tags:
[[API]] [[Isbitski]] [[back-end]] [[said.]] [[ZDNet]]
