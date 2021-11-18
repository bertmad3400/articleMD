# Glitch service abused to host short-lived phishing sites
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/glitch-service-abused-to-host-short-lived-phishing-sites/)
+ Date: November 18, 2021
+ Author: Bill Toulas


## Article:
![glitch](https://www.bleepstatic.com/content/hl-images/2021/11/18/Glitch-hp.jpg?rand=1542190110)


Phishing actors are now actively abusing the Glitch platform to host short-lived credential-stealing URLs for free while evading detection and takedowns.


The recent campaigns are targeting employees at major corporations who work with the Middle East.


Based on an analysis by the DomainTools research team, this phishing campaign started in July 2021 and is still ongoing.


"Clean" PDFs that evade detection
---------------------------------


The actors send emails with PDF document attachments that do not contain any malicious code, so no antivirus alerts are generated.


Instead, these PDFs contain a link that directs the user to a page hosted at Glitch, which would display a landing page.


An example of the URL embedded in these PDF documents is shown below:


[DomainTools](https://www.domaintools.com/resources/blog/seeing-red?) sourced 70 PDFs of this type and found that they all used a unique email and URL to link to various Glitch-hosted "red.htm" pages.



![List of sites where PDFs point to](https://www.bleepstatic.com/images/news/u/1220909/Security/red_htm.jpg)**List of sites where PDFs point to**  
*Source: DomainTools*
Abusing Glitch
--------------


Glitch is a cloud hosting service that allows people to deploy apps and websites using Node.js, React, and other development platforms.


This platform is enticing for phishing attacks because they offer a free version that lets users create an app/page and keep it live on the web for five minutes. After that, the user has to enable it again manually.


Because Glitch is a generally trustworthy platform, network security tools treat its domains favorably, not serving warnings when visiting the site.


This favorable view by security platforms combined with the short-lived URLs and the fact that threat actors can host them for free makes Glitch an excellent target for abuse by phishing actors.


By digging deeper, DomainTools found a live Glitch site linked to a commercial malware sandbox service containing a screenshot of a Microsoft SharePoint phishing login page.



![SharePoint phishing page](https://www.bleepstatic.com/images/news/u/1220909/Phishing/sharepoint_page.jpg)**SharePoint phishing page**  
*Source: DomainTools*
The PDF document that led there had been submitted to VirusTotal so that researchers could tie the sample to several HTML documents.


After pulling these pages, the researchers found chunks of obfuscated JavaScript used for exfiltrating credentials to an email address after passing them through compromised WordPress sites.


The deobfuscation revealed an Outlook email address that received the stolen credentials, which led to the discovery of a set of additional PDFs created in September 2021.



![The JavaScript code used for URL re-direction](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**The JavaScript code used for URL re-direction**  
*Source: DomainTools*
The threat actors hosted these documents on various services similar to Glitch, such as Heroku, or through content distribution networks like SelCDN.


This means that Glitch was only one of the many channels the phishing actors abused to evade detection and steal credentials.


DomainTools has reached out to Glitch to inform them of their findings but hasn't received a response yet.




#### Tags:
[[DomainTools]] [[phishing]] [[PDFs]] [[PDF]] [[URL]] [[Bleeping Computer]]
