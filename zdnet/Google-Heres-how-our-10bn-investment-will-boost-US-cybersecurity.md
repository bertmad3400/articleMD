# Google: Here's how our $10bn investment will boost US cybersecurity
### Google has outlined its efforts to shape the US government's zero-trust initiative based on President Biden's Executive Order on cybersecurity.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/software-supply-chain-security-google-touts-its-10bn-investment-and-zero-trust-work/)
+ Date: August 27, 2021 -- 10:26 GMT (11:26 BST)
+ Author: Liam Tung


## Article:
Unknown

Google has outlined its efforts to shape the US government's zero-trust initiative, based on Biden's May Executive Order on cybersecurity.

Google's $10 billion commitment to beefing up critical US infrastructure includes expanding zero-trust programs, helping to secure software supply chains, and enhancing open-source security.

Its contributions will see the company leverage initiatives that have been underway [at Google for many years](https://www.zdnet.com/article/google-releases-new-open-source-security-software-program-scorecards/), spanning [open-source fuzzing tools](https://www.zdnet.com/article/googles-automated-fuzz-bot-has-found-over-9000-bugs-in-the-past-two-years/) to [funding Linux kernel developers to work on security](https://www.zdnet.com/article/google-funds-linux-kernel-developers-to-work-exclusively-on-security/), and pushing for the use of memory-safe languages in Linux. 

It comes after US president Joe Biden called on the chiefs of Apple, Google, Microsoft and JPMorgan Chase earlier this week to beef up the nation's protection of critical infrastructure.

Although Google was [not among the 18 cybersecuity companies selected to work with the U.S. Department of Commerce's National Institute of Standards and Technology (NIST) program](https://www.zdnet.com/article/microsoft-touts-role-in-meeting-bidens-cybersecurity-order/) -- which will establish create Zero Trust designs for federal agencies to implement -- it is now collaborating with NIST to develop a framework, [Google's Eric Brewer and Dan Lorenc said in a blog post](https://security.googleblog.com/2021/08/updates-on-our-continued-collaboration.html). 

Zero Trust assumes that a network has been breached and refocuses cybersecurity on apps, data and people, rather than hardening the network perimeter.   

"Instead of being reactive to vulnerabilities, we should eliminate them proactively with secure languages, platforms, and frameworks that stop entire classes of bugs," said Brewer and Lorenc.






"Preventing problems before they leave the developer's keyboard is safer and more cost-effective than trying to fix vulnerabilities and their fallout."


Biden appealed to the private sector at the White House cybersecurity summit on Wednesday, noting that federal government alone couldn't meet the challenge of protecting critical infrastructure from cyberattacks. 

Google and Microsoft [committed $10 billion and $20 billion, respectively](https://www.zdnet.com/article/tech-giants-make-cybersecurity-commitments-after-white-house-meeting/), over five years to improve the US response to future threats, following recent high-profile cyber attacks including the [Colonial Pipeline ransomware attack](https://www.zdnet.com/article/colonial-pipeline-ransomware-attack-everything-you-need-to-know/), the [SolarWinds software supply chain attack](https://www.zdnet.com/article/microsoft-solarwinds-attack-took-more-than-1000-engineers-to-create/) and [widespread hacking of Microsoft Exchange server vulnerabities](https://www.zdnet.com/article/fbi-blasts-away-web-shells-on-us-servers-in-wake-of-exchange-vulnerabilities/).   

"You have the power, capacity and responsibility, I believe, to raise the bar on cybersecurity. Ultimately we've got a lot of work to do," Biden said, [according to The Washington Post](https://www.washingtonpost.com/technology/2021/08/25/white-house-cybersecurity-summit-apple-amazon/). 

In June, Brewer [submitted four papers](https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity/enhancing-software-supply-chain-security) in response to Biden's cybersecurity [Executive Order 14028](https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity) on enhancing software supply chain security. 

One of the papers discusses the security problems inherent to coding in the C programming language and the emergence of Rust. 

"Secure languages and application frameworks can be used to impose a structure on software that enables high-confidence reasoning about its security, at scale," Brewer wrote. 


"But ensuring that this requirement is actually fulfilled for real-world C code is challenging, and often requires difficult reasoning about heap memory structure. Similarly, it is difficult to ensure correct validation and escaping for all data that flows into a web application's HTML markup, since data often passes through several components on its way from inputs to outputs, such as through a storage schema."

"In contrast, Rust has emerged as a practical alternative to C and C++ as a systems-development language, embodying a secure-by-construction stance on memory safety. Rust's type system imposes an ownership discipline that ensures, for example, that freed memory cannot be accessed."

To that end, Google is backing a [plan to get Rust into the Linux kernel](https://www.zdnet.com/article/rust-in-the-linux-kernel-just-got-a-big-boost-from-google/) as a second language to C. Lorenc and Brewer argue that software bugs should be limited from the outset, rather than just reacting to new vulnerabilities. Microsoft and Amazon Web Services are [also backing Rust](https://www.zdnet.com/article/amazon-were-hiring-software-engineers-who-know-programming-language-rust/) as a memory-safe alternative to C and C++ for systems programming.    

Google advocates for software code testing, including using tools from Microsoft-owned [GitHub, such as Dependabot -- a tool for keeping open source software packages or dependencies up to date](https://www.zdnet.com/article/github-rolls-out-dependency-review-offers-alerts-for-new-vulnerabilities-to-developers/). 

Google also offered its opinion on the idea of a [software bill of materials](https://www.zdnet.com/article/linux-and-open-source-communities-rise-to-bidens-cybersecurity-challenge/) (SBOMs) as part of the official US response to software supply chain attacks. The Linux Foundation is contributing this aspect of Biden's order. It's a complex problem to solve in both open-source and proprietary software due to the vast number of library dependencies used in modern programs. 

"SBOMs need a reasonable signal-to-noise ratio: if they contain too much information, they won't be useful, so we urge the NTIA [National Telecommunications and Information Administration] to establish both minimum and maximum requirements on granularity and depth for specific use-cases," Google said.





#### Tags:
[[Google]] [[Biden]] [[Microsoft]] [[open-source]] [[Linux]] [[cybersecurity]] [[ZDNet]]
