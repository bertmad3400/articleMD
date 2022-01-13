# Windows 11 setup: Which user account type should you choose? | ZDNet
### When you set up a new PC running Windows 10 or Windows 11, you have a choice of four types of user accounts, from the old-school local account to the newest, Azure Active Directory. Here's how to make the right choice.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/windows-10-which-user-account-type-should-you-choose/
+ Date: 2022-01-13 14:49:00
+ Author: Ed Bott


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/72a7646df0ee7447997ed7fbe666470068e0d5f5/2019/07/22/938be27d-d095-40ab-b007-26979ee3c075/which-windows-account.jpg?width=770&height=578&fit=crop&auto=webp)

When you set up a Windows PC for the first time, you're required to create a user account that will serve as the administrator for the device. Depending on your Windows edition and network setup, you have a choice of up to four separate account types.

On business editions (Pro, Pro for Workstations, Enterprise, and Education), the Windows Setup program asks you to choose whether you want to set the PC up for personal use or for use on a network managed by your organization, as shown below. If you choose the second option, you can set up the PC using an account in your Windows Active Directory domain or you can sign in using an Azure Active Directory account, such as the one associated with an Office 365 Business or Enterprise subscription.

![user-account-personal-or-organization.jpg]()![user-account-personal-or-organization.jpg](https://www.zdnet.com/a/img/resize/d9f40bfc48d5c5f6ad01dded53948d489de15a35/2019/07/23/5516990f-9ffb-4dae-a102-3fb533de31d9/user-account-personal-or-organization.jpg?fit=bounds&auto=webp)This choice is only available with Windows 10 Pro or Enterprise

On Windows 10 Home edition, that choice isn't available, and you're limited to only the personal options: a local account or a Microsoft account. The Setup program is extremely persistent about trying to coax you into signing in with a Microsoft account. Windows 11 Home edition gives you only the option for a Microsoft account, although can add a local account (or remove the connection to the Microsoft account) after you've signed in for the first time.

In this post, I'll explain the pros and cons of each account type and explain why your best option might be a combination of two account types.


* [Windows 11: Do these six things right away after you finish setup](https://www.zdnet.com/article/six-things-you-should-do-right-away-with-your-new-windows-11-pc/)

### Microsoft account

This is Microsoft's free online account for personal use, required for signing in to the company's consumer services, including OneDrive, Xbox Live, Skype, and Microsoft 365 (formerly Office 365) Family and Personal subscriptions, among others.

If you have an email account at Outlook.com or Hotmail.com (or, for old-timers, at live.com or msn.com), you already have a Microsoft account. You can also sign up for a new account anytime, choosing a new address at Outlook.com or using your own email address.

Signing in to your Windows 10 or Windows 11 PC with a Microsoft account offers several distinct benefits:

* On PCs designed for Windows 10 or Windows 11, signing in with a Microsoft account automatically enables [full-disk encryption for the system drive](https://support.microsoft.com/en-us/help/4502379/windows-10-device-encryption), even on systems running Home edition. If you turn on BitLocker encryption (Pro and Enterprise editions only), your recovery key is stored in OneDrive, allowing you to retrieve your data if you find yourself locked out.
* Signing in with a Microsoft account stores a record of your successful activation, allowing you to easily restore your activation (no product key required) if you ever have to reinstall Windows.
* Windows allows you to sync settings between PCs where you sign in using the same Microsoft account. That includes personalization settings like your desktop background, saved passwords (including Wi-Fi profiles), language and regional settings, and more. (For a full list, see ["Windows 10 roaming settings reference."](https://docs.microsoft.com/en-us/azure/active-directory/devices/enterprise-state-roaming-windows-settings-reference))
* You can sign in automatically to any Microsoft consumer service using your saved Microsoft Account credentials.
* You can sync data and settings for preinstalled Windows apps (Mail and Calendar, for example) and easily restore apps you download from the Store.






Note that Windows telemetry data is tied to your device and isn't associated with a Microsoft account.

And, of course, you can create a Microsoft account and use it exclusively for signing in to Windows while keeping your email, cloud storage, and other services elsewhere. But if you do use a Microsoft account for services such as Office 365 and OneDrive, it makes sense to sign in to Windows using the same account. 

### Local account

A local account is about as old school as Windows gets. You don't need a network connection or an email address; instead, you create a username (up to 20 characters) and a password, both of which are stored on the PC where you create them and grant access only to that device.

There's no particular security or privacy advantage to signing in with a local account (indeed the lack of device encryption is a negative, in my book); but if that's your preference, you can do so when you first set up Windows 10 (any edition) or Windows 11 Pro on a new PC.

Windows 11 Home requires you to sign in with a Microsoft account during initial setup. You can do so by creating a brand-new Microsoft account, and then, after signing in for the first time, go to Settings > Accounts > Your Info. Under the Account Settings heading, choose Sign In With A Local Account Instead and follow the prompts.

On Windows 10, when you reach the Sign In With Microsoft screen shown here, click the "Offline Account" option in the lower left corner; then click "No" on the Sign In With Microsoft Instead screen, which appears next.

![set-up-a-local-account.jpg]()![set-up-a-local-account.jpg](https://www.zdnet.com/a/img/resize/2aed5a10efe801270d1805605a9f5e86d75c1ac1/2019/07/23/40eed284-8369-468c-b6e6-3fe95c79872a/set-up-a-local-account.jpg?fit=bounds&auto=webp)That option in the lower left corner allows you to set up a local account

After you get past those speed bumps, you can enter your username and password. 

With a Microsoft account, you have multiple options to recover if you forget your password. With local accounts, you've historically had no such option if you forget your password. On Windows 10, setting up a local account on Windows 10 requires that you fill in answers to three security questions, to help you recover in the event you forget your password.

You can't bypass those questions, nor can you choose alternatives other than the six predefined questions. If you're worried that a thief with a search engine can guess those answers, do as I do and ... be creative. For example, you can answer the three security questions with a three-word passphrase of your own, entered one word at a time. Or, if you'd prefer to bypass the whole feature, just mash the keyboard to create random "answers" that no one (including you) could possibly guess. If you choose either option, don't blame me if you forget your password.

You can switch at will between a local account and a Microsoft account, using options in Settings > Accounts > Your Info.

Even if you prefer a local account, consider signing in first with a Microsoft account. After you confirm that your system is properly activated and the activation status is recorded with that Microsoft account, switch back to a local account and go on about your business.

Likewise, if you're fussy about the name of your default user profile folder, consider signing in with a local account first, and then attach your Microsoft account. If you follow that procedure, Windows uses the exact local username you specify as the folder name and retains that name when you switch; if you start with a Microsoft account, your user profile folder name is the first five characters of the portion of your email address to the left of the @ sign.

### Active Directory (domain join)

On an enterprise network with a Windows server running as a domain controller, you can join a Windows 10 ow Windows 11 PC to the domain. Creating that type of account requires that a domain administrator create an Active Directory account, after which you can sign in using the credentials in the format *domain\username* (or *username@domain*, if the domain is associated with a fully qualified domain name).

Ironically, before you can join a PC to a domain and sign in with your Active Directory account, you have to first create a local account.

### Azure Active Directory

This is the newest option in the lineup of Windows account types. Like a domain account, an Azure AD account is managed by an organization's administrator, but it doesn't require a local server. Instead, the credentials are managed in Microsoft's Azure cloud.

If your organization uses Microsoft 365 or has an Office 365 Business or Enterprise subscription, you have an Azure AD account. It behaves similarly to a Microsoft account, with the ability to sync settings across devices where you're signed in with the same account. The big difference is that your access to the device is managed by your organization's administrator, who can apply security settings and restrict some options.

To manage Azure AD accounts, administrators use the [Azure AD admin center](https://aad.portal.azure.com/), which also includes the option to synchronize the cloud-based directory with a local domain's Active Directory, an option called Azure AD Connect.

![azure-ad-porta.jpg]()![azure-ad-porta.jpg](https://www.zdnet.com/a/img/resize/e21e2a869dcd52e4b2755a63d57e0ad50c0cf63d/2019/07/23/b4fa3c2c-6807-4f8e-8d95-bd0130a12cc1/azure-ad-porta.jpg?width=1200&fit=bounds&auto=webp)Administrators can manage Azure AD from this portal

A basic Azure AD account is free, but like all Microsoft enterprise services, upsell options abound. Paying for Azure AD Premium (included with an Enterprise Mobility and Security E5 subscription) unlocks advanced security features.

And you can mix and match account types on the same device for the sake of flexibility. You might want a local account to handle routine administrative tasks, a Microsoft account for personal use, and an Azure AD account for connecting to your organization's servers. (To set up additional accounts after the first one, use Settings > Accounts > Family & Other Users > Add Someone Else To This PC). Just choose the right account when you first sign in to a new session.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=CALENDAR]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Education]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Windows]] [[(or]] [[Onedrive]] [[Username]] [[ZDNet]]

