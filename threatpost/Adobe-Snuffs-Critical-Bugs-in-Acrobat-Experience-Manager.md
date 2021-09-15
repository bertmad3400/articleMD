# Adobe Snuffs Critical Bugs in Acrobat, Experience Manager
### Adobe releases security updates for 59 bugs affecting its core products, including Adobe Acrobat Reader, XMP Toolkit SDK and Photoshop.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169467)
+ Date: September 14, 2021  5:02 pm
+ Author: Tom Spring


## Article:
Adobe is urging its throngs of Acrobat Reader users to update their software to fix critical vulnerabilities that could allow adversaries to execute arbitrary code on unpatched versions.


The warnings are part of the firm’s [September monthly security update](https://helpx.adobe.com/security.html), which this month addresses 59 bugs found in 15 of its products, including in Photoshop, Premiere Elements, ColdFusion and InCopy.


In all, 36 of the vulnerabilities are rated “critical,” which is an Adobe-specific label indicating that the flaws, if exploited, “would allow malicious native-code to execute, potentially without a user being aware.”


As for the Adobe Acrobat family of software, 26 bugs were patched, 13 of which were critical and given an Adobe priority rating of “2,” meaning that the affected product is at “elevated risk” of being attacked.  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Other high-rated bugs include a bevy of code execution vulnerabilities triggered via a type confusion, heap-based buffer overflow or a use-after-free style of attack.


“[One] single bug fixed by [a] Photoshop patch could … lead to code execution when opening a specially crafted file,” commented [Zero-Day Initiative in a Tuesday post](https://www.zerodayinitiative.com/blog/2021/9/14/the-september-2021-security-update-review-kpgpb).


“If you’re still using ColdFusion, you’ll definitely want to patch the two critical rated security feature bypass bugs being fixed today,” ZDI continued.


Of those Adobe bugs rated the highest in severity – when it comes to MITRE’s Common Vulnerability Scoring System (CVSS) – standouts include a Framemaker bug (CVE-2021-39830) rated 8.8. Another 8.8 high-severity bug (CVE-2021-39820), like the former, allows a threat actor to execute code arbitrarily in versions of Adobe InDesign.


Next, in terms of high-severity CVSS scores, is a flaw in Adobe Digital Editions, rated 8.6 in severity. The vulnerability ([CVE-2021-39826](https://helpx.adobe.com/security/products/Digital-Editions/apsb21-80.html)) is described as an OS command-injection bug.


“The software constructs all or part of an OS command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended OS command when it is sent to a downstream component,” [MITRE explained](https://cwe.mitre.org/data/definitions/78.html) about the Digital Editions flaw.


None of the bugs fixed by Adobe this month are believed to be publicly known or under active attack, according to Adobe.


**It’s time to evolve threat hunting into a pursuit of adversaries.**[**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**Threatpost and Cybersixgill for**[**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**and get a guided tour of the dark web and learn how to track threat actors before their next attack.**[**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with independent researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[]] [[ThreatPost]]
