# Microsoft Exchange ‘ProxyToken’ Bug Allows Email Snooping
### The bug (CVE-2021-33766) is an information-disclosure issue that could reveal victims’ personal information, sensitive company data and more.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169030)
+ Date: August 30, 2021  1:31 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26141726/Windows-Abstract.jpg)
A serious security vulnerability in Microsoft Exchange Server that researchers have dubbed ProxyToken could allow an unauthenticated attacker to access and steal emails from a target’s mailbox.


Microsoft Exchange uses two websites; one, the front end, is what users connect to in order to access email. The second is a back-end site that handles the authentication function.


“The front-end website is mostly just a proxy to the back end. To allow access that requires forms authentication, the front end serves pages such as /owa/auth/logon.aspx,” according to a [Monday posting](https://www.zerodayinitiative.com/blog/2021/8/30/proxytoken-an-authentication-bypass-in-microsoft-exchange-server) on the bug from Trend Micro’s Zero Day Initiative. “For all post-authentication requests, the front end’s main role is to repackage the requests and proxy them to corresponding endpoints on the Exchange Back End site. It then collects the responses from the back end and forwards them to the client.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The issue arises specifically in a feature called “Delegated Authentication,” where the front end passes authentication requests directly to the back end. These requests contain a SecurityToken cookie that identify them; i.e., if the front end finds a non-empty cookie named SecurityToken, it delegates authentication to the back end. However, Exchange has to be specifically configured to have the back end perform the authentication checks; in a default configuration, the module responsible for that (the “DelegatedAuthModule”) isn’t loaded.


“When the front end sees the SecurityToken cookie, it knows that the back end alone is responsible for authenticating this request,” according to ZDI. “Meanwhile, the back end is completely unaware that it needs to authenticate some incoming requests based upon the SecurityToken cookie, since the DelegatedAuthModule is not loaded in installations that have not been configured to use the special delegated authentication feature. The net result is that requests can sail through, without being subjected to authentication on either the front or back end.”


From there, attacker could install a forwarding rule allowing them to read the victim’s incoming mail.


“With this vulnerability, an unauthenticated attacker can perform configuration actions on mailboxes belonging to arbitrary users,” according to the post. “As an illustration of the impact, this can be used to copy all emails addressed to a target and account and forward them to an account controlled by the attacker.”


ZDI outlined an exploitation scenario wherein an attacker has an account on the same Exchange server as the victim. However, if an administrator permits forwarding rules having arbitrary internet destinations, no Exchange credentials are needed at all, researchers noted.


The bug ([CVE-2021-33766](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-33766)) was reported to the Zero Day Initiative by researcher Le Xuan Tuyen of VNPT ISC, and it was patched by Microsoft in the July Exchange cumulative updates. Organizations should update their products to avoid compromise.


The ProxyToken revelation comes after [the disclosure of](https://threatpost.com/attackers-target-proxylogon-cryptojacker/165418/) ProxyLogon in early March; that’s an exploit chain comprised of four Exchange flaws (CVE-2021-26855, CVE-2021-26857, CVE-2021-26858, CVE-2021-27065), which together create a pre-authentication remote code execution (RCE) exploit. Attackers can take over unpatched servers without knowing any valid account credentials, giving them access to email communications and the opportunity to install a web shell for further exploitation within the environment. ProxyLogon was weaponized in [wide-scale attacks](https://threatpost.com/fbi-proxylogon-web-shells/165400/) throughout the spring.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Microsoft]] [[end.]] [[SecurityToken]] [[ThreatPost]]
