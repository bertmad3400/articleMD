# BillQuick Billing App Rigged to Inflict Ransomware
### A SQL injection bug in the BillQuick billing app has not only leaked sensitive information, it’s also let malicious actors remotely execute code and deploy ransomware. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175720)
+ Date: October 25, 2021  4:51 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/25163951/time_clock-e1635194404919.jpg)
Threat actors are picking apart a now-patched, critical vulnerability in a popular time and billing system to take over vulnerable servers and inflict companies’ networks with ransomware.


Discovered by Huntress Labs earlier this month, the ongoing attacks focus on a SQL injection bug in BillQuick Web Suite from BQE Software.


“Hackers were able to successfully exploit [CVE-2021-42258](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-42258) – using it to gain initial access to a US engineering company – and deploy ransomware across the victim’s network,” Caleb Stewart, a security researcher for Huntress Labs, [said in a Friday post.](https://www.huntress.com/blog/threat-advisory-hackers-are-exploiting-a-vulnerability-in-popular-billing-software-to-deploy-ransomware).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The flaw concerns an SQL injection attack: a type of attack that allows a cyberattacker to interfere with the queries that an application makes to its database. These attacks are typically carried out by inserting malicious SQL statements into an entry field for execution.


Attackers used the SQL injection vulnerability, which allows for remote code execution (RCE), to gain initial access to the unnamed engineering company and to unleash a ransomware attack on its network, Huntress said.


BQE claims to have a user base of more than 400,000 users worldwide, including what the company describes as “leading architects, engineers, accountants, attorneys, IT specialists and business consultants.”


That kind of number is great for brand promotion, not so great for a malicious campaign targeting its customers base, Huntress Labs said.


Warning Bells
-------------


Stewart said that Huntress’ spidey senses started to tingle after some of its so-called ransomware canary files were tripped. Those are files set up by Huntress managed service providers (MSPs) to trigger alerts if they’re changed, moved, or deleted,


The files were in an engineering company managed by one of Huntress’ MSPs. On investigating, Huntress analysts discovered Microsoft Defender antivirus alerts indicating malicious activity as the MSSQLSERVER$ service account, indicating that a threat actor may have exploited a web app to gain initial access.


Signs pointed to a foreign IP poking at a server hosting BillQuick, Stewart explained: “The server in question hosted BillQuick Web Suite 2020 (WS2020), and the connection logs indicated a foreign IP repeatedly sending POST requests to the web server logon endpoint leading up to the initial compromise.”


Huntress suspected that a bad actor was attempting to exploit BillQuick, so its researchers started to reverse-engineer the web app in order to trace the attacker’s steps. They managed to recreate the SQL injection attack, confirming that threat actors can use it to access customers’ BillQuck data and to run malicious commands on on-premises Windows servers.


Huntress notified BQE about the bug. At this point, Huntress is keeping details close to the vest while it assesses code changes implemented in the BillQuick update, [WebSuite 2021 version 22.0.9.1](http://billquick.net/download/Support_Download/BQWS2021Upgrade/WebSuite2021LogFile_9_1.pdf) – released on Oct. 7 – and while it works with BQE to address “multiple security concerns” that Huntress raised over the company’s BillQuick and Core products.


Eight More Bugs
---------------


Specifically, these are the other bugs found by Huntress that are now awaiting patches:


Bug Can Be Triggered with a Single Character
--------------------------------------------


Huntress said that triggering the now-patched SQL injection vulnerability is drop-dead simple: All you have to do is submit a login request with invalid characters in the username field. “Simply navigating to the login page and entering a single quote (`’`) can trigger this bug,” according to the analysis. “Further, the error handlers for this page display a full traceback, which could contain sensitive information about the server-side code.”


Huntress’ investigation found that the problem lies in concatenated SQL queries. The process of concatenation – i.e., joining two strings together – leads to SQL injection, whether it’s due to input that’s incorrectly filtered or wrongly typed.


“Essentially, this function allows a user to control the query that’s sent to the MSSQL database –which in this case, enables blind SQL injection via the application’s main login form,” Stewart explained.


In other words, an unauthorized user could exploit the vulnerability to dump the content of the MSSQL database used by the BillQuick app or for RCE, which could lead to attackers gaining control over an entire server.


Huntress is reportedly warning customers still running BillQuick Web Suite 2018 to 2021 v22.0.9.0 to update their billing suites. Threatpost reached out to BQE to find out how many users have been targeted in the ransomware campaign and which ransomware is in play and will update this story if we hear back.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[SQL]] [[BillQuick]] [[BQE]] [[ransomware]] [[Huntress’]] [[ThreatPost]]
