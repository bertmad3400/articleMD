# Former Ubiquiti dev charged for trying to extort his employer
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/former-ubiquiti-dev-charged-for-trying-to-extort-his-employer/)
+ Date: December 1, 2021
+ Author: Sergiu Gatlan


## Article:
![Former Ubiquiti dev charged for trying to extort his employer](https://www.bleepstatic.com/content/hl-images/2021/04/01/Ubiquiti.jpg)


Nickolas Sharp, a former employee of networking device maker Ubiquiti, was arrested and charged today with data theft and attempting to extort his employer while posing as a whistleblower and an anonymous hacker.


"As alleged, Nickolas Sharp exploited his access as a trusted insider to steal gigabytes of confidential data from his employer, then, posing as an anonymous hacker, sent the company a nearly $2 million ransom demand," U.S. Attorney Damian Williams said today.


"As further alleged, after the FBI searched his home in connection with the theft, Sharp, now posing as an anonymous company whistleblower, planted damaging news stories falsely claiming the theft had been by a hacker enabled by a vulnerability in the company's computer systems."


Exposed by an Internet outage
-----------------------------


According to the indictment [[PDF](https://www.justice.gov/usao-sdny/press-release/file/1452706/download)], Sharp stole gigabytes of confidential data from Ubiquiti's AWS (on December 10, 2020) and GitHub (on December 21 and 22, 2020) infrastructure using his cloud administrator credentials, cloning hundreds of GitHub repositories over SSH.


Throughout this process, the defendant tried hiding his home IP address using Surfshark's VPN services. However, his actual location was exposed after a temporary Internet outage.


To hide his malicious activity, Sharp also altered log retention policies and other files that would have exposed his identity during the subsequent incident investigation.


"Among other things, SHARP applied one-day lifecycle retention policies to certain logs on AWS which would have the effect of deleting certain evidence of the intruder's activity within one day," the court documents read.


After Ubiquiti disclosed a [security incident](https://www.bleepingcomputer.com/news/security/networking-giant-ubiquiti-alerts-customers-of-potential-data-breach/) in January following Sharp's data theft, while working to assess the scope and remediate the security breach effects he also tried extorting the company (posing as an anonymous hacker).


His ransom note demanded almost $2 million in exchange for returning the stolen files and the identification of a remaining vulnerability.


The company refused to pay the ransom and, instead, found and removed a second backdoor from its systems, changed all employee credentials, and issued the [January 11 security breach notification](https://www.bleepingcomputer.com/news/security/networking-giant-ubiquiti-alerts-customers-of-potential-data-breach/).


Billions of dollars in losses after stock drop
----------------------------------------------


After his extortion attempts failed, Sharp shared information with the media while pretending to be a whistleblower and accusing the company of downplaying the incident.


This caused [Ubiquiti's stock price to fall by roughly 20%](http://www.google.com/finance/quote/UI:NYSE?window=1Ywww.google.com/finance/quote/UI:NYSE?window=1Y), from $349 on March 30 to $290 on April 1, amounting to losses of over $4 billion in market capitalization.


"SHARP subsequently re-victimized his employer by causing the publication of misleading news articles about the company's handling of the breach that he perpetrated, which were followed by a significant drop in the company's share price associated with the loss of billions of dollars in its market capitalization," the Department of Justice (DOJ) [said](https://www.justice.gov/usao-sdny/pr/former-employee-technology-company-charged-stealing-confidential-data-and-extorting).


The company confirmed on April 1 that it was [the target of an extortion attempt following a January security breach](https://www.bleepingcomputer.com/news/security/ubiquiti-confirms-extortion-attempt-following-security-breach/) with no indication that customer accounts were affected after Sharp (acting as a whistleblower) challenged his employer's take on the breach [saying that the incident's actual impact was massive.](https://www.bleepingcomputer.com/news/security/ubiquiti-cyberattack-may-be-far-worse-than-originally-disclosed/)


He also said Ubiquiti did not have a logging system thus preventing them from checking what data or systems the attacker accessed. This lines up with DOJ's info on him tampering with the company's logging systems.


While the DOJ didn't name Sharp's employer in today's press release or the indictment, all the details perfectly align with previous info on [the Ubiquiti breach](https://www.bleepingcomputer.com/tag/ubiquiti/) and information presented in [Sharp's LinkedIn account](https://www.linkedin.com/in/nickolassharp).


Sharp is charged with four counts and is facing a maximum sentence of 37 years in prison if found guilty. 




#### Tags:
[[Ubiquiti]] [[Bleeping Computer]]
