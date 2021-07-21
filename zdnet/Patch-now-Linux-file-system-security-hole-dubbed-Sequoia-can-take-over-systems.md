# Patch now: Linux file system security hole, dubbed Sequoia, can take over systems
### This Linux kernel's filesystem security vulnerability can enable any user to grab root privileges.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/patch-now-linux-file-system-security-hole-dubbed-sequoia-can-take-over-systems/)
+ Date: July 21, 2021 -- 20:00 GMT (21:00 BST)
+ Author: Steven J. Vaughan-Nichols


## Article:
Unknown

Some days, it doesn't rain, it pours. That's the case with Linux today. Not one, but two serious security holes have recently been exposed. First, there was a [systemd bug which could easily knock out systems](https://www.zdnet.com/article/nasty-linux-systemd-security-bug-revealed/). Now there's this security hole in the Linux kernel's file system, which any user could use to take over a computer. Like I said, some days it just pours.


The [Qualys Research Team](https://www.qualys.com/research/security-advisories/), which uncovered the file system bug, also discovered a size\_t-to-int type conversion vulnerability in the Linux kernel's filesystem. This [Linux security hole has been named Sequoia](https://blog.qualys.com/vulnerabilities-threat-research/2021/07/20/sequoia-a-local-privilege-escalation-vulnerability-in-linuxs-filesystem-layer-cve-2021-33909) and it's been designated [CVE-2021-33909](https://nvd.nist.gov/vuln/detail/CVE-2021-33909).

Doesn't sound like much, does it? Au contraire! It can be used against most Linux distributions in their default configurations. And, worse still, any -- I repeat, any -- unprivileged user can abuse it to gain root privileges.

Here's how it works. We all use filesystems every day, but you probably don't think about how it works. Who, except for developers, does? In Linux's case, the file system interface is implemented in a three-layered architecture. There's the user interface layer; the file system implementation; and the storage device drivers. 

Within the Linux kernel's seq\_file interface produces virtual files containing sequences of records. Each record must fit into a seq\_file buffer. When it runs out of space, it's just enlarged by doubling its size. That's not a problem. You'll run out of memory long before you can hack the system with this. The problem shows up because this size\_t variable is also passed to functions whose size argument is a signed 32-bit integer, not a size\_t. And that, my friend, while a very large number, can be overrun. 

Then, as Bharat Jogi, Qualys' Senior Manager of Vulnerabilities and Signatures, explains, "If an unprivileged local attacker creates, mounts, and deletes a deep directory structure whose total path length exceeds 1GB, and if the attacker open()s and read()s /proc/self/mountinfo, then" through a series of other maneuvers you can write to out of bounds memory. 

And, with that, you can corrupt data, crash the system, or, worst of all, execute unauthorized code. Alas, there are numerous known hacks that use memory overruns to become the root user and grab control of a computer. 






In fact, that's exactly what Qualys security team did. They developed an exploit, which they then used to obtain full root privileges on default installations of [Ubuntu](https://ubuntu.com/) 20.04, Ubuntu 20.10, Ubuntu 21.04, [Debian](https://www.debian.org/) 11, and [Fedora](https://getfedora.org/) 34. OK, let's just admit it. Pretty much any Linux distro is vulnerable to this trick.

Is this a great day to be a Linus sysadmin or what?

The good news is that while this problem is alive and nasty in any system running the Linux kernel 3.16 through 5.13.x before 5.13.4, patches are available. In fact, I patched my [Linux Mint](https://linuxmint.com/) desktop for it, before I even started to write this story. Yes, it's that bad. 

Eric Sandeen, [Red Hat](https://www.redhat.com/en)'s top file system developer, came up with a fix for the problem. 

Greg Kroah-Hartman, the Linux kernel maintainer for the Linux stable branch, subsequently released the [kernel patch for Sequoia](https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.13.4) on July 20th in the Linux kernel 5.13.4 release.

If you can't upgrade your kernel, you can still mitigate the problem by setting /proc/sys/kernel/unprivileged\_userns\_clone to 0. This prevents an attacker from mounting a long directory in a user namespace. However, the attacker may still be able to mount a poisonously long directory via [Filesystem in Userspace (FUSE)](https://github.com/libfuse/libfuse). You should also set /proc/sys/kernel/unprivileged\_bpf\_disabled to 1. This prevents an attacker from loading an [eBPF](https://ebpf.io/) program into the kernel. However, there may be other ways to attack. The only sure way to stop this security hole in its track is to update your kernel. 

This fix is also available in most Linux distributions now. So, if you've been sitting on your hands and not updating your Linux computers, it's time to get off them and start typing in patching commands.

**Related Stories:**

* [Nasty Linux systemd security bug revealed](https://www.zdnet.com/article/nasty-linux-systemd-security-bug-revealed/)
* [Major Linux RPM problem uncovered](https://www.zdnet.com/article/major-linux-rpm-problem-uncovered/)  

* [CloudLinux releases UChecker security tool for Linux servers](https://www.zdnet.com/article/cloudlinux-releases-uchecker-security-tool-for-linux-servers/)  






#### Tags:
[[Linux]] [[Qualys]] [[Ubuntu]] [[13]] [[ZDNet]]
