# Critical Linux Kernel Bug Allows Remote Takeover
### The bug (CVE-2021-43267) exists in a TIPC message type that allows Linux nodes to send cryptographic keys to each other.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176000)
+ Date: November 4, 2021  11:50 am
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/04112500/popcorn-e1636039519750.jpg)
A critical heap-overflow security vulnerability in the Transparent Inter Process Communication (TIPC) module of the Linux kernel could allow local exploitation and remote code execution, leading to full system compromise.


TIPC is a peer-to-peer protocol used by nodes within a Linux cluster to communicate with each other in an optimized way; [it enables](https://www.kernel.org/doc/html/latest/networking/tipc.html) various types of messages that are used for different purposes. According to SentinelOne’s SentinelLabs, the bug in question (CVE-2021-43267) specifically resides in a message type that allows nodes to send cryptographic keys to each other. When received, the keys can be used to decrypt further communications from the sending node.


**TIPC: Popping Open the Kernel**
---------------------------------


“When loaded by a user, [TIPC] can be used as a socket and can be configured on an interface…as an unprivileged user,” explained SentinelLabs researcher Max Van Amerongen, in a [Thursday posting](https://www.sentinelone.com/labs/tipc-remote-linux-kernel-heap-overflow-allows-arbitrary-code-execution/). “All message construction and parsing is performed in the kernel.” This makes it an ideal target for attack, he said.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


As for the heap overflow: When it comes to that message construction, every TIPC message has a common header format. According to the researcher, that common header contains a “header size” allocation, which is the actual header size shifted to the right by two bits; and a “message size” allocation that is equal to the length of the entire TIPC message. These two sizes are validated by the tipc\_msg\_validate function, he said.


“The message size is correctly validated as greater than the header size, the payload size is validated against the maximum user message size, and the message size is validated against the actual received packet length,” Van Amerongen said – so far, so good. However, a new message type was introduced in September 2020 that lacks such size validations, opening the door to a heap-overflow exploit.


The additional message type, “MSG\_CRYPTO,” allows peers to send cryptographic keys to each other, as mentioned. The messages contain the name of the key algorithm and the key itself, according to the analysis. The size allocation for this is the message size itself, minus the header size.


However, “there are no [size-validation] checks for either the [key length] or the size of the key algorithm name itself (TIPC\_AEAD\_ALG\_NAME) against the message size,” the researcher explained. “This means that an attacker can create a packet with a small body size to allocate heap memory, and then use an arbitrary size in the [key length (keylen)] attribute to write outside the bounds of this location.”


Also, the message-validation function only checks that the message size in the header is within the bounds of the actual packet: “That means that an attacker could create a 20-byte packet and set the message size to 10 bytes without failing the check,” Van Amerongen added.


**Patching the Linux Kernel**
-----------------------------


The bug affects Linux kernel versions between 5.10 and 5.15. It should be noted that while the TIPC module comes with all major Linux distributions, it’s not “on” by default and does need to be enabled in order for an implementation to be vulnerable to attack.


To protect themselves, affected Linux users should apply the [just-released patch](https://github.com/torvalds/linux/commit/fa40d9734a57bcbfa79a280189799f76c88f7bb0), which adds appropriate size-verification checks to the process.


The stakes are significant, the researcher warned: “While TIPC itself isn’t loaded automatically by the system but by end users, the ability to configure it from an unprivileged local perspective and the possibility of remote exploitation makes this a dangerous vulnerability for those that use it in their networks,” warned Van Amerongen. “What is more concerning is that an attacker that exploits this vulnerability could execute arbitrary code within the kernel, leading to a complete compromise of the system.”


Linux kernel bugs aren’t that common, but they do crop up occasionally. For instance, in April, an information-disclosure vulnerability (CVE-2020-28588) [was reported](https://threatpost.com/linux-kernel-bug-wider-cyberattacks/165640/) that could be exploited to expose information in the kernel stack memory of vulnerable ARM devices.


***Want to win back control of the flimsy passwords standing between your network and the next cyberattack? Join Darren James, head of internal IT at Specops, and Roger Grimes, data-driven defense evangelist at KnowBe4, to find out how during a free, LIVE Threatpost event,*** [***“Password Reset: Claiming Control of Credentials to Stop Attacks,”***](https://bit.ly/3bBMX30) ***on Wed., Nov. 17 at 2 p.m. ET. Brought to you by Specops.***


***[Register NOW](https://bit.ly/3bBMX30)******for the LIVE event and submit questions ahead of time to Threatpost’s Becky Bracken at <mailto:becky.bracken@threatpost.com>.***




#### Tags:
[[Linux]] [[TIPC]] [[ThreatPost]]
