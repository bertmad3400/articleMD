# Microsoft Edge adds Super Duper Secure Mode to Stable channel
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-edge-adds-super-duper-secure-mode-to-stable-channel/)
+ Date: November 23, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft Edge adds Super Duper Secure Mode to Stable channel](https://www.bleepstatic.com/content/hl-images/2021/06/01/Microsoft_Edge.jpg)


Microsoft has quietly added a 'Super Duper Secure Mode' to the Microsoft Edge web browser, a new feature that brings security improvements without significant performance losses.


Users can enable Super Duper Secure Mode after upgrading Edge to stable version 96.0.1054.29 or later, and they can toggle between Balanced and Strict modes for different levels of security increase.


The new feature, under testing by the Edge Vulnerability Research team [since August](https://www.bleepingcomputer.com/news/microsoft/microsoft-edge-just-got-a-super-duper-secure-mode-upgrade/), removes Just-In-Time Compilation (JIT) from the V8 processing pipeline, thus reducing the attack surface threat actors can exploit to hack into Edge users' systems. 


Microsoft describes Super Duper Secure Mode as "a browsing mode in Microsoft Edge where the security of your browser takes priority, providing you an extra layer of protection when browsing the web."


"We quietly released Super Duper Secure Mode to stable (96.0.1054.29)," [said](https://twitter.com/spoofyroot/status/1462871833942773763) Johnathan Norman, Microsoft Edge Vulnerability Research Lead.


"Balanced learns what sites you use often and trusts those, strict is well.. strict :) Users can now add their own exceptions."



![Enabling Super Duper Secure Mode in Microsoft Edge](https://www.bleepstatic.com/images/news/u/1109292/2021/Edge_Super_Duper_Secure_Mode.png)*Enabling Super Duper Secure Mode in Microsoft Edge (BleepingComputer)*
When toggled on, Super Duper Secure Mode disables JIT (TurboFan/Sparkplug) and enables Intel's [Control-flow Enforcement Technology](https://software.intel.com/content/www/us/en/develop/articles/technical-look-control-flow-enforcement-technology.html) (CET), a hardware-based exploit mitigation that provides a more secure browsing experience.


As Norman revealed in August when the feature was first announced, roughly 45% of all security vulnerabilities found in the V8 JavaScript and WebAssembly engine were related to the JIT engine, accounting for over half of all 'in the wild' Chrome exploits abusing JIT bugs.


By disabling JIT, the attack surface is drastically reduced by removing almost half of the V8 bugs that should be fixed.


"This reduction in attack surface kills half of the bugs we see in exploits and every remaining bug becomes more difficult to exploit. To put it another way, we lower costs for users but increase costs for attackers," Norman explained.


In the future, Microsoft aims to include support for [Arbitrary Code Guard](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/exploit-protection-reference?view=o365-worldwide#arbitrary-code-guard) (ACG) in Super Duper Secure Mode, another security mitigation that would block attackers from loading malicious code into memory, a known technique used by most web browser exploits.


The Edge Vulnerability Research team also plans to ship the new feature with the Android and macOS Edge versions.




> 
> At the moment we are disabling JIT and enabling CET in the renderer process. ACG enablement is next after we do some testing. We also have plans for Android and Mac as well. Android being the most interesting since mobile is such a key target 6/?
> 
> 
> — Johnathan Norman (@spoofyroot) [August 4, 2021](https://twitter.com/spoofyroot/status/1423011020524589059?ref_src=twsrc%5Etfw)




#### Tags:
[[Microsoft]] [[JIT]] [[V8]] [[Android]] [[Bleeping Computer]]
