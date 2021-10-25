# Hackers use SQL injection bug in BillQuick billing app to deploy ransomware
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/hackers-use-sql-injection-bug-in-billquick-billing-app-to-deploy-ransomware/)
+ Date: October 25, 2021
+ Author: Catalin Cimpanu


## Article:
![Hackers use SQL injection bug in BillQuick billing app to deploy ransomware](https://therecord.media/wp-content/uploads/2021/10/billing-dashboard.png)

At least one hacking group is exploiting a security flaw in a popular billing software suite to gain initial access, take over servers, and then deploy ransomware inside companies’ networks.


Discovered by Huntress Labs this month, the attacks targeted BillQuick Web Suite, a billing solution developed by California-based [BQE](https://www.bqe.com/products/billquick/).


“Hackers were able to successfully exploit [CVE-2021-42258](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-42258)—using it to gain initial access to a US engineering company—and deploy ransomware across the victim’s network,” Caleb Stewart, a security researcher for Huntress Labs, [said over the weekend](https://www.huntress.com/blog/threat-advisory-hackers-are-exploiting-a-vulnerability-in-popular-billing-software-to-deploy-ransomware).


Stewart said Huntress investigated the attack and was able to reproduce the attacker’s exploit, described as an SQL injection vulnerability in the app’s login page.


“Simply navigating to the login page and entering a single quote (`’`) can trigger this bug,” Steward said. “Further, the error handlers for this page display a full traceback, which could contain sensitive information about the server-side code.”


Huntress said the vulnerability could be abused to dump the content of the MSSQL database used by the BillQuick software and even for remote code execution scenarios that would allow hackers control over the entire server.


This is how Huntress believes the threat actor was able to enter customer networks and deploy ransomware.


### Eight other issues also discovered; patches available


In addition to the SQL injection bug exploited in the ransomware attacks, Stewart said Huntress also discovered eight other vulnerabilities in the BillQuick software during their investigation.


All issues were reported to the vendor, which released patches for the actively-exploited CVE-2021-42258 SQL injection bug in [WebSuite 2021 version 22.0.9.1](http://billquick.net/download/Support_Download/BQWS2021Upgrade/WebSuite2021LogFile_9_1.pdf) on October 7. Patches for the eight other issues are forthcoming.


Huntress is now warning customers who still run BillQuick Web Suite 2018 to 2021 v22.0.9.0 to update their billing suites.


According to the BQE website, the company claims more than 400,000 customers. A BQE spokesperson was not immediately available for comment.





#### Tags:
[[BillQuick]] [[ransomware]] [[SQL]] [[The Record]]
