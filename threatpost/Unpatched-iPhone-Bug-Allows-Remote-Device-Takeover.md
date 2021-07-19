# Unpatched iPhone Bug Allows Remote Device Takeover
### A format-string bug believed to be a low-risk denial-of-service issue turns out to be much nastier than expected.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167922)
+ Date: July 19, 2021  5:31 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/03/31152348/iphone-privacy.jpg)
A vulnerability in Apple iOS opens the door to remote code execution (RCE), researchers found. The assessment is a revision from a previous understanding of the flaw that viewed it as a low-risk (and [somewhat wacky](https://threatpost.com/iphone-wi-fi-weird-network/167075/)) denial-of-service (DoS) problem affecting iPhone’s Wi-Fi feature.


Apple fixed the original DoS issue with iOS 14.6, without issuing a CVE. But when ZecOps analyzed the bug, researchers found that it could be used for RCE without little interaction with the victim – and that the attack worked on fully patched iPhones.


A successful exploit of the bug, which ZecOps dubbed “WiFiDemon,” would allow an attacker to take over the phone, install malware and steal data. It’s expected to be patched in the next week or so, [according to some sources.](https://twitter.com/Chasapple/status/1416848570343297025)



**Format-String Woes**
----------------------


The original DoS issue is a string-format bug discovered by researcher Carl Schou, who found that connecting to an access point with the SSID “%p%s%s%s%s%n” would disable a device’s Wi-Fi.


String-format problems occur when operating systems mistakenly read certain characters as commands: In this case, the “%” combined with various letters.


“My iPhone permanently disabled it’s [sic] Wi-Fi functionality,” Schou wrote in his writeup, in June. “Neither rebooting nor changing SSID fixes it :~)”


It can, however, be fixed by resetting the Wi-Fi feature in settings – something that wipes out all saved passwords, but which will restore Wi-Fi connections.


ZecOps said that a user would need to connect to a malicious access point for the bug to be exploited. But for earlier iPhone releases, there’s no need to lure a victim in: The Auto Join feature is turned on by default on iPhones, allowing them to automatically connect to available Wi-Fi networks in the background. Thus, an attacker would only need to set up an open, non-password-required malicious SSID within range of the target, and then sit back and wait.


An anonymous researcher was credited with finding the zero-click aspect of the bug, [a fix for which](https://support.apple.com/en-us/HT212146) occurred in iOS 14.4.


At the time of Schou’s writeup, Dirk Schrader, global vice president at New Net Technologies, predicted that the bug would inspire threat actors to dig “deeper into the inner workings of Apple’s Wi-Fi stack” to find out “what, exactly, causes the behavior and how to exploit it.” That prediction turned out to be true.


**Achieving Remote Code Execution**
-----------------------------------


ZecOps researchers explained that while further probing the bug, they discovered that an RCE weakness exists within “wifid,” a system daemon that handles protocols associated with Wi-Fi connections (“wifid” and “daemon” are the genesis of the name of the bug, as an aside.) Wifid runs as root, researchers said.


They issued a few technical details on a potential exploit path. To use the bug for RCE, an attacker can set up a series of Wi-Fi hotspots with names containing “%@.” The character combo is uniquely used by the Objective-C programming language for commands.


The exploit opportunity, researchers said, is to use an object in memory that has been released on the stack, alter the content of that memory using a spray method, and then use %@ to treat it as an Objective-C object, “like a typical use-after-free [(UAF) vulnerability] that could lead to code execution.”


[UAF bugs](https://encyclopedia.kaspersky.com/glossary/use-after-free/) are related to incorrect use of dynamic memory during program operation. If after freeing a memory location, a program does not clear the pointer to that memory, an attacker can use the error to hack the program.


Researchers were able to accomplish a proof-of-concept attack using a beacon-flooding approach for spraying, which “broadcasts countless beacon frames and results in many access points appearing on the victim’s device.”


They carried out the whole attack using a $10 a wireless dongle and a Linux virtual machine.


**How to Protect Against Wi-Fi Proximity Attacks**
--------------------------------------------------


So far, Apple hasn’t issued a patch for the RCE part of the bug. And while ZecOps hasn’t seen any attacks in the wild yet, researchers expect that to change.


“Since this vulnerability was widely published, and relatively easy to notice, we are highly confident that various threat actors have discovered the same information we did, and we would like to encourage an issuance of a patch as soon as possible,” they said.


In the meantime, users can disable the Wi-Fi Auto-Join feature via Settings->WiFi->Auto-Join Hotspot->Never. Also, iPhone enthusiasts should avoid connecting to unknown Wi-Fi hotspots in general, and especially any that contain the “@” symbol to avoid this specific attack.


Apple did not immediately return a request for comment.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


 




#### Tags:
[[Wi-Fi]] [[RCE]] [[ZecOps]] [[iPhone]] [[Schou]] [[SSID]] [[ThreatPost]]
