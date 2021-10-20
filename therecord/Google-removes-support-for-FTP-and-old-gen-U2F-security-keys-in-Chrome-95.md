# Google removes support for FTP and old-gen U2F security keys in Chrome 95
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/google-removes-support-for-ftp-and-old-gen-u2f-security-keys-in-chrome-95/)
+ Date: October 20, 2021
+ Author: Catalin Cimpanu


## Article:
![Google removes support for FTP and old-gen U2F security keys in Chrome 95](https://therecord.media/wp-content/uploads/2021/08/Google-Chrome.jpg)

Google has released today Chrome v95, the latest version of its popular web browser, a version that contains several changes that will likely cause problems for a considerable part of its users.


The problematic changes include:


* removing support for File Transfer Protocol (FTP) URLs — ftp://
* removing support for the Universal 2nd Factor (U2F) standard, used in old-generation security keys (Chrome will only support FIDO2/WebAuth security keys going forward)
* adding file size limits for browser cookies [see [here](https://www.chromestatus.com/feature/4946713618939904)]
* removing support for URLs with non-IPv4 hostnames ending in numbers, such as *http://example.0.1* [see [here](https://www.chromestatus.com/feature/5679790780579840)]


In addition to breaking changes, Chrome 95 also comes with a new UI component called the “Side Panel,” which can be used to view the Chrome browser’s Reading List and Bookmarks. This panel can be enabled via the following Chrome flag:


**chrome://flags/#side-panel**


![Chrome95-side-panel](https://www-therecord.recfut.com/wp-content/uploads/2021/10/Chrome95-side-panel-1024x585.png)Image: The Record
Additionally, Chrome 95 also ships with [developer-focused changes](https://blog.chromium.org/2021/09/chrome-95-beta-secure-payment.html) and [security fixes](https://chromereleases.googleblog.com/2021/10/stable-channel-update-for-desktop_19.html). Other changes are detailed in the image below:


![Chrome95-release-notes](https://www-therecord.recfut.com/wp-content/uploads/2021/10/Chrome95-release-notes.png)Image: The Record



#### Tags:
[[]] [[The Record]]
