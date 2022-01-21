# Nasty Linux kernel bug found and fixed | ZDNet
### A heap overflow bug was recently discovered in the Linux kernel. The patch is available now in most major Linux distributions.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/nasty-linux-kernel-bug-found-and-fixed/
+ Date: 2022-01-21 12:23:32
+ Author: Steven Vaughan-Nichols


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/05ce9e2c4d28b1c4b3e0c154d2bbb2e1e2b84d79/2022/01/21/521374b7-5ef6-415f-883f-e322108a1f5b/linux-security.jpg?width=770&height=578&fit=crop&auto=webp)

Most reported Linux "security" bugs actually aren't Linux bugs. For example, security vendor [CrowdStrike](https://www.crowdstrike.com/)'s report on the biggest [Linux-based malware families](https://www.zdnet.com/article/linux-malware-is-on-the-rise-here-are-three-top-threats-right-now/) was really about system administration security blunders with telnet, SSH, and Docker, not Linux at all. But, that doesn't mean Linux doesn't have security holes.  For example, a new [nasty Linux kernel problem](https://seclists.org/oss-sec/2022/q1/54) has just popped up.  


In this one, there's a heap overflow bug in the legacy\_parse\_param in the Linux kernel's fs/fs\_context.c program. This parameter is used in Linux filesystems during superblock creation for mount and superblock reconfiguration for a remount. The superblock records all of a filesystem's characteristics such as file size, block size, empty and filled storage blocks. So, yeah, it's important. 

The legacy\_parse\_param() "PAGE\_SIZE - 2 - size" [calculation was mistakenly made an](https://www.spinics.net/lists/stable/msg526298.html) [unsigned type](https://www.spinics.net/lists/stable/msg526298.html). This means a large value of "size" results in a high positive value instead of a negative value as expected. Whoops. 

This, in turn, meant you copy data beyond the memory slab allocated for it. And, as all programmers know, writing beyond the memory your program is supposed to have access to is a terrible thing.

One big reason why [Rust is being incorporated into Linux](https://www.zdnet.com/article/rust-takes-a-major-step-forward-as-linuxs-second-official-language/) is that Rust makes this kind of memory mistake much harder to do. As every C developer knows, it's all too easy to trip over memory allocation in a C program. 

So, how bad is it? By the Common Vulnerability Scoring System (CVSS) v3.1 scoring test, it's a solid 7.7. That's considered a high-security vulnerability. 

A local attacker can use it to escalate their user privileges or crash the system. This can be done with a specially crafted program that triggers this integer overflow. That done, it's trivial to execute arbitrary code and give the attacker root privileges.






To exploit it requires the CAP\_SYS\_ADMIN privilege to be enabled. If that's the case,  an unprivileged local user can open a filesystem that does not support the File System Context application programming interface (API). In this situation, it drops back to legacy handling, and from there, the flaw can escalate an attacker's system privileges. 

Exploiting is not as hard to do as you might think. Its discoverer, Linux kernel developer William Liu reports he created exploits against [Ubuntu 20.04](https://releases.ubuntu.com/20.04/) and container escape exploits against Google's hardened [Container-Optimized (COS)](https://cloud.google.com/container-optimized-os/docs).

This security hole was introduced back on Feb 28, 2019, in the [Linux 5.1-rc1 kernel](https://github.com/torvalds/linux/commit/3e1aeb00e6d132efc151dacc062b38269bc9eccc#diff-c4a9ea83de4a42a0d1bcbaf1f03ce35188f38da4987e0e7a52aae7f04de14a05). It's now present in all Linux kernels. Yes, all of them. [Fortunately, the patch is in](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=722d94847de29310e8aa03fcbdb41fc92c521756).  

You can also disable it by disabling user namespaces by setting user.max\_user\_namespaces to with the following shell code on the [Red Hat](https://www.redhat.com/en) Linux family.

* echo "user.max\_user\_namespaces=0" > /etc/sysctl.d/userns.conf
* sysctl -p /etc/sysctl.d/userns.conf

On Ubuntu and related distros, you can protect your system with this shellcode:

* sysctl -w kernel.unprivileged\_userns\_clone=0

However, keep in mind that you must have namespace available on containerized Linux distros, such as [Red Hat OpenShift Container Platform](https://www.redhat.com/en/technologies/cloud-computing/openshift/container-platform) since it needs this functionality enabled. In these circumstances, you'll need to patch your Linux distro as soon as your distributor makes the patch available.

Stay safe, stay patched.

**Related stories:**

* [In 2022, security will be priority number one for Linux and open-source developers](https://www.zdnet.com/article/in-2022-security-will-be-linux-and-open-source-developers-job-number-one/).
* [It's time to improve Linux's security](https://www.zdnet.com/article/a-call-to-improve-linuxs-security/).
* [When open-source developers go bad](https://www.zdnet.com/article/when-open-source-developers-go-bad/).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Mis-Type]] [[action.malware.name=Net]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Linux]] [[ZDNet]]

