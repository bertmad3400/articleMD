# Mozilla Firefox cracks down on malicious add-ons used by 455,000 users
### The troublesome add-ons misused an API that controlled how Firefox connected to the internet.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/mozilla-firefox-cracks-down-on-malicious-add-ons-used-by-455000-users/)
+ Date: October 26, 2021
+ Author: Charlie Osborne


## Article:
Unknown

Mozilla's Firefox browser team has cracked down on malicious add-ons, blocking software with a 455,000 user base. 


On October 25, the [development team said](https://blog.mozilla.org/security/2021/10/25/securing-the-proxy-api-for-firefox-add-ons/) that in early June, Firefox discovered add-ons that were misusing the browser's proxy API, used by software to manage how the browser connects to the internet. 

Add-ons are software modules that can be installed to customize a user's browsing experience and may include anti-tracking software, ad blockers, themes, and utilities.  

However, they may also become a conduit for malicious purposes, such as data theft or eavesdropping, a challenge faced by all browser developers.  

According to Mozilla, the add-ons removed in the sweep tampered with the browser's update functionality; in particular, users were unable to download updates, access updated blocklists, or update remotely configured Firefox content.  

The add-ons have been blocked, and approval was temporarily paused for new add-on developer submissions when the proxy API was in use to create and deploy a fix.  

Firefox, starting with v.91.1, now also includes changes to harden the update process. A fallback mechanism to direct connections for update purposes and other "important requests" made by the browser has been implemented, allowing downloads to take place whether or not a proxy configuration causes connection issues.  






The system add-on, "Proxy Failover," has been deployed to Firefox users.  

Mozilla released [Firefox version 93](https://www.zdnet.com/article/firefox-93-arrives-with-tab-unloading-insecure-download-blocks-and-enforced-referrer-trim/) at the beginning of October. The latest build includes a new tab unloading feature, the ability to block HTTP downloads from HTTPS web pages, and the end of default support for 3DES encryption.  

Mozilla has urged users to make sure their Firefox version is up to date. Developers making use of the proxy API are being asked to start including the code "browser\_specific\_settings ": {   "gecko": {     "strict\_min\_version": "91.1"   }  } in their add-ons to expedite future reviews.  

"We take user security very seriously at Mozilla," the team says. "Our add-on submission process includes automated and manual reviews that we continue to evolve and improve in order to protect Firefox users." 

###  Previous and related coverage

* [Firefox 93 arrives with tab unloading, insecure download blocks and enforced referrer trim](https://www.zdnet.com/article/firefox-93-arrives-with-tab-unloading-insecure-download-blocks-and-enforced-referrer-trim/)
* [Mozilla: Superman, Batman, Spider-Man dominate list of passwords leaked in breaches](https://www.zdnet.com/article/mozilla-superman-batman-spider-man-dominate-list-of-passwords-leaked-in-breaches/)
* [Mozilla artists question whether AI could predict police killings](https://www.zdnet.com/article/mozilla-artists-question-whether-ai-could-predict-police-killings/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Firefox]] [[Mozilla]] [[add-ons]] [[ZDNet]]
