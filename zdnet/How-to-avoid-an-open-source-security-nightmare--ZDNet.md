# How to avoid an open source security nightmare | ZDNet
### Just as it would be a mistake to say that all closed source projects are bug-free, it's a mistake to say that all open source projects are security risks. Different projects have different focuses; some of them are much more concerned with the security of their releases.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/how-to-avoid-an-open-source-security-nightmare/
+ Date: 2022-01-28 16:06:00
+ Author: Forrester Research


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/4c41083a804455f9a13034d0dcdf4655d53d865f/2022/01/18/b0256ff2-881d-45cf-ba36-63708db9a6b1/open-source.jpg?width=770&height=578&fit=crop&auto=webp)

There have been a few high-profile security problems with open source software. A disgruntled developer recently delivered intentionally modified releases of his faker.js and colors.js packages, which broke "[thousands of projects](https://www.bleepingcomputer.com/news/security/dev-corrupts-npm-libs-colors-and-faker-breaking-thousands-of-apps/)" that relied on them. Some are wondering if it's safe to use open source software at all. The White House certainly is — they've [asked major technology companies](https://www.whitehouse.gov/briefing-room/statements-releases/2022/01/13/readout-of-white-house-meeting-on-software-security/) to comment about software security in the aftermath of the Log4j issue, which exposed countless servers to remote exploitation. 


Is code that's written by volunteers less secure than code written by professional developers? Do you need to have someone sue if a product fails? Do you really get what you pay for? 

**What is Open Source?**

Just as it would be a mistake to say that all closed source projects are bug-free, it's a mistake to say that all open source projects are security risks. Different projects have different focuses; some of them are much more concerned with the security of their releases. 

Josh Berkus has identified [five types of open source projects](https://wackowiki.org/doc/Org/Articles/5TypesOpenSourceProjects) based on their structure: 

* A **solo** project is the passion of one individual or, at most, a few dedicated people with the same vision.
* A **monarchy** is a successful solo project like Linux that's gained the support of a large community of contributors, so the original creator acts as a benevolent tyrant.
* A **community** project such as PostgreSQL springs up among peers with a similar goal and is driven by consensus.
* A **corporate** project is often released as a fork of a commercial project, as when Sun released OpenOffice as an open source fork of StarOffice. Its direction is guided by the company that released it.
* A **foundation**, the most formal, is a standalone business structure — of which Apache is perhaps the best example. There, a steering board makes the decisions.

In general, solo projects are the most exposed to security risks. Just as a writer can update his web page with any content whatsoever, a solo developer can update her code in the same way. Often, there's not enough interest in a community to fork solo projects, so they become de facto standards. We saw this with faker.js and colors.js, when Marak Squires modified his code to print flags and enter infinite loops. 

The security of both open and closed source projects depends on the focus of their contributors, rather than their structure. We've been lucky that Linus Torvalds has had security as one of his concerns. Theo de Raadt, has been conscious of security for OpenBSD from the beginning. In contrast, both StarOffice (commercial) and OpenOffice had security holes that allowed remote execution of arbitrary code in XML documents. 






**Many eyes focused elsewhere?**

One of the ironies of open source is the assumption that many eyes improve security. For years, we heard claims that open source was more secure because "the community" could review the code. The problem: "The community" rarely reviews the code, and everyone just assumed that someone else was doing it. That false sense of security really blew up during Heartbleed — the reality of too much code and too few eyes means that we need better processes and automation to improve open source security. 

There's another false sense of security, though: Don't assume that closed source software has better processes just because you can't see them. In the case of Heartbleed, "the community" did eventually review the holes in OpenSSL, and the solution was … more open source. LibreSSL, a fork of OpenSSL, had a focus on security rather than backward compatibility. 

**Open Source requires shared accountability**

Although you don't pay money when you use open source software, that doesn't mean you don't have obligations — to your business, to your customers, and to the community. Be responsible when making use of open source software: 

* **Know what you're using.** One of the biggest dangers of some ecosystems is the ease with which one open source project can include another. Many projects today include other projects as components. Systems like npm make it easy to bring in code without realizing it. Tools exist to help generate software bills of materials (SBOMs) and to scan your code to see if you're dependent on something you didn't know about.
* **Avoid solo and abandoned projects.** A single malicious developer can inject a lot of harm — especially if you're upgrading automatically. The danger of using abandoned projects is that they may not account for modern vulnerabilities. Evaluate the status of the projects you use with every release.
* **Test before you release.** Much of the danger with open source projects comes from upgrading without testing. If your code includes an open source library with an exploit, your users will hold you responsible. Certify with specific versions of projects and keep those up to date. Fork open source libraries that you use and dedicate resources to reviewing what has been committed.
* **Plan for updates.** The Log4j vulnerability was particularly dangerous because it allowed the execution of arbitrary code on platforms that have software baked into ROM. For some internet-of-things devices, there's no way to upgrade the Log4j library to fix it. This leaves a persistent vulnerability that can't be addressed. Don't put your product in the same predicament. Provide an upgrade (and downgrade!) path for every component. Don't wait for a security issue to upgrade your code, either — plan to update regularly to more recent versions to improve your code's hygiene.
* **Contribute to open source projects**. Many open source projects deliver useful code with few resources. Commit to contributing either financially or by supplying development or QA resources to the open source libraries you use. Don't limit your open source contributions to the day you pull the library — open source needs ongoing support, so include open source contributions in your annual budget and long-term planning. You want to be sure the latest release is as secure as the one you first pulled.
* **Invest in DevSecOps.** Assume that frequent updates are the norm, not the exception. Whether it's code created by your own team or code you brought in from an open source project, realize that bugs will happen, updates will be needed, and that, in some cases, rapid iteration will be required to keep up with changes. DevOps, in the form of CI/CD, is now table stakes; up the ante by adding "Sec" — the ability to shift-left automated security checks directly into the dev cycle so that when those updates come in, you're better prepared to get the fix out the door with fewer all-nighters and much less toil and stress.

**Wake up from the nightmare**

If you're afraid of using open source, it's too late. You're unlikely to use a product today without open source components. It's almost certain that you're reading this with a browser based on open source technology, served by a web server that has an open source core — all built with open source tools. Although a nightmare isn't reality, it may be a response to legitimate anxiety. Use open source software responsibly to avoid the goosebumps. 

*This post was written by Senior Analyst Andrew Cornwall and it originally appeared* [*here*](https://www.forrester.com/blogs/avoid-an-open-source-security-nightmare/?utm_source=zdnet&utm_medium=pr&utm_campaign=sr)*.*





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[ZDNet]]

