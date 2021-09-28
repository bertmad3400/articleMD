# SAS 2021: FinSpy Surveillance Kit Re-Emerges Stronger Than Ever
### A ‘nearly impossible to analyze’ version of the malware sports a bootkit and ‘steal-everything’ capabilities.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175068)
+ Date: September 28, 2021  1:45 pm
+ Author: Tara Seals


## Article:
The FinSpy surveillance kit has been driven from its hiding place following an eight-month investigation by Kaspersky researchers. Detections of the spyware trojan have dwindled since 2018, but it turns out that it hasn’t gone away – it’s simply been hiding behind various first-stage implants that have helped to cloak its activities. At the same time, it’s continued to advance its capabilities.


FinSpy (aka FinFisher or Wingbird) is a multiplatform software for Windows, macOS and Linux that’s marketed as a tool for law enforcement. However, much like [NSO Group’s Pegasus](https://threatpost.com/pegasus-spyware-uses-iphone-zero-click-imessage-zero-day/168899/), it’s often seen [being used for far more malicious purposes](https://threatpost.com/finspy-modules-secure-messaging-apps/146372/). First discovered in 2011, it’s a full-service spyware, capable of stealing information and credentials as well as keeping tabs on user activities. For instance, it gathers file listings and deleted files, as well as various documents; can livestream or record data via webcam and microphone; can snoop on messaging chats; and it uses the developers’ mode in browsers to intercept traffic protected with an HTTPS protocol. [![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


In the middle of 2019, several suspicious installers for legitimate applications such as TeamViewer, VLC Media Player and WinRAR were found to contain malicious code. However, they didn’t seem connected to any known malware, according to Kaspersky. But one day researchers stumbled across a Burmese-language website that hosted both the trojanized installers as well as samples of FinSpy for Android.


“We began detecting some suspicious installers of legitimate applications, backdoored with a relatively small, obfuscated downloader,” according to Kaspersky researchers Igor Kuznetsov and Georgy Kucherin, presenting at a retro-themed and virtual Security Analyst Summit (SAS) 2021 on Tuesday. “Over the course of our investigation, we found out that the backdoored installers are nothing more than first-stage implants that are used to download and deploy further payloads before the actual FinSpy trojan.”


**Multiple Evasion Techniques**
-------------------------------


The new samples are protected with multiple layers of evasion tactics. For one, after a victim downloads and executes a trojanized application, they’re vetted by two components, according to the analysis. The first is a “pre-validator” that runs multiple security checks to ensure that the device it is infecting does not belong to a security researcher.


The pre-validator downloads a host of security shellcodes from the command-and-control (C2) server and executes them – 33 of them in all. Each shellcode collects specific system information (e.g., the current process name) and uploads it back to the server, researchers noted. If any of the checks fail, the command-and-control (C2) server terminates the infection process.


If all security checks pass, the server provides a second component, dubbed the “post-validator.” It collects information that allows it to identify the victim machine and perhaps validate a specific target (it logs running processes, recently opened documents and screenshots) and sends it to a C2 server specified in its configuration.


Based on the information collected, the C2 server decides whether to deploy the full-fledged trojan platform or remove the infection, according to Kaspersky.


If FinSpy is finally deployed, it arrives heavily obfuscated with four complex, custom-made obfuscators, according to Kaspersky’s analysis.


“The primary function of this obfuscation is to slow down the analysis of the spyware,” the researchers explained.


Another evasion tactic involves a sample of FinSpy that infects machines by replacing the Windows UEFI bootloader, which is responsible for launching the operating system.


“This method of infection allowed the attackers to install a bootkit without the need to bypass firmware security checks,” according to [the research](https://securelist.com/finspy-unseen-findings/104322/). “UEFI infections are very rare and generally hard to execute, they stand out due to their evasiveness and persistence. While in this case the attackers did not infect the UEFI firmware itself, but its next boot stage, the attack was particularly stealthy, as the malicious module was installed on a separate partition and could control the boot process of the infected machine.”


The amount of work put into making FinSpy inaccessible to security researchers is particularly worrying, if impressive, said Kuznetsov. “It seems like the developers put at least as much work into obfuscation and anti-analysis measures as in the trojan itself,” he noted. “The fact that this spyware is deployed with high precision and is practically impossible to analyze also means that its victims are especially vulnerable, and researchers face a special challenge – having to invest an overwhelming amount of resources into untangling each and every sample.”


**Highly Modular FinSpy**
-------------------------


Kaspersky also looked into the capabilities of the latest samples to see if there have been advancements and found that FinSpy’s architecture remains highly modular, but more difficult to analyze than ever. That’s because a component called “the hider” encrypts all of them.


“It encrypts all of the memory pages, belonging to the whole infrastructure, including the orchestrator and all of the plugins, and all the memory pages will just stay encrypted until they are needed,” explained Kuznetsov. “The moment the code has to be executed or data has to be accessed, that one page is decrypted. Then when it is no longer needed, it’s just encrypted back.”


He added, “This means that if you even make a live memory image of an infected machine it will be very hard to find the trojan in memory, because the only unencrypted thing that you will see, will be a tiny part of this hider.”


The hider is also responsible for starting “the orchestrator,” which is a core module that will load the rest of the functionality and control the plugins, according to the analysis. It remains more or less the same as it was in previous samples, Kuznetsov said, but it adds a new module called “the communicator,” which is a hard-coded binary within a resource section of the orchestrator used to maintain C2 communication.


Another new module is a process worm.


“This doesn’t infect or propagate between the machines. Instead, it propagates within the machine, starting from the top process where the whole architecture started (usually explorer.exe or Winlogon.exe),” explained Kuznetsov. “It will make copies of itself in all the child processes, and all these child processes infected will maintain communication with the parent process.”


This worm module also hooks the keyboard, mouse clicks and various APIs to FinSpy’s various plugins, for data-collection purposes.


“The plugins themselves are used mostly to collect information about the victim,” he said. “There are not many plugins devoted to other tasks. We haven’t found any plugins devoted to lateral movement for example, though there is one curious plugin that is devoted to infecting BlackBerry devices.”


There are individual plugins for stealing credentials for VPNs, dial-up credentials, Microsoft product key information, browser search and browsing history, information about Wi-Fi connections, file listings, and more. There’s also a generic plugin for recording audio from any voice over IP (VoIP) software.


“What is also interesting is that there are forensic tools for uncovering information about deleted files and storing that deleted-file history,” Kuznetsov said. “There is also quite a unique plugin that exploits the debug function of modern browsers. By setting a particular environment variable, they make the browsers dump all the SSL encryption keys on disk. And by doing this, the attackers can decrypt all the SSL traffic from the victim.”


All of the information can be collected in real time and can be live-streamed to the attackers or pre-recorded. Data collection can be triggered by launching an application of interest as well, the researcher noted.


One thing is clear: FinSpy remains under active development, and its authors have put a herculean effort into avoiding analysis.


“We spent about eight months full time, with several researchers,” Kuznetsov said. “During that time we really had to upgrade all our tooling. We had to invent and make some tools from scratch, all of which led to producing a 300-page report on this. And what is the conclusion here? We think that there is no conclusion, because we believe that this story is never-ending. They will keep updating and upgrading their infrastructure, all the time.”


***Rule #1 of Linux Security:****No cybersecurity solution is viable if you don’t have the basics down.*[***JOIN***](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)*Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the*[***4 Golden Rules of Linux Security***](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)*. Your top takeaway will be a Linux roadmap to getting the basics right!*[***REGISTER NOW***](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)*and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.*




#### Tags:
[[FinSpy]] [[Linux]] [[it’s]] [[Kuznetsov]] [[analysis.]] [[“The]] [[plugins]] [[Kaspersky]] [[noted.]] [[C2]] [[ThreatPost]]
