# Microsoft shares guidance on securing Windows 365 Cloud PCs
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-shares-guidance-on-securing-windows-365-cloud-pcs/)
+ Date: August 22, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft shares guidance on securing Windows 365 Cloud PCs](https://www.bleepstatic.com/content/hl-images/2021/08/19/Windows_365.jpg)


Earlier this week, Microsoft has shared guidance on securing Windows 365 Cloud PCs and more info on their built-in security capabilities.


The guidance is broken down into actions customers can take to secure Cloud PCs enrolled in Windows 365 Business and Windows 365 Enterprise subscription plans.


"All Cloud PCs, like their physical PC counterparts, come with Microsoft Defender—securing the device beginning with the first-run experience," [said](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/securing-your-windows-365-cloud-pcs/ba-p/2663129) Christiaan Brinkhoff, Principal Program Manager for Windows 365.


"Cloud PCs are also provisioned using a gallery image that is automatically updated with the latest cumulative updates for Windows 10 through Windows Update for Business."


Securing Windows 365 Cloud PCs
------------------------------


In the case of small businesses that choose Windows 365 Business, where end users are automatically granted local admin rights, IT admins are advised to follow standard IT security practices to set each user as standard users on their devices using Microsoft Endpoint Manager.


This process requires you to go through the following steps:


* Configure the devices to enroll into Microsoft Endpoint Manager using [automatic enrollment](https://docs.microsoft.com/mem/intune/enrollment/quickstart-setup-auto-enrollment).
* Manage the Local Administrators group. For more details on how to do this using Azure Active Directory (Azure AD, see [How to manage the local administrators group on Azure AD joined devices](https://docs.microsoft.com/azure/active-directory/devices/assign-local-admin). For an example of how to do this using Microsoft Endpoint Manager, see [this post](https://www.petervanderwoude.nl/post/easier-managing-local-administrators-via-windows-10-mdm-on-windows-10-20h2-and-later/) from Microsoft MVP Peter van der Woude.
* Consider enabling Microsoft Defender Attack surface reduction (ASR) rules. ASR rules are in-depth defense mitigations for specific security concerns, such as blocking credential stealing from the Windows local security authority subsystem. For details on how to enable ASR rules, see [Enable attack surface reduction rules](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/enable-attack-surface-reduction).


IT managers who need to secure Windows 365 Enterprise Cloud PCs have an easier task as they're all enrolled in Microsoft Endpoint Manager out of the box.


They also come with reporting of Microsoft Defender Antivirus alerts and optional onboarding into Microsoft Defender for Endpoint capabilities.


End-users of Windows 365 Enterprise PCs are also automatically set up as standard users by default, with admins being provided with the ability to make per-user exceptions if needed.


To further secure their cloud PCs, Microsoft advises Windows 365 Enterprise customers to:


* Follow standard Windows 10 security practices, including limiting who can log on to their Cloud PCs using local administrator privileges.
* Deploy the Windows 365 security baseline to their Cloud PCs from Microsoft Endpoint Manager and leverage Microsoft Defender to provide in-depth defense to their endpoints, including all Cloud PCs. The Windows 365 security baseline enables the ASR rules discussed above.
* Deploy Azure AD conditional access to secure authentication to their Cloud PCs, including multifactor authentication (MFA) and user/sign-in risk mitigation.


The virtualized Windows 365 service is streaming Cloud PCs from Azure which bundles trusted launch (tech that boosts VM's security by toggling on secure boot and TPM 2.0).


However, Windows 365 is not yet leveraging it to secure customers' Cloud PCs. Redmond plans to bring it together with Windows 11 later this year to all Azure regions where Windows 365 is available.


Windows 365 security mishaps
----------------------------


While Microsoft's Windows 365 service running on top of Azure Virtual Desktop [has just reached general availability](https://www.bleepingcomputer.com/news/microsoft/microsofts-windows-365-cloud-pc-service-is-live-costs-from-24-to-162/) on August 2, security researchers have already found security vulnerabilities exposing customers' networks to attacks.


To have an idea of the popularity of Microsoft's Cloud PCs, [the company quickly ran out of free trials](https://www.bleepingcomputer.com/news/microsoft/microsoft-halts-windows-365-trials-after-running-out-of-servers/) as people rushed to get a free virtual PC for two months.


[Mimikatz creator Benjamin Delpy](https://twitter.com/gentilkiwi) told BleepingComputer last week that he found a way to [dump a logged-in user's plaintext Microsoft Azure credentials](https://www.bleepingcomputer.com/news/microsoft/windows-365-exposes-microsoft-azure-credentials-in-plaintext/) on Microsoft's new Windows 365 Cloud PC service with the help of [Mimikatz](https://github.com/gentilkiwi/mimikatz/wiki).


While attackers would need Administrator permissions and know your Azure account credentials for this to work, this can quickly be done using a combination of phishing, a remote access program deployed on the targeted Cloud PC, and the exploitation of a privilege escalation bug such as PrintNightmare.


Once the attacker gets their hands on your Windows 365 credentials, they can move laterally through other Microsoft services and, potentially, to a corporate network.


Delpy recommends using 2FA, smart cards, Windows Hello, and [Windows Defender Remote Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/remote-credential-guard) to protect against such attacks.


However, unfortunately, Microsoft has not yet made these security features available in Windows 365.




#### Tags:
[[Windows]] [[Microsoft]] [[Cloud]] [[PCs]] [[PCs,]] [[ASR]] [[Bleeping Computer]]
