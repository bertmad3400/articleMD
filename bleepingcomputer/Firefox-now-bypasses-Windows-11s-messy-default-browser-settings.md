# Firefox now bypasses Windows 11's messy default browser settings
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/firefox-now-bypasses-windows-11s-messy-default-browser-settings/)
+ Date: September 13, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 11](https://www.bleepstatic.com/content/hl-images/2021/09/01/windows-11-glow-glass.jpg)


Likely fed up with the new Windows 11 default apps interface, Mozilla has bypassed Microsoft's policies to make it easier for users to switch their default browser.


In the past, when a Windows application wanted to become the default program, it would programmatically make the change by modifying the Registry.


After some programs began hijacking default program settings without permission, Microsoft added restrictions in Windows 10 by requiring users to specifically choose their default programs.


Starting in Windows 10, when an application wanted to become the default program, it was required to programmatically launch the Default Apps settings screen and prompt the user to select the application they would like to use, as shown below.



![Windows 10 default apps settings screen](https://www.bleepstatic.com/images/news/web-browsers/firefox/91/windows-11-default-programs/windows-10-defualt-program.jpg)**Windows 10 default apps settings screen**  
*Source: BleepingComputer*
If a program hijacked the Registry entries without using this interface, Windows 10 would reset the settings to the Windows defaults and issue a warning.



![](https://www.bleepstatic.com/images/news/web-browsers/firefox/91/windows-11-default-programs/windows-10-warning.jpg)Warning about hijacked default browser settings  
*Source: [Microsoft](https://techcommunity.microsoft.com/t5/ask-the-performance-team/how-to-configure-file-associations-for-it-pros/ba-p/1313151)*
For the most part, this method has worked really well in Windows 10 as it prevents programs from hijacking settings and puts the user in control of their default programs.


Windows 11 turns default programs into a mess
---------------------------------------------


Unfortunately, this all changed with Windows 11 as Microsoft introduced a new and confusing interface for the Default apps settings that now require you to manually change the default program for every protocol and file type.


For example, if you wish to change your default browser, it's not as simple as just clicking on the 'Web browser' setting and selecting the browser of your choice.


Instead, you now have to search for each file extension (.html and .htm) and protocol (HTTP or HTTPS) and manually associate them to the program you wish to use, as shown below.



![New Windows 11 default apps settings screen](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**New Windows 11 default apps settings screen**  
*Source: BleepingComputer*
Instead of having their users wade through a series of annoying Windows 11 settings, Mozilla has reverse-engineered Window 11's default settings process to allow users to make Firefox the default browser with one click.


As [first reported](http://www.theverge.com/2021/9/13/22671182/mozilla-default-browser-windows-protections-firefox) by The Verge, starting in Firefox 91, when a user clicks on the 'Make Default' button, the browser will automatically become the default browser without opening Windows 10 or Windows 11's 'Default apps' settings screen, as shown below.



![Firefox now programmatically changing the default browser](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Firefox now programmatically changing the default browser**  
*Source: BleepingComputer*
"People should have the ability to simply and easily set defaults, but they don’t,” a Mozilla spokesperson told The Verge. "All operating systems should offer official developer support for default status so people can easily set their apps as default. Since that hasn’t happened on Windows 10 and 11, Firefox relies on other aspects of the Windows environment to give people an experience similar to what Windows provides to Edge when users choose Firefox to be their default browser."


With this new change, Mozilla Firefox still leaves users in control over their default browser but allows them to switch to Firefox in a much easier way if they choose.


As Mozilla Firefox is open source, other browser developers may analyze the changes and implement them in their browsers.


BleepingComputer has contacted Microsoft with questions about this bypass but has not heard back at this time.




#### Tags:
[[Windows]] [[Firefox]] [[apps]] [[Mozilla]] [[Microsoft]] [[BleepingComputer]] [[below.]] [[Bleeping Computer]]
