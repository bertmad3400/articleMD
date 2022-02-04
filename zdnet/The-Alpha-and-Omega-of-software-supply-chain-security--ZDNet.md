# The Alpha and Omega of software supply chain security | ZDNet
### The Alpha-Omega Project will improve open-source software's security. While it's a good start, it may not be enough.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/the-alpha-and-omega-of-software-supply-chain-security/
+ Date: 2022-02-04 15:53:22
+ Author: Steven Vaughan-Nichols


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/c391d16668e34b6d73a82ec7f76bdb770829c37d/2020/10/29/eb5a5558-c07a-464b-b0b0-1c0a25baa707/openssf-certifcate.jpg?width=770&height=578&fit=crop&auto=webp)

What is the [Alpha-Omega Project](https://openssf.org/community/alpha-omega/)? Its purpose is to "improve global open source software supply chain security by working with project maintainers to systematically look for new, as-yet-undiscovered vulnerabilities in open-source code" and then fix them. This is vital to improving open-source security. 


To make this happen, the [Linux Foundation](https://linuxfoundation.org/)'s partner group -- [Open Source Security Foundation (SSF)](https://openssf.org/), Google, and Microsoft -- are joining forces to work with security experts and use automated security testing to improve open-source security. Microsoft and Google are bringing an initial investment of $5 million to the Alpha-Omega Project. 

[Software supply chain security](https://www.zdnet.com/article/linux-foundation-adds-software-supply-chain-security-to-lfx/) has become essential. One major security problem after another -- including the [SolarWinds software supply chain attack](https://www.zdnet.com/article/microsoft-solarwinds-attack-took-more-than-1000-engineers-to-create/), the [Log4j vulnerability](https://www.zdnet.com/article/the-log4j-flaw-hasnt-led-to-massive-hacking-attacks-but-that-doesnt-mean-the-threat-is-over/), and the [npm bad code injection](https://www.zdnet.com/article/when-open-source-developers-go-bad/) episode -- can be traced back to software supply chain vulnerabilities. 

Hackers and national adversaries have made widely-deployed open-source projects their top targets. These days, when a new vulnerability is disclosed, it's only a matter of hours until it's exploited. For instance, the widely deployed [Log4j library problems forced many organizations into crisis mode](https://www.zdnet.com/article/log4j-flaw-hunt-shows-how-complicated-the-software-supply-chain-really-is/) as they raced to update applications before they could be attacked. 

A separate part of the problem, as  Jack Aboutboul VP of Products at software chain security company, [CodeNotary](https://codenotary.com/) points out, is paying developers and maintainers for this work. He asks: "Did you hear about the Fortune 500 corporation that emailed an open-source maintainer to "[Demand Answers](https://twitter.com/bagder/status/1484672924036616195)" about his software package, which they've never paid for, and which they've now realized is being used in their software? We did. And we didn't think it was funny. This story showcases what is perhaps the most obvious truth about how the software supply chain can be secured – by paying maintainers. Any project or initiative, such as the one launched by OpenSSF, will never be complete and never fully actualized unless money is being earmarked to pay those maintainers of Omega software. Otherwise, the outcome will just be to identify more holes in a maintainer's code which will cause them to work more hours, not less, for the same non-existent compensation."

The Alpha-Omega Project aims to skip all of this by finding open-source code vulnerabilities and fixing them before they can be targeted. I wish them luck. 

### The Alpha...

Alpha will work with the most critical open-source project maintainers. Specifically, Alpha will cover both standalone projects and core ecosystem services selected based on the work by the OpenSSF [Securing Critical Projects working group](https://github.com/ossf/wg-securing-critical-projects). To do this, Alpha will use both expert opinions and data. This will include data from open-source security projects, such as the OpenSSF [Criticality Score](https://github.com/ossf/criticality_score) and [Harvard's "Census" analysis](https://www.coreinfrastructure.org/programs/census-program-ii/).






For these selected projects, Alpha team members will provide tailored help to understand and address security gaps. This will include threat modeling, automated security testing, source code audits, and support remediating vulnerabilities that are discovered. Its best practices will be drawn in part from the OpenSSF [Scorecard](https://github.com/ossf/scorecard) and [Best Practices Badge](https://bestpractices.coreinfrastructure.org/) criteria.

### ...and the Omega

The Omega side of the project will start by identifying at least 10,000 widely deployed open-source programs. Once that's done, the project's team will apply automated security analysis and scoring to the programs' code. Finally, the Omega crew will follow up by giving remediation guidance to the maintainer communities. 

This is by no means easy. Omega will do this with automated methods and tools to identify critical security vulnerabilities. To make this happen, its developers will use a combination of technology, cloud-scale analysis' people, security analysts triaging findings; and process, confidentially reporting critical vulnerabilities to the programs' stakeholders. To make this happen, Omega will use a dedicated team of software engineers. They will be continually working on reducing false-positive rates and identifying new vulnerabilities.

Even with its own security team, as Eric Brewer, Google VP of Infrastructure and Fellow pointed out, "The long tail of important open-source software, the 'Omega' of this endeavor, is always the hardest part—it will require not only considerable funding and perseverance, but its scale will also drive extensive automation for tracking and ideally fixing vulnerabilities. Enabling automation will be one of the greatest improvements for open source security."

"Open-source software is a vital component of critical infrastructure for modern society. Therefore we must take every measure necessary to keep it and our software supply chains secure," said Brian Behlendorf, OpenSSF's General Manager. "Alpha-Omega supports this effort in an open and transparent way by directly improving the security of open source projects through proactively finding, fixing, and preventing vulnerabilities."

If all goes well, Mark Russinovich, Microsoft Azure CTO, said "Alpha-Omega will provide assurance and transparency for key open-source projects through direct engagement with maintainers and by using state-of-the-art security tools to detect and fix critical vulnerabilities. We look forward to collaborating with industry partners and the open-source community on this important initiative."

### Questions remain

But is this enough? Aboutboul doesn't think so. Technically, Aboutboul is concerned that neither Alpha-Omega's [sigstore](https://www.sigstore.dev/) technology ( particularly [cosign](https://github.com/sigstore/cosign) and [Rekor](https://github.com/sigstore/rekor)) nor its financial and personnel resources are up to the job.. "First, [cosign is based on certificates and keys](https://codenotary.com/blog/openssfs-alpha-omega-project-good-but-not-enough/) – ancient technologies. What happens if you sign billions of artifacts with a certificate and then that certificate is now compromised? Will you go back and revoke the trust of all your assets? Furthermore, what if the actual trust root becomes compromised somehow? Serious questions to be asked and answered."

Aboutboul also worries that [Rekor](https://www.rekor.ai/), which is meant as the project's immutable, tamper-resistant ledger and functions as a transparency log of metadata about artifacts in a supply chain, isn't good enough. That's because "Rekor utilizes [Google's Trillian](https://github.com/google/trillian) for its underlying append-only data structure and requires MySQL or MariaDB and Redis underneath. Ultimately, this leaves room for vulnerability. There are too many moving pieces at play here, and the more pieces means more pieces you need to trust, or actually shouldn't need to trust."

Finally, on the technical side of things, Aboutboul notes that Rekor comes right out and says,  "'[IMPORTANT: This instance is currently operated on a best-effort basis](https://github.com/sigstore/rekor). We will take the log down and reset it with zero notice. We will improve the stability and publish SLOs over time.' Yikes!"

Aboutboul deals with these issues by relying on its open-source immutable database, [immudb](https://github.com/codenotary/immudb/). Why? CodeNotary eats its own dog food because "immudb is itself an immutable database and doesn't rely on any external piece of infrastructure, there is no room for doubt, no room for risk. What goes into immudb is stored in immudb, in a tamper-proof and verifiable way."

Besides the technology, Aboutboul has two other important issues he thinks need to be addressed. First, "While  $5 million sounds like a lot of money (and it is), it seems like a paltry sum to carry out this mission. The depth of penetration of open source into the global software supply chain is daunting. When you start to take a look at your potential Alpha projects, say, the Linux Kernel, etc. the effort there alone can potentially utilize almost all of that. How do you get to all your Omega projects then?"

That said, Aboutboul agrees that  Alpha-Omega is a good, major step forward. But, Aboutboul makes several excellent points. In the end, the elephant in the room is money for developers and maintainers. Like it or not, we must make paying for open-source security a priority. 

**Related Stories:**

* [Securing the open-source ecosystem: SBOMs are no longer optional](https://www.zdnet.com/article/securing-the-open-source-ecosystem-sboms-are-no-longer-optional/)
* [Codenotary: Notarize and verify your software bill of materials](https://www.zdnet.com/article/codenotary-open-source-notarization-service-for-software-bill-of-material-arrives/)
* [For security alone, we could try paying open-source projects properly](https://www.zdnet.com/article/for-security-alone-we-could-try-paying-open-source-projects-properly/)





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Open-source]] [[Aboutboul]] [[Alpha-omega]] [[Openssf]] [[Google]] [[Immudb]] [[Microsoft]] [[Rekor]] [[ZDNet]]

