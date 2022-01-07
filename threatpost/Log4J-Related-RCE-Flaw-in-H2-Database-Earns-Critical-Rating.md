# Log4J-Related RCE Flaw in H2 Database Earns Critical Rating
### Critical flaw in the H2 open-source Java SQL database are similar to the Log4J vulnerability, but do not pose a widespread threat.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177448
+ Date: 2022-01-07T15:12:26+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/05/19095410/red-bug-1200-e1621432463155.jpeg)

Researchers discovered a bug related to the Log4J logging library vulnerability, which in this case opens the door for an adversary to execute remote code on vulnerable systems. However, this flaw does not pose the same risk as the previously identified in Log4Shell, they said.


JFrog security discovered the flaw and rated critical in the context of the H2 Java database console, a popular open-source database, according to a Thursday [blog post](https://jfrog.com/blog/the-jndi-strikes-back-unauthenticated-rce-in-h2-database-console/) by researchers.


H2 is attractive to developers for its lightweight in-memory solution–which precludes the requirement for data to be stored on disk—and is used in web platforms such as [Spring Boot](https://spring.io/projects/spring-boot) and IoT platforms such as [ThingWorks](https://www.ptc.com/en/products/thingworx).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


However, the flaw ([CVE-2021-42392](https://nvd.nist.gov/vuln/detail/CVE-2021-42392)) is similar to Log4Shell. “[I]t should not be as widespread” due to a few conditions and factors, JFrog researchers Andrey Polkovnychenko and Shachar Menashe wrote in their post.


Log4Shell ([CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)) was tied to the Apache Log4j logging library in early December and immediately exploited by attackers. It [spawned](https://threatpost.com/apache-log4j-log4shell-mutations/176962/) 60 variants of the original exploit created for the flaw in a 24-hour period as well as [a faulty fix](https://threatpost.com/apache-patch-log4shell-log4j-dos-attacks/177064/) that could cause DoS attacks when it was first released.


How is the H2 Bug Similar to Log4J?
-----------------------------------


The root cause of the H2 flaw is based in JNDI remote class loading, making it similar to Log4Shell in that it allows several code paths in the H2 database framework pass unfiltered attacker-controlled URLs to the javax.naming.Context.lookup function. This allows for remote codebase loading, also known as Java code injection or remote code execution, researchers said.


“Specifically, the org.h2.util.JdbcUtils.getConnection method takes a driver class name and database URL as parameters,” they explained in the post. “If the driver’s class is assignable to the javax.naming.Context class, the method instantiates an object from it and calls its lookup method.”


**Reasons to Be Wary, but Not Panic**
-------------------------------------


However, unlike Log4Shell, the H2 flaw has a “direct” scope of impact, meaning that typically the server that processes the initial request—that is, the H2 console—will feel the direct brunt of the remote code execution (RCE) bug, researchers wrote in a post published Thursday.


“This is less severe compared to Log4Shell since the vulnerable servers should be easier to find,” researchers wrote.


Secondly, by default on vanilla distributions of the H2 database, the H2 console only listens to localhost connections, thus making the default setting safe, they noted.


“This is unlike Log4Shell which was exploitable in the default configuration of Log4j,” researchers wrote. Still, the H2 console can easily be modified to listen to remote connections as well, which would widen the risk, researchers added.


Indeed, this aspect of the execution of the flaw definitely lessens its severity in comparison to the Log4j issue, noted one security professional.


“Log4j was unique in that any number of attack-manipulated strings, from headers to URL paths, could result in exploitation of the victim depending on how the application was set up to utilize logging with Log4j,” Matthew Warner, CTO and co-founder at automated threat detection and response technology provider [Blumira](https://www.blumira.com/), wrote in an email to Threatpost. “In this case, the H2 database console must be purposefully exposed to the internet by changing the configuration.”


Thirdly, while many vendors may be running the H2 database, they may not run the H2 console with it, JFrog researchers said. There are other attack vectors that can exploit the H2 flaw; however, they are “context-dependent and less likely to be exposed to remote attackers,” researchers observed.


**Who Is At Risk?**
-------------------


If the H2 flaw doesn’t deserve the same alarm as Log4Shell, why is it worth noting, one may ask. The JFrog team said that it can be extremely critical and allow for unauthenticated RCE to those running an H2 console exposed to a local area network (LAN) or, even worse, a wide area network (WAN). Indeed, attacking the H2 console directly is the most severe attack vector, researchers said.


Blumira’s Warner said that according to open-source intelligence (OSINT), there are likely less than 100 servers on the internet impacted by the H2 flaw, “so only a very limited number of organizations” are directly affected, he said.


“This vulnerability is a good reminder that it is important to ensure that sensitive services are only internally exposed to mitigate potential future risks,” Warner added.


Still, JFrog researchers said that many developer tools rely on the H2 database and specifically expose the H2 console. This is worrying due to the “recent trend of supply chain attacks targeting developers, such as [malicious packages in popular repositories](https://jfrog.com/blog/malicious-npm-packages-are-after-your-discord-tokens-17-new-packages-disclosed/).”


These attacks emphasize “the importance of developer tools being made secure for all reasonable use cases,” researchers wrote, which is why they hope many H2-dependent tools will be safer after applying their recommended fix.


On that point, the JFrog team recommends that  all users of the H2 database to upgrade to [version 2.0.206](https://github.com/h2database/h2database/releases/tag/version-2.0.206), which fixes CVE-2021-42392 by limiting JNDI URLs to use the local java protocol only, denying any remote LDAP/RMI queries, researchers explained.


“This is similar to the fix applied in [Log4j 2.17.0](https://jfrog.com/cheat-sheet/log4j-log4shell-survival-guide/),” they wrote.


Even those not directly using the H2 console should update “due to the fact that other attack vectors exist, and their exploitability may be difficult to ascertain,” researchers added.


***Password** **Reset:** **[On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):** Fortify 2022 with a password-security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the new password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken. **[Register & stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)** – sponsored by Specops Software.*





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Paris]] [[victim.country.name=France]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[H2]] [[Log4shell]] [[Jfrog]] [[“this]] [[Log4j]] [[Threatpost]] [[ThreatPost]]
#### CVE's
[[CVE-2021-42392]] [[CVE-2021-44228]]

