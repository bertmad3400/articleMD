# Meet Balikbayan Foxes: a threat group impersonating the Philippine gov't
### The gang is also taking advantage of COVID-19 to propagate Trojan malware.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/proofpoint-unmasks-balikbayan-foxes-a-threat-group-impersonating-the-philippine-govt/)
+ Date: October 27, 2021
+ Author: Charlie Osborne


## Article:
Unknown

Proofpoint has uncovered a new, "highly active" threat group that is impersonating the Philippine government and businesses to spread Trojan malware. 


On Wednesday, researchers Selena Larson and Joe Wise said the threat actors, dubbed "Balikbayan Foxes" and [tracked as TA2722](https://www.proofpoint.com/us/blog/threat-insight/new-threat-actor-spoofs-philippine-government-covid-19-health-data-widespread), are concentrated in the Philippines but are targeting the shipping, logistics, manufacturing, pharmaceutical, business, and energy sectors across the US, Europe, and Asia. 

Balikbayan Foxes has conducted campaigns over 2021 in which the group sent phishing emails claiming to be from Philippine government entities including the country's department of health, employment agency, and customs.  

In addition, the threat actors have impersonated DHL Philippines -- DHL being a common victim of impersonation worldwide as a delivery service -- and the Manila embassy for the Kingdom of Saudi Arabia (KSA). 

According to the researchers, phishing, spoofed email addresses, and emailed lures are used to snag their victims. These included messages surrounding COVID-19 infection rates, billing, invoicing, and industry advisories. 

Some of the targets are involved in large supply chains, and so if compromised, these attacks could have a far-reaching impact.  

Every campaign tracked by Proofpoint was designed to deploy the Remcos and NanoCore Remote Access Trojans (RATs) for the purposes of surveillance and data theft. 






In some cases, phishing emails were sent containing OneDrive links to malicious .RAR files, whereas in others, crafted .PDFs were attached that contained embedded URLs to malicious executables. The group also utilized another common malware payload deployment method -- Office documents containing macros which, when enabled, triggered Trojan execution.  

Proofpoint believes the threat actor's activities may go back as far as August 2020 based on the activities of multiple clusters and command-and-control (C2) servers now tied to Balikbayan Foxes.  

Recently, the group appears to be expanding its tactics to also include credential harvesting. In September, the name of the Philippines Bureau of Customs CPRS was used to persuade victims to visit a malicious domain and to submit account details in business email compromise (BEC) scams. 

Of interest is that a single email address tied to multiple IPs associated with this wave of attacks has also been connected with [2017 campaigns](https://abuse.ch/blog/adwind-a-cross-plattform-rat/) designed to deploy the Adwind/jRAT Trojan, which has been available to criminals as a malware-as-a-service offering since 2016.  

###  Previous and related coverage

* [New advanced hacking group targets governments, engineers worldwide](https://www.zdnet.com/article/new-advanced-hacking-group-targets-governments-engineers-worldwide/)
* [ESET discovers a rare APT that stayed undetected for nine years](https://www.zdnet.com/article/eset-discovers-a-rare-apt-that-stayed-undetected-for-nine-years/)
* [Chinese APT LuminousMoth abuses Zoom brand to target gov't agencies](https://www.zdnet.com/article/chinese-apt-luminousmoth-abuses-zoom-brand-to-target-govt-agencies/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Proofpoint]] [[ZDNet]]
