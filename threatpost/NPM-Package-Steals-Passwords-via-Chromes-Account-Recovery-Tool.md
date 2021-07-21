# NPM Package Steals Passwords via Chrome’s Account-Recovery Tool
### In another vast software supply-chain attack, the password-stealer is filching credentials from Chrome on Windows systems via ChromePass.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168004)
+ Date: July 21, 2021  2:11 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/21130321/chrome-password-stealer.jpeg)
A credentials-stealing code bomb that uses legitimate password-recovery tools in Google’s Chrome web browser was found lurking in the npm open-source code repository, waiting to be planted within the sprawling galaxy of apps that pull code from that source.


Researchers caught the malware filching credentials from Chrome on Windows systems. The password-stealer is multifunctional: It also listens for incoming commands from the attacker’s command-and-control (C2) server and can upload files, record from a victim’s screen and camera, and execute shell commands.



npm (originally short for Node Package Manager, or NPM) is the default package manager for the JavaScript runtime environment Node.js, which is built on Chrome’s V8 JavaScript engine. It’s similar to other code repositories such as GitHub, RubyGems and PyPI in that it’s part of a (very long) software supply chain.


“Vast” would be an understatement to describe the ecosystem: npm hosts more than 1.5 million unique packages, and serves up more than 1 billion requests for JavaScript packages per day, to around 11 million developers worldwide.


Abusing Google ChromePass Utility
---------------------------------


Besides textual JavaScript files, npm also holds various types of executables, such as PE, ELF and Mach-O. ReversingLabs researchers, who published their findings in a [Wednesday post](https://blog.secure.software/groundhog-day-npm-package-caught-stealing-browser-passwords), said that during an analysis of the code repository, they found an interesting embedded Windows executable file: a credential-stealing threat. Labeled “Win32.Infostealer.Heuristics”, it showed up in two packages: nodejs\_net\_server and temptesttempfile.


At least for now, the first, main threat is nodejs\_net\_server. Some details:


Using static analysis, researchers found the Win32.Infostealer.Heuristics file in several versions of the nodejs\_net\_server package. Its metadata showed that the file’s original name was “a.exe” and that it was located inside the “lib” folder. A single-letter filename with an extension like that raises a red flag to threat hunters, the researchers noted. Sure enough, a.exe turned out to be a utility called ChromePass: a legitimate tool used to recover passwords stored inside of a Chrome web browser.


chrunlee buffed up the nodejs\_net\_server package through 12 versions until finally upgrading it last December with a script to download the password-stealer, which the developer hosts on a personal website. It was subsequently tweaked to run TeamViewer.exe instead, “probably because the author didn’t want to have such an obvious connection between the malware and their website,” researchers theorized.


chrunlee published the first version “just to test the publishing process of an NPM package,” the analysts described. Three months later, the malware maker implemented remote shell functionality that was polished over several subsequent versions. Then, in April 2020, chrunlee made minor modifications to the shell functionality in versions 1.0.7 and 1.0.8. Finally, in December 2020, version 1.1.0 was updated with a script to download the password-stealing tool.


The Second Problem Package
--------------------------


One of chrunlee’s npm packages – tempdownloadtempfile – also has non-existing links. One of its files – file/test.js – implements the same remote shell functionality as the ones found in versions of the nodejs\_net\_server package, but this package doesn’t perform execution hijacking, and it lacks a persistence mechanism, making its purpose “a bit unclear,” ReversingLabs said.


Fun Developer F-Up
------------------


ReversingLabs analysts dug up a development “fun fact” when picking through nodejs\_net\_server code: Its author, chrunlee, not only authored a credential-stealer but also accidentally published their own, stored login credentials, cheek-to-jowl with the password grabber, opening the author themself up to attack.


“It appears that the published versions 1.1.1 and 1.1.2 from the npm repository include the results of testing the ChromePass tool on the author’s personal computer,” researchers observed. “These login credentials were stored in the ‘a.txt’ file located in the same folder as the password-recovery tool, named ‘a.exe’.”


Another fun fact: That text file has 282 login credentials captured from chrunlee’s browser, some of which may still be valid (ReversingLabs didn’t verify them). And, some of those credentials feature the lamest of lame passwords (“111,” for example) and user names (“admin,” anyone?).


“Just looking at some of the recovered credentials…shows that the author didn’t always care about best password policy practices,” the analysts gracefully understated.


Bad Packages Haven’t Been Removed
---------------------------------


ReversingLabs contacted the npm security team on July 2 to give them a heads-up about the nodejs\_net\_server and tempdownloadtempfile packages and circled back once again last week, on Thursday, since the team still hadn’t removed the packages from the repository. Threatpost reached out to npm Inc., which maintains the repository, and will update this story with any update or feedback.


If they aren’t taken down by the time this article posts, these are the packages and SH1 to look out for:


Earlier npm Hijacks
-------------------


This isn’t the first time that npm has been infiltrated by poisonous code. Earlier this year, three malicious software packages [were published](https://threatpost.com/discord-stealing-malware-npm-packages/163265/) to npm; any applications corrupted by the code could steal tokens and other information from Discord users, researchers said.


In July 2018, an attacker [compromised the npm credentials](https://eslint.org/blog/2018/07/postmortem-for-malicious-package-publishes) of an ESLint maintainer and published malicious versions of the popular “eslint-scope” and “eslint-config-eslint” packages to the npm registry. The malicious code copied the npm credentials of the machine running eslint-scope and uploaded them to the attacker.


A few months later, in November 2018, another malicious package was discovered: it was a dependency to version 3.3.6 of the popular package, “event-stream.” The malicious package, called “flatmap-stream,” contained an encrypted payload that was tailored to [steal Bitcoins](https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident) from the Copay application.


Repositories Are Increasingly Popular Targets
---------------------------------------------


It’s not just npm in cyberattacker crosshairs, mind you. Earlier this month, researchers stumbled on a group of [cryptominers that infiltrated PyPI](https://threatpost.com/cryptominers-python-supply-chain/167135/), aka the Python Package Index (PyPI), a repository of software code created in the Python programming language.


According to the report, the npm infiltration is just the latest example of how developers are putting too much trust in third-party code, reusing libraries to get fast, easy results and “rarely [making] in-depth security assessments before including them into their project.”


Granted, there’s a whole lot of code to suss out.


“This omission is a result of the overwhelming nature, and the vast quantity, of potential security issues found in third-party code,” according to ReversingLabs. “Hence in general, packages are quickly installed to validate whether they solve the problem and, if they don’t, move on to the alternative. This is a dangerous practice, and it can lead to incidental installation of malicious software.”


In the report’s conclusion, ReversingLabs noted that software supply-chain attacks are becoming “a powerful strategy” for malicious actors, with developers being targeted as a critical entry point to their organization and its client base.


“One of the most frequent attack vectors targeting developers is exploitation of public package repositories,” the report warned. “As these repositories have a large number of hosted packages, they offer a good hiding place for malware to lurk in. Repetitive discovery of malicious packages in these repositories has proven that there is a growing need for security solutions that can provide reliable identification and protection against these types of attacks.”


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[npm]] [[ReversingLabs]] [[nodejs_net_server]] [[chrunlee]] [[malware]] [[JavaScript]] [[exe]] [[PyPI]] [[ChromePass]] [[1]] [[ThreatPost]]
