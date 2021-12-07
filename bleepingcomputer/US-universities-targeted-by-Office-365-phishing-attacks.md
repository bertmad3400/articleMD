# US universities targeted by Office 365 phishing attacks
### US universities are being targeted in multiple phishing attacks designed to impersonate college login portals to steal valuable Office 365 credentials.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/us-universities-targeted-by-office-365-phishing-attacks/
+ Date: 2021-12-07T15:23:12-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2020/08/10/Office-365.jpg)

![Office 365 phishing](https://www.bleepstatic.com/content/hl-images/2020/08/10/Office-365.jpg)


US universities are being targeted in multiple phishing attacks designed to impersonate college login portals to steal valuable Office 365 credentials.


The lures used in the latest campaigns include COVID-19 Delta and Omicron variants and various themes on how these allegedly impact the educational programs.


These campaigns are believed to be conducted by multiple threat actors starting in October 2021, with [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/university-targeted-credential-phishing-campaigns-use-covid-19-omicron-themes) sharing details on the tactics, techniques, and procedures (TTPs) used in the phishing attacks.


Targeting US universities
-------------------------


The phishing attack begins with an email that pretends to be information about the new Omicron variant, COVID-19 test results, additional testing requirements, or class changes.


These emails urge the recipient to click on an attached HTM file, which takes them to a cloned login page for their university's login portal.



![HTM attachment arriving with the phishing email](https://www.bleepstatic.com/images/news/u/1220909/Phishing/htm_attachment.jpg)**HTM attachment arriving with the phishing email**  
*Source: Proofpoint*
The samples published by Proofpoint look very convincing in terms of their appearance, and URLs use a similar naming pattern that includes the .edu top-level domain. 


For example, a phishing attack targeting students of Arkansas State University used an URL of sso2[.]astate[.]edu[.]boring[.]cf.



![Spoofed university page with a login section](https://www.bleepstatic.com/images/news/u/1220909/Phishing/vanderbilt.png)**Spoofed university page with a login section**  
*Source: Proofpoint*
Other examples of malicious domains set up to support the phishing campaign are given below:


* sso[.]ucmo[.]edu[.]boring[.]cf/Covid19/authenticationedpoint.html
* hfbcbiblestudy[.]org/demo1/includes/jah/[university]/auth[.]php*
* afr-tours[.]co[.]za/includes/css/js/edu/web/etc/login[.]php*
* traveloaid[.]com/css/js/[university]/auth[.]php*

HTM attachments are having great success in phishing lately because they enable actors to [smuggle malware](https://www.bleepingcomputer.com/news/security/microsoft-warns-of-surge-in-html-smuggling-phishing-attacks/) and assemble it on the target device. In this case, however, the HTM contains a link to a credential-stealing site.


In some cases (marked with an asterisk), these destinations are legitimate WordPress sites that were compromised to steal credentials, so no alarms will be raised by internet security or email protection tools when the victim lands on them.


Based on the URLs shared by Proofpoint, some of the universities targeted in these attacks include the University of Central Missouri, Vanderbilt, Arkansas State University, Purdue, Auburn, West Virginia University, and the University of Wisconsin-Oshkosh.


Snatching Duo OTPs
------------------


To bypass MFA (multi-factor authentication) protection on targeted university login pages, the threat actors have also created landing pages that spoof a DUO MFA page, which is used to steal the one-time passcodes sent to students and faculty.


After a victim enters their credentials on the spoofed login page, the victim is requested to enter the code they received via SMS on their phone so that actors can snatch it and use it directly to take over the account.



![Spoofing the Duo MFA system](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Spoofing the Duo MFA system**  
*Source: Proofpoint*
This step requires immediate action since OTPs have short expiration times. 


Implications
------------


Office 365 credentials can be used by malicious actors to access the corresponding email account, send messages to other users in the workgroup, divert payments, and further the phishing to steal more valuable accounts.


Additionally, the actor can access and exfiltrate sensitive information stored in the account’s OneDrive and SharePoint folders.


These phishing attacks could potentially lead to damaging BEC incidents and highly-disruptive ransomware infections for universities.


HTM files are opened in a browser, so technically, you can never be 100% safe. Do not give in to the curiosity if you receive one as an attachment in an unsolicited email.


Just mark the message as spam and delete it.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Education]] [[victim.industry.name=Education]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Phishing]] [[Proofpoint]] [[Htm]] [[Mfa]] [[Bleeping Computer]]

