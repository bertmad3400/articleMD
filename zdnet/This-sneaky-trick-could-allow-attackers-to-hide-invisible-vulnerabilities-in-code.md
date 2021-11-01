# This sneaky trick could allow attackers to hide 'invisible' vulnerabilities in code
### Rust programming language project has an update that addresses Unicode security flaw that affects it, Java, Python and more.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/this-sneaky-trick-could-allow-attackers-to-hide-invisible-vulnerabilities-in-code/)
+ Date: November 1, 2021
+ Author: Liam Tung


## Article:
Unknown

If you're using the Rust programming language — or JavaScript, Java, Go or Python — in a project, you may want to check for potential differences between reviewed code versus the compiled code that's been output. 

The Rust Security Response working group (WG) has flagged a strange security vulnerability that is being tracked as CVE-2021-42574 and is urging developers to upgrade Rust version 1.56.1. 

News of the [obscure bug was disseminated in a mailing list today](https://groups.google.com/g/rustlang-security-announcements/c/bKPH8XYMvJU). The Rust project has also [flagged the Unicode "bidirectional override" issue in a blogpost](https://blog.rust-lang.org/2021/11/01/cve-2021-42574.html). But it's a general bug that doesn't affect just Rust but all code that's written in popular languages that use Unicode.  

Since it is Unicode, this bug affects not just Rust but other top languages, such as Java, JavaScript, Python, C-based languages and code written in other modern languages, [according to security researcher Ross Anderson.](https://www.lightbluetouchpaper.org/2021/11/01/trojan-source-invisible-vulnerabilities/) 

Open-source projects such as operating systems often rely on human review of all new code to detect any potentially malicious contributions by volunteers. But the security researchers at Cambridge University said they have discovered ways of manipulating the encoding of source code files so that human viewers and compilers see different logic. 

"We have discovered ways of manipulating the encoding of source code files so that human viewers and compilers see different logic. One particularly pernicious method uses Unicode directionality override characters to display code as an anagram of its true logic. We've verified that this attack works against C, C++, C#, JavaScript, Java, Rust, Go, and Python, and suspect that it will work against most other modern languages," [writes Anderson, detailing this bug and a similar "homoglyph" issue tracked as CVE-2021-42694](https://www.lightbluetouchpaper.org/2021/11/01/trojan-source-invisible-vulnerabilities/).

"The trick is to use Unicode control characters to reorder tokens in source code at the encoding level. These visually reordered tokens can be used to display logic that, while semantically correct, diverges from the logic presented by the logical ordering of source code tokens. Compilers and interpreters adhere to the logical ordering of source code, not the visual order," the [researchers said](https://trojansource.codes/). The attack is to use control characters embedded in comments and strings to reorder source code characters in a way that changes its logic.






Software development is international and Unicode — a foundation for text and emoji — supports left-to-right languages, such as English, and right-to-left languages, such as Persian. It does this through "bidirectional override", an invisible feature called a codepoint that enables embedding left-to-right words inside a right-to-left sentence and vice versa. 

While they're normally used to embed a word inside a sentence constructed in the reverse direction, Anderson and Microsoft security researcher Nicholas Boucher discovered that they could be used to change how source code is displayed in certain editors and code review tools. 

It means that reviewed code can be different than the compiled code and shows how organizations could be hacked through tampered open-source code. 

"This attack is particularly powerful within the context of software supply chains. If an adversary successfully commits targeted vulnerabilities into open source code by deceiving human reviewers, downstream software will likely inherit the vulnerability," the researchers warn.

Google [has found that open-source software supply chain attacks have escalated in the past year](https://www.zdnet.com/article/open-source-security-google-has-a-new-plan-to-stop-software-supply-chain-attacks/). 

Rust isn't a widely used programming language, but it has been adopted for systems (versus application) programming by [Google, Facebook, Microsoft, Amazon Web Services (AWS) and more](https://www.zdnet.com/article/linux-foundation-well-host-mozillas-rust-programming-language-based-servo-web-engine/?ftag=COS-05-10aaa0h&utm_campaign=trueAnthem:%20Trending%20Content&utm_medium=trueAnthem&utm_source=facebook&fbclid=IwAR3y9NWOJnepqGmbe4TAkTd6KYf9xnKc2GjvxSMQkJLKubNqn20bU3qOlj0) for its memory-related safety guarantees. 

"Rust 1.56.1 introduces two new lints to detect and reject code containing the affected codepoints. Rust 1.0.0 through Rust 1.56.0 do not include such lints, leaving your source code vulnerable to this attack if you do not perform out-of-band checks for the presence of those codepoints," the Rust project said. 

The Rust project analyzed its add-on software packages, dubbed "crates" — it reviewed everything published on crates.io from 17 October 2021 — and determined that five crates have the affected codepoints in their source code. However, it didn't find any malicious codepoints.





#### Tags:
[[Unicode]] [[languages,]] [[logic.]] [[JavaScript,]] [[Java,]] [[ZDNet]]
