# CISA urges admins to patch critical Discourse code execution bug
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/cisa-urges-admins-to-patch-critical-discourse-code-execution-bug/)
+ Date: October 25, 2021
+ Author: Bill Toulas


## Article:
![code bug](https://www.bleepstatic.com/content/hl-images/2021/10/25/code_bug.jpg?rand=1085707803)


A critical Discourse remote code execution (RCE) vulnerability tracked as CVE-2021-41163 was fixed via an urgent update by the developer on Friday


Discourse is an open-source forum, long-form chat, and mailing list management platform widely deployed on the web, offering excellent usability and integration potential while focusing heavily on social features. 






The vulnerable versions are 2.7.8 and older, and the best way to address the risk is to update to 2.7.9 or later, which came out on Friday. The latest beta and test versions have also been patched against the flaw. 


According to official stats, Discourse was used to publish 3.5 million posts viewed by 405 million users in September 2021 alone.


Because of Discourse's widespread use, CISA also published [an alert](https://us-cert.cisa.gov/ncas/current-activity/2021/10/24/critical-rce-vulnerability-discourse) about the flaw, urging forum admins to update to the latest available version or apply the necessary workarounds. 


[The exploit](https://nvd.nist.gov/vuln/detail/CVE-2021-41163) is triggered by sending a maliciously crafted request to the vulnerable software, taking advantage of a lack of validation in the 'subscribe-url' values. 


Calls to `open()` with user supplied input allows to invoke OS commands with whatever rights the web app runs on, which is typically 'www-data' (admin). 


The implications of a CVE-2021-41163 exploit and the ease of leveraging it (sending an unauthenticated POST) result in a CVSS v3 score of 10.0 (critical), so patching it should be treated as an emergency.


A Shodan search has returned 8,641 Discourse deployments, many of which could still be exposed to RCE exploitation potential. However, all SaaS instances have been patched since Wednesday.



![Discourse deployments](https://www.bleepstatic.com/images/news/u/1220909/Security/shodan%20search.jpg)**Discourse deployments**
Anyone who can't update to the latest version is advised to [block requests](https://github.com/discourse/discourse/security/advisories/GHSA-jcjx-pvpc-qgwq) with a path starting with '/webhooks/aws' at an upstream proxy. 


At this time, the flaw is still undergoing technical analysis, but the researcher who discovered it has [published rich technical details](https://0day.click/recipe/discourse-sns-rce/) about it.  


Publishing too many details about the flaw only a few days after a fix has been made available would only give pointers to hackers on how to exploit it. Still, the researcher told us the patch itself made deductions easy anyway. 


The [researcher](https://twitter.com/joernchen) who discovered the flaw told BleepingComputer that he reported the problem to the Discourse team immediately, on October 10, 2021.


We have reached out to Discourse to find out if they have seen any evidence of exploitation of CVE-2021-41163 in the wild, and we will update this post as soon as we hear back from them.. 




#### Tags:
[[CVE-2021-41163]] [[Bleeping Computer]]
