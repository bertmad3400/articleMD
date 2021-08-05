# Microsoft announces new ‘Super Duper Secure Mode’ for Edge
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/microsoft-announces-new-super-duper-secure-mode-for-edge/)
+ Date: August 4, 2021
+ Author: Catalin Cimpanu


## Article:
![Microsoft announces new ‘Super Duper Secure Mode’ for Edge](https://therecord.media/wp-content/uploads/2021/06/Microsoft-Edge-1-e1628118995558.jpg)

Microsoft said today it plans to run an experiment in its Edge web browser where it will intentionally disable an important performance and optimization feature in order to enable more advanced security upgrades in what the company is calling Edge **Super Duper Secure Mode**.


[Announced today](https://microsoftedge.github.io/edgevr/posts/Super-Duper-Secure-Mode/) by Johnathan Norman, Microsoft Edge Vulnerability Research Lead, the idea behind the new Super Duper Secure Mode is to disable support for JIT (Just-In-Time) inside V8, the Edge browser’s JavaScript engine.


[JIT](https://en.wikipedia.org/wiki/Just-in-time_compilation), while unknown to most end-users, plays a crucial role in all of today’s web browsers. JIT works by taking JavaScript and compiling it to machine code ahead of time. If the browser needs the code, it gains a significant speed boost. If it doesn’t, the code is discarded.


However, JIT support in V8 is complex. Norman said JIT-related security issues amounted to 45% of all V8 vulnerabilities in 2019. Furthermore, more than half of the “in the wild” Chrome exploits rely on JIT-related bugs.


Norman said that recent tests carried out by the Edge team have shown that despite its pivotal role in speeding up browsers in the early and mid-2010s, JIT is not a crucial feature anymore to Edge’s performance.


![Edge-performance-tests](https://www-therecord.recfut.com/wp-content/uploads/2021/08/Edge-performance-tests.png)Image: Microsoft
Encouraged by these findings, Norman said the Edge team is now working on Super Duper Secure Mode, an Edge configuration where they disable JIT and enable three other security features such as [Controlflow-Enforcement Technology](https://software.intel.com/content/www/us/en/develop/articles/technical-look-control-flow-enforcement-technology.html) (CET) and [Arbitrary Code Guard](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/exploit-protection-reference?view=o365-worldwide#arbitrary-code-guard) (ACG)—two features that would normally clash with V8’s JIT implementation.


As Norman explained, Super Duper Secure Mode is currently classified as an experiment, and there are no plans set in stone to ship it to users just yet.





However, while Super Duper Secure Mode does not have a certain future, the feature is already live and ready for testing. Users of Edge Canary, Dev, and Beta can go to the following address and enable it in their browsers:


**edge://flags/#edge-enable-super-duper-secure-mode**


![](https://www-therecord.recfut.com/wp-content/uploads/2021/08/MS-EDGE-SDSM.png)Image: Microsoft



#### Tags:
[[JIT]] [[Microsoft]] [[The Record]]
