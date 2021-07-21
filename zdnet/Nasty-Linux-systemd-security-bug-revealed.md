# Nasty Linux systemd security bug revealed
### Qualsys has found an ugly Linux systemd security hole that can enable any unprivileged user to crash a Linux system. The patch is available, and you should deploy it as soon as possible.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/nasty-linux-systemd-security-bug-revealed/)
+ Date: July 20, 2021 -- 16:04 GMT (17:04 BST)
+ Author: Steven J. Vaughan-Nichols


## Article:
Unknown

[Systemd](https://www.freedesktop.org/wiki/Software/systemd/), the Linux system and service manager that has largely replaced [init](https://www.lifewire.com/how-to-use-the-init-command-in-linux-4066930) as the master Linux startup and control program, has always had its critics. Now, with [Qualys](https://www.qualys.com/)'s [discovery of a new systemd security bug](https://blog.qualys.com/vulnerabilities-threat-research/2021/07/20/cve-2021-33910-denial-of-service-stack-exhaustion-in-systemd-pid-1), systemd will have fewer friends. Successful exploitation of this newest vulnerability enables any unprivileged user to cause a denial of service via a kernel panic.  

In a phrase, "that's bad, that's really bad." 


As Bharat Jogi, Qualys's senior manager of Vulnerabilities and Signatures, wrote, "Given the breadth of the attack surface for this vulnerability, Qualys recommends users apply patches for this vulnerability immediately." You can say that again.  

Systemd is used in almost all modern Linux distributions. This particular security hole arrived in the systemd code in April 2015.  

It works by enabling attackers to misuse the alloca() function in a way that would result in memory corruption. This, in turn, allows a hacker to crash systemd and hence the entire operating system. Practically speaking, this can be done by a [local attacker mounting a filesystem on a very long path](https://access.redhat.com/security/cve/cve-2021-33910). This causes too much memory space to be used in the systemd stack, which results in a system crash.  

That's the bad news. The good news is that [Red Hat Product Security](https://access.redhat.com/security) and systemd's developers have immediately patched the hole.  

There's no way to remedy this problem. While it's not present in all current Linux distros, you'll find it in most distros such as the [Debian 10 (Buster)](https://www.debian.org/releases/buster/) and its relatives like [Ubuntu](https://ubuntu.com/) and [Mint](https://linuxmint.com/). Therefore, you must, if you value keeping your computers working, patch your version of systemd as soon as possible. You'll be glad you did. 

### **Related Stories:**

* [Major Linux RPM problem uncovered](https://www.zdnet.com/article/major-linux-rpm-problem-uncovered/)
* [CloudLinux releases UChecker security tool for Linux servers](https://www.zdnet.com/article/cloudlinux-releases-uchecker-security-tool-for-linux-servers/)
* [Linux kernel vulnerability exposes stack memory, causes data leaks](https://www.zdnet.com/article/linux-kernel-vulnerability-exposes-stack-memory/)





#### Tags:
[[systemd]] [[Linux]] [[Qualys]] [[ZDNet]]
