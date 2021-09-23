# Google: Manifest V2 Chrome extensions to stop working in 2023
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/google/google-manifest-v2-chrome-extensions-to-stop-working-in-2023/)
+ Date: September 23, 2021
+ Author: Sergiu Gatlan


## Article:
![Google: Manifest V2 Chrome extensions to stop working in 2023](https://www.bleepstatic.com/content/hl-images/2021/05/26/0_Google-Chrome.jpg)


Google has shared the phase-out timeline for Manifest V2 Chrome extensions and its plans to bring Manifest V3 to full feature parity.


Extension capabilities are restricted using a mechanism called [extension manifest](https://developer.chrome.com/extensions/manifestVersion). Google made available the new version, Manifest V3, when Chrome 88 [was announced](https://blog.chromium.org/2020/12/manifest-v3-now-available-on-m88-beta.html) earlier this year.


Google first [revealed the future Manifest V3 changes](https://www.bleepingcomputer.com/news/security/chrome-extension-manifest-v3-may-break-ublock-origin-content-blocker/) through a provisional document in 2019, which announced the removal of webRequest API blocking options and requirements for content blockers to switch to declarativeNetRequest.


"Years in the making, Manifest V3 is more secure, performant, and privacy-preserving than its predecessor," [said David Li](https://developer.chrome.com/en/blog/mv2-transition/), Product Manager for Chrome Extensions & Chrome Web Store.


"It is an evolution of the extension platform that takes into consideration both the changing web landscape and the future of browser extensions."


As outlined today by Li, Google will focus the Manifest V2 extensions phase out around two specific dates:


* **January 17, 2022**: New Manifest V2 extensions will no longer be accepted by the Chrome Web Store. Developers may still push updates to existing Manifest V2 extensions, but no new Manifest V2 items may be submitted.


* **January 2023**: The Chrome browser will no longer run Manifest V2 extensions. Developers may no longer push updates to existing Manifest V2 extensions.





![Manifest V3 transition plans](https://www.bleepstatic.com/images/news/u/1109292/2021/Manifest%20V3%20transition%20plans.png)*Manifest V3 transition plans (Google)*
Google to keep improving Manifest V3 based on feedback
------------------------------------------------------


Until Manifest V2 Chrome extensions are fully deprecated, Google promised to continue bringing the new manifest to full feature parity with the older version and addressing the requests made by developers.


Google says it already added additional mechanisms to the new [Scripting API](https://developer.chrome.com/docs/extensions/reference/scripting/) and expanded the [Declarative Net Request API](https://developer.chrome.com/docs/extensions/reference/declarativeNetRequest/) to support multiple static rulesets, session-scoped rules, and filtering based on tab ID.


"In the coming months, we'll also be launching support for dynamically configurable content scripts and an in-memory storage option, among other new capabilities," Li added.


"These changes were crafted with community feedback in mind, and we will continue to build more powerful extension API functionality as developers share more information about their migration challenges and business needs."


The company also plans to share additional information on how these incoming changes will affect users and extension developers.


Detailed and up-to-date info on exact dates and milestone details for the Manifest V2 phase-out is available [here](https://developer.chrome.com/docs/extensions/mv3/mv2-sunset/).


A fully detailed timeline with all expected Chrome Web Store and Chrome browser behavior changes is embedded below.





| **Date** | **Chrome Web Store behavior changes** | **Chrome Browser behavior changes** |
| **01/17/22** | • Chrome Web Store stops accepting new Manifest V2 extensions with visibility set to “Public" or "Unlisted”  

• Existing Manifest V2 extensions can no longer be changed from “Private” to "Public" or "Unlisted" | *no change* |
| **06/01/22** | • Chrome Web Store stops accepting new Manifest V2 extensions with visibility set to “Private” | *no change* |
| **01/01/23** | • Chrome Web Store stops accepting updates to existing Manifest V2 extensions | • Chrome stops running Manifest V2 extensions  

• Enterprise policy can let Manifest V2 extensions run on Chrome deployments [within the organization](https://support.google.com/chrome/a/answer/9296680?hl=en). |
| **06/01/23** | *no change* | • Manifest V2 extensions no longer function in Chrome even with the use of enterprise policy |


Controversy behind the transition to Manifest V3
------------------------------------------------


In the initial Manifest V3 version, Google changed webRequest's API so that extensions could only monitor browser connections but not alter any of the content before being displayed.


The new declarativeNetRequest API was also changed to tell the browser, not extensions, to strip content or resources from visited sites. The biggest drawback to these changes was that this API came with a limit of 30,000 rules, drastically limiting ad blockers' functionality.


As [uBlock Origin's](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm) Raymond Hill [said at the time](https://www.bleepingcomputer.com/news/security/chrome-extension-manifest-v3-may-break-ublock-origin-content-blocker/), ad blockers that rely on webRequest API's original functionality need more rules than are available in the declarativeNetRequest API.


As Google told BleepingComputer at the time and confirmed by Li today, "these changes are in the design process," with the company still adding new features and capabilities based on developer and user feedback.


Li also said today that Google continues to work with other browser vendors in the Web Extensions Community Group to build a common cross-browser extension model.




#### Tags:
[[V2]] [[Google]] [[API]] [[V3]] [[webRequest]] [[Bleeping Computer]]
