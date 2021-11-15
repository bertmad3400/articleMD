# New Microsoft emergency updates fix Windows Server auth issues
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/new-microsoft-emergency-updates-fix-windows-server-auth-issues/)
+ Date: November 15, 2021
+ Author: Sergiu Gatlan


## Article:
![New Microsoft emergency updates fix Windows Server auth issues](https://www.bleepstatic.com/content/hl-images/2021/09/15/Microsoft_passwordless.jpg)


Microsoft has released out-of-band updates to address authentication failures related to Kerberos delegation scenarios impacting Domain Controllers (DC) running supported versions of Windows Server.


On impacted systems, end-users cannot sign into services or applications using [Single Sign-On (SSO)](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/what-is-single-sign-on) in Active Directory on-premises or hybrid Azure Active Directory environments.


These issues affect systems running Windows Server 2019 and lower versions, including Windows Server 2016, Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 SP1, and Windows Server 2008 SP2.


The emergency updates address "a known issue that might cause authentication failures related to Kerberos tickets you acquired from Service for User to Self (S4U2self)," a Microsoft announcement explained on Sunday.


"This issue occurs after you install the November 9, 2021 security updates on domain controllers (DC) that are running Windows Server."


**The complete list of out-of-band updates released by Microsoft over the weekend includes:**


* Windows Server 2019: [KB5008602](https://support.microsoft.com/help/5008602) — [DOWNLOAD](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5008602)
* Windows Server 2016: [KB5008601](https://support.microsoft.com/help/5008601) — [DOWNLOAD](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5008601)
* Windows Server 2012 R2: [KB5008603](https://support.microsoft.com/help/5008603) — [DOWNLOAD](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5008603)
* Windows Server 2012: [KB5008604](https://support.microsoft.com/help/5008604) — [DOWNLOAD](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5008604)
* Windows Server 2008 R2 SP1: [KB5008605](https://support.microsoft.com/help/5008605) — [DOWNLOAD](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5008605)
* Windows Server 2008 SP2: [KB5008606](https://support.microsoft.com/help/5008606) — [DOWNLOAD](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5008606)


How to deploy the OOB updates
-----------------------------


You will not be able to install these emergency updates through Windows Update, and they will also not install automatically on affected DCs.


To download the standalone update package, you will have to search for them in the Microsoft Update Catalog (you can also use the download links available above).


You can import this update into Windows Server Update Services (WSUS) manually using the instructions available in the [Microsoft Update Catalog](https://docs.microsoft.com/en-us/windows-server/administration/windows-server-update-services/manage/wsus-and-the-catalog-site#the-microsoft-update-catalog-site).


On Thursday, when Microsoft confirmed these issues, the company said that users might see one or more of the following errors on impacted systems:


* Event Viewer might show Microsoft-Windows-Kerberos-Key-Distribution-Center [event 18](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc733969(v=ws.10)) logged in the System event log
* Error 0x8009030c with text Web Application Proxy encountered an unexpected is logged in the Azure AD Application Proxy event log in Microsoft-AAD Application Proxy Connector event 12027
* Network traces contain the following signature similar to the following:
	+ 7281 24:44 (644) 10.11.2.12 .contoso.com KerberosV5 KerberosV5:TGS Request Realm: CONTOSO.COM Sname: http/xxxxx-xxx.contoso.com
	+ 7282 7290 (0) . CONTOSO.COM




#### Tags:
[[Windows]] [[Microsoft]] [[Bleeping Computer]]
