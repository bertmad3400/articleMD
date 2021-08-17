# Securing Microsoft Edge: Switch off JIT compilers or sandbox?
### Microsoft's Super Duper Secure Mode is ready for testing, but Google has an alternative approach to JIT vulnerabilities in the V8 engine.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/securing-microsoft-edge-switch-off-jit-compilers-or-sandbox/)
+ Date: August 17, 2021 -- 14:04 GMT (15:04 BST)
+ Author: Liam Tung


## Article:
Unknown

Google and Microsoft, which now both contribute to the Chromium project, apparently share concerns about the Just-In-Time (JIT) compiler in Chrome's V8 JavaScript engine.  

Microsoft's Edge Vulnerability Research (VR) team last week [announced the start of testing Microsoft's Super Duper Secure Mode (SDSM) for Edge](https://www.zdnet.com/article/microsoft-is-testing-a-super-duper-secure-mode-for-its-edge-browser/), which works by removing Just-In-Time (JIT) compilation from the V8 processing pipeline. 


Google's V8 JavaScript engine for Chrome was a key turning point for web applications in the history of browsers, Microsoft's creator of TypeScript (a superset of JavaScript) acknowledged in an [interview with ZDNet last year](https://www.zdnet.com/article/typescript-creator-how-the-programming-language-beat-microsofts-open-source-fears/).

Per [MS Poweruser](https://mspoweruser.com/microsoft-edge-super-duper-secure-mode-now-has-a-settings-toggle/) and [Reddit users](https://www.reddit.com/r/MicrosoftEdge/comments/p5m6wq/super_duper_secure_mode_can_now_be_enabled_or/?context=3), unstable [Edge Canary](https://www.microsoftedgeinsider.com/en-us/download/canary) now includes a flag that enables SDSM in Edge. That is, JIT compilation in V8 in Edge is disabled by going to *edge://flags/#edge-enable-super-duper-secure-mode.* 

Microsoft is not alone in taking new approaches to the V8 engine's JIT compilers. Google [Project Zero](https://googleprojectzero.blogspot.com/p/about-project-zero.html) is also exploring how to tackle vulnerabilities surrounding JIT compilation in V8, but with a different solution -- namely, creating a custom sandbox for V8.   

[As Microsoft's browser vulnerability researchers noted](https://microsoftedge.github.io/edgevr/posts/Super-Duper-Secure-Mode/), JITs exist to optimise JavaScript performance. Disabling JIT would remove half of the V8 bugs that must be fixed, they argue, and go on to note that Microsoft's tests found that disabling JIT results in virtually no changes to browser performance across memory, page load and startup times, and power consumption.   

Since Microsoft Edge is based on Chromium and Google Chrome is the most widely used browser on Windows, there is a mutual area of concern for both firms.






With V8's JIT compilation turned off, Microsoft [could enable Edge memory and hardware-based protections](https://www.zdnet.com/article/edge-super-duper-secure-mode-turns-off-the-javascript-jit-compiler-for-extra-security/) -- such as the hardware-based Control-flow Enforcement Technology (CET) from Intel, and Windows' Arbitrary Code Guard (ACG) and Control Flow Guard (CFG) -- that were previously incompatible with JIT. 

Google is not unaware of this, but some within Google believe that the benefits of these hardware-based protections might not be as effective as believed. Interestingly, in May, Google's Chrome team [opted to enable Intel's CET mitigations for Chrome on Windows 10](https://www.zdnet.com/article/google-chrome-this-new-feature-makes-it-tougher-for-hackers-to-attack-windows-10-pcs/) to mitigate return-oriented programming (ROP) attacks. 

[Earlier this month](https://www.zdnet.com/article/bugs-in-chromes-javascript-engine-can-lead-to-powerful-exploits-this-project-aims-to-stop-them/), Google Project Zero researcher Samuel Groß outlined a sandbox approach to tackle JITs within the context of V8. He warned that his proposal had many hurdles to cross. Those hurdles could come from other teams within Google, such as the Chrome team, from Microsoft, or from other interested parties. 

Groß explained that the problem with V8 stems from JIT compilers that can be used to trick a machine into emitting machine code that corrupts memory at runtime. 

"Many V8 vulnerabilities exploited by real-world attackers are effectively 2nd order vulnerabilities: the root-cause is often a logic issue in one of the JIT compilers, which can then be exploited to generate vulnerable machine code (e.g. code that is missing a runtime safety check). The generated code can then in turn be exploited to cause memory corruption at runtime," Groß said. 

"This appears to be a somewhat natural problem of JIT compilers for dynamic languages, as one of their major purposes is to remove (redundant) runtime checks that would otherwise be performed by the interpreter." 

He's less confident in the technologies that Microsoft researchers highlight would be enabled by switching JIT compilers off -- and hence why the better approach may be to create a custom sandbox for V8. 

As Groß also noted, CPU side-channel vulnerabilities, and the potency of V8 vulnerabilities, mean that "upcoming hardware security features such as memory tagging will likely be bypassable most of the time." 

 Also see
---------

**[Microsoft tests Super-Duper Secure Mode for Edge](https://www.zdnet.com/article/microsoft-is-testing-a-super-duper-secure-mode-for-its-edge-browser/)** 

**[Edge Super Duper Secure Mode turns off the JavaScript JIT compiler for extra security](https://www.zdnet.com/article/edge-super-duper-secure-mode-turns-off-the-javascript-jit-compiler-for-extra-security/)** 

[**Google Project Zero testing 30-day grace period on bug details to boost user patching**](https://www.zdnet.com/article/google-project-zero-testing-30-day-grace-period-on-bug-details-to-boost-user-patching/) 





#### Tags:
[[JIT]] [[V8]] [[Microsoft]] [[Google]] [[JavaScript]] [[Groß]] [[V8.]] [[hardware-based]] [[ZDNet]]
