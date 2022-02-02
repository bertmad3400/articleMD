# Thousands of Malicious npm Packages Threaten Web Apps
### Attackers increasingly are using malicious JavaScript packages to steal data, engage in cryptojacking and unleash botnets, offering a wide supply-chain attack surface for threat actors.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178137
+ Date: 2022-02-02T14:00:23+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/01/22125253/NPM-e1611337986238.jpg)

More than 1,300 malicious packages have been identified in the most oft-downloaded JavaScript package repository used by developers, [npm](https://www.npmjs.com/), in the last six months — a rapid increase that showcases how npm has become a launchpad for a range of nefarious activities.


New research from open-source security and management firm [WhiteSource](https://www.whitesourcesoftware.com/) has discovered the disturbing increase in the delivery of malicious npm packages, which are used as building blocks for web applications. Any app using a malicious code block could be serving up data theft, cryptojacking, botnet delivery and more to its users.


Out of the malicious packages found, 14 percent were designed to steal sensitive information like credentials, while nearly 82 percent of those packages were performing “reconnaissance,” which involved adversaries actively or passively gathering information that can be used to support targeting, the firm said.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

Because npm packages in general are being downloaded upwards of 20 billion times a week—and thus installed across countless web-facing components of software and applications across the world–exploiting them means a sizeable playing field for attackers, researchers said in their [Wednesday report](https://www.whitesourcesoftware.com/whitesource-npm-threat-report-for-javascript-package-registry/). An average of 32,000 new npm package versions are published every month (17,000 daily), and a full 68 percent of developers depend upon it to create rich online functionality, according to WhiteSource.


That level of activity enables threat actors to launch a number of software supply-chain attacks, researchers said. Accordingly, WhiteSource investigated malicious activity in npm, identifying more than 1,300 malicious packages in 2021 — which were subsequently removed, but may have been brought into any number of applications before they were taken down.


“Attackers are focusing more efforts on using npm for their own nefarious purposes and targeting the software supply chain using npm,” they wrote in the report. “In these supply-chain attacks, adversaries are shifting their attacks upstream by infecting existing components that are distributed downstream and installed potentially millions of times.”


To boot, with so many npm packages being released monthly, it’s also easy for some vulnerabilities to slip through the cracks, researchers noted.


**Why Attack npm?**
-------------------


JavaScript is the most commonly used programming language, and there are about 16.4 million JavaScript developers globally, according to WhiteSource.


Its widespread use and deployment across applications and systems that use the internet also makes the JavaScript ecosystem a major target for attackers, researchers said.


Indeed, this is something that was clearly evidenced in the ongoing spate of attacks on the now-infamous [Log4J](https://threatpost.com/zero-day-in-ubiquitous-apache-log4j-tool-under-active-attack/176937/) vulnerability[, Log4Shell](https://threatpost.com/log4j-vulnerability-pressures-security-world/177721/)–a scenario in which threat actors have pounced on an opportunity to exploit [a flaw](https://www.netspi.com/news/netspi-in-the-news/threatpost-log4shell-is-spawning-even-nastier-mutations/) in a ubiquitous JavaScript logging library. The incident has caused and [continues to cause](https://threatpost.com/microsoft-rampant-log4j-exploits-testing/177358/) numerous headaches for security professionals.


JavaScript packages—installed using tools like npm–are a popular attack vector that can cause a similar ripple effect across IT environments if attacks aren’t kept in check, according to WhiteSource.


Package registries like npm store packages, the metadata associated with them, and the configurations that are needed to install them, as well as track versions of packages. Npm itself is one of the most popular package managers and registries, containing more than 1.8 million active packages, each of which has an average of 12.3 versions, researchers said.


However, though npm and other registries play an integral role in the JavaScript development process, “there is a minimum standard of security associated with them” because most of them are maintained and verified by open-source communities or consortiums, researchers said. This makes them ripe for exploitation by attackers, they said.


Indeed, attackers are certainly on to the malicious opportunity npm represents and have already targeted its popular registries in several high-profile attacks last year.


In January, attackers used npm to spread the CursedGrabber malware [that could steal Discord tokens](https://threatpost.com/discord-stealing-malware-npm-packages/163265/) and thus enable attacks on users’ accounts and servers. Then in July, researchers found [a malicious npm package](https://threatpost.com/npm-package-steals-chrome-passwords/168004/) that was stealing passwords via Chrome’s account-recovery tool.


In December, attackers [used npm to target Discord](https://threatpost.com/malicious-npm-code-packages-discord/176886/) again, hiding malicious code within the package manager to harvest Discord tokens that can be used to take over unsuspecting users’ accounts and servers.


**Common Malware, Targets and Impact**
--------------------------------------


WhiteSource researchers identified some of the most common malware hidden in malicious npm packages that they observed in the report, with payloads that can steal credentials or crypto and run botnets among the top offenders.


Some of the malicious packages and their functionality that WhiteSource identified in its investigation include the following:


–mos-sass-loader and css-resources-loader, which engage in brandjacking for remote code execution (RCE);


–circle-admin-web-app and browser-warning-ui, which select external packages including malware for download;


–@grubhubprod\_cookbook, which engages in dependency confusion aimed at entering Grubhub company data;


— H98dx,a remote shell executable that runs upon install to infect machine; and


–Azure-web-pubsub-express, which enables data aggregation that collects host information.


Researchers also described a supply-chain attack that they observed in October using a popular npm library, ua-parser-js, which is used to parse user agent strings to identify a user’s browser, OS, device and other attributes. The library has more than 7 million weekly downloads, they said.


Threat actors used ua-parser-js to leverage the software supply chain and gain access to sensitive data, as well as vulnerable enterprise resources in the cloud, researchers explained.


“Attackers inserted malicious code into three versions of ua-parser-js after seemingly taking over the developer’s npm account,” researchers wrote. “Three new versions of this package were released in an attempt to get users to download them.”


While the previously clean version of the package was 0.7.28, the attacker published identical 0.7.29, 0.8.0 and 1.0.0 packages, “each containing malicious code that was activated upon installation,” they explained.


The author of the package responded quickly to mitigate attacks and attempt to minimize the number of people who were inadvertently installing a malicious package by publishing 0.7.30, 0.8.1 and 1.0.1, researchers added.


Developers should be especially vigilant when downloading npm packages on weekends, as they are the most time of the week for attackers to release malicious packages, researchers found. This is likely because less people are working and thus online, making it easier for their activity to go unnoticed, they said.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.city.name=Quito]] [[victim.country.name=Ecuador]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Npm]] [[Javascript]] [[Whitesource]] [[Supply-chain]] [[Malware]] [[Ua-parser-js]] [[ThreatPost]]

