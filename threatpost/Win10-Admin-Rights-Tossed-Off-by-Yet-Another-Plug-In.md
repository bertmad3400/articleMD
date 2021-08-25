# Win10 Admin Rights Tossed Off by Yet Another Plug-In
### Then again, you don’t even need the actual device – in this case, a SteelSeries peripheral – since emulation works just fine to launch with full SYSTEM rights. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168927)
+ Date: August 25, 2021  2:23 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/25141841/steel-series-e1629915533369.jpeg)
It’s not just Razer’s mice and keyboards that [gobble up Windows 10’s](https://threatpost.com/windows-10-admin-rights-razer-devices-mouse-peripherals/168855/) tip-top, admin-level SYSTEM privileges: A SteelSeries bug also tosses off Windows 10 admin rights if you just plug in a device.


… Or, then again, you can save yourself some cash by simply tricking an Android phone into thinking a local privilege-escalation (LPE) testing script is a real human.


… Or, at least, it did work, until [SteelSeries](https://steelseries.com/) – a Danish manufacturer of gaming peripherals and accessories such as headsets, keyboards, mice, controllers and mousepads – patched the bug. The bug could be leveraged during the device setup process, by using a link in the License Agreement screen that opened with SYSTEM privileges.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


[0xsp](http://0xsp.com/) research team leader [Lawrence Amer](https://twitter.com/zux0x3a) published the bug on Monday, and [BleepingComputer](https://www.bleepingcomputer.com/news/security/steelseries-bug-gives-windows-10-admin-rights-by-plugging-in-a-device/) reported about it on Tuesday. SteelSeries later responded, telling the outlet that the company was aware of the issue and that it had removed the risk of exploitation by preventing the installation software from launching on plugging in a SteelSeries device.



> 
> it is not only about [@Razer](https://twitter.com/Razer?ref_src=twsrc%5Etfw).. it is possible for all.. just another priv\_escalation with [@SteelSeries](https://twitter.com/SteelSeries?ref_src=twsrc%5Etfw) <https://t.co/S2sIa1Lvjv> [pic.twitter.com/E3NPQnxqo2](https://t.co/E3NPQnxqo2)
> 
> 
> — Lawrence 勞倫斯 (@zux0x3a) [August 23, 2021](https://twitter.com/zux0x3a/status/1429841541036527616?ref_src=twsrc%5Etfw)
> 
> 



The statement it sent to BleepingComputer: “We are aware of the issue identified and have proactively disabled the launch of the SteelSeries installer that is triggered when a new SteelSeries device is plugged in. This immediately removes the opportunity for an exploit and we are working on a software update that will address the issue permanently and be released soon.”


Or Will It?
-----------


Amer, the researcher who discovered the bug, questions the company’s assertion that its patch will fix the problem, which is that you can get full admin privileges on Windows 10 just by plugging in (or by mimicking plugin of) a SteelSeries device.


Amer told BleepingComputer that SteelSeries’ patch wouldn’t work and that the vulnerability could still be exploited even after patching, given that an attacker could “save the vulnerable signed executable dropped in the temporary folder when plugging in a SteelSeries device and serve it in a DNS poisoning attack,” as the publication reported.


DNS poisoning, aka DNS spoofing or DNS cache poisoning, entails introducing corrupt Domain Name System data into the DNS resolver’s cache, causing the name server to return an incorrect result record, such as an IP address.


Security is a dynamic, ever-changing thing, as ongoing research on this bug makes clear. Early on Wednesday, Amer [told BleepingCo](https://twitter.com/BleepinComputer/status/1430454633491832833)mputer that yes, SteelSeries’ patch would work. Then, when Threatpost reached out to Amer late Thursday morning East Coast time to confirm his findings, the researcher told us he’s still trying to figure out whether it will or won’t work.



> 
> We received confirmation from [@zux0x3a](https://twitter.com/zux0x3a?ref_src=twsrc%5Etfw), the researcher that found the bug, that the solution from SteelSeries works
> 
> 
> — BleepingComputer (@BleepinComputer) [August 25, 2021](https://twitter.com/BleepinComputer/status/1430454633491832833?ref_src=twsrc%5Etfw)
> 
> 



“I am still trying to reproduce the dns poisoning in order to serve the same executable, i am not sure the main reason stopped me from doing that but i think it is due to steelseries has revoked the whole installation, as I mentioned there fix is temporary until they pushed an update to fix installer package,” Amer told Threatpost in a Twitter conversation. “from there i think we can do signed exe poisoning. … Doing hijacking for software updates is something possible but for now I can’t fully confirm as they have removed … the complete installer.”


SteelSeries hadn’t responded to Threatpost’s request for comment by the time this story posted.


Revolt of the USB Gadgets
-------------------------


This pair of Windows 10 takeovers via USB plug-in gadgets – Razer’s and SteelSeries’ – was kicked off over the weekend. News emerged that a zero-day bug in the device installer software for Razer peripherals – be they a Razer mouse, keyboard or any device that uses the company’s Synapse utility – gives the plugger-inner full admin rights on Windows 10, just by inserting a compatible peripheral and downloading Synapse. Razer’s Synapse software enables users to configure hardware devices, set up macros or map buttons.


Researchers’ interest was understandably piqued by the question of whether the bug would work with other devices to pull off LPE. Initial research by jonhat, the researcher who found the Razer bug, led to suggestions that the vulnerability wasn’t necessarily confined to just Razer peripherals. One commenter, @Lechatquirit, claimed that the attack also works “with any asus ROG mouse. It will prompt to install armory [sic] crate and execute it as Sys,” the user [tweeted](https://twitter.com/Lechatquirit/status/1429374730860208128) in response to jonhat. [Armoury Crate](https://www.asus.com/support/FAQ/1042459/) is a software portal that displays real-time performance and settings information for connected devices and which works with ROG, TUF Gaming and ASUS products.


As Amer’s research went on to show, the LPE will work with yet more plug-in USB devices, though the exploit takes on a different flavor. As mentioned, Amer found that you can get full admin privileges on Windows 10 just by plugging in (or by mimicking plugin) a SteelSeries device, which triggers its device installation software.


On Monday, Amer plugged in a SteelSeries keyboard and discovered an LPE vulnerability that allowed him to run the Command Prompt in Windows 10 with admin privileges, similar to how jonhat found that when could plug in a Razer device (or dongle, if it’s a wireless peripheral), Windows automatically fetches an installer containing driver software and the Razer Synapse utility. The plug-and-play Razer Synapse installation then allows users to gain SYSTEM privileges on the Windows device lickety-split, since, as part of the setup routine, it opens an Explorer window that prompts the user to specify where the driver should be installed.


Since the RazerInstaller.exe executable was launched via a Windows process running with SYSTEM privileges, the Razer installation program inherited those same Admin privileges. jonhat found that if a user opts to change the default location of the installation folder, it triggers a “Choose a folder” dialog. At that point, you can right-click the installation window and press the Shift key, which opens a PowerShell terminal with those same elevated privileges.


When Amer plugged in his SteelSeries keyboard, he saw that the installation process started with downloading the SteelSeries software (SteelSeriesGG6.2.0Setup.exe) to the Windows temporary folder.


But as BleepingComputer pointed out, you don’t need an actual SteelSeries device to pull this off, given that penetration testing researcher István Tóth “published an [open-source script](https://github.com/tothi/usbgadget-tool) that can mimic human interface devices (HID) on an Android phone, specifically for testing local privilege escalation (LPE) scenarios.”


That gadget, dubbed the USB Gadget Generator tool, can emulate either Razer or SteelSeries devices.


Amer published his research on Monday. As you can see in the video below, the method that worked with the Razer zero-day flaw didn’t work with SteelSeries, given that its installation doesn’t require user interaction. What did work to hijack privileges with SteelSeries: a link to the company’s privacy policy that appeared along with the license agreement. Amer clicked the link and found that the dialog for choosing a launching app appeared.


The researcher used Internet Explorer to open the link – the only available way to open it on his virtual machine. IE spawned the app with SYSTEM privileges, after which Amer used IE to save the web page. He then launched an elevated privileges Command Prompt by right-clicking and choosing the “Save As” dialog.


Amer told BleepingComputer that he tried to disclose the bug to SteelSeries but said that he couldn’t find a public bug bounty program or a contact for product security. … again, similar to what happened when jonhat initially didn’t hear back from Razer and went ahead and published his proof of concept video.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[SteelSeries]] [[Amer]] [[Windows]] [[BleepingComputer]] [[DNS]] [[USB]] [[Razer’s]] [[device.]] [[privileges.]] [[bug,]] [[ThreatPost]]
