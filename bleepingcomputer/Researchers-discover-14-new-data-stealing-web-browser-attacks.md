# Researchers discover 14 new data-stealing web browser attacks
### IT security researchers from Ruhr-Universität Bochum (RUB) and the Niederrhein University of Applied Sciences have discovered 14 new types of 'XS-Leak' cross-site leak attacks against modern web browsers, including Google Chrome, Microsoft Edge, Safari, and Mozilla Firefox.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/researchers-discover-14-new-data-stealing-web-browser-attacks/
+ Date: 2021-12-03T10:34:03-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/03/privacy-eye.jpg)

![Privacy](https://www.bleepstatic.com/content/hl-images/2021/12/03/privacy-eye.jpg)


IT security researchers from Ruhr-Universität Bochum (RUB) and the Niederrhein University of Applied Sciences have discovered 14 new types of 'XS-Leak' cross-site leak attacks against modern web browsers, including Google Chrome, Microsoft Edge, Safari, and Mozilla Firefox.


These types of side-channel attacks are called 'XS-Leaks,' and allow attacks to bypass the 'same-origin' policy in web browsers so that a malicious website can steal info in the background from a trusted website where the user enters information.


"The principle of an XS-Leak is to use such side-channels available on the web to reveal sensitive information about users, such as their data in other web applications, details about their local environment, or internal networks they are connected to," explains the [XS-Leaks wiki](https://xsleaks.dev/).


For example, an XS-Leak attack could help a background site siphon the email inbox contents from an active tab used for accessing webmail.



![The process of an XS-Leak](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/attack(1).jpg)**The process of an XS-Leak**  
*Source: XSinator*
Cross-site leaks aren't new, but as the researchers point out, not all of them have been identified and classified as XS-Leaks, and their root cause remains unclear.


Their research aims to systematically search for new XS-Leaks, evaluate potential mitigations, and generally gain a better understanding of how they work.


Finding new XS-Leaks
--------------------


[The researchers](https://news.rub.de/english/press-releases/2021-12-02-it-security-14-new-attacks-web-browsers-detected) first identified three characteristics of cross-site leaks and evaluated all inclusion methods and leak techniques for a large set of web browsers.


The three main ingredients of all XS-Leaks are inclusion methods, leak techniques, and detectable differences.


After creating a model based on the above, the researchers found 34 XS-Leaks, 14 of which were novel (marked with a plus sign below).



![All of the XS-Leaks identified in the study.](https://www.bleepstatic.com/images/news/u/1220909/Tables/new_attacks_table.jpg)**All of the XS-Leaks identified in the study.**  
*Source: XSinator*
Next, they tested the 34 XS-Leaks against 56 combinations of browsers and operating systems to determine how vulnerable each of them was.


Then they built a web application named XSinator, consisting of three components:


1. A testing site that acts as the attacker page, implementing known and novel X-Leaks
2. A vulnerable web app that simulates the behavior of a state-dependent resource.
3. A database containing all previous test results.

You can visit the [XSinator page](https://xsinator.com/) yourself and run the test to see how well your web browser and OS fare against the 34 X-Leaks.



![Testing against the latest version of Google Chrome](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Testing against the latest version of Google Chrome**  
*Source: BleepingComputer*
You can find a full list of XS-leaks that various browsers are vulnerable to below:



![Sample results from the team's evaluation](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Sample results from the team's evaluation**  
*Source: XSinator*
How to defend against X-Leaks
-----------------------------


Mitigating or addressing the risks that arise from these side-channel attacks need to be resolved by browser developers.


Researchers suggest denying all event handler messages, minimizing error message occurrences, applying global limit restrictions, and creating a new history property when redirection occurs.


Other effective mitigation methods are using X-Frame-Options to prevent iframe elements from loading HTML resources and implementing the CORP header to control if pages can embed a resource.


“COIU, also known as First-Party Isolation (FPI), is an optional security feature that users can enable in FF's expert settings (about:config) and was initially introduced in Tor Browser.” - from [the paper](https://xsinator.com/paper.pdf).


One of the participating researchers, Lukas Knittel, told Bleeping Computer the following:



> 
> "Depending on the website, XS-Leaks can have a severe impact on users. Users can use an up-to-date browser that allows them to disable third-party cookies. This would protect against most XS-Leaks, even when the website doesn't implement new mitigations like COOP, CORP, SameSite Cookies, and so on." - Knittel.
> 
> 
> 


The researcher also said they informed the web browser development teams of their findings, who are now fixing the various issues. The problems have already been fixed in the currently-available versions in some cases.


As for future work, the team believes that new browser features constantly add new potential XS-Leak opportunities, so this is a space of constant interest.


Also, Knittel told us that they might explore the development of a website-scanning tool, but for now, they want to focus on determining how common these flaws are in real-world websites.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Information]] [[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Xs-leaks]] [[Xsinator]] [[Website]] [[Xs-leak]] [[X-leaks]] [[Knittel]] [[Bleeping Computer]]

