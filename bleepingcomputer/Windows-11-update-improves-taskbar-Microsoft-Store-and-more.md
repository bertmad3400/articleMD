# Windows 11 update improves taskbar, Microsoft Store and more
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-11-update-improves-taskbar-microsoft-store-and-more/)
+ Date: July 22, 2021
+ Author: Mayank Parmar


## Article:
![Windows 11](https://www.bleepstatic.com/content/hl-images/2021/07/08/Windows-11.jpg)


Microsoft has released a new preview build 22000.100 to Windows 11 Insiders in the Dev channel of the Windows Insider program.


As part of the latest Windows 11 update, Microsoft is updating the hidden icons flyout on the lower right of the Taskbar to match the new visuals of Windows 11.



![Windows 11 taskbar](https://www.bleepstatic.com/images/news/u/1097497/Windows-10/Flyout.png)Taskbar flyout
Microsoft is also introducing a new design feature that will tell you when an app requires attention. As shown in the below screenshot, the app will automatically flash on the Taskbar. This new alert design matches the look and feel of Windows 11, and the focus is on minimizing the impact of unwarranted distractions.



![Windows 11 alert](https://www.bleepstatic.com/images/news/u/1097497/Windows-10/Alert.png)Alert
Build 22000.100 also comes with improvements for the new Microsoft Store. This new update will improve the performance of the Microsoft Store, especially when you select an app or movie.


**Changes and Improvements**
----------------------------


* [We have started rolling out Chat from Microsoft Teams to Insiders in the Dev Channel](https://blogs.windows.com/windows-insider/2021/07/20/first-preview-of-chat-from-microsoft-teams-begins-rolling-out-to-windows-insiders/).
* When a background activity from an app requires attention, the app will flash on the Taskbar to get your attention. In Windows 11, we have updated this design so that it still grabs your attention but with a calming treatment that minimizes the impact of unwarranted distractions. The subtle flashing eventually stops, and you will see a slightly red backplate and red pill under the app icon continuing to note a background activity needs your attention. Let us know what you think!
* The touch keyboard icon in the Taskbar has been adjusted to be more consistent with the size of the other icons in the corner of the Taskbar.
* The Taskbar calendar flyout will now fully collapse down when clicking the chevron in the top corner to give you more room for notifications.
* In the latest Microsoft Store update rolling out to Insiders, we made navigation in our new Microsoft Store feel fast and fun. When you select an app or movie you’re interested in, you might notice some animations that help you keep track of what you’re browsing. Give it a try, we hope you like it as much as we do.


 
 
 
**Fixes**
---------


* Taskbar:
	+ We fixed the issue that was causing Explorer.exe to crash when the date and time button on the Taskbar is clicked to access new notifications with Focus Assist turned off.
	+ Added the missing settings icons for the context menu entries when right clicking network, volume, and battery in the Taskbar.
	+ Fixed an issue that was making the clock in the Taskbar get stuck and out of sync.
	+ Addressed an explorer.exe that could happen after resuming from standby, related to the volume icon in the Taskbar.
	+ There is an issue where the progress bar below app icons in the Taskbar wasn’t always displaying when it was expected to and have fixed it.
	+ Clicking on the Taskbar when either Start or Search is open will now make them dismiss.
	+ If you tap Taskbar icons using touch you should now see the same icon animation that was visible when using the mouse.
	+ The lunar calendar (when enabled) text should no longer overlap the numbers in the Taskbar calendar flyout.
	+ The calendar flyout should now show the correct month when in a collapsed state.
	+ The date at the top of the calendar flyout should now follow your preferred format and not the format matching your display language.
	+ If the Start menu is open, when hovering over Task View the window will now appear above Start menu instead of behind it.
	+ Right-clicking Task View will now make the preview window dismiss so you can actually use the context menu.
	+ Fixed an issue where if you click on a snap group in the Taskbar, it might not bring up all the app windows after docking and undocking.
	+ The icons used for the On / Off indicators in the Taskbar for the Pinyin IME are now a consistent size.
	+ Signing out and back in when battery saver is running should no longer result in Taskbar becoming transparent.
	+ Mitigated an issue making the network icon sometimes unexpectedly not show in the Taskbar.
	+ The Taskbar previews will no longer draw offscreen after upgrading to this build.
* Settings:
	+ We fixed an issue causing multiple buttons and options in Settings to not work in the previous flight, including Go Back and Reset Your PC under Recovery, enabling Developer mode, renaming your PC, and enabling Remote Desktop.
	+ The page titles in Settings should no longer be drawing too high up / off screen.
	+ Searching for add and remove programs in Settings should now return the expected Settings page.
	+ We’ve done some work to help search in Settings initialize faster.
	+ Addressed an issue that was causing crashes in Settings when interacting with the Windows Insider Program section.
	+ Fixed an issue that could make Settings crash on launch.
	+ Fixed an icon rendering issue in Power and Battery Settings.
	+ Fixed some reliability issues with the Language and Region page in Settings.
	+ Made a change to help address a problem where the preview in Personalization Settings sometimes unexpectedly showed you were using a black wallpaper when you weren’t.
	+ The font used in the Lock Screen Settings preview should now match the actual lock screen.
	+ Fixed a bug making all the icons in Quick Settings appear unexpectedly flipped for Insiders using the Arabic display language.
	+ Using the brightness slider in Quick Settings should now show a number as you’re adjusting, like it does with volume.
* File Explorer:
	+ Using mouse to open the context menu in File Explorer and on the desktop should no longer display a keyboard focus rectangle on first launch (until you start using the keyboard to navigate it).
	+ We’ve tweaked the context menu to address feedback that sometimes submenus were unexpectedly closing when you were trying to use them.
	+ Fixed a flicker where you could see New become New Item in the context menu.
	+ We’ve done some work on the context menu positioning logic so that submenus should no longer appear partially offscreen or unexpectedly far away.
	+ We fixed two issues impacting explorer.exe reliability when bringing up the context menu, including specifically when right-clicking on a zip file.
	+ Addressed an issue causing the “Unpin from Start” option when right clicking an app to not work.
* Search:
	+ Fixed an issue making Search’s shadow appear boxy.
	+ Have adjusted the positioning of the Search window when the Taskbar is left aligned, so that it matches Start.
	+ We’ve addressed an issue where what was displaying when hovering over the Search icon in the Taskbar wasn’t in sync with what would actually launch when you clicked one of the entries.
	+ If you’ve launched websites using Search, those should now be properly displayed in the recent searches when hovering over the Search icon in the Taskbar.
	+ Made a change to address an issue where some Insiders were unexpectedly not seeing the brightness slider in Quick Settings after upgrading.
* Widgets:
	+ We fixed an issue resulting in your widget configurations not getting saved and unexpectedly being reset.
	+ The widgets board and content should now be sized for the correct screen when using multiple monitors.
	+ Addressed an issue where sign-in wasn’t working for widgets in some scenarios due to authentication hanging.
	+ We’ve made another fix to address the clock in the widgets board not following your preferred format.
* Other:
	+ Device Security should no longer say “Standard hardware security not supported” for Insiders with supported hardware.
	+ With this build the access keys for WIN + X (so that you can do things like “WIN + X M” to launch Device Manager) should now appear consistently.
	+ Fingerprint sign in should no longer stop working after rebooting your PC.
	+ Addressed an accessibility issue where keyboard focus would disappear from Start after pressing Tab then Shift + Tab.
	+ Fixed a bug causing the informational pop ups in voice typing to not dismiss on click.
	+ Fixed an infinite loop making some Insider’s devices hang during shutdown.
	+ We made an adjustment to help address an issue causing the title bar to not render correctly on certain apps.
	+ Made a fix to stop your wallpaper from flashing when switching between Desktops.
	+ Updated the snap layouts window to now use the default animation for flyouts instead of just popping in.
	+ Addressed an issue that was making Sticky Notes and Microsoft To Do crash on launch sometimes.
	+ Fixed a DWM memory leak that was happening when rotating your device back and forth between landscape and portrait mode.
	+ Made a change to address the issue where text could become truncated in the message dialog from Windows Update alerting that an update was ready.
	+ Window borders should now be displayed correctly when using high contrast.
	+ Turning off “Show shadows under windows” in Performance Options should now actually turn off the shadows under windows.
	+ We’ve made some tweaks to fix an issue where context menus and tooltip were appearing far from the mouse when using Windows with the Arabic display language.
	+ Addressed an issue where the network icons on the lock screen and login screen weren’t consistent.


**Known issues**
----------------


* **[REMINDER]** When upgrading to Windows 11 from Windows 10 or when installing an update to Windows 11, some features may be deprecated or removed. [See details here](https://www.microsoft.com/en-us/windows/windows-11-specifications#primaryR4).
* Start:
	+ In some cases, you might be unable to enter text when using Search from Start or the Taskbar. If you experience the issue, press WIN + R on the keyboard to launch the Run dialog box, then close it.
	+ System and Windows Terminal is missing when right-clicking on the Start button (WIN + X).
* Taskbar:
	+ The Taskbar will sometimes flicker when switching input methods.
* Settings:
	+ When launching the Settings app, a brief green flash may appear.
	+ When using Quick Settings to modify Accessibility settings, the settings UI may not save the selected state.
	+ Settings will crash when clicking “Facial recognition (Windows Hello)” under Sign-in Settings if Windows Hello is already set up.
* File Explorer:
	+ exe crashes in a loop for Insiders using the Turkish display language when battery charge is at 100%.
	+ The context menu sometimes doesn’t render completely and ends up truncated.
	+ Clicking a desktop icon or context menu entry may result in the wrong item being selected.
* Search:
	+ After clicking the Search icon on the Taskbar, the Search panel may not open. If this occurs, restart the “Windows Explorer” process, and open the search panel again.
	+ When you hover your mouse over the Search icon on the Taskbar, recent searches may not be displayed. To work around the issue, restart your PC.
	+ Search panel might appear as black and not display any content below the search box.
* Widgets:
	+ Widgets board may appear empty. To work around the issue, you can sign out and then sign back in again.
	+ Launching links from the widgets board may not invoke apps to the foreground.
	+ Widgets may be displayed in the wrong size on external monitors. If you encounter this, you can launch the widgets via touch or WIN + W shortcut on your actual PC display first and then launch on your secondary monitors.
* Store:
	+ We are working to improve search relevance in the Store including resolving an issue where in some cases the ordering of search results is inaccurate.
	+ The install button might not be functional yet in some limited scenarios.
	+ Rating and reviews are not available for some apps.
* Windows Security
	+ “Automatic sample submission” is unexpectedly turned off when you restart your PC.
	+ Windows Hello (Face) may show an error saying “Something went wrong” when attempting to sign in after upgrading. To work around this, sign in with your password or PIN and:
		- Open Device Manager.
		- Uninstall “Windows Hello Face Software Device” under “Biometric devices”.
	+ Localization
		- There is an issue where some Insiders may be some missing translations from their user experience for a small subset of languages running the latest Insider Preview builds. To confirm if you have been impacted, [please visit this Answers forum post](https://aka.ms/UnderLocIssue) and follow the steps for remediation


How to get the update
---------------------


By joining the Windows Insider program, you can download early preview builds of Windows 11.  o get started with the Windows 10 Insider Program, you need to signup for the program here and follow these steps:


1. Open **Settings**.
2. Navigate to **Update & security** and then select the **Windows Insider program** settings.
3. Click the Get started button to begin joining the Windows 10 Insider Program
4. Register your Microsoft account with the Windows Insider Program.
5. After your account is linked, you will be prompted to select a Ring.
6. To download Windows 11, select the Dev channel.
7. Restart Windows when prompted.




#### Tags:
[[Taskbar]] [[Windows]] [[Microsoft]] [[ve]] [[flyout]] [[exe]] [[window]] [[windows]] [[apps]] [[Bleeping Computer]]
