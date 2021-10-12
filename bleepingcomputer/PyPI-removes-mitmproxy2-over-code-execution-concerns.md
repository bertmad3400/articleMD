# PyPI removes 'mitmproxy2' over code execution concerns
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/pypi-removes-mitmproxy2-over-code-execution-concerns/)
+ Date: October 12, 2021
+ Author: Ax Sharma


## Article:
![pypi](https://www.bleepstatic.com/content/hl-images/2021/05/20/bg_pypi_smaller.png)


The PyPI repository has removed a Python package called 'mitmproxy2' that was an identical copy of the official "mitmproxy" library, but with an "artificially introduced" code execution vulnerability.


The official 'mitmproxy' Python library is a free and open-source interactive HTTPS proxy with over 40,000 weekly downloads.


Copycat package could trick devs into falling for 'newer' version
-----------------------------------------------------------------


Yesterday, Maximilian Hils, who is one of the developers behind the 'mitmproxy' Python library drew everyone's attention towards a counterfeit 'mitmproxy2' package uploaded to PyPI.


'mitmproxy2' is essentially "the same as regular mitmproxy but with an artificial RCE vulnerability included."




> 
> The more popular you get, the more shit you attract: Someone uploaded "mitmproxy2" to [@PyPI](https://twitter.com/pypi?ref_src=twsrc%5Etfw), which is the same as regular mitmproxy but with an artificial RCE vulnerability included.
> 
> 
> — Maximilian Hils (@maximilianhils) [October 11, 2021](https://twitter.com/maximilianhils/status/1447525552370458625?ref_src=twsrc%5Etfw)


Hils' main concern, as he describes to BleepingComputer, was that some software developers might mistake 'mitmproxy2' as a newer version" of 'mitmproxy' and inadvertently introduce insecure code in their apps.


Hils found this copycat package in what he calls a "happy little accident" while looking into an unrelated PyPI warehouse [issue](https://github.com/pypa/warehouse/issues/10171).



![mitmproxy2 pypi page](https://www.bleepstatic.com/images/news/u/1164866/2021/Oct-2021/mitm-pypi-malware/mitmproxy2-page.jpg)**Now-removed 'mitmproxy2' PyPI package page** (BleepingComputer)
On analyzing the differences between 'mitmproxy2' and his 'mitmproxy,' [something important stood out](http://web.archive.org/web/20211012105244/https://gist.github.com/mhils/7ff29d50b25a1c99e06834cf95684333). The former had all safeguards removed from the API:


"When you run mitmproxy's web interface, we expose an HTTP API for that. If you remove all safeguards from that API, everyone on the same network can execute code on your machine with a single HTTP request," Hils told BleepingComputer in an email interview.



!['mitmproxy2' had API safeguards removed](https://www.bleepstatic.com/images/news/u/1164866/2021/Oct-2021/mitm-pypi-malware/diff.jpeg)**'mitmproxy2' had API safeguards removed** (BleepingComputer)
It isn't clear either if the user who published the copycat 'mitmproxy2' package did so with willful malicious intent or just out of insecure coding practices. 


"To be clear, this really isn't the most malicious thing an attacker could do. It would be much more straightforward to just add some malicious code that gets executed on install right away."


"The problem is of course if you upload that to PyPI as 'mitmproxy2' with a version number that indicates it's newer/a successor, people will inevitably download that not knowing about the changes."


Hils thanked PyPI volunteers for swiftly reacting to this report. Within four hours of Hils' tweet 'mitmproxy2' was taken down.


Whack-a-mole: another copycat appears hours later
-------------------------------------------------


While analyzing 'mitmproxy2', BleepingComputer discovered another package 'mitmproxy-iframe' had appeared on the PyPI registry, less than a day after 'mitmproxy2' was removed.


Once again, this package is an exact replica of the official *mitmproxy*, but with the aforementioned safeguards removed from the "app.py" file, as seen by BleepingComputer.


Interestingly, *mitmproxy-iframe* is also published by the same user who is behind 'mitmproxy2', now casting doubts on what the user's intentions are:



![mitmproxy-iframe with same code execution vulnerability](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Another package 'mitmproxy-iframe' appears with same code execution vulnerability**(BleepingComputer)
Because anyone can publish packages to open-source ecosystems, security threats and attacks like [malware injection](https://www.bleepingcomputer.com/news/security/malicious-pypi-packages-hijack-dev-devices-to-mine-cryptocurrency/), [typosquatting](https://www.bleepingcomputer.com/news/security/malicious-npm-project-steals-discord-accounts-browser-info/), [brandjacking](https://www.bleepingcomputer.com/news/security/npm-package-steals-chrome-passwords-on-windows-via-recovery-tool/), and [dependency confusion](https://www.bleepingcomputer.com/news/security/researcher-hacks-over-35-tech-firms-in-novel-supply-chain-attack/) have increased rapidly in recent times.


Unless concrete validations are put in place by open-source registries, these "whack-a-mole" situations are bound to repeat themselves.


BleepingComputer notified PyPI of the 'mitmproxy-iframe' package prior to publishing and the package was taken down.




#### Tags:
[[PyPI]] [[Hils]] [[open-source]] [[mitmproxy]] [[(BleepingComputer)]] [[BleepingComputer]] [[Bleeping Computer]]
