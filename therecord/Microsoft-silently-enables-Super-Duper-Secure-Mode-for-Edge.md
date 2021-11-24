# Microsoft silently enables ‘Super Duper Secure Mode’ for Edge
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/microsoft-silently-enables-super-duper-secure-mode-for-edge/)
+ Date: November 23, 2021
+ Author: Catalin Cimpanu


## Article:
![Microsoft silently enables ‘Super Duper Secure Mode’ for Edge](https://therecord.media/wp-content/uploads/2021/06/Microsoft-Edge-1-e1628118995558.jpg)

Microsoft last week secretly added a security feature in its Edge web browser that allows users to sacrifice the browser’s performance for improved security.


[Announced in August this year](https://therecord.media/microsoft-announces-new-super-duper-secure-mode-for-edge/), the feature is named **Super Duper Secure Mode** and was in Edge v96.0.1054.29, released last Friday on November 19, according to Johnathan Norman, Microsoft Edge Vulnerability Research Lead.


Under the hood, the feature works by allowing users to disable support for an Edge component named the JIT (Just-In-Time) compiler, a toolkit that compiles JavaScript code into machine code ahead of time in order to speed up the browser.


While the feature was initially designed to improve website loading speeds and to help with complex and dynamic websites, the feature has recently been a whirlpool of security flaws.


As the Edge team [explained in a blog post in August](https://microsoftedge.github.io/edgevr/posts/Super-Duper-Secure-Mode/), the JIT compiler has been the source of 45% of all security vulnerabilities discovered in Edge’s browser engine and at the source of half the zero-days exploited in Chromium browsers since 2019.


Super Duper Secure Mode lets users disable JIT compilation by going in Edge’s settings section, at edge://settings/privacy, and flipping a switch.


Two options are provided, Balanced, which disables JIT on new sites that the user doesn’t usually visit, and Strict, which disables JIT on all sites at once.


![Edge-super-duper-stable](https://www-therecord.recfut.com/wp-content/uploads/2021/11/Edge-super-duper-stable-1024x530.png)Image: The Record
Currently, Super Duper Secure Mode just disables JIT, but Norman said in August that other security features will be added to this umbrella security option, such as adding support in Edge for [MiraclePtr](https://chromium.googlesource.com/chromium/src/+/ddc017f9569973a731a574be4199d8400616f5a5/base/memory/raw_ptr.md), [Controlflow-Enforcement Technology](https://software.intel.com/content/www/us/en/develop/articles/technical-look-control-flow-enforcement-technology.html) (CET), and [Arbitrary Code Guard](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/exploit-protection-reference?view=o365-worldwide#arbitrary-code-guard) (ACG)


“I’m really excited to see what impact we have here. Although for it really to matter, we will need SDSM enabled by default,” Norman [tweeted](https://twitter.com/spoofyroot/status/1462871835813445635) on Monday.





#### Tags:
[[JIT]] [[The Record]]
