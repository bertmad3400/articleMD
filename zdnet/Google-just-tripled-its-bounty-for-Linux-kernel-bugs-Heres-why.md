# Google just tripled its bounty for Linux kernel bugs. Here's why
### Linux is everywhere and it needs extra protection, according to Google.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/google-just-tripled-its-bounty-for-linux-kernel-bugs-heres-why/)
+ Date: November 2, 2021
+ Author: Liam Tung


## Article:
Unknown

Google has kicked off a special three-month bug bounty targeting flaws in the Linux kernel with triple the rewards for security researchers.

The new bounty, [announced this week](https://security.googleblog.com/2021/11/trick-treat-paying-leets-and-sweets-for.html), looks to harden the Linux kernel in specific edge cases. It's offering up to $31,337 ([Leet](https://en.wikipedia.org/wiki/Leet)) to security researchers who can exploit privilege escalation in Google's lab environment with a patched vulnerability; and $50,337 for anyone who can finds a previously undisclosed or zero-day flaw, or for discovering a new exploit technique. 


"We are constantly investing in the security of the Linux Kernel because much of the internet, and Google – from the devices in our pockets, to the services running on [Kubernetes](https://kubernetes.io/) in the cloud – depend on the security of it," said [Eduardo Vela from the Google Bug Hunters Team](https://security.googleblog.com/2021/11/trick-treat-paying-leets-and-sweets-for.html).

**SEE:** [**Ransomware: It's a 'golden era' for cyber criminals - and it could get worse before it gets better**](https://www.zdnet.com/article/ransomware-its-a-golden-era-for-cyber-criminals-and-it-could-get-worse-before-it-gets-better/)

The Linux kernel — [hatched as a hobby by Linus Torvalds in Helsinki 30 years ago](https://www.zdnet.com/article/linus-torvalds-on-linuxs-30th-birthday/) — now powers most of the top websites and internet infrastructure, from AWS to Microsoft Azure, Google, Facebook and Wikipedia.   

Google's base rewards for each publicly patched vulnerability is $31,337, capped at one exploit per vulnerability. However, the reward can go up to $50,337 if the bug was otherwise unpatched in the Linux kernel (a zero-day); or if the exploit uses a new attack or technique in Google's view.

"We hope the new rewards will encourage the security community to explore new Kernel exploitation techniques to achieve privilege escalation and drive quicker fixes for these vulnerabilities," Vela said.






He adds that "the easiest exploitation primitives are not available in our lab environment due to the hardening done on [Container-Optimized OS](https://cloud.google.com/container-optimized-os/docs)." This is a Chromium-based OS for Google Compute Engine virtual machines that's built to run on Docker containers. 

However, since this three month bounty complements Android's VRP rewards, exploits that work on Android could also be eligible for up to [$250,000](https://bughunters.google.com/about/rules/6171833274204160) (that's in addition to this program).

The Google environment has some specific requirements that were demonstrated by Google security engineer, Andy Nguyen, who [found the 15-year-old BleedingTooth bug (CVE-2021-22555) in Linux's Bluetooth stack](https://www.zdnet.com/article/google-warns-of-severe-bleedingtooth-bluetooth-flaw-in-linux-kernel/). 

**SEE:** [**Cloud security in 2021: A business guide to essential tools and best practices**](https://www.zdnet.com/article/cloud-security-in-2021-a-business-guide-to-essential-tools-and-best-practices/)

That bug was a heap out-of-bounds write vulnerability in Linux Netfilter that could bypass all modern security mitigations, achieve kernel code execution, and could break the Kubernetes pod isolation of the [kCTF (capture the flag) cluster](https://google.github.io/kctf/vrp.html) used for security competitions. Nguyen [details his work in a writeup on GitHub](https://github.com/google/security-research/blob/master/pocs/linux/cve-2021-22555/writeup.md). 

Vela recommends that participants also include a patch if they want extra cash via its Patch Reward Program.

Given the nature of open-source software development, Google notes that it doesn't want to receive details about unpatched vulnerabilities before they've been publicly disclosed and patched. Researchers need to provide exploit code and the algorithm used to calculate the identifier. It would, however, like to receive a rough description of the exploit strategy. 





#### Tags:
[[Google]] [[Linux]] [[ZDNet]]
