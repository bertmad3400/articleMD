# Malicious npm Code Packages Built for Hijacking Discord Servers
### The lurking code-bombs lift Discord tokens from users of any applications that pulled the packages into their code bases.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176886
+ Date: 2021-12-08T22:30:04+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/01/22125253/NPM-e1611337986238.jpg)

A series of malicious packages in the Node.js package manager (npm) code repository are looking to harvest Discord tokens, which can be used to take over unsuspecting users’ accounts and servers.


The npm repository is an open-source home for JavaScript developers to share and reuse code blocks. The packages can represent a supply-chain threat given that they can be used as building blocks in various web applications. Any applications corrupted by malicious code can attack its users.


According to the JFrog Security research team, in this case a set of 17 malicious packages were published, with varying payloads and tactics. However, they were all built to target Discord, the virtual meeting platform used by 350 million users that enables communication via voice calls, video calls, text messaging and files.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“The packages’ payloads are varied, ranging from infostealers up to full remote-access backdoors,” researchers said in a [Wednesday advisory](https://jfrog.com/blog/malicious-npm-packages-are-after-your-discord-tokens-17-new-packages-disclosed/). “Additionally, the packages have different infection tactics, including [typosquatting](https://threatpost.com/attackers-use-typo-squatting-to-steal-npm-credentials/127235/), dependency confusion and trojan functionality.”


There are a few reasons, apart from its massive user base, that Discord is an attractive target, researchers noted:


1. **Using the platform as part of an attack.** Discord servers are often used as anonymous command-and-control (C2) servers, controlling a remote access trojan (RAT) or even an entire botnet. Alternatively, compromised Discord servers can also be used as an anonymous exfiltration channel, since any attack using these credentials would be traced to the legitimate user and not the attacker.
2. **Spreading malware to Discord users.** Hacked Discord accounts can be used for social-engineering purposes, to keep spreading malware – either manually or automatically via a worm. “A victim is much more likely to accept (and execute) an arbitrary file from a friend’s account on Discord, versus a file sent by a complete stranger,” according to JFrog.
3. **Selling stolen premium accounts.** Attackers may be targeting Discord accounts that have purchased Nitro in order to resell them for cheap in an online marketplace. Discord Nitro costs $100 per year and offers enhancements like emojis and badges, plus the option to “boost” call and video quality on chosen servers.


**Building a Discord-Stealing Malicious Package**
-------------------------------------------------


JFrog researchers noted that it’s easy to find Discord token grabbers on GitHub, which come complete with instructions. These can be used to develop a malware-laden package.


“Any novice hacker can do this with ease in a matter of minutes,” they said. “It’s important to note these payloads are less likely to be caught by antivirus solutions, versus a full-on RAT backdoor, since a Discord stealer does not modify any files, does not register itself anywhere (to be executed on next boot, for example) and does not perform suspicious operations such as spawning child processes.”


To lure users into downloading the packages, the malicious projects employ various tactics. For instance, two of the 17 packages, called “discord-lofy” and “discord-selfbot-v14,” masquerade as modifications of the legitimate library discord.js, which enables interaction with the Discord API.


“The malware’s author took the original discord.js library as the base and injected obfuscated malicious code into the file src/client/actions/UserGet.js,” according to JFrog, which added, “In classic trojan manner, the packages attempt to misdirect the victim by copying the README.md from the original package.”


Another, dubbed the “fix-error” package, claims to “fix errors in discord selfbot.” In actuality, it uses an obfuscated version of the PirateStealer tool, which steals private data stored in the Discord client by injecting malicious JavaCcript code – such as credit cards, login credentials and personally identifiable information (PII).


“The injected code spies on the user and sends back the stolen information to a hardcoded Webhook address,” researchers explained.


Fully 10 of the packages eschew any legitimate or trojanized functionality at all, and instead just contain a small snippet of malicious code, researchers said. These all steal environment variables, which are dynamic-named values that can affect the way running processes will behave on a computer.


“This is a dangerous payload since environment variables are a prime location for keeping secrets that need to be used by the runtime (as they are safer than keeping the secrets in cleartext storage or passing the secrets via command-line variables),” researchers explained. “The types of machines targeted by these malicious packages, namely developer and CI/CD machines, are very likely to contain such secrets and access keys in the user’s environment.”


The npm code maintainers have removed the flagged packages, which nonetheless live on in any applications they’re built into.


**Package Repositories in the Crosshairs**
------------------------------------------


Using malicious packages as a cyberattack vector has become more and more common, and not just in npm. Here’s a rundown of recent discoveries:


* In December, RubyGems, an open-source package repository and manager for the Ruby web programming language, took two of its software packages offline after they were found to be laced with Bitcoin-stealing malware.
* In January, other Discord-stealing malware [was discovered](https://threatpost.com/discord-stealing-malware-npm-packages/163265/) in npm.
* In March, researchers [spotted](https://threatpost.com/malicious-code-bombs-amazon-lyft-slack-zillow/164455/) malicious packages targeting internal applications for Amazon, Lyft, Slack and Zillow (among others) inside the npm public code repository – all of which exfiltrated sensitive information. That attack was based on research from security researcher Alex Birsan, who found that it’s possible to [inject malicious code](https://threatpost.com/supply-chain-hack-paypal-microsoft-apple/163814/) into common tools for installing dependencies in developer projects. Such projects typically use public repositories from sites like GitHub. The malicious code then can use these dependencies to propagate malware through a targeted company’s internal applications and systems.
* In June, a group of cryptominers was found [to have infiltrated](https://threatpost.com/cryptominers-python-supply-chain/167135/) the Python Package Index (PyPI), which is a repository of software code created in the Python programming language. Researchers found six different malicious packages hiding in PyPI, which had a collective 5,000 downloads.
* And in July, a credentials-stealing package that uses legitimate password-recovery tools in Google’s Chrome web browser [was found lurking in](https://threatpost.com/npm-package-steals-chrome-passwords/168004/)npm.


“We are witnessing a recent barrage of malicious software hosted and delivered through open-source software repositories,” according to JFrog researchers. “Public repositories have become a handy instrument for malware distribution: the repository’s server is a trusted resource, and communication with it does not raise the suspicion of any antivirus or firewall. In addition, the ease of installation via automation tools such as the npm client, provides a ripe attack vector.”


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** ***[REGISTER TODAY](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)*** ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This [LIVE, interactive Threatpost Town Hall](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article), sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***for the LIVE event!***


 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Npm]] [[Malware]] [[Jfrog]] [[“the]] [[Open-source]] [[ThreatPost]]

