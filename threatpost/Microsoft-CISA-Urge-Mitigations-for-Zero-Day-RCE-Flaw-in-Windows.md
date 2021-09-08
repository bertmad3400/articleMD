# Microsoft, CISA Urge Mitigations for Zero-Day RCE Flaw in Windows
### Attackers are actively attempting to exploit a vulnerability in MSHTML that allows them to craft a malicious ActiveX control to be used by Microsoft Office files.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169273)
+ Date: September 8, 2021  8:24 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2020/09/15073634/Microsoft-Office.jpg)
Both Microsoft and federal cybersecurity officials are urging organizations to use mitigations to combat a zero-day remote control execution (RCE) vulnerability in Windows that allows attackers to craft malicious Microsoft Office documents.


Microsoft has not revealed much about the MSHTML bug, tracked as [CVE-2021-40444](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-40444), beyond that it is  “aware of targeted attacks that attempt to exploit this vulnerability by using specially-crafted Microsoft Office documents,” according to an advisory released Tuesday.


However, it’s serious enough that the Cybersecurity and Infrastructure Security Agency (CISA) released [an advisory](https://us-cert.cisa.gov/ncas/current-activity/2021/09/07/microsoft-releases-mitigations-and-workarounds-cve-2021-40444) of its own alerting users and administrators to the vulnerability and recommending that they use the mitigations and workarounds Microsoft recommends.


The vulnerability allows an attacker to craft a malicious ActiveX control that can be used by a Microsoft Office document that hosts the browser rendering engine, according to Microsoft.  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)The attacker would then have to convince the user to open the malicious document for an attack to be successful, the company said. Moreover, users whose accounts are configured to have fewer user rights on the system could be less impacted than users who operate with administrative user rights, according to the advisory.


**Affecting More than Office**
------------------------------


Though Microsoft is still investigating the vulnerability, it could prove to go beyond affecting just Microsoft Office documents due to the ubiquitous use of MSHTML on Windows, warned Jake Williams, co-founder and CTO at incident response firm [BreachQuest](https://breachquest.com/).


“If you’ve ever opened an application that seemingly ‘magically’ knows your proxy settings, that’s likely because it uses MSHTML under the hood,” he said in an e-mail to Threatpost. “Vulnerabilities like these tend to have extremely long lifetimes for exploitation in the wild.”


Even if the vulnerability’s reach does not go beyond Office documents, its presence and the fact that attackers are already trying to exploit are worrisome enough for organizations to take immediate action, noted another security professional.


Malicious Office documents are a popular tactic with cybercriminals and state-sponsored threat actors, and the vulnerability give them “more direct exploitation of a system and the usual tricking users to disable security controls,” observed John Bambenek, principal threat hunter at digital IT and security operations firm [Netenrich](https://netenrich.com/).


“As this is already being exploited, immediate patching should be done,” he advised. “However, this is a stark reminder that in 2021, we still can’t send documents from point A to point B securely.”


**Mitigations and Workarounds**
-------------------------------


Microsoft has offered some advice for organizations affected by the vulnerability—first discovered by Rick Cole of the Microsoft Security Response Center, Haifei Li of EXPMON, and Dhanesh Kizhakkinan, Bryce Abdo and Genwei Jiang of Mandiant–until it can offer its own security update. That may come in the form of a Patch Tuesday fix or an out-of-band patch, depending on what researchers discover, the company said.


Until then, customers should keep anti-malware products up to date, though those who use automatic updates don’t need to take action now, Microsoft said. For enterprise customers who manage updates, they should select the detection build 1.349.22.0 or newer and deploy it across their environments, the company added.


Workarounds for the flaw include disabling the installation of all ActiveX controls in Internet Explorer, which mitigates a potential attack, according to Microsoft.


“This can be accomplished for all sites by updating the registry,” the company said in its advisory. “Previously-installed ActiveX controls will continue to run, but do not expose this vulnerability.”


However, Microsoft warned organizations to take care when using the Registry Editor, because doing so incorrectly can “cause serious problems that may require you to reinstall your operating system.” “Use Registry Editor at your own risk,” the company advised.


**It’s time to evolve threat hunting into a pursuit of adversaries.**[**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**Threatpost and Cybersixgill for**[**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**and get a guided tour of the dark web and learn how to track threat actors before their next attack.**[**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with independent researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[Microsoft]] [[MSHTML]] [[ActiveX]] [[said.]] [[ThreatPost]]
