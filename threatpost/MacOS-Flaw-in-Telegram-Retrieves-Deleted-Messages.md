# MacOS Flaw in Telegram Retrieves Deleted Messages
### Telegram declined to fix a scenario in which the flaw can be exploited, spurring a Trustwave researcher to decline a bug bounty and to disclose his findings instead.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168412)
+ Date: August 5, 2021  11:26 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/05112428/delete-telegram-message-e1628177080885.jpg)
A vulnerability in a high-level privacy feature of [Telegram](https://threatpost.com/telegram-toxiceye-malware/165543/) on macOS that sets up a “self-destruct” timer for messages on both the sender’s and recipient’s devices can allow someone to retrieve these messages even after they’ve been deleted, a researcher has found.


Reegun Richard Jayapaul, [Trustwave](https://www.trustwave.com/en-us/) SpiderLabs Lead Threat Architect, discovered the flaw in the Self-Destruct feature of Telegram MacOS, which is part of the Secret-Chats aspect of the messaging app that uses end-to-end encryption.


This encryption – the key to which even Telegram administrators do not have – “is meant for people who are concerned about the security and privacy of their chat history,” he said in a [blog post about his findings](https://link.edgepilot.com/s/183e1c69/INyq1HnCIk_Zye4QR-mmUg?u=https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/telegram-self-destruct-not-always/) published Thursday.



Indeed, [Telegram](https://threatpost.com/telegram-triangulation-users-locations/162762/) in general is widely viewed as one of the more secure messaging apps; many users have opted to switch from Facebook’s WhatsApp to Telegram because they are concerned about their privacy.


Jayapaul worked with Telegram to patch the flaw, which can allow the privacy of users to be violated via two scenarios. In doing so, he said he learned of a caveat of the company’s vulnerability disclosure program that prevents researchers from disclosing a flaw if they agree to accept a bug bounty – something Jayapaul said he was not on board with.


In the first scenario, Shared Location, video and audio messages can leak even after the messages have been timed to self-destruct on both the sender’s and recipient’s device, he wrote. In the second scenario, these same messages can leak without a recipient even opening or deleting the message.


However, while Telegram fixed the issue creating the first scenario, the company declined to fix the second. Because of this, the Trustwave researcher declined the bug bounty from Telegram, as it “would have kept us from disclosing this research to the community,” Jayapaul wrote.


“We feel bug bounties that require permanent silence about a vulnerability do not help the broader community to improve their security practices and can serve to raise questions about what exactly the bug bounty is compensating the individual for – reporting a vulnerability to the bounty payer or their silence to the broader community,” he said. “This is especially serious in this case, where one of the issues reported went unaddressed.”


**How It Can Be Exploited**
---------------------------


Jayapaul discovered the flaw in macOS Telegram version 7.5, where any shared location, audio, video or documents sent via the app are stored in the Telegram cache in the following path: “/Users/Admin/Library/Group Containers/XXXXXXX.ru.keepcoder.Telegram/appstore/account-1271742300XXXXXX/postbox/media”.


Telegram stores the Secret-Chat in this directory with the prefix “secret-file-xxxxxx”. “By default, any media files, except attachments, sent to Telegram are downloaded to the above cache folder,” he explained in the post. “Shared locations are stored as a picture.”


In his disclosure, Jayapaul outlined in detail how the flaw can be exploited in the two scenarios – one that violates the privacy of both the sender and recipient of the messages or locations, the other in which just the sender is affected.


In the first scenario, someone sends a voice recording, video message or image, or shares his or her location, and then enables the “self-destruct” feature. Once the recipient reads the message, it does indeed get deleted according to how the feature works. “However, the files are still stored locally inside the cache folder available for recovery,” Jayapaul said.


The second scenario depends upon the recipient of the message going into the cache folder to grab the file that’s set to self-destruct, or deletes the messages without reading them within the Telegram app. Either way, the sender won’t know whether the message was read, and the recipient “will retain a permanent copy of the media,” according to the post.


**Telegram’s Response and Disclosure**
--------------------------------------


When Jayapaul contacted Telegram, the company quickly responded to fix the vulnerability in the first scenario, in which “any chats/media can be recovered from the cache even after they are supposedly self-deleted after opening the message in the app,” he wrote. While the initial fix didn’t apply to Shared Locations initially, the company eventually published a fix for this as well, he said.


The company declined to patch the caching issue in the second scenario as applied to media files, however, citing “some ways to work around” the self-destruct timer in the app “that are outside” what the app can control, Jayapaul wrote. Telegram acknowledged that it warns users about “such circumstances” on a [“FAQ” page](https://telegram.org/faq#q-can-telegram-protect-me-against-everything) on its website.


For his part, Jayapaul said he thinks the fix “would be a simple one” that needs only to apply the same caching method that the self-destruct chats use for attachments.


“If you attach media files to a message, the attachments cannot be accessed in the cache prior to clicking the message,” Jayapaul explained. “Only after the message is opened in the app are the attachments downloaded and then deleted after the timer.”


Telegram offered the researcher a bug bounty that he was “delighted” to receive, but he ultimately declined it because he chose to publish his findings.


“Public disclosure is an important part of the vulnerability discovery and remediation process,” Jayapaul said. “It is essential for the public in a variety of ways. Because of these concerns and my commitment to information security, I have declined the bug bounty in exchange for disclosure.”


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[Jayapaul]] [[scenario,]] [[wrote.]] [[said.]] [[self-destruct]] [[ThreatPost]]
