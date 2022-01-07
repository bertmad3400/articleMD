# EoL Systems Stonewalling Log4j Fixes for Fed Agencies
### End of life, end of support, pandemic-induced shipping delays and remote work, scanning failures: It’s a recipe for a patching nightmare, federal cyberserurity CTO Matt Keller says.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177475
+ Date: 2022-01-07T22:16:03+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/07171457/lizard-stone-wall-e1641593709939.jpeg)

Last month, federal agencies were given a Christmas Eve [deadline](https://federalnewsnetwork.com/cybersecurity/2021/12/agencies-get-christmas-eve-deadline-to-address-extremely-concerning-vulnerability/) – Dec. 24 – to address the “extremely concerning” [Log4j](https://threatpost.com/log4j-related-flaw-h2-database/177448/) and other vulnerabilities.


Nobody said it would be easy.


Besides the difficulty of tracking down all instances of the ubiquitous Apache logging library, the job of patching the flaws has been further complicated for many agencies by end-of-life (EoL) and end-of-support (EoS) systems connected to the network.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Matt Keller, Federal CTO of cybersecurity firm GuidePoint Security, told Threatpost in the following Q&A that many agencies are unable to patch Log4j, et al., due to network-connected EoL and EoS systems: an issue that’s further complicated by pandemic-wrought supply chain delays and remote-work issues.


Due to all these snafus, Keller has found that agencies are relying on running command-line scripts to find affected systems. They’re also constructing [tiger teams](https://www.lucidchart.com/blog/what-is-a-tiger-team) to tear into the monumental workload: i.e., specialized, cross-functional teams brought together to solve or investigate a specific problem or critical issue.


Between technology issues and travel restrictions/shipping delays involved in replacing these systems, Keller predicts that agencies are months away from being able to address Log4j.


**Threatpost:** What are the repercussions of not patching, particularly given the Federal Trade Commission’s (FTC’s) promise to [go after companies](https://threatpost.com/ftc-pursue-companies-log4j/177368/) that fail to protect consumer data from Log4Shell?


**Keller:** FTC saber rattling doesn’t affect the government directly. They can only hit up the companies, and if the government has budget or done their due-diligence to replace the capability … the government and FTC wouldn’t be able to find the company. Most of these [vendor] companies have provided solutions or resolutions for current software. It’s like having Windows 95 and telling [Microsoft] that they have to support the software forever because of a vulnerability like this.


**Threatpost:** How are organizations dealing with issues presented by EoL/EoS? Are they being forced to upgrade more or less at gunpoint?


**Keller:** Most organizations know they are running EoL or EoS software, and they haven’t put in the plan to do the migration because funding might have been pulled in 2020 or 2021 for COVID telework requirements. Also, with most government agencies working remotely, it’s hard to do a migration if you’re not able to be in the office or have the desire to come into the office.


**Threatpost:** What kind of issues does that entail? When you say that there are travel restrictions/shipping delays, what kind of time lags does that introduce? …. or is it unknown, is it anybody’s guess? If they can’t upgrade, what other options do they have?


**Keller:** One of our clients said it will take three+ months to ship equipment from their site to another site overseas because of logistics. Then once the equipment arrives, it may take another three months to put that server in the rack for the migration to happen. The only option is to do risk mitigation. If its mission is critical then we do protection and monitoring on that system. If it can be disabled until the replacement arrives then we support it that way.


**Threatpost:** What’s involved with having to run command-line scripts to find affected systems? How much does it slow things down?


**Keller:** To run some of these command-line scripts, you either need to have access to the system (remote/physical) to run the command or have an ability to run the command via scripting across the enterprise. The issue with running the script remotely is you could possibly miss a system that could be offline or doesn’t report back the results.


You hope your system management capability can provide a level of details to make sure systems are accurately reporting back in. There are just a ton of variables that have to be planned for with running scripts across the system.


**Threatpost:** What’s wrong with using available scanners? Are they missing a lot of Log4j instances? Why is that, if so?


**Keller:** Well, Log4J wasn’t really software installed on a system, so the normal software and software inventory scanner didn’t pick it up. Vulnerability Management scanners also have some original problems with supporting many of these same scans.


We have seen over the past month that Application Security products do a better job of finding the systems affected, but most agencies don’t deploy a robust [AppSec practice](https://threatpost.com/next-generation-application-security/175765/), so #1, having the software on hand was one issue, and #2 having the ability to figure out all of the [government off-the-shelf, or GOTs products: a term for software and hardware government that are ready to use and which were created and are owned by a government agency] solutions being built that use Log4J was a bigger issue.


Most of the OEM or [commercial off-the-shelf, or COTS] solutions had information out about Log4J in two weeks or less, but the COTS solutions had the EoL or EoS issues, which was more directly related to [the government] not planning for migration or replacements.


*Photo by [Maysam Yabandeh](https://pixnio.com/media/lizard-stone-wall-rough-architecture-texture) on [Pixnio](https://pixnio.com/). [Licensing details](https://creativecommons.org/licenses/publicdomain/).*


**Password** **Reset:** **[On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):** Fortify 2022 with a password security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the *new* password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken. **[Register & Stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)** – sponsored by Specops Software.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Derusbi]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=Dili]] [[victim.country.name=East Timor]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.city.name=Quito]] [[victim.country.name=Ecuador]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Keller]] [[Threatpost]] [[Log4j]] [[Eol]] [[Command-line]] [[Log4j]] [[ThreatPost]]

