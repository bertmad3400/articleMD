# Google tests if 'Chrome/100.0' user agent breaks websites
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/google/google-tests-if-chrome-1000-user-agent-breaks-websites/)
+ Date: September 23, 2021
+ Author: Lawrence Abrams


## Article:
![Google tests if Chrome/100.0 user agent breaks websites](https://www.bleepstatic.com/content/hl-images/2021/09/23/Chrome_flare.jpg)


Google is testing whether changing the Chrome user agent to three-digit 'Chrome/100' will cause loss of functionality on websites that are expecting a two digit version number.


A user agent is a string sent by a web browser to a website to let the site know what browser the visitor is using, its version, and integrated technology.


When a new version of a browser, such as Google Chrome, is released, the developers will increment the version number in a user agent string.


For example, the user agent for Google Chrome version 93 is:


While for the current version, Chrome 94, it is:


As you can see, the Chrome version number in the user agent string is incremented to match the browser's version number.


By sending the browser user agent to a website, it allows site developers to change a site or app's functionality to accommodate various browser quirks, features, and abilities.


Testing if Chrome 100 user agent breaks websites
------------------------------------------------


As Google Chrome version numbers are currently two digits, Chrome engineers are investigating whether any site, or its functionality, breaks when Chrome 100 is released in March 2022.


"To avoid any UA string breakage when Chrome ships v100, we should add a flag to chrome://flags which flips the current major version to 100 in the User-Agent string as well as navigator.userAgent," Google Chrome engineer Mike Taylor explains in a [bug post](https://bugs.chromium.org/p/chromium/issues/detail?id=1249220) first spotted by [Techdows](https://techdows.com/2021/09/chrome-version-100-user-agent.html).


When conducting the test, Chrome users will have their user agent changed to the following string with the hopes that if anything breaks, they will [report it to Google](https://crbug.com/new).


A [similar test was conducted by Mozilla](https://www.bleepingcomputer.com/news/software/mozilla-tests-if-firefox-1000-user-agent-breaks-websites/) in August 2021 where the Firefox user agent was changed to "Firefox/100.0" user agent.


For the most part, there have [not been too many issues](https://github.com/webcompat/web-bugs/labels/version100), with only a few sites stating the browser is unsupported or problems with the functionality of the site.


Slack's web interface also showed some problems with popup menu buttons, but was [quickly fixed](https://github.com/webcompat/web-bugs/issues/67866) by the Slack developers.


To test the Google Chrome 100 user agent on your own sites or sites you visit, you can enable this test using the following steps:


1. Open [Google Chrome Canary](https://www.google.com/chrome/canary/), enter **chrome://flags** in the address bar, and press **enter**.
2. Search for **Force major version to 100 in User-Agent** in the search field**,**and when the option appears, enable it as shown below.

![Adding the general.useragent.override setting](https://www.bleepstatic.com/images/news/web-browsers/chrome/user-agent-100/chrome-flag.jpg)**Adding the general.useragent.override setting**
3. When prompted to relaunch the browser, please do so.
4. Once the browser is opened again, you can close the chrome://flags screen.


Now that this setting is enabled, when you visit web page it will send a user agent indicating that the browser is Chrome 100.


To change Chrome's user agent back to its default, simply follow this process and change the flag's setting to **Default** and relaunch the browser again.




#### Tags:
[[Google]] [[chrome://flags]] [[Bleeping Computer]]
