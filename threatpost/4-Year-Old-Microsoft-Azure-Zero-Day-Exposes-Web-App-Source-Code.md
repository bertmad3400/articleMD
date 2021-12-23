# 4-Year-Old Microsoft Azure Zero-Day Exposes Web App Source Code
### The security vulnerability could expose passwords and access tokens, along with blueprints for internal infrastructure and finding software vulnerabilities.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177270
+ Date: 2021-12-23T19:04:13+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/23140337/cloud.jpg)

The Microsoft Azure App Service has a four-year-old vulnerability that could reveal the source code of web apps written in PHP, Python, Ruby or Node, researchers said, that were deployed using Local Git.


The bug has almost certainly been exploited in the wild as a zero-day, according to an analysis from Wiz. The firm dubbed the vulnerability “NotLegit,” and said it has existed since September 2017.


The Azure App Service (aka Azure Web Apps) is a cloud computing-based platform for hosting websites and web applications. Local Git meanwhile allows developers to initiate a local Git repository within the Azure App Service container in order to deploy code straight to the server. After deployment, the application is accessible for anyone on the internet under the *.azurewebsites.net domain.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The issue arises because when using Local Git, the Git folder is also uploaded and publicly accessible on unpatched systems; it’s placed in the “/home/site/wwwroot” directory, which anyone could access.


This has serious ramifications from a security perspective, according to the firm.


“Besides the possibility that the source contains secrets like passwords and access tokens, leaked source code is often used for further sophisticated attacks like gathering intel on the R&D division, learning the internal infrastructure, and finding software vulnerabilities,” researchers noted in [a posting](https://www.wiz.io/blog/azure-app-service-source-code-leak) this week. “Finding vulnerabilities in software is much easier when the source code is available.”


They added, “basically, all a malicious actor had to do was to fetch the ‘/.git’ directory from the target application, and retrieve its source code.”


**Botched Mitigation**
----------------------


Microsoft did originally deploy a mitigation, in the form of adding a “web.config” file to the Git folder within the public directory that restricted public access; it turns out this is an incomplete fix though.


“Only Microsoft’s IIS webserver handles web.config files,” according to Wiz. “But [if] you use PHP, Ruby, Python or Node…these programming languages are deployed with different webservers (Apache, Nginx, Flask, etc.), which do not handle web.config files, leaving them unimpacted by the mitigation and therefore completely vulnerable.”


Wiz reported the lingering bug to Microsoft in October and was awarded a $7,500 bounty for the discovery; and the computing giant deployed fixes between the Dec. 7-15 via email to affected users.


**Likely Exploited in the Wild**
--------------------------------


Git folders are often mistakenly exposed through misconfiguration (not just vulnerabilities, as in this case), and as such, cybercriminals are on the lookout for them, researchers warned.


“An exposed Git folder is a common security issue that users make without even realizing it,” they said. “Malicious actors are continuously scanning the internet for exposed Git folders from which they can collect secrets and intellectual property.”


Wiz deployed a vulnerable Azure App Service application and linked it to an unused domain to see if there would be any exploitation.


“[We] waited patiently to see if anyone tried to reach the Git files,” they said. “Within four days of deploying, we were not surprised to see multiple requests for the Git folder from unknown actors….this exploitation method is extremely easy, common and is actively being exploited.”


The following users should evaluate the potential risk, according to Wiz, and make sure to update their systems:


* Users who deployed code via FTP or Web Deploy or Bash/SSH which resulted in files getting initialized in the web app before any git deployment;
* Users who enabled LocalGit on the web app;
* Users who subsequent Git clone/push sequence to publish updates.


“Because the security issue was in an Azure service, cloud users were exposed on a big scale, and without them knowing or having any control over it,” researchers noted.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=FTP]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[ThreatPost]]

