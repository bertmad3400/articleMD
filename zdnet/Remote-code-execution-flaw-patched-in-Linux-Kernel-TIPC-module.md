# Remote code execution flaw patched in Linux Kernel TIPC module
### The bug was spotted within a year of introduction to the codebase.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/remote-code-execution-flaw-patched-in-linux-kernel-tipc-module/)
+ Date: November 4, 2021
+ Author: Charlie Osborne


## Article:
Unknown

A code execution vulnerability has been patched in the TIPC module of the Linux Kernel.


The Transparent Inter Process Communication ([TIPC](https://www.kernel.org/doc/html/latest/networking/tipc.html)) module has been designed to facilitate intra-cluster communication across Ethernet or UDP connections and is capable of service addressing, tracking, managing communication between nodes, and more. 

This protocol is implemented in a kernel module package with major Linux distros.  

On Thursday, SentinelOne [researchers said](https://www.sentinelone.com/labs/tipc-remote-linux-kernel-heap-overflow-allows-arbitrary-code-execution/) that [CodeQL](https://codeql.github.com) has been used recently in bug hunting investigations on open source projects. CodeQL is a semantic code analysis engine that allows users to query code "as if it were data," and it was this tool that allowed the team to find a severe bug in the TIPC module project.  

According to the researchers, a heap overflow vulnerability was uncovered that could be exploited either locally or remotely to gain kernel-level privileges, "allowing an attacker to not just compromise a single service but the entire system itself." 

SentinelOne found a feature introduced in September 2020 as part of the TIPC module roadmap, a new user message type called MSG\_CRYPTO, was the source of the issue.  

While the module correctly validates Message and Header sizes against packet lengths received, there is a lack of validation for the keylen member of the MSG\_CRYPTO message and the size of key algorithm names. 






"This means that an attacker can create a packet with a small body size to allocate heap memory, and then use an arbitrary size in the keylen attribute to write outside the bounds," the researchers explained. "This vulnerability can be exploited both locally and remotely." 

"While local exploitation is easier due to greater control over the objects allocated in the kernel heap, remote exploitation can be achieved thanks to the structures that TIPC supports." 

The security flaw impacts kernel version 5.10. 

There is currently no evidence of in-the-wild abuse and it should also be noted that while the module is included with major distributions, it has to be loaded for the protocol to be enabled -- and so only builds with this feature active may be vulnerable to exploit.  

SentinelOne reported the flaw to the Kernel.org team on October 19. A patch was finalized by the module's maintainers by October 21 and released on [lore.kernel.org](http://lore.kernel.org/) four days later. The fix has now also been added to the mainline repository, released on October 29 under version 5.15.  

###  Previous and related coverage

* [FontOnLake malware strikes Linux systems in targeted attacks](https://www.zdnet.com/article/fontonlake-malware-strikes-linux-systems-in-targeted-attacks/)
* [Linux Foundation adds software supply chain security to LFX](https://www.zdnet.com/article/linux-foundation-adds-software-supply-chain-security-to-lfx/)
* [Microsoft repents of its open-source .NET blunder](https://www.zdnet.com/article/microsoft-repents-of-its-open-source-net-blunder/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[TIPC]] [[Linux]] [[SentinelOne]] [[ZDNet]]
