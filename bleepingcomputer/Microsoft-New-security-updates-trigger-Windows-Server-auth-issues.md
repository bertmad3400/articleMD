# Microsoft: New security updates trigger Windows Server auth issues
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-new-security-updates-trigger-windows-server-auth-issues/)
+ Date: November 11, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft: New security updates trigger Windows Server auth issues](https://www.bleepstatic.com/content/hl-images/2021/10/28/cybersecurity-header-2.jpg)


Microsoft says users might experience authentication issues on Domain Controllers (DC) running Windows Server. after installing security updates released during the November Patch Tuesday.


These authentication issues impact systems running Windows Server 2019 and lower versions with certain Kerberos delegation scenarios.


The list of affected platforms also includes Windows Server 2016, Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 SP1, and Windows Server 2008 SP2.


The authentication issues prevent end-users in Active Directory on-premises or hybrid Azure Active Directory environments from signing into services or applications using [Single Sign-On (SSO)](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/what-is-single-sign-on).


"After installing the November security updates, [..] you might have authentication failures on servers relating to Kerberos Tickets acquired via S4u2self," Microsoft [explains](https://docs.microsoft.com/en-us/windows/release-health/status-windows-10-1809-and-windows-server-2019#2748msgdesc) on the Windows health dashboard.


"The authentication failures are a result of Kerberos Tickets acquired via S4u2self and used as evidence tickets for protocol transition to delegate to backend services which fail signature validation."


The complete list of originating updates for this Windows Server known issue includes:


* [KB5007206](https://support.microsoft.com/help/5007206) - Windows Server 2019
* [KB5007192](https://support.microsoft.com/help/5007192) - Windows Server 2016
* [KB5007247](https://support.microsoft.com/help/5007247) - Windows Server 2012 R2
* [KB5007260](https://support.microsoft.com/help/5007260) - Windows Server 2012
* [KB5007236](https://support.microsoft.com/help/5007236) - Windows Server 2008 R2 SP1
* [KB5007263](https://support.microsoft.com/help/5007263) - Windows Server 2008 SP2


Microsoft said it's working on a resolution to address this Windows Server issue and estimates that it will provide a solution soon.



> 
> Kerberos authentication will fail on Kerberos delegation scenarios that rely on the front-end service to retrieve a Kerberos ticket on behalf of a user to access a backend service. Important Kerberos delegation scenarios where a Kerberos client provides the front-end service with an evidence ticket are not impacted. Pure Azure Active Directory environments are not impacted by this issue. - Microsoft
> 
> 
> 


Impacted environments
---------------------


According to Microsoft, affected environments might be using one of the following services or apps:


* Azure Active Directory (AAD) Application Proxy Integrated Windows Authentication (IWA) using Kerberos Constrained Delegation (KCD)
* Web Application Proxy (WAP) Integrated Windows Authentication (IWA) Single Sign On (SSO)
* Active Directory Federated Services (ADFS)
* Microsoft SQL Server
* Internet Information Services (IIS) using Integrated Windows Authentication (IWA)
* Intermediate devices including Load Balancers performing delegated authentication


Users might see one or more of the errors below on impacted systems:


* Event Viewer might show Microsoft-Windows-Kerberos-Key-Distribution-Center [event 18](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc733969(v=ws.10)) logged in the System event log
* Error 0x8009030c with text Web Application Proxy encountered an unexpected is logged in the Azure AD Application Proxy event log in Microsoft-AAD Application Proxy Connector event 12027
* Network traces contain the following signature similar to the following:
	+ 7281 24:44 (644) 10.11.2.12 .contoso.com KerberosV5 KerberosV5:TGS Request Realm: CONTOSO.COM Sname: http/xxxxx-xxx.contoso.com
	+ 7282 7290 (0) . CONTOSO.COM




#### Tags:
[[Windows]] [[Kerberos]] [[Microsoft]] [[R2]] [[(IWA)]] [[Bleeping Computer]]
