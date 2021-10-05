# The Telegraph exposes 10 TB database with subscriber info
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/the-telegraph-exposes-10-tb-database-with-subscriber-info/)
+ Date: October 5, 2021
+ Author: Bill Toulas


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/10/05/The_Telegraph_UK.jpg?rand=680772335)


‘The Telegraph’, one of the UK’s largest newspapers and online media outlets, has leaked 10 TB of data after failing to properly secure one of its databases.


The exposed information includes internal logs, full subscriber names, email addresses, device info, URL requests, IP addresses, authentication tokens, and unique reader identifiers.


Bob Diachenko, the researcher who discovered the unprotected dataset on September 14, 2021, has confirmed that at least 1,200 unencrypted contacts were accessible without a password at the time of his review.


![telegraph record](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/the-telegraph-giant-1.png)A sample of the exposed records. Source: cooltechzone.com
Notably, many of these cases concern registrant information of Apple News subscribers, also including passwords in plaintext form.


The newspaper was contacted and warned about the exposure immediately, but it took them two days to eventually respond and secure the database.


The instance was indexed on specialized search engines on September 1, 2021, so the period of exposure is at least three weeks. That’s plenty of time for attackers and automated scanners to find the exposed database and exfiltrate the contained data.


Only affects a subset of subscribers
------------------------------------


For those of you who might have been exposed as a result of this data leak, the main risk you’re running is getting scammed or phished via email.


The leak of the URL requests may also cause a privacy risk as someone could use them to construct the users' browsing history on the news platform.


As for the consequences for The Telegraph, stolen access tokens could be used by non-subscribers to access content locked behind its paywall, but they could solve this with a reset. 


In response to the above, The Telegraph [issued the following statement](https://cooltechzone.com/leaks/the-telegraph-giant-data-leak) regarding Diachenko's findings:



> 
> We became aware of this discovery on 16 September and took immediate action to secure the data. An investigation showed that only a small number of records were exposed – less than 0.1% of our users and we have contacted all the users to advise them. The investigation also concluded that whilst the data was exposed it was not breached other than the discovery posted by the researcher. We are grateful for the work of independent researchers who responsibly disclose vulnerabilities and exposures and who are vital in our continued work to protect our assets.
> 
> 
> 


According to this statement, the number of the impacted individuals is 600, which is less than what Daichenko saw exposed. The Telegraph also states that none of them run any risks of exploitation since Diachenko was the first and last person to access the sensitive dataset.


Out of an abundance of caution, if you’re a subscriber to The Telegraph, we would suggest that you reset your password and remain vigilant against unsolicited emails that make bold claims or ask you to take urgent action to secure your account.




#### Tags:
[[]] [[Bleeping Computer]]
