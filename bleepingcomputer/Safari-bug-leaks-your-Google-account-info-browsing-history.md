# Safari bug leaks your Google account info, browsing history
### There's a problem with the implementation of the IndexedDB API in Safari's WebKit engine, which could result in leaking browsing histories and even user identities to anyone exploiting the flaw.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/safari-bug-leaks-your-google-account-info-browsing-history/
+ Date: 2022-01-17T08:47:31-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/05/08/data-leak-hose.jpg)

![leak](https://www.bleepstatic.com/content/hl-images/2021/05/08/data-leak-hose.jpg?rand=1718541194)


There's a problem with the implementation of the IndexedDB API in Safari's WebKit engine, which could result in leaking browsing activity in real-time and even user identities to anyone exploiting this flaw.


IndexedDB is a widely used browser API that is a versatile client-side storage system with no capacity limits.


It is typically deployed for caching web application data for offline viewing, while modules, dev tools, and browser extensions can also use it to store sensitive information.


To prevent data leaks from cross-site scripting attacks, IndexedDB follows the "same-origin" policy, controlling which resources can access each piece of data.


However, FingerprintJS analysts discovered the IndexedDB API doesn't follow the same-origin policy in the WebKit implementation used by Safari 15 on macOS, leading to the disclosure of sensitive data.


This privacy violation bug also impacts web browsers using the same browser engine in the latest iOS and iPadOS versions.


The problem in Safari 15
------------------------


By violating the same-origin policy, the implementation of IndexedDB in Safari 15 on iOS, iPadOS, and macOS allows any website to draw the database names created in the same session.


Since the database names are typically unique and website-specific, this is essentially like leaking the browsing history to anyone.


To make matters worse, some database names feature user-specific identifiers (after login), so this API leak could potentially lead to user identification.



Impact and mitigation
---------------------


According to the analysts, identifying someone through this flaw requires logging in and visiting popular websites such as YouTube and Facebook, or services like Google Calendar, and Google Keep.


Logging in on these sites creates a new IndexedDB database and appends the Google User ID on its name. When multiple Google accounts are used, individual databases are created for each of them.


"We checked the homepages of Alexa's Top 1000 most visited websites to understand how many websites use IndexedDB and can be uniquely identified by the databases they interact with," mentions [the FingerprintJS report](https://fingerprintjs.com/blog/indexeddb-api-browser-vulnerability-safari-15/).


"The results show that more than 30 websites interact with indexed databases directly on their homepage, without any additional user interaction or the need to authenticate."


"We suspect this number to be significantly higher in real-world scenarios as websites can interact with databases on subpages, after specific user actions, or on authenticated parts of the page."


In some cases where subresources create UUID (universally unique identifiers) databases, Safari's tracking prevention systems intervene to block the leak of information. This positive side-mitigation effect is further enhanced if ad-blocking extensions are used.


The private mode in Safari 15 is still affected, but each browsing session is restricted to a single tab. Hence, the extent of information that could be potentially leaked is at least limited to websites visited through that one tab.


Note that since this is a problem in WebKit, any browser using this particular engine (e.g., Brave or Chrome for iOS) is also vulnerable.


To determine the bug's impact on your browser, you may visit [this demonstration page](https://safarileaks.com/), which reproduces the API leak.



![Safari on iPadOS 15.2 leaking browsing history](https://www.bleepstatic.com/images/news/u/1220909/Website%20snaps/example.png)*Safari on iPadOS 15.2 leaking browsing history (Bleeping Computer)*
The vulnerability was reported to WebKit Bug Tracker on November 28, 2021, and at the time of writing this, it's still unaddressed.


One way to mitigate the problem until security updates become available is to block all JavaScript, but this is a drastic measure bound to cause functionality issues on many web pages.


Switching to a non-WebKit-based web browser is the only viable solution, but it only applies to macOS. On the iOs and iPadOS, all web browsers are affected.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=CALENDAR]] [[action.malware.name=Elise]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Indexeddb]] [[Websites]] [[Api]] [[Webkit]] [[Ipados]] [[Google]] [[Same-origin]] [[Macos]] [[Bleeping Computer]]

