# Missing Microsoft Intune certs break email, VPN on Samsung devices
### Microsoft says Samsung devices enrolled in Microsoft Intune using a work profile will experience email and VPN connectivity issues due to missing certificates after upgrading to Android 12.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/missing-microsoft-intune-certs-break-email-vpn-on-samsung-devices/
+ Date: 2022-01-25T09:15:00-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/11/12/Microsoft_Intune_headpic.jpg)

![Missing Microsoft Intune certs break email, VPN on Samsung devices](https://www.bleepstatic.com/content/hl-images/2021/11/12/Microsoft_Intune_headpic.jpg)


Microsoft says Samsung devices enrolled in Microsoft Intune using a work profile will experience email and VPN connectivity issues due to missing certificates after upgrading to Android 12.


[Microsoft Intune](https://docs.microsoft.com/en-us/mem/intune/fundamentals/what-is-intune) is a cloud-based service designed to help admins manage Windows, macOS, iOS/iPadOS, and Android apps and devices in enterprise environments.


It also enforces device-specific policies when accessing proprietary data from company-owned or personal devices.


Gmail, Outlook, and VPN issues
------------------------------


"Microsoft Intune was recently alerted to an issue for Samsung devices enrolled with a work profile that, after updating to Android 12, some email and VPN applications are losing access to certificates when the user tries to access them (such as Gmail and AnyConnect VPN)," the Intune Support Team says.


"The missing certificates prevent users from being able to access their email on Gmail and VPN apps."


According to Microsoft, those attempting to use the AnyConnect VPN app will see prompts suggesting that the client certificate the app needs to make a connection to its servers could not be found, and another valid certificate should be chosen instead.


The Gmail app will also prompt users of affected Samsung devices to select a certificate when accessing Gmail and then display a "Can’t reach server" error after selecting the appropriate certificate. 


Customers have also reported experiencing issues accessing their Outlook email because the SMIME certificate deployed with Microsoft Endpoint Manager disappears from Outlook's SMIME settings after the Android 12 upgrade.


Available workarounds
---------------------


While Microsoft is still working with Samsung to address these issues, users can work around these issues by clearing the app data cache for impacted VPN apps.


Gmail can be revived by users removing and reinstalling the work profile and Company Portal on each device or by IT admins removing and re-adding the Gmail device configuration.


According to other customers' reports, Outlook users can also temporarily fix this by removing and reinstalling the application.


AnyConnect VPN and Gmail users can find detailed workaround instructions in [Intune Support Team's Tech Community blog post](http://techcommunity.microsoft.com/t5/intune-customer-success/known-issue-missing-certificates-after-updating-samsung-work/ba-p/3039834).


"We are working closely with Samsung to resolve this issue but wanted to share temporary workarounds to help users access their VPN apps," Microsoft added.


Redmond is also [investigating another Microsoft Intune bug](https://techcommunity.microsoft.com/t5/intune-customer-success/known-issue-samsung-devices-are-noncompliant-after-restart-or/ba-p/2952544) that forces Android Enterprise fully managed Samsung Galaxy devices into non-compliant states after automatic restarts or installing managed updates.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=njRAT]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Vpn]] [[Gmail]] [[Samsung]] [[Android]] [[Apps]] [[Anyconnect]] [[Bleeping Computer]]

