# Microsoft Intune bug forces Samsung devices into non-compliant state
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-intune-bug-forces-samsung-devices-into-non-compliant-state/)
+ Date: November 12, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft Intune bug forces Samsung devices into non-compliant state](https://www.bleepstatic.com/content/hl-images/2021/11/12/Microsoft_Intune__headpic.jpg)


Microsoft says some Samsung Galaxy devices will be marked as non-compliant with the organization's security requirements in Microsoft Intune's management interface after automatic restarts or after installing managed updates.


[Microsoft Intune](https://docs.microsoft.com/en-us/mem/intune/fundamentals/what-is-intune) is a cloud service that allows admins to manage Windows, macOS, iOS/iPadOS, and Android applications and devices in their enterprise environment.


It also allows securing proprietary data accessed and shared by users from company-owned or personal devices by enforcing device-specific policies.


Impacts Samsung devices running Android 9 or later
--------------------------------------------------


"This could potentially affect access to corporate resources, depending on the Conditional Access policies set by the IT administrator," the Intune Support Team said.


Depending on how affected Samsung Galaxy devices are managed, the issue can impact a wide range of Android versions from Android 9 and up.


It can be encountered after automatic restarts scheduled from the Settings dialog on devices running Android 9 and later, with an Android Enterprise personally-owned work profile or enrolled using Android device administrator (DA), also known as "legacy" Android management.


On Android Enterprise fully managed Samsung devices running Android 11 or later, the known issue will trigger after completing a [managed update](https://docs.microsoft.com/mem/intune/fundamentals/manage-os-versions).


In both cases, the immediate result of the device being tagged as non-compliant is that users will likely be blocked from accessing corporate resources.


Workarounds available
---------------------


For both classes of devices, users can work around the issue by triggering a [device sync](https://docs.microsoft.com/mem/intune/user-help/sync-device-android) to restore access to blocked corporate resources.


The difference between Android (DA) managed devices and Android Enterprise fully managed devices is the method used to start the sync process.


For Android 9 or later, you will have to trigger the sync from the Company Portal, while for those running Android 11+ you need to do it from the Device Policy Controller app.


"We are working to resolve this issue with Samsung, but in the meantime, we wanted to give you more information and workaround instructions to help you bring devices back into compliance," Microsoft added.




#### Tags:
[[Android]] [[Microsoft]] [[Samsung]] [[later,]] [[Bleeping Computer]]
