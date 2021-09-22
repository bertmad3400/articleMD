# Microsoft Exchange Autodiscover bug leaks hundreds of thousands of domain credentials
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/microsoft-exchange-autodiscover-bug-leaks-hundreds-of-thousands-of-domain-credentials/)
+ Date: September 22, 2021
+ Author: Catalin Cimpanu


## Article:
![Microsoft Exchange Autodiscover bug leaks hundreds of thousands of domain credentials](https://therecord.media/wp-content/uploads/2021/03/Microsoft-Exchange.png)

Security researchers have discovered a design flaw in a feature of the Microsoft Exchange email server that can be abused to harvest Windows domain and app credentials from users across the world.


Discovered by Amit Serper, AVP of Security Research at security firm Guardicore, the bug resides in the [Microsoft Autodiscover protocol](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/autodiscover-for-exchange), a feature of Exchange email servers that allows email clients to automatically discover email servers, provide credentials, and then receive proper configurations.


[auto –>]


The protocol is a crucial part of Exchange email servers as it allows admins an easy way to make sure clients use proper SMTP, IMAP, LDAP, WebDAV, and other settings.


But to get these automatic configurations, email clients typically ping a series of predetermined URLs derived from the user’s email address domain:


* https://autodiscover.example.com/autodiscover/autodiscover.xml
* http://autodiscover.example.com/autodiscover/autodiscover.xml
* https://example.com/autodiscover/autodiscover.xml
* http://example.com/autodiscover/autodiscover.xml


Serper said he found that this autodiscovery mechanism used a “back-off” procedure in case it doesn’t find the Exchange server’s Autodiscover endpoint on the first try.



> This “back-off” mechanism is the culprit of this leak because it is always trying to resolve the autodiscover portion of the domain and it will always try to “fail up” so to speak. Meaning, the result of the next attempt to build an autodiscover URL would be: http://**autodiscover.com**/autodiscover/autodiscover.xml. This means that whoever owns autodiscover.com will receive all of the requests that can’t reach the original domain.
> 
> Amit Serper, AVP of Security Research, North America, Guardicore


Based on his finding, Serper said he registered a series of Autodiscover-based top-level domains that were still available online. This included:


* **Autodiscover.com.br** – Brazil
* **Autodiscover.com.cn** – China
* **Autodiscover.com.co** – Columbia
* **Autodiscover.es** – Spain
* **Autodiscover.fr** – France
* **Autodiscover.in** – India
* **Autodiscover.it** – Italy
* **Autodiscover.sg** – Singapore
* **Autodiscover.uk** – United Kingdom
* **Autodiscover.xyz**
* **Autodiscover.online**


The researcher said Guardicore ran honeypots on these servers in order to understand the scale of the problem.


For more than four months, between April 16, 2021, and August 25, 2021, Serper said these servers received hundreds of requests, complete with thousands of credentials, from users that were trying to set up their email clients, but their email clients were failing to find their employer’s proper Autodiscover endpoint.


“The interesting issue with a large amount of the request that we received was that there was no attempt on the client’s side to check if the resource is available or even exists on the server before sending an authenticated request,” Serper explained in a [report](https://www.guardicore.com/labs/autodiscovering-the-great-leak/) published today.


“Guardicore has captured 372,072 Windows domain credentials and 96,671 unique credentials from various applications such as Microsoft Outlook,” the researcher added.


While sifting to the domains that connected to their honeypots, Serper said he found credentials for companies from multiple verticals, such as:


* Food manufacturers
* Investment banks
* Power plants
* Power delivery
* Real estate
* Shipping and logistics
* Fashion and jewelry
* and publicly traded companies in the Chinese market


All the collected credentials came via unencrypted HTTP connections, but Serper also detailed in his report today ways to collect credentials from more secure forms of authentication such as NTLM and Oauth.


While Serper provided some mitigations to prevent these leaks for system administrators and email software makers, an update from Microsoft’s side to the Autodiscover protocol design would also be needed.


Microsoft did not return a request for comment seeking additional details on Guardicore’s discovery.





#### Tags:
[[Serper]] [[Microsoft]] [[Autodiscover]] [[The Record]]
