# Over 30,000 GitLab servers still unpatched against critical bug 
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/over-30-000-gitlab-servers-still-unpatched-against-critical-bug/)
+ Date: November 2, 2021
+ Author: Bill Toulas


## Article:
![coder](https://www.bleepstatic.com/content/hl-images/2021/11/02/coder.jpg?rand=1710330047)


A critical unauthenticated, remote code execution GitLab flaw fixed on April 14, 2021, remains exploitable, with over 50% of deployments remaining unpatched.


The vulnerability is tracked as [CVE-2021-22205](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22205) and has a CVSS v3 score of 10.0, allowing an unauthenticated, remote attacker to execute arbitrary commands as the 'git' user (repository admin).


This vulnerability gives the remote attacker full access to the repository, including deleting, modifying, and stealing source code.


Exploitation in the wild
------------------------


Hackers first started exploiting internet-facing GitLab servers [in June 2021](https://security.humanativaspa.it/gitlab-ce-cve-2021-22205-in-the-wild/) to create new users and give them admin rights.


The actors used a working exploit [published on GitHub](https://github.com/CsEnox/Gitlab-Exiftool-RCE/blob/main/exploit.py) on June 4, 2021, allowing them to abuse the vulnerable ExifTool component.


The threat actors do not need to authenticate or use a CSRF token or even a valid HTTP endpoint to use the exploit.


With the exploitation continuing to this day, researchers from Rapid7 decided to look into the number of unpatched systems and determine the scope of the underlying problem.


According to a report published by [Rapid7](https://www.rapid7.com/blog/post/2021/11/01/gitlab-unauthenticated-remote-code-execution-cve-2021-22205-exploited-in-the-wild/), at least 50% of the 60,000 internet-facing GitLab installations they found are not patched against the critical RCE flaw [fixed six months ago](http://about.gitlab.com/releases/2021/04/14/security-release-gitlab-13-10-3-released/).


Moreover, another 29% may or may not be vulnerable, as the analysts couldn't extract the version string for those servers.


Admins need to update to one of the following versions to patch the flaw:


* 13.10.3
* 13.9.6
* 13.8.8


Any versions earlier than that and down to 11.9 are vulnerable to exploitation whether you’re using GitLab Enterprise Edition (EE) or GitLab Community Edition (CE).


For more details on how to update GitLab, check out this [dedicated portal](https://about.gitlab.com/update/).


To ensure that your GitLab instance isn't vulnerable to exploitation, you can check its response to POST requests that attempt to exploit ExifTool's mishandling of image files.


The patched versions still allow someone to reach out to ExifTool, but the response to the request [should be a rejection](https://attackerkb.com/topics/D41jRUXCiJ/cve-2021-22205/rapid7-analysis) in the form of an HTTP 404 error.




#### Tags:
[[GitLab]] [[Bleeping Computer]]
