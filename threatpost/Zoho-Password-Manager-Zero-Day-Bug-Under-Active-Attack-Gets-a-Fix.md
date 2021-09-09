# Zoho Password Manager Zero-Day Bug Under Active Attack Gets a Fix
### An authentication bypass vulnerability leading to remote code execution offers up the keys to the corporate kingdom.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169303)
+ Date: September 9, 2021  8:58 am
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/09085735/keys-e1631192268247.jpg)
A critical security vulnerability in the Zoho ManageEngine ADSelfService Plus platform could allow remote attackers to bypass authentication and have free rein across users’ Active Directory (AD) and cloud accounts.


The issue (CVE-2021-40539) has been actively exploited in the wild as a zero-day, according to the Cybersecurity and Infrastructure Security Agency (CISA).


Zoho issued a patch on Tuesday, and CISA [warned that](https://us-cert.cisa.gov/ncas/current-activity/2021/09/07/zoho-releases-security-update-adselfservice-plus) admins should not only apply it immediately, but also ensure in general that ADSelfService Plus is not directly accessible from the internet. The issue affects builds 6113 and below (the fixed version is 6114).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The Zoho ManageEngine ADSelfService Plus is a self-service password management and single sign-on (SSO) solution for AD and cloud apps, meaning that any cyberattacker able to take control of the platform would have multiple pivot points into both mission-critical apps (and their sensitive data) and other parts of the corporate network via AD. It is, in other words, a powerful, highly privileged application which can act as a convenient point-of-entry to areas deep inside an enterprise’s footprint for both users and attackers alike.


“Ultimately, this underscores the threat posed to internet-facing applications,” Matt Dahl, principal intelligence analyst for Crowdstrike, [noted](https://twitter.com/voodoodahl1/status/1435673342925737991). “These don’t always get the same attention as exploit docs with decoy content, but the variety of these web-facing services gives actors lots of options.”


This isn’t Zoho’s first zero-day rodeo. In March 2020, [researchers disclosed](https://threatpost.com/critical-zoho-zero-day-flaw-disclosed/153484/) a zero-day vulnerability in Zoho’s ManageEngine Desktop Central, an endpoint management tool to help users manage their servers, laptops, smartphones and more from a central location. The critical bug (([CVE-2020-10189](https://nvd.nist.gov/vuln/detail/CVE-2020-10189), with a CVSS score of 9.8) allowed an unauthenticated, remote attacker to gain complete control over affected systems – “basically the worst it gets,” researchers said at the time.


**Authentication Bypass and RCE**
---------------------------------


The issue at hand is an authentication bypass vulnerability affecting the REST API URLs in ADSelfService Plus, which could lead to remote code execution (RCE), according to Zoho’s [knowledge-base advisory](https://www.manageengine.com/products/self-service-password/kb/how-to-fix-authentication-bypass-vulnerability-in-REST-API.html).


“This vulnerability allows an attacker to gain unauthorized access to the product through REST API endpoints by sending a specially crafted request,” according to the firm. “This would allow the attacker to carry out subsequent attacks resulting in RCE.”


Echoing CISA’s assessment, Zoho also noted that “We are noticing indications of this vulnerability being exploited.” The firm characterized the issue as “critical” although a CVSS vulnerability-severity rating has not yet been calculated for the bug.


Further technical details are for now scant (and no public exploit code appears to be making the rounds — yet), but Dahl noted that the zero-day attacks have been going on for quite some time:



> 
> Observed exploitation of this vuln \_before\_ CVE-2021-26084 (Atlassian Confluence) which got a lot of attention last week. Some very general observations:
> 
> 
> 1/ <https://t.co/rIfxxeBlmO>
> 
> 
> — Matt Dahl (@voodoodahl1) [September 8, 2021](https://twitter.com/voodoodahl1/status/1435673338693754886?ref_src=twsrc%5Etfw)
> 
> 



However, he said that the attacks have thus far been highly targeted and limited, and possibly the work of a single (unknown, for now) actor.


“Actor(s) appeared to have a clear objective with ability to get in and get out quickly,” he tweeted.


He also noted similarities to the attacks taking place on Atlassian Confluence instances (CVE-2021-26084), which also started out as limited and targeted. However, in that case, researchers were able to “rapidly produce” a PoC exploit, he pointed out, and eventually there was proliferation to multiple targeted-intrusion actors, usually resulting in cryptomining activity ([as seen in](https://threatpost.com/jenkins-atlassian-confluence-cyberattacks/169249/) the recent Jenkins attack). Atlassian Confluence, like AD SelfService Plus, allows centralized cloud access to a raft of sensitive corporate information, being a collaboration platform where business teams can organize its work in one place.


How to Know if Zoho AD SelfService Plus is Vulnerable
-----------------------------------------------------


Users can tell if they’ve been affected by taking a gander at the \ManageEngine\ADSelfService Plus\logs folder to see if the following strings are found in the access log entries:


Zoho also said that users will find the following files in the ADSelfService Plus installation folder if running a vulnerable version:


**It’s time to evolve threat hunting into a pursuit of adversaries.**[**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**Threatpost and Cybersixgill for**[**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**and get a guided tour of the dark web and learn how to track threat actors before their next attack.**[**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with independent researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[Zoho]] [[ADSelfService]] [[ManageEngine]] [[cloud]] [[Zoho’s]] [[zero-day]] [[ThreatPost]]
