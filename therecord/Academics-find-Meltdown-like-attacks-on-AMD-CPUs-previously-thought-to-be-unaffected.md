# Academics find Meltdown-like attacks on AMD CPUs, previously thought to be unaffected
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/academics-find-meltdown-like-attacks-on-amd-cpus-previously-thought-to-be-unaffected/)
+ Date: October 13, 2021
+ Author: Catalin Cimpanu


## Article:
![Academics find Meltdown-like attacks on AMD CPUs, previously thought to be unaffected](https://therecord.media/wp-content/uploads/2021/10/AMD.jpg)

Two academic papers have been published over the past two months detailing new side-channel attacks in AMD processors that have eerily similar consequences to the Meltdown attack disclosed in early 2018, to which AMD CPUs were previously thought to be immune.


The original idea of the [Meltdown attack](https://meltdownattack.com/) was that malicious apps could abuse a CPU’s [speculate execution](https://en.wikipedia.org/wiki/Speculative_execution) operations to break the barrier between apps and the operating system kernel.


Academics said the attack could allow a malicious app to steal sensitive information from the kernel, such as passwords, encryption keys, and user data, information to which an app would normally not be able to access.


Initially, the team behind the Meltdown attack said their technique only worked against Intel processors and that AMD had used a different design for its speculate execution feature that was not vulnerable to their attack.


While later research found that Arm processors were also vulnerable, a classic Meltdown attack was never proven to be successful against AMD’s CPUs.


#### Two Meltdown-like attacks disclosed in AMD CPUs in two months


However, in a [paper](https://arxiv.org/abs/2108.10771) published in August, academics from the Technical University in Dresden, Germany, said that after more than three years, they found a way to attack AMD CPUs with what they called a Meltdown-like technique.


The attack, which is too complex to explain in this article, was found to work against AMD’s Zen processor line, but in a [security advisory](https://www.amd.com/en/corporate/product-security/bulletin/amd-sb-1010) last month, AMD admitted that all its CPUs were affected.


And if this wasn’t enough, a [second paper](https://cispa.de/en/research/publications/3507-amd-prefetch-attacks-through-power-and-time) published this month described a second method of launching Meltdown-like attacks against AMD CPUs.


This second technique, discovered by three of the researchers who found the original Meltdown attack back in 2018, abuses x86 PREFETCH instructions and has the same effect of leaking kernel address space information, the team explained.


Yesterday, AMD [confirmed](https://www.amd.com/en/corporate/product-security/bulletin/amd-sb-1017) this second attack as well and said that just like the issue disclosed in August, all AMD CPUs are vulnerable.


The chipmaker has not released any firmware patches for either of the two attacks —tracked as CVE-2020-12965 and CVE-2021-26318— but instead, it asked software developers to follow secure coding methodologies [[PDF](https://developer.amd.com/wp-content/resources/90343-D_SoftwareTechniquesforManagingSpeculation_WP_9-20Update_R2.pdf)], the [same advice](https://software.intel.com/content/www/us/en/develop/articles/software-security-guidance/secure-coding/security-best-practices-side-channel-resistance.html) that Intel has been giving since 2018.


It also needs to be said that despite being disclosed in early 2018, security researchers/firms have yet to see the Meltdown and Spectre attacks in any real-world scenarios.


However, as academics explained at the time, the attacks are “unlike usual malware” and would also be very hard to detect.





#### Tags:
[[AMD]] [[Meltdown-like]] [[The Record]]
