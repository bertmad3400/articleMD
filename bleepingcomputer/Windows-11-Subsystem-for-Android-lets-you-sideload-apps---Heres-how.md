# Windows 11 Subsystem for Android lets you sideload apps - Here's how
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-11-subsystem-for-android-lets-you-sideload-apps-heres-how/)
+ Date: October 20, 2021
+ Author: Lawrence Abrams


## Article:
![Android](https://www.bleepstatic.com/content/hl-images/2021/09/17/Android_headpic.jpg)


Microsoft has released the first preview version of the Windows Subsystem for Android for Windows 11 Insiders, and one of the more interesting features is that you can sideload Android apps.


The [Windows Subsystem for Android](https://www.bleepingcomputer.com/news/microsoft/hands-on-with-microsofts-android-app-support-in-windows-11/) is a new feature of Windows 11 that allows you to run native Android apps directly from the desktop in a virtualized environment.






These apps will have graphics support, audio, and even network access, allowing you to play multiplayer games online.


To install Android apps, Microsoft has partnered with Amazon to create the Amazon Appstore, which currently contains 50 curated apps.



![Amazon Appstore](https://www.bleepstatic.com/images/news/Microsoft/windows-11/a/windows-subsystem-for-android/preview-release/amazon-app-store.jpg)**Amazon Appstore**
However, the Windows Subsystem for Android also allows you to sideload apps using the [Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb), theoretically allowing you to install any app you wish.


How to sideload apps in Windows Subsystem for Android
-----------------------------------------------------


While the apps available in the Amazon Appstore have been curated by Microsoft to make sure they are bug-free and work well with the new Android feature, many other apps will work as well.


The good news is that you can use sites like APKPure or APKMirror to download APKs and sideload them using ADB.


To sideload an Android app in the Windows Subsystem for Android (WSA), please follow these steps:


1. Download the Android app you want from [APKPure](https://m.apkpure.com/) or [APKMirror](https://www.apkmirror.com/).
2. Download the [Android SDK Platform-Tools for Windows](https://dl.google.com/android/repository/platform-tools-latest-windows.zip) and extract it to your hard drive.
3. Click on the Start menu and type Android. When the **Windows Subsystem for Android** search result is displayed, click on it, as shown in the image below.

![Opening the Windows Subsystem for Android](https://www.bleepstatic.com/images/news/Microsoft/windows-11/a/windows-subsystem-for-android/sideload/start-menu-android.jpg)**Opening the Windows Subsystem for Android**
4. The Windows Subsystem for Android settings screen will now open. Scroll down and enable **'Developer mode**' and then click on the '**Copy**' button in the IP address field. If you do not see an IP address, click Refresh and try again.   
  

If you are still cannot see an IP address, open the '**Files**' option at the top of the Settings to make sure the subsystem is enabled.

![Windows Subsystem for Android Settings](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Windows Subsystem for Android Settings**
5. Open a command prompt and **CD** to the folder you extracted the platform tools. For example, if you extracted the tools to C:\Platform-tools, you would enter `cd c:\platform-tools` and press enter.
6. You will now be in the folder containing the Android SDK platform tools.  Enter the command `adb connect ipaddress`, where the IP address is the one you copied in step 4.  
  

For example, to connect to the WSA running on my computer, you would enter `adb connect 172.30.204.180`. If you see an error about it not being authenticated, ignore the message.
7. Now you want to install the APK using the `adb install apk` command. For example, if your APK is named 'com.innersloth.spacemafia\_2021.6.30-967\_minAPI23(arm64-v8a,armeabi-v7a)(nodpi)\_apkmirror.com.apk' and was saved in the Downloads folder,  you would type:  
  
`adb install %UserProfile%\downloads\com.innersloth.spacemafia_2021.6.30-967_minAPI23(arm64-v8a,armeabi-v7a)(nodpi)_apkmirror.com.apk`

![Sideloading an APK in WSA](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Sideloading an APK in WSA**
8. When you are done sideloading your apps, you will find them listed in your Start Menu.

![Sideloaded Among Us now available in the Windows 11 Start Menu](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Sideloaded Among Us now available in the Windows 11 Start Menu**
9. You can now close the command prompt.


To launch your sideloaded apps, simply click on them from the Start Menu. Like apps installed through the Amazon Appstore, sideloaded apps will have network access and sound.



![Sus screenshot of the Among Us Android app](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Sus screenshot of the Among Us Android app**
At this time, not all sideloaded apps will work in WSA yet, so you may experience blank screens when you attempt to launch an app.


There are also many malicious Android apps floating around the Internet, so be careful of what you install as it is not clear what access Android apps have to the rest of the Windows environment.


BleepingComputer has reached out to Microsoft with questions about sideloading apps but has not heard back at this time.




#### Tags:
[[Android]] [[Windows]] [[apps]] [[sideload]] [[Microsoft]] [[IP]] [[apps,]] [[example,]] [[adb]] [[WSA]] [[Bleeping Computer]]
