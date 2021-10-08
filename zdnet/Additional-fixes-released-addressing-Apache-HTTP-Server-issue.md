# Additional fixes released addressing Apache HTTP Server issue
### CISA said the vulnerabilities have been exploited in the wild.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/additional-fixes-released-addressing-apache-http-server-issue/)
+ Date: October 8, 2021
+ Author: Jonathan Greig


## Article:
Unknown

Apache [released](https://httpd.apache.org/security/vulnerabilities_24.html#CVE-2021-42013) additional fixes for CVE-2021-41773 on Thursday as government agencies like CISA warned that one vulnerability related to the Apache HTTP Server issue had been exploited in the wild. 

As ZDNet [reported](https://www.zdnet.com/article/apache-http-server-project-patches-exploited-zero-day-vulnerability/) on Wednesday, developers behind the Apache HTTP Server Project urged users to apply a fix immediately to resolve a zero-day vulnerability. 

The Apache Software Foundation [released](https://httpd.apache.org/) Apache HTTP Server version 2.4.50 to address two vulnerabilities that would allow an attacker to take control of an affected system. In a [notice](https://us-cert.cisa.gov/ncas/current-activity/2021/10/06/apache-releases-security-update-apache-http-server) on Wednesday, CISA said one of the vulnerabilities, [CVE-2021-41773](https://www.cve.org/CVERecord?id=CVE-2021-41773), has already been exploited in the wild.

"It was found that the fix for CVE-2021-41773 in Apache HTTP Server 2.4.50 was insufficient. An attacker could use a path traversal attack to map URLs to files outside the directories configured by Alias-like directives. If files outside of these directories are not protected by the usual default configuration "require all denied", these requests can succeed. If CGI scripts are also enabled for these aliased pathes, this could allow for remote code execution," Apache said in a notice.

"This issue only affects Apache 2.4.49 and Apache 2.4.50 and not earlier versions."

CISA [said](https://twitter.com/USCERT_gov/status/1446208533356236805) that "active scanning of Apache HTTP Server CVE-2021-41773 & CVE-2021-42013 is ongoing and expected to accelerate, likely leading to exploitation." 

"These vulnerabilities have been exploited in the wild. Please patch immediately if you haven't already -- this cannot wait until after the weekend," the government agency added. 






According to [Bleeping Computer](https://www.bleepingcomputer.com/news/security/apache-emergency-update-fixes-incomplete-patch-for-exploited-bug/), about [25% of websites worldwide](https://news.netcraft.com/archives/category/web-server-survey/) are backed by the open-source, cross-platform Apache HTTP Server. 

[Sonatype researchers](https://blog.sonatype.com/apache-servers-actively-exploited-in-wild-importance-of-prompt-patching) said that approximately 112,000 Apache servers are running the vulnerable version, with roughly 40% located in the United States. Rapid7 Labs [said](https://www.rapid7.com/blog/post/2021/10/06/apache-http-server-cve-2021-41773-exploited-in-the-wild/) it identified about 65,000 potentially vulnerable versions of Apache httpd exposed to the public internet on Wednesday. 

Researchers [say](https://twitter.com/bad_packets/status/1445617322815721473) the issue is actively being [scanned](https://twitter.com/GreyNoiseIO/status/1445565658758991875?s=20) for in the wild.

![map3-1-1024x635.png]()![map3-1-1024x635.png](https://www.zdnet.com/a/img/resize/1841d4d702bfa357ddcb78810991348262d32345/2021/10/07/107cb79b-87b5-4f9b-b450-97fc16a74c93/map3-1-1024x635.png?width=470&fit=bounds&auto=webp)
 Censys
 "The vulnerability itself is not exploitable in normal or default conditions. The biggest impact this issue will have will be on applications that have packaged Apache 2.4.49 and a configuration that enables the vulnerability. One such application is Control Webpanel (also known as CentOS Webpanel), which is used by hosting providers to administer websites, similar to cPanel," said Derek Abdine, CTO at Censys. 

"There are currently just over 21,000 of these that are Internet-facing and appear vulnerable."  

Censys senior security researcher Mark Ellzey added that he expects there to be some fallout for this but that it may not be widespread. Compared to recent vulnerabilities related to [Confluence](https://www.zdnet.com/article/us-cybercom-says-mass-exploitation-of-atlassian-confluence-vulnerability-ongoing-and-expected-to-accelerate/) or [VMware](https://www.zdnet.com/article/exploit-released-for-vmware-vulnerability-after-cisa-warning/), he said the urgency and effectiveness of exploits for this issue don't rise to a similar level. 

"Anything outside of the bad config is probably going to be a targeted attack on specific applications. I'd wager that we might see some code leaks," Ellzey said. 

The vulnerabilities were first [discovered](https://lists.apache.org/thread.html/r98d704ed4377ed889d40479db79ed1ee2f43b2ebdd79ce84b042df45@%3Cannounce.apache.org%3E) by Ash Daulton of the cPanel security team and the latest issues were found by Shungo Kumasaka, Dreamlab Technologies' Juan Escobar and NULL Life CTF's Fernando Muñoz. Exploits were quickly [created](https://twitter.com/ducnt_/status/1445386557574324234?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1445386557574324234%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Ftherecord.media%2Fapache-fixes-actively-exploited-web-server-zero-day%2F) and [released](https://twitter.com/ptswarm/status/1445376079548624899?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1445376079548624899%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Ftherecord.media%2Fapache-fixes-actively-exploited-web-server-zero-day%2F) once the vulnerability was publicized. 





#### Tags:
[[HTTP]] [[CVE-2021-41773]] [[wild.]] [[ZDNet]]
