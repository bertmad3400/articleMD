# NPM fixes private package names leak, serious authorization bug
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/npm-fixes-private-package-names-leak-serious-authorization-bug/)
+ Date: November 16, 2021
+ Author: Ax Sharma


## Article:
![npm](https://www.bleepstatic.com/content/hl-images/2021/10/23/npm-supply-chain-attack.jpg)


The largest software registry of Node.js packages, npm, has disclosed multiple security flaws that were identified and remedied recently.


The first flaw concerns leak of names of private npm packages on the npmjs.com's 'replica' server—feeds from which are consumed by third-party services.


Whereas, the second flaw allows attackers to publish new versions of any existing npm package that they do not own or have rights to, due to improper authorization checks.


Private npm package names leaked
--------------------------------


This week, npm's parent company, GitHub has disclosed two security flaws that were identified and resolved in the npm registry between October and this month.


The first one is a data leak on the npmjs' replication server, which was caused by 'routine maintenance.' The leak exposed a list of names of private npm packages, but not the content of these packages during the maintenance window.


"During maintenance on the database that powers the public npm replica at *replicate.npmjs.com*, records were created that could expose the names of private packages," states GitHub Chief Security Officer, Mike Hanley in a [blog post](https://github.blog/2021-11-15-githubs-commitment-to-npm-ecosystem-security/).


"This briefly allowed consumers of *replicate.npmjs.com* to potentially identify the names of private packages due to records published in the public changes feed. No other information, including the content of these private packages, was accessible at any time."


Note, while the content of the private packages was not exposed, knowledge of the private package names is enough for threat actors to conduct targeted [dependency confusion](https://www.bleepingcomputer.com/news/security/malicious-npm-packages-target-amazon-slack-with-new-dependency-attacks/) and [typosquatting](https://www.bleepingcomputer.com/news/security/malicious-npm-libraries-install-ransomware-password-stealer/) attacks in an automated fashion, as we have [seen](https://www.bleepingcomputer.com/tag/dependency-confusion/) time and time again.


The leak specifically concerns scoped private npm libraries that look like "*@owner/package*" and were created before October 20th. Names of such libraries were exposed "between October 21 13:12:10Z UTC and October 29 15:51:00Z UTC," according to GitHub.


The data leak was identified by GitHub on October 26th and by the 29th, all records containing private package names were deleted from the npm's replication database. Although, GitHub does warn that despite this, the *replicate.npmjs.com*service is consumed by third parties who may, therefore, continue to retain a copy or "may have replicated the data elsewhere."


To prevent such an issue from recurring, GitHub has made changes to its process of generating the public replication database which is expected to eliminate the possibility of leaking private package names in the future.


Flaw could let unauthorized publication of new versions
-------------------------------------------------------


Additionally, GitHub disclosed a serious bug that could "allow an attacker to publish new versions of any npm package using an account without proper authorization."


This vulnerability stemmed from improper authorization checks and data validation in between several microservices that process requests to the npm registry.


"In this architecture, the authorization service was properly validating user authorization to packages based on data passed in request URL paths. However, the service that performs underlying updates to the registry data determined which package to publish based on the contents of the uploaded package file," explains Hanley.


"This discrepancy provided an avenue by which requests to publish new versions of a package would be authorized for one package but would actually be performed for a different, and potentially unauthorized, package. We mitigated this issue by ensuring consistency across both the publishing service and authorization service to ensure that the same package is being used for both authorization and publishing."


Researchers [Kajetan Grzybowski](https://twitter.com/dr_brix) and [Maciej Piechota](http://twitter.com/haqpl) have been credited for responsibly reporting the flaw via GitHub's [security bug bounty program](https://bounty.github.com/).


And, so far, it seems there is no evidence of exploitation. The vulnerability existed in the npm registry "beyond the timeframe for which we have telemetry to determine whether it has ever been exploited maliciously," but there is some reassurance.


GitHub has stated with high confidence that the vulnerability has not been exploited maliciously since at least September 2020, which is around the time telemetry became available.


"We quickly validated the report, began our incident response processes, and patched the vulnerability within six hours of receiving the report," states GitHub.


npm to require two-factor authentication from 2022
--------------------------------------------------


Both announcements come not too long after popular npm libraries, '[ua-parser-js](https://www.bleepingcomputer.com/news/security/popular-npm-library-hijacked-to-install-password-stealers-miners/),' ['coa,' and 'rc'](https://www.bleepingcomputer.com/news/security/popular-coa-npm-library-hijacked-to-steal-user-passwords/) were hijacked in a series of attacks aimed at infecting open source software consumers with trojans and crypto-miners.


These attacks were attributed to the compromise of npm accounts [[1](https://twitter.com/npmjs/status/1456310627362742284), [2](https://github.com/faisalman/ua-parser-js/issues/536#issuecomment-949742904)] belonging to the maintainers behind these libraries. None of the maintainers of these popular libraries had two-factor authentication (2FA) enabled on their accounts, according to GitHub.


Attackers who can manage to hijack npm accounts of maintainers can trivially publish new versions of these legitimate packages, after contaminating them with malware.


As such, to minimize the possibility of such compromises from recurring in near future, GitHub will start requiring npm maintainers to enable 2FA, sometime in the first quarter of 2022.


As for cases where typosquatting and dependency confusion malware is published to npm from an attacker-owned account, rather than from a hijacked account, GitHub continues to invest in resources and security improvements for automating real-time malware detection in newly published versions of npm packages.




#### Tags:
[[npm]] [[GitHub]] [[packages,]] [[GitHub.]] [[Bleeping Computer]]
