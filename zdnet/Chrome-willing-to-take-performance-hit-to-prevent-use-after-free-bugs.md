# Chrome willing to take performance hit to prevent use-after-free bugs
### Various attempts will be made in the browser to make memory handling safer.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/chrome-willing-to-take-performance-hit-to-prevent-use-after-free-bugs/)
+ Date: September 22, 2021
+ Author: Chris Duckett


## Article:
Unknown

![chrome-icon-close-up.jpg](https://www.zdnet.com/a/img/resize/a9b12ff10b1e5da01be7c94d0a8dbd643e5aeb50/2021/06/02/c2d75b27-893c-4946-ae60-fdb7eb8c9a8b/chrome-icon-close-up.jpg?width=1200&fit=bounds&auto=webp)
 Image: Shutterstock
 The Chrome security team has said it is willing to make the browser slightly slower if it means the tradeoff is a much more secure browser. 

Pointing to previous figures that [70% of all security problems are related to memory safety](https://www.zdnet.com/article/chrome-70-of-all-security-bugs-are-memory-safety-issues/), the team said in a [blog post](https://security.googleblog.com/2021/09/an-update-on-memory-safety-in-chrome.html) that it was looking at three approaches: Compile-time checks, runtime checks, and using a memory safe language. 

Thanks to the use of C++, the first option was not possible, but it was looking at solutions such as [MiraclePtr](https://chromium.googlesource.com/chromium/src/+/ddc017f9569973a731a574be4199d8400616f5a5/base/memory/raw_ptr.md) for runtime checking. 

"MiraclePtr prevents use-after-free bugs by quarantining memory that may still be referenced. On many mobile devices, memory is very precious and it's hard to spare some for a quarantine," the team said. 

"Nevertheless, MiraclePtr stands a chance of eliminating over 50% of the use-after-free bugs in the browser process -- an enormous win for Chrome security, right now." 

At the same time, the browser is continuing to look at how to integrate the Rust language to allow for compile-time checks which subsequently do not impact performance. 

"There are open questions about whether we can make C++ and Rust work well enough together," the team said. 






"Even if we started writing new large components in Rust tomorrow, we'd be unlikely to eliminate a significant proportion of security vulnerabilities for many years. And can we make the language boundary clean enough that we can write parts of existing components in Rust? We don't know yet. " 

The team said it is trying out some limited usage of Rust, but this has yet to make it through to production builds of Chrome. 

Invented by Mozilla, Rust has been used in [parts of Firefox](https://www.zdnet.com/article/mozilla-begins-process-of-letting-firefox-rust/) since 2016, and Google's Android team has pushed to introduce [Rust into the Linux kernel](https://www.zdnet.com/article/google-backs-effort-to-bring-rust-to-the-linux-kernel/).

### Related Coverage

* [Google's Chrome browser is about to get a lot faster](/article/googles-chrome-browser-is-about-to-get-a-lot-faster/)
* [Google patches two Chrome zero-days](/article/google-patches-two-chrome-zero-days/)
* [Chrome 91 will warn users when installing untrusted extensions](/article/chrome-91-will-warn-users-when-installing-untrusted-extensions/)
* [Need to save a bunch of tabs? Chrome will do it for you soon](/article/need-to-save-a-bunch-of-tabs-chrome-will-do-it-for-you-soon/)





#### Tags:
[[]] [[ZDNet]]
