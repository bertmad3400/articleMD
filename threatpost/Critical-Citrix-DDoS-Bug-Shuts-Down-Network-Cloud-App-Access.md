# Critical Citrix DDoS Bug Shuts Down Network, Cloud App Access
### The distributed computing vendor patched the flaw, affecting Citrix ADC and Gateway, along with another flaw impacting availability for SD-WAN appliances.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176183)
+ Date: November 10, 2021  1:24 pm
+ Author: Tara Seals


## Article:
![Citrix critical flaw XenMobile server](https://media.threatpost.com/wp-content/uploads/sites/103/2020/08/12095849/Citrix.jpg)
A critical security bug in the Citrix Application Delivery Controller (ADC) and Citrix Gateway could allow cyberattackers to crash entire corporate networks without needing to authenticate.


The two affected Citrix products (formerly the NetScaler ADC and Gateway) are used for application-aware traffic management and secure remote access, respectively. The federated working specialist pushed out a security patch on Tuesday for the vulnerability, tracked as CVE-2021-22955, which allows unauthenticated denial of service (DoS), due to uncontrolled resource consumption, according to [the advisory](https://support.citrix.com/article/CTX330728).


Citrix also addressed a lower-severity bug that is likewise due to uncontrolled resource consumption. It impacts both previous products, as well as the Citrix SD-WAN WANOP Edition appliance. The latter provides optimization for Citrix SD-WAN deployments, which enable secure connectivity and seamless access to virtual, cloud and software-as-a-service (SaaS) apps across enterprise and branch locations.


Tracked as CVE-2021-22956, the second flaw allows temporary disruption of: A device’s management GUI; the Nitro API for configuring and monitoring NetScaler appliances programmatically; and remote procedure call (RPC) communication, which is what essentially enables distributed computing in Citrix settings.


In terms of the impact of exploitation, all three products are widely deployed globally, with Gateway and ADC alone installed in at least 80,000 companies in 158 countries as of early 2020, according to an assessment from Positive Technologies at the time.


Disruption to any of the appliances could prevent remote and branch access to corporate resources and general blocking of cloud and virtual assets and apps.


All of this makes them an attractive target for cybercriminals, and indeed, the Citrix ADC and Gateway in particular are no spring chickens when it comes to the critical vulnerability scene.


In the summer of 2020, multiple vulnerabilities [were discovered](https://threatpost.com/citrix-bugs-allow-unauthenticated-code-injection-data-theft/157214/) that would allow code injection, information disclosure and denial of service, with many exploitable by an unauthenticated, remote attacker. And, in December of 2019, a critical RCE bug [was disclosed](https://threatpost.com/critical-citrix-bug-80000-corporate-lans-at-risk/151444/) as a zero-day that took the vendor weeks to patch.


**Few Technical Details, Many Affected Products**
-------------------------------------------------


While Citrix didn’t release technical details on the latest bugs, VulnDB [noted on Wednesday](https://vuldb.com/?id.186468) that for CVE-2021-22955, “the exploitability is told to be difficult. The attack can only be initiated within the local network. The exploitation doesn’t require any form of authentication.” It assigned a severity score of 5.1 out of 10 to the bug, despite Citrix’ internal rating of “critical.”


The site also reported that exploits are calculated to be worth up to $5,000, and noted that “manipulation with an unknown input leads to a denial of service vulnerability…This is going to have an impact on availability.”


The vendor said the vulnerabilities affect the following supported versions:


Citrix ADC and Citrix Gateway (CVE-2021-22955 and CVE-2021-22956):


Citrix SD-WAN WANOP Edition (CVE-2021-22956):


In the case of the first Citrix ADC and Gateway bug, appliances must be configured as a VPN or AAA virtual server in order to be vulnerable.


In the second bug’s case, appliances must have access to NSIP or SNIP with management interface access.


Customers using Citrix-managed cloud services are unaffected.


***Want to win back control of the flimsy passwords standing between your network and the next cyberattack? Join Darren James, head of internal IT at Specops, and Roger Grimes, data-driven defense evangelist at KnowBe4, to find out how during a free, LIVE Threatpost event,*** [***“Password Reset: Claiming Control of Credentials to Stop Attacks,”***](https://bit.ly/3bBMX30) ***on Wed., Nov. 17 at 2 p.m. ET. Sponsored by Specops.***


[***Register NOW***](https://bit.ly/3bBMX30)***for the LIVE event and submit questions ahead of time to Threatpost’s Becky Bracken at***[***becky.bracken@threatpost.com***](mailto:becky.bracken@threatpost.com)***.***


.




#### Tags:
[[Citrix]] [[SD-WAN]] [[cloud]] [[ThreatPost]]
