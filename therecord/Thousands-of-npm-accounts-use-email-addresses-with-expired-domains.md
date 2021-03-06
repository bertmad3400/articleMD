# Thousands of npm accounts use email addresses with expired domains
### An academic research project found that thousands of JavaScript developers are using an email address with an expired domain for their npm accounts, leaving their projects exposed to easy hijacks.

## Information:
+ Source: The Record
+ Link: https://therecord.media/thousands-of-npm-accounts-use-email-addresses-with-expired-domains/
+ Date: 2022-02-11T16:28:12+00:00
+ Author: Catalin Cimpanu


## Article:
![Article Image](https://therecord.media/wp-content/uploads/2022/02/npm.png)

An academic research project found that thousands of JavaScript developers are using an email address with an expired domain for their npm accounts, leaving their projects exposed to easy hijacks.


The study, performed last year by researchers from Microsoft and North Caroline State University, analyzed the metadata of 1,630,101 libraries uploaded on [Node Package Manager (npm)](https://www.npmjs.com/), the de-facto repository for JavaScript libraries and the largest package repository on the internet.


### 2,818 developers exposed to account hijacks


Researchers said they found that 2,818 project maintainers were still using an email address for their accounts that had an expired domain, some of which they found on sale on sites like GoDaddy.


The team argued that attackers could buy these domains, re-register the maintainer’s address on their own email servers, and then reset the maintainer’s account password and take over his npm packages.


An attack like this would work because the npm portal does not enforce two-factor authentication (2FA) for account owners, meaning that once the attacker reset the owner’s password, they would be free to alter packages with any other hindrance.


In total, the research team said the 2,818 maintainer accounts managed 8,494 packages, which had an average of 2.43 direct dependents, denoting that any attack would also hit tens of thousands of other downstream projects.


Account hijacks like these could be spotted by the account owners, but researchers also pointed out that many npm libraries and accounts are either unmaintained (58.7%) or abandoned (44.3%), and there would be a big chance that attackers would be able to carry out their attacks without the maintainers even noticing.


### npm team appears to have reacted to the findings


The research team said they notified the npm security team of their report’s findings but did not say how the npm team reacted. An email sent to GitHub, which owns npm, was not returned before this article’s publication.


However, it is worth noting that days before this study was published in December 2021, npm [announced plans](https://github.blog/2021-12-07-enrolling-npm-publishers-enhanced-login-verification-two-factor-authentication-enforcement/) to slowly start enforcing 2FA for developer accounts. This process was scheduled to take place in multiple stages, with the Top 100 maintainer accounts being enrolled in mandatory 2FA [at the start of this month](https://therecord.media/npm-enrolls-top-100-package-maintainers-into-mandatory-2fa/).


Additional details on the study are available in the “[What are Weak Links in the npm Supply Chain?](https://arxiv.org/abs/2112.10165)” research paper. Some of the research team’s other findings are also listed below:


* 2.2% (33,249) of packages used install scripts, which could be abused to run malicious commands and is against npm best security practices;
* The Top 1% packages (14,941) had an average of 32.4 maintainers per package, opening the door for attacks via the accounts of inactive or inattentive developers;
* 389 packages had 40 contributors for every maintainer, opening the door for the accidental insertion of security flaws or flooding a project with contributions to sneak in malicious code;
* The top 1% maintainers own an average number of 180.3 packages with direct dependents of 4,010 average packages, meaning some developers could be overworked or not have time to thoroughly maintain or review package changes.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Npm]] [[The Record]]

