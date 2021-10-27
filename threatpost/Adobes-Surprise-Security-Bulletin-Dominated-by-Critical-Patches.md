# Adobe’s Surprise Security Bulletin Dominated by Critical Patches
### Out of 92 security vulnerabilities, 66 are rated critical in severity, mostly allowing code execution. The most severe can lead to information disclosure.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175825)
+ Date: October 27, 2021  3:13 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/06/29072304/Adobe-Logo.jpg)
Adobe has dropped a mammoth out-of-band security update this week, addressing 92 vulnerabilities across 14 products.


The majority of the disclosed bugs are [critical-severity problems](https://threatpost.com/adobe-critical-flaws-windows/164611/), and most allow arbitrary code execution (ACE). Privilege escalation, denial-of-service and memory leaks/information disclosure are all well-represented, as well.


Adobe After Effects, Animate, Audition, Bridge, Character Animator, Illustrator, InDesign, Lightroom Classic, Media Encoder, Photoshop, Prelude, Premiere Pro, Premiere Elements and the XMP Toolkit SDK all received patches.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


There’s plenty of commonality across the advisories. For instance, the lion’s share of the bugs allow access to a memory location after the end of a buffer, leading to ACE (a [type of memory issue](https://cwe.mitre.org/data/definitions/788.html) that can be exploited, like a standard buffer overflow in the worst-case scenario).


Also, almost all of the critical problems rate 7.8 on the CVSS vulnerability severity scale, except for one type. The advisory lists “NULL pointer dereference bugs causing memory leak” flaws as the most severe issues in the bunch, all rating 8.3 on the CVSS scale. These pop up in Bridge, Media Encoder, Prelude and Premiere Elements (and are *italicized*, below).


**Adobe October Out-of-Band CVEs**
----------------------------------


Here’s the full breakdown of the critical bugs:


**After Effects:**


**Animate:**


**Audition:**


**Bridge:**


**Character Animator:**


**Illustrator:**


**InDesign:**


**Lightroom Classic:**


**Media Encoder:** 


**Photoshop:**


**Prelude:**


**Premiere Elements:**


**Premiere Pro:**


**XMP Toolkit SDK:**


This bulletin was prompted by findings from two teams that deserve busy-beaver awards: Adobe credited researchers from TopSec Alpha Team and Trend Micro’s Zero-Day Initiative for all of the bugs, except for CVE-2021-40746 in Illustrator, credited to “Tmgr.” This could also explain some of the commonalities in the bulletins.


The fixes come two weeks after Adobe released its normal monthly Patch Tuesday patches. A company spokesperson characterized the release as “planned” rather than an emergency response – and indeed, Adobe said in [its advisories](https://helpx.adobe.com/security/security-bulletin.html) that there’s no evidence that any of the bugs are being exploited in the wild.


“While we strive to release regularly scheduled updates on Patch Tuesday, occasionally these regularly scheduled security updates are released on non-Patch Tuesday dates,” a company spokesperson told [the Register](https://www.theregister.com/2021/10/26/adobe_october_extra_patches/).


Of note: The advisory for Bridge is listed as priority 2 for patching, which in Adobe [parlance](https://helpx.adobe.com/security/severity-ratings.html) means that the product has historically been at elevated risk for exploitation, so it comes with a recommendation that administrators patch within 30 days. The other advisories are priority 3, which is the lowest risk level, meaning that administrators can patch “at their discretion.”


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[]] [[ThreatPost]]
