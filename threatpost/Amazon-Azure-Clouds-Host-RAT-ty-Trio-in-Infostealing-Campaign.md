# Amazon, Azure Clouds Host RAT-ty Trio in Infostealing Campaign
### A cloudy campaign delivers commodity remote-access trojans to steal information and execute code.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177606
+ Date: 2022-01-12T21:04:58+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/12150239/RATs2-e1642017822522.jpg)

Cyberattackers are abusing Amazon Web Services (AWS) and Azure Cloud services to deliver a trio of remote access trojans (RATs), researchers warned – all aimed at hoovering up sensitive information from target users.


According to an [analysis](https://blog.talosintelligence.com/2022/01/nanocore-netwire-and-asyncrat-spreading.html) from Cisco Talos, threat actors have been pushing out variants of the malware known as AsyncRAT, Netwire and Nanocore since October, mainly to targets in Italy, Singapore and the United States. A few of the targets have been in South Korea and Spain as well, according to the firm.


As in many campaigns, the attacks start with a phishing email containing a malicious .ZIP attachment, researchers said. But the attackers have a cloud-based trick up their sleeve.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“These .ZIP archive files contain an ISO image with a malicious loader in the form of JavaScript, a Windows batch file or Visual Basic script,” Talos researchers explained on Wednesday. “When the initial script is executed on the victim’s machine, it connects to a download server to download the next stage, which can be hosted on an Azure Cloud-based Windows server or an AWS EC2 instance.”


**Clouding the (Malicious) Issue**
----------------------------------


Using cloud services to host the payloads is a savvy effort to avoid detection while cutting the costs of the campaign, researchers noted, since they don’t have to set up their own infrastructure.


“These types of cloud services like Azure and AWS allow attackers to…connect to the internet with minimal time or monetary commitments,” according to the analysis. “It also makes it more difficult for defenders to track down the attackers’ operations.”


The actor behind this campaign maintains a distributed infrastructure consisting of download servers, command-and-control servers (C2s) and malicious subdomains, researchers noted. The downloading servers are the ones hosted on Microsoft Azure and AWS cloud services.


“Threat actors use well-known cloud services in their campaigns because the public passively trusts big companies to be secure,” Davis McCarthy, principal security researcher at Valtix, said via email. “Network defenders may think communications to an IP address owned by Amazon or Microsoft is benign because those communications occur so frequently across a myriad of services.”


Beyond that, the main JavaScript downloader used in the campaign leverages a four-layer, complex obfuscation technique in its script: “Each stage of the deobfuscation process results with the decryption methods for the subsequent stages to finally arrive at the actual malicious downloader method,” researchers explained. “The deobfuscation process is performed at each stage with every next stage generated as the result of the previous stage deobfuscation function.”


The campaign uses a range of other dropper trojans as well, including a batch-file downloader and a VBScript downloader.


“The batch script contains an obfuscated command that runs PowerShell to download and run a payload from a download server…on Azure Cloud,” researchers said. “Obfuscated VB downloaders execute a PowerShell command which runs and connects to the download server…running on AWS EC2.”


And finally, to further cover their tracks, the attackers are using the DuckDNS dynamic DNS service to change the domain names of the C2  hosts. Talos found they have registered several malicious subdomains using the service.


“The fact that the hackers are constantly modifying their C2 centers with DuckDNS, a freeware DNS service – just shows how ‘by any means necessary’ the hackers are willing to operate,” Garret Grajek, CEO at YouAttest said via email. “The attacks like this one show a team effort in scanning, exploiting, obfuscation and then finally exfiltration.”


**RATs Swarm Their Victims**
----------------------------


The RATs used in the campaign come in three flavors, all sporting multiple features to steal the victims’ information, according to the analysis:


* **AsyncRAT** is used to remotely monitor and control computers through a secure encrypted connection to the C2 server. It [also has features](https://threatpost.com/loader-aviation-spy-rats/166133/) like a keylogger, screen recorder and a system-configuration manager, to allow the attacker to steal confidential data from the victim’s machine.
* **NetwireRAT** is [a known threat](https://threatpost.com/taxpayers-targeted-with-improved-netwire-rat-variant/154830/) used by cyberattackers to steal victim’s passwords, login credentials and credit-card data. It also has the capability to remotely execute the commands and collects file-system information.
* **Nanocore** is a 32-bit .NET portable executable – a [commodity threat](https://threatpost.com/nanocore-rat-email-defenses-zipx/164701/) first seen in the wild in 2013. The version used in this campaign, which has a build date of Oct. 26, contains two plugins, called Client and SurveillanceEx. Client handles the communications with the C2 server; and SurveillanceEX captures video and audio, and monitors remote-desktop activity.


**Detection Tips: Inspect Outgoing Cloud Connections**
------------------------------------------------------


Threat actors are actively using cloud services in their malicious campaigns, Talos researchers warned, noting that to detect malicious activity, organizations should be inspecting outgoing connections to cloud-computing services.


“Organizations should deploy comprehensive multi-layered security controls to detect similar threats and safeguard their assets,” they concluded. “Defenders should monitor traffic to their organization and implement robust rules around the script execution policies on their endpoints. It is even more important for organizations to improve email security to detect and mitigate malicious email messages, and break the infection chain as early as possible.”


Valtix’ McCarthy added, “The use of dynamic DNS gives the threat actor a flexible infrastructure that doesn’t require a static IP address. This prevents campaign disruption and provides a layer of obfuscation when threat hunting for a specific dynamic DNS provider’s domain. Creating an inventory of known cloud services and their network communication behaviors may aid in detecting this type of campaign.”


And, YouAttest’s Grajek warned organizations to take a holistic approach to detection: “Privilege escalation is often part of these attacks to ensure the hacker can laterally move across the enterprise. Thus, it’s imperative to be monitoring both new malware installations and new traffic – but also modifications in access and privilege rights.”


**Cloud Providers Have Responsibility**
---------------------------------------


Miclain Keffeler, application security consultant at nVisium, noted that the rise in the adoption of cloud technologies has continued to shift security.


“What was once a wall with clear barriers and holes has now shifted into a labyrinth of complexity — where many of the entrances to the maze are being infiltrated by RATs and other obscure vermin (attacks),” he said via email.


As such, cloud providers are on the hook for defense too, he added.


“Enterprise organizations have a large role to play in this conundrum, but so do public cloud platforms,” he noted. It is equally their responsibility to ensure that when malicious usage of their services and cloud environment are found, they are immediately halted,” he said. “These kinds of attacks aren’t going anywhere, so it’s important that cloud providers like AWS and Microsoft Azure step in to develop more processes around the notification of malicious use cases — especially given the complex nature of the current threatscape.”


***Password******Reset:******[On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):*** *Fortify 2022 with a password-security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the new password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken.****[Register & stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)****– sponsored by Specops Software.*


 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Maze]] [[action.malware.name=NanoCore]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=NETWIRE]] [[action.malware.name=Power Loader]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]] [[action.malware.name=VERMIN]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Singapore]] [[victim.continent.name=Asia]] [[victim.city.name=Singapore]] [[victim.country.name=Singapore]] [[victim.continent.name=Asia]] [[victim.country.name=South Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.country.name=Spain]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Cloud]] [[Aws]] [[“the]] [[Talos]] [[Downloader]] [[Dns]] [[C2]] [[Cloud]] [[“these]] [[Microsoft]] [[ThreatPost]]

