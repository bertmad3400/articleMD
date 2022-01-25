# Software is crammed full of bugs. This exciting project could banish most of them | ZDNet
### Can a new initiative eradicate some of the most common software flaws?

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/software-is-crammed-full-of-bugs-this-exciting-project-could-banish-most-of-them/
+ Date: 2022-01-25 10:53:41
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/ef2b875fe7bdc3c1fc0437ae25fd54c80be936b0/2021/10/08/6043c4ed-b75a-4557-8b06-c68866d1f7a3/developers-coding-team-programming.jpg?width=770&height=578&fit=crop&auto=webp)

Chip designer Arm has released a prototype of its Morello development board for researchers at Google, Microsoft and industry to test its goal for a CPU design that wipes out a chunk of memory-related security flaws in code.

The [Morello board](https://www.arm.com/company/news/2022/01/morello-research-program-hits-major-milestone-with-hardware-now-available-for-testing) is the product of a collaboration between Arm, Cambridge University, Microsoft and others based on the Capability Hardware Enhanced RISC Instructions (CHERI) architecture. Microsoft says the board and system on chip (SoC) is the first high-performance implementation of CHERI, which provides "fine-grained spatial memory safety at a hardware level". If it proves successful after testing with legacy software, it could pave the way for future CPU designs.


CHERI architectural extensions are designed to mitigate memory safety vulnerabilities. CHERI augments pointers – the variables in computer code that reference where data is stored in memory – with limits as to how those references can be used, the address ranges that they can use to access, and which functionality they can use. "Once baked into silicon, they cannot be forged in software," [Arm explained](https://www.arm.com/blogs/blueprint/morello). CHERI was developed by the University of Cambridge and SRI International after it received funding from DARPA's Clean-slate design of Resilient, Adaptive, Secure Hosts ([CRASH](https://www.darpa.mil/program/clean-slate-design-of-resilient-adaptive-secure-hosts)) program.

**SEE:** [**The IT skills gap is getting worse. Here are 10 ways you can avoid a crisis**](https://www.zdnet.com/article/the-it-skills-gap-is-getting-worse-here-are-10-ways-you-can-avoid-a-crisis/#link=%7B%22linkText%22:%22The%20IT%20skills%20gap%20is%20getting%20worse.%20Here%20are%2010%20ways%20you%20can%20avoid%20a%20crisis%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/the-it-skills-gap-is-getting-worse-here-are-10-ways-you-can-avoid-a-crisis/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)

The Morello architecture is based on CHERI. Arm kicked off work on hardware for the Morello program in 2019 with backing from the UK government's Digital Security by Design (DSbD) program and UK Research and Innovation (UKRI).       

The Morello demonstrator board is a tweaked Arm Neoverse N1, a 2.5GHz quad-core server core CPU with support for Armv8.2a 64-bit architecture that has extra features to enable CHERI-based "compartmentalization" to counter exploits against memory-related security flaws. 

"For any research project, this phase is both exciting and critical. There has never been a silicon implementation of this hardware capability technology in a high-performance CPU," said Arm.






The Morello board is a significant advancement for CHERI, which has been in development for over a decade. Saar Amar, of Microsoft's Security Research and Defense team, [notes](https://msrc-blog.microsoft.com/2022/01/20/an_armful_of_cheris/) the top existing implementation of CHERI topped was Toooba, which –while a "significant achievement" – could only run in an FPGA at 50MHz in a dual-core configuration. It was "roughly equivalent in microarchitecture to a mid-'90s CPU" that wasn't good enough for testing complex software stacks at scale.  

The CHERI and Morello architectures may be one way of tackling memory-related security flaws that stem from code written in programming languages like C and C++. Microsoft and [Google say](https://www.zdnet.com/article/chrome-70-of-all-security-bugs-are-memory-safety-issues/) the [majority of security bugs](https://www.zdnet.com/article/microsoft-70-percent-of-all-security-bugs-are-memory-safety-issues/) are memory safety issues and they're often due to coding issues written in these languages. 

The volume of these bugs and patches they require has prompted major software firms like Microsoft, Google and Amazon to explore 'type safe' languages like Rust for systems programming. However, Rust is generally used to write new components because vast, existing code bases written in C or C++ are left in place, [as Google is doing for Android's code base](https://www.zdnet.com/article/rust-support-moves-into-android-underpinnings/).     

The Morello boards are being shared with researchers to test the hypothesis of CHERI's compartmentalization approach and whether it is a viable security architecture for businesses and consumers in the future. 

As detailed in a [paper about CHERI by Google researcher Ben Laurie and peers](https://www.links.org/files/Why%20You%20Should%20Care%20About%20CHERI.pdf), various CHERI modes can be more effective and efficient than mitigations in conventional memory management unit (MMU) hardware, which are used to translate virtual memory addresses to physical addresses. 

CHERI allows for software compartmentalization in a similar way to process isolation in software for today's operating systems, notes Laurie. It also includes an in-process memory safety mechanism that avoids the need to make major changes to source-code – a potentially major benefit for existing code bases.    

"Contemporary type-safe languages prevent big classes by construction, whereas CHERI memory protection prevents the exploitation of some of these bug classes," writes Microsoft's Armar. 

"There are billions of lines of C and C++ code in widespread use, and CHERI's strong source-level compatibility provides a path to achieving the goals of high-performance memory safety without requiring a ground-up rewrite."





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=Arp]] [[action.malware.name=at]] [[action.malware.name=RTM]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Construction]] [[victim.industry.name=Education]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Cheri]] [[Microsoft]] [[Google]] [[Memory-related]] [[High-performance]] [[C++]] [[ZDNet]]

