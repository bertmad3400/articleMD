# Microsoft Azure App Service flaw exposed customer source code
### A security flaw found in Azure App Service, a Microsoft-managed platform for building and hosting web apps, led to the exposure of PHP, Node, Python, Ruby, or Java customer source code deployed on Microsoft's cloud infrastructure.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/microsoft-azure-app-service-flaw-exposed-customer-source-code/
+ Date: 2021-12-22T14:15:54-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/09/05/Microsoft.jpg)

![Microsoft Azure App Service flaw exposed customer source code](https://www.bleepstatic.com/content/hl-images/2021/09/05/Microsoft.jpg)


A security flaw found in Azure App Service, a Microsoft-managed platform for building and hosting web apps, led to the exposure of PHP, Node, Python, Ruby, or Java customer source code deployed on Microsoft's cloud infrastructure.


Only Azure App Service Linux customers were impacted by the issue discovered and reported by researchers at cloud security vendor Wiz.io, with IIS-based applications deployed by Azure App Service Windows customers not being affected.


"The vulnerability, which we dubbed as 'NotLegit,' has existed since September 2017 and has probably been exploited in the wild," [Wiz.io added](https://www.wiz.io/blog/azure-app-service-source-code-leak).


"Small groups of customers are still potentially exposed and should take certain user actions to protect their applications, as detailed in several email alerts Microsoft issued between the 7th - 15th of December, 2021."


The researchers tested their theory that the insecure default behavior in Azure App Service Linux was likely exploited in the wild by deploying their own vulnerable app. 


Within just four days, they saw the first attempts made by threat actors to access the contents of the exposed source code folder.



![Attempts to access exposed source code](https://www.bleepstatic.com/images/news/u/1109292/2021/Attempts_to_access_exposed_source_code.PNG)*Attempts to access exposed source code (Wiz.io)*
While this could point to attackers already knowing of the NotLegit flaw and specifically trying to find exposed Azure App Service apps' source code, these scans could also be explained as normal scans for exposed .git folders.


As BleepingComputer previously reported, attackers have gained access to files belonging to high-profile organizations after finding public .git folders, including [multiple Indian government sites](https://www.bleepingcomputer.com/news/security/researchers-hacked-indian-govt-sites-via-exposed-git-and-env-files/) and the [United Nations Environmental Programme (UNEP)](https://www.bleepingcomputer.com/news/security/united-nations-data-breach-exposed-over-100k-unep-staff-records/).


Affected Azure App Service applications include all PHP, Node, Python, Ruby, and Java apps coded to serve static content if:


* deployed using Local Git on a clean default application in Azure App Service starting with 2013
* deployed in Azure App Service since 2013 using any Git source, after a file was created or modified in the app container

Flaw mitigated, exposed customers notified
------------------------------------------


"MSRC was informed by Wiz.io [..] of an issue where customers can unintentionally configure the .git folder to be created in the content root, which would put them at risk for information disclosure," Microsoft [said](https://msrc-blog.microsoft.com/2021/12/22/azure-app-service-linux-source-repository-exposure/) today.


"This, when combined with an application configured to serve static content, makes it possible for others to download files not intended to be public."


The Azure App Service team and MSRC have already applied a fix designed to cover most impacted customers and alerted all customers still exposed after enabling in-place deployment or uploading the .git folder to the content directory.


Microsoft mitigated the flaw by updating PHP images to disallow serving the .git folder as static content.


The Azure App Service documentation was also updated with a new section on properly [securing apps' source code](https://docs.microsoft.com/en-us/azure/app-service/security-recommendations#data-protection) and [in-place deployments](https://github.com/projectkudu/kudu/wiki/Deploying-inplace-and-without-repository#inplace-deployment).



Further technical details on the NotLegit security flaw and a disclosure timeline can be found in [Microsoft's blog post](https://msrc-blog.microsoft.com/2021/12/22/azure-app-service-linux-source-repository-exposure/) and [Wiz Research Team's report](https://www.wiz.io/blog/azure-app-service-source-code-leak).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Apps]] [[Php]] [[Wiz.io]] [[Bleeping Computer]]

