# Mozilla tests if 'Firefox/100.0' user agent breaks websites
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/software/mozilla-tests-if-firefox-1000-user-agent-breaks-websites/)
+ Date: August 9, 2021
+ Author: Lawrence Abrams


## Article:
![Firefox](https://www.bleepstatic.com/content/hl-images/2020/11/17/Firefox.jpg)


Mozilla has launched an experiment where they change the Firefox browser user agent to a three-digit "Firefox/100.0" version to see if it will break websites.


A user agent is a string used by a web browser that includes information about the software, including its name, version, and technologies that it uses.



When a new version of a browser is released, the developers also increment the version number in the user agent string.


For example, the current user agent for Mozilla Firefox version 90 is listed below.


*Note, if you have the Firefox 'privacy.resistFingerprinting' setting set to 'True,' your user agent will be locked to 'Firefox/78.0.'*


For Google Chrome 92, the current user agent is:


When visiting a website, the user agent strings are sent to a website so that the site knows the software capabilities of the visitor. This information allows the website to modify its response to account for different features of browsers.


Testing whether Firefox 100 user agent breaks websites
------------------------------------------------------


As Firefox version numbers are currently two digits, Mozilla developers are investigating if anything breaks when they release Firefox Nightly version 100 in March 2022.


"We would like to run an experiment to test whether a UA string with a three-digit Firefox version number will break many sites," Mozilla Staff Engineering Program Manager Chris Peterson said in a [bug post](https://bugzilla.mozilla.org/show_bug.cgi?id=1719070) first spotted by [Techdows](https://techdows.com/2021/08/firefox-version-100-ua-string-experiment.html).


"This new temporary `general.useragent.experiment.firefoxVersion` pref can override the UA string's Firefox version."


When conducting the test, a enrolled Firefox user will have their user agent changed to the following string with the hopes that if anything breaks, they will report it to Mozilla.


Peterson said he has been testing using the browser with a "Firefox/100.0" user agent string for about four months and has only [encountered an issue when using Slack.](https://github.com/webcompat/web-bugs/issues/67866)


"I discovered Slack's message popup menu's buttons (such as "Add reaction" or "Reply in thread") stop working for Firefox versions >= 100 and = 520," explained Peterson.


In this case, the issue appears to be a bug with Slack comparing the version numbers are strings rather than numbers (integers). While Slack quickly fixed this issue, it illustrates how simple coding errors can produce unexpected results when the user agent changes to version 100.


If continued tests show that many sites are broken by the new user agent, Firefox is may freeze the user agent to a two-digit number like "Firefox/99.0."


For those who wish to test the upcoming user agent change on their own sites or sites they frequently visit, you can manually change your user agent string using these steps:


1. Open Firefox, enter **about:config** in the address bar, and press **enter**.
2. Search for **general.useragent.override**.
3. When it appears, select 'String' and then click on the plus (+) sign, as shown in the image below.

![Adding the general.useragent.override setting](https://www.bleepstatic.com/images/news/web-browsers/firefox/v100-user-agent-test/firefox-add-setting.jpg)**Adding the general.useragent.override setting**
4. After clicking on the + icon, a field should open where you should enter the text: **Mozilla/5.0 (Windows NT 10.0; rv:100.0) Gecko/20100101 Firefox/100.0**as shown below.

![](https://www.bleepstatic.com/images/news/web-browsers/firefox/v100-user-agent-test/configured-user-agent-setting.jpg)**Configured Firefox 100 user agent**
5. Then click on the checkmark button to save the setting.
6. You can close the about:config tab.


While this setting is in place, the browser will send the new user agent string to websites. If you run into any issues with the websites you visit, you should [create a new bug report for Mozilla](https://bugzilla.mozilla.org/enter_bug.cgi).


To change your user agent back to its original string, simply go back into **about:config** and search for **general.useragent.override** setting again. 


When it appears, click on the trash can icon to delete the configured setting.




#### Tags:
[[Firefox]] [[Mozilla]] [[below.]] [[about:config]] [[Bleeping Computer]]
