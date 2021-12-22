# Critical Apache HTTPD Server Bugs Could Lead to RCE, DoS
### Don’t freak: It’s got nothing to do with Log4Shell, except it may be just as far-reaching as Log4j, given HTTPD’s tendency to tiptoe into software projects.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177234
+ Date: 2021-12-22T17:59:55+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/22123327/cat-hiding.jpeg)

Don’t duck at the latest mention of Apache: Two critical bugs in its HTTP web server – HTTPD – need to be patched pronto, lest they lead to attackers triggering denial of service (DoS) or bypassing your security policies.


Apache, the open-source software foundation behind the Log4J logging library that’s been making for so many [Log4Shell](https://threatpost.com/conti-ransomware-gang-has-full-log4shell-attack-chain/177173/) headlines, on Monday put out an update to fix the two bugs in HTTPD, which is a web server that’s right up there with Log4j in its ubiquity.


Both vulnerabilities are found in Apache HTTP Server 2.4.51 and earlier.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The first issue (CVE-2021-44790) is with the function “r:parsebody” of the component “mod\_lua Multipart Parser.” As the [VulDB](https://vuldb.com/?id.188754) vulnerability database describes it, “manipulation with an unknown input leads to a memory-corruption vulnerability” that “is going to have an impact on confidentiality, integrity and availability.”


VulDB also noted that the issue is reportedly easy to exploit: It is possible to launch the attack remotely. The exploitation doesn’t require any form of authentication.”


Although technical details are known, there’s no available exploit – at least, not yet. As of Monday, the vulnerability’s structure had suggested that an exploit would fetch between $5,000 and $25,000, VulDB estimated.


In a Tuesday [writeup](https://nakedsecurity.sophos.com/2021/12/21/apaches-other-product-critical-bugs-in-httpd-web-server-patch-now/) of the two CVEs, Sophos principal security researcher Paul Ducklin said that the two bugs could leave servers at risk of some serious hurt.


“These bugs might not be exposed in your configuration, because they are part of optional run-time modules that you might not actually be using,” Ducklin noted. “But if you are using these modules, whether you realize it or not, you could be at risk of server crashes, data leakage or even remote code execution.”


On Monday, Apache published these details for the two CVEs in its [changelog:](https://downloads.apache.org/httpd/CHANGES_2.4.52)


* [CVE-2021-44790](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44790): Possible buffer overflow when parsing a carefully crafted request in the mod\_lua multipart parser of Apache HTTP Server 2.4.51 and earlier. Apache said that its HTTPD team hasn’t seen an exploit, but “it might be possible to craft one.”
* [CVE-2021-44224](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44224): Possible NULL dereference or Server Side Request Forgery (SSRF) in forward proxy configurations, likewise in Apache HTTP Server 2.4.51 and earlier.


On Tuesday, CERT-FR sent out an alert about the issue.



> 
> CERTFR-2021-AVI-972 : Multiples vulnérabilités dans Apache httpd (21 décembre 2021)<https://t.co/SB0gpBJcd4>
> 
> 
> — CERT-FR (@CERT\_FR) [December 21, 2021](https://twitter.com/CERT_FR/status/1473327492484186115?ref_src=twsrc%5Etfw)
> 
> 



HTTPD: It’s Here, It’s There, It’s Every-Bleeping-Where
-------------------------------------------------------


Ducklin noted that Apache’s brawny server has “more than 3,000 files totaling close to a million [lines] of source code,” making it not only “a large and capable server,” but one with “myriad combinations of modules and options, making it both powerful and dangerous at the [same] time.”


These bugs shouldn’t get lost amidst the Log4J brouhaha, Ducklin said, given that “you almost certainly have Apache HTTPD in your network somewhere. Just like Log4j, HTTPD has a habit of getting itself quietly included into software projects, for example as part of an internal service that works so well that it rarely draws attention to itself, or as a component built unobtrusively into a product or service you sell that isn’t predominantly thought of as ‘containing a web server.'”


Sean Nikkel, senior cyber-threat intel analyst at Digital Shadows, noted that a quick peek at the Shodan search engine reveals that there more than 3 million public devices running some version of HTTPD as of this writing, meaning there’s a chance that HTTPD is running on some internal or otherwise non-public instances.


That could mean that this vulnerability “may also be just as far-reaching as log4j,” Nikkel said.


The silver lining: “Apache dissuades people from using the mod\_lua functionality in several circumstances due to the amount of control it potentially has,” he told Threatpost on Wednesday. In fact, Apache has this cautionary note on its [mod\_lua](https://httpd.apache.org/docs/trunk/mod/mod_lua.html) site:



> This module holds a great deal of power over httpd, which is both a strength and a potential security risk. It is not recommended that you use this module on a server that is shared with users you do not trust, as it can be abused to change the internal workings of httpd.
> 
> 


However, Nikkel said, that doesn’t rule out the human factor: “There’s always the chance a server was misconfigured,” he noted.


Kudos to Patchy Apache
----------------------


Used to be, the name “Apache” was presumed to be a pun for building “patchy” software, given how the open-source software was built on existing code and a bunch of software patches (but that’s not really how it got its name, according to the project’s [official documentation](https://web.archive.org/web/19970415054031/http://www.apache.org/info.html)).


Still, kudos to Apache for being extremely patchy of late, security experts said.


“It should be noted that Apache has done an exceptional job addressing the vulnerabilities that have been discovered in their products this year,” Hank Schless, senior manager of security solutions at  Lookout, commented to Threatpost via email. “They’re pushing updates as soon as possible, and making it widely known that patches are available for teams. It’s important to keep in mind that software vulnerabilities are inevitable – especially these days when applications are so complex and users expect constant updates from the developers.”


OK, gratitude aside, could we just catch up with all these issues, already? That’s what Yaniv Bar-Dayan, CEO and co-founder at Vulcan Cyber, wants to know. “The integrated IT security industry is not very good at effectively mitigating known vulnerabilities, and Apache vulnerabilities are no exception,” he told Threatpost via email. “Our cyber-debt specific to Apache software was substantial prior to Log4Shell or these new HTTPD web server vulns.”


He pointed to CVE-2020-1938, the so-called “Ghostcat” security bug in the popular Apache Tomcat web server that cropped up in 2020, as an example. The bug led to a [working exploit leaking on GitHub](https://threatpost.com/apache-tomcat-exploit-stealing-files/154055/) that made it a snap to exploit.


That same bug, in the Apache JServ Protocol (AJP), “has been getting a lot of interest on Remedy Cloud almost a full two years after it was disclosed,” Bar-Dayan said.


If Apache were the only software the industry had to worry about securing when vulnerabilities are found, that would be manageable, he said. But no: According to NIST, 2021 will be another record year for new vulnerability disclosures, Bar-Dayan continued.


“We need to do much better as cybersecurity pros to identify the vulnerabilities that matter to our businesses and organizations, by assessing and prioritizing associated risk,” he said. “Then we need to take control and orchestrate the mitigation effort while measuring our ability to drive cyber-hygiene and attain acceptable levels of risk.”


This Is a Priority Patch
------------------------


Schless urged IT teams to address the CVEs immediately, prioritizing anything that’s publicly accessible or web-facing. “These assets are the ones that attackers will scan for in order to find vulnerable systems and exploit the vulnerability,” he said.


After that, security teams should then move on to assessing and addressing internal servers and applications to which only employees have access, he added.


“The scope of impact is likely more limited than what we’ve seen recently, but that shouldn’t change the urgency with which the CVEs are patched,” Schless recommended. “If attackers aren’t yet in a vulnerable environment, they will be scanning the internet for vulnerable software using HTTPD. However, if the attacker has already made their initial entry and is performing reconnaissance on the environment, they will likely try to locate vulnerable internal assets. This highlights the importance of understanding how every user in your infrastructure accesses and interacts with your apps and the data stored in them.”


Nikkel noted that support teams that might be stressing over yet another patch might wring some solace out of the fact that there are “some conditions and mitigations to this, so it may not apply to all installations.”


Still, given that “these are typical web services deployed facing the internet,” the “patch ASAP” rule yet again applies, he said.


*Image courtesy of [Tom Thai](https://www.flickr.com/photos/eviltomthai/4411718240). [Licensing details](https://creativecommons.org/licenses/by/2.0/).* 


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Httpd]] [[Http]] [[Cves]] [[Ducklin]] [[Nikkel]] [[Threatpost]] [[Teams]] [[Vuldb]] [[Mod_lua]] [[Httpd]] [[ThreatPost]]
#### urls
https://t.co/SB0gpBJcd4
#### CVE's
[[CVE-2021-44790]] [[CVE-2021-44224]] [[CVE-2020-1938]]

