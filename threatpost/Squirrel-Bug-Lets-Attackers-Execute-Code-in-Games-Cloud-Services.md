# Squirrel Bug Lets Attackers Execute Code in Games, Cloud Services
### The out-of-bounds read vulnerability enables an attacker to escape a Squirrel VM in games with millions of monthly players – such as Counter-Strike: Global Offensive and Portal 2 – and in cloud services such as Twilio Electric Imp.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175586)
+ Date: October 19, 2021  5:42 pm
+ Author: Lisa Vaas


## Article:
An out-of-bounds read vulnerability in the Squirrel programming language lets attackers break out of sandbox restrictions and execute arbitrary code within a Squirrel virtual machine (VM), thus giving a malicious actor complete access to the underlying machine.


Given where Squirrel lives – in games and embedded in the internet of things (IoT) – the bug potentially endangers the millions of monthly gamers who play video games such as [Counter-Strike: Global Offensive](https://developer.valvesoftware.com/wiki/Squirrel) and Portal 2, as well as cloud services such as the [Twilio Electric Imp](https://developer.electricimp.com/libraries/webservices/twilio) IoT platform, with its ready-to-use open-source code library.


[Squirrel](http://squirrel-lang.org/) is an open-source, object-oriented programming language used by video games and cloud services for customization and plugin development. It’s a lightweight scripting language that suits the size, memory bandwidth and real-time requirements of applications like video games and embedded systems.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Both of the games mentioned above use the Squirrel Engine game library to enable anyone to create custom game modes and maps.


Tracked as [CVE-2021-41556](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41556), the Squirrel out-of-bounds read vulnerability can be exploited when a Squirrel Engine is used to execute untrusted code, as it is with Twilio Electric Imp or certain video games.


The vulnerability was discovered by SonarSource and detailed in [a post](https://blog.sonarsource.com/squirrel-vm-sandbox-escape) published on Tuesday. In that writeup, vulnerability researchers Simon Scannell and Niklas Breitfeld suggested a real-world scenario in which an attacker could embed a malicious Squirrel script into a community map and distribute it via the trusted [Steam Workshop](https://www.lifewire.com/everything-you-need-to-know-about-steam-workshop-4587072#:~:text=The%20Steam%20Workshop%20is%20a,it%20into%20the%20Steam%20Workshop.&text=You%20can%20also%20view%20a,directly%20from%20your%20Steam%20library.): a mod repository for Steam Games that lets creators upload their mods for a massive built-in audience while providing regular players with an easy way to obtain mods.


“When a server owner downloads and installs this malicious map onto his server, the Squirrel script is executed, escapes its VM, and takes control of the server machine,” the researchers explained.


The security flaw concerns an “out-of-bounds access via index confusion” when defining Squirrel classes. “The fact that bitflags are set within indexes is problematic as it is entirely possible for an attacker to create a class definition with 0x02000000 methods,” the researchers explained. They created the following, “very simple” proof of concept (PoC): just a nibble’s worth of code that could be exploited to hijack a program and grant an attacker full control of the Squirrel VM.


“The rawset and rawget functions allow us to handily access members of a given class,” according to the analysis. “In this PoC, the squirrel interpreter will dereference a null pointer and segfault because the \_defaultvalues array has not been allocated yet.”


An attacker could trigger the vulnerability by:


The vulnerability is dangerous because a malicious actor could set up a fake array that could read and write values. By doing so themselves, the researchers found they could “hijack the control flow of the program and gain full control of the Squirrel VM,” which they did by overwriting function pointers.


SonarSource provided the following chart, which shows the chain of attacker-controlled pointer that enabled reading and writing to the entire address space:


Squirrel GitHub Repository Patched
----------------------------------


The maintainer of the Squirrel GitHub repository acknowledged the vulnerability in August. A patch was pushed out as part of a [code commit](https://github.com/albertodemichelis/squirrel/commit/23a0620658714b996d20da3d4dd1a0dcf9b0bd98) on Sept. 16.


But as noted by [The Hacker News](https://thehackernews.com/2021/10/squirrel-engine-bug-could-let-attackers.html), the changes haven’t been included in a new stable release, with the last official version (v3.1) released on March 27, 2016.


Thus, the researchers who discovered the vulnerability are “highly” recommending that maintainers who use Squirrel in their projects apply the available fix commit in order to protect against attacks.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[]] [[ThreatPost]]
