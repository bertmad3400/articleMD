# Microsoft removes Window 11 hack to enable Windows 10 Start Menu
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-removes-window-11-hack-to-enable-windows-10-start-menu/)
+ Date: July 10, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 11](https://www.bleepstatic.com/content/hl-images/2021/06/24/Windows-11-start-menu.jpg)


 Microsoft removed a registry hack in the latest preview build that allowed Windows 11 users to revert to the "Classic" Windows 10 Start Menu.


When the Windows 11 preview build was leaked in June, one of the most significant and most controversial changes was a new floating Start Menu centered in the middle of the Taskbar.


This new Start Menu was taken from the now-shelved Windows 10X and includes a redesigned interface with the removal of app groups and Live Tiles.



![Windows 11 Start Menu](https://www.bleepstatic.com/images/news/Microsoft/windows-11/s/start-menu-classic/Windows-11-start-menu.jpg)**Windows 11 Start Menu**
For those who did not like the new Start Menu, it was possible to use a Registry hack to revert to a "Classic Mode," the Windows 10 Start Menu.


To switch to the Windows 10 Start Menu, users could create the '**Start\_ShowClassicMode**' value and set it to **1** under the **HKEY\_CURRENT\_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced** registry key.


Once you created the registry value and restarted the Windows Explorer process, the old Start Menu would be available again, as shown below.



![Windows 10 Start Menu in WIndows 11](https://www.bleepstatic.com/images/news/Microsoft/windows-11/s/start-menu-classic/classic-start-menu.jpg)**Windows 10 Start Menu in Windows 11**
On Thursday, [Microsoft released Windows 11 build 22000.65](https://www.bleepingcomputer.com/news/microsoft/new-windows-11-dev-build-released-with-bug-fixes-and-new-features/) to Insiders on the 'Dev' channel. Unfortunately, after installing the new cumulative update, users could no longer use the Registry hack to bring back the old Start Menu.




> 
> [@JenMsft](https://twitter.com/JenMsft?ref_src=twsrc%5Etfw) I've noticed that with 22000.65 the option to bring back the old start menu (Start\_ShowClassicMode) doesn't work anymore. Is there any minor chance at all that you guys revert that change so people who REALLY want it back, can use it?
> 
> 
> — Tourniquet  (@wenti\_man) [July 8, 2021](https://twitter.com/wenti_man/status/1413264402552442886?ref_src=twsrc%5Etfw)


BleepingComputer has also independently confirmed that the Registry hack no longer works, but it is unclear whether Microsoft will enable it again in the future.


BleepingComputer has reached out to Microsoft to learn more about this change but has not heard back at this time.


*Thx to Jacob for the tip.*




#### Tags:
[[Windows]] [[Microsoft]] [[Bleeping Computer]]
