# Zimbra Server Bugs Could Lead to Email Plundering
### Two bugs, now patched except in older versions, could be chained to allow attackers to hijack Zimbra server by simply sending a malicious email. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168188)
+ Date: July 27, 2021  1:30 pm
+ Author: Lisa Vaas


## Article:
Zimbra webmail server has two flaws that could let an attacker paw through the inbox and outbox of all the employees in all the enterprises that use the immensely popular collaboration tool, researchers say.


In a Tuesday [writeup](https://blog.sonarsource.com/zimbra-webmail-compromise-via-email), SonarSource called it a “drastic” situation, given Zimbra’s popularity and the highly sensitive nature of the scads of messages that it handles. According to Zimbra’s site, its email and collaboration tools are used by over 200,000 businesses, over a thousand government and financial institutions, and hundreds of millions of users to exchange emails every day.


“When attackers get access to an employee’s email account, it often has drastic security implications,” according to the report. “Besides the confidential information and documents that are exchanged, an email account is often linked to other sensitive accounts that allow a password reset. Think about it, what could an attacker do with your inbox?”



Well, they’d freely romp through accounts, for one. SonarSource researchers discovered two vulnerabilities in the open-source Zimbra code that can be chained together to give attackers unrestricted access to Zimbra mail servers and to all sent and received emails of all employees.


Malicious Email Could Carry Crafted JavaScript Payload
------------------------------------------------------


Discovered by Simon Scannell, a vulnerability researcher at SonarSource, the first flaw could be triggered just by opening a malicious email containing a JavaScript payload. If a victim were to open such a riggedd email, they’d trigger a cross-site scripting (XSS) bug (CVE-2021-35208) in their browser. When executed, that payload would provide an attacker with access to the victim’s emails of the victim, as well as their webmail session, SonarSource said.


Plus, it would be ground zero for other attacks, they said: “With this, other features of Zimbra could be accessed and further attacks could be launched.”


The second flaw is a bypass of an allow-list that leads to a powerful server-side request forgery (SSRF) vulnerability (CVE-2021-35209) that can be exploited by an authenticated account belonging to a member of a targeted organization who has any permission role whatsoever.


The two bugs, if combined, would give a remote attacker the power to extract precious goodies, including Google Cloud API Tokens or AWS IAM credentials from instances within the cloud infrastructure.


The $80 Million Misconfiguration
--------------------------------


That may ring a bell: The researchers pointed to a 2019 breach of Capital One that involved a similar SSRF bug. Thanks to a cloud misconfiguration, the attacker – notably, a [former AWS engineer](https://threatpost.com/aws-arrest-data-breach-capital-one/146758/) – got away with the [personal data of over 100 million people](https://www.nytimes.com/2019/07/29/business/capital-one-data-breach-hacked.html). The [FBI got him](https://threatpost.com/aws-arrest-data-breach-capital-one/146758/), but that was one costly SSRF glitch: Capital One had to fork over [$80 million](https://www.nytimes.com/2020/08/06/business/capital-one-hack-settlement.html) to settle federal bank regulators’ claims that it lacked proper cybersecurity protocols.


SonarSource put it mildly: “SSRF vulnerabilities have become an increasingly dangerous bug class, especially for cloud-native applications,” according to the writeup. The security firm said that it doesn’t know whether Zimbra Cloud, a SaaS solution using AWS, was affected by the vulnerability.


Scannell told [PortSwigger](https://portswigger.net/daily-swig/chained-zimbra-flaws-gave-attackers-unrestricted-access-to-mail-servers) that the SSRF flaw lets an attacker send HTTP requests to arbitrary hosts or ports. “Combined with protocol smuggling, this could lead to RCE,” he was quoted as saying. “It could also enable an attacker to steal highly sensitive metadata, such as access tokens to the account that is associated with the instance that would have been exploited.”


Specifically, as mentioned previously, an attacker could get at access tokens including Google Cloud API tokens or AWS IAM credentials from cloud instances.


The Zimbra team has fixed both issues, with Patch 18 for the 8.8.15 series and Patch 16 for the 9.0 series. SonarSource says that prior versions of both branches are, however, still vulnerable. Threatpost reached out to Zimbra to find out what the plan is for patching older versions and will update the article if we find out.


The issues were reported to Zimbra on May 20 and 22, with patches released on June 28 for the 8.8.15 and 9.0 series.


Scannell told PortSwigger that the vulnerabilities, both rated as medium severity, could have had serious effects.”Both vulnerabilities work on default configuration and are affecting the Zimbra core,” he told the outlet: a lot of potential impact, given those 200,000 businesses to which Zimbra lays claim.


Past Pouncing on Zimbra
-----------------------


It’s a safe bet that attackers will try to exploit the vulnerabilities, given the number of bullseyes that have been painted onto Zimbra’s back.


In April, a Zimbra bug – CVE-2019-9670, in Synacor Zimbra Collaboration Suite (XXE) – was one of [five flaws under nation-state attack](https://threatpost.com/nsa-security-bugs-active-nation-state-cyberattack/165446/) that prompted a National Security Agency (NSA) warning about an APT29 campaign that was bent on stealing credentials and more.


Zimbra must be a favorite target of the Russia-linked APT29 threat group: Before the April campaign, in July 2020, the cybergang set its sights on pharma research in Western nations in a likely attempt to [steal research](https://threatpost.com/state-sponsored-hackers-steal-covid-19-vaccine-research/157514/) for a COVID-19 vaccine. The grab included using exploits for known vulnerabilities, including one in Zimbra (CVE-2019-9670).


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[Zimbra]] [[SonarSource]] [[Zimbra’s]] [[emails]] [[AWS]] [[cloud]] [[SSRF]] [[vulnerabilities,]] [[ThreatPost]]
