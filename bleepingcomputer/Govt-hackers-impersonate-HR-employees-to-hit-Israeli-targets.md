# Govt hackers impersonate HR employees to hit Israeli targets
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/govt-hackers-impersonate-hr-employees-to-hit-israeli-targets/)
+ Date: August 17, 2021
+ Author: Ionut Ilascu


## Article:
![Nation-state hackers impersonate HR employees to hit Israeli targets](https://www.bleepstatic.com/content/hl-images/2021/05/25/Iran-fingerprint.jpg)


Hackers associated with the Iranian government have focused attack efforts on IT and communication companies in Israel, likely in an attempt to pivot to their real targets.


The campaigns have been attributed to the Iranian APT group known as Lyceum, Hexane, and Siamesekitten, running espionage campaigns since at least 2018 [[1](https://www.bleepingcomputer.com/news/security/new-actors-attack-industrial-control-systems-old-ones-mature/), [2](https://www.bleepingcomputer.com/news/security/lyceum-hexane-threat-group-uses-common-hacking-tactics/)].


In multiple attacks detected in May and July, the hackers combined social engineering techniques with an updated malware variant that would ultimately give them remote access to the infected machine.


In one case, the hackers used the name of a former HR manager at technology company ChipPC to create a fake LinkedIn profile, a clear indication that the attackers did their homework before starting the campaign.



![Fake LinkedIn profile for ChipPC HR manager](https://www.bleepstatic.com/images/news/u/1100723/APT/Lyceum%20-%20Hexane/FakeLinkedInProfile_ClearSky.jpg)source:ClearSky
Threat researchers at cybersecurity company ClearSky in a [report](https://www.clearskysec.com/wp-content/uploads/2021/08/Siamesekitten.pdf) [PDF] today say that Siamesekitten actors then used the fake profile to deliver malware to potential victims under the pretext of a job offer:


1. Identifying the potential victim (employee)
2. Identifying the human resources department employee to impersonate
3. Creating a phishing website that impersonates the target organization
4. Creating lure files compatible with the impersonated organization
5. Setting up a fake profile on LinkedIn in the name of the HR employee
6. Contacting potential victims with an "alluring" job offer, detailing a position in the impersonated organization
7. Sending the victim to a phishing website with a lure file
8. A backdoor infects the system and connects to the C&C server over DNS and HTTPS
9. The DanBot RAT is downloaded to the infected system
10. Hackers get data for espionage purposes and try to spread on the network


ClearSky believes that Siamesekitten has spent months trying to breach a large number of organizations in Israel using supply chain tools.


While the threat actor’s interest seems to have changed from organizations in the Middle East and Africa, the researchers say that the IT and communication companies in Israel are just a means to getting to the real targets.



“We believe that these attacks and their focus on IT and communication companies are intended to facilitate supply chain attacks on their clients. According to our assessment, the group's main goal is to conduct espionage and utilize the infected network to gain access to their clients’ networks. As with other groups, it is possible that espionage and intelligence gathering are the first steps toward executing impersonation attacks targeting ransomware or wiper malware” - ClearSky



The researchers discovered two websites that are part of Siamesekitten’s infrastructure for the cyberespionage campaigns targeting companies in Israel.


One imitates the site of German enterprise software company Software AG and the other mimics the website of ChipPc. In both cases, the potential victim is asked to download an Excel (XLS) file that purportedly contains details about the job offer or the resume format.


The two files include a password-protected malicious macro that starts the infection chain by extracting a backdoor called MsNpENg.



![Extracting MsNpENg backdoor](https://www.bleepstatic.com/images/news/u/1100723/APT/Lyceum%20-%20Hexane/MsNpENgExtraction_ClearSky.jpg)source: ClearSky
ClearSky notes that between the two campaigns (May through July) they observed, Siamesekitten switched from an older backdoor version written in C++ and named Milan to a newer variant called Shark, which is written in .NET.


Today’s report [[PDF](https://www.clearskysec.com/wp-content/uploads/2021/08/Siamesekitten.pdf)] contains technical details for both variants along with IP addresses for the attacker’s infrastructure, email addresses used to register servers, and hashes for malicious files.




#### Tags:
[[ClearSky]] [[Siamesekitten]] [[website]] [[Bleeping Computer]]
