# Mozilla properly fuzzed NSS and still ended up with a simple memory corruption hole
### Bug detection king Tavis Ormandy simply made a really big signature with NSS, and bad things happened.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/mozilla-properly-fuzzed-nss-and-still-ended-up-with-a-simple-memory-corruption-hole/)
+ Date: December 2, 2021
+ Author: Chris Duckett


## Article:
Unknown

![Mozilla logo](https://www.zdnet.com/a/img/resize/6349fffc8338222d643809811ffb33e7ce53b19b/2020/11/19/4da7f391-c50a-4987-b32c-a208cb745974/mozilla-logo.png?fit=bounds&auto=webp)When it comes to fuzzing, Mozilla has plenty of cred, and has been doing so for [some time](https://www.zdnet.com/article/opera-uses-mozilla-fuzzer-to-find-fix-severe-browser-flaw/), and yet, its prized Network Security Services (NSS) library was busted by Google Project Zero's Tavis Ormandy quite easily. 

In a [blog post](https://googleprojectzero.blogspot.com/2021/12/this-shouldnt-have-happened.html) well worth your time, entitled *This shouldn't have happened*, Ormandy found that if NSS was made to create an ASN.1 signature bigger than the maximum 16384 bits it expected, overwriting of memory would occur. 

"What happens if you just ... make a signature that's bigger than that? Well, it turns out the answer is memory corruption. Yes, really," Ormandy wrote. 

"The untrusted signature is simply copied into this fixed-sized buffer, overwriting adjacent members with arbitrary attacker-controlled data. The bug is simple to reproduce and affects multiple algorithms." 

Given the designation CVE-2021-43527, Mozilla [said](https://www.mozilla.org/en-US/security/advisories/mfsa2021-51/) in its advisory that Firefox was not impacted, but the likes of Thunderbird, LibreOffice, Evolution, and Evince were "believed to be impacted". 

In Mozilla's defence, Ormandy said it has a world-class security team, and has been leading the way in fuzzing, but thanks to the modular design of NSS, the library did not have end-to-end testing as each part was fuzzed independently. This was compounded by the fuzzers having a limit of 10,000 bytes on input while NSS has no such limit. 

"This issue demonstrates that even extremely well-maintained C/C++ can have fatal, trivial mistakes," Ormandy wrote. 






The hole has been patched in versions 3.73.0 and 3.68.1 of NSS. 

### Related Coverage

* [Apache HTTP Server Project patches exploited zero-day vulnerability](/article/apache-http-server-project-patches-exploited-zero-day-vulnerability/)
* [Google fixes two high-severity zero-day flaws in Chrome](/article/google-fixes-two-high-severity-zero-day-flaws-in-chrome/)
* [Security company faces backlash for waiting 12 months to disclose Palo Alto 0-day](/article/security-company-faces-backlash-for-waiting-12-months-to-disclose-palo-alto-0-day/)
* [Mozilla Firefox joins browsers implementing Global Privacy Control](/article/mozilla-firefox-joins-browsers-implementing-global-privacy-control/)
* [Mozilla Firefox cracks down on malicious add-ons used by 455,000 users](/article/mozilla-firefox-cracks-down-on-malicious-add-ons-used-by-455000-users/)
* [Bad Santa: Amazon, Facebook top Mozilla's naughty list of privacy-crushing gifts](/article/bad-santa-amazon-facebook-top-mozillas-naughty-list-of-privacy-crushing-gifts/)





#### Tags:
[[Ormandy]] [[Mozilla]] [[Firefox]] [[ZDNet]]
