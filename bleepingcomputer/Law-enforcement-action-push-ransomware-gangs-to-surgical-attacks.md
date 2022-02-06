# Law enforcement action push ransomware gangs to surgical attacks
### The numerous law enforcement operations leading to the arrests and takedown of ransomware operations in 2021 have forced threat actors to narrow their targeting scope and maximize the efficiency of their operations.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/law-enforcement-action-push-ransomware-gangs-to-surgical-attacks/
+ Date: 2022-02-06T10:17:34-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/12/ransomware.jpg)

![surgical](https://www.bleepstatic.com/content/hl-images/2022/01/12/ransomware.jpg?rand=1762358919)


The numerous law enforcement operations leading to the arrests and takedown of ransomware operations in 2021 have forced threat actors to narrow their targeting scope and maximize the efficiency of their operations.


Most of the notorious Ransomware-as-a-Service (RaaS) gangs continue their operations even after the law enforcement authorities have [arrested key members](https://www.bleepingcomputer.com/news/security/the-week-in-ransomware-october-29th-2021-making-arrests/) but have refined their tactics for maximum impact.


Shift in victimology
--------------------


According to an analysis published by Coveware, which looks at ransom negotiation data from Q4 2021, ransomware groups now demand higher ransom payments instead of increasing the volume of their attacks.


In numbers, the average ransom payment in Q4 2021 reached **$322,168**, which is 130% higher compared to the previous quarter. The median ransom payment amount was **$117,116**, up 63% compared to Q3.



![Ransom payment figures](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/payment(1).png)**Ransom payment figures**  
*Source: Coveware*
Because disrupting the operation of large firms provokes investigations and creates political tensions on the international level, crooks are now striving for a delicate balance.


They target large enough firms to receive hefty ransom payment demands but not that big or critical that will cause them more geopolitical troubles than gains.


When looking at the company size in terms of employee count, entities with over 50,000 employees experienced fewer incidents as threat actors chose to focus more on mid-sized organizations.



![Size of companies targeted by ransomware](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/size(1).png)**Size of companies targeted by ransomware**  
*Source: Coveware*
"Although medium and large organizations continue to be impacted, ransomware remains a small business problem with 82% of attacks impacting organizations with less than one thousand employees," [explains Coveware](https://www.coveware.com/blog/2022/2/2/law-enforcement-pressure-forces-ransomware-groups-to-refine-tactics-in-q4-2021)


Group tactics and activity
--------------------------


In Q4 2021, the most frequently encountered variant was Conti, accounting for 19.4% of all detections, LockBit 2.0 came second with 16.3%, and Hive third with 9.2%.



![Ransomware group activity in Q4 2021](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Ransomware group activity in Q4 2021**  
*Source: Coveware*
Considering that the top three ransomware operations engage in double-extortion tactics, it is no surprise that 84% of all attacks in Q4 2021 involved stolen data too.


This percentage would be even higher if it relied only upon the actors' intentions, as in some cases, the attacks are detected and stopped by defense systems prematurely.


In terms of the techniques and procedures (TTPs), Coveware reports the following:


* Establishing **persistence** through scheduled tasks and startup code execution characterized 82% of the infections.
* The actors performed **lateral movement** in 82% of ransomware attacks, attempting to pivot to more systems on the same network.
* **Credential access** underpinned 71% of the observed ransomware cases.
* A **command and control** center orchestrating remote access operations was used in 63% of the incidents.
* **Gathering data** such as keyboard inputs, screenshots, emails, video, and other espionage-related information characterized 61% of the cases.

Another notable change in the tactics concerns the initial compromise vector. RDP access which used to be a widely-bartered item on dark web markets, is steadily dropping as ransomware actors turn to exploiting vulnerabilities.



![Access vectors in ransomware attacks](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Access vectors in ransomware attacks**  
*Source: Coveware*
The most exploited flaws for network entry in Q4 2021 were CVE-2021-34473, CVE-2021-26855, and CVE-2018-13379, on Microsoft Exchange and Fortinet firewall appliances.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Coveware]] [[Q4]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-34473]] [[CVE-2021-26855]] [[CVE-2018-13379]]

