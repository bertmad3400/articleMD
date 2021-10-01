# Android, Java bug bunting tool Mariana Trench goes open source
### Mariana Trench originated as an internal Facebook tool.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/android-java-bug-bunting-tool-mariana-trench-becomes-open-source/)
+ Date: October 1, 2021
+ Author: Charlie Osborne


## Article:
Unknown

Facebook has released the Mariana Trench bug hunting software to the open source community.


This week, Dominik Gabi, Facebook software engineer [said in a blog post](https://engineering.fb.com/2021/09/29/security/mariana-trench/) that Mariana Trench was originally an internal tool for the company's security engineers but has now been released to the public "to help scale security through building automation." 

Mariana Trench (MT) is a tool for finding vulnerabilities in Android and Java, with a particular focus on examining code in Android applications. According to the tech giant, MT is able to scan "large mobile codebases" and will alert users to potential security problems found in the code by analyzing data flows prior to production.  

MT hones in on data flows as a common source for bugs, whether this is due to incorrect data exposure or collection, or if they contain flaws that allow for the injection of malicious packages. MT scans the source of information and its sinks, tracking possible paths and then will compute models using static analysis to hunt for errors and issues in the codebase. 

"A security engineer would start by broadly defining the boundaries of the data flows she is interested in scanning the codebase for," Facebook explained. "If she wants to find SQL injections, she would need to specify where user-controlled data is entering the code, and where it is not meant to go. However, this is only the start -- defining a rule connecting the two is not enough. Engineers also have to review the identified issues and refine the rules until the results are sufficiently high-signal." 

Facebook warns that [this tool](https://mariana-tren.ch/docs/getting-started/) is only one addition to a security engineer's arsenal, and false positives prior to production need to be considered.  

"In using MT at Facebook, we prioritize finding more potential issues, even if it means showing more false positives," the company says. "This is because we care about edge cases: data flows that are theoretically possible and exploitable but rarely happen in production." 






MT is now available [on GitHub](https://github.com/facebook/mariana-trench/) and a binary distribution has also been released on [PyPI](https://pypi.org/project/mariana-trench/). In addition, Facebook has released the Static Analysis Post Processor ([SAPP](https://github.com/facebook/sapp)), an analysis tool for analyzing MT results.  

###  Previous and related coverage

* [Congress scolds Facebook over the harms its platforms cause: What's next?](https://www.zdnet.com/article/congress-scolds-facebook-over-the-harms-its-platforms-cause-what-next/)  

* [Facebook is the AOL of 2021](https://www.zdnet.com/article/facebook-is-the-aol-of-2021/)  

* [Facebook says Chinese hackers used its platform in targeted campaign to infect, surveil user devices](https://www.zdnet.com/article/facebook-says-chinese-hackers-used-its-platform-in-targeted-campaign-to-infect-surveil-user-devices/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Facebook]] [[ZDNet]]
