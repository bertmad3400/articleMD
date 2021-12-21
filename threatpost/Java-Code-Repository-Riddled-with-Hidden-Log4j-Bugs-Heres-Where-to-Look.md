# Java Code Repository Riddled with Hidden Log4j Bugs; Here's Where to Look
### There are 17,000npatched Log4j packages in the Maven Central ecosystem, leaving massive supply-chain risk on the table from Log4Shell exploits.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177211
+ Date: 2021-12-21T20:46:35+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/21151757/Logs-e1640117899602.png)

There’s an enormous amount of software vulnerable to the Log4j bug through Java software supply chains — and administrators and security pros likely don’t even know where to look for it.


About 17,000 Java packages in the Maven Central repository, the most significant collection of Java packages available to developers, are [vulnerable to Log4j](https://security.googleblog.com/2021/12/understanding-impact-of-apache-log4j.html) — and it will likely take “years” for it to be fixed across the ecosystem, according to Google security.


Following the CVE update that just Log4j-core was affected, eliminating vulnerable instances of the Log4j-api, Google Security determined that as of Dec. 19, more than 17,000 packages in Maven Central were vulnerable, about 4 percent of the entire repository. Of those, just 25 percent of the packages had updated versions available, Google added.


For comparison, the Google researchers explained in a Tuesday blog post that the average bug affects between 2 percent and less than .01 percent of such packages.


Sonatype, the organization which maintains Maven Central, has a dashboard that’s updated several times a day with the latest on Log4j and reported that since Dec. 10, more than 40 percent of the packages being downloaded were still [vulnerable](https://www.sonatype.com/resources/log4j-vulnerability-resource-center?utm_campaign=Log4j%3A%20External%20Campaign&utm_medium=email&_hsmi=198291559&_hsenc=p2ANqtz--Kuyq9bjSL5oCJeOC6g7dceRsjhsJFZIVeV6vzkAkYz_epiF3YgQiGLaOBsV3uGqDcti1A2hGt_liiropxvTZqbQfNbQGok9j2RkX667DUULsgl7I&utm_content=198291559&utm_source=hs_email), totaling nearly 5 million downloads.


And those are new downloads that leave apps and projects open to [Log4j attacks](https://threatpost.com/log4j-attacks-state-actors-worm/177088/).


**Start At the Deepest Point in Supply Chain and Work Up**
----------------------------------------------------------


Log4j is lurking in “dependencies” on flawed code, both direct and indirect, up and down the supply chain, Google explained.


“The majority of affected artifacts come from indirect dependencies (that is, the dependencies of one’s own dependencies), meaning Log4j is not explicitly defined as a dependency of the artifact, but gets pulled in as a transitive dependency,” the Google team said.


Making these [unpatched Log4j versions](https://threatpost.com/conti-ransomware-gang-has-full-log4shell-attack-chain/177173/) even sneakier to track down is “how far down the software supply chain it’s typically deployed,” the analysts added.


“For greater than 80 percent of the packages, the vulnerability is more than one level deep, with a majority affected five levels down (and some as many as nine levels down),” the report warned. “These packages will require fixes throughout all parts of the tree, starting from the deepest dependencies first.”


**Why Java Is Trickier Than Other Ecosystems**
----------------------------------------------


Adding another degree of difficulty to ferreting out the Log4j bugs is Java’s “soft” version requirements, according to Google.


“Propagating a fix often requires explicit action by the maintainers to update the dependency requirements to a patched version,” the Google researchers said. “This practice is in contrast to other ecosystems, [such as npm](https://threatpost.com/discord-stealing-malware-npm-packages/163265/), where it’s common for developers to specify open ranges for dependency requirements.”


In the face of these unique challenges, Google reported open-source maintainers and security teams have already made incredible efforts to patch systems. But there’s still a ton of work left to do before Log4j is in the industry’s rear view for good.


To help out, Google has pulled together a list of the [500 most-used and impacted Java code packages](https://security.googleblog.com/2021/12/understanding-impact-of-apache-log4j.html).


“We looked at all publicly disclosed critical advisories affecting Maven packages to get a sense of how quickly other vulnerabilities have been fully addressed,” the team said. “Less than half (48 percent) of the artifacts affected by a vulnerability have been fixed, so we might be in for a long wait, likely years.”


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=Paris]] [[victim.country.name=France]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Google]] [[Log4j]] [[ThreatPost]]

