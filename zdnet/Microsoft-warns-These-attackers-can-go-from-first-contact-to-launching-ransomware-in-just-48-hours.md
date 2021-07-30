# Microsoft warns: These attackers can go from first contact to launching ransomware in just 48 hours
### Human operators make BazaCall malware harder than usual to detect malicious email. The group sometimes installs nasty Ryuk ransomware.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/microsoft-warns-these-attackers-can-go-from-first-contact-to-launching-ransomware-in-just-48-hours/)
+ Date: July 30, 2021 -- 10:21 GMT (11:21 BST)
+ Author: Liam Tung


## Article:
Unknown

Microsoft is warning that the BazarCall (or Bazacall) call center malware operation is actually more dangerous than first thought, with initial attacks potentially leading to ransomware attacks within 48 hours.   

The group had been targeting Office 365/Microsoft 365 customers with phishing email regarding 'expiring' bogus trial subscriptions that dupe the target into calling a call center to chat with an operator, who then try to trick the victim into installing the Bazacall backdoor. 

The Microsoft 365 Defender Threat Intelligence Team [spotlighted the group in June](https://www.zdnet.com/article/microsoft-warns-now-attackers-are-using-a-call-centre-to-trick-you-into-downloading-ransomware/), as ZDNet reported at the time, and in a new post it outlines how it's a more dangerous threat than previously reported, allowing the attackers to distribute ransomware or steal data within 48 hours of infection.     

"Apart from having backdoor capabilities, the BazaLoader payload from these campaigns also gives a remote attacker hands-on-keyboard control on an affected user's device, which allows for a fast network compromise," [the Microsoft team says](https://www.microsoft.com/security/blog/2021/07/29/bazacall-phony-call-centers-lead-to-exfiltration-and-ransomware/). 

"In our observation, attacks emanating from the BazaCall threat could move quickly within a network, conduct extensive data exfiltration and credential theft, and distribute ransomware within 48 hours of the initial compromise."

The BazaCall group has apparently teamed up with group behind the Ryuk ransomware, which [has made about $150 million in Bitcoin from its attacks](https://www.zdnet.com/article/ryuk-gang-estimated-to-have-made-more-than-150-million-from-ransomware-attacks/).   

A few notable differences with the BazaCall group's tactics include that they don't use phishing links or send malicious attachments, helping avoid classic detection systems. The technique is closer to call center fraudsters and victims are also connected to a human operator. 






"Hands-on-keyboard control further makes this threat more dangerous and more evasive than traditional, automated malware attacks," Microsoft warns.

The call center and email outreach parts of the operation seem reasonably well-organized. While subject lines in emails are repeated, each email is tagged with unique alpha-numeric string, creating a user ID or transaction code, in order to identify the victim across multiple calls. 

The initial call center operator discusses the expiring subscription and then recommends the victim visit a faked website where they can supposedly cancel the subscription to avoid future monthly fees.

Microsoft has provided additional details regarding the group's use of malicious macros in Excel files to download the Cobalt Strike penetration testing kit and gain 'hands-on-keyboard' control of a victim's machine and the ability to search a network for admin and domain administrator account info to exfiltrate data or deploy Ryuk or Conti, a related ransomware. 

The agent instructs the victim to navigate to the account page and cancel the subscription by download a file, which turns out to be a macro-enabled Excel document. The call center agent instructs the victim to enable content on Microsoft's default warning in Excel that macros have been disabled. 

The group is, according to Microsoft's description, using relatively sophisticated 'living-off the-land' (or misusing legit software tools) for nefarious network activities.     

If the attacker finds a high-value target, they use 7-Zip to archive intellectual property — such as information about security operations, finance and budgeting — for exfiltration.

In cases where ransomware was deployed after compromise, the attacker used high privilege compromised accounts with Cobalt Strike's PsExec functionality to distribute Ryuk or Conti ransomware on network devices, according to Microsoft. 





#### Tags:
[[Microsoft]] [[ransomware]] [[BazaCall]] [[Ryuk]] [[ZDNet]]
