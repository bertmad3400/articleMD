# Windows Terminal now lets you drag and drop folders to open tabs
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-terminal-now-lets-you-drag-and-drop-folders-to-open-tabs/)
+ Date: September 1, 2021
+ Author: Lawrence Abrams


## Article:
![Windows Terminal](https://www.bleepstatic.com/content/hl-images/2020/09/22/windows-terminal-menu.jpg)


Microsoft released Windows Terminal Preview v1.11 yesterday, and comes numerous improvements and features, including the ability to open a Terminal window by dropping a folder on the new tab button.


Windows Terminal is one of my favorite features to come to Windows 10 over the past few years as it provides a multi-tabbed console window that you can use for PowerShell, WSL, and Command Prompt consoles.


When using Windows Terminal, you can open multiple console tabs simultaneously with a mix of different shells, depending on your needs and the applications installed.


Windows Terminal is now a built-in application in Windows 10 and can be added as the default console program when right-clicking on a folder.


Even better, [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal-preview/9n8g5rfz9xk3?rtc=1&activetab=pivot:overviewtab) is [open source](https://github.com/microsoft/terminal/), allowing developers outside of Microsoft to contribute new features and fixes.


Windows Terminal Preview v1.11
------------------------------


Windows Terminal Preview v1.11 includes many fixes, but for us, one stands out - the new ability to drag and drop a folder on the new tab button to open a console directly to that folder.



![New Windows Terminal drag and drop feature](https://www.bleepstatic.com/images/news/Microsoft/w/windows-terminal/v1.11/windows-terminal-drag-and-drop.gif)**New Windows Terminal drag and drop feature**
This feature is still a little buggy as if you have increased text scaling in Windows 10, the hot spot to drop a folder will not be directly over the new tab button.


Other highlighted changes in this release are listed below:


* You can now delete autogenerated profiles.
* Terminal will now optionally present a tray icon and minimize windows to it.
* You can now set special font features and custom axis values!
* Bold or "intense" text can now be displayed as bright colors, a bold font, or both.
* There is a new "Split Tab" item in each tab's context menu, which will split the active profile.
* Terminal now supports displaying the titlebar¹ or tab row with the acrylic material.
* There's a new "unfocused appearance" editor at the bottom of the Appearance page (per profile).
* Key bindings now support the browser keys found on some keyboards newer than, say, 2000?
* You can now open a new tab by dropping a folder on the + button.
* Those of you with international keyboards can now specify very particular key bindings to "virtual key" codes or scancodes.
* On newer versions of Windows, startingDirectory can now accept Linux paths when launching a WSL profile.
* Tabs created with wt and default terminal instances will now have the launched command line as their title, instead of the default profile name.
* You can now navigate through panes in creation order using `nextPane` and `previousPane`.
* Navigating through panes with the move-focus action works much better and now also works correctly on startup.
* The toggleSplitOrientation action has been added and it switches a pair of panes from a vertical to a horizontal layout.
* The taskbar will now show the progress state of all of the panes/tabs combined, regardless of which is in focus. This is helpful if you’re running a build in an unfocused tab, for example.
* You can now use sc() and vk() for binding keys, which allows many more keys to be bindable.


You can find more detailed information about the bug fixes and changes in the [Windows Terminal Preview 1.11 Release notes](https://devblogs.microsoft.com/commandline/windows-terminal-preview-1-11-release/) and on the [project's GitHub releases page](https://github.com/microsoft/terminal/releases).




#### Tags:
[[Windows]] [[v1.11]] [[button.]] [[Bleeping Computer]]