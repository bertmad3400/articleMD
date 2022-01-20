# Pervasive Apple Safari Bug Exposes Web-Browsing Data, Google IDs
### The information-disclosure issue, affecting Macs, iPhones and iPads, allows a snooping website to find out information about other tabs a user might have open.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177809
+ Date: 2022-01-20T16:50:30+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2019/12/23170046/Apple-bug-bounty.jpg)

A security vulnerability in Apple’s browsers for macOS, iOS and iPadOS can lead to information disclosure, researchers have warned. Apple has just marked the issue as “resolved,” but it will take some time for the fixes to roll out, they said, so users should implement mitigations.


According to researchers at FingerprintJS, the bug is a same-origin policy violation. Typically, a web browser permits scripts on one web page to access data on a second web page only if both pages have the same origin/back-end server. Without this security policy in place, a snooper who manages to inject a malicious script into one website would be able to have free access to any data contained in other tabs the victim may have open in the browser, including access to online banking sessions, emails, healthcare portal data and other sensitive information.


In this case, the specific issue exists in Safari 15’s implementation of the IndexedDB API, researchers said in a [recent posting](https://fingerprintjs.com/blog/indexeddb-api-browser-vulnerability-safari-15/). If exploited, cyberattackers could use a malicious website to track a victim’s internet activity and could possibly uncover the user’s identity.


[![Password Management Webinar](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/12124026/specops_300x250_watch.jpg)](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)


“IndexedDB is a browser API for client-side storage designed to hold significant amounts of data,” explained researchers at Malwarebytes, in a [Wednesday overview](https://blog.malwarebytes.com/exploits-and-vulnerabilities/2022/01/browsers-on-ios-ipados-and-mac-leak-your-browsing-activity-and-personal-identifiers/) of the original analysis. “The researchers found that the current version of WebKit, the browser engine that powers Safari…can be tricked into skipping the same-origin check. To put it simply, the names of all IndexedDB databases are available to any site that you are visiting in the same session.”


While actual access to the content of each database is restricted, a malicious actor could still harvest information about what other websites a person visited in different tabs or windows, plus information about certain logged-in accounts (including Google accounts).


“Google services store an IndexedDB instance for each of your logged in accounts, with the name of the database corresponding to your Google User ID. This ID can be retrieved using this leak as well,” Malwarebytes researchers explained. They added, “authenticated users can be uniquely and precisely identified. This includes, for example, your Google profile picture, which can be looked up using an ID attached to certain sites’ IndexedDB caches.”


Put simply, malicious websites can learn a user’s identity and link it to multiple separate accounts that use the same ID (Gmail, Google Calendar, Google Keep, YouTube, Google Docs and so on, to continue the Google example), researchers warned. That makes the use of any stolen credentials that much more dangerous.


**Exploiting the Safari 15 Browser Bug**
----------------------------------------


Achieving a leak does not require any specific user action beyond visiting a malicious website, researchers warned.


“A tab or window that runs in the background and continually queries the IndexedDB API for available databases, can learn what other websites a user visits in real-time,” according to FingerprintJS. “Alternatively, websites can open any website in an iframe or pop-up window in order to trigger an IndexedDB-based leak for that specific site.”


Beyond Google sites, the firm found that users of at least 30 of the Alexa Top 1,000 most-visited websites could be likewise affected by the identity leakage.


“The results show that more than 30 websites interact with indexed databases directly on their homepage, without any additional user interaction or the need to authenticate,” FingerprintJS researchers noted. “We suspect this number to be significantly higher in real-world scenarios as websites can interact with databases on subpages, after specific user actions, or on authenticated parts of the page.”


The researchers [have created](http://www.safarileaks.com/) a proof-of-concept (PoC) demo that demonstrates how a malicious website can learn the Google account identity of any visitor.


**How to Protect Against Apple Leakage**
----------------------------------------


Apple engineers began working on the bug on Sunday, according to FingerprintJS, which reported that they have so far [merged potential fixes](https://github.com/WebKit/WebKit/commit/f73005ed826014988f8ee447de23927749fb56e5). No CVE has been issued.


“However, the bug continues to persist for end users until these changes are released,” researchers warned.


In the meantime, there are only a few steps that users can take to fend off any attacks. The first is to only visit trusted websites – though even the most secure could potentially suffer code injection via cross-site scripting (XSS) or other means (though the risk is much lower).


Beyond that, private-mode sessions in Safari 15 are restricted to a single tab, which reduces the extent of information available via the leak. Similarly, a user could simply make sure to only have one tab open at a time. Nonetheless, if a user visits “multiple different websites within the same tab, all databases these websites interact with are leaked to all subsequently visited websites,” warned the firm.


Another alternative for Safari users on Macs is to simply switch to a different browser – though iOS and iPadOS users are out of luck since all browsers in iPhone/iPad are affected.


“Unfortunately, there isn’t much Safari, iPadOS and iOS users can do to protect themselves without taking drastic measures,” FingerprintJS concluded. “The only real protection is to update your browser or OS once the issue is resolved by Apple.”


Apple did not immediately return a request for comment.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=CALENDAR]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Finance]] [[victim.industry.name=Healthcare]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Websites]] [[Google]] [[Fingerprintjs]] [[Website]] [[Indexeddb]] [[Ipados]] [[Api]] [[“the]] [[ThreatPost]]

