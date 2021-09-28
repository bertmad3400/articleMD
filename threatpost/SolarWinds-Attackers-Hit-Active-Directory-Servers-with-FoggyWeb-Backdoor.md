# SolarWinds Attackers Hit Active Directory Servers with FoggyWeb Backdoor
### Microsoft is warning that the Nobelium APT is compromising single-sign-on servers to install a post-exploitation backdoor that steals data and maintains network persistence.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175056)
+ Date: September 28, 2021  10:39 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/28102455/foggyweb-e1632839155760.jpg)
The threat actors behind the notorious SolarWinds supply-chain attacks have dispatched new malware to steal data and maintain persistence on victims’ networks, researchers have found.


Researchers from the Microsoft Threat Intelligence Center (MSTIC) have observed the APT it calls Nobelium using a post-exploitation backdoor dubbed FoggyWeb, to attack Active Directory Federation Services (AD FS) servers. AD FS enables single sign-on (SSO) across cloud-based apps in a Microsoft environment, by sharing digital identity and entitlements rights.


The attacks started as far back as April, Ramin Nafisi from MSTIC wrote in a [blog post](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/) published Monday.


Nobelium is employing “multiple tactics to pursue credential theft” to gain admin privileges to AD FS servers, Nafisi wrote. Then, once a server is compromised, the threat group deploys FoggyWeb “to remotely exfiltrate the configuration database of compromised AD FS servers, decrypted [token-signing certificates](https://docs.microsoft.com/windows-server/identity/ad-fs/design/token-signing-certificates) and [token-decryption certificates](https://docs.microsoft.com/windows-server/identity/ad-fs/design/certificate-requirements-for-federation-servers),” he said, which can be used to penetrate into users’ cloud accounts.


In addition to remotely exfiltrating sensitive data, FoggyWeb also achieves persistence and communicates with a a command-and-control (C2) server to receive additional malicious components and execute them, Nafisi added.


**Backdoor Breakdown**
----------------------


Nafisi provides a thorough breakdown of the sophisticated FoggyWeb backdoor, which operates by allowing abuse of the Security Assertion Markup Language (SAML) token in AD FS, he explained in the post.


“The backdoor configures HTTP listeners for actor-defined URIs that mimic the structure of the legitimate URIs used by the target’s AD FS deployment,” Nafisi wrote. “The custom listeners passively monitor all incoming HTTP GET and POST requests sent to the AD FS server from the intranet/internet and intercept HTTP requests that match the custom URI patterns defined by the actor.”


Attackers store the malware in an encrypted file called *Windows.Data.TimeZones.zh-PH.pri*, while the malicious file *version.dll* acts as a loader. The DLL file leverages the CLR hosting interfaces and APIs to load FoggyWeb, a managed DLL, in the same Application Domain within which legitimate AD FS managed code is executed.


In this way, FoggyWeb gains access to the AD FS codebase and resources, including the AD FS configuration database. The malware also inherits AD FS service account permissions that are required to access the AD FS configuration database, Nafisis wrote.


Additionally, “because FoggyWeb is loaded into the same application domain as the AD FS managed code, it gains programmatical access to the legitimate AD FS classes, methods, properties, fields, objects and components that are subsequently leveraged by FoggyWeb to facilitate its malicious operations,” he added.


Moreover, FoggyWeb is also AD FS version-agnostic, which means it doesn’t need to keep track of legacy versus modern configuration table names and schemas, named pipe names and other version-dependent properties of AD FS, Nafisi wrote.


**Malware Mitigation**
----------------------


Microsoft has notified all customers observed being targeted or compromised by FoggyWeb, as well as included a comprehensive list of compromise indicators in the post.


The company also has recommended several mitigation actions for organizations, including: Auditing of on-premises and cloud infrastructure to identify any changes the actor might have made to maintain access; removing user and app access, reviewing configurations for each, and re-issuing new, strong credentials; and using a hardware security module to prevent the exfiltration of sensitive data.


Microsoft also is advising that all customers review their AD FS Server configuration and implement whatever changes are needed to secure the systems from attacks.


**Tracking a Known Threat Actor**
---------------------------------


Microsoft researchers have been keeping a wary eye on Nobelium since the company [got caught up](https://threatpost.com/microsoft-solarwinds-spy-attack-federal-agencies/162414/) in the [SolarWinds attack](https://threatpost.com/solarwinds-default-password-access-sales/162327/) that was first discovered late last year. They’ve been tracking the threat group’s activity and capabilities, which have expanded as the actors have built and deployed new malware.


Since [the SolarWinds incident](https://threatpost.com/dhs-sophisticated-cyberattack-foreign-adversaries/162242/), researchers have observed Nobelium steadily building out its arsenal beyond the Sunburst/Solorigate backdoor and Teardrop malware it initially deployed in that attack, which affected tens of thousands of organizations around the globe.


The group used malware called [Raindrop](https://threatpost.com/solarwinds-malware-arsenal-raindrop/163153/) in follow-on SolarWinds attacks, then later added [GoldMax, GoldFinder and Sibot](https://threatpost.com/solarwinds-malware-arsenal-raindrop/163153/) malware for layered persistence to its toolset.


Microsoft researchers also identified EnvyScout, BoomBox, NativeZone and VaporRage as four pieces of malware that were used in a Nobelium [email-based attack chain](https://threatpost.com/solarwinds-nobelium-phishing-attack-usaid/166531/) earlier this year.


***Rule #1 of Linux Security:****No cybersecurity solution is viable if you don’t have the basics down.*[***JOIN***](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)*Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the*[***4 Golden Rules of Linux Security***](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)*. Your top takeaway will be a Linux roadmap to getting the basics right!*[***REGISTER NOW***](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)*and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.*


 




#### Tags:
[[malware]] [[FoggyWeb]] [[Microsoft]] [[Nafisi]] [[Linux]] [[SolarWinds]] [[wrote.]] [[FoggyWeb,]] [[HTTP]] [[ThreatPost]]
