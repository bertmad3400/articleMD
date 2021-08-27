# FIN8 Targets US Bank With New ‘Sardonic’ Backdoor
### The latest refinement of the APT’s BadHatch backdoor can leverage new malware on the fly without redeployment, making it potent and nimble. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168982)
+ Date: August 27, 2021  1:32 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/02114512/bank-e1625240724563.jpg)
The financially motivated FIN8 cybergang used a brand-new backdoor – dubbed Sardonic by the Bitdender researchers who first spotted it – in attempted (but unsuccessful) breaches of networks belonging to two unidentified U.S. financial organizations.


It’s a nimble newcomer, researchers wrote: “The Sardonic backdoor is extremely potent and has a wide range of capabilities that help the threat actor leverage new malware on the fly without updating components,” according to Bitdefender’s report.


[FIN8](https://malpedia.caad.fkie.fraunhofer.de/actor/fin8) has typically gone after financial services and payment-card data from [point-of-sale (PoS) systems](https://threatpost.com/fin8-targets-card-data-fuel-pumps/151105/), particularly those of retailers, restaurants and [the hotel industry](https://www.bankinfosecurity.com/fin8-group-returns-targeting-pos-devices-new-tools-a-12819). It’s been active since at least [January 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.htmlhttps://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html), but it periodically pops in and out of dormancy in order to fine-tune tactics, techniques and procedures (TTPs) and thereby evade detection and ramp up its success rate.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


True to form, in March, Bitdefender spotted FIN8 re-emerging after a period of relative quiet with a [new version of the BadHatch backdoor](https://threatpost.com/fin8-resurfaces-backdoor-malware/164684/) to compromise companies in the chemical, insurance, retail and technology industries. Sardonic is an updated version of BadHatch that’s apparently still under development, Bitdefender said.


It’s a refinement of BadHatch in that it can be automatically boosted with new functionality without the malware needing to be redeployed: A way to make it more agile, Bitdefender said.


Bogdan Botezatu, director of threat research for Bitdefender, told [BankInfoSecurity](https://www.bankinfosecurity.com/fin8-using-updated-backdoor-a-17381) that the security firm has seen FIN8 carrying out two attacks over the past few months, what he called “unusually high activity for a threat actor that used to take long breaks between attacks.”


Besides BadHatch – a backdoor that provides file transfer and reverse-shell functionality – FIN8’s well-stocked [arsenal](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/) has included [malware variants](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/) such as ShellTea, a backdoor also known as [PunchBuggy](https://www.fireeye.com/blog/threat-research/2016/05/windows-zero-day-payment-cards.html), and the memory-scraper tool [PoSlurp/PunchTrack](https://otx.alienvault.com/pulse/594821fe9cf28a6bee21691d/). FIN8 has also used the TTPs of exploiting [Windows zero-days](https://www.fireeye.com/blog/threat-research/2016/05/windows-zero-day-payment-cards.html) and [spear-phishing](https://unit42.paloaltonetworks.com/powersniff-malware-used-in-macro-based-attacks/).


Bitdefender isn’t sure what the initial infection vector was on the thwarted bank attack, but based on [FIN8’s prior attacks](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf), it was likely via social engineering and spear-phishing campaigns.


Sardonic Still Being Refined
----------------------------


And now, there’s Sardonic. Earlier this week, Bitdefender published a [deep dive](https://businessinsights.bitdefender.com/deep-dive-into-a-fin8-attack-a-forensic-investigation) describing a forensic investigation that led to the discovery of the new backdoor. Artifacts led researchers to conclude that the threat actors use that name to describe “an entire project including the backdoor itself, the loader and some additional scripts,” according to Bitdefender.


Sardonic is apparently still under development, and Bitdefender suspects that the threat actors will be using additional updates still to come.


The Two Attacks
---------------


During one of the attacks – a recent attack against an unidentified financial institution in the U.S. – FIN8 used a three-stage process to deploy and execute the Sardonic backdoor: A PowerShell script, a .NET loader and downloader shellcode.


After it was loaded, Bitdefender said that the embedded dynamic link library obtained the value of the Y1US environment variable and extracted the string that contained options for behavior customization so it could make changes.


Bitdefender said that the new backdoor tried to evade security monitoring by using TLS encryption in order to conceal Powershell commands. After it gains network access, FIN8 has used the access to scan for victim networks, give attackers remote access, install a backdoor and deliver other malware payloads.


Fending Off Financial Malware
-----------------------------


Bitdefender recommends that companies in the targeted verticals – retail, hospitality and finance – check for potential compromise by applying the indicators of compromise (IoCs) listed in its whitepaper ([PDF](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)), and implementing endpoint detection and response (EDR), extended detection and response (XDR) and other security defenses.


Bitdefender offered these protective measures:


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Bitdefender]] [[FIN8]] [[malware]] [[BadHatch]] [[It’s]] [[ThreatPost]]
