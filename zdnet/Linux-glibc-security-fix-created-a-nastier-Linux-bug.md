# Linux glibc security fix created a nastier Linux bug
### Sometimes a programming cure is worse than the disease. That's the case with this Linux glibc security bug.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/linux-glibc-security-fix-created-a-nastier-linux-bug/)
+ Date: August 16, 2021 -- 20:27 GMT (21:27 BST)
+ Author: Steven J. Vaughan-Nichols


## Article:
Unknown

The [GNU C Library (glibc)](https://www.gnu.org/s/libc/) is essential to Linux. So, when something goes wrong with it, it's a big deal. When a fix was made in early June for a relatively minor problem, [CVE-2021-33574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33574), which could result in application crashes, this was a good thing. Unfortunately, it turned out the fix introduced a new and nastier problem, [CVE-2021-38604](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-38604). It's always something!


The first problem wasn't that bad. As Siddhesh Poyarekar, a [Red Hat](https://www.redhat.com/en) principal software engineer wrote, "In order to [mount a minimal attack using this flaw, an attacker needs many pre-requisites](https://sourceware.org/bugzilla/show_bug.cgi?id=27896#c4) to be able to even crash a program using this mq\_notify bug." Still, it needed patching and so it was fixed. Alas, the fix contained an even nastier bug.

While checking the patch, Nikita Popov, a member of the [CloudLinux](https://www.cloudlinux.com/) [TuxCare Team](https://tuxcare.com/), found the problem. It turns out that it is possible to cause a situation where a [segmentation fault could be triggered within the library](https://blog.tuxcare.com/cve/tuxcare-team-identifies-cve-2021-38604-a-new-vulnerability-in-glibc). This can lead to any application using the library crashing. This, of course, would cause a Denial-of-Service (DoS) issue. This problem, unlike the earlier one, would be much easier to trigger. Whoops.

Red Hat gives the problem in its [Common Vulnerability Scoring System (CVSS) a score of 7.5](https://access.redhat.com/security/cve/cve-2021-38604), which is "high." An attack using it would be easy to build and requires no privileges to be made. In short, it's bad news. 

Popov himself thinks "every Linux application including interpreters of other languages (python, PHP) is linked with glibc. It's the second important thing after the kernel itself, so the impact is quite high."

Popov found the problem while doing "his usual routine of porting CVE-2021-33574 fix to our supported distros."  He found that null pointers could be passed in certain situations. 

Technically, the problem lay in the 'mq\_' function family. These provide [POSIX](https://pubs.opengroup.org/onlinepubs/9699919799.2018edition/) compliant message queue application programming interface (API) functionality. Typically these are used for inter-process communications (IPC) processes. Every Linux application including interpreters of other languages (Python, PHP) is linked with glibc library.






Popov found "two situations where the Linux Kernel would use the message NOTIFY\_REMOVED while passing copied thread attributes along the way in the data.attr field. Unfortunately, a host application is able to pass a NULL value there if it wants glibc to spawn a thread with default attributes. In this case, glibc would dereference a NULL pointer in pthread\_attr\_destroy, leading to a crash of the entire process."

The C programmers among you are already closing their eyes and shaking their heads ruefully. One of the common rules of C programming is to [never, ever dereference a null pointer](https://cwe.mitre.org/data/definitions/476.html). The question isn't "Will it crash the program?" It's "How badly will it crash the program?"  

The good news is both the vulnerability and code fix have been submitted to the glibc development team. It has already been incorporated into upstream glibc.

In addition, a new test has been submitted to glibc's automated test suite to pick up this situation and prevent it from happening in the future. The bottom line is sometimes changed in unrelated code paths can lead to behaviors changing elsewhere without the programmer realizing what's going on. This test will catch this situation.

The Linux distributors are still working out the best way to deploy the fix. In the meantime, if you want to be extra careful -- and I think you should be -- you should upgrade to the newest stable version of glibc 2.34 or higher. 

**Related Stories:**

* [It's time to improve Linux's security](https://www.zdnet.com/article/a-call-to-improve-linuxs-security/)
* [Qualys partners with Red Hat to improve Linux and Kubernetes security](https://www.zdnet.com/article/qualys-partners-with-red-hat-to-improve-linux-and-kubernetes-security/)
* [Patch now: Linux file system security hole, dubbed Sequoia, can take over systems](https://www.zdnet.com/article/patch-now-linux-file-system-security-hole-dubbed-sequoia-can-take-over-systems/)





#### Tags:
[[Linux]] [[glibc]] [[problem,]] [[ZDNet]]
