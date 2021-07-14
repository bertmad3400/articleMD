# Google Chrome will add HTTPS-First Mode to keep your data safe
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/google-chrome-will-add-https-first-mode-to-keep-your-data-safe/)
+ Date: July 14, 2021
+ Author: Sergiu Gatlan


## Article:
![Google Chrome will add HTTPS-First Mode to keep your data safe](https://www.bleepstatic.com/content/hl-images/2021/05/26/0_Google-Chrome.jpg)


Google will add an HTTPS-First Mode to the Chrome web browser to block attackers from intercepting or eavesdropping users' web traffic.


"Beginning in M94, Chrome will offer HTTPS-First Mode, which will attempt to upgrade all page loads to HTTPS and display a full-page warning before loading sites that don't support it." Google said.



"Users who enable this mode gain confidence that Chrome is connecting them to sites over HTTPS whenever possible, and that they will see a warning before connecting to sites over HTTP."


By upgrading all connections to websites to HTTPS, Google Chrome 94 will protect users from man-in-the-middle (MITM) attacks trying to snoop on or alter data exchanged with Internet servers over the unencrypted HTTP protocol.




> 
> To summarize, we're building an HTTPS-First Mode that you can enable in settings, and experimenting w/ replacing the padlock icon to adapt to a 90%+ HTTPS world. And we're evaluating how to better protect and inform users while they're visiting websites that still use http://
> 
> 
> — Emily Stark (@estark37) [July 14, 2021](https://twitter.com/estark37/status/1415357690885206020?ref_src=twsrc%5Etfw)


HTTPS-First Mode already available for Chrome Canary users
----------------------------------------------------------


BleepingComputer has reported earlier this month that [Google's web browser will get an HTTPS-Only Mode](https://www.bleepingcomputer.com/news/security/google-chrome-will-get-an-https-only-mode-for-secure-browsing/) for secure browsing.


The new feature is currently being tested in the Chrome 93 Canary preview releases for Mac, Windows, Linux, Chrome OS, and Android.


If you want to test the experimental feature right now, you will have to enable the "HTTPS-Only Mode Setting" flag by going to *chrome://flags/#https-only-mode-setting*.


This will add an "Always use secure connections" option to Chrome's security settings which, once enabled, will set up the web browser to upgrade all navigation to HTTPS and show alerts before loading websites that don't support it.


![](https://www.bleepstatic.com/images/news/u/1109292/2021/Chrome%20HTTPS-Only%20Mode.png)


HTTPS all the way
-----------------


Google is not the first web browser vendor to consider, including automatically upgrading all navigation to HTTPS.


For instance, [Mozilla added an HTTPS-Only Mode](https://www.bleepingcomputer.com/news/software/firefox-83-boosts-security-with-https-only-mode-zero-day-fix/) starting with Firefox 83 to secure web browsing by rewriting URLs to use the HTTPS protocol (even though disabled by default, this feature can be enabled from the browser's settings).


Microsoft Edge now can also be set up to switch users to secure HTTPS connections when connecting to websites over HTTP after enabling a new experimental [Automatic HTTPS option](https://www.bleepingcomputer.com/news/security/microsoft-adds-automatic-https-in-edge-for-secure-browsing/) available in the Canary and Developer preview channels, with an estimated release later this month.


Google has also previously updated [Chrome to default to HTTPS](https://www.bleepingcomputer.com/news/google/google-chrome-90-released-with-https-as-the-default-protocol/) for all URLs typed in the address bar if the user doesn't specify a protocol.


"While we are excited to see users adopt HTTPS-First Mode in future versions of Chrome, HTTP connections will still continue to be supported and Chrome will take additional steps to protect and inform users whenever they are using insecure connections," Google [added](https://blog.chromium.org/2021/07/increasing-https-adoption.html).


"Continuing from our past efforts to [restrict new features to secure origins](https://www.chromium.org/Home/chromium-security/prefer-secure-origins-for-powerful-new-features) and [deprecate powerful features on insecure origins](https://www.chromium.org/Home/chromium-security/deprecating-powerful-features-on-insecure-origins), we'll evaluate a broad set of web platform features to determine if they should be limited or restricted on HTTP webpages."




#### Tags:
[[HTTPS]] [[Google]] [[HTTPS-First]] [[HTTP]] [[websites]] [[HTTPS-Only]] [[Bleeping Computer]]
