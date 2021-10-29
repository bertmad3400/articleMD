# Google fixes two high-severity zero-day flaws in Chrome
### This is the third set of zero-day patches for Chrome in three months.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/google-fixes-two-high-severity-zero-day-flaws-in-chrome/)
+ Date: October 29, 2021
+ Author: Liam Tung


## Article:
Unknown

It's time to update Chrome and once again, for the third month in a row, Google has fixed two previously unknown 'zero-day' bugs in the world's most popular desktop browser.

Google disclosed that it had patched the two high-severity zero-day flaws in release notes for the stable release of Chrome version 95.0.4638.69 for Windows, Mac and Linux. Any version number higher than that will have the fixes.


It's a good idea to check out [Google's support page for Chrome updates](https://support.google.com/chrome/answer/95414?hl=en&co=GENIE.Platform=Desktop#:~:text=Go%20to%20%22About%20Google%20Chrome,Chrome%20to%20apply%20the%20update), which explains how Chrome can be set to automatically update when patches become available. Otherwise, Chrome has an 'Update' button that is coloured red if an update is at least a week old, indicating that it should be installed.

**SEE:** [**This new ransomware encrypts your data and makes some nasty threats, too**](https://www.zdnet.com/article/this-new-ransomware-encrypts-your-data-and-makes-some-nasty-threats-too/)

The two zero-day flaws -- which are being exploited by attackers now -- are being tracked with the identifiers CVE-2021-38000 and CVE-2021-38003. Both were found by Google's Threat Analysis Group (TAG), which tracks state-sponsored and cyber-criminal exploit activity. 

The second of the two zero-days was also reported by Samuel Groß from Google Project Zero on 26 October, indicating how fast Google is responding to zero-day discoveries.

CVE-2021-38000 is a design flaw due to "insufficient validation of untrusted input in Intents". It was reported by TAG on September 15.






CVE-2021-38003 -- a memory corruption flaw, [according to Google Project Zero's zero-day tracker](https://docs.google.com/spreadsheets/d/1lkNJ0uQwbeC1ZTRrxdtuPLCIl7mlUreoKfSIgajnSyY/view#gid=2129022708) -- is described vaguely as "inappropriate implementation in V8". V8 is [Chrome's powerful JavaScript engine that Groß hopes to shore up](https://www.zdnet.com/article/bugs-in-chromes-javascript-engine-can-lead-to-powerful-exploits-this-project-aims-to-stop-them/) with additional sandboxing protections. As he [noted in his proposal](https://docs.google.com/document/d/1FM4fQmIhEqPG8uGp5o9A-mnPB5BOeScZYpkHjo0KKA8/edit#heading=h.calchrb3vnqq), V8 bugs allow attackers to create "unusually powerful exploits" that are hard to mitigate with existing security technologies.

"Google is aware that exploits for CVE-2021-38000 and CVE-2021-38003 exist in the wild," [Google said in release notes](https://chromereleases.googleblog.com/2021/10/stable-channel-update-for-desktop_28.html). The update will roll out over the coming days or weeks, according to Google. 

There are eight, mostly memory-related, security fixes in this Chrome update. The currently listed high-severity flaws include a [use-after-free](https://encyclopedia.kaspersky.com/glossary/use-after-free/) in Sign-in, another use-after-free in Chrome's garbage collection, insufficient data validation in Chrome's New Tab page, a type confusion in V8, and a use-after-free in Web Transport.

**SEE:** [**Cloud security in 2021: A business guide to essential tools and best practices**](https://www.zdnet.com/article/cloud-security-in-2021-a-business-guide-to-essential-tools-and-best-practices/)

This Chrome release marks the 14th zero-day flaw Google has patched in Chrome this year. The [10th was in mid-September](https://www.zdnet.com/article/google-patches-two-chrome-zero-days/) when it patched two zero-days. It patched two [more zero-days at the end of September](http://v) and a further two on Thursday.

Google hasn't attributed the exploits to any hacking group. 

That Google has patched an unusually high number of zero-day flaws in Chrome in 2021 could be interpreted in several ways. The more that get discovered and the quicker they're fixed via updates is good for end-users. Once patched, the exploit is less valuable. This could mean defenders are getting better at spotting zero-days.

On the other hand, Google Project Zero has seen an [uptick in zero-days affecting major platforms like Chrome, Windows, and iOS in the past year](https://www.zdnet.com/article/google-details-recent-malware-campaigns-amid-uptick-in-zero-day-attacks/). The reason for that could be the commercialisation of the zero-day exploit market, providing a shortcut to the acquisition of exploits that otherwise require skills to develop.





#### Tags:
[[Google]] [[zero-day]] [[zero-days]] [[use-after-free]] [[ZDNet]]
