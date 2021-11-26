# Google: Half of compromised cloud instances have weak or no passwords
### And many attackers are installing cryptomining malware within 22 seconds of compromising cloud instances.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/google-half-of-compromised-cloud-instances-have-weak-or-no-passwords/)
+ Date: November 26, 2021
+ Author: Liam Tung


## Article:
Unknown

Online criminals are deploying cryptocurrency miners within just 22 seconds of compromising misconfigured cloud instances running on Google Cloud Platform (GCP).

Cryptocurrency mining is by far the main malicious activity conducted by attackers after taking advantage of misconfigured instances hosted on GCP, making up 86% of all actions carried out after compromise. 

And in many cases, the attackers move extremely quickly after compromising an instance and installing cryptomining malware to free-ride off others' CPU and GPU resources to turn a profit for themselves. 


"Analysis of the systems used to perform unauthorized cryptocurrency mining, where timeline information was available, revealed that in 58% of situations the cryptocurrency mining software was downloaded to the system within 22 seconds of being compromised," [Google says in its first Cloud Threat Intelligence report](https://services.google.com/fh/files/misc/gcat_threathorizons_full_nov2021.pdf).

**SEE:** [**Cloud security in 2021: A business guide to essential tools and best practices**](https://www.zdnet.com/article/cloud-security-in-2021-a-business-guide-to-essential-tools-and-best-practices/)

Another striking trend was how quickly attackers are finding and compromising unsecured, internet-facing instances. The shortest time a compromise took place was 30 minutes after those instances were deployed. In 40% of cases, the time-to-compromise was under eight hours. 

Security firm Palo Alto Networks [similarly found](https://unit42.paloaltonetworks.com/exposed-services-public-clouds/) that 80% of 320 internet-facing 'honeypot' instances hosted in the cloud — and designed to attract attackers — were compromised within 24 hours. 






As Google's report highlights, crypto-mining malware is a problem for users on GCP who don't take steps to protect their cloud instances. 

"While data theft did not appear to be the objective of these compromises, it remains a risk associated with the cloud asset compromises as bad actors start performing multiple forms of abuse. The public Internet-facing Cloud instances were open to scanning and brute force attacks," Google notes. 

**SEE:** [**Dark web crooks are now teaching courses on how to build botnets**](https://www.zdnet.com/article/college-for-cyber-criminals-dark-web-crooks-are-teaching-courses-on-how-to-build-botnets/#link=%7B%22role%22:%22standard%22,%22href%22:%22https://www.zdnet.com/article/college-for-cyber-criminals-dark-web-crooks-are-teaching-courses-on-how-to-build-botnets/%22,%22target%22:%22_blank%22,%22absolute%22:%22%22,%22linkText%22:%22Dark%20web%20crooks%20are%20now%20teaching%20courses%20on%20how%20to%20build%20botnets%22%7D)

Internet-facing GCP instances were a significant target for attackers. Just under half of compromised instances were carried by attackers gaining access to instances with either no password or a weak password for user accounts or API connections, which meant these instances could be easily scanned and brute forced.

"This suggests that the public IP address space is routinely scanned for vulnerable cloud instances. It will not be a matter of if a vulnerable Cloud instance is detected, but rather when," Google said.

Additionally, 26% of compromised instances were due to vulnerabilities in third-party software being used by the owner.

"Many successful attacks are due to poor hygiene and a lack of basic control implementation," [said Bob Mechler, director at Google Cloud's office of the CISO](https://cloud.google.com/blog/products/identity-security/coin-mining-ransomware-apts-target-cloud-gcat-report).

The report is a wrap up of observations over the last year by Google Threat Analysis Group (TAG), Google Cloud Security and Trust Center, and Google Cloud Threat Intelligence for Chronicle, Trust and Safety.





#### Tags:
[[Google]] [[Cloud]] [[cloud]] [[instances.]] [[ZDNet]]
