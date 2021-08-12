# SAP Patches Nine Critical & High-Severity Bugs
### Experts urged enterprises to patch fast: SAP vulnerabilities are being weaponized in a matter of hours.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168558)
+ Date: August 11, 2021  11:27 am
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/04/06142606/SAP2-e1617733579541.jpg)
SAP has released 19 new and updated [security patches](https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=582222806), three of them rated as “HotNews” critical and six as high-priority.


“HotNews” is the severity rating that SAP gives to critical vulnerabilities. Two of this month’s sizzlers have a CVSS score of 9.9 and affect SAP Business One and SAP NetWeaver Development Infrastructure.


SAP applications help organizations manage critical business processes – including enterprise resource planning (ERP), product lifecycle management, customer relationship management (CRM) and supply-chain management.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


One of the 9.9ers is CVE-2021-33698, an unrestricted file-upload issue affecting SAP Business One, which is the German company’s business management software for small and medium-sized enterprises. The vulnerability allows an attacker to upload files, including malicious scripts, to the server.


According to Thomas Fritsch, an SAP security researcher at enterprise security firm Onapsis, the only reason it wasn’t given the top CVSS rating of 10 is because it needs a minimal set of authorizations.


In his patch Tuesday [writeup](https://onapsis.com/blog/sap-security-patch-day-august-2021), Fritsch said that fortunately for those customers who can’t immediately apply the related hotfix, there’s a workaround: “Simply deactivate the affected functionality,” he instructed. Of course, that’s just a quick fix. As always, SAP is stressing that the workaround be considered a temporary fix and not a permanent solution.


SAP described the second critical security bug, CVE-2021-33690, as a server-side request forgery (SSRF) affecting NetWeaver Development Infrastructure (SAP NWDI) in a servlet of the Component Build Service.


Onapsis said that the servlet was exposed to the outside world, “allowing attackers to perform proxy attacks by sending crafted queries.” According to Fritsch, SAP warned that the severity of the flaw depends on whether users are running NWDI on the intranet or internet. It’s bad news for those who are running it on the internet, SAP has emphasized, given that it “could completely compromise sensitive data residing on the server, and impact its availability,” the company reportedly said in its note.


As far as the third HotNews vulnerability goes – CVE-2021-33701 – the flaw is a SQL injection in the SAP NZDT (Near Zero Downtime Technology) service used by S/4HANA and the DMIS mobile plug-in. Its CVSS severity rating is 9.1.


“The tool is used by SAP’s corresponding NZDT service for time-optimized system upgrades and system conversions,” Fritsch explained. “When using the NZDT service, the maintenance is performed on a clone of the production system. All changes are recorded and transferred to the clone after the maintenance tasks are completed. During the final downtime, only a few activities are executed, including a switch of the production to the new system (clone).”


Again, there’s a workaround available for customers who’ve activated the Unified Connectivity (UCON) runtime check, he wrote: Don’t assign the used remote-enabled function module to any communication assembly in UCON.


Four High-Severity Bugs
-----------------------


Onapsis gave a shout-out to Yvan Genuer, from the Onapsis Research Labs, who collaborated with SAP to fix four vulnerabilities in SAP Enterprise Portal.


One was CVE-2021-33702, a cross-site scripting (XSS) vulnerability in SAP NetWeaver Enterprise Portal that was caused by one of the portal’s servlets and given a rating of CVSS 8.3. It involves insufficient sanitization that allows for injection of JavaScript into the corresponding web page: an issue that could lead to a victim navigating to an infected servlet and triggering a vulnerable script to execute in their browser. The impact is high, but successful exploitation would be “highly complex” and would require user interaction, Fitsch explained, which are conditions that led to its lower CVSS score.


The quartet of high-severity patches includes a second XSS vulnerability, CVE-2021-33703, similarly found in another servlet of SAP NetWeaver Enterprise Portal and also rated CVSS 8.3.


The third high-priority fix is CVE-2021-33705. This one addresses a server-side request forgery (SSRF) vulnerability in one of the design-time components of SAP NetWeaver Enterprise Portal that would allow an unauthenticated attacker to craft a malicious URL that could send any type of request – POST or GET, for example – to any internal or external server were a user to click on it.


The fourth hole that Onapsis worked with SAP to seal up – CVE-2021-33707 – was tagged with a CVSS score of 6.1. It concerns a URL-redirection bug in SAP Knowledge Management that would allow remote attackers to “redirect users to arbitrary websites and conduct phishing attacks via a URL stored in a component,” Fitsch detailed: A scenario that would give attackers the ability “to compromise the user’s confidentiality and integrity.”


Other critical vulnerabilities covered on Tuesday were an authentication issue affecting SAP systems accessed through a Web Dispatcher, a task hijacking issue in the Fiori Client mobile app for Android and a missing authentication flaw in SAP Business One.


Last Month = Calm, This Month = Storm
-------------------------------------


Given the nine critical patches, Fritsch dubbed [last month’s light SAP Patch Tuesday](https://onapsis.com/blog/sap-security-patch-day-july-2021-serious-vulnerabilities-sap-netweaver-java-fixed) the “calm before the storm.” In fact, he said, Tuesday’s raft of patches have earned August the dubious honor of being “the most noteworthy SAP Patch Day this year” for customers, he wrote.


“The small group of SAP applications that are affected by a CVSS 9.9 vulnerability in 2021 is now extended with SAP Business One and SAP NetWeaver Development Infrastructure,” Fritsch noted.


Word of caution to SAP Enterprise Portal customers in particular, he said, given the four patches released for the app, three of them rated high priority.


Critical Flaws Weaponized in Less Than 72 hours
-----------------------------------------------


Enterprises will hopefully jump on the patches with utmost speed, given how fast SAP bugs are weaponized. An April threat intelligence [report](https://www.onapsis.com/active-cyberattacks-business-critical-sap-applications) from Onapsis and SAP found that critical SAP vulnerabilities are turned into exploits “in less than 72 hours of a patch release.” It’s even worse for new, unprotected SAP apps provisioned in cloud environments: They’re being discovered and compromised in less than three hours, according to the alert.


“Threat actors are active, capable and widespread,” the report advised, citing evidence of more than 300 automated exploitations leveraging seven SAP-specific attack vectors and 100+ hands-on-keyboard sessions from a wide range of threat actors. The companies found “clear evidence of sophisticated domain knowledge, including the implementation of SAP patches post-compromise.”


Adversaries were [carrying out a range of attacks](https://threatpost.com/sap-bugs-cyberattack-compromise/165265/), according to Onapsis and SAP, including theft of sensitive data, financial fraud, disruption of mission-critical business processes and other operational disruptions, and delivery of ransomware and other malware.


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)**Worried about where the next attack is coming from? We’ve got your back. [REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar) for our upcoming live webinar, How to Think Like a Threat Actor, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on [Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar).**




#### Tags:
[[CVSS]] [[NetWeaver]] [[Onapsis]] [[Fritsch]] [[servlet]] [[NZDT]] [[ThreatPost]]
