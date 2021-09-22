# Microsoft Autodiscover abused to collect web requests, credentials
### Researchers were able to exploit a protocol design feature on a vast scale.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/design-flaw-in-microsoft-autodiscover-abused-to-leak-windows-domain-credentials/)
+ Date: September 22, 2021
+ Author: Charlie Osborne


## Article:
Unknown

A "design flaw" in the Microsoft Autodiscover protocol was subject to an investigation by researchers who found they were able to harvest domain credentials. 


On Wednesday, Guardicore Labs' AVP of Security Research Amit Serper published [the results](https://www.guardicore.com/labs/autodiscovering-the-great-leak/) of an analysis of Autodiscover, a protocol used to authenticate to Microsoft Exchange servers and to configure client access.  

There are different iterations of the protocol available for use. Guardicore explored an implementation of [Autodiscover](https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/pox-autodiscover-request-for-exchange?redirectedfrom=MSDN) based on POX XML and found a "design flaw" that can be exploited to 'leak' web requests to Autodiscover domains outside of a user's domain, as long as they were in the same top-level domain (TLD).  

To test out the protocol, the team first registered and purchased a number of domains with a TLD suffix, including Autodiscover.com.br, Autodiscover.com.cn, Autodiscover.com.fr, and Autodiscover.com.uk, and so on.  

These domains were then assigned to a Guardicore web server, and the researchers say they "were simply waiting for web requests for various Autodiscover endpoints to arrive." 

The "back-off" procedure is described as the "culprit" of the leak as failures to resolve URLs based on parsed, user-supplied email addresses will result in a "fail up": 

"Meaning, the result of the next attempt to build an Autodiscover URL would be: http://Autodiscover.com/Autodiscover/Autodiscover.xml," the researchers explained. "This means that whoever owns Autodiscover.com will receive all of the requests that cannot reach the original domain. [...] To our surprise, we started seeing significant amounts of requests to Autodiscover endpoints from various domains, IP addresses, and clients."






In total, Guardicore was able to capture 372,072 Windows domain credentials and 96,671 unique sets of credentials from sources including Microsoft Outlook and email clients between April 16 and August 25, 2021. Some sets were sent via HTTP basic authentication.

![screenshot-2021-09-20-at-14-21-26.png]()![screenshot-2021-09-20-at-14-21-26.png](https://www.zdnet.com/a/img/resize/fa9f3a4482547e79603b55d100f7a028e26d8f93/2021/09/20/c17f8640-4606-4e24-ab28-60978eb739ab/screenshot-2021-09-20-at-14-21-26.png?width=1200&fit=bounds&auto=webp)
 Guardicore
 Chinese companies, food manufacturers, utility firms, shipping and logistics organizations, and more were included.  

"The interesting issue with a large amount of the requests that we received was that there was no attempt on the client's side to check if the resource is available or even exists on the server before sending an authenticated request," the team explained.  

Guardicore was also able to create an attack method based on an attacker controlling relevant TLD domains which downgraded credentials sent to them in alternative authentication systems -- such as NTLM and OAuth -- to HTTP basic authentication. 

Serper told ZDNet, "the protocol flaw isn't new; we were just able to exploit it at a massive scale." 

Past research conducted by Shape Security and published in 2017 explores Autodiscover and its potential [for abuse](https://www.blackhat.com/docs/asia-17/materials/asia-17-Nesterov-All-Your-Emails-Belong-To-Us-Exploiting-Vulnerable-Email-Clients-Via-Domain-Name-Collision-wp.pdf) (.PDF). However, the paper focuses on Autodiscover implementations in mobile email clients. 

Guardicore says it has "initiated responsible disclosure processes with some of the vendors affected" by the latest discovery.

In order to mitigate this issue, Guardicore says that Autodiscover TLD domains should be blocked by firewalls, and when Exchange setups are being configured, support for basic authentication should be disabled -- as this is "the same as sending a password in clear text over the wire." 

ZDNet has reached out to Microsoft and we will update when we hear back.  

###  Previous and related coverage

* [Former AWS exec Charlie Bell to head new Microsoft Security, Compliance, Identity, and Management org](https://www.zdnet.com/article/former-aws-exec-charlie-bell-to-head-new-microsoft-security-compliance-identity-and-management-org/)  

* [Everything you need to know about the Microsoft Exchange Server hack](https://www.zdnet.com/article/everything-you-need-to-know-about-microsoft-exchange-server-hack/)  

* [UK and White House blame China for Microsoft Exchange Server hack](https://www.zdnet.com/article/uk-white-house-blames-china-for-microsoft-exchange-server-hack/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Autodiscover]] [[Guardicore]] [[Microsoft]] [[TLD]] [[ZDNet]]
