# Microsoft Warns: Another Unpatched PrintNightmare Zero-Day
### The out-of-band warning pairs with a working proof-of-concept exploit for the issue, circulating since mid-July.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168613)
+ Date: August 12, 2021  9:19 am
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27211434/nightmare-e1627434884417.jpeg)
One day after dropping its scheduled August Patch Tuesday update, Microsoft issued a warning about yet another unpatched privilege escalation/remote code-execution (RCE) vulnerability in the Windows Print Spooler.


The zero-day bug, tracked as CVE-2021-36958, carries a CVSS vulnerability-severity scale rating of 7.3, meaning that it’s rated as “important.” Microsoft said that it allows for a local attack vector requiring user interaction, but that the attack complexity is low, with few privileges required.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“A remote code-execution vulnerability exists when the Windows Print Spooler service improperly performs privileged file operations,” the computing giant explained in its [Wednesday advisory](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36958). “An attacker who successfully exploited this vulnerability could run arbitrary code with SYSTEM privileges. An attacker could then install programs; view, change or delete data; or create new accounts with full user rights.”


The CERT Coordination Center actually flagged the issue in mid-July, when it warned that a [working exploit](https://twitter.com/gentilkiwi/status/1416429860566847490) was available. That proof-of-concept (PoC), issued by Benjamin Delpy, comes complete with a video.



> 
> Hey guys, I reported the vulnerability in Dec'20 but haven't disclosed details at MSRC's request. It looks like they acknowledged it today due to the recent events with print spooler.
> 
> 
> — Victor Mata (@offenseindepth) [August 11, 2021](https://twitter.com/offenseindepth/status/1425574625384206339?ref_src=twsrc%5Etfw)
> 
> 



On Thursday, CERT/CC issued more details on the issue, explaining that it arises from an oversight in signature requirements around the “Point and Print” capability, which allows users without administrative privileges to install printer drivers that execute with SYSTEM privileges via the Print Spooler service.


While Microsoft requires that printers installable via Point are either signed by a WHQL release signature or by a trusted certificate, Windows printer drivers can specify queue-specific files that are associated with the use of the device, which leaves a loophole for malicious actors.


“For example, a shared printer can specify a CopyFiles directive for arbitrary files,” according to the CERT/CC [advisory](https://www.kb.cert.org/vuls/id/131152). “These files, which may be copied over alongside the digital-signature-enforced printer driver files, are not covered by any signature requirement. Furthermore, these files can be used to overwrite any of the signature-verified files that were placed on a system during printer driver install. This can allow for local privilege escalation to SYSTEM on a vulnerable system.”


Microsoft credited Victor Mata of FusionX at Accenture Security with originally reporting the issue, which Mata said occurred back in December 2020:



> 
> Hey guys, I reported the vulnerability in Dec’20 but haven’t disclosed details at MSRC’s request. It looks like they acknowledged it today due to the recent events with print spooler.
> 
> 
> — Victor Mata (@offenseindepth) [August 11, 2021](https://twitter.com/offenseindepth/status/1425574625384206339?ref_src=twsrc%5Etfw)
> 
> 


So far, Microsoft hasn’t seen any attacks in the wild using the bug, but it noted that exploitation is “more likely.” With a working exploit in circulation, that seems a fair assessment.


**Print Spooler-Palooza and the PrintNightmare**
------------------------------------------------


Delpy characterized this latest zero-day as being part of the string of Print Spooler bugs collectively known as PrintNightmare.


The bad dream started in early July, when a PoC exploit for a bug tracked as CVE-2021-1675 was [dropped on GitHub](https://threatpost.com/poc-exploit-windows-print-spooler-bug/167430/). The flaw was originally addressed in [June’s Patch Tuesday updates](https://threatpost.com/microsoft-patch-tuesday-in-the-wild-exploits/166724/) from Microsoft as a minor elevation-of-privilege vulnerability, but the PoC showed that it’s actually a critical Windows security vulnerability that can be used for RCE. That prompted Microsoft to issue a different CVE number – in this case, CVE-2021-34527 – to designate the RCE variant, and it prompted [an emergency partial patch](https://threatpost.com/microsoft-emergency-patch-printnightmare/167578/), too.


“This vulnerability is similar but distinct from the vulnerability that is assigned CVE-2021-1675, which addresses a different vulnerability in RpcAddPrinterDriverEx(),” the company wrote in the advisory at the time. “The attack vector is different as well. CVE-2021-1675 was addressed by the June 2021 security update.”


Both bugs – which are really just variants of a single issue – are collectively known as PrintNightmare. The PrintNightmare umbrella expanded a bit later in July, when yet another, [similar bug was disclosed](https://threatpost.com/microsoft-unpatched-bug-windows-print-spooler/167855/), tracked as CVE-2021-34481. It remained unpatched until it was finally addressed with [an update](https://support.microsoft.com/en-us/topic/kb5005652-manage-new-point-and-print-default-driver-installation-behavior-cve-2021-34481-873642bf-2634-49c5-a23b-6d8e9a302872) issued alongside the [August Patch Tuesday updates](https://threatpost.com/exploited-windows-zero-day-patch/168539/) (which itself detailed three additional Print Spooler vulnerabilities, one critical).


Print Spooler issues offer an attractive avenue for a range of cybercriminals, including ransomware gangs. Researchers from CrowdStrike warned in a [Wednesday report](https://www.crowdstrike.com/blog/magniber-ransomware-caught-using-printnightmare-vulnerability/) that the operators of the Magniber ransomware quickly weaponized CVE-2021-34527 to attack users in South Korea, with attacks dating back to at least July 13.


“In technology, almost nothing ages gracefully,” Chris Clements, vice president of solutions architecture and Cerberus security officer at Cerberus Sentinel, told Threatpost. “The Print Spooler in Windows is proving that rule. It’s likely that the code has changed little in the past decades and likely still bears a striking resemblance to source code that was made public in previous Windows leaks. I’ve heard it said that ransomware gangs might also be referred to as ‘technical debt collectors,’ which would be funnier if the people suffering most from these vulnerabilities weren’t Microsoft’s customers.”


**How to Protect Systems from Print Spooler Attacks**
-----------------------------------------------------


As mentioned, there’s no patch yet for the bug, but users can protect themselves by simply stopping and disabling the Print Spooler service:


CERT/CC also said that since public exploits for Print Spooler attacks use the SMB file-sharing service for remote connectivity to a malicious shared printer, blocking outbound connections to SMB resources would thwart some attacks by blocking malicious SMB printers that are hosted outside of the network.


“However, Microsoft indicates that printers can be shared via the Web Point-and-Print Protocol, which may allow installation of arbitrary printer drivers without relying on SMB traffic,” according to CERT/CC. “Also, an attacker local to your network would be able to share a printer via SMB, which would be unaffected by any outbound SMB traffic rules.”


In its update advisory for CVE-2021-34481, Microsoft also detailed how to amend the default Point and Print functionality, which prevents non-administrator users from installing or updating printer drivers remotely and which could help mitigate the latest zero-day.


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[Microsoft]] [[Windows]] [[SMB]] [[Mata]] [[bug,]] [[CERT/CC]] [[ransomware]] [[ThreatPost]]
