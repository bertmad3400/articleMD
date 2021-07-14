# Firefox 90 lands with just-in-time support for unblocking Facebook when users log in
### Facebook trackers remained blocked by default in strict mode and private windows, but if a user wants to login using Facebook then SmartBlock 2.0 will lower its shields.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/firefox-90-lands-with-just-in-time-support-for-unblocking-facebook-when-users-log-in/)
+ Date: July 14, 2021 -- 05:02 GMT (06:02 BST)
+ Author: Chris Duckett


## Article:
Unknown

![firefox.png](https://www.zdnet.com/a/hub/i/2019/11/01/a4fb8186-b7f3-4e61-8a77-16050e1b1fb6/firefox.png)
 Image: Mozilla
 Firefox 90 appeared from Mozilla this week, and one of the new features that arrived was better support for logging in using Facebook credentials when the browser is in strict tracker blocking mode, or a private window. 

[SmartBlock](https://www.zdnet.com/article/firefox-87-launch-packed-with-private-browsing-smartblock/) first appeared in Firefox 87, released in March, and it provided local stand-ins for blocked third-party tracking scripts. 

"These stand-in scripts behave just enough like the original ones to make sure that the website works properly. They allow broken sites relying on the original scripts to load with their functionality intact," Mozilla said at the time. 

One area where SmartBlock failed though, was supporting Facebook login buttons across the web. In a [blog post](https://blog.mozilla.org/security/2021/07/13/smartblock-v2/), Mozilla explained it was due to Facebook trackers being included on the list of tracker provided by its partner, but the updated SmartBlock 2.0 should fix this. 

"Prior to Firefox 90, if you were using a private browsing window, when you clicked on the 'Continue with Facebook' button to sign in, the 'sign in' would fail to proceed because the third-party Facebook script required had been blocked by Firefox," the blog states. 

"Now, SmartBlock 2.0 in Firefox 90 eliminates this login problem. Initially, Facebook scripts are all blocked, just as before, ensuring your privacy is preserved. But when you click on the 'Continue with Facebook' button to sign in, SmartBlock reacts by quickly unblocking the Facebook login script just in time for the sign-in to proceed smoothly." 

Mozilla said the new functionality worked on "numerous websites", and Firefox would continue blocking Facebook trackers on all sites where a user has not logged in. 






Users on Windows will now have Firefox [updated in the background](https://support.mozilla.org/en-US/kb/enable-background-updates-firefox-windows), with Firefox 90 checking every 7 hours for a new version. To enable background updating, users need to allow for updates to be automatically installed and tick a "When Firefox is not running" checkbox. The feature only works when the browser has been installed from its installer, rather than decompressed from a zip file, and does not have a language pack installed. 

Although Mozilla said it would gradually roll out the feature, a napp.update.background.scheduling.enabled flag exists for users to turn it on now. 

Firefox on Windows will also gain an [about:third-party page](https://support.mozilla.org/en-US/kb/identify-problems-third-party-modules-firefox-windows) that lists modules, such as anti-virus, that have been injected into the browser and could cause issues. 

Firefox 90 will also support [Fetch Metadata Request Headers](https://blog.mozilla.org/security/2021/07/12/firefox-90-supports-fetch-metadata-request-headers/) to allow web apps to defend against some cross-site attacks. 

"The HTTP request header Sec-Fetch-Site allows the web application server to distinguish between a same-origin request from the corresponding web application and a cross-origin request from an attacker-controlled website," Mozilla said. 

"Inspecting Sec-Fetch-* Headers ultimately allows the web application server to reject or also ignore malicious requests because of the additional context provided by the Sec-Fetch-* header family. In total there are four different Sec-Fetch-* headers: Dest, Mode, Site, and User which together allow web applications to protect themselves and their end users against [cross-site attacks]." 

The latest edition of Firefox finally marks the [end of support for FTP](https://www.zdnet.com/article/mozilla-to-start-disabling-ftp-next-week-with-removal-set-for-firefox-90/) in the browser, and most users who do not have hardware-accelerated WebRender will use software WebRender instead. 

### Related Coverage

* [Firefox 88 clamps down on window.name abuses by trackers](/article/firefox-88-clamps-down-on-window-name-abuses-by-trackers/)
* [Firefox 87 launch packed with private browsing 'SmartBlock'](/article/firefox-87-launch-packed-with-private-browsing-smartblock/)
* [Chinese cyberspies targeted Tibetans with a malicious Firefox add-on](/article/chinese-cyberspies-targeted-tibetans-with-a-malicious-firefox-add-on/)
* [Firefox to block Backspace key from working as "Back" button](/article/firefox-to-block-backspace-key-from-working-as-back-button/)





#### Tags:
[[Firefox]] [[Facebook]] [[Mozilla]] [[SmartBlock]] [[window]] [[third-party]] [[Sec-Fetch-]] [[ZDNet]]
