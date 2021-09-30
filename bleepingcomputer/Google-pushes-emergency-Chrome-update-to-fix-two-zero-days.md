# Google pushes emergency Chrome update to fix two zero-days
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/google-pushes-emergency-chrome-update-to-fix-two-zero-days/)
+ Date: September 30, 2021
+ Author: Lawrence Abrams


## Article:
![Google Chrome zero-day vulnerabilities](https://www.bleepstatic.com/content/hl-images/2021/09/23/Chrome_flare.jpg)


Google has released Chrome 94.0.4606.71 for Windows, Mac, and Linux, to fix two zero-day vulnerabilities that have been exploited by attackers.


"Google is aware the exploits for CVE-2021-37975 and CVE-2021-37976 exist in the wild," Google disclosed in the [list of security fixes](https://chromereleases.googleblog.com/2021/09/stable-channel-update-for-desktop_30.html) fixed in today's Google Chrome release.


Google has started rolling out Chrome 94.0.4606.71 to users worldwide in the Stable Desktop channel and should be available to all users within the coming days.


To install the update immediately, Google Chrome users can go to **Chrome menu**> **Help**> **About Google Chrome**, and the browser will begin performing the update.


In our tests, the new version of the browser was installed immediately using the above steps.



![Chrome 94.0.4606.71 installed immediately](https://www.bleepstatic.com/images/news/web-browsers/chrome/chrome-94.jpg)**Chrome 94.0.4606.71 was installed immediately**
Google Chrome will also check for available updates and install them the next time you launch the web browser.


Zero-day attacks' details not disclosed
---------------------------------------


While this Chrome release includes fixes for four security vulnerabilities, the two zero-days are concerning as they are known to have been exploited in the wild.


The first zero-day, tracked as **CVE-2021-37976**, is described as an "Information leak in core" and was assigned a Medium severity level. This vulnerability was discovered by Clément Lecigne from Google TAG, with technical assistance from Sergei Glazunov and Mark Brand from Google Project Zero, on September 21st, 2021.


The second zero-day, tracked as **CVE-2021-37975**, is a High severity [user after free](http://cwe.mitre.org/data/definitions/416.html) bug in the Chrome V8 JavaScript engine. The researcher disclosed this vulnerability on September 24th and wished to remain anonymous.


Use after free bugs are commonly used to perform remote code execution or escape the browser's security sandbox.


At this time, there are no other details regarding how these zero-day vulnerabilities were used in attacks but may be released in future reports by Google TAG or Project Zero.




> 
> 2 more in-the-wild 0days fixed by Chrome:  
> 
> * CVE-2021-37975 use-after-free in V8 by anonymous  
> 
> * CVE-2021-37976 info leak in core by [@\_clem1](https://twitter.com/_clem1?ref_src=twsrc%5Etfw) [#itw0days](https://twitter.com/hashtag/itw0days?src=hash&ref_src=twsrc%5Etfw)  
>   
> 
> The release cycle that Chrome is making happen in order to get these patches out is pretty impressive<https://t.co/j1xPY4zjlP>
> 
> 
> — Maddie Stone (@maddiestone) [September 30, 2021](https://twitter.com/maddiestone/status/1443660891837239304?ref_src=twsrc%5Etfw)


Chrome users should perform a manual upgrade or restart their browser to install the latest version and prevent exploitation attempts.


Thirteenth zero-day fixed this year
-----------------------------------


With these two fixes, Google has patched 13 zero-day vulnerabilities in the Chrome web browser since the start of 2021.


The other Chrome zero-day bugs Google fixed this year are:


* [CVE-2021-21148](https://www.bleepingcomputer.com/news/security/google-fixes-chrome-zero-day-actively-exploited-in-the-wild/) - February 4th, 2021
* [CVE-2021-21166](https://www.bleepingcomputer.com/news/security/google-fixes-second-actively-exploited-chrome-zero-day-bug-this-year/) - March 2nd, 2021
* [CVE-2021-21193](https://www.bleepingcomputer.com/news/security/google-fixes-second-actively-exploited-chrome-zero-day-this-month/) - March 12th, 2021
* [CVE-2021-21220](https://chromereleases.googleblog.com/2021/04/stable-channel-update-for-desktop.html) - April 13th, 2021
* [CVE-2021-21224](https://www.bleepingcomputer.com/news/security/google-fixes-exploited-chrome-zero-day-dropped-on-twitter-last-week/) - April 20th, 2021
* [CVE-2021-30551](https://www.bleepingcomputer.com/news/security/google-fixes-sixth-chrome-zero-day-exploited-in-the-wild-this-year/) - June 9th, 2021
* [CVE-2021-30554](https://www.bleepingcomputer.com/news/security/google-fixes-seventh-chrome-zero-day-exploited-in-the-wild-this-year/) - June 17th, 2021
* [CVE-2021-30563](https://www.bleepingcomputer.com/news/security/google-patches-8th-chrome-zero-day-exploited-in-the-wild-this-year/) - July 15th, 2021
* [CVE-2021-30632 and CVE-2021-30633](https://www.bleepingcomputer.com/news/google/google-patches-10th-chrome-zero-day-exploited-in-the-wild-this-year/) - September 13th
* [CVE-2021-37973](https://www.bleepingcomputer.com/news/security/emergency-google-chrome-update-fixes-zero-day-exploited-in-the-wild/) - September 24th, 2021


As Google is rushing out Chrome updates to fix zero-days as they are reported, it is always critical to install new browser updates as soon as they become available.




#### Tags:
[[Google]] [[zero-day]] [[Bleeping Computer]]
