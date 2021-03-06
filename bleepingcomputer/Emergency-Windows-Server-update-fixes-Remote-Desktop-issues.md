# Emergency Windows Server update fixes Remote Desktop issues
### Microsoft has released an emergency out-of-band update to address a Windows Server bug leading to Remote Desktop connection and performance issues.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/emergency-windows-server-update-fixes-remote-desktop-issues/
+ Date: 2022-01-04T18:51:25-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/07/23/Windows-attack.jpg)

![Emergency Windows Server update fixes Remote Desktop issues](https://www.bleepstatic.com/content/hl-images/2021/07/23/Windows-attack.jpg)


Microsoft has released an emergency out-of-band update to address a Windows Server bug leading to Remote Desktop connection and performance issues.


"Microsoft is releasing Out-of-band (OOB) updates today, January 4, 2022, to resolve issues in which Windows Server might experience a black screen, slow sign in, or general slowness," the company [explains](https://docs.microsoft.com/en-us/windows/release-health/windows-message-center#2772).


"You might also be unable to use Remote Desktop to reach the server. In some circumstances, the server might stop responding."


Affected platforms include Windows Server 2022, Windows Server 2019, Windows Server 2016, and Windows Server 2012 R2.


The updates that address this issue are not available from Windows Update and will not install automatically on affected systems.


You can get the standalone [KB5010196](https://support.microsoft.com/help/5010196) update package for Windows Server 2019 using the instructions available in [this knowledgebase article](https://support.microsoft.com/en-us/topic/january-4-2022-kb5010196-os-build-17763-2369-out-of-band-1a7a9a37-b154-4e73-92dc-1a2f65a4c0d1).


You can also download the update from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5010196). Enterprise admins can import this update into Windows Server Update Services (WSUS) manually using the instructions available in the [Microsoft Update Catalog](https://docs.microsoft.com/en-us/windows-server/administration/windows-server-update-services/manage/wsus-and-the-catalog-site#the-microsoft-update-catalog-site).


KB5010196 is a cumulative update, so you will not have to deploy previous Windows Server updates before installing it.


Fix not yet available for all impacted Windows versions
-------------------------------------------------------


Microsoft has not yet released the updates for Windows Server 2022, Windows Server 2016, and Windows Server 2012 R2, but it's working on a fix and will provide a solution in the coming days.


In November, [Redmond released out-of-band updates](https://www.bleepingcomputer.com/news/microsoft/new-microsoft-emergency-updates-fix-windows-server-auth-issues/) to fix authentication issues linked to Kerberos delegation scenarios impacting Domain Controllers (DC) running supported versions of Windows Server.


As Microsoft explained, on impacted systems, end-users couldn't sign into services or applications using [Single Sign-On (SSO)](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/what-is-single-sign-on) in Active Directory on-premises or hybrid Azure Active Directory environments.


One week earlier, [Microsoft had to issue another set of emergency updates](https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5008295-emergency-update-fixes-built-in-app-mess/) to address Windows 11 issues while opening or using some built-in apps and features [due to an expired Microsoft digital certificate](https://www.bleepingcomputer.com/news/microsoft/some-windows-11-apps-are-broken-due-to-expired-certificate/).


Before this, last year, the company also pushed a string of out-of-band updates to fix [printing issues](https://www.bleepingcomputer.com/news/microsoft/new-windows-10-emergency-updates-fix-remaining-printing-issues/), [WiFi crashes](https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-emergency-fix-for-windows-10-wifi-crashes/), [PDF opening issues,](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5004760-emergency-update-fixes-pdf-opening-issue/) the [Windows PrintNightmare zero-day](https://www.bleepingcomputer.com/news/security/microsoft-pushes-emergency-update-for-windows-printnightmare-zero-day/), and another series of [printing issues](https://www.bleepingcomputer.com/news/microsoft/new-windows-10-kb5005394-emergency-update-fixes-printing-issues/).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[Out-of-band]] [[Bleeping Computer]]

