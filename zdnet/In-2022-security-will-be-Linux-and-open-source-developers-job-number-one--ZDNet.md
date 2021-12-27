# In 2022, security will be Linux and open-source developers job number one | ZDNet
### Linux and open-source software will be hotter than ever, but the real changes will be in how they're secured.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/in-2022-security-will-be-linux-and-open-source-developers-job-number-one/
+ Date: 2021-12-27 14:40:09
+ Author: Steven Vaughan-Nichols


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/02a36bda191409e58cc3d9aefc81fd694a36f3e5/2020/08/17/abe5a63a-ed4e-4836-be49-48ebf7d409f2/istock-5429285961.jpg?width=770&height=578&fit=crop&auto=webp)

Linux is everywhere. It's what all the [clouds, even Microsoft Azure, run](https://www.zdnet.com/article/microsoft-developer-reveals-linux-is-now-more-used-on-azure-than-windows-server/).  It's [what makes all 500 of the Top 500 supercomputers work](https://www.zdnet.com/article/microsoft-now-has-one-of-the-worlds-fastest-supercomputers-and-no-it-doesnt-run-on-windows/). Heck, even desktop Linux is growing if you can believe [Pornhub, which claims Linux users grew by 28%](https://www.pornhub.com/insights/yir-2021#Age-Demographics), while Windows users declined by 3%. 


Open-source software is also growing by leaps and bounds. According to [Gartner's 2021 Hype Cycle for Open-Source Software (OSS)](https://more.suse.com/Global_Webpage_Gartner_Open_Source_Report.html): "Through 2025, more than 70% of enterprises will increase their IT spending on OSS, compared with their current IT spending. Plus, by 2025, software as a service (SaaS) will become the preferred consumption model for OSS due to its ability to deliver better operational simplicity, security, and scalability."

Thinking of databases, the beef and potatoes of enterprise software, [Gartner](https://www.gartner.com/en) predicts that over 70% of new in-house applications will be developed on an open-source database. Simultaneously,  50% of existing proprietary relational database instances will have been converted or are being converted to open-source DBMSs.

I'll buy those numbers. I've been following Linux and open-source software since day one. Everywhere I go and everyone I talk to acknowledges that the pair run the software universe.

But with great power also comes great responsibility as Spider-Man knows. And, as many developers recently found out when multiple [security vulnerabilities with the Apache Java logging open-source library log4j2](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/) were discovered, also comes great headaches.  

The log4j2 problems are as bad as bad can get. By the National Vulnerability Database (NVD) scale, it's rated as 10.0 CVSSv3 which is perfectly awful.

 Its real trouble isn't so much with open-source itself. There's [nothing magical about open-source methodology and security](https://www.computerworld.com/article/2478585/open-source-still-the-best-way-to-develop-software.html). Security mistakes can still enter the code. [Linus's law](https://opensource.com/article/21/2/open-source-security) is that given enough eyeballs, all bugs are shallow. But, if not enough developers are looking, security vulnerabilities will still go unnoticed. As what I'm now calling Schneier's law, "[Security is a process, not a product](https://www.schneier.com/essays/archives/2000/04/the_process_of_secur.html)," points out constant vigilance is needed to secure all software. 






That said, the real pain-in-the-rump with log4j is with how Java hides what libraries its source code and binaries use in numerous [Java Archive (JAR)](https://docs.oracle.com/javase/8/docs/technotes/guides/jar/jarGuide.html) variations. The result? You may be using a vulnerable version of log4j and not know until it's been exploited. 

As Josh Bressers, [Anchore](http://www.anchore.com/)'s vice president of security recently explained, "One of the challenges the log4j vulnerability poses is actually finding it. Java applications and dependencies are usually in some sort of packaging format that makes the distribution and running really easy, but it can make figuring out what's inside of those software packages difficult."

Fortunately, there are [log4j scanners](https://www.zdnet.com/article/multiple-log4j-scanners-released-by-cisa-crowdstrike-more/) that can help you spot defective log4j libraries in use. But, they're not perfect.

Behind the log4j mess is another problem, That's "How do you know what open-source components your software is using?" For example, log4j2 has been in use since 2014. You can't expect anyone to remember if they used that first version in some program you're still using today. 

The answer is one that the open-source community started taking seriously in recent years: The creation of [Software Bills of Material (SBOM)](https://www.ntia.gov/SBOM). An SBOM spells out exactly what software libraries, routines, and other code has been used in any program. Armed with this, you can examine what component versions are used in your program.

As David A. Wheeler, the [Linux Foundation](https://linuxfoundation.org/)'s Director of Open Source Supply Chain Security, has explained, by using SBOMs and [verified reproducible builds](https://reproducible-builds.org/), you can make sure you know what's what in your programs. That way, if a security hole is found in a component, you can simply patch it rather than search like a maniac for any possible problem code before being able to fix it. 

"A reproducible build," by the way explains Wheeler,  is one "that always produces the same outputs given the same inputs so that the build results can be verified. A verified reproducible build is a process where independent organizations produce a build from source code and verify that the built results come from the claimed source code."

To do this, you and your developers need to track your programs in an SBOM using the Linux Foundation's [Software Package Data Exchange (SPDX) format](https://spdx.dev/). Then, to further safeguard that your code is really what it claims to be you need to notarize and verify your SBOM with services such as the [Codenotary Community Attestation Service](http://cas.codenotary.com/) and [Tidelift Catalogs](https://www.zdnet.com/article/securing-your-open-source-software-supply-chain-with-tidelift-catalogs/).

All this is easy to say. Doing it hard. In 2022, pretty much all open-source developers are going to be spending a lot of time checking their code for problems and then building SPDX-based SBOMs. Users, worried over [Solarwind type disasters](https://www.zdnet.com/article/solarwinds-defense-how-to-stop-similar-attacks/) and log4j security problems, will be demanding this.  

At the same time, Linux developers are working on further securing the operating system by making [Rust Linux's second language](https://www.zdnet.com/article/rust-takes-a-major-step-forward-as-linuxs-second-official-language/). Why? Because, unlike C, Linux's primary language, Rust is much more secure. Specifically, Rust is much safer than C  at handling memory errors.

As Ryan Levick, a Microsoft principal cloud developer advocate, explained, "[Rust is completely memory safe](https://msrc-blog.microsoft.com/2019/07/22/why-rust-for-safe-systems-programming/)." That's a huge deal, since, as Linux kernel developers Alex Gaynor and Geoffrey Thomas pointed out at the 2019 Linux Security Summit, almost [two-thirds of Linux kernel security holes](https://static.sched.com/hosted_files/lssna19/d6/kernel-modules-in-rust-lssna2019.pdf) come from memory safety issues. And where do those come from? Inherent problems with C and C++.  

Now Linux is going to be rewritten in Rust. At least not this decade, check with me again in the 2030s, but a lot of Linux drivers and other code will be written going forward in Rust. 

As Linus Torvalds told me while he's "in no way 'pushing' for Rust," he's "open to it considering the promised advantages and avoiding some safety pitfalls. Still, he concluded, "I also know that sometimes promises don't pan out." 

We'll see how it all works out. No matter how the specifics go, one thing I know for certain. We're going to see securing code become the top issue for Linux and open-source developers in 2022.  They've both become too important for it to go any other way. 

**Related Stories:**

* [2022 technology trend review, part one: Open source, cloud, blockchain](https://www.zdnet.com/article/2022-technology-trend-review-part-one-open-source-cloud-blockchain/)
* [Codenotary: Notarize and verify your software bill of materials](https://www.zdnet.com/article/codenotary-open-source-notarization-service-for-software-bill-of-material-arrives/)
* [Rust takes a major step forward as Linux's second official language](https://www.zdnet.com/article/rust-takes-a-major-step-forward-as-linuxs-second-official-language/)





## Tags:

#### Action:
[[action.malware.name=Anchor]] [[action.malware.name=at]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Linux]] [[Open-source]] [[Log4j]] [[Log4j2]] [[Sbom]] [[ZDNet]]

