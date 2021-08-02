# Google Chrome to no longer show secure website indicators
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/google/google-chrome-to-no-longer-show-secure-website-indicators/)
+ Date: August 2, 2021
+ Author: Lawrence Abrams


## Article:
![Google Chrome](https://www.bleepstatic.com/content/hl-images/2021/03/24/Google-Chrome-headpic.jpg)


Google Chrome will no longer show whether a site you are visiting is secure and only show when you visit an insecure website.


For years, Google has been making a concerted effort to push websites into using HTTPS to provide a more secure browsing experience.



To further push web developers into only using HTTPS on their sites, Google introduced the [protocol as a ranking factor](https://developers.google.com/search/blog/2014/08/https-as-ranking-signal). Those not hosting a secure site got a potentially minor hit in their Google search results rankings.


It has appeared to have worked as according to the '[HTTPS encryption on the web](https://transparencyreport.google.com/https/overview)' of Google's Transparency Report, over 90% of all browser connections in Google Chrome currently use an HTTPS connection.



![Google Chrome HTTPS usage by platform](https://www.bleepstatic.com/images/news/web-browsers/chrome/chrome-93/security-indicators/https-usage-chart.jpg)**Google Chrome HTTPS usage by platform**  
*Source: Google*
Currently, when you visit a secure site, Google Chrome will display a little locked icon indicating that your communication with the site is encrypted, as shown below.



![Security indicator shown in address bar](https://www.bleepstatic.com/images/news/web-browsers/chrome/chrome-93/security-indicators/secure-site-indicator.jpg)**Security indicator shown in address bar**
As most website communication is now secure, Google is testing a new feature that removes the lock icon for secure sites. This feature is available to test in Chrome 93 Beta, and Chrome 94 Canary builds by enabling the '**Omnibox Updated connection security indicators**' flag.



![Security indicators to be removed in Google Chrome](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Security indicators to be removed in Google Chrome**
With this feature enabled, Google Chrome will only display security indicators when the site is not secure, as shown below.



![Showing 'Not secure' indicator for insecure sites](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Showing 'Not secure' indicator for insecure sites**
For businesses who wish to have continued HTTPS security indicators, Google has added an enterprise policy for Chrome 93 named 'LockIconInAddressBarEnabled' that can be used to enable the lock icon again on the address bar.


How to disable Chrome's security indicators
-------------------------------------------


For those who want to test out the disabling of Chrome security indicators feature, you can enable it in Chrome Beta or Chrome Canary using these instructions.


1. Enter **chrome://flags** in the address bar and press **enter**.
2. Search for '**security indicators**.'
3. When the '**Omnibox Updated connection security indicators**' flag is shown, click on '**Default**' and select '**Enabled**.'

![Omnibox Updated connection security indicators Chrome flag](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Omnibox Updated connection security indicators Chrome flag**
4. Now relaunch the browser when prompted.


Google will no longer show you if a site is secure and only show an indicator when you visit an insecure site.




#### Tags:
[[Google]] [[HTTPS]] [[Bleeping Computer]]
