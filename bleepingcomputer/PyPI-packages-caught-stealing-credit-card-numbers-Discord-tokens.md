# PyPI packages caught stealing credit card numbers, Discord tokens
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/pypi-packages-caught-stealing-credit-card-numbers-discord-tokens/)
+ Date: July 30, 2021
+ Author: Ax Sharma


## Article:
![python red](https://www.bleepstatic.com/content/hl-images/2020/12/15/Python_malware.jpg)


The Python Package Index (PyPI) registry has removed several Python packages this week aimed at stealing users' credit card numbers, Discord tokens, and granting code execution capabilities to attackers.


These malicious packages were published under three different PyPI accounts and are estimated to have scored over 30,000 downloads put together, according to the researchers' report.


Malware steals credit card numbers, browser files, Discord tokens
-----------------------------------------------------------------


This week, security researchers Andrey Polkovnichenko, Omer Kaspi and Shachar Menashe at JFrog have analyzed several malicious Python packages that they caught on the PyPI registry.


These packages are as follows, divided into categories:


Most of the packages steal Discord tokens, credit card numbers, and web-browser files, although some provide attackers with code execution abilities.


All of the packages in the list use simple obfuscation techniques, akin to those used by most novice Python malware, say the researchers.


The Python code is base64-encoded and passed to *eval()* after being decoded.



![eval example](https://www.bleepstatic.com/images/news/u/1164866/2021/Jul-2021/jfrog-pypi-malware/eval-example.jpg)**An example excerpt from the *noblesse2* package showing simple obfuscation**(JFrog)
However, "the packages *aryi* and *suffer* were obfuscated using PyArmor, suggesting that malware developers are experimenting with different obfuscation methods," state the researchers in their [report](https://jfrog.com/blog/malicious-pypi-packages-stealing-credit-cards-injecting-code/).


As seen by BleepingComputer, the *noblesse* malware family falsely advertises itself as optimization packages, with messages like "This Module Optimises your PC For Python," both inside Python packages, and on the PyPI pages (now removed):



![noblesse pypi](https://www.bleepstatic.com/images/news/u/1164866/2021/Jul-2021/jfrog-pypi-malware/noblesse.jpg)***noblesse* malware falsely touts itself as a code optimizer**(BleepingComputer)
Different packages under the *noblesse* family obtain the user's Discord authentication tokens and web-browser files that store credit card numbers.


Such credit card numbers are often saved in web browsers by users aiming to use them later via "autocomplete."



![credit card stored via autocomplete](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Credit cards stored in web browser for later use via "autocomplete"**(JFrog)
"An authentication token allows the attacker to impersonate the user that originally held the token (similar to HTTP session cookies)."


"The payload stealing the tokens is based on the infamous [dTGPG](https://pastebin.com/0q0Fk0Ej) (Discord Token Grabber Payload Generator) payload."


"This is a generator tool that was never released publicly, but the payloads (the individualized token grabbers) are shared publicly, and some examples were also uploaded to [GitHub](https://github.com/wodxgod/Discord-Token-Grabber)," state the researchers.


The Discord token stealers are similar in their functionality (but not the code) to [npm Discord stealers](https://www.bleepingcomputer.com/news/security/malicious-npm-project-steals-discord-accounts-browser-info/) BleepingComputer has previously reported on.


Not your usual Pythagorean theorem
----------------------------------


Yet another strand of malware loaded by some of these packages was aimed at reconnaissance activities to gather system information.


Although these packages have now been removed from PyPI, as a security researcher at Sonatype, I was able to peek inside their archived copies stored by Sonatype's automated malware detection systems.


This particular family of *noblesse* is designated to capture screenshots, Windows version and license key information, IP address, computer name/user name, etc., and upload these pieces of information to a Discord Webhook:



![recon pypi sonatype](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Screenshot capturing and info-stealing capabilities inside *noblesse2***(BleepingComputer)
The "pytagora" package, on the other hand, contains the [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem) formula, along with some base64 payload snuck in.


The payload when executed attempts to connect to a private IP address on TCP port 9009 and "listens" for incoming commands.


The reasons behind the attacker's choice of a private IP address (172.16.60.80) or what the IP represents are not clear.



![pytagora pypi code](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)***pytagora* package with encoded (left) base64 payload, which when decoded (right) connects to a private IP address**  

Source: BleepingComputer
Another day, another malicious package
--------------------------------------


Over the last few months, open-source software registries including, [npm](https://www.bleepingcomputer.com/news/security/new-linux-macos-malware-hidden-in-fake-browserify-npm-package/), PyPI and [RubyGems](https://www.bleepingcomputer.com/news/security/malicious-rubygems-packages-used-in-cryptocurrency-supply-chain-attack/) have persistently been hit with malware or [unwanted content](https://www.bleepingcomputer.com/news/security/spammers-flood-pypi-with-pirated-movie-links-and-bogus-packages/).


This report from JFrog comes just a few weeks after malicious [cryptomining packages](https://www.bleepingcomputer.com/news/security/malicious-pypi-packages-hijack-dev-devices-to-mine-cryptocurrency/) were caught by Sonatype on PyPI.


And, just this month, following an advisory from ReversingLabs, npm removed packages aimed at stealing Chrome browser credentials via [legitimate password recovery](https://www.bleepingcomputer.com/news/security/npm-package-steals-chrome-passwords-on-windows-via-recovery-tool/) tools.


With a massive surge in attackers targeting software registries and developers' code, the problem isn't expected to go away anytime soon.


A report from the European Union Agency for Cybersecurity (ENISA) on software supply-chain security released today states, 66% of attacks are focused on the supplier's code.


Emerging supply chain attacks in 2021 are expected to increase by **four times** compared to those reported in 2020.


"Such new trend stresses the need for policymakers and the cybersecurity community to act now."


"This is why novel protective measures to prevent and respond to potential supply chain attacks in the future while mitigating their impact need to be introduced urgently," states ENISA in their [report](http://www.enisa.europa.eu/news/enisa-news/understanding-the-increase-in-supply-chain-security-attacks).




#### Tags:
[[malware]] [[IP]] [[PyPI]] [[numbers,]] [[report.]] [["This]] [[Bleeping Computer]]
