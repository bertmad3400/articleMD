# Microsoft informs customers of 'NotLegit' Azure bug | ZDNet
### The issue affects some Azure App Service Linux customers.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/notlegit-azure-bug-addressed-by-microsoft/
+ Date: 2021-12-23 20:40:57
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/ae2b6c6c16c9f0b2730ed4ce9da332f831f78976/2021/10/14/345a9c26-72e2-46a1-b1cd-789556569f1a/microsoft.jpg?width=770&height=578&fit=crop&auto=webp)

Microsoft's Security Response Center [has released a blog](https://msrc-blog.microsoft.com/2021/12/22/azure-app-service-linux-source-repository-exposure/) explaining its response to the ["NotLegit" bug in Azure](https://www.wiz.io/blog/azure-app-service-source-code-leak) that was discovered by cloud security company Wiz.io.

Wiz.io said all PHP, Node, Ruby, and Python applications that were deployed using "Local Git" on a clean default application in Azure App Service since September 2017 are affected. They added that all PHP, Node, Ruby, and Python applications that were deployed in Azure App Service from September 2017 onward using any Git source, after a file was created or modified in the application container, were also affected.

Microsoft clarified in their response that the issue affects App Service Linux customers who deployed applications using Local Git after files were created or modified in the content root directory. They explained that this happens "because the system attempts to preserve the currently deployed files as part of repository contents, and activates what is referred to as in-place deployments by deployment engine (Kudu)." 

"The images used for PHP runtime were configured to serve all static content in the content root folder. After this issue was brought to our attention, we updated all PHP images to disallow serving the .git folder as static content as a defense in depth measure," Microsoft explained. 

"For these languages since the application code controls whether it serves static content, we recommend customers review the code to make sure that only the relevant code is served out."

They noted that not all users of Local Git were impacted by the vulnerability and that the Azure App Service Windows was not affected. 

Microsoft has notified the customers that are affected by the problem, including those that were impacted due to the activation of in-place deployment and those who had the .git folder uploaded to the content directory. They also updated their Security Recommendations document with an additional section on securing source code and updated the documentation for in-place deployments.






The Wiz Research Team said on Tuesday that it first notified Microsoft of the issue on October 7 and worked with them through the month to address it. The fix was deployed in November and customers were notified by December. Wiz was paid a bug bounty of $7,500.

Microsoft did not say if the vulnerability has been exploited but Wiz said "NotLegit" is "extremely easy, common, and is actively being exploited."

"To assess the chance of exposure with the issue we found, we deployed a vulnerable Azure App Service application, linked it to an unused domain, and waited patiently to see if anyone tried to reach the .git files. Within 4 days of deploying, we were not surprised to see multiple requests for the .git folder from unknown actors," the researchers explained. 

"Small groups of customers are still potentially exposed and should take certain user actions to protect their applications, as detailed in several email alerts Microsoft issued between the 7th - 15th of December, 2021."

The Wiz Research Team noted that accidentally exposing the Git folder through user error is a security issue that has impacted organizations like the [United Nations](https://johnjhacking.com/blog/unep-breach/) and a number of [Indian government sites](https://johnjhacking.com/blog/indian-government-breached-massive-amount-of-critical-vulnerabilities/). 

Vectra CTO Oliver Tavakoli said the impact of the vulnerability will be highly variable. Accessing the source code underlying an application (and possibly other files which might have been left in the same directory) may provide information that could be leveraged for other attacks, Tavakoli said. 

"The fact that the researchers set up what amounts to a honeypot and saw the vulnerability exploited in the wild is of particular concern as it means that the vulnerability was not a well-kept secret," Tavakoli explained. 

JupiterOne field security director Jasmine Henry told ZDNet that leaked source code puts an organization in an incredibly vulnerable position to threat actors who can instantly steal intellectual property or launch an exploit tailored to unique weaknesses in the source code. 

"The NotLegit vulnerability is especially eye-opening since it highlights the growing security risk caused by privileged accounts and services, even in the absence of developer error," Henry said. 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Php]] [[Notlegit]] [[In-place]] [["the]] [[Tavakoli]] [[ZDNet]]

