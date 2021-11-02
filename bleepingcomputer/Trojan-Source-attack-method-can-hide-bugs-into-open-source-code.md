# 'Trojan Source' attack method can hide bugs into open-source code
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/trojan-source-attack-method-can-hide-bugs-into-open-source-code/)
+ Date: November 1, 2021
+ Author: Ionut Ilascu


## Article:
!['Trojan Source' attack can smuggle bugs into open-source code](https://www.bleepstatic.com/content/hl-images/2021/11/01/source-code.jpg)


Academic researchers have released details about a new attack method they call “Trojan Source” that allows injecting vulnerabilities into the source code of a software project in a way that human reviewers can’t detect.


Trojan Source relies on a simple trick that does not require modifying the compiler to create vulnerable binaries.


The method works with some of the most widely used programming languages today and adversaries could use it for supply-chain attacks.


### Abusing text-encoding standards


Researchers from the University of Cambridge, United Kingdom, disclosed and demonstrated the “Trojan Source” class of attacks that could compromise first-party software and supply chains.


The examples they provide are for projects written in C, C++, C#, JavaScript, Java, Rust, Go, and Python where an attacker can target the encoding of source code files to inject vulnerabilities.


“The trick is to use Unicode control characters to reorder tokens in source code at the encoding level,” [reveals Nicholas Boucher](https://trojansource.codes/), one of the researchers that discovered Trojan Source.


“We have discovered ways of manipulating the encoding of source code files so that human viewers and compilers see different logic. One particularly pernicious method uses Unicode directionality override characters to display code as an anagram of its true logic,” [explains Ross Anderson](https://www.lightbluetouchpaper.org/2021/11/01/trojan-source-invisible-vulnerabilities/), the other researcher behind testing the Trojan Source attack method.


By using control characters embedded in comments and strings, a threat actor can reorder the source code to change its logic in a way that creates an exploitable vulnerability.


### Bidirectional and homoglyph attack


The researchers showed that one way this can be achieved is by using Unicode controls for bidirectional text (e.g. LRI -left-to-right isolate, and RLI -right-to-left isolate) to dictate the direction in which the content is displayed. This method is now tracked as [CVE-2021-42574](https://nvd.nist.gov/vuln/detail/CVE-2021-42574).


The bidirectional (Bidi) controls LRI and RLI are invisible characters, and they are not the only ones. By injecting these instructions, a compiler can compile code that is completely different from what a human sees.


In the image below, using the RLI/RLI controls inside the string the second line is compiled while the human eye reads it as a comment that the compiler would ignore.



![Trojan Source attack - Bidi override characters](https://www.bleepstatic.com/images/news/u/1100723/2021/TrojanSourceAttack02.jpg)source: [Nicholas Boucher](https://trojansource.codes/)
Injecting Unicode Bidi override characters into comments and strings, an adversary could “produce syntactically-valid source code in most modern languages for which the display order of characters presents logic that diverges from the real logic.”


Another way is a homoglyph attack ([CVE-2021-42694](https://nvd.nist.gov/vuln/detail/CVE-2021-42694)), where two different characters have a similar visual representation, such as the number “zero” and the letter “O,” or the lowercase “L” and the uppercase “i.”


In a homoglyph Trojan Source attack as exemplified below, the human eye will see both functions identical, while the compiler distinguishes between the Latin "H" and the Cyrillic "H" and treats the code as having two different functions, so the outcome will not be the same.


![Trojan Source attack - Homoglyph](https://www.bleepstatic.com/images/news/u/1100723/2021/TrojanSourceAttack_03.jpg)


In a [paper](https://trojansource.codes/trojan-source.pdf) [PDF] detailing the new Trojan Source attack method, the researchers highlight that the bidirectional (Bidi) override characters persist through copy/paste action on most browsers, editors, and operating systems.


The researchers tested the Trojan Source attack against multiple code editors and web-based repositories that are commonly used in programming and found that their method worked on many of them.


![Trojan Source attack - vulnerable compilers and repository front ends](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)


Following the principle of using Bidi overrides to create code that is valid when reordered, the researchers found at least three techniques that allow exploiting of the source code:


* Early Returns - hide a genuine ‘return’ statement in a comment so that it can cause a function to return earlier than it appears to
* Commenting Out - trick human review by placing important code, such as a conditional, in a comment so that it is disregarded by the compiler or the interpreter
* Stretched Strings - reverse-order the code to make it seem to be outside a string literal


One way to defend against Trojan Source is to reject the use of control characters for text directionality in language specifications and in compilers that implement the languages.



"In most settings, this simple solution may well be sufficient. If an application wishes to print text that requires Bidi overrides, developers can generate those characters using escape sequences rather than embedding potentially dangerous characters into source code"



### Coordintated disclosure


On July 25, the researchers informed multiple maintainers of products found to be impacted by the Trojan Source attack method and set a 99-day embargoed disclosure period.


The CERT Coordination Center also received a vulnerability report and assisted with the coordintated disclosure by providing a shared communication platform for vendors implementing defenses.


Following their report, the researchers received an average of $2,246 in bug bounties from five of the recipients, although 11 of them had a bug bounty program.


At the moment, multiple compilers are unable to stop the Trojan Source attack method, despite almost two dozen software suppliers being aware of the threat.


Since many maintainers are still to implement a patch, the two researchers recommend governments and companies identify their suppliers and pressure them into adopting the necessary defenses.



"The fact that the Trojan Source vulnerability affects almost all computer languages makes it a rare opportunity for a system-wide and ecologically valid cross-platform and crossvendor comparison of responses"



The researchers added that three companies that maintain code repositories are currently deploying defenses against Trojan Source.


In a [repository on GitHub](https://github.com/nickboucher/trojan-source), they provide proof-of-concept (PoC) scripts that demonstrates how much of a threat the Trojan Source attack can be.




#### Tags:
[[Unicode]] [[homoglyph]] [[Bleeping Computer]]
