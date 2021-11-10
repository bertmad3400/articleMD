# These invisible characters could be hidden backdoors in your JS code
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/these-invisible-characters-could-be-hidden-backdoors-in-your-js-code/)
+ Date: November 10, 2021
+ Author: Ax Sharma


## Article:
![backdoor](https://www.bleepstatic.com/content/hl-images/2021/08/25/hack.jpg)


Could malicious backdoors be hiding in your code, that otherwise appears perfectly clean to the human eye and text editors alike?


A security researcher has shed light on how invisible characters can be snuck into JavaScript code to introduce security risks, like backdoors, into your software.


Not everything is what it seems, in Unicode
-------------------------------------------


Earlier this month, University of Cambridge researchers revealed a clever attack dubbed '[Trojan Source](https://www.bleepingcomputer.com/news/security/trojan-source-attack-method-can-hide-bugs-into-open-source-code/)' for injecting vulnerabilities into the source code, in a way that the malicious code cannot be easily detected by human reviewers.


The method works with some of the most widely used programming languages today and adversaries could use it for supply-chain attacks.


Trojan Source attack, however, leverages the ambiguity introduced by [homoglyphs](https://en.wikipedia.org/wiki/Homoglyph), and the [Unicode bidirectional mechanism (Bidi)](https://www.w3.org/International/articles/inline-bidi-markup/uba-basics)—a feature used for accommodating both left-to-right and right-to-left character sets.


This week, a researcher has disclosed how certain characters could be injected into JavaScript code to introduce invisible backdoors and security vulnerabilities.


Security researcher [Wolfgang Ettlinger](https://twitter.com/ettisan), who is also the Director of Certitude Consulting, surmised "what if a backdoor literally cannot be seen and thus evades detection even from thorough code reviews?"


And surely enough, it didn't take long for Ettlinger to come up with a proof of concept (PoC) code shown below. Can you spot the invisible backdoor?


"The script implements a very simple network health check HTTP endpoint that executes *ping -c 1 google.com* as well as *curl -s http://example.com* and returns whether these commands executed successfully. The optional HTTP parameter *timeout* limits the command execution time," explains the researcher in his [blog post](https://certitude.consulting/blog/en/invisible-backdoor/).


Turns out, the backdoor is on the following lines, where the invisible character U+3164 aka '[Hangul Filler](https://www.compart.com/en/unicode/U+3164)' resides.


Being a Unicode "letter," the Hangul Filler can be trivially used as a JavaScript variable name.


In effect, this alters the logic and workflow of the two lines than what was previously understood.


"A [destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) is used to deconstruct the HTTP parameters from `req.query`," explains the researcher.


Previously, it appeared as if the *timeout* parameter was the only parameter being unpacked from the *req.query* attribute. But in actuality, an additional variable denoted by the invisible character is also retrieved.


"If a HTTP parameter named [invisible character] is passed, it is assigned to the invisible variable. Similarly, when the *checkCommands* array is constructed, this [invisible variable] is included into the array," continues Ettlinger.


All of this means, assuming the above JavaScript code was placed on a web server, reachable at *host:8080*, an attacker could sneak in a GET parameter representing the invisible variable, in its URL-encoded form, to execute arbitrary code:


"Each element in the array, the hardcoded commands as well as the user-supplied parameter, is then passed to the *exec* function. This function executes OS commands," states Ettlinger.


Another interesting PoC example shared by Ettlinger in his report is a conditional statement, that leverages homoglyphs:


Except, the ǃ= characters are not the same as the "[not equal to](https://en.wikipedia.org/wiki/Operators_in_C_and_C%2B%2B#Comparison_operators/relational_operators)" operator we are used to, because 'ǃ' is not an exclamation mark but a Unicode character known as [Alveolar click](https://en.wikipedia.org/wiki/Alveolar_click).


Once again, the result of this expression will always be 'true' as the *environment* will actually be set equal to *ENV\_PROD,* with the interpreter almost ignoring the 'ǃ'. 


"There are many other characters that look similar to the ones used in code which may be used for such proposes (e.g. “／”, “−”, “＋”, “⩵”, “❨”, “⫽”, “꓿”, “∗”). Unicode calls these characters '[confusables](https://unicode.org/reports/tr36/#visual_spoofing)'," states Ettlinger.


Your text editor's mileage may vary
-----------------------------------


Depending on your development tookit, not all text editors may be able to highlight the mysterious or invisible characters.


Syntax highlighting isn't a reliable approach as invisible characters may not be shown at all, let alone be colorized by the text editor of an IDE.


"The attack requires the IDE/text editor (and the used font) to correctly render the invisible characters," explains Ettlinger.


"At least Notepad++ and VS Code render it correctly (in VS Code the invisible character is slightly wider than ASCII characters). The script behaves as described at least with Node 14."


However, some IDEs do seem to be clearly highlighting these invisible characters, [including](https://news.ycombinator.com/item?id=29171903) JetBrains WebStorm and PhpStorm, making this attack more difficult to pull off:



![Invisible characters spotted by some IDEs](https://www.bleepstatic.com/images/news/u/1164866/2021/Nov-2021/js-invisible-backdoor/invisible-chars-IDE-text-editor.jpg)**Invisible characters spotted by some IDEs like JetBrains**(Imgur)
Playing around with invisible Unicode characters isn't new knowledge either.


Previously, a Rust developer tried using these characters for a prank, which failed, [possibly](https://news.ycombinator.com/item?id=29171785) because of Rust's "compiler-level defenses against these glyph based attacks."




> 
> I hate Rust, it won't let me prank my coworkers [pic.twitter.com/BzHKeBw2uv](https://t.co/BzHKeBw2uv)
> 
> 
> — Gulshan (@skyslasher11) [July 21, 2019](https://twitter.com/skyslasher11/status/1152824207555698688?ref_src=twsrc%5Etfw)


Last month, the popular Node.js library 'ua-parser-js' was hijacked, with threat actors injecting code in its npm releases [to install cryptominers and password stealers](https://www.bleepingcomputer.com/news/security/popular-npm-library-hijacked-to-install-password-stealers-miners/) on the victim's machines.


And just last week, malicious releases of [hijacked 'coa' and 'rc' libraries](https://www.bleepingcomputer.com/news/security/popular-coa-npm-library-hijacked-to-steal-user-passwords/) broke React pipelines around the world, as first reported by BleepingComputer.


Luckily, these supply-chain attacks were caught because despite containing obfuscated code, it remained possible for a human reviewer or a bot to spot malicious activity—especially since software builds around the world started breaking as soon as the hijacked versions of these packages hit npm.


Similarly, in April this year, [misleading 'patches'](https://www.bleepingcomputer.com/news/security/linux-bans-university-of-minnesota-for-committing-malicious-code/) made by the University of Minnesota researchers that in turn introduced vulnerabilities were eventually caught by the Linux kernel maintainers.


But, what happens when threat actors are able to hide backdoors in quasi-benign code that can't be easily spotted?


"The Cambridge team proposes restricting Bidi Unicode characters [as a solution to Trojan Source]. As we have shown, homoglyph attacks and invisible characters can pose a threat as well," says Ettlinger.


"It might therefore be a good idea to disallow any non-ASCII characters," advises the researcher.




#### Tags:
[[Unicode]] [[Ettlinger.]] [[JavaScript]] [[HTTP]] [[backdoors]] [[code,]] [["The]] [[Bleeping Computer]]
