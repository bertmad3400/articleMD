# Get paid to improve Linux and open-source security
### The Linux Foundation and allies will pay developers to help secure Linux and open-source software programs.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/get-paid-to-improve-linux-and-open-source-security/)
+ Date: August 23, 2021 -- 21:11 GMT (22:11 BST)
+ Author: Steven J. Vaughan-Nichols


## Article:
Unknown

![paid-shutterstock-1369879709.jpg](https://www.zdnet.com/a/hub/i/r/2021/08/23/def9879d-80cb-4f10-90bb-de13495baf2f/resize/1200xauto/45df8db2cce2b07c10b57624dcfadee2/shutterstock-1369879709.jpg)Linux and open-source software are much easier to secure than proprietary software. As open-source co-founder Eric S. Raymond pointed out with [Linus' law: "Given enough eyeballs, all bugs are shallow."](http://www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/ar01s04.html) But it requires eyeballs looking for bugs in the first place to make it work. Jim Zemlin, the [Linux Foundation](https://linuxfoundation.org/) (LF)'s executive director, said in the aftermath of the [Heartbleed](https://www.zdnet.com/article/heartbleed-open-sources-worst-hour/) and [Shellshock](https://www.zdnet.com/article/shellshock-how-to-protect-your-unix-linux-and-mac-servers/) security fiascos: "In these cases, [the eyeballs weren't really looking.](https://www.esecurityplanet.com/applications/why-all-linux-security-bugs-arent-shallow/)" 

To help remedy this, David A. Wheeler, the LF's director of Open Source Supply Chain Security, recently revealed the LF or its related foundations and projects [directly fund people to do security work](https://linuxfoundation.org/blog/funded-open-source-security-work-at-the-linux-foundation). Here's how it works.


The funding comes from a variety of pro-Linux and open-source organizations. These include Google, Microsoft, the [Open Source Security Foundation (OpenSSF)](https://openssf.org/), the [LF Public Health foundation](https://www.lfph.io/), and the LF itself. When a problem is found, a developer reaches out to the appropriate LF organization. Generally speaking, [a contract that briefly describes what problem needs to be fixed and how it will be done](https://docs.google.com/document/d/1iIDAWRY_xBatKsbrXUe4iR0a_VTxqYCYJ40ZCrhlOKg/edit), the funds required for it, and who will do the work is set up.  

The proposal is then examined by the appropriate LF technical review point of contact (POC). This [POC is often Wheeler](mailto:dwheeler@linuxfoundation.org) himself. 

Once your project is approved, progress reports are made approximately once a month. These must include:

* A stable URL of a publicly accessible post (e.g., a blog or archived mailing list post) describing what you did that month.
* The post must briefly describe what has been accomplished using the funding since the last invoice. Include its date and hyperlinks to details. If git commits were involved, include hyperlinks to them. Make it easy for technical people to learn details (e.g., via hyperlinks).
* Also briefly describe why this work is important or link to such description(s), for someone who is not intimately familiar with it. Some readers may see your post out of context.
* Give credit, similar to National Public Radio. (e.g., "This work to <X> was [partially] funded by the OpenSSF, Google, and The Linux Foundation.") Thanking others is always polite. We also want people to consider funding OSS security as normal.
* Publicly provide an identifier (a personal name, pseudonym, or project name) of who's doing the work. This simplifies referring to the work. You do not need to reveal your personal name(s) publicly, though you're welcome to do so.

This is a lightweight process. It shouldn't take more than 20 minutes to write these reports. You may find it easier to write your post while you do the work. Funded work must be available under the appropriate open-source licenses. For example, bug fixes to Linux must be licensed under the [Gnu General Public Licenses Version 2 (GPLv2)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).

The POC will then review the post, and if it seems reasonable, approve the payment. Wheeler explained: "We understand that sometimes problems arise. We just want to see credible efforts. If there's a serious roadblock, try to suggest ways to overcome it or provide partial/incremental benefits. We need to provide confidence to funders that we aren't wasting their money."






So, what kind of projects are we walking about? Wheeler cites several examples. These include:

Ariadne Conill, the [Alpine Linux](https://www.alpinelinux.org/) security team chair, is improving this important container Linux distro's security. In particular, Conill has improved its vulnerability processing and made it reproducible. For example, this resulted in Alpine 3.14 being released with the lowest open vulnerability count in the final release in a long time. 

On [Git](https://git-scm.com/), the vital distributed version control system, David Huseby has been working on modifying [git to have a much more flexible cryptographic signing infrastructure](https://public-inbox.org/git/cover.1620454449.git.dwh@linuxprogrammer.org/T/%20https://dwhuseby.medium.com/universal-cryptographic-signing-protocol-for-git-42e7741b8773). This will make it easier to verify the integrity of software source code.

It's not just Linux-related programs that get security help. Theo de Raadt, founder and leader of [OpenBSD](https://www.openbsd.org/) and [OpenSSH](https://www.openssh.com/), has received funding to secure OpenSSH's plumbing. OpenSSH is an important suite of secure Secure Shell (ssh)networking utilities based on the protocol. De Raadt has also been funded to help secure [Resource Public Key Infrastructure (RPKI)](https://www.arin.net/resources/manage/rpki/), which protects internet routing protocols from attack. 

Besides fixing known problems, the LF and company are also looking for security troubles we don't know about yet. That's being done with security audits via the [Open Source Technology Improvement Fund (OSTIF)](https://ostif.org/). These projects include two Linux kernel security audits. One for [signing and key management policies](https://ostif.org/a-review-of-the-linux-kernels-release-signing-and-key-management-policies/) and the other for [vulnerability reporting and remediation.](https://ostif.org/a-review-of-the-linux-kernels-vulnerability-reporting-and-remediation/) Subject matter experts perform the audit reports, while Wheeler ensures these reports are clear to non-experts while still being accurate.

Looking ahead, OpenSSF is also working on improving overall open-source software security. These include [free courses on how to develop secure software](https://openssf.org/edx-courses/) and the [CII Best Practices badge](https://bestpractices.coreinfrastructure.org/) project. Other [projects improve OSS security](https://www.linuxfoundation.org/blog/how-lf-communities-enable-security-measures-required-by-the-us-executive-order-on-cybersecurity/), include [sigstore](https://sigstore.dev/), which is making cryptographic signatures much easier and improving [software bill-of-materials (SBOMs)](https://www.linuxfoundation.org/blog/what-is-an-sbom/).

If you'd like to help pay for this kind of work, the LF wants to hear from you. You can contribute to the [OpenSSF](https://openssf.org/) by just contacting the organization, Or, if you'd rather, you can create a grant directly with the Linux Foundation itself. If you have questions just email Wheeler at [dwheeler@linuxfoundation.org](https://mail.google.com/mail/?view=cm&fs=1&tf=1&to=dwheeler@linuxfoundation.org). For smaller amounts -- say, to fund a specific project -- you can also use the [LFX crowdfunding tools](https://lfx.linuxfoundation.org/tools/crowdfunding/) to fund or request funding.

Having trouble with the business side of funding security coding and audits? You're not alone. As Wheeler said: "Many people and organizations struggle to pay individual open-source software developers because of the need to handle taxes and oversight. If that's your concern, talk to us. The LF has experience and processes to do all that, letting experts focus on getting the work done."

### **Related Stories:**

* [It's time to improve Linux's security](https://www.zdnet.com/article/a-call-to-improve-linuxs-security/)
* [Patch now: Linux file system security hole, dubbed Sequoia, can take over systems](https://www.zdnet.com/article/patch-now-linux-file-system-security-hole-dubbed-sequoia-can-take-over-systems/)
* [Nasty Linux systemd security bug revealed](https://www.zdnet.com/article/nasty-linux-systemd-security-bug-revealed/).





#### Tags:
[[Linux]] [[open-source]] [[work.]] [[(e.g.,]] [[ZDNet]]
