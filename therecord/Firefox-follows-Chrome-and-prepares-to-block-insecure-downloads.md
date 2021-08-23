# Firefox follows Chrome and prepares to block insecure downloads
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/firefox-follows-chrome-and-prepares-to-block-insecure-downloads/)
+ Date: August 23, 2021
+ Author: Catalin Cimpanu


## Article:
![Firefox follows Chrome and prepares to block insecure downloads](https://therecord.media/wp-content/uploads/2021/08/Firefox-block-downloads.png)

Mozilla developers are putting the finishing touches on a new feature that will block insecure file downloads in Firefox.


Called **mixed content downloaded blocking**, the feature works by blocking files downloads initiated from an encrypted HTTPS page but which actually take place via an unencrypted HTTP channel.


The idea behind this feature is to prevent Firefox users from getting misled by the URL bar and think they’re downloading a file securely via HTTPS when, in reality, the file could be tampered with by third parties while in transit.


**Feature specifics:**


* All HTTP files download from an HTTPS page will be blocked with a message in the Firefox Download Center (CTRL+J).
* An option will be available to let users allow the download if they choose to.
* HTTP file downloads from HTTP pages will not be blocked.
* Directly accessed HTTP download links (copy-pasted in the Firefox address bar) will not be blocked.
* The feature is already live and activated in Firefox Beta, Developer, and Nightly editions.
* Based on current Firefox [bug](https://bugzilla.mozilla.org/show_bug.cgi?id=1721146) [tracker](https://bugzilla.mozilla.org/show_bug.cgi?id=1722286) entries, the feature is expected to be activated for all Firefox users in v92, scheduled for a formal release at the start of September 2021.


A similar feature is [already present in Chrome](https://blog.chromium.org/2020/02/protecting-users-from-insecure.html) and the vast majority of Chromium-based browsers since late 2020, having been rolled out in multiple stages from Chrome v81 to v88.


Firefox Stable users who’d like to test it right now can go to the **about:config** settings page and enable the following option:


**dom.block\_download\_insecure**—set to true





#### Tags:
[[Firefox]] [[HTTP]] [[HTTPS]] [[The Record]]
