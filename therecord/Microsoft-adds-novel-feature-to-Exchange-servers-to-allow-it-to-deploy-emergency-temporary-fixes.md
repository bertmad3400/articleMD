# Microsoft adds novel feature to Exchange servers to allow it to deploy emergency temporary fixes
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/microsoft-adds-novel-feature-to-exchange-servers-to-allow-it-to-deploy-emergency-temporary-fixes/)
+ Date: September 27, 2021
+ Author: Catalin Cimpanu


## Article:
![Microsoft adds novel feature to Exchange servers to allow it to deploy emergency temporary fixes](https://therecord.media/wp-content/uploads/2021/03/Microsoft-Exchange.png)

Microsoft will roll out tomorrow a new security feature for its Exchange email servers, which have been at the center of several hacking campaigns over the past two years.


Called the **Microsoft Exchange Emergency Mitigation (EM) service**, the new feature works by automatically installing temporary mitigations that block active exploitation of security flaws until Microsoft is ready to release official patches.


The EM service will be enabled by default for all Exchange servers once they install the [September 2021 Cumulative Updates (CUs)](https://techcommunity.microsoft.com/t5/exchange-team-blog/new-security-feature-in-september-2021-cumulative-update-for/ba-p/2783155) for Exchange servers, which are shipping out tomorrow, after Microsoft [delayed](https://techcommunity.microsoft.com/t5/exchange-team-blog/delay-of-september-2021-cumulative-update-for-exchange-server/ba-p/2758450) their release last week to have more time to work on it.


Under the hood, the feature will work by connecting to the Office Config Service (OCS) and downloading mitigations (in the form of XML rules) from the following URL:


***[officeclient.microsoft.com/getexchangemitigations](https://officeclient.microsoft.com/getexchangemitigations)***


These mitigations contain three types of configuration changes:


* **IIS URL Rewrite rule mitigation**. This is a rule that blocks specific patterns of malicious HTTP requests that can endanger an Exchange server.
* **Exchange service mitigation**. This disables a vulnerable service on an Exchange server.
* **App Pool mitigation** This disables a vulnerable app pool on an Exchange server.


Once Microsoft detects a new attack, it will push out temporary mitigations via EM to all Exchange servers around the world and begin working on a software patch.


“Since in the future mitigations may be released at any time, we chose to have the EM service check for mitigations**hourly**,” the Microsoft Exchange team said last week.


For Exchange servers that are installed in highly secured environments, Microsoft is also providing a way to disable the EM service and let administrators apply mitigations by hand or by using the [Exchange On-premises Mitigation Tool](https://msrc-blog.microsoft.com/2021/03/15/one-click-microsoft-exchange-on-premises-mitigation-tool-march-2021/) (EOMT).


Instructions on disabling the EM service are available on this [documentation page](https://docs.microsoft.com/en-us/exchange/exchange-emergency-mitigation-service?view=exchserver-2019).


The EM service is one of the first-of-its-kind security features that can automatically deploy temporary fixes to a software app until a permanent fix is available.


Several security experts lauded Microsoft last week for its forward-thinking when it came to addressing the problem of deploying mitigations, most of which are complex configuration changes that typically need to be applied by hand. Furthermore, many are often applied incorrectly or are left incomplete when users accidentally skip or miss a step, leaving their systems still vulnerable to attacks.









#### Tags:
[[Microsoft]] [[mitigations]] [[The Record]]
