# Registry Explorer is the registry editor every Windows user needs
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/registry-explorer-is-the-registry-editor-every-windows-user-needs/)
+ Date: August 1, 2021
+ Author: Lawrence Abrams


## Article:
![Registry Explorer header image](https://www.bleepstatic.com/content/posts/2021/07/registry-explorer-header.jpg)


Last week, a new open-source Registry Editor was released that puts Windows Regedit software to shame by supporting a host of advanced features, making editing the Registry easier than ever.


The [Windows Registry](https://www.bleepingcomputer.com/tutorials/demystifying-the-windows-registry/) is a centralized, hierarchical database used by the operating system to store system settings, hardware configurations, and user preferences. 



If you are a Windows administrator or power user, then you have likely made changes to the Registry at one point using Windows built-in Registry Editor (regedit.exe) to fix a bug or tweak a configuration setting.


However, Microsoft has not made many changes to the Registry Editor over the years to modernize the application, and many useful features are missing that people may want.


Enter Registry Explorer
-----------------------


Last weekend, Windows Internals expert [Pavel Yosifovich](https://twitter.com/zodiacon) released a program called Registry Explorer that aims to modernize the registry editor with a slew of new features.


Registry Explorer was released as an open-source project [on GitHub](https://github.com/zodiacon/RegExp). Still, for those who do not want to compile the program, Yosifovich has also released a [precompiled beta version](https://github.com/zodiacon/RegExp/releases/tag/v0.7) that can be downloaded and launched immediately.


After running Registry Explorer, you will be greeted with a view of all the Registry hives, which users can expand to see their subkeys and values just like the standard Windows Registry editor.



![Registry Explorer](https://www.bleepstatic.com/images/news/software/r/registry-explorer/registry-explorer.jpg)**Registry Explorer**
However, where the program shines is an included dark mode, the ability to copy and paste keys and values to different locations, an undo changes button, and an advanced search feature.


Registry Explorer's search feature is far more advanced than regedit's as it allows you to find and display all search results in a single dialog box, as shown below. You can then look through the search results and double-click an entry to open that Registry key or value automatically.



![Registry Explorer showing all the Registry search results in one window](https://www.bleepstatic.com/images/news/software/r/registry-explorer/registry-search.jpg)**Registry Explorer showing all the Registry search results in one window**
Making the wrong change to the Registry could cause Windows not to operate correctly, Registry Explorer starts in a 'Read Only Mode' that prevents you from making changes until the mode is turned off.


A full list of features in Registry Explorer are listed below:


* Show real Registry (not just the standard one)
* Sort list view by any column
* Key icons for hives, inaccessible keys, and links
* Key details: last write time and number of keys/values
* Displays MUI and REG\_EXPAND\_SZ expanded values
* Full search (Find All / Ctrl+Shift+F)
* Enhanced hex editor for binary values
* Undo/redo
* Copy/paste of keys/values


Even better, if you find you really like Registry Explorer, you can configure it to automatically replace the Windows Registry editor and be the default file handler for .reg file.


If you find yourself constantly editing the Windows Registry, searching for values, or exporting your configuration to .reg files, then I strongly suggest you give Registry Explorer a try as you will likely find many of the features very useful.


To try Registry Explorer, you can visit the [project's GitHub page](https://github.com/zodiacon/RegExp).




#### Tags:
[[Windows]] [[Explorer,]] [[Bleeping Computer]]
