# Windows admins now can block external devices via layered Group Policy
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-admins-now-can-block-external-devices-via-layered-group-policy/)
+ Date: August 4, 2021
+ Author: Sergiu Gatlan


## Article:
![Windows admins now can block external devices via layered Group Policy](https://www.bleepstatic.com/content/hl-images/2021/05/12/Windows_10.jpg)


Microsoft has added support for layered Group Policies, which allow IT admins to control what internal or external devices users can be installed on corporate endpoints across their organization's network.


Devices that can be blocked or allowed to install on endpoints include printers, USB storage drives, and other USB peripherals added to a given organization's prohibited or approved list of devices.


Benefits of controlling device installation with the help of group policies include reducing support costs and decreasing the risk of corporate data theft.


All devices come with their own set of "device identifiers" understood by the system (e.g., class, device ID, and instance ID).


Using these identifiers, an admin can create an 'allow list' of allowed devices that will block all other devices from being installed.


The new apply layered Group Policy feature provides more granular control over what devices are blocked from installation using a set of device identifiers such as instance IDs, hardware IDs, setup class, and removable device property.



![Device installation flowchart](https://www.bleepstatic.com/images/news/u/1109292/2021/device-installation-flowchart-1.png)*Image: Microsoft*
Per Microsoft, using the apply layered Group Policy with already existing device installation policies improves flexibility and intuitive usage:


* Intuitive usage: the new policy allows you to make sure that only device classes on the prohibited list are blocked from installation
* Flexibility: the new policy introduces hierarchical layering using the Device instance IDs > Device IDs > Device setup class > Removable devices order, which overrides conflicting prevent and allow policy settings.


If you want to apply right now in your environment, the path to the new Group Policy is Computer Configuration > Administrative Templates > System > Device Installation > Device Installation Restrictions > 'Apply layered order of evaluation for Allow and Prevent device installation policies across all device match criteria'.



![Layered group policy](https://www.bleepstatic.com/images/news/u/1109292/2021/Layered%20group%20policy.png)*Image: Microsoft*
"Applying layered Group Policy is available on all Windows 10 systems where as part of the July 2021 optional 'C' client release, and will be made more broadly available beginning in the August 2021 Update Tuesday release," Microsoft [said](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/introducing-the-ability-to-apply-layered-group-policy/ba-p/2608462).


"The Windows Server release will follow thereafter. This feature will also be supported in Windows 11."


Additional information on the "Apply layered order of evaluation for Allow and Prevent device installation policies across all device match criteria" policy setting is available on the [Microsoft 365 docs website](https://docs.microsoft.com/en-us/windows/client-management/manage-device-installation-with-group-policy#apply-layered-order-of-evaluation-for-allow-and-prevent-device-installation-policies-across-all-device-match-criteria).




#### Tags:
[[Microsoft]] [[Windows]] [[Bleeping Computer]]
