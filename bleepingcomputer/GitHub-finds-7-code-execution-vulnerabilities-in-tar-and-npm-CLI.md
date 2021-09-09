# GitHub finds 7 code execution vulnerabilities in 'tar' and npm CLI
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/github-finds-7-code-execution-vulnerabilities-in-tar-and-npm-cli/)
+ Date: September 8, 2021
+ Author: Ax Sharma


## Article:
![github](https://www.bleepstatic.com/content/hl-images/2021/08/18/GitHub_headpic.jpg)


GitHub security team has identified several high-severity vulnerabilities in npm packages, "tar" and "@npmcli/arborist," used by npm CLI.


The *tar* package receives 20 million weekly downloads on average, whereas *arborist* gets downloaded over 300,000 times every week.


The vulnerabilities affect both Windows and Unix-based users, and if left unpatched, can be exploited by attackers to achieve arbitrary code execution on a system installing untrusted npm packages.


Bug bounty hunters awarded $14,500 for ZIP slips
------------------------------------------------


Between July and August this year, security researchers and bug bounty hunters [Robert Chen](http://github.com/chen-robert) and [Philip Papurt](http://github.com/ginkoid) identified arbitrary code execution vulnerabilities in the open-source Node.js packages, *[tar](https://www.npmjs.com/package/tar)* and *[@npmcli/arborist](https://www.npmjs.com/package/@npmcli/arborist)*.


On discovery of these vulnerabilities, the researchers privately notified npm via one of GitHub's bug bounty programs.


On further review of the researchers' reports, GitHub security team found some more high-severity vulnerabilities in the aforementioned packages, affecting both Windows and Unix-based systems.


Node.js package *tar* remains a core dependency for installers that need to unpack npm packages post-installation. The package is also used by thousands of other open source projects, and as such receives roughly 20 million downloads every week. The *arborist* package is a core dependency relied on by npm CLI and is used to manage *node\_modules* trees.


These [ZIP slip](https://www.bleepingcomputer.com/news/security/zip-slip-vulnerability-affects-thousands-of-projects-across-multiple-ecosystems/) vulnerabilities pose a problem for developers installing untrusted npm packages using the npm CLI, or using "tar" to extract untrusted packages.


By default, npm packages are shipped as .*tar.gz* or .*tgz* files which are ZIP-like archives and as such need to be extracted by the installation tools.


The tools extracting these archives should ideally ensure any malicious paths within the archive don't end up overwriting existing files, especially the sensitive ones, on the filesystem.


But, because of the vulnerabilities listed below, the npm package when extracted could overwrite arbitrary files with the privileges of the user running the *npm install* command:


1. [CVE-2021-32803](https://github.com/npm/node-tar/security/advisories/GHSA-r628-mhmh-qjhw)
2. [CVE-2021-32804](https://github.com/npm/node-tar/security/advisories/GHSA-3jfq-g458-7qm9)
3. [CVE-2021-37701](https://github.com/npm/node-tar/security/advisories/GHSA-9r2w-394v-53qc)
4. [CVE-2021-37712](https://github.com/npm/node-tar/security/advisories/GHSA-qq89-hq3f-393p)
5. [CVE-2021-37713](https://github.com/npm/node-tar/security/advisories/GHSA-5955-9wpr-37jh)
6. [CVE-2021-39134](https://github.com/npm/arborist/security/advisories/GHSA-2h3h-q99f-3fhc)
7. [CVE-2021-39135](https://github.com/npm/arborist/security/advisories/GHSA-gmw6-94gg-2rc2)


"CVE-2021-32804, CVE-2021-37713, CVE-2021-39134, and CVE-2021-39135 specifically have a security impact on the npm CLI when processing a malicious or untrusted npm package install," explains [Mike Hanley](https://github.com/mph4), Chief Security Officer at GitHub.


"Some of these issues may result in arbitrary code execution, even if you are using *--ignore-scripts* to prevent the processing of package lifecycle scripts."


GitHub Security team thanked both Chen and Papurt for their responsible disclosure and awarded them a total bounty of $14,500 for their efforts in keeping GitHub secure.


npm urging users to fix vulnerabilities
---------------------------------------


npm, owned by GitHub, is also prompting developers to fix these vulnerabilities ASAP in a tweet:




> 
> action recommended: following newly discovered vulnerabilities in `tar` and `@npmcli/arborist`, we recommend upgrading to the latest versions of [@nodejs](https://twitter.com/nodejs?ref_src=twsrc%5Etfw) 12 / 14 / 16 or npm 6 / 7 as well as updating any dependencies you may have on `tar`. read more: <https://t.co/t4WaVwJ0mx>
> 
> 
> — npm (@npmjs) [September 8, 2021](https://twitter.com/npmjs/status/1435634361701789696?ref_src=twsrc%5Etfw)


Developers should upgrade their *tar* dependency versions to 4.4.19, 5.0.11, or 6.1.10, and upgrade @npmcli/arborist version 2.8.2 to patch the vulnerabilities.


For npm CLI, versions [v6.14.15](https://github.com/npm/cli/releases/tag/v6.14.15), [v7.21.0](https://github.com/npm/cli/releases/tag/v7.21.0), or newer contain the fix. Additionally, Node.js version 12, 14, or 16 come with the fixed *tar* version and can be safely upgraded to, according to GitHub.


Complete details related to these vulnerabilities are available in GitHub's detailed [blog post](https://github.blog/2021-09-08-github-security-update-vulnerabilities-tar-npmcli-arborist/).




#### Tags:
[[npm]] [[GitHub]] [[packages,]] [[Node.js]] [[Bleeping Computer]]
