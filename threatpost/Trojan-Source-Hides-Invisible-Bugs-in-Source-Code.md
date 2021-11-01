# ‘Trojan Source’ Hides Invisible Bugs in Source Code
### The old RLO trick of exploiting how Unicode handles script ordering and a related homoglyph attack can imperceptibly switch the real name of malware.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175891)
+ Date: November 1, 2021  12:28 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/01122223/code_image-e1635783756646.jpg)
Researchers have found a new way to encode potentially evil source code, such that human reviewers see a harmless version and compilers see the invisible, wicked version.


Named “[Trojan Source attacks](https://www.trojansource.codes/),” the method “exploits subtleties in text-encoding standards such as [Unicode](https://home.unicode.org/) to produce source code whose tokens are logically encoded in a different order from the one in which they are displayed, leading to vulnerabilities that cannot be perceived directly by human code reviewers,” Cambridge University researchers Nicholas Boucher and Ross Anderson said in a paper ([PDF](https://trojansource.codes/trojan-source.pdf)) published on Monday.


Boucher and Anderson said that the attacks jeopardize all source code, posing “an immediate threat both to first-party software and of supply-chain compromise across the industry.” They’ve [published](https://github.com/nickboucher/trojan-source) working proofs of concept (PoCs) of attacks in the C, C++, C#, JavaScript, Java, Rust, Go and Python programming languages, though the researchers note that they suspect that the attack will also work against “most other modern languages.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Coordinated Disclosure for Two CVEs
-----------------------------------


The researchers have coordinated disclosure with 19 organizations, many of which are now releasing updates to address the security weakness in code compilers, interpreters, code editors and repositories. Some of those organizations dismissed the notification because it didn’t match vulnerabilities with which they’re more familiar, the researchers noted.


There are two CVEs involved, both of which MITRE issued against the Unicode specification. What the researchers called a “potentially devastating” attack against the Unicode [bidirectional algorithm (BiDi)](https://www.w3.org/International/articles/inline-bidi-markup/uba-basics) through version 14.0 is tracked as [CVE-2021-42574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-42574). BiDi handles the order in which text displays – for example, from left to right with the Latin alphabet, or from right to left with Arabic or Hebrew characters.


A related attack relies on the use of visually similar characters, known as homoglyphs, tracked as [CVE-2021-42694](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-42694).


With regards to the BiDi attack, the paper explains that computer systems need a deterministic way to resolve conflicting directionality when it comes to mixed scripts – i.e., Latin scripts mixed in with Arabic – that have conflicting display orders.


In Unicode, that conflict is typically handled by the BiDi algorithm. But sometimes, the algorithm doesn’t suffice, in which case Unicode uses override control characters that insert invisible characters to enable the switching of character display ordering.


The Old Unicode Right-to-Left Override Shtick
---------------------------------------------


The Unicode BiDi override trick – known as the right-to-left (RLO) technique – is an old attack that keeps getting dusted off. The overrides enable even single-script characters to be displayed in an order that’s different from their logical encoding, the researchers explained – a fact that’s previously been exploited to disguise the real name of a malicious executable spread via email or, in one 2013 attack, [a registry key](https://threatpost.com/sirefef-malware-found-using-unicode-right-to-left-override-technique/102033/).


More recently, in 2018, attackers used RLO to [deliver cryptomining malware](https://threatpost.com/venerable-unicode-technique-used-to-deliver-cryptomining-malware-through-telegram/129929/) by exploiting a zero-day vulnerability in the Telegram messaging application, as Kaspersky researchers [detailed](https://securelist.com/zero-day-vulnerability-in-telegram/83800/) at the time.


What makes these attacks possible is that most “well-designed” programming languages shun arbitrary control characters found in source code, since they screw up the logic, the researchers explained. Random BiDi override characters will typically result in a compiler or interpreter syntax error – errors that are avoided by tucking them into comments or strings, both of which are ignored by compilers and interpreters.


“While both comments and strings will have syntax-specific semantics indicating their start and end, these bounds are not respected by Bidi overrides,” according to the writeup. “Therefore, by placing Bidi override characters exclusively within comments and strings, we can smuggle them into source code in a manner that most compilers will accept.”


Novel Supply-Chain Attack
-------------------------


The researchers suggested that if you put it all together, you get the ability to create perfectly valid, perfectly malicious source code that could be used to create a novel supply-chain attack that can be carried out on source code.


“By injecting Unicode Bidi override characters into comments and strings, an adversary can produce syntactically-valid source code in most modern languages for which the display order of characters presents logic that diverges from the real logic,” they wrote. “In effect, we anagram program A into program B.”


Such an attack would be tough for a human code reviewer to detect, given how kosher the rendered source code looks. “If the change in logic is subtle enough to go undetected in subsequent testing, an adversary could introduce targeted vulnerabilities without being detected,” they continued.


But wait, it gets worse: the paper cautioned: Bidi override characters persist in copy-and-paste functions on most modern browsers, editors and operating systems, meaning that “any developer who copies code from an untrusted source into a protected code base may inadvertently introduce an invisible vulnerability.”


That kind of dangerous code copying has happened before in real-world security exploits, the researchers noted. One example was in June 2020, when at least 26 open-source code repositories were found to be [infected](https://threatpost.com/octopus-scanner-tentacles-github-repositories/156204/) with Octopus Scanner malware, which targets the Apache NetBeans Java integrated development environment (IDE) and was found nesting in GitHub source-code repositories, just waiting to take over developer machines.


Homoglyph Attacks Are Even Worse
--------------------------------


The Trojan Source attacks that rely on BiDi RLO can become even worse if an attacker switches to using homoglyphs, the researchers noted. An early example is a July 2020 campaign in which spammers tried to trick users into [disclosing their PayPal passwords](https://www.zdnet.com/article/paypal-alert-beware-the-paypai-scam-5000109103/) by switching the lowercase “l” in the brand name to the visually similar uppercase “I.”


“These domain attacks become even more severe with the introduction of Unicode, which has a much larger set of visually similar characters, or homoglyphs, than ASCII,” the researchers warned – making homoglyph attacks a favorite of spammers a la the “Paypai” scammers. Homoglyphs being used in URLs is a recognized danger – one that Unicode has focused on in security reports [such as this one](https://www.unicode.org/reports/tr36/tr36-15.html).


“The fact that the Trojan Source vulnerability affects almost all computer languages makes it a rare opportunity for a system-wide and ecologically valid cross-platform and cross-vendor comparison of responses,” the researchers noted. “As powerful supply-chain attacks can be launched easily using these techniques, it is essential for organizations that participate in a software supply chain to implement defenses.”


Matthew Green, an associate professor at the Johns Hopkins Information Security Institute, told [KrebsOnSecurity](https://krebsonsecurity.com/2021/11/trojan-source-bug-threatens-the-security-of-all-code/) that the possibility of exploiting Unicode isn’t surprising, but the fact that so many compilers “happily parse Unicode without any defenses, and how effective their right-to-left encoding technique is at sneaking code into codebases,” does take him aback.. “That’s a really clever trick I didn’t even know was possible. Yikes,” he told security journalist Brian Krebs.


On the plus side, the researchers conducted a widespread vulnerability scan that didn’t turn up any evidence that the security weakness has been exploited so far. On the scary side, there’s no defenses against Trojan Source, Green said, so we should all pray that compiler and code editor developers patch quickly.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Unicode]] [[noted.]] [[code,]] [[supply-chain]] [[didn’t]] [[homoglyphs,]] [[strings,]] [[ThreatPost]]
