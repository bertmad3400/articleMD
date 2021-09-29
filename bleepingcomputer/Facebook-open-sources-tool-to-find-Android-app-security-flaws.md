# Facebook open-sources tool to find Android app security flaws
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/facebook-open-sources-tool-to-find-android-app-security-flaws/)
+ Date: September 29, 2021
+ Author: Sergiu Gatlan


## Article:
![Facebook open-sources tool to find Android app security flaws](https://www.bleepstatic.com/content/hl-images/2021/09/29/Facebook_Mariana_Trench_headpic.jpg)


Facebook today open-sourced a static analysis tool its software and security engineers use internally to find potentially dangerous security and privacy flaws in the company's Android and Java applications.


This security-focused tool, dubbed [Mariana Trench](https://mariana-tren.ch/) (MT), can analyze large codebases of tens of millions of lines of code to spot vulnerabilities before they're introduced in the codebase.


Facebook revealed that its engineers found more than 50% of all security bugs across the company's apps using automated tools similar to Mariana Trench.


How it works
------------


Mariana Trench [works by analyzing the information flow](https://mariana-tren.ch/docs/overview) from "sources" (user sensitive data such as passwords or locations) to "sinks" (functions or methods using data originating from sources).


Mariana Trench is specifically designed to automatically discover such issues, which, in most cases, could lead to severe privacy and security bugs.


"By default Mariana Trench analyzes dalvik bytecode and can work with or without access to the source code," Facebook explains on the tool's [documentation website](https://mariana-tren.ch/docs/overview).


"A flow from sources to sinks indicate that for example user passwords may get logged into a file, which is not desirable and is called as an 'issue' under the context of Mariana Trench," Facebook Software Engineer Dominik Gabi [said](https://engineering.fb.com/2021/09/29/security/mariana-trench/).


Developers and engineers can use the tool to focus on specific security and privacy issues by adjusting and training it by adding new rules and model generators so that it homes in on the areas sensitive data shouldn't end up. 




> 
> The latest of our static analysis tools - Mariana Trench. It’s open source and designed to detect and prevent security bugs in [#Android](https://twitter.com/hashtag/Android?src=hash&ref_src=twsrc%5Etfw) and [#Java](https://twitter.com/hashtag/Java?src=hash&ref_src=twsrc%5Etfw) applications, more here: <https://t.co/1HNlvVghGJ> <https://t.co/prOnVDpnDi>
> 
> 
> — Facebook Security (@fbsecurity) [September 29, 2021](https://twitter.com/fbsecurity/status/1443290418683138049?ref_src=twsrc%5Etfw)


Third code analysis tool open-sourced since 2019
------------------------------------------------


The company previously released two other static code analysis tools designed to detect and prevent security issues for Python code ([Pysa](https://engineering.fb.com/2020/08/07/security/pysa/)) and [Hack](https://hacklang.org/) code ([Zoncolan](https://engineering.fb.com/2019/08/15/security/zoncolan/)).


You can find the Mariana Trench code analysis tool on [GitHub](https://github.com/facebook/mariana-trench/) and [its own dedicated website](https://mariana-tren.ch/), a binary distribution on[PyPI](https://pypi.org/project/mariana-trench/), and a [short tutorial](https://mariana-tren.ch/docs/getting-started) to help get started.


'We built MT to focus particularly on Android applications. There are differences in patching and ensuring the adoption of code updates between mobile and web applications, so they require different approaches," Gabi added.


"While server-side code can be updated almost instantaneously for web apps, mitigating a security bug in an Android application relies on each user updating the application on the device they own in a timely way.


"This makes it that much more important for any app developer to put systems in place to help prevent vulnerabilities from making it into mobile releases, whenever possible."




#### Tags:
[[Facebook]] [[Android]] [[Bleeping Computer]]
