# Microsoft: Shrootless bug lets hackers install macOS rootkits
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/microsoft-shrootless-bug-lets-hackers-install-macos-rootkits/)
+ Date: October 28, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft: Shrootless bug lets hackers install macOS rootkits](https://www.bleepstatic.com/content/hl-images/2020/10/07/Microsoft.jpg)


Attackers could use a new macOS vulnerability discovered by Microsoft to bypass System Integrity Protection (SIP) and perform arbitrary operations, elevate privileges to root, and install rootkits on vulnerable devices.


The Microsoft 365 Defender Research Team reported the vulnerability dubbed **Shrootless** (now tracked as [CVE-2021-30892](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30892)) to Apple by via the Microsoft Security Vulnerability Research (MSVR).


[SIP](https://support.apple.com/en-us/HT204899) (also known as rootless) is a macOS security technology that blocks potentially malicious software from modifying protected folders and files by restricting the root user account and limiting the actions it can perform on protected parts of the OS.


By design, SIP only allows processes signed by Apple or those with special entitlements (i.e., Apple software updates and Apple installers) to modify these protected parts of macOS.


"We found that the vulnerability lies in how Apple-signed packages with post-install scripts are installed. A malicious actor could create a specially crafted file that would hijack the installation process," [explained](https://www.microsoft.com/security/blog/2021/10/28/microsoft-finds-new-macos-vulnerability-shrootless-that-could-bypass-system-integrity-protection/) Jonathan Bar Or, a principal security researcher at Microsoft.


"After bypassing SIP’s restrictions, the attacker could then install a malicious kernel driver (rootkit), overwrite system files, or install persistent, undetectable malware, among others."



![Shrootless PoC exploit](https://www.bleepstatic.com/images/news/u/1109292/2021/Shrootless_poc_exploit.png)*Shrootless PoC exploit (Microsoft)*
Apple issued a fix to address the security flaw with the [security updates](https://support.apple.com/en-us/HT201222) released two days ago, on October 26.


"A malicious application may be able to modify protected parts of the file system," Apple said in the [security advisory](http://support.apple.com/en-us/HT212872).


Apple addressed the inherited permissions issue behind the Shrootless bug was with additional restrictions.


"We want to thank the Apple product security team for their professionalism and responsiveness in fixing the issue," Jonathan Bar Or added.


Last week, Microsoft also reported finding [new variants of macOS WizardUpdate malware](https://www.bleepingcomputer.com/news/security/microsoft-wizardupdate-mac-malware-adds-new-evasion-tactics/) (also tracked as UpdateAgent or Vigram), updated to use new evasion and persistence tactics.


This trojan deploys second-stage malware payloads, including Adload, a malware strain active [since late 2017](https://labs.sentinelone.com/how-adload-macos-malware-continues-to-adapt-evade/) and known for being able to [slip through Apple's YARA signature-based XProtect built-in antivirus](https://www.bleepingcomputer.com/news/apple/new-adload-malware-variant-slips-through-apples-xprotect-defenses/) to infect Macs.


In June, Redmond's security researchers also discovered [critical firmware vulnerabilities in some NETGEAR router models](https://www.bleepingcomputer.com/news/security/microsoft-finds-netgear-router-bugs-enabling-corporate-breaches/) that attackers could use to breach and move laterally within enterprise networks.




#### Tags:
[[Microsoft]] [[macOS]] [[Shrootless]] [[malware]] [[Bleeping Computer]]
