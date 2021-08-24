# SteelSeries bug gives Windows 10 admin rights by plugging in a device
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/steelseries-bug-gives-windows-10-admin-rights-by-plugging-in-a-device/)
+ Date: August 24, 2021
+ Author: Ionut Ilascu


## Article:
![SteelSeries bug gives Windows 10 admin rights by plugging in a device](https://www.bleepstatic.com/content/posts/2021/08/24/SteelSeriesKeyboard.jpg)


The official app for installing SteelSeries devices on Windows 10 can be exploited to obtain administrator rights, a security researcher has found.


Leveraging the bug is possible during the device setup process, using a link in the License Agreement screen that is opened with SYSTEM privileges. A real SteelSeries device is not necessary to exploit the bug.


### Emulating a device also works


The discovery comes after [news broke](https://www.bleepingcomputer.com/news/security/razer-bug-lets-you-become-a-windows-10-admin-by-plugging-in-a-mouse/) over the weekend that the Razer Synapse software can be used to gain elevated privileges when connecting a Razer mouse or keyboard.


Encouraged by the research from [jonhat](https://twitter.com/j0nh4t), offensive security researcher [Lawrence Amer](https://twitter.com/zux0x3a/) (research team leader at [0xsp](http://0xsp.com/)) found that the same can be achieved with the SteelSeries device installation software.


Playing with a recently acquired SteelSeries keyboard on Monday, the researcher discovered a privilege escalation vulnerability that allowed him to run the Command Prompt in Windows 10 with admin privileges.


The SteelSeries software is not just for keyboards (Apex 7/Pro), though. It also installs and allows configuring mice (Rival 650/600/710) and headsets (Arctis 9, Pro) from the maker; it even lets users control the RGB lighting on the QCK Prism gaming mousepad.


[Amer](https://twitter.com/zux0x3a/) started by plugging in his keyboard and monitoring the installation process, which started with downloading the SteelSeries software (SteelSeriesGG6.2.0Setup.exe) to the Windows temporary folder.


A real SteelSeries device is not necessary for this attack to work. Penetration testing researcher István Tóth published an [open-source script](https://github.com/tothi/usbgadget-tool) that can mimic human interface devices (HID) on an Android phone, specifically for testing local privilege escalation (LPE) scenarios.


![USB Gadget Generator Tool](https://www.bleepstatic.com/images/news/u/1100723/2021/Vulnerabilities/USB_Gadget.png)


Although an experimental version, the script can successfully emulate both Razer and SteelSeries devices.


After Amer published his research, Tóth [published a video](https://twitter.com/an0n_r0/status/1430010974073987081) demonstrating that LPE discovered by Amer can be achieved using his USB Gadget Generator Tool.



 


### Finding the right context


In trying to find a weak spot, Amer poked around trying to find a way to load a missing DLL or EXE from folders accessible to unprivileged users but did not find any.


However, he noticed that the device setup app was launched with SYSTEM rights immediately after downloading it. Another process running with the highest privileges provided a new opportunity for attack.



![SteelSeries software running with SYSTEM privileges](https://www.bleepstatic.com/images/news/u/1100723/2021/Vulnerabilities/SteelSeriesSYS.jpg)source: [Lawrence Amer](http://0xsp.com/security%20research%20&%20development%20(SRD)/local-administrator-is-not-just-with-razer-it-is-possible-for-all)
Amer tried the same method that worked for the Razer zero-day vulnerability, but it did not work because the installation carries on without user interaction.


The researcher caught a lucky break when the License Agreement appeared with a link to SteelSeries’ privacy policy. When clicking on the link, the dialog for choosing a launching app appeared.


Amer tested the scenario in a virtual machine that did not have file associations defined. The only process available for opening the link was Internet Explorer, which spawned as SYSTEM.


From there, it was a simple matter of using IE to save the web page and launch an elevated privileges Command Prompt from the right-click menu of the “Save As” dialog.



![Launching Command Prompt with SYSTEM authority](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)source: [Lawrence Amer](http://0xsp.com/security%20research%20&%20development%20(SRD)/local-administrator-is-not-just-with-razer-it-is-possible-for-all)
Amer told BleepingComputer that he tried informing SteelSeries about the vulnerability but could not find a public bug bounty program or a contact for product security.


BleepingComputer reached out to SteelSeries about this but did not hear back by publishing time.


The researcher says that the vulnerability could still be exploited even after patching it. An attacker could save the vulnerable signed executable dropped in the temporary folder when plugging in a SteelSeries device and serve it in a DNS poisoning attack.




#### Tags:
[[SteelSeries]] [[Amer]] [[Windows]] [[Bleeping Computer]]
