# Microsoft Exchange ProxyToken bug can let hackers steal user email
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/microsoft-exchange-proxytoken-bug-can-let-hackers-steal-user-email/)
+ Date: August 30, 2021
+ Author: Ionut Ilascu


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/03/06/microsoft-exchange-header.jpg)


Technical details have emerged on a serious vulnerability in Microsoft Exchange Server dubbed ProxyToken that does not require authentication to access emails from a target account.


An attacker can exploit the vulnerability by crafting a request to web services within the Exchange Control Panel (ECP) application and steal messages from a victim’s inbox.


### Delegation confusion


Tracked as CVE-2021-33766, ProxyToken gives unauthenticated attackers access to the configuration options of user mailboxes, where they can define an email forwarding rule.


As a result, email messages intended for a target user can also be delivered to an account that the attacker controls.


The bug was discovered by Le Xuan Tuyen, a researcher at the Information Security Center of Vietnam Posts and Telecommunications Group ([VNPT-ISC](http://sec.vnpt.vn/)) and reported through the [Zero-Day Initiative](https://www.zerodayinitiative.com/advisories/ZDI-21-798/) (ZDI) program in March.


He found that Microsoft Exchange’s frontend site (Outlook Web Access, Exchange Control Panel) functions largely as a proxy for the backend site (Exchange Back End), to which it passes authentication requests.


In Microsoft Exchange deployments where the “Delegated Authentication” feature is active, the frontend forwards the requests that need authentication to the backend, which identifies them by the presence of a ‘SecurityToken’ cookie.



!['SecurityToken' cookie necessary to exploit ProxyToken vulnerability in Microsoft Exchange Server](https://www.bleepstatic.com/images/news/u/1100723/2021/Vulnerabilities/ProxyTokenSecurityToken.jpg)source: ZDI
When there is a non-empty ‘SecurityToken’ cookie in a request within ‘/ecp’, the frontend delegates the authentication decision to the backend.


However, the default configuration of Microsoft Exchange does not load for the backend ECP site the module responsible for delegating the validation process (DelegatedAuthModule).



“In summary, when the front end sees the SecurityToken cookie, it knows that the back end alone is responsible for authenticating this request. Meanwhile, the back end is completely unaware that it needs to authenticate some incoming requests based upon the SecurityToken cookie since the DelegatedAuthModule is not loaded in installations that have not been configured to use the special delegated authentication feature” - [Zero-Day Initiative](http://www.zerodayinitiative.com/blog/2021/8/30/proxytoken-an-authentication-bypass-in-microsoft-exchange-server)



Exploiting the ProxyToken vulnerability is not complete without another issue, albeit a minor one: requests for the /ecp page need a ticket known as “ECP canary,” which can be obtained when triggering an HTTP 500 error.


As it turns out, requests without the ticket trigger the HTTP 500 error that contains the valid string necessary for successfully issuing an unauthenticated request.



![ECP canary string to exploit ProxyToken vulnerability in Microsoft Exchange Server](https://www.bleepstatic.com/images/news/u/1100723/2021/Vulnerabilities/ProxyTokenTicket.jpg)source: ZDI
A patch has been available from Microsoft since July, according to the company's [public advisory](https://www.bleepingcomputer.com/news/microsoft/microsoft-july-2021-patch-tuesday-fixes-9-zero-days-117-flaws/). Rapid7's [Tom Sellers notes](https://twitter.com/TomSellers/status/1432342969965760514) that version numbers and dates indicate that the patches had been released as early as April, though.


The vulnerability is not critical. NIST calculated its severity score at 7.5 out of 10. This is because an attacker needs an account on the same Exchange server as the victim.


As an example, a request from an attacker looks like this:



![HTTP request to trigger ProxyToken vulnerability in Microsoft Exchange Server](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)Caption
In a [blog post](http://www.zerodayinitiative.com/blog/2021/8/30/proxytoken-an-authentication-bypass-in-microsoft-exchange-server) today, the Zero-Day Initiative notes that some Exchange server administrators set a global configuration value that permits creating an email forwarding rule to an arbitrary destination. In such cases, the attacker needs no credentials.


### Exploit attempts


Although technical details for ProxyToken have been released only today, exploit attempts have been recorded as early as three weeks ago.


According to [Rich Warren](https://twitter.com/buffaloverflow), red teamer for NCC Group, he saw a larger number of exploitation attempts on August 10.



![ProxyToken exploit attempts](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)source: [Rich Warren](https://twitter.com/buffaloverflow/status/1432364885804036097)
As in the case of [ProxyShell vulnerabilities](https://www.bleepingcomputer.com/news/microsoft/microsoft-exchange-servers-scanned-for-proxyshell-vulnerability-patch-now/), if administrators of Microsoft Exchange servers have not installed the patches for ProxyToken, they should prioritize the task.




#### Tags:
[[Microsoft]] [[ProxyToken]] [[Zero-Day]] [[frontend]] [[source:]] [[Bleeping Computer]]
