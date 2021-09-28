# New Microsoft Exchange service mitigates high-risk bugs automatically
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/new-microsoft-exchange-service-mitigates-high-risk-bugs-automatically/)
+ Date: September 28, 2021
+ Author: Sergiu Gatlan


## Article:
![New Microsoft Exchange service mitigates high-risk bugs automatically](https://www.bleepstatic.com/content/hl-images/2021/09/28/Exchange_headpic.jpg)


Microsoft has added a new Exchange Server feature that automatically applies interim mitigations for high-risk (and likely actively exploited) security flaws to secure on-premises servers against incoming attacks and give admins more time to apply security updates.


This update comes after multiple Microsoft Exchange zero-day vulnerabilities were exploited [[1](https://www.bleepingcomputer.com/news/security/more-hacking-groups-join-microsoft-exchange-attack-frenzy/), [2](https://www.bleepingcomputer.com/news/microsoft/microsoft-exchange-servers-are-getting-hacked-via-proxyshell-exploits/)] by state-sponsored and financially motivated hacking groups to compromise servers whose admins had no patch or mitigation info available.


Automated protection for vulnerable Exchange servers
----------------------------------------------------


The new Exchange Server component, aptly named Microsoft Exchange Emergency Mitigation (EM) service, builds upon Microsoft's [Exchange On-premises Mitigation Tool](https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-one-click-exchange-on-premises-mitigation-tool/) (EOMT) released in March to help customers minimize the attack surface exposed by [the ProxyLogon bugs](https://www.bleepingcomputer.com/tag/proxylogon/).


EM runs as a Windows service on Exchange Mailbox servers and it will be automatically installed on servers with the Mailbox role after deploying the September 2021 (or later) CU on Exchange Server 2016 or Exchange Server 2019.


It works by detecting Exchange Servers vulnerable to one or more known threats and applies interim mitigations until a security update is available for admins to install.


Mitigations applied automatically through the EM service are temporary fixes until the Security Update that fixes the vulnerability can be installed and are not a replacement for Exchange SUs. 


Once installed on an Exchange email server, the EM service can apply three types of mitigations:


* **IIS URL Rewrite rule mitigation:**a rule that blocks specific patterns of malicious HTTP requests that can endanger an Exchange server.
* **Exchange service mitigation:** disables a vulnerable service on an Exchange server.
* **App Pool mitigation**: disables a vulnerable app pool on an Exchange server.


Optional feature that can be disabled
-------------------------------------


"This new service is not a replacement for installing Exchange Server Security Updates (SUs), but it is the fastest and easiest way to mitigate the highest risks to Internet-connected, on-premises Exchange servers prior to installing applicable SUs," the Exchange Team explained.


EM is an EOMT version built within Exchange Server that works with the cloud-based Office Config Service (OCS) to download and protect against high-risk bugs with known mitigations.


Admins can [disable the EM service](https://docs.microsoft.com/en-us/exchange/exchange-emergency-mitigation-service?view=exchserver-2019#disabling-auto-apply-of-mitigations-through-em-service) if they don't want Microsoft to apply mitigations to their Exchange servers automatically.


They can also [control applied mitigations](https://docs.microsoft.com/en-us/exchange/exchange-emergency-mitigation-service?view=exchserver-2019#viewing-applied-mitigations) using PowerShell cmdlets and scripts, which allow viewing, reapplying, blocking, or removing mitigations.


"Our plan is to release mitigations only for the most severe security issues, such as issues that are being actively exploited in the wild," the Exchange Team [added](http://techcommunity.microsoft.com/t5/exchange-team-blog/new-security-feature-in-september-2021-cumulative-update-for/ba-p/2783155).


"Because applying mitigations may reduce server functionality, we plan on releasing mitigations only when the highest impact or severity issues are found."




#### Tags:
[[mitigations]] [[Microsoft]] [[admins]] [[mitigation:]] [[server.]] [[Bleeping Computer]]
