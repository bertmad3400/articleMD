# BillQuick says patch coming after Huntress report identifies vulnerabilities used in ransomware attack
### A company spokesperson said a short-term patch will be released on 10/26.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/billquick-says-patch-coming-after-huntress-report-identifies-vulnerabilities-used-for-ransomware/)
+ Date: October 25, 2021
+ Author: Jonathan Greig


## Article:
Unknown

BillQuick has said a short-term patch will be released addressing some of the vulnerabilities identified this weekend by cybersecurity firm Huntress. 

In a [blog post](https://www.huntress.com/blog/threat-advisory-hackers-are-exploiting-a-vulnerability-in-popular-billing-software-to-deploy-ransomware) on Friday, Huntress security researcher Caleb Stewart said the company's ThreatOps team "discovered a critical vulnerability in multiple versions of BillQuick Web Suite, a time and billing system from BQE Software." 

"Hackers were able to successfully exploit CVE-2021-42258 -- using it to gain initial access to a US engineering company -- and deploy ransomware across the victim's network. Considering BQE's self-proclaimed user base of 400,000 users worldwide, a malicious campaign targeting their customer base is concerning," Stewart said. 

"This incident highlights a repeating pattern plaguing SMB software: well-established vendors are doing very little to proactively secure their applications and subject their unwitting customers to significant liability when sensitive data is inevitably leaked and/or ransomed."

Huntress also found eight other vulnerabilities: CVE-2021-42344, CVE-2021-42345, CVE-2021-42346, CVE-2021-42571, CVE-2021-42572, CVE-2021-42573, CVE-2021-42741, CVE-2021-42742.

In a statement to ZDNet, BQE Software said their engineering team is aware of the issues with BillQuick Web Suite, which customers use to host BillQuick, and said that vulnerability has been patched. 

"Huntress also identified additional vulnerabilities, which we have been actively investigating. We expect a short-term patch to the BQE Web Suite vulnerabilities to be in place by end of day on 10/26/2021 along with a firm timeline on when a full fix will be implemented," the spokesperson added. 






"The issue with BQE Web Suite affects fewer than 10% of our customers; we will be proactively communicating to each of them the existence of these issues, when they can expect the issues to be resolved, and what steps they can take in the interim to minimize their exposure."

Huntress explained how they were able to recreate the SQL injection-based attack, which they showed can be used to access customers' BillQuick data and run malicious commands on their on-premises Windows servers.

Huntress said it worked with BQE Software on the issue and commended the company for being responsive while also taking the issues seriously.

But the blog post notes that the bug could easily be triggered by "simply navigating to the login page and entering a single quote (`'`)."

"Further, the error handlers for this page display a full traceback, which could contain sensitive information about the server-side code," Stewart wrote. 

CVE-2021-42258 was [patched by BQE Software on October 7](http://billquick.net/download/Support_Download/BQWS2021Upgrade/WebSuite2021LogFile_9_1.pdf) in WebSuite 2021 version 22.0.9.1. But the eight other issues still need patches. 

Stewart told [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-used-billing-software-zero-day-to-deploy-ransomware/) that unnamed hackers used CVE-2021-42258 as an entry point into the US engineering company as part of a ransomware attack that took place over the Columbus Day weekend. The news outlet reported that the ransomware group did not leave a ransom note and did not have a readily-identifiable name.





#### Tags:
[[BQE]] [[BillQuick]] [[CVE-2021-42258]] [[ransomware]] [[ZDNet]]
