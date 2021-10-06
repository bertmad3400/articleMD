# Firefox improves advertising tracker blocking in private browsing
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/firefox-improves-advertising-tracker-blocking-in-private-browsing/)
+ Date: October 6, 2021
+ Author: Sergiu Gatlan


## Article:
![Firefox now blocks Google Analytics tracking in private browsing](https://www.bleepstatic.com/content/hl-images/2021/10/06/Firefox.jpg)


*Image: [Richard Horvath](https://unsplash.com/@orwhat)/BleepingComputer*


Mozilla says that Firefox users will be better protected from advertising trackers (like Google Analytics scripts) while browsing the Internet in Private Browsing mode and using Strict Tracking Protection.


This is because, starting with the Firefox 93 version released yesterday, the browser comes with improved web compatibility for privacy protections via SmartBlock 3.0.


The [SmartBlock](https://blog.mozilla.org/security/2021/03/23/introducing-smartblock/) mechanism, introduced by Mozilla with the release of Firefox 87 in March, ensures that the [Tracking Protection](https://www.bleepingcomputer.com/news/software/firefox-86-gets-a-privacy-boost-with-total-cookie-protection/) feature and Strict Mode don't break websites when blocking tracking scripts.


It does that by loading local and privacy-preserving alternatives to blocked resources with behavior similar enough to the original ones to ensure that the site still works properly.


"The third iteration of SmartBlock brings vastly improved support for replacing the popular Google Analytics scripts and added support for popular services such as Optimizely, Criteo, Amazon TAM and various Google advertising scripts," Mozilla [said](https://blog.mozilla.org/security/2021/10/05/firefox-93-features-an-improved-smartblock-and-new-referrer-tracking-protections/).


"As usual, these replacements are bundled with Firefox and can not track you in any way.


Starting with this release, Firefox also comes with enhanced Referrer Tracking Protection which blocks sites from sharing sensitive user data via HTTP referrers by trimming the HTTP referrer for cross-site requests, regardless of the site's settings.


How Firefox private browsing defends your privacy
-------------------------------------------------


Mozilla also announced in July that the SmartBlock cross-site tracking blocking tech was [updated to block Facebook tracking scripts](https://www.bleepingcomputer.com/news/security/firefox-90-adds-enhanced-tracker-blocking-to-private-browsing/) while still allowing logins to work.


In June, it also enabled [Total Cookie Protection by default in Private Browsing](https://www.bleepingcomputer.com/news/security/firefox-now-blocks-cross-site-tracking-by-default-in-private-browsing/) windows starting with Firefox 89, automatically protecting users from cross-site tracking.


While browsing the Internet in private mode, Firefox is designed to protect your privacy with several privacy protection technologies, all of them enabled by default:


* [Total Cookie Protection](https://www.bleepingcomputer.com/news/software/firefox-86-gets-a-privacy-boost-with-total-cookie-protection/) isolates cookies to the site where they were created.
* [Supercookie protections](https://www.bleepingcomputer.com/news/software/firefox-85-adds-supercookie-protection-removes-flash-support/) stop supercookies from following you from site to site.
* [Cookies and caches are cleared](https://support.mozilla.org/en-US/kb/private-browsing-use-firefox-without-history#w_what-does-private-browsing-not-save) at the end of every Private Browsing session and aren't shared with standard windows.
* [Trackers are blocked](https://blog.mozilla.org/blog/2019/06/04/firefox-now-available-with-enhanced-tracking-protection-by-default/), including cookies, scripts, tracking pixels, and other resources from domains on Disconnect's list of known trackers.
* [Many fingerprinting scripts are blocked](https://blog.mozilla.org/security/2020/01/07/firefox-72-fingerprinting/)**,** according to Disconnect's list of invasive fingerprinting domains.
* [SmartBlock](https://blog.mozilla.org/security/2021/03/23/introducing-smartblock/) intelligently fixes up web pages that were previously broken when tracking scripts were blocked.


To switch to private browsing, you have to open the Application Menu by clicking the button (☰) on the top right corner and choose "New Private Window."


You can also enable private browsing mode by using the Ctrl + Shift + P (or Cmd + Shift + P on macOS) keyboard shortcut.


In related news, Firefox 93 now also [blocks downloads over HTTP](https://blog.mozilla.org/security/2021/10/05/firefox-93-protects-against-insecure-downloads/) to protect against potentially unsafe or malicious downloads.


Furthermore, when available system memory is critically low on Windows devices, [Firefox will automatically unload browsing tabs](https://www.mozilla.org/en-US/firefox/93.0/releasenotes/) based on their last access time, memory usage, and other attributes to reduce out-of-memory crashes.




#### Tags:
[[Firefox]] [[SmartBlock]] [[Mozilla]] [[Google]] [[HTTP]] [[cross-site]] [[Bleeping Computer]]
