# Ford bug exposed customer and employee records from internal systems
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/ford-bug-exposed-customer-and-employee-records-from-internal-systems/)
+ Date: August 15, 2021
+ Author: Ax Sharma


## Article:
![ford](https://www.bleepstatic.com/content/hl-images/2021/08/15/ford-background-2.png)


A bug on Ford Motor Company's website allowed for accessing sensitive systems and obtaining proprietary data, such as customer databases, employee records, internal tickets, etc.


The data exposure stemmed from a misconfigured instance of Pega Infinity customer engagement system running on Ford's servers.


From data exfiltration to account takeovers
-------------------------------------------


This week, researchers have disclosed a vulnerability found on Ford's website that let them peek into confidential company records, databases and perform account takeovers.


The vulnerability was discovered by [Robert Willis](https://twitter.com/rej_ex) and [*break3r*](https://twitter.com/1337break3r), with further validation and support provided by members of [Sakura Samurai](https://twitter.com/sakurasamuraii) ethical hacking group—[Aubrey Cottle](https://twitter.com/Kirtaner), [Jackson Henry](https://twitter.com/JacksonHHax), and [John Jackson](https://twitter.com/johnjhacking).


The issue is caused by CVE-2021-27653, an information exposure vulnerability in [improperly configured](https://collaborate.pega.com/discussion/pega-security-advisory-%E2%80%93-b21) Pega Infinity customer management system instances.


Researchers shared many screenshots of Ford's internal systems and databases with BleepingComputer. For example, the company's ticketing system is shown below:



![Ford ticket system exposed](https://www.bleepstatic.com/images/news/u/1164866/2021/Aug-2021/ford-pega/ticket-system-redacted(1).jpg)**Ford's internal ticket system exposed to researchers**
To exploit the issue, an attacker would first have to access the backend web panel of a misconfigured Pega Chat Access Group portal instance:


https://www.rpa-pega-1.ford.com/prweb/PRChat/app/RPACHAT\_4089/  

bD8qH******bIw4Prb*/!RPACHAT/$STANDARD...
As seen by BleepingComputer, different payloads provided as URL arguments could enable attackers to run queries, retrieve database tables, OAuth access tokens, and perform administrative actions.


The researchers state that some of the exposed assets contained sensitive Personal Identifiable Information (PII), and included:


* Customer and employee records
* Finance account numbers
* Database names and tables
* OAuth access tokens
* Internal support tickets
* User profiles within the organization
* Pulse actions
* Internal interfaces
* Search bar history


"The impact was large in scale. Attackers could use the vulnerabilities identified in the broken access control and obtain troves of sensitive records, perform account takeovers, and obtain a substantial amount of data," Willis writes in a [blog posting](https://robertwillishacking.com/ford-breach-august-2021-disclosure/).


Took six months to 'force disclose'
-----------------------------------


In February 2021, the researchers had [reported their findings](https://robertwillishacking.com/cve-2021-27653-march-2021/) to Pega that fixed the CVE in their chat portal relatively quickly.


The issue was also reported to Ford around the same time via their HackerOne vulnerability disclosure program.


But, the researchers told BleepingComputer that communication from Ford was thin and faded as the responsible disclosure timeline progressed:


"At one point in time, they completely stopped answering our questions. It took HackerOne mediation to get an initial response on our vulnerability submission from Ford," John Jackson told BleepingComputer in an email interview.


Jackson states that as the disclosure timeline progressed further, the researchers heard back from HackerOne only after tweeting about the flaw, but without giving out any sensitive details:




> 
> Here are some of the many things that are exposed:  
>   
> 
> Customer Databases, Employee Records, Internal Ticketing Systems, OAuth Tokens, Request Info, Finances...actually there are about 8 pages worth of Database Tables so it would be really difficult to express.
> 
> 
> — John Jackson 桜の侍 (@johnjhacking) [March 5, 2021](https://twitter.com/johnjhacking/status/1367626404666384384?ref_src=twsrc%5Etfw)


"When the vulnerability was marked as resolved, Ford ignored our disclosure request. Subsequently, HackerOne mediation ignored our request for help disclosing which can be seen in the PDF."


"We had to wait the full six months to force disclose per [HackerOne's policy](https://www.hackerone.com/disclosure-guidelines) out of fear of the law and negative repercussions," continued Jackson.


At this time, Ford's vulnerability disclosure program [does not offer](https://hackerone.com/ford?type=team) monetary incentives or bug bounties, so a coordinated disclosure in light of public interest was the only "reward" researchers were hoping for.


A copy of the disclosure report shared with BleepingComputer indicates Ford refrained from commenting on specific security-related actions.


"The findings you submitted... are considered private. These vulnerability reports are intended to prevent compromises which may require disclosure."


"In this scenario, the system was taken offline shortly after you submitted your findings to HackerOne," Ford shared with HackerOne and the researchers, as per the discussion in the PDF.


Although the endpoints were taken offline by Ford within 24 hours of the report, the researchers comment in the same report that the endpoints remained accessible even afterward, and requested another review and remediation.


It is not yet known if any threat actors exploited the vulnerability to breach systems at Ford, or if sensitive customer/employee PII was accessed.


BleepingComputer reached out to Ford multiple times well in advance of publishing but we did not hear back.




#### Tags:
[[HackerOne]] [[BleepingComputer]] [[records,]] [[OAuth]] [[Bleeping Computer]]
