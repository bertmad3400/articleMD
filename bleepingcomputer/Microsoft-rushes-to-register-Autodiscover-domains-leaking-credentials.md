# Microsoft rushes to register Autodiscover domains leaking credentials
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-rushes-to-register-autodiscover-domains-leaking-credentials/)
+ Date: September 24, 2021
+ Author: Lawrence Abrams


## Article:
![Microsoft](https://www.bleepstatic.com/content/hl-images/2021/09/12/Microsoft-Defender.jpg)


Microsoft is rushing to register Internet domains used to steal Windows credentials sent from faulty implementations of the Microsoft Exchange Autodiscover protocol.


On Monday, Guardicore's Amit Serper [released new research](https://www.bleepingcomputer.com/news/microsoft/microsoft-exchange-autodiscover-bugs-leak-100k-windows-credentials/) about how the issue caused the exposure of close to 100,000 unique Windows and email credentials.


When users configure their Exchange accounts on email clients, the app will attempt to authenticate to various Autodiscover URLs associated with Microsoft Exchange servers for their organization. If a successful authentication occurs, the Exchange server will send back settings that the mail client should use.



![Microsoft Outlook using Autodiscover to retrieve settings](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/e/exchange/autodiscover-credentials-leak/connecting-to-autodiscover-urls.jpg)**Microsoft Outlook using Autodiscover to retrieve settings**
However, many mail clients, including some versions of Microsoft Outlook and Office 365, incorrectly implement the Autodiscover protocol causing them to try and authenticate to third-party autodiscover.[tld] URLs that are not related to a user's organization.


Examples of such domains include autodiscover.com, autodiscover.uk, and autodiscover.de.


Threat actors could register autodiscover.[tld] domains and begin collecting the leaked Windows and email credentials for attacks against the organization.


Microsoft rushes to register autodiscover domains
-------------------------------------------------


Research regarding faulty Microsoft Autodiscover protocol implementations leaking Windows credentials is not new, and Microsoft has been aware of the issue for years.


The research was first disclosed in a [Black Hat Asia 2017 briefing](https://www.blackhat.com/asia-17/briefings/schedule/#all-your-emails-belong-to-us-exploiting-vulnerable-email-clients-via-domain-name-collision-5301), together with a [formal research paper](https://www.blackhat.com/docs/asia-17/materials/asia-17-Nesterov-All-Your-Emails-Belong-To-Us-Exploiting-Vulnerable-Email-Clients-Via-Domain-Name-Collision-wp.pdf) explaining the leaks. Other researchers also said they have reported the issue to Microsoft in the past and were told it was not a bug.


However, after Serper released his report, Microsoft issued a statement to BleepingComputer indicating that the information was new to them.



> 
> "We are actively investigating and will take appropriate steps to protect customers. We are committed to coordinated vulnerability disclosure, an industry standard, collaborative approach that reduces unnecessary risk for customers before issues are made public. Unfortunately, this issue was not reported to us before the researcher marketing team presented it to the media, so we learned of the claims today." Jeff Jones, Sr. Director, Microsoft.
> 
> 
> 


Since then, Microsoft has been rushing to register any autodiscover.[tld] domains it can find to prevent them from being used to steal Windows credentials.



![Microsoft registering autodiscover domains](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/e/exchange/autodiscover-credentials-leak/autodiscover-registration.jpg)**Microsoft registering autodiscover domains**
At the time of this writing, BleepingComputer has confirmed that Microsoft registered at least 68 domains related to Autodiscover, which are listed below.





| autodiscover.af | autodiscover.tl | autodiscover.pn |
| autodiscover.ax | autodiscover.gf | autodiscover.pr |
| autodiscover.as | autodiscover.tf | autodiscover.re |
| autodiscover.ag | autodiscover.gl | autodiscover.rw |
| autodiscover.am | autodiscover.gp | autodiscover.lc |
| autodiscover.ac | autodiscover.gt | autodiscover.pm |
| autodiscover.by | autodiscover.gy | autodiscover.st |
| autodiscover.bj | autodiscover.ht | autodiscover.sn |
| autodiscover.bi | autodiscover.hn | autodiscover.sc |
| autodiscover.cm | autodiscover.hk | autodiscover.sl |
| autodiscover.cl | autodiscover.je | autodiscover.sx |
| autodiscover.do | autodiscover.ke | autodiscover.sk |
| autodiscover.tl | autodiscover.ly | autodiscover.sb |
| autodiscover.gf | autodiscover.li | autodiscover.so |
| autodiscover.tf | autodiscover.mg | autodiscover.so |
| autodiscover.gl | autodiscover.mw | autodiscover.gs |
| autodiscover.af | autodiscover.mq | autodiscover.com.es |
| autodiscover.ax | autodiscover.yt | autodiscover.org.es |
| autodiscover.as | autodiscover.mn | autodiscover.ch |
| autodiscover.ag | autodiscover.ms | autodiscover.tj |
| autodiscover.am | autodiscover.ma | autodiscover.tg |
| autodiscover.ac | autodiscover.na | autodiscover.tt |
| autodiscover.by | autodiscover.nz | autodiscover.ug |
| autodiscover.bj | autodiscover.ni | autodiscover.vi |
| autodiscover.bi | autodiscover.ng | autodiscover.uz |
| autodiscover.cm | autodiscover.nf | autodiscover.vu |
| autodiscover.cl | autodiscover.pa | autodiscover.vn |
| autodiscover.do | autodiscover.pe | autodiscover.wf |


BleepingComputer also knows of thirty-eight other domains registered since September 22nd whose owners are hidden behind privacy or WHOIS restrictions that were likely registered by Microsoft, researchers, or potentially threat actors.


The actual number of registered domains is likely far larger, as BleepingComputer has seen Microsoft register multiple autodiscover domains for the same TLD, such as autodiscover.com.es and autodiscover.org.es.


One domain, autodiscover.ch, has been registered since at least 2015 and uses microsoftonline.com as the DNS servers, but it is not clear who owns it.


While registering autodiscover.[tld] domains will block some of the leaks, Microsoft will need to issue fixes for the poor Autodiscover implementation in their Microsoft Outlook and Office 365 mail clients to resolve the issue further.


As other non-Microsoft applications also have faulty protocol implementations, Microsoft will also have to release guidance on how to properly create Autodiscover URLs so that credentials are not sent to untrustworthy domains.




#### Tags:
[[Microsoft]] [[Autodiscover]] [[Windows]] [[autodiscover.[tld]]] [[BleepingComputer]] [[URLs]] [[organization.]] [[autodiscover]] [[Bleeping Computer]]
