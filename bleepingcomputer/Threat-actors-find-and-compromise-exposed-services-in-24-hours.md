# Threat actors find and compromise exposed services in 24 hours
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/threat-actors-find-and-compromise-exposed-services-in-24-hours/)
+ Date: November 23, 2021
+ Author: Bill Toulas


## Article:
![honeybees](https://www.bleepstatic.com/content/hl-images/2021/11/23/honeybees.jpg?rand=826708893)


Researchers set up 320 honeypots to see how quickly threat actors would target exposed cloud services and report that 80% of them were compromised in under 24 hours.


Malicious actors are constantly scanning the Internet for exposed services that could be exploited to access internal networks or perform other malicious activity.


To track what software and services are targeted by threat actors, researchers create publicly accessible honeypots. Honeypots are servers configured to appear as if they are running various software as lures to monitor threat actors' tactics.


A tempting lure
---------------


In a new study conducted by Palo Altos Networks' Unit 42, researchers set up 320 honeypots and found that 80% of the honeypots were compromised within the first 24 hours.


The deployed honeypots included ones with remote desktop protocol (RDP), secure shell protocol (SSH), server message block (SMB), and Postgres database services and were kept alive from July to August 2021.


These honeypots were deployed worldwide, with instances in North America, Asian Pacific, and Europe.



![Honeypot experiment infrastructure](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/infrastructure.jpg)**Honeypot experiment infrastructure**  
*Source: Unit 42*
How attackers move
------------------


The time to first compromise is analogous to how much the service type is targeted.


For SSH honeypots which were the most targeted, the mean time for the first compromise was three hours, and the mean time between two consecutive attacks was about 2 hours.



![Mean time between two consecutive attacks](https://www.bleepstatic.com/images/news/u/1220909/Security/mean_time.jpg)**Mean time between two consecutive attacks**  
*Source: Unit 42*
Unit 42 also observed a notable case of a threat actor compromising 96% of the experiment's 80 Postgres honeypots in just 30 seconds.


This finding is very concerning as it could take days, if not longer, to deploy new security updates as they are released, while threat actors just need hours to exploit exposed services.


Finally, regarding whether the location makes any difference, the APAC region received the most attention from threat actors.



![Attacks against each service type by region](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Attacks against each service type by region**  
*Source: Unit 42*
Do firewalls help?
------------------


The vast majority (85%) of attacker IPs were observed on a single day, which means that actors rarely (15%) reuse the same IP on subsequent attacks.


This constant IP change makes ‘layer 3’ firewall rules ineffective against the majority of threat actors.


What could have better chances of mitigating the attacks is to block IPs by drawing data from network scanning projects which identify hundreds of thousands of malicious IPs daily.


However, Unit 42 tested this hypothesis on a sub-group of 48 honeypots and found that blocking over 700,000 IPs had no significant difference in the number of attacks between the sub-group and the control group.



![Comparison between firewall and no-firewall groups](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Comparison between firewall and no-firewall groups**  
*Source: Unit 42*
To protect cloud services effectively, Unit 42 recommends that admins do the following:


* Create a guardrail to prevent privileged ports from being open.
* Create audit rules to monitor all the open ports and exposed services.
* Create automated response and remediation rules to fix misconfigurations automatically.
* Deploy next-generation firewalls (WFA or VM-Series) in front of the applications.


Finally, always install the latest security updates as they become available as threat actors rush to utilize exploits for new vulnerabilities as they are published.




#### Tags:
[[honeypots]] [[hours.]] [[Bleeping Computer]]
