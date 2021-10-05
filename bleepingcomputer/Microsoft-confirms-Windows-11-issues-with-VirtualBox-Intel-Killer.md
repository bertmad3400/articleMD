# Microsoft confirms Windows 11 issues with VirtualBox, Intel Killer
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-11-issues-with-virtualbox-intel-killer/)
+ Date: October 5, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft confirms Windows 11 issues with VirtualBox, Intel Killer](https://www.bleepstatic.com/content/hl-images/2021/09/01/Windows_11_headpic.jpg)


Right after officially releasing Windows 11, Microsoft has added three know issues to the Windows 11 12H2 release health dashboard.


Microsoft has [released Windows 11 worldwide yesterday](https://www.bleepingcomputer.com/news/microsoft/windows-11-is-released-what-you-need-to-know-and-new-features/) and is now rolling it out via Windows Update to new Windows 10 devices and those pre-loaded with Windows 11.


Windows 10 users can now upgrade to Windows 11 via Windows Update as long as their computers come with [compatible hardware](https://www.bleepingcomputer.com/news/microsoft/microsoft-publishes-the-windows-11-system-requirements/). Devices also need to run Windows 10 2004 and later and have installed at least the September 2021 updates.


Windows 11 incompatible with Oracle VirtualBox VMs
--------------------------------------------------


The company [confirmed](https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2#1704msgdesc) previous reports that the latest Windows version has [compatibility issues with the Oracle VirtualBox virtualization software](https://www.bleepingcomputer.com/news/microsoft/windows-11-is-no-longer-compatible-with-oracle-virtualbox-vms/) where customers might be unable to start their Virtual machines (VMs) and might receive an error.


"Microsoft and Oracle have found a compatibility issue between VirtualBox and Windows 11, when Hyper-V or Windows Hypervisor is installed," Redmond explained.


Microsoft has applied a compatibility hold to safeguard the users' experience, blocking impacted devices from being offered or installing Windows 11.


Customers who try to update affected systems will receive the "VirtualBox. Your PC requires the latest version of this app. Click Learn More for more information on how to update this app." message.


Oracle is currently working on resolving this known issue with an estimated release date for a compatible VirtualBox version later this month.


While Oracle is fixing the issue, Microsoft has provided a workaround to enable impacted customers to mitigate the safeguard hold.


"You will need to remove Hyper-V or Windows Hypervisor until this issue is resolved with an update Oracle plans to release in October 2021," the company said.


"You can check Oracle's progress by monitoring their ticket #20536. If you are no longer using VirtualBox, uninstalling it should also mitigate the safeguard. Please note, if there are no other safeguards that affect your device, it can take up to 48 hours before the upgrade to Windows 11 is offered."


Intel 'Killer' networking software and Cốc Cốc browser issues
-------------------------------------------------------------


Microsoft has also found Windows 11 compatibility issues with the Intel "Killer" networking software and the Cốc Cốc browser.


The [incompatible Intel networking software](https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2#1699msgdesc) can lead to slower streaming and site loading due to User Datagram Protocol (UDP) performance issues caused by dropped UDP packets under certain conditions.


Cốc Cốc browser users [might also be unable to open sites](https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2#1698msgdesc) and encounter other issues or errors on some affected Windows 11 devices.


Microsoft has applied an additional compatibility hold on devices running Cốc Cốc browser to prevent Windows 11 upgrades that could degrade the user experience.


Microsoft is currently investigating and working on finding a solution for these Windows 11 known issues, with an update addressing them to be released with the October Patch Tuesday.


For all these issues, Redmond recommends that you not attempt to manually upgrade via the *Update now* button or use the Media Creation Tool until a fix is available.




#### Tags:
[[Windows]] [[Cốc]] [[Microsoft]] [[VirtualBox]] [[Bleeping Computer]]
