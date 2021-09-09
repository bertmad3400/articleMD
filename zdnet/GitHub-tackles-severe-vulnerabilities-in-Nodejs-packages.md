# GitHub tackles severe vulnerabilities in Node.js packages
### Bugs impacting tar and @npmcli/arborist were reported through a bug bounty program.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/github-tackles-seven-vulnerabilities-in-node-js-packages/)
+ Date: September 9, 2021 -- 09:36 GMT (10:36 BST)
+ Author: Charlie Osborne


## Article:
Unknown

GitHub has resolved numerous vulnerabilities in Node.js packages tar and @npmcli/arborist, with the worst allowing file overwrites and arbitrary code execution. 


On Wednesday, GitHub said the company [received reports](https://github.blog/2021-09-08-github-security-update-vulnerabilities-tar-npmcli-arborist/) from Robert Chen and Philip Papurt, between July 21 and August 13, of security flaws impacting the packages via one of GitHub's bug bounty programs, which give researchers credit and financial rewards for responsibly disclosing vulnerabilities to the vendor.  

GitHub's Chief Security Officer Mike Hanley says that these reports prompted GitHub to conduct its own review of tar and @npmcli/arborist, leading to the discovery of additional security issues.  

The [tar Node.js](https://www.npmjs.com/package/tar) package is used to mimic the tar archive system on Unix, whereas [@npmcli/arborist](https://www.npmjs.com/package/@npmcli/arborist) has been developed to manage node\_modules trees. Tar is a core npm dependency for npm package extraction, and @npmcli/arborist is a core dependency for npm CLI. 

Node-tar has accounted for 22,390,735 weekly downloads, at the time of writing, whereas @npmcli/arborist has been downloaded 405,551 times over the past week.  

In total, seven vulnerabilities have been verified through the bug bounty reports and the security team at GitHub's findings: 

**Tar:** 

* [CVE-2021-32803](https://github.com/npm/node-tar/security/advisories/GHSA-r628-mhmh-qjhw), high impact: Arbitrary File Creation/Overwrite via insufficient symlink protection. A malicious tar archive could create/overwrite arbitrary files with the privileges of the process using tar.
* [CVE-2021-32804](https://github.com/npm/node-tar/security/advisories/GHSA-3jfq-g458-7qm9), high impact: Arbitrary File Creation/Overwrite due to insufficient absolute path sanitization. Malicious npm packages could create/overwrite files with the privileges of the user running the install, leading to code execution.
* [CVE-2021-37701](https://github.com/npm/node-tar/security/advisories/GHSA-9r2w-394v-53qc), high impact: A path separator issue in file names could lead to malicious tar archives creating/overwriting arbitrary files with the privilege levels of the process running tar.
* [CVE-2021-37712](https://github.com/npm/node-tar/security/advisories/GHSA-qq89-hq3f-393p), high impact: Unicode conversions and Windows 8.3 file name semantics could cause directory cache poisoning and symlink check bypasses, leading to arbitrary file creation and overwrite.
* [CVE-2021-37713](https://github.com/npm/node-tar/security/advisories/GHSA-5955-9wpr-37jh), high impact: Arbitrary File Creation/Overwrite on Windows via insufficient relative path sanitization. Malicious npm packages could create and overwrite files outside of their installation root, with user privileges.






**@npmcli/arborist:** 

* [CVE-2021-39134](https://github.com/npm/arborist/security/advisories/GHSA-2h3h-q99f-3fhc), medium impact: An issue in how symbolic links within the node\_modules tree are handled. Exploitation could result in malicious packages overwriting files outside of an installation root with user privileges.
* [CVE-2021-39135](https://github.com/npm/arborist/security/advisories/GHSA-gmw6-94gg-2rc2), medium impact: This vulnerability also impacts symbolic link handling, specifically when untrusted packages are installed on case insensitive file systems.

"CVE-2021-32804, CVE-2021-37713, CVE-2021-39134, and CVE-2021-39135 specifically have a security impact on the npm CLI when processing a malicious or untrusted npm package install," GitHub says. "Some of these issues may result in arbitrary code execution, even if you are using --ignore-scripts to prevent the processing of package lifecycle scripts." 

To make developers aware of these bugs, GitHub created 16.7 million Dependabot alerts and released 1.8 million notifications.  

GitHub has requested project managers that use npm CLI and download it directly to upgrade to v6.14.15, v7.21.0, or newer. If Node.js is in use, the organization recommends an upgrade to the latest releases of Node 12, 14, or 16, all of which contain patches to resolve the security flaws. Tar users are now able to upgrade to versions 4.4.19, 5.0.11, and 6.1.10. The [latest version](https://www.npmjs.com/package/@npmcli/arborist/v/2.8.3) of @npmcli/arborist available is 2.8.3. 

Chen and Papurt have been awarded a combined bounty of $14,500 for their reports.   

###  Previous and related coverage

* [Linux boosts Microsoft NTFS support as Linus Torvalds complains about GitHub merges](https://www.zdnet.com/article/linux-boosts-microsoft-ntfs-support-as-linus-torvalds-complains-about-github-merges/)  

* [GitHub pushes users to enable 2FA following end of password authentication for Git operations](https://www.zdnet.com/article/github-pushes-users-to-enable-2fa-following-end-of-password-authentication-for-git-operations/)  

* [GitHub to replace "master" with alternative term to avoid slavery references](https://www.zdnet.com/article/github-to-replace-master-with-alternative-term-to-avoid-slavery-references/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[GitHub]] [[npm]] [[impact:]] [[@npmcli/arborist]] [[Node.js]] [[Creation/Overwrite]] [[ZDNet]]
