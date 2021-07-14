# The impact of Apple’s sideloading philosophy on developers
### On June 23, Apple unleashed messaging to explain why users should only install Apple-approved apps through its App Store on iOS.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/the-impact-of-apples-sideloading-philosophy-on-developers/)
+ Date: July 13, 2021 -- 21:22 GMT (22:22 BST)
+ Author: Forrester Research


## Article:
Unknown

![shutterstock-200250458.jpg](https://www.zdnet.com/a/hub/i/r/2021/07/13/29bb5b74-f4ed-430f-9720-4d1f3ebe0dfc/resize/1200xauto/1f257a4ccf28a69d91b25be9bd2e0bd8/shutterstock-200250458.jpg)(Image: Apple)

On June 23, Apple [unleashed messaging](https://www.apple.com/privacy/docs/Building_a_Trusted_Ecosystem_for_Millions_of_Apps.pdf) to explain why users should only install Apple-approved apps through its App Store on iOS. This is an extension of the US District Court case between Apple and Epic, where Apple positioned "sideloading," the practice of installing apps outside its App Store, as dangerous. 

While it is true that Apple has led the industry in privacy -- in particular making it difficult for businesses and rogue apps to obtain unnecessary personal information -- connecting this messaging to non-Apple installs seems a bit of an overreach. Moreover, it sets up a challenging dichotomy for developers: Do you promise choice or reassurance as your app's key marketing message? 


### **Smartphone As A "Pattern-Of-Life" Device**

Apple has cited at least one study saying,"[…] devices that run on Android had 15 times more infections from malicious software than iPhone." In a June 16 interview, Tim Cook said that Android has 47 times more malware than iOS does. These are interesting numbers, given the relative sizes of the Android and iOS markets. [Android has almost 73% market share worldwide, while iOS sits at just under 27%](https://gs.statcounter.com/os-market-share/mobile/worldwide). As with the PC and Mac markets, it makes sense that the prime targets are those with the largest market share. However, this also brings up an interesting conundrum -- there are billions of PCs and, pointedly, Macs in the world, and they don't have locked ecosystems. 

Apple further makes the argument that smart devices are carried with you all day, so they can gather [more "pattern-of-life" details](https://www.fastcompany.com/90649203/apple-iphone-sideloading-safety-apps-tech) than traditional computers. But how well does this apply to iPads, which are just as mobile as iPhones, and that Apple is also positioning as traditional laptop replacements? 

### **What This Means For The Mobile Developer**

Regardless of messaging, Apple's tactics have an impact on app developers. Small development shops may suffer remembering the hoops they jumped through to sign an iOS app before Xcode 8. Even today, some developers hold their breath when submitting to the App Store. In 2020, Apple says it rejected almost a million new apps. Of those, about half were misleading, violated privacy guidelines, contained undocumented features, or had fraudulent violations. 

Regardless, as an iOS developer, you have two basic choices: Ship using the App Store or not. If you are a smaller developer and want to monetize to any reasonable degree, you must use the Store. However, let's say you're not as worried about monetization -- perhaps you are a larger organization with different needs. What options do you have to distribute your app outside the App Store? 

* **Use the web.**Despite the limitations that Apple has put on web APIs, you can still do a lot with JavaScript on Safari. Creating a progressive web app allows you to "install" it. You'll have to walk your users through adding your icon to the home screen, but if you can live without push notifications, geofences, Bluetooth, serial connections, magnetometers, light sensors, NFC, and battery life (among other things), you can create code that runs in Safari. Microsoft recently did this to allow [cloud streaming of Xbox games](https://news.xbox.com/en-us/2021/04/19/xbox-cloud-gaming-windows-pc-and-apple-limited-beta/). The good news for web developers: Biometric ID support was added in Safari 14 (PublicKey.isUserVerifyingPlatformAuthenticatorAvailable), and camera and microphone APIs were added in Safari 11 (MediaDevices.getUserMedia). Geolocation has been around since Safari 3 (Geolocation.getCurrentPosition).
* **Join the Apple Developer Enterprise Program.** If your app is meant for employees of your company and you work with more than 100 employees, your company can apply to enter the Apple Developer Enterprise Program. This will permit you to ship your app to employees without going through the App Store. In the past, enterprise certificates were used to distribute apps outside an organization; now, Apple has said it reserves the right to review apps distributed via enterprise certificates.
* **Use ad hoc distribution.** If you have a small number of high-value customers, you can distribute your app as a .ipa file that you generate and make available for download. Installation can be tricky: You will need to get the UDID of each device (up to 100) and entitle the devices in your account on developer.apple.com. Some developers point users to <http://whatsmyudid.com/> to walk them through the process. You'll also have to manage revoking and readding UDIDs and reissuing provisioning profiles on your own if your users switch devices.
* **Ship the source.** Since 2015, Xcode has allowed you to build software for iOS devices without a developer account. Telling users how to download and install the Xcode binaries, and possibly the Xcode command line binaries, if you want to automate an install is not trivial. However, it does allow you to deploy your software to customer devices -- if those customers have a Mac with a version of macOS that supports the Xcode version you want to use. Since users have your source, they are free to change it. You can package your code into a framework or library to reduce what users can modify.
* **Require a jailbroken device.** This is extreme and limits your user base to those who have the technical skill to hack their device. There's also the obvious concern of taking advantage of security defects to run arbitrary code, and there may not be exploits for all iOS devices. However, your more technical users may have already jailbroken. Jailbreaking requires a Mac, and some jailbreaks require that the phone remain tethered to a computer while booting. Once jailbroken, a user can install your app from a third-party app store -- [Cydia](https://cydia-app.com/) is a commonly used one.

Of course, there's also a sixth option, which we don't recommend: Give up on Apple. Given that Android apps will run not just on Android devices but [now Windows 11 desktops and laptops](https://blogs.windows.com/windowsexperience/2021/06/24/introducing-windows-11/), that is an option for those who want to make their own decisions about security, privacy, and what they install. 






Really, it comes down to use case. For consumer-facing or information-worker apps, you likely have to abide by Apple's sideloading philosophy. However, for task worker apps, where enterprises provision the device to employees or even business partners, sideloading flexibility has some value. If you are supporting franchisees or an extended network of suppliers, you have the option of preferring Android rather than navigating Apple's restrictions. 

*This post was written by Senior Analyst Andrew Cornwall, and it originally appeared*[*here*](https://go.forrester.com/blogs/the-impact-of-apples-sideloading-philosophy-on-developers/?utm_source=zdnet&utm_medium=pr&utm_campaign=tech)*.*






#### Tags:
[[apps]] [[Android]] [[--]] [[Xcode]] [[sideloading]] [[jailbroken]] [[ZDNet]]
