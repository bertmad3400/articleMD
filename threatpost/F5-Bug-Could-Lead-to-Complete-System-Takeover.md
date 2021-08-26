# F5 Bug Could Lead to Complete System Takeover
### The worst of 13 bugs fixed by the August updates could lead to complete system compromise for users in sensitive sectors running products in Appliance mode. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168952)
+ Date: August 26, 2021  12:40 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/04/29155056/F5-Big-IP-e1619725870974.jpg)
Application delivery and networking firm F5 released a baker’s dozen of 13 fixes for high-severity bugs, including one that could lead to complete system takeover and hence is boosted to “critical” for customers in “especially sensitive sectors.”


F5 – maker of near-ubiquitously installed enterprise networking gear – released nearly 30 vulnerabilities for multiple devices in its [August security updates](https://support.f5.com/csp/article/K50974556).


The worst of the bunch is tracked as [CVE-2021-23031](https://support.f5.com/csp/article/K41351250) and affects BIG-IP modules Advanced WAF (Web Application Firewall) and the Application Security Manager (ASM) – specifically, the Traffic Management User Interface (TMUI).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


F5 said that when the vulnerability is exploited, “an authenticated attacker with access to the Configuration utility can execute arbitrary system commands, create or delete files, and/or disable services,” potentially leading to “complete system compromise.”


CVE-2021-23031 normally entails a high rating of 8.8 severity, but that gets jacked up to 9.9 for just those customers that are using [Appliance mode](https://support.f5.com/csp/article/K12815). The Appliance mode adds technical restrictions and is designed to meet the needs of customers in “especially sensitive sectors” by “limiting the BIG-IP system administrative access to match that of a typical network appliance and not a multi-user UNIX device.”


F5 lists a number of products that contain the affected code but aren’t vulnerable, given that attackers can’t exploit the code in default, standard or recommended configurations. F5 noted that there are a limited number of customers using it in the mode – i.e., Appliance mode – that elevates the vulnerability’s CVSSv3 severity score to 9.9 (critical).


No Viable Mitigation
--------------------


F5 said that there’s “no viable mitigation” that also allows users access to the Configuration utility, given that this attack can be pulled off by legitimate, authenticated users. The only way to mitigate is to pull the access of any users who aren’t “completely trusted,” according to the advisory.


Customers who can’t install a fixed version right off the bat can use the following temporary mitigations, which restrict access to the Configuration utility to only trusted networks or devices and thereby limit the attack surface:


Besides the critical CVE-2021-23031 flaw, the dozen high-severity security bugs addressed in this month’s patch release and listed in the table below have risk scores of between 7.2 and 7.5. The flaws include authenticated remote command execution (RCE), cross-site scripting (XSS) and request forgery, as well as insufficient permission and denial-of-service (DOS).


Half of them affect all modules, five impact the Advanced WAF and ASM, and one affects the DNS module.


CISA Security Advisory
----------------------


The Cybersecurity and Infrastructure Security Agency (CISA) issued a [security advisory](https://us-cert.cisa.gov/ncas/current-activity/2021/08/25/f5-releases-august-2021-security-advisory) encouraging users and admins to review [F5’s security advisory](https://support.f5.com/csp/article/K50974556) and to update the software or to apply mitigations ASAP.


“Don’t delay” is, of course, good advice when it comes to F5 equipment, given that the company’s enterprise networking can be found in some of the largest tech companies in the world, including Facebook, Microsoft and Oracle. It’s also found in the halls of a trove of Fortune 500 companies, including some of the world’s biggest financial institutions and ISPs.


That gear is also gleefully picked apart by attackers: [CVE 2020-5902](https://threatpost.com/patch-critical-f5-flaw-active-attack/157164/), a critical vulnerability in F5 Networks’ BIG-IP advanced delivery controller networking devices that, as of July 2020, was being exploited by attackers to scrape credentials, launch malware and more, was recently featured in [CISA’s list of top 30 bugs](https://threatpost.com/cisa-top-bugs-old-enough-to-buy-beer/168247/) “routinely” exploited in 2020 and into this year.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[F5]] [[CVE-2021-23031]] [[BIG-IP]] [[ThreatPost]]
