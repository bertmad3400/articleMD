# Mozilla blocks malicious add-ons installed by 455K Firefox users
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/mozilla-blocks-malicious-add-ons-installed-by-455k-firefox-users/)
+ Date: October 25, 2021
+ Author: Sergiu Gatlan


## Article:
![Mozilla blocks add-ons installed by 455,000 users for API abuse](https://www.bleepstatic.com/content/hl-images/2021/05/26/Mozilla.jpg)


Mozilla blocked malicious Firefox add-ons installed by roughly 455,000 users after discovering in early June that they were abusing the [proxy API](https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/proxy) to block Firefox updates.


The add-ons (named Bypass and Bypass XM) were using the API to intercept and redirect web requests to block users from downloading updates, updating remotely configured content, and accessing updated blocklists.


"To prevent additional users from being impacted by new add-on submissions misusing the proxy API, we paused on approvals for add-ons that used the proxy API until fixes were available for all users," Mozilla's  Rachel Tublitz and Stuart Colville said.


"Starting with Firefox 91.1, Firefox now includes changes to fall back to direct connections when Firefox makes an important request (such as those for updates) via a proxy configuration that fails.


"Ensuring these requests are completed successfully helps us deliver the latest important updates and protections to our users."


To block similar malicious add-ons to abuse the same API, Mozilla has added a system add-on (hidden, impossible to disable, and updateable restartlessly) dubbed [Proxy Failover](https://ftp.mozilla.org/pub/system-addons/proxy-failover/).


This new add-on prevents attempts to interfere with update mechanisms in current and older Firefox versions.



![Bypass blocked from installing](https://www.bleepstatic.com/images/news/u/1109292/2021/Bypass_blocked.png)*Malicious Bypass add-onn blocked from installing (BleepingComputer)*
While Mozilla didn't share if the two add-ons were doing anything else malicious in the background, BleepingComputer found after analyzing them that they likely were using a reverse proxy to bypass paywalled sites.


However, the add-ons also had Mozilla's domain in the paywall list which inadvertently also blocked browser updates.


A Mozilla spokesperson wasn't able to provide more details when contacted by BleepingComputer earlier today.


How to make sure you're not affected
------------------------------------


Mozilla advises users to update their web browsers to at least the latest release version (Firefox 93), which can make sure that they're protected from add-ons abusing the proxy API.


"It is always a good idea to keep Firefox up to date, and if you’re using Windows to make sure Microsoft Defender is running. Together, Firefox 93 and Defender will make sure you’re protected from this issue," Tublitz and Colville [added](https://blog.mozilla.org/security/2021/10/25/securing-the-proxy-api-for-firefox-add-ons/).


Microsoft Defender is [the only anti-malware solution detecting the add-ons as malicious](https://www.virustotal.com/gui/file/df743f9de2cdefa5b2f949ea8fe30f31bf944d460d38a266d55f00e72ca98a79/detection), tagging them as [BrowserModifier:JS/BypassPaywall.A](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=BrowserModifier:JS/BypassPaywall.A&threatId=303550).


If you're not running Firefox 93 and have not disabled browser updates, you could be impacted by this issue. To make sure, try to update Firefox to the latest versions since it bundles an updated blocklist designed to disable these malicious add-ons automatically.


If you still can't update Firefox, you also have the option to find the add-ons that block you from upgrading to a newer version and [remove them](https://support.mozilla.org/kb/disable-or-remove-add-ons) by going through these steps:


1. Visit the [Troubleshooting Information page](https://support.mozilla.org/kb/use-troubleshooting-information-page-fix-firefox#w_accessing-the-troubleshooting-information-page).
2. In the Add-ons section, search for one of the following entries:


Name: Bypass


ID: {7c3a8b88-4dc9-4487-b7f9-736b5f38b957}


Name: Bypass XM


ID: {d61552ef-e2a6-4fb5-bf67-8990f0014957}


NOTE: Make sure the IDs match exactly as there might be other, unrelated add-ons using those or similar names. If none of those IDs are shown in the list, you are not affected.


If you want to ensure that there are no traces left, you can also [refresh Firefox](https://support.mozilla.org/kb/refresh-firefox-reset-add-ons-and-settings) to reset all add-ons and settings or start from scratch by [downloading and installing a new copy of Firefox](https://www.mozilla.org/firefox/all).




#### Tags:
[[add-ons]] [[Firefox]] [[Mozilla]] [[API]] [[add-on]] [[Bleeping Computer]]
