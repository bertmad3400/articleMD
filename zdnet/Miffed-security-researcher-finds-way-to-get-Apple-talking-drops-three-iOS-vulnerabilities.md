# Miffed security researcher finds way to get Apple talking, drops three iOS vulnerabilities
### Almost six months after reporting the first vulnerability to Apple, a security researcher has gone public to reopen lines of communication with Apple.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/miffed-security-researcher-finds-way-to-get-apple-talking-drop-three-ios-vulnerabilities/)
+ Date: September 27, 2021
+ Author: Chris Duckett


## Article:
Unknown

![appleevent-sep14keynote-tim-cook-03.jpg](https://www.zdnet.com/a/hub/i/r/2021/09/14/c64deb89-21f6-486d-a8b6-0059c8cac43a/resize/1200xauto/57f8d00d07e627dc074d5190ea46023e/appleevent-sep14keynote-tim-cook-03.jpg)
 Image: Apple
 For most of 2021, a security researcher going by the name of illusionofchaos has been engaged in an unfruitful conversation with Apple to fix a number of vulnerabilities that allow apps to make API calls to pull down user information that they should not be able to. 

On Friday, the researcher went public with their [findings](https://habr.com/en/post/579714/), which contained one vulnerability fixed in iOS 14.7 and three unpatched vulnerabilities. 

The fixed bugs involved Analyticsd and allowed apps to access logs containing medical information, device usage information, application crashes, and information on device accessories. 

The unpatched vulnerabilities included the gamed service not properly checking game-center permission and allowing access to the Core Duet database that contains all contacts from Mail, SMS, iMessages, and some attachments; Apple ID email, full name, and authentication tokens allowing access to access at least one [apple.com](http://apple.com/) endpoint; and read access to speed dial database and address book.  

A vulnerability in Nehelper allowed for an app to check whether any other app was installed, and another Nehelper bug allowed for unauthorised access to Wi-Fi information. 

The researcher said when Apple fixed the Analyticsd issue, they were not credited, with Apple saying in July that credit was forthcoming. By September, the researcher was still waiting. 

For each vulnerability, the researcher published proof-of-concept code on GitHub. 






On Saturday, the researcher received a response from Apple, which said it had seen the blog post and apologised for the delay. 

"We want to let you know that we are still investigating these issues and how we can address them to protect customers. Thank you again for taking the time to report these issues to us, we appreciate your assistance," Apple said. 

ZDNet asked Apple for comment on Friday, but we are still awaiting a response. 

Over the weekend, a blind developer [complained](https://twitter.com/oriol_gomez92/status/1442018220135927810) that Apple had labelled as spam an update to make an accessible version of Hangman run on iOS 15. 

"My app is made for the blind and that all the other hangman games I have seen on the app store are half playable and ... this is a bugfix update and already existing users who have paid for the app are unable to play using iOS 15," Oriol Gómez sentís wrote. 

"To my horror, they replied saying that yes, 'we understand that your app has voiceover', hello? My app has voiceover? But unfortunately the rejection is still in place." 

By the early hours of Monday morning, the developer said Apple had approved the update, but the app remained in violation of App Store guidelines. 

### Related Coverage

* [Apple releases patches for Catalina and iOS 12.5.5 vulnerabilities](/article/apple-releases-patches-for-catalina-and-ios-12-5-5-vulnerabilities/)
* [EU wants USB-C to become standard charging port for all smartphones to limit e-waste](/article/eu-wants-usb-c-to-become-standard-charging-port-for-all-smartphones-to-cut-down-e-waste/)
* [Don't like the iPhone's new Safari in iOS 15? Here's how to fix it](/article/dont-like-the-iphones-new-safari-in-ios-15-heres-how-to-fix-it/)
* [Apple bans Epic Games from App Store until all litigation is finalised](/article/apple-bans-epic-games-from-app-store-until-all-litigation-is-finalised/)
* [Facebook sees Q3 turbulence over Apple privacy changes](/article/facebook-sees-q3-turbulence-over-apple-privacy-changes/)





#### Tags:
[[]] [[ZDNet]]
