# Telegram for Mac bug lets you save self-destructing messages forever
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/telegram-for-mac-bug-lets-you-save-self-destructing-messages-forever/)
+ Date: August 5, 2021
+ Author: Lawrence Abrams


## Article:
![Telegram](https://www.bleepstatic.com/content/hl-images/2021/08/05/telegram-lighter.jpg)


​Researchers have discovered a way for users on Telegram for Mac to keep specific self-destructing messages forever or view them without the sender ever knowing.


Telegram offers an optional 'Secret Chat' mode that increases the privacy of chats by enabling a variety of additional features.


When you start a Secret Chat with another Telegram user, the connection will become end-to-end encrypted, and all messages, attachments, and media will be set to automatically self-destruct and be removed from all devices after a certain period.


However, new bugs discovered by Reegun Richard Jayapaul, Trustwave SpiderLabs' Lead Threat Architect, allow Telegram for Mac users to save self-destructing messages and attachments forever.


When media files, other than attachments, are sent in a message, they are saved in a cache folder located at the following path, with the XXXXXX unique numbers associated with an account.


Telegram will not download attachments (documents like text, doc, or pdf files, and Audio and video) unless a recipient attempts to open them. This is likely done due to the larger size of attachments.


When a recipient reads the message or views the content, the self-destruct timer will start, and when finished, the content will be automatically be deleted.


However, Reegun discovered that the self-destructing media was not deleted from the cache folder, and a user could save it to another location on their hard drive.


This bug was fixed by Telegram for macOS in version 7.7 (215786) or later after it was responsibly reported, but there's an additional bug that lets you save self-destructible media.


Copying unopened self-destructing media
---------------------------------------


As voice recordings, video messages, images, or location sharing images are automatically downloaded to the cache, Reegun discovered that a user could simply copy the media from the cache folder before viewing it in the program.


"Bob sends a media message to Alice (whether voice recordings, video messages, images, or location sharing). Without opening the message, since it may self-destruct, Alice instead goes to the cache folder and grabs the media file," Reegun explains in his report.


"She can also delete the messages from the folder without reading them in the app. Regardless, Bob will not know whether Alice has read the message, and Alice will retain a permanent copy of the media."



![Accessing unopened Telegram media directly from the cache folder](https://www.bleepstatic.com/images/news/security/vulnerabilities/t/telegram/keep-self-destructing-media/telegram-cache.png)**Accessing unopened Telegram media directly from the cache folder**
Telegram told Reegun that this second bug would not be fixed as there is no way to protect against direct access to the app's folder.



> 
> "Please note that the primary purpose of the self-destruct timer is to serve as a simple way to auto-delete individual messages. However, there  are some ways to work around it that are outside what the Telegram app  an control (like copying the app’s folder), and we clearly warn users about such circumstances: <https://telegram.org/faq#q-can-telegram-protect-me-against-everything>" - Telegram.
> 
> 
> 


Reegun told BleepingComputer that he disagrees and that Telegram could fix the bug by treating all self-destructing media the same way as attachments and not download them to the local file system until they are opened.


In February, security researcher Dhiraj Mishra [discovered a similar vulnerability](https://www.bleepingcomputer.com/news/security/telegram-privacy-feature-failed-to-delete-self-destructing-video-files/) in the Secret Chat feature that caused self-destructing media not to be deleted from recipients' devices.


"This is a similar bug, but the media was left in an entirely different file location. This researcher’s findings were patched in Telegram v7.4, while our researcher’s findings weren’t fully patched until v7.7,"  Karl Sigler, Senior Security Research Manager, Trustwave SpiderLabs, told BleepingComputer. "It’s apparent that Telegram has a history of leaving these supposedly “Self-Destruct” media files behind."


BleepingComputer has contacted Telegram about the bug to ask why this fix is not being instituted but has not heard back.


A demonstration of how this bug works can be seen in the video below.





#### Tags:
[[self-destructing]] [[Reegun]] [[messages,]] [[self-destruct]] [[However,]] [[message,]] [[Bleeping Computer]]
