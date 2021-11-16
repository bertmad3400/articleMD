# Google Chrome 96 breaks Twitter, Discord, video rendering and more
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/google/google-chrome-96-breaks-twitter-discord-video-rendering-and-more/)
+ Date: November 16, 2021
+ Author: Mayank Parmar


## Article:
![chrome](https://www.bleepstatic.com/content/hl-images/2021/09/23/Google_Chrome.jpg)


Google Chrome 96 was released yesterday, and users are reporting problems with Twitter, Discord, and Instagram caused by the new version.


After upgrading to Chrome 96, users report errors in their Twitter notifications, with the website warning that "Something went wrong. Try reloading," as shown below.


![Twitter](https://www.bleepstatic.com/images/news/u/1097497/Google/Twitter-Chrome-96.jpg)


Other Twitter users are reporting GIFs turning black, images not displayed, or videos unable to play. In their place, Twitter shows the same error message reading, "Something went wrong."


![Twitter bug](https://www.bleepstatic.com/images/news/u/1097497/Google/Twitter-bug.jpg)


Other users have reported that Discord features are also partially broken, with the web app feeling slower and the loading icon not appearing correctly.


Google is aware of the issues
-----------------------------


The issues have been reported to Google in a Chromium [bug post](https://bugs.chromium.org/p/chromium/issues/detail?id=1270437) where Google employees have started to investigate the problems.


"We're continuing to see user reports about this behavior, including reports from our social team," notes Google product manager Craig Tumblison.


"One user has shared that disabling the "chrome://flags/#cross-origin-embedder-policy-credentialless" flag resolves the behavior. Another report shares a specific error message: "The connection was rejected at [https://cards-frame.twitter.com](https://cards-frame.twitter.com/)". Test team, would you be able to try enabling that flag to see if the behavior appears?"


The 'chrome://flags/#cross-origin-embedder-policy-credentialles' flag is related to a [new Cross-Origin-Embedder-Policy feature](https://chromestatus.com/feature/4918234241302528) released with Chrome 96.


Google states that you can fix these bugs in some cases by setting the "chrome://flags/#cross-origin-embedder-policy-credentialless" to disabled.


If you are affected by these issues, you can copy and paste the above chrome:// address into the Google Chrome address bar and press enter. When the experimental flag appears, please set it to **Disabled**and relaunch the browser when prompted.


If this policy is related to the issues seen on Twitter, Discord, and Instagram, Google will likely push out a configuration change to disable the feature until they resolve the conflicts.




#### Tags:
[[Google]] [[Bleeping Computer]]
