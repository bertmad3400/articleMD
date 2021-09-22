# Microsoft Exchange Autodiscover bugs leak 100K Windows credentials
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-exchange-autodiscover-bugs-leak-100k-windows-credentials/)
+ Date: September 22, 2021
+ Author: Lawrence Abrams


## Article:
![Microsoft Exchange](https://www.bleepstatic.com/content/hl-images/2021/03/10/Exchange4.jpg)


Bugs in the implementation of Microsoft Exchange's Autodiscover feature have leaked approximately 100,000 login names and passwords for Windows domains worldwide.


In a new report by Amit Serper, Guardicore's AVP of Security Research, the researcher reveals how the incorrect implementation of the Autodiscover protocol, rather than a bug in Microsoft Exchange,  is causing Windows credentials to be sent to third-party untrusted websites.


Before we get to the meat of the issue, it is important to take a quick look at Microsoft Exchange's Autodiscover protocol and how it's implemented.


What is Microsoft Exchange Autodiscover
---------------------------------------


Microsoft Exchange uses an [Autodiscover feature](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/autodiscover-for-exchange) to automatically configure a user's mail client, such as Microsoft Outlook, with their organization's predefined mail settings.


When an Exchange user enters their email address and password into an email client, such as Microsoft Outlook, the mail client then attempts to authenticate to various Exchange Autodiscover URLs.


During this authentication process, the login name and password are sent automatically to the Autodiscover URL.



![Microsoft Outlook trying to configure account using Autodiscover](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/e/exchange/autodiscover-credentials-leak/connecting-to-autodiscover-urls.jpg)**Microsoft Outlook trying to configure account using Autodiscover**  
*Source: Guardicore*
The Autodiscover URLs that will be connected to are derived from the email address configured in the client.


For example, when Serper tested this feature using the email 'amit@example.com', he found that the mail client tried to authenticate to the following Autodiscover URLs:


* https://Autodiscover.example.com/Autodiscover/Autodiscover.xml
* http://Autodiscover.example.com/Autodiscover/Autodiscover.xml
* https://example.com/Autodiscover/Autodiscover.xml
* http://example.com/Autodiscover/Autodiscover.xml


The mail client would try each URL until it was successfully authenticated to the Microsoft Exchange server and configuration information was sent back to the client.


Leaking credentials to external domains
---------------------------------------


If the client could not authenticate to the above URLs, Serper found that some mail clients, including Microsoft Outlook, would perform a "back-off" procedure. This procedure attempts to create additional URLs to authenticate to, such as the autodiscover.[tld] domain, where the TLD is derived from the user's email address.


In this particular case, the URL generated is http://Autodiscover.com/Autodiscover/Autodiscover.xml.


In a new report by Amit Serper, Guardicore's AVP of Security Research, the researcher reveals how the incorrect implementation of the Autodiscover protocol is causing mail clients to authenticate to untrusted domains, such as autodiscover.com, which is where the trouble begins.


As the email user's organization does not own this domain, and credentials are automatically sent to the URL, it would allow the domain owner to collect any credentials sent to them.


To test this, Guardicore registered the following domains and set up web servers on each to see how many credentials would be leaked by the Microsoft Exchange Autodiscover feature.


* Autodiscover.com.br - Brazil
* Autodiscover.com.cn - China
* Autodiscover.com.co - Columbia
* Autodiscover.es - Spain
* Autodiscover.fr - France
* Autodiscover.in - India
* Autodiscover.it - Italy
* Autodiscover.sg - Singapore
* Autodiscover.uk - United Kingdom
* Autodiscover.xyz
* Autodiscover.online


After these domains were registered and used, Serper found that email clients, including Microsoft Outlook, sent many account credentials using Basic authentications, making them easily viewable.



![Email client connecting to an autodiscover.xyz URL](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/e/exchange/autodiscover-credentials-leak/autodiscover-tld.jpg)**Email client connecting to an autodiscover.xyz URL**  
*Source: Guardicore*
For Microsoft Outlook clients that sent credentials using NTLM and Oauth, Serper created an attack dubbed "The ol' switcheroo" that would force the client to downgrade the request to a Basic authentication request.


This would once again allow the researcher to access the clear-text passwords for the user.



![Attack forcing the client to downgrade to Basic authentication](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Attack forcing the client to downgrade to Basic authentication**  
*Source: Guardicore*
When conducting these tests between April 20th, 2021, and August 25th, 2021, Guardicore servers received a:


* 648,976 HTTP requests targeting their Autodiscover domains.
* 372,072 Basic authentication requests.
* 96,671 unique pre-authenticated requests.


Guardicore says the domains that sent their credentials include:


* Publicly traded companies in the Chinese market
* Food manufacturers
* Investment banks
* Power plants
* Power delivery
* Real estate
* Shipping and logistics
* Fashion and Jewelry


Mitigating the Microsoft Exchange Autodiscover leaks
----------------------------------------------------


Serper has provided a few suggestions that organizations and developers can use to mitigate these Microsoft Exchange Autodiscover leaks.


For organizations using Microsoft Exchange, you should block all Autodiscover.[tld] domains at your firewall or DNS server so that your devices cannot connect to them. Guardicore has created a [text file containing all Autodiscover domains](https://github.com/guardicore/labs_campaigns/tree/master/Autodiscover) that can be used to create access rules.


Organizations are also recommended to disable Basic authentication, as it essentially sends credentials in cleartext.


For software developers, Serper recommends users prevent their mail clients from failing upwards when constructing Autodiscover URLs so that they never connect to Autodiscover.[tld] domains.




#### Tags:
[[Microsoft]] [[Autodiscover]] [[Guardicore]] [[Serper]] [[Outlook,]] [[URLs]] [[Bleeping Computer]]
