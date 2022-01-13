# When open-source developers go bad | ZDNet
### JavaScript developer Marak Squires wasn't happy about not making money from his open-source libraries, so he deliberately corrupted them, leaving programmers and end-users with dead-in-the-water programs.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/when-open-source-developers-go-bad/
+ Date: 2022-01-13 13:38:00
+ Author: Steven Vaughan-Nichols


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/0817cd2ff2c7b4654cfb1aff8e0043653d240f9d/2014/08/18/afdcd90a-26bf-11e4-8c7f-00505685119a/securitys-future-belongs-to-open-source.jpg?width=770&height=578&fit=crop&auto=webp)

Chances are unless you're a [JavaScript](https://www.javascript.com/) programmer, you've never heard of the open-source Javascript libraries ['colors.js](https://www.npmjs.com/package/colors)' and ['faker.js](https://github.com/faker-js/faker)." They're simple programs that respectively let you use colored text on your [node.js](https://nodejs.org/), a popular JavaScript runtime, console, and create fake data for testing. Faker.js is used with more than 2,500 other [Node Package Manager (NPM)](https://www.npmjs.com/) programs and is downloaded 2.4 million times per week. Colors.js is built into almost 19,000 other NPM packages and is downloaded 23 million times a week. In short, they're everywhere. And, when their creator, JavaScript developer Marak Squires, fouled them up, tens of thousands of JavaScript programs blew up.


Thanks, guy.

* [Developers are in short supply. Here are the skills and programming languages employers need](https://www.zdnet.com/article/finding-developers-is-going-to-be-your-biggest-hiring-headache-this-year/)

This isn't the first time a developer deliberately sabotaged their own open-source code. Back in 2016, [Azer Koçulu deleted a 17-line npm package called 'left-pad,](https://www.zdnet.com/article/disgruntled-developer-breaks-thousands-of-javascript-node-js-apps/) 'which killed thousands of Node.js programs that relied on it to function. Both then and now the actual code was trivial, but because it's used in so many other programs its effects were far greater than users would ever have expected.  

Why did Squires do it? We don't really know. In [faker.js's GitHub README file](https://github.com/marak/Faker.js/), Squires said, "What really happened with Aaron Swartz?" This is a reference to hacker activist [Aaron Swartz who committed suicide](https://www.zdnet.com/article/hacker-activist-aaron-swartz-commits-suicide/) in 2013 when he faced criminal charges for allegedly trying to make MIT academic journal articles public.

Your guess is as good as mine as to what this has to do with anything.

What's more likely to be the reason behind his putting an infinite loop into his libraries is that he wanted money. In a since-deleted GitHub post, Squires said, "Respectfully, [I am no longer going to support Fortune 500s](https://web.archive.org/web/20210704022108/https://github.com/Marak/faker.js/issues/1046) ( and other smaller-sized companies ) with my free work. There isn't much else to say. Take this as an opportunity to send me a six-figure yearly contract or fork the project and have someone else work on it."

Excuse me. While open-source developers should be fairly compensated for their work, wrecking your code isn't the way to persuade others to pay you. 

* [Best online computer programming degrees 2021: Top picks](https://www.zdnet.com/education/computers-tech/best-online-computer-programming-degree/)






This is a black eye for open-source and its developers. We don't need programmers who crap on their work when they're ticked off at the world.

Another problem behind the problem is that too many developers simply automatically download and deploy code without ever looking at it. This kind of deliberate blindness is just asking for trouble. 

Just because a software package was made by an open-source programmer doesn't mean that it's flawless. Open-source developers make as many mistakes as any other kind of programmer. It's just that in open source's case, you have the opportunity to check it out first for problems. If you choose to not look before you deploy, what happens next is on you.

Some criminal developers are already using people's blind trust to sneak malware into their programs. For example, the DevOps security firm [JFrog](https://jfrog.com/) recently discovered [17 new JavaScript malicious packages](https://www.zdnet.com/article/malicious-npm-packages-stealing-discord-tokens-highlights-problem-of-malware-distribution-in-public-repositories/) in the NPM repository that deliberately attack and steal a user's Discord tokens. These can then be used on the [Discord communications and digital distribution platform](https://discord.com/).

Is that a lot of work? You bet it is. But, there are tools such as [NPM audit](https://docs.npmjs.com/cli/audit/), [GitHub's DependendaBot](https://github.com/dependabot), and [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/) that can help make it easier. 

In addition, you can simply make sure that before any code goes into production, you simply run a sanity check on it in your [continuous integration/continuous distribution (CI/CD)](https://practical-tech.com/2018/07/10/continuous-integration-and-delivery-tool-basics/) before deploying it to production. 

I mean, seriously, if you'd simply run either of these libraries in the lab they would have blown up during testing and never, ever make it into the real world. It's not that hard!

In the meantime, GitHub suggests you revert back to older, safer versions. To be exact, that's colors.js 1.40 and faker.js 5.5.3. 

As [CodeNotary](https://codenotary.com/), a software supply chain company,  pointed out in a recent blog post, "Software is never complete and the [code base including its dependencies is an always updating document](https://codenotary.com/blog/detect-non-malicious-but-unwanted-dependencies-in-your-software-like-versions-of-fakerjs-or-colorsjs/). That automatically means you need to track it, good and bad, keeping in mind that something good can turn bad." Exactly!

Therefore, they continued, "The only real solution here is to be on top of the dependency usage and deployment. [Software Bill of Materials (SBOMs)](https://www.zdnet.com/article/codenotary-open-source-notarization-service-for-software-bill-of-material-arrives/) can be a solution to that issue, but they need to be tamper-proof, queryable in a fast and scalable manner, and versioned.

CodeNotary suggests, of course, you use their software, [Codenotary Cloud](https://codenotary.com/category/codenotary-cloud/) and the [vcn command-line tool](https://medium.com/vchaincodenotary/vcn-command-line-for-vchain-codenotary-to-sign-code-and-more-d047eb6cc319), for this job. There are other companies and projects that address SBOM as well. If you want to stay safe, moving forward you must--I repeat must--use an SBOM. Supply chain attacks, both from within projects and without, are rapidly becoming one of the main security problems of our day.

**Related Stories:**

* [Malicious npm packages are stealing Discord tokens](https://www.zdnet.com/article/malicious-npm-packages-stealing-discord-tokens-highlights-problem-of-malware-distribution-in-public-repositories/)
* [Codenotary: Notarize and verify your software bill of materials](https://www.zdnet.com/article/codenotary-open-source-notarization-service-for-software-bill-of-material-arrives/)
* [Linux Foundation announces new open-source software signing service](https://www.zdnet.com/article/linux-foundation-announces-new-open-source-software-signing-service/)





## Tags:

#### Threatactor:
[[threatactor.name=BRONZE BUTLER]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Open-source]] [[Javascript]] [[Github]] [[Npm]] [[ZDNet]]

