# Edge Super Duper Secure Mode turns off the JavaScript JIT compiler for extra security
### Microsoft experiments with disabling the JIT JavaScript compiler in an effort to provide better security.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/edge-super-duper-secure-mode-turns-off-the-javascript-jit-compiler-for-extra-security/)
+ Date: August 5, 2021 -- 06:02 GMT (07:02 BST)
+ Author: Chris Duckett


## Article:
Unknown

![Microsoft Edge](https://www.zdnet.com/a/hub/i/2020/12/01/5fcf9ee6-b2ef-4166-94e8-af89484ba5ee/microsoft-edge.png)
 Image: Microsoft
 The lead of Microsoft Edge Vulnerability Research Johnathan Norman has [detailed](https://microsoftedge.github.io/edgevr/posts/Super-Duper-Secure-Mode/) an experiment in Edge that disabled the JavaScript just-in-time (JIT) compiler to enable some extra security protections. 

Describing JIT compiling as a "remarkably complex process that very few people understand and it has a small margin for error", Norman pointed out that half of all vulnerabilities for the V8 JavaScript engine was related to the process. 

With the JIT engine turned off, it was possible for Edge to turn on protections -- such as the hardware-based Control-flow Enforcement Technology (CET) from Intel, and Windows' Arbitrary Code Guard (ACG) and Control Flow Guard (CFG) -- that were previously incompatible with JIT. 

"This is unfortunate because the renderer process handles untrusted content and should be locked down as much as possible," Norman said. 

"By disabling JIT, we can enable both mitigations and make exploitation of security bugs in any renderer process component more difficult. 

"This reduction in attack surface kills half of the bugs we see in exploits and every remaining bug becomes more difficult to exploit. To put it another way, we lower costs for users but increase costs for attackers." 

![ms-edge-super-duper-improvement-and-regression.png]()![ms-edge-super-duper-improvement-and-regression.png](https://www.zdnet.com/a/hub/i/r/2021/08/05/7d41c060-8c68-4581-8ce3-3d9d141afdae/resize/1200xauto/28b9eca9371c113dc8afb1d620a9c54a/ms-edge-super-duper-improvement-and-regression.png)
 Image: Microsoft
 In testing Edge with JIT disabled, Norman said users rarely noticed a difference in daily browsing, but the JIT-less Edge was hosed in benchmark tests, with performance reduced by as much as 58%. 






"Our tests that measured improvements in power showed 15% improvement on average and our regressions showed around 11% increase in power consumption. Memory is also a mixed story with negatively impacted tests showing a 2.3% regression, but a larger gain on the tests that showed improvements," Norman wrote. 

"Page Load times show the most severe decrease with tests that show regressions averaging around 17%. Startup times, however, have only a positive impact and no regressions." 

Super Duper Secure Mode is currently available via edge://flags for users of canary, dev, and beta release channels of the browser, and currently switches CET on, but is not currently compatible with WebAssembly. 

"It will take some time, but we hope to have CET, ACG, and CFG protection in the renderer process. Once that is complete, we hope to find a way to enable these mitigations intelligently based on risk and empower users to balance the tradeoffs," Norman said. 

"This is of course just an experiment; things are subject to change, and we have quite a few technical challenges to overcome. Also, our tongue-in-cheek name will likely need to change to something more professional when we launch as a feature." 

On Twitter, Norman said [plans were afoot](https://twitter.com/spoofyroot/status/1423011020524589059) to take Super Duper Mode to MacOS and Android, and to get WebAssembly working. 

### Related Coverage

* [Windows 11 has advanced hardware security. Here's how to get it in Windows 10 today](/article/windows-11-has-advanced-hardware-security-heres-how-to-get-it-in-windows-10-today/)
* [Microsoft Edge 92 starts rolling out to mainstream users](/article/microsoft-edge-92-starts-rolling-out-to-mainstream-users/)
* [Get patching: US, UK, and Australia issue joint advisory on top 30 exploited vulnerabilities](/article/get-patching-us-uk-and-australia-issue-joint-advisory-on-top-30-exploited-vulnerabilities/)
* [Windows Print Spooler hit with local privilege escalation vulnerability](/article/windows-print-spooler-hit-with-local-privilege-escalation-vulnerability/)
* [Microsoft support agent and some basic customer details hit by SolarWinds attackers](/article/microsoft-support-agent-and-some-basic-customer-details-hit-by-solarwinds-attackers/)





#### Tags:
[[Microsoft]] [[JIT]] [["This]] [[ZDNet]]
