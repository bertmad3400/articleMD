# Apache Web Server Zero-Day Exposes Sensitive Data
### The open-source project has rolled out a security fix for CVE-2021-41773, for which public cyberattack exploit code is circulating.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175340)
+ Date: October 5, 2021  4:01 pm
+ Author: Tara Seals


## Article:
Apache Software has quickly issued a fix for a zero-day security bug in the Apache HTTP Server, which was first reported to the project last week. The vulnerability is under active exploitation in the wild, it said, and could allow attackers to access sensitive information.


According to a [security advisory](https://httpd.apache.org/security/vulnerabilities_24.html) issued on Monday, the issue (CVE-2021-41773) could allow path traversal and subsequent file disclosure. Path traversal issues allow unauthorized people to access files on a web server, by tricking either the web server or the web application running on it into returning files that exist outside of the web root folder.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


In this case, the issue affects only version 2.4.49 of Apache’s open-source web server, which offers cross-platform operability with all modern operating systems, including UNIX and Windows.


“A flaw was found in a change made to path normalization in Apache HTTP Server 2.4.49,” according to the advisory. “An attacker could use a path-traversal attack to map URLs to files outside the expected document root. If files outside of the document root are not protected by ‘require all denied,’ these requests can succeed.”


The bug could also expose the source of interpreted files like CGI scripts, the advisory added, which which may contain sensitive information that attackers can exploit for further attacks.


Researchers such as the offensive team at Positive Technologies quickly created proof-of-concept exploits verifying the attack path, so expect more attack avenues to be availably publicly soon:



Tenable [noted that](https://www.tenable.com/blog/cve-2021-41773-path-traversal-zero-day-in-apache-http-server-exploited) a Shodan search on Tuesday turned up about 112,000 Apache HTTP Servers that are confirmed to be running the vulnerable version, including 43,000 or so in the U.S.


“However, other vulnerable web servers might be configured to not display version information,” according to the firm’s blog.


Users can protect themselves by upgrading to version 2.4.50. It should be noted that “require all denied” (which denies access to all requests) is the default for protecting documents outside of the web root, [researchers have reported](https://twitter.com/damian_89_/status/1445388530130227208) – which mitigates the issue.


Apache credited Ash Daulton and the cPanel Security Team for reporting the bug.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[HTTP]] [[ThreatPost]]
