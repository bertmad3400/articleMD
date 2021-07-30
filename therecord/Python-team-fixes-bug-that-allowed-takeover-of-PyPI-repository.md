# Python team fixes bug that allowed takeover of PyPI repository
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/python-team-fixes-bug-that-allowed-takeover-of-pypi-repository/)
+ Date: July 30, 2021
+ Author: Catalin Cimpanu


## Article:
![Python team fixes bug that allowed takeover of PyPI repository](https://therecord.media/wp-content/uploads/2021/07/PyPI-logo.png)

The Python security team has fixed today three vulnerabilities impacting the Python Package Index (PyPI), the official repository for Python libraries, including one that could have allowed a threat actor to take full control over the portal.


The three vulnerabilities were discovered by Japanese security researcher [RyotaK](https://twitter.com/ryotkak), the same who earlier this month found a [bug in Cloudflare’s CDNJS service](https://blog.ryotak.me/post/cdnjs-remote-code-execution-en/) that could have allowed a third party to run malicious code on roughly 12% of today’s websites.


In a [new report](https://blog.ryotak.me/post/pypi-potential-remote-code-execution-en/) published today, RyotaK said he analyzed [PyPI](https://pypi.org/), a web portal that serves as an official package index and repository for Python libraries. The site is basically a database, which works in conjunction with the official Python **pip** package installer, and allows developers and amateur programmers to easily search and install Python components for their projects.


In tune with the Python Software Foundation’s mantra, the source code of the PyPI service is also [available on GitHub](https://github.com/pypa/warehouse/). By analyzing this public codebase, RyotaK said he found three bugs that could be exploited to:


* [Delete other projects’ documentation files](https://python-security.readthedocs.io/pypi-vuln/index-2021-07-26-legacy-document-deletion.html)
* [Delete another project permission roles](https://python-security.readthedocs.io/pypi-vuln/index-2021-07-27-role-deletion.html)
* [Run bash commands on the PyPI codebase itself via GitHub Actions workflows](https://python-security.readthedocs.io/pypi-vuln/index-2021-07-27-combine-prs-workflow.html)


Of the three, RyotaK described the first two as low-impact vulnerabilities that could “only be used for harassment at best.”


However, a third bug was a critical issue as attackers could run commands on the PyPI’s infrastructure to gather tokens or other secrets from the codebase that an attacker could later use to access and modify the PyPI code itself.


“I could modify top page of pypi.org,” the researcher told *The Record* in an interview earlier today.


“It was [also] possible to modify the contents of packages, as pypa/warehouse contains a [code](https://github.com/pypa/warehouse/blob/cb917fc58ed8b049bc468e92a15fa63c3de06855/warehouse/forklift/legacy.py#L765-L1486) [for it](https://github.com/pypa/warehouse/blob/cb917fc58ed8b049bc468e92a15fa63c3de06855/warehouse/forklift/legacy.py#L765-L1486),” he added.


The Python Software Foundation has awarded the researcher $1,000 for each of his bug reports, along with a public acknowledgment of his work.








#### Tags:
[[RyotaK]] [[PyPI]] [[The Record]]
