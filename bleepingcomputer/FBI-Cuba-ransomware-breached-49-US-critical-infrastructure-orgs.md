# FBI: Cuba ransomware breached 49 US critical infrastructure orgs
### The Federal Bureau of Investigation (FBI) has revealed that the Cuba ransomware gang has compromised the networks of at least 49 organizations from US critical infrastructure sectors.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/fbi-cuba-ransomware-breached-49-us-critical-infrastructure-orgs/
+ Date: 2021-12-03T12:16:45-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/11/10/FBI.jpg)

![FBI: Cuba ransomware breached 49 US critical infrastructure orgs](https://www.bleepstatic.com/content/hl-images/2021/11/10/FBI.jpg)


The Federal Bureau of Investigation (FBI) has revealed that the Cuba ransomware gang has compromised the networks of at least 49 organizations from US critical infrastructure sectors.


"The FBI has identified, as of early November 2021 that Cuba ransomware actors have compromised at least 49 entities in five critical infrastructure sectors, including but not limited to the financial, government, healthcare, manufacturing, and information technology sectors," the federal law enforcement agency said.


The FBI also added that this ransomware group had made over $40 million since it started targeting US companies.


"Cuba ransomware actors have demanded at least US $74 million and received at least US $43.9 million in ransom payments," the FBI added.


This was disclosed in a [flash alert](https://www.ic3.gov/Media/News/2021/211203-2.pdf) issued in coordination with the Cybersecurity and Infrastructure Security Agency (CISA) and focused on sharing indicators of compromised linked with Cuba ransomware.


Cuba ransomware delivered via Hancitor
--------------------------------------


Cuba ransomware is [delivered on victims' networks through the Hancitor malware downloader](https://www.bleepingcomputer.com/news/security/cuba-ransomware-partners-with-hancitor-for-spam-fueled-attacks/), which allows the ransomware gang to gain easier access to previously compromised corporate networks.


Hancitor (Chancitor) is known for delivering information stealers, Remote Access Trojans (RATs), and other types of ransomware. 


[Zscaler spotted it](https://www.zscaler.com/blogs/security-research/chanitor-downloader-actively-installing-vawtrak) distributing the Vawtrak information-stealing trojan. Since then, it switched to password-stealers, including [Pony](https://www.fireeye.com/blog/threat-research/2016/09/hancitor_aka_chanit.html) and Ficker, and, more recently, Cobalt Strike.


For initial compromise of their victims' systems, Hancitor uses phishing emails and stolen credentials, exploits Microsoft Exchange vulnerabilities, or break-in via Remote Desktop Protocol (RDP) tools.


Once in using the access provided by Hancitor, Cuba ransomware operators will use legitimate Windows services (e.g., PowerShell, PsExec, and various other unspecified services) to deploy their ransomware payloads remotely and encrypt files using the ".cuba" extension.


Request for info associated with Cuba ransomware attacks
--------------------------------------------------------


In the flash alert, the FBI also asked systems admins and security professionals who detect Cuba ransomware activity within their enterprise networks to share any related information they have with their local FBI Cyber Squad.


Useful information that can be shared to help identify the attackers behind this ransomware gang includes "boundary logs showing communication to and from foreign IP addresses, Bitcoin wallet information, the decryptor file, and/or a benign sample of an encrypted file."


The FBI added that it does not encourage ransomware payments and advised targets against it since there's no guarantee that paying will prevent data leaks or future attacks. 


This, instead, acts as a motivating for ransomware operations to target more victims and incentivizes other cybercrime groups to join them in conducting similar illegal activities.


However, the federal agency recognizes the damage ransomware attacks can inflict on a business since executives could be forced to consider paying the ransoms to protect shareholders, customers, or employees. The FBI strongly urges reporting such incidents to [local FBI field offices](https://www.fbi.gov/contact-us/field-offices).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Cuba]] [[action.malware.name=Hancitor]] [[action.malware.name=Net]] [[action.malware.name=Pony]] [[action.malware.name=PsExec]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Healthcare]] [[victim.industry.name=Manufacturing]]

#### Location:
[[victim.country.name=Cuba]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Hancitor]] [[Bleeping Computer]]

