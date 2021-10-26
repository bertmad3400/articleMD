# Mozilla Firefox Blocks Malicious Add-Ons Installed by 455K Users
### The misbehaving Firefox add-ons were misusing an API that controls how Firefox connects to the internet. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175745)
+ Date: October 26, 2021  11:44 am
+ Author: Lisa Vaas


## Article:
![mozilla](https://media.threatpost.com/wp-content/uploads/sites/103/2019/11/20152110/mozilla.jpg)
Mozilla’s Firefox team has blocked add-ons that were abusing the proxy API in order to prevent around 455,000 users from updating their browsers.


In a Monday post, Mozilla’s development team members Rachel Tublitz and Stuart Colville [said](https://blog.mozilla.org/security/2021/10/25/securing-the-proxy-api-for-firefox-add-ons/) that they’d discovered the misbehaving add-ons in early June. The add-ons were misusing the [proxy API](https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/proxy), which APIs use to control how Firefox connects to the internet.


Add-ons are powerful snippets of software that can be added to Firefox or other apps to customize the browser by doing things like preventing tracking, blocking ads, downloading videos from websites or providing content translation.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


On the flip side, they can be nasty little critters that install malware, like the 28 add-ons for Facebook, Vimeo, Instagram and others that [researchers found](https://threatpost.com/3m-users-malicious-facebook-insta-browser-add-ons/162350/) in commonly used browsers from Google and Microsoft last year. The add-ons were siphoning off sensitive data, had the ability to enable further malware downloads, and were tweaking links that victims clicked on in order to redirect them to phishing sites and ads.


The Firefox team said that the misbehaving Firefox add-ons they found in June – named Bypass and Bypass XM – were misusing the API to intercept and redirect users from downloading updates, accessing updated blocklists and updating remotely configured content.


Blocking the Update Blockers
----------------------------


Mozilla has blocked the malicious add-ons in order to keep them from being installed by yet more users. Developers who were waiting on approvals for new add-ons that use the proxy API are also going to have to wait a bit longer, since approval has been paused until fixes are out for all users.


Mozilla has also made a change to how important requests such as update requests get handled by the browser. Starting with Firefox 91.1, if an important request is made via a proxy configuration that fails, Firefox will resort to direct connections instead.


“Ensuring these requests are completed successfully helps us deliver the latest important updates and protections to our users,” the Firefox developers said.


In addition, the team has deployed a [system add-on](https://firefox-source-docs.mozilla.org/toolkit/mozapps/extensions/addon-manager/SystemAddons.html) named [Proxy Failover](https://ftp.mozilla.org/pub/system-addons/proxy-failover/) (ID: proxy-failover@mozilla.com) to block similar malicious add-ons. System add-ons – a way to ship Firefox extensions – are hidden, impossible to disable, and can be updated without the need to restart. Proxy Failover has been shipped to both current and older Firefox versions, Mozilla said.


What Firefox Users Should Do
----------------------------


First, make sure you’re running on the latest version, which as of Monday was Firefox 93 or Firefox ESR 91.2. You should be running at minimum the [latest release version](https://wiki.mozilla.org/Release_Management/Calendar), Mozilla said. Here’s how to [check what version you’re running](https://support.mozilla.org/kb/find-what-version-firefox-you-are-using).


Next, if you’re using Firefox on Windows, make sure that [Microsoft Defender](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/microsoft-defender-antivirus-windows) is running, Mozilla said: “Together, Firefox 93 and Defender will make sure you’re protected from this issue.”


Mozilla said that those who aren’t running the latest version and who haven’t disabled updates might want to check if they’ve been affected by the malicious add-ons. The first step is to try to [update Firefox](https://support.mozilla.org/kb/update-firefox-latest-release): Recent versions come with an updated blocklist that automatically disables the malicious add-ons.


If that doesn’t work, Mozilla provided other ways to fix the problem in [its post](https://blog.mozilla.org/security/2021/10/25/securing-the-proxy-api-for-firefox-add-ons/).


What Firefox Add-on Developers Should Do
----------------------------------------


Mozilla is asking all developers of add-ons that require the use of the proxy API to start including a strict\_min\_version key in their manifest.json files targeting “91.1” or above, as shown in this example:


 **“browser\_specific\_settings”: { “gecko”: { “strict\_min\_version”: “91.1” } }**


“Setting this explicitly will help us to expedite review for your add-on,” the Firefox developers said. “Thank you in advance for helping us to keep Firefox users secure.”


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Firefox]] [[add-ons]] [[Mozilla]] [[API]] [[said.]] [[you’re]] [[add-ons.]] [[ThreatPost]]
