# Log4j flaw: 10 questions you need to be asking | ZDNet
### NSCS warns that the Log4j flaw won't be fixed overnight and that defenders could suffer burnout during the process.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/log4j-flaw-10-questions-you-should-be-asking/
+ Date: 2021-12-21 12:08:08
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/32d5e4606a71596e1ea97276ba10aea050ad4cda/2021/03/19/6c4e4301-f8e2-4321-8518-ecf035f74ec4/istock-992574526-2.jpg?width=770&height=578&fit=crop&auto=webp)

The UK National Cyber Security Centre (NCSC) is urging company boards to start asking key questions about how prepared they are to mitigate and remediate the widespread, critical Log4Shell flaw in Java-based application error logging component Log4j.

NCSC [calls Log4Shell](https://www.ncsc.gov.uk/blog-post/log4j-vulnerability-what-should-boards-be-asking) "potentially the most severe computer vulnerability in years" and called upon company boards to treat this bug with urgency. It stresses the Log4j bug – also known as Log4Shell – is a software component rather than a piece of software, which means it will be much more complicated to patch. 

Log4Shell is [bad news today](https://www.zdnet.com/article/google-unleashes-security-fuzzer-on-log4shell-bug-in-open-source-software/) and will [likely lurk in enterprise systems for years](https://www.zdnet.com/article/log4j-flaw-this-new-threat-is-going-to-affect-cybersecurity-for-a-long-time/) despite major efforts from [the US government](https://www.zdnet.com/article/cisa-orders-federal-agencies-to-mitigate-log4j-vulnerabilities-in-emergency-directive/), big tech and [open-source contributors](https://www.zdnet.com/article/apache-releases-new-2-17-0-patch-for-log4j-to-solve-denial-of-service-vulnerability/) to address flaws in the original Log4J version 2 project, its implementation in major software products, and its deployment in hundreds of millions of enterprise applications, servers and internet-facing devices. 



---

### LOG4J FLAW COVERAGE – WHAT YOU NEED TO KNOW NOW

* **[Log4j flaw: Attackers are making thousands of attempts to exploit this severe vulnerability](https://www.zdnet.com/article/log4j-flaw-attackers-are-making-thousands-of-attempts-to-exploit-this-severe-vulnerability)**
* **[Security warning: New zero-day in the Log4j Java library is already being exploited](https://www.zdnet.com/article/security-warning-new-zero-day-in-the-log4j-java-library-is-already-being-exploited/)**
* **[Log4j RCE activity began on December 1 as botnets start using vulnerability](https://www.zdnet.com/article/log4j-rce-activity-began-on-december-1-as-botnets-start-using-vulnerability/)**



---

There are ongoing efforts via the Apache Foundation to patch the core Log4j project, as well as downstream efforts [by IBM, Cisco, Oracle, VMware](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/) and others to patch products containing vulnerable versions of the Log4j component. Google has also released tools to [prevent developers using vulnerable Log4j versions in new builds of open-source software](https://www.zdnet.com/article/google-unleashes-security-fuzzer-on-log4shell-bug-in-open-source-software/). And the US government has ordered all federal agencies [to patch or mitigate Log4Shell by Christmas](https://www.zdnet.com/article/cisa-orders-federal-agencies-to-mitigate-log4j-vulnerabilities-in-emergency-directive/).   

The urgency is justified. State-sponsored hackers have started scoping out the bug for potential future attacks, [according to Microsoft](https://www.zdnet.com/article/log4j-flaw-now-state-backed-hackers-are-using-bug-as-part-of-attacks-warns-microsoft/) and Google, while cyber criminals are figuring out how to profit from it. Meanwhile, [the Belgian Ministry of Defense confirmed an attack on its network using the Log4j bug](https://www.zdnet.com/article/belgian-defense-ministry-confirms-cyberattack-through-log4j-exploitation/).   

Key challenges NCSC outlines include organizations finding out what services use Log4j; identifying which of these services an organizations uses; and then finding out if these services are vulnerable. CISA has already required [all US federal agencies to enumerate any external-facing devices with Log4j installed](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/). That's no small task, especially given the number of [affected products from Cisco, IBM, Oracle and VMware](https://www.zdnet.com/article/vmware-patches-critical-non-log4j-flaw-as-ibm-cisco-release-log4j-fixes/). Because of the component's widespread use in other products, CISA estimates hundreds of millions of devices worldwide are exposed.

"How concerned should boards be?" NCSC asks. 






Very, unless a business can afford disruptions to its operations from ransomware. While Microsoft has [not found instances of the more dangerous human-operated ransomware](https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/#ransomware-update) using the vulnerability, it has [seen Iranian threat actors tooling up to use it for ransomware attacks](https://www.zdnet.com/article/log4j-flaw-now-state-backed-hackers-are-using-bug-as-part-of-attacks-warns-microsoft/). 

NCSC has posed 10 questions for boards worried about the flaw:

* Who is leading on our response?
* What is our plan?
* How will we know if we're being attacked and can we respond?
* What percentage visibility of our software/servers do we have?
* How are we addressing shadow IT/appliances?
* Do we know if key providers are covering themselves?
* Does anyone in our organisation develop Java code?
* How will people report issues they find to us?
* When did we last check our business continuity plans and crisis response?
* How are we preventing teams from burning out?

Boards should also consider Log4Shell's impact if the business needs to disclose where personal data was affected, as well as any costs linked to incident response and recovery, and damage to reputation. 

"Managing this risk requires strong leadership, with senior managers working in concert with technical teams to initially understand their organisation's exposure, and then to take appropriate actions."

NCSC says Log4Shell warrants organizations creating a "tiger team" of core staff, including a leader, to address the threat. Boards should also ask 'what's our plan?', and to understand how Log4j issues will be remedied. Boards should understand this will take weeks or months to remediate, not days.   

Boards should know how the company is prepared to respond to a Log4Shell attack if and when it happens, and whether the company can detect if such an attack were to take place. It stresses that boards should understand what visibility its teams have of vulnerable software and servers, including IT assets that are centrally managed and unmanaged.



---

### LOG4J FLAW COVERAGE - HOW TO KEEP YOUR COMPANY SAFE

* **[**Log4j zero-day flaw: What you need to know and how to protect yourself**](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/#link=%7B%22linkText%22:%22Log4j%20zero-day%20flaw:%20What%20you%20need%20to%20know%20and%20how%20to%20protect%20yourself%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)**
* **[**Security warning: New zero-day in the Log4j Java library is already being exploited**](https://www.zdnet.com/article/security-warning-new-zero-day-in-the-log4j-java-library-is-already-being-exploited/#link=%7B%22linkText%22:%22Security%20warning:%20New%20zero-day%20in%20the%20Log4j%20Java%20library%20is%20already%20being%20exploited%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/security-warning-new-zero-day-in-the-log4j-java-library-is-already-being-exploited/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)**
* **[**Log4j flaw could be a problem for industrial networks 'for years to come'**](https://www.zdnet.com/article/log4j-flaw-could-be-a-problem-for-industrial-networks-for-years-to-come/#link=%7B%22linkText%22:%22Log4j%20flaw%20could%20be%20a%20problem%20for%20industrial%20networks%20'for%20years%20to%20come'%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/log4j-flaw-could-be-a-problem-for-industrial-networks-for-years-to-come/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)**



---

The software supply chain is another key consideration. NSCS recommends organizations have an "open and honest conversation" with software-as-a-service suppliers that may also be trying to get a grip on which of their products are affected. 

Java is a [hugely popular programming language](https://www.zdnet.com/article/programming-languages-java-founder-james-gosling-reveals-more-on-java-and-android/) in enterprise IT that's [used by an estimated 12 million developers worldwide](https://www.zdnet.com/article/oracles-java-15-new-features-aim-to-keep-millions-away-from-languages-like-rust-kotlin/). 

"Java developers may have legitimately used Log4j, so it's important to ensure that any software written is not vulnerable," NCSC notes. As it's [previously noted](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/), Log4j version 2 ships with Log4j version 2 (Log4j2) popular Apache frameworks including Struts2, Solr, Druid, Flink, and Swift.   

Finally, after two years of [supporting remote work during the pandemic](https://www.zdnet.com/article/cybersecurity-teams-are-struggling-with-burnout-but-the-attacks-keep-coming/), a year of [professional ransomware attacks](https://www.zdnet.com/article/updated-kaseya-ransomware-attack-faq-what-we-know-now/) and state-sponsored attacks on the [software supply chain](https://www.zdnet.com/article/microsoft-solarwinds-attack-took-more-than-1000-engineers-to-create/) and of[the critical Exchange Server zero-day vulnerabilities](https://www.zdnet.com/article/microsoft-exchange-server-attacks-theyre-being-hacked-faster-than-we-can-count-says-security-company/), NCSC is warning that some cybersecurity teams could suffer burnout during Log4Shell remediation. This is a board-level concern.

"Remediating this issue is likely to take weeks, or months for larger organisations. The combination of an ever evolving situation (and the potential for severe impacts) can lead to burnout in defenders, if they're not supported by leadership," NSCS stressed.   





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Entertainment]]

#### Location:
[[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Log4shell]] [[Ncsc]] [[Zero-day]] [[Ransomware]] [[Teams]] [[ZDNet]]

