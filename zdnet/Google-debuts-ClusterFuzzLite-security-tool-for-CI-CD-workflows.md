# Google debuts ClusterFuzzLite security tool for CI, CD workflows
### The fuzzing solution is set to bolster software supply chain security.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/google-debuts-clusterfuzzlite-for-ci-cd-workflows/)
+ Date: November 11, 2021
+ Author: Charlie Osborne


## Article:
Unknown

Google has launched ClusterFuzzLite, a continuous fuzzing solution for improving software supply chain security. 


On Thursday, Google software engineers Jonathan Metzman and Oliver Chang, together with product lead for Google's CI/CD products, Michael Winser, said in [a blog post](https://security.googleblog.com/) that the new tool can run "as part of CI/CD workflows to find vulnerabilities faster than ever before."

Fuzzing is an automated testing technique for finding bugs and unexpected behavior by inputting invalid and random data into programs. This can flag up vulnerabilities or errors that may otherwise go unnoticed through manual analysis.  

The new tool, [ClusterFuzzLite](https://github.com/google/clusterfuzzlite), is based on ClusterFuzz, an open source scalable fuzzing infrastructure previously released by Google and used as the fuzzing backbone for the [OSS-Fuzz](https://github.com/google/oss-fuzz) program.  

According to Google, ClusterFuzzLite can be integrated into existing workflows to fuzz pull requests, improving the chance of vulnerabilities to be found earlier in the development process and before changes are committed.  

While [ClusterFuzz](https://google.github.io/clusterfuzz/) and ClusterFuzzLite contain some of the same features -- including continuous fuzzing, coverage report creation, and sanitizer support -- the team says that the main difference is ClusterFuzz is easy to set up with closed source projects, and so developers can make use of it to quickly fuzz their software.  

As of now, ClusterFuzzLite supports GitHub Actions, Google Cloud Build, and Prow.  






"With ClusterFuzzLite, fuzzing is no longer just an idealized "bonus" round of testing for those who have access to it, but a critical must-have step that everyone can use continuously on every software project," the team said. "By finding and preventing bugs before they enter the codebase we can build a more secure software ecosystem." 

Documentation on the tool can be accessed at [GitHub](https://google.github.io/clusterfuzzlite/).  

In February, Google launched the [Open Source Vulnerabilities](https://www.zdnet.com/article/google-our-new-tool-makes-open-source-security-bugs-easier-to-spot/) (OSV) website, a platform for open source vulnerability mapping. 

###  Previous and related coverage

* [Google sets up research grant for finding bugs in browser JavaScript engines](https://www.zdnet.com/article/google-sets-up-research-grant-for-finding-bugs-in-browser-javascript-engines/)
* [Google open-sources Atheris, a tool for finding security bugs in Python code](https://www.zdnet.com/article/google-open-sources-atheris-a-tool-for-finding-security-bugs-in-python-code/)
* [Google: Our new tool makes open-source security bugs easier to spot](https://www.zdnet.com/article/google-our-new-tool-makes-open-source-security-bugs-easier-to-spot/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Google]] [[ClusterFuzzLite,]] [[ClusterFuzzLite]] [[ZDNet]]
