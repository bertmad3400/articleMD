# Cloudflare fixes CDN code execution bug affecting 12.7% of all sites
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/cloudflare-fixes-cdn-code-execution-bug-affecting-127-percent-of-all-sites/)
+ Date: July 16, 2021
+ Author: Ax Sharma


## Article:
![cloudflare](https://www.bleepstatic.com/content/hl-images/2020/10/06/cloudflare-ddos.jpg)


Cloudflare has fixed a critical vulnerability in its free and open-source CDNJS potentially impacting [12.7% of all websites](https://w3techs.com/technologies/details/cd-cdnjs) on the internet.


CDNJS serves millions of websites with over 4,000 JavaScript and CSS libraries stored publicly on GitHub, making it the second-largest JavaScript CDN.


The vulnerability exploits comprised publishing packages to Cloudflare's CDNJS using GitHub and npm, to trigger a Path Traversal vulnerability, and eventually remote code execution.


If exploited, the vulnerability would lead to a complete compromise of CDNJS infrastructure.


From "ZIP Slip" to remote code execution
----------------------------------------


This week, security researcher [*RyotaK*](https://twitter.com/ryotkak) explains how he was able to find a method to completely compromise Cloudflare's CDNJS network while researching supply-chain attacks.


Content delivery networks (CDNs) perform a critical role in upholding the security, integrity, and availability of the Internet as a vast majority of websites rely on these services to load popular JavaScript libraries and CSS scripts.


CDNs can become a choice of targets for adversaries as, if compromised, the attack can have far-reaching consequences for many websites, online stores, and their customers.


While glancing over cdnjs.com, RyotaK noticed that for libraries that did not yet exist in CDNJS, he could suggest the addition of a new library via CDNJS' [GitHub repository](https://github.com/cdnjs/packages).



![cdnjs package not found](https://www.bleepstatic.com/images/news/u/1164866/2021/Jul-2021/cloudflare-cdnjs-rce/cdnjs-package-not-found.jpg)**Users can request a package to be published to CDNJS' GitHub repo**
After exploring this GitHub repository and the adjacent ones that together make the CDNJS ecosystem work, RyotaK figured a way to trick the servers into executing arbitrary code.


Particularly, the researcher studied the scripts present in [cdnjs/bot-ansible](https://github.com/cdnjs/bot-ansible) and [cdnjs/tools](https://github.com/cdnjs/tools), including an [*autoupdate*](https://github.com/cdnjs/tools/blob/285c11bc7290e07ecc07191c3196cbf57d482868/cmd/autoupdate/main.go#L149) script that facilitated automatic retrieval of library updates.


These scripts would periodically update the CDNJS server with newer versions of software libraries released by their authors on the corresponding npm registry.


In other words, for every library published to CDNJS' GitHub repo, its newer version would be downloaded from the linked npm registry, with the npm version also maintained by the library author.


RyotaK wondered what would happen if a library he had published to CDNJS had its corresponding npm version containing a [Path Traversal](https://en.wikipedia.org/wiki/Directory_traversal_attack) exploit.


Note, npm packages are published as TGZ (.tar.gz) archives which can easily be crafted with path traversal exploits hiding within.


The researcher first published a test library called *[hey-sven](https://cdnjs.com/libraries/hey-sven)* to CDNJS using GitHub, and then began releasing newer versions of "hey-sven" on the npm registry.


In the newer "hey-sven" versions [published](https://www.npmjs.com/package/hey-sven) to npm, which would eventually [get processed](https://github.com/cdnjs/packages/blob/master/packages/h/hey-sven.json#L12) by CDNJS' update bots, the researcher injected Bash scripts at strange-looking paths.


These distinct paths are nothing other than Path Traversal exploits hidden inside ZIP/TGZ archives, a concept popularized in 2018 as "[ZIP Slip](https://www.bleepingcomputer.com/news/security/zip-slip-vulnerability-affects-thousands-of-projects-across-multiple-ecosystems/)."



![npm package had a path traversal exploit](https://www.bleepstatic.com/images/news/u/1164866/2021/Jul-2021/cloudflare-cdnjs-rce/zipslip-poc-cloudflare.jpg)**The npm versions 1.0.1 & 1.0.2 of "hey-sven" library contained Path Traversal exploits**​​​​​​  

Source: BleepingComputer
Once CDNJS servers processed the crafted "hey-sven" npm archives, the contents of these Bash scripts would be executed on the server.


But, the researcher did not want to accidentally overwrite an existing script so he first used a [symlink vulnerability](https://en.wikipedia.org/wiki/Symlink_race) to read the contents of the file he was about to overwrite, during this proof-of-concept (PoC) test.


"As Git supports symbolic links by default, it may be possible to read arbitrary files from the cdnjs library update server by adding symlink into the Git repository."


"If the regularly executed script file is overwritten to execute arbitrary commands, the automatic update function may be broken, so I decided to check the arbitrary file reading first," said the researcher.


As soon as his crafted PoC hit the server, *RyotaK* was able to unexpectedly dump sensitive secrets such as GITHUB\_REPO\_API\_KEY and WORKERS\_KV\_API\_TOKEN into scripts served by the CDN at **https://cdnjs.cloudflare.com/...**



![output of symlink poc](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Output from the initial symlink PoC provided the researcher with secret keys**  

Source: BleepingComputer
*GITHUB\_REPO\_API\_KEY* is an API key granting write permissions—enabling an attacker to **alter any library** on the CDNJS, or tamper with the *cdnjs.com* website itself!


*WORKERS\_KV\_API\_TOKEN*secret on the other hand could be used to tamper with the libraries present in the cache of Cloudflare Workers.


"By combining these permissions, the core part of CDNJS, such as the origin data of CDNJS, the KV cache, and even the CDNJS website, could be completely tampered [with]," explains the researcher.


Cloudflare issues many fixes to squash the bug
----------------------------------------------


The researcher reported this vulnerability to Cloudflare via HackerOne's vulnerability disclosure program on April 6th, 2021, and saw Cloudflare's team applying an intermittent fix within hours.


The initial fix seen by BleepingComputer is aimed at resolving the symlink vulnerability:



![symlink fix applied by cdnjs](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Initial fix applied by Cloudflare's CDNJS**([GitHub](https://github.com/cdnjs/tools/commit/a6028c6427a1344713133342d93e593736dde52a))
However, due to the complexity of the CDNJS ecosystem, a series of more concrete fixes were applied over the following weeks to different repositories, according to the researcher.


RyotaK shared with BleepingComputer that while the first fix was centered around rejecting symbolic links (symlinks) in Git repositories, it only remediated a part of the problem.


"They tried to refuse symlinks first, but they noticed that current design of the bot is too dangerous. So they isolated most dangerous features."


"And for other features, they [applied](https://github.com/cdnjs/bot-ansible/pull/24) AppArmors," the researcher told BleepingComputer in an email interview.


Application Armor or AppArmor is a security feature that restricts the capabilities of programs running on Unix-based envionments with predefined profiles so that the programs don't inadvertently exceed their intended scope of access.


The researcher also shared a series of fixes with BleepingComputer deployed by Cloudflare to secure the automated bot processing the updated libraries:



![multiple fixes applied by cloudflare](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Cloudflare makes multiple changes to CDNJS to resolve the bug**
"While this vulnerability could be exploited without any special skills, it could impact many websites."


"Given that there are many vulnerabilities in the supply chain, which are easy to exploit but have a large impact, I feel that it's very scary," says RyotaK in his [blog post](https://blog.ryotak.me/post/cdnjs-remote-code-execution-en/).


As previously reported by BleepingComputer, a Magecart supply-chain attack impacting [thousands of online stores](https://www.bleepingcomputer.com/news/security/c-is-for-credit-card-magecart-hits-volusion-e-commerce-sites/) stemmed from the compromise of Volusion's CDN infrastructure.


The researcher praised Cloudflare's fast-paced incident response teams, who, within minutes of receiving the researcher's report, rotated the leaked secrets and worked with him to study the PoC exploits.


BleepingComputer has reached out to Cloudflare with some questions, including if this vulnerability has been widely exploited. We are awaiting their response.




#### Tags:
[[CDNJS]] [[Cloudflare]] [[npm]] [[GitHub]] [[BleepingComputer]] [[RyotaK]] [[cdnjs]] [[websites]] [[hey-sven]] [[symlink]] [[Bleeping Computer]]
