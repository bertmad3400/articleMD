# Microsoft Edge just got a 'Super Duper Secure Mode' upgrade
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-edge-just-got-a-super-duper-secure-mode-upgrade/)
+ Date: August 5, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft Edge just got a 'Super Duper Secure Mode' upgrade](https://www.bleepstatic.com/content/hl-images/2021/06/01/Microsoft_Edge.jpg)


Microsoft has announced that the Edge Vulnerability Research team is experimenting with a new feature dubbed "Super Duper Secure Mode" and designed to bring security improvements without significant performance losses.


When enabled, the new Microsoft Edge Super Duper Secure Mode will remove Just-In-Time Compilation (JIT) from the V8 processing pipeline, reducing the attack surface threat actors can use to hack into Edge users' systems. 


Security without a major performance hit
----------------------------------------


Based on CVE (Common Vulnerabilities and Exposures) data collected since 2019, around 45% of vulnerabilities found in the V8 JavaScript and WebAssembly engine were related to the JIT engine, more than half of all 'in the wild' Chrome exploits abusing JIT bugs.


"This reduction of attack surface has potential to significantly improve user security; it would remove roughly half of the V8 bugs that must be fixed," [explained](https://microsoftedge.github.io/edgevr/posts/Super-Duper-Secure-Mode/) Johnathan Norman, Microsoft Edge Vulnerability Research Lead.


"This reduction in attack surface kills half of the bugs we see in exploits and every remaining bug becomes more difficult to exploit. To put it another way, we lower costs for users but increase costs for attackers."


Additionally, while the JIT compiler is designed to increase performance by compiling computer during program execution (at run time), disabling it in Super Duper Secure Mode "does not always have negative impacts."


While still in the experimental stage, Super Duper Secure Mode can be enabled by users of Microsoft Edge preview releases (including Beta, Dev, and Canary) by going to `edge://flags/#edge-enable-super-duper-secure-mode` and toggling on the new feature.



![Edge Super Duper Secure Mode](https://www.bleepstatic.com/images/news/u/1109292/2021/Microsoft%20Edge%20Super%20Duper%20Secure%20Mode.png)*Image: BleepingComputer*
Right now, when enabled, Super Duper Secure Mode disables JIT (TurboFan/Sparkplug) and enables [Control-flow Enforcement Technology](https://software.intel.com/content/www/us/en/develop/articles/technical-look-control-flow-enforcement-technology.html) (CET), an Intel hardware-based exploit mitigation designed to provide a more secure browsing experience.


In the future, Microsoft also wants to add support for [Arbitrary Code Guard](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/exploit-protection-reference?view=o365-worldwide#arbitrary-code-guard) (ACG), another security mitigation that would prevent loading malicious code into memory, a technique used by most web browser exploits.


"This is of course just an experiment; things are subject to change, and we have quite a few technical challenges to overcome," Norman concluded.


"Also, our tongue-in-cheek name will likely need to change to something more professional when we launch as a feature. For now, we are going to continue having fun with it."




> 
> I'm not sure if this will land as a feature. But I think this experiment is worth a shot. If you try it please share your feedback in Edge (click the 3 dots -> feedback) or post on the forum <https://t.co/As3jeqMSyC> . We are curious to see if this is something users want. 7/?
> 
> 
> — Johnathan Norman (@spoofyroot) [August 4, 2021](https://twitter.com/spoofyroot/status/1423011021766107137?ref_src=twsrc%5Etfw)




#### Tags:
[[Microsoft]] [[JIT]] [[V8]] [["This]] [[feature.]] [[Bleeping Computer]]
