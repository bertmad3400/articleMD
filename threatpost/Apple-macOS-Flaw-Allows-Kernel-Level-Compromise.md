# Apple macOS Flaw Allows Kernel-Level Compromise
### ‘Shrootless’ allows bypass of System Integrity Protection IT security measures to install a malicious rootkit that goes undetected and performs arbitrary device operations.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175927)
+ Date: November 2, 2021  11:50 am
+ Author: Elizabeth Montalbano


## Article:
Apple has patched a vulnerability in macOS can allow attackers to bypass a key OS protection and install a malicious rootkit to perform arbitrary operations on a device, researchers from Microsoft have discovered.


The problem—dubbed “Shrootless”–is associated with a security technology called System Integrity Protection (SIP) found in macOS, Jonathan Bar Or from the Microsoft 365 Defender Research Team explained in a [blog post](https://www.microsoft.com/security/blog/2021/10/28/microsoft-finds-new-macos-vulnerability-shrootless-that-could-bypass-system-integrity-protection/) published last week. SIP restricts a user at the root level of the OS from performing operations that may compromise system integrity.


Researchers were assessing processes entitled to bypass SIP protections when they discovered the vulnerability, which is being tracked as [CVE-2021-30892](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30892), Or wrote.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“We found that the vulnerability lies in how Apple-signed packages with post-install scripts are installed,” he explained in the post. “A malicious actor could create a specially crafted file that would hijack the installation process. After bypassing SIP’s restrictions, the attacker could then install a malicious kernel driver (rootkit), overwrite system files, or install persistent, undetectable malware, among others.”


Microsoft Security Vulnerability Research (MSVR) shared the researchers’ findings to Apple through its Coordinated Vulnerability Disclosure (CVD), and the company responded promptly, Or said. Apple included a fix for the flaw in a raft of [security updates](https://support.apple.com/en-us/HT212872) it released on Oct. 26


Microsoft’s interest in a MacOS flaw demonstrates researchers’ interest in security for  enterprise networks that use hybrid environments, which increase the attack surface for threat actors to compromise myriad devices regardless of OS, Or noted.


“This OS-level vulnerability and others that will inevitably be uncovered add to the growing number of possible attack vectors for attackers to exploit,” he wrote. “As networks become increasingly heterogeneous, the number of threats that attempt to compromise non-Windows devices also increases.”


**How SIP Works**


Or explained how SIP works to give context for the flaw. Apple first introduced the process, also known as “rootless,” in macOS Yosemite. The process “essentially locks down the system from root by leveraging the Apple sandbox to protect the entire platform,” Or explained.


Two NVRAM variables control the system: **csr-active-config****, a** bitmask of enabled protections; and **csr-data****, which** stores netboot configuration.


“These variables cannot be legitimately modified in non-recovery mode,” Or wrote. “Therefore, the only legitimate way to disable SIP is by booting into recovery mode and turning SIP off. Turning SIP on or off is done using the built-in *csrutil* tool, which can also display the SIP status.”


SIP has a number of protections that it uses to secure the macOS kernel and other root processes. Attackers can bypass SIP, however, using a bypass of any of them, setting up a number of attack scenarios, Or wrote.


They could load untrusted kernel extensions could compromise the kernel and allow the said extensions to perform operations without any checks, or bypass filesystem checks that allow a kernel extension to enforce SIP to itself completely. Attackers also could freely modify the NVRAM to control SIP itself, researchers said.


**Breakdown of Shrootless**


Researchers discovered Shrootless when, in their analysis, they came across the daemon *system\_installd*, which has the powerful *com.apple.rootless.install.heritable* entitlement. With this entitlement, any child process of *system\_installd* would be able to bypass SIP filesystem restrictions altogether, Or wrote.


Upon examining all the child processes of *system\_installd*, researchers discovered a few cases that could allow attackers to abuse its functionality and bypass SIP, he explained.


“For instance, when installing an Apple-signed package (.pkg file), the said package invokes *system\_installd*, which then takes charge of installing the former,” Or wrote. “If the package contains any post-install scripts, *system\_installd* runs them by invoking a default shell, which is [*zsh*](https://zsh.sourceforge.io/) on macOS. Interestingly, when *zsh* starts, it looks for the file */etc/zshenv*, and—if found—runs commands from that file automatically, even in non-interactive mode.”


Therefore, an attacker can perform arbitrary operations on the device by creating a malicious */etc/zshenv* file and then waiting for *system\_installd* to invoke *zsh*, he explained.


Researchers created a fully functional proof-of-concept (POC) Shrootless exploit that could override the kernel extension exclusion list using three steps. The POC: downloads an Apple-signed package (using *wget*) that is known to have a post-install script; plants a malicious */etc/zshenv* that checks for its parent process and, if it’s *system\_installd*, writes to restricted locations; and invokes the *installer* utility to install the package.


The Microsoft team also found that *zshenv* could be used as a general attack technique as a persistence mechanism or to elevate privileges besides being used for a SIP bypass, Or wrote.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[wrote.]] [[Microsoft]] [[system_installd,]] [[macOS]] [[Apple-signed]] [[post-install]] [[explained.]] [[Shrootless]] [[system_installd]] [[ThreatPost]]
