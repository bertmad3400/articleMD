# Signal fixes bug that sent random images to wrong contacts
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/signal-fixes-bug-that-sent-random-images-to-wrong-contacts/)
+ Date: July 26, 2021
+ Author: Ax Sharma


## Article:
![signal](https://www.bleepstatic.com/content/hl-images/2021/01/08/Signal.jpg)


Signal has fixed a serious bug in its Android app that, in some cases, sent random unintended pictures to contacts without an obvious explanation.


Although the issue was reported in December 2020, given the difficulty of reproducing the bug, it isn't until this month that a fix was rolled out to the Android users of the end-to-end encrypted messaging app.



Random images sent out to wrong contacts
----------------------------------------


This month Signal patched a bug affecting their Android app users under some circumstances.


When sending an image using the Signal Android app to one of your contacts, the contact would occasionally receive not just the selected image, but additionally a few random, unintended images, that the sender had never sent out.


An example screenshot below demonstrates how the sender (left) merely sent a GIF as a part of a text conversation, but the recipient (right) got two additional images with no plausible explanation: 



![signal app bug](https://www.bleepstatic.com/images/news/u/1164866/2021/Jul-2021/signal-app-bug/signal-screenshot-bug.jpg)**A Signal user (left) sent one GIF to a contact who received multiple, unintended images (right)**
The issue was first reported in December 2020 by Rob Connolly on the app's [GitHub](https://github.com/signalapp/Signal-Android/issues/10247) page. Other users gradually stepped in confirming Connolly's findings.


Connolly also stated that considering the sender had not sent out the additional images, this was either the case of messages getting "crossed over" from another contact of the recipient or worse, from an unknown party.


Luckily, in the example shown above, the exposed images were not of a sensitive nature.


February this year, another technologist confirmed the issue:


"Sorry for the bump but I wanted to say this is happening consistently for me now."


"Anytime I send images or links (with a preview), other images or images from link previews are sent to the other party as well (regardless if they were privy to the previous images)."


"It's gotten to the point where I send the images to my desktop via '*note to self*' (which exhibits the same behavior) and then I download the image and send it along to the correct person," said Christopher M. Hobbs in the same [thread](https://github.com/signalapp/Signal-Android/issues/10247#issuecomment-770536908).


Bug caused by "rare intersection" of database properties
--------------------------------------------------------


Following the initial December 2020 report, Signal's team immediately stepped in requesting logs, in order to debug and remediate the issue.


But, it took quite some time and effort to effectively reproduce the issue.


As such, it isn't until this month that a fixed version of the Signal Android app was rolled out.


"This is crazy. This bug should be the number 1 priority for Signal right now and yet all they do is ask for logs and make enhancements that aren't anywhere near as important as fixing this. This is a bug that should kill Signal, honestly," [complained](https://github.com/signalapp/Signal-Android/issues/10247#issuecomment-886203550) pseudonymous security and privacy advocate *InfiniteLight*.


Another user, Adrian Ostrowski [expressed](https://github.com/signalapp/Signal-Android/issues/10247#issuecomment-765492216) that a bug like this effectively made it impossible to share images confidentially via Signal.


To which Signal's Android developer Greyson Parrelli responded that a fix had been rolled out in version 5.17 of the Signal Android app, released this month.


Parelli also stepped in on a YCombinator Hacker News thread stating Signal takes bugs like these [very seriously](https://news.ycombinator.com/item?id=27951708):


"We do, in fact, take issues like this very seriously. This bug was extraordinarily rare, and because we have no metrics/remote log collection, there was an initial period where we had to spend time adding logging and collecting user-submitted logs to try to track it down."


"As soon as we were able to pick up a scent, it was all we worked on, and we were able to get a fix out very quickly," said the developer.



![signal play store release](https://www.bleepstatic.com/images/news/u/1164866/2021/Jul-2021/signal-app-bug/signal-play-store.jpg)**Google Play store shows the latest version 5.17.3 was released July 19th, 2021**
For those interested, the issue stemmed from the "ID" fields not being set to [auto-increment](http://www.sqlite.org/autoinc.html) in the SQLite database tables used by the app.


The fix commits [[1](https://github.com/signalapp/Signal-Android/commit/83086a5a2b8cae3ac40dea75d8c9533457a31858), [2](https://github.com/signalapp/Signal-Android/commit/b9657208fea1c7bcfb90b7400037a7858ba56516)] shared by Signal show "AUTOINCREMENT" has now been added to a few tables that needed the property:



![fix commit snippet](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**The fixes added "AUTOINCREMENT" keyword to ID field** (GitHub)
"For some background, this bug came about as a rare intersection of some database properties and a separate bug."


"The TL;DR is that if someone had conversation trimming on, it could create a rare situation where a database ID was re-used in a way that could result in this behavior."


"It was very difficult to track down, with earlier phases involving getting additional logging into builds."


"Once we had some more information, it did in fact become our top priority, a fix was made, and we got it out as quickly and as safely as possible. The fix itself should make it so that database issues like the one that caused this bug can't happen again," concluded Parelli in his response on GitHub.


At this time, the issue seems to have only impacted the Android version of the app.


Signal Android app users should update to the latest version of the app, available on Google Play store.




#### Tags:
[[Android]] [[Connolly]] [[GitHub]] [[Bleeping Computer]]
