# Coursera Flunks API Security Test in Researchers’ Exam
### The problem APIs included numero uno on the OWASP API Security Top 10: a Broken Object Level Authorization (BOLA) issue that could have exposed personal data. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167630)
+ Date: July 8, 2021  2:29 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/09070346/school-teacher.jpg)
Researchers have discovered multiple application programming interface (API) issues in Coursera, the online learning platform used by 82 million learners and hundreds of Fortune 500 companies.


On Thursday, the Checkmarx Security Research Team published a [report](https://www.checkmarx.com/blog/technical-blog/api-crash-course-broken-object-level-authorization-found-in-coursera/) on its findings, which included user and account enumeration via the reset password feature, lack of resources limiting on both a GraphQL and REST API, a GraphQL misconfiguration, and the whopper of them all: a Broken Object Level Authorization (BOLA) issue that affects users’ preferences.


BOLA is at the top of OWASP’s [Top 10 list of API security issues](https://www.cloudvector.com/owasp-api-security-top-10-broken-object-level-authorization/), given how easy these issues are to exploit and how tough it is to defend against the threat “in an organized way.”


Coursera’s BOLA issue, now fixed, meant that “anonymous users” could retrieve, and change, user preferences, according to the report, written by security researcher Paulo Silva. Some of the user preferences, such as recently viewed courses and certifications, also leaked some metadata: for example, activity date and time.



Silva said in the report that Checkmarx was inspired to check out Coursera’s security posture given how “remote everything” – including on-demand and e-learning courses – has boomed during the pandemic.


According to estimates, the remote learning and training will be a [$350 billion industry by 2025, up from $18 billion in 2019](https://www.weforum.org/agenda/2020/04/coronavirus-education-global-covid19-online-digital-learning/).


Coursera states, in its [Vulnerability Disclosure Program](https://hackerone.com/coursera?type=team), that access control issues are a security concern. That includes when an unauthorized user can get at other users’ private data, such as their grades or private forum posts. Other security issues covered by the platform’s disclosure program are those that enable users to mess with other learners, including by causing scripts to run on another user’s browser or by changing another user’s grades. Finally, the program covers leaks that expose Coursera’s internal administrative control systems.


The BOLA issue “perfectly fits” Coursera’s concerns about access control issues, Silva explained. “This vulnerability could have been abused to understand general users’ courses preferences at a large scale, but also to somehow bias users’ choices, since manipulating their recent activity affected the content rendered on Coursera’s homepage for a specific user,” he wrote.


Leaky APIs and the Ships They Sink
----------------------------------


Generally speaking, APIs are an intermediary between applications that define how they can talk to one another and that enable them to swap information.


API leaks are not uncommon and have been main contributors to major security issues. Insecure APIs are what led to [Experian leaking](https://threatpost.com/experian-api-leaks-american-credit-scores/165731/) most Americans’ credit scores in April. In May, a leaky API [spilled Peloton riders’ private data](https://threatpost.com/pelotons-spilled-riders-data/165880/).


Badly programmed APIs are an [obvious attack vector](https://threatpost.com/apis-next-frontier-cybercrime/158536/) and one of the most common threat vectors used to [take advantage of poorly secured applications](https://threatpost.com/clubhouse-users-data-hacker-forum/165354/) to get to data. They’re as common as dandelions in spring: When researcher Alissa Knight with Approov tried to break into the APIs of 30 different mHealth app vendors, she found that [they were all vulnerable](https://threatpost.com/mhealth-apps-millions-cyberattacks/163966/) to one degree or another. Seventy-seven percent of them contained [hardcoded API keys](https://threatpost.com/cybercriminals-exploits-zyxel-flaw/162789/) – some of which don’t expire – that would allow an attacker to intercept API exchange of information. Seven percent of those APIs belonged to third-party payment processors that explicitly warn against hard-coding their secret keys in plain text.


Knight also found that 100 percent of API endpoints tested were vulnerable to BOLA attacks, which allowed the researcher to view the personal health information and personally identifiable information (PII) for patients that weren’t assigned to the researcher’s account.


In his writeup, Silva confirmed that API access control issues are “one of the biggest security problems facing APIs.”


“As vulnerable APIs increasingly fall into adversaries’ sights, it’s critical that developers receive proper education on best practices for embedding security into their design from the get-go,” he said.


Checkmarx disclosed its findings to Coursera’s security team in October. By May 24, 2021, Coursera had resolved all the API issues, including a new one that Checkmarx found and reported in January.


A Coursera spokesperson told Threatpost that “The privacy and security of learners on Coursera is a top priority. We’re grateful to Checkmarx for bringing the low-risk API-related issues — which did not expose any personal data of learners, customers, or partners — to the attention of our security team last year, who were able to promptly address and resolve the issues.”


070821 17:14 UPDATE: Added statement from Coursera.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Coursera]] [[API]] [[Checkmarx]] [[ThreatPost]]
