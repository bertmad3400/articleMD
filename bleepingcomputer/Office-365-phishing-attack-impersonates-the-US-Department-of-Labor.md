# Office 365 phishing attack impersonates the US Department of Labor
### A new phishing campaign impersonating the United States Department of Labor asks recipients to submit bids to steal Office 365 credentials.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/office-365-phishing-attack-impersonates-the-us-department-of-labor/
+ Date: 2022-01-19T06:00:00-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/08/USA_flag.jpg)

![us-flag](https://www.bleepstatic.com/content/hl-images/2021/12/08/USA_flag.jpg?rand=145695813)


A new phishing campaign impersonating the United States Department of Labor asks recipients to submit bids to steal Office 365 credentials.


The phishing campaign has been ongoing for at least a couple of months and utilizes over ten different phishing sites impersonating the government agency.


Spoofed addresses and server abuse
----------------------------------


In a new report by email security firm [INKY](https://www.inky.com/blog/fresh-phish-phishers-lure-victims-with-fake-invites-to-bid-on-nonexistent-federal-projects), who shared the report with Bleeping Computer before publication, researchers illustrated how the phishing attack is used to steal credentials.


The emails are sent from spoofed domains that look as if they came from the actual Department of Labor (DoL) site, while some are based on a set of newly created look-alike domains such as:


* dol-gov[.]com
* dol-gov[.]us
* bids-dolgov[.]us

Most of the emails pass through abused servers owned by non-profit organizations to evade email security blocks.



![email headers reflecting the bouncing](https://www.bleepstatic.com/images/news/u/1220909/Phishing/email-headers.jpg)**Email headers reflecting the bouncing**  
*Source: INKY*
In other cases, they are sent through newly registered and unreported domains that aren't yet included on anti-phishing lists.


The sender pretends to be a senior DoL employee who invites the recipient to submit their bid for an ongoing government project.



![Email sample used in the campaign](https://www.bleepstatic.com/images/news/u/1220909/Phishing/email-sample.jpg)**Sample of the email used in the campaign**  
*Source: INKY*
The emails contain a valid letterhead, professionally-arranged content, and a three-page PDF attachment of a seemingly legitimate form.



![The button that leads to the phishing site](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**The button that leads to the phishing site**  
*Source: INKY*
The PDF contains a "BID" button, which, if clicked, takes the victim to one of the phishing sites. INKY has confirmed the following landing pages as part of this campaign:


* opendolbid[.]us
* usdol-gov[.]com
* bid-dolgov[.]us
* us-dolbids[.]us
* dol-bids[.]us
* openbids-dolgov[.]us
* open-biddolgov[.]us
* openbids-dolgov[.]com
* usdol-gov[.]us
* dolbids[.]com
* openbid-dolgov[.]us
* dol[.]global

The spoofed site looks convincing, containing identical HTML and CSS to the real one. The threat actors have even included an instructions pop-up message to direct victims through the bidding (phishing) process.



![Instructions message on one of the phishing sites](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Instructions message on one of the phishing sites**  
*Source: INKY*
Those who bid for a project will be taken to a credential harvesting form that targets their Microsoft Office 365 email address and password.



![Stealing victim's credentials](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Stealing Microsoft Office 365 credentials**  
*Source: INKY*
No matter what's inputted there, the website returns a bogus error to trick the victim into entering them again, thus reducing the chances of stealing mistyped credentials.


If the victim falls for the trap for a second time, they are eventually re-directed to the actual DoL site, left with little evidence as to what exactly has happened.


Similar campaigns on the rise
-----------------------------


This campaign's level of sophistication and diligence in setting up convincing web pages and writing error-free phishing emails is worrying.


We saw [something similar](https://www.bleepingcomputer.com/news/security/phishing-attacks-impersonate-pfizer-in-fake-requests-for-quotation/) in December 2021, with phishing actors impersonating Pfizer and using well-crafted PDF attachments to invite recipients to submit bids to the pharmaceutical company.


In this case, the actors take things one step further by abusing legitimate mail servers to send their phishing lures.


Unfortunately, all that leaves email recipients with is very subtle evidence of the trickery targeting them, so ultimate vigilance is advised.


In this case, the most obvious sign of the scam would be the Department of Labor requiring anyone to log in with Office 365 credentials to view a document, something that isn't the case on any U.S. government website.





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Mis-Type]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=RTM]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=Dili]] [[victim.country.name=East Timor]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Phishing]] [[Emails]] [[Pdf]] [[Bleeping Computer]]

