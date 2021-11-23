# Ethical Hacking, book review: A hands-on guide for would-be security professionals
### Daniel G Graham's book won't help hackers, who already have a wide range of tools to attack networks and devices. But it will help defenders who want to turn those techniques to more benevolent use.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/ethical-hacking-book-review-a-hands-on-guide-for-would-be-security-professionals/)
+ Date: November 23, 2021
+ Author: Mary Branscombe


## Article:
Unknown

[![ethical-hacking-book-main.jpg](https://www.zdnet.com/a/img/resize/5c9decdd0a3da3c9e818acdf13d93e341a3d72fe/2021/11/23/c656648b-123a-488e-a105-80d5a4f7a5fd/ethical-hacking-book-main.jpg?width=370&fit=bounds&auto=webp)](https://www.penguinrandomhouse.com/books/690696/ethical-hacking-by-daniel-graham/)Ethical Hacking: A Hands-on Introduction to Breaking In • By Daniel G Graham • No Starch Press • 376 pages • ISBN 9781718501874 • £41.99 / $49.99   

The parlous state of software and IT infrastructure security is also a career opportunity, with malware analysts, security researchers, penetration testers and red teams all in demand. Defenders need to know how attackers think, and what tools they use, so they can assess their own infrastructure for vulnerabilities and learn to detect malicious activity in the network.  

In [*Ethical Hacking: A Hands-on Introduction to Breaking In*](https://www.penguinrandomhouse.com/books/690696/ethical-hacking-by-daniel-graham/), Daniel G Graham sets out to deliver a practical guide for learning hacking techniques, and you jump straight into the hands-on guide by creating a set of Linux VMs to host the environment you're going to break into (since you can't ethically hack someone else's environment). You then work through some known vulnerabilities, progressing to capturing traffic, building a botnet and a ransomware server, generating phishing emails and deepfakes.  

Although you'll need to know how to write and run Python code, you don't need a great deal of expertise to get started because the step-by-step instructions are clear and detailed. Along the way, complex concepts are explained well: if you want to execute ransomware or try to bypass [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security), you need to understand encryption first, you need to understand syscalls and the underpinnings of Linux for rootkits, and likewise hashing for cracking passwords. 


Graham steps through common hacking techniques, creating deepfake video and audio, exploring how publicly available information is interconnected with [Maltego](https://www.maltego.com/) to reveal information about an organisation's staff and infrastructure, downloading databases of cracked and breached passwords, looking for exposed vulnerable devices with [Masscan](https://github.com/robertdavidgraham/masscan), [Shodan](https://www.shodan.io/) and [Nessus](https://www.tenable.com/lp/campaigns/19/try-nessus/), building Trojans and Linux rootkits (you'll need to know C coding for this), using SQL injection to extract usernames and passwords from websites, cross-site scripting attacks and privilege escalation once you get into a network. You're unlikely to discover your own zero days, but you will learn fuzzing, and how to exploit the [OpenSSL Heartbleed](https://heartbleed.com/) vulnerability. 

Along the way, Graham introduces other hacking tools like [King Phisher](https://github.com/securestate/king-phisher), the [swaks](https://www.kali.org/tools/swaks/) SMTP auditing tool in Kali Linux, [John the Ripper](https://www.openwall.com/john/) for password cracking, [Hydra](https://www.kali.org/tools/hydra/) for automating brute force password attacks and many others.  

The chapter on attacking domain servers, Active Directory and Kerberos on large Windows networks could probably be expanded to fill a book of its own, but if you're a Windows network admin and you don't already know how to use [Mimikatz](https://github.com/gentilkiwi/mimikatz), even this quick survey of the approaches hackers will take should be something of a wake-up call. (Microsoft has extensive guidance on remediating many of the issues covered here.)  

While this book will help even a relative beginner to become familiar with a wide range of tools that are useful to hackers, it is -- as promised -- a hands-on introduction. Readers will be in a position to explore further, and the final chapter talks you through hardening a hosted VM that you can use for actual ethical hacking. It also mentions some tantalising advanced targets like industrial systems and cellular infrastructure, although readers won't immediately be in a position to go after those without doing quite a bit of extra work.  






Even if you don't plan to do any active ethical hacking, it should be a salutary warning to anyone in IT that hacking tools are both sophisticated and widely available. There are plenty of tutorials aimed at using them maliciously, so the detail in this book doesn't increase the risk to those with vulnerable systems. If you do want to pursue this as a career, *Ethical Hacking* will guide you through the first steps.  

**Read more book reviews** 

* [The New Breed book review: Use animals, not humans, as the model for robots](https://www.zdnet.com/article/the-new-breed-book-review-use-animals-not-humans-as-the-model-for-robots/)
* [Exponential, book review: Technology acceleration and its impact on society](https://www.zdnet.com/article/exponential-book-review/)
* [TikTok Boom, book review: The rise and rise of YouTube's younger, hipper competitor](https://www.zdnet.com/article/tiktok-boom-book-review-the-rise-and-rise-of-youtubes-younger-hipper-competitor/)
* [Social Warming, book review: Temperature rising, regulation required](https://www.zdnet.com/article/social-warming-book-review/)
* [The Token Woman, book review: How to handle common workplace irritations](https://www.zdnet.com/article/the-token-woman-book-review-how-to-handle-common-workplace-irritations/)





#### Tags:
[[review:]] [[Linux]] [[ZDNet]]
