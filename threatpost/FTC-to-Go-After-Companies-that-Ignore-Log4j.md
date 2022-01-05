# FTC to Go After Companies that Ignore Log4j
### Companies that fail to protect secure consumer data from Log4J attacks are at risk of facing Equifax-esque legal action and fines, the FTC warned.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177368
+ Date: 2022-01-05T19:00:03+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/05121242/gavel-scaled-e1641402780877.jpg)

The Federal Trade Commission (FTC) will muster its legal muscle to pursue companies and vendors that fail to protect consumer data from the risks of the [Log4j](https://threatpost.com/microsoft-rampant-log4j-exploits-testing/177358/) vulnerabilities, it [warned](https://www.ftc.gov/news-events/blogs/techftc/2022/01/ftc-warns-companies-remediate-log4j-security-vulnerability) on Tuesday.


“The FTC intends to use its full legal authority to pursue companies that fail to take reasonable steps to protect consumer data from exposure as a result of Log4j, or similar known vulnerabilities in the future,” according to the warning.


Those companies that bungle consumer data, leaving vulnerabilities unpatched and thus opening the door to exploits and the resulting possible “loss or breach of personal information, financial loss, and other irreversible harms,” are risking consequences tied to weighty laws that have resulted in fat fines, the FTC said.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


It mentioned, among others, the [Federal Trade Commission Act](https://www.ftc.gov/enforcement/statutes/federal-trade-commission-act) and the [Gramm-Leach-Bliley Act](https://threatpost.com/privacy-regulation-could-be-a-test-for-states-rights/138303/). The FTC Act, the commission’s primary statute, enables it to seek monetary redress and other relief for conduct injurious to consumers. [Gramm-Leach-Bliley](https://www.ftc.gov/tips-advice/business-center/privacy-and-security/gramm-leach-bliley-act) requires financial institutions to safeguard sensitive data.


“ It is critical that companies and their vendors relying on Log4j act now, in order to reduce the likelihood of harm to consumers, and to avoid FTC legal action,” the FTC urged.


The FTC means it: Its warning included a reference to the complaints against Equifax, which agreed to pay $700 million to settle actions by the FTC, the Consumer Financial Protection Bureau, and all fifty states over its infamous [2017 data leak](https://threatpost.com/equifax-says-breach-affects-143-million-americans/127880/). (Consumers’ reaction at the time: [Make it hurt more](https://threatpost.com/200k-sign-petition-against-equifax-data-breach-settlement/148560/).)


According to the complaint in Equifax, its  failure to patch a known vulnerability “irreversibly exposed the personal information of 147 million consumers.” Expect more of the same if your company fails to protect consumer data from exposure as a result of Log4j or whatever similar, known vulnerabilities crop up, it said.


The FTC advised companies to use [guidance](https://www.cisa.gov/uscert/apache-log4j-vulnerability-guidance) from the Cybersecurity and Infrastructure Security Agency (CISA) to check if they’re using Apache’s Log4j logging library, which is at the heart of the cluster of vulnerabilities known as [Log4Shell](https://threatpost.com/zero-day-in-ubiquitous-apache-log4j-tool-under-active-attack/176937/).


Companies that find that they are using Log4j should do the following, CISA recommended:


* Update your Log4j software package to the [most current version](https://logging.apache.org/log4j/2.x/security.html).
* Consult [CISA guidance](https://www.cisa.gov/uscert/apache-log4j-vulnerability-guidance) to mitigate this vulnerability.
* Ensure remedial steps are taken to ensure that your company’s practices do not violate the law. Failure to identify and patch instances of this software may violate [the FTC Act](https://www.ftc.gov/enforcement/statutes/federal-trade-commission-act).
* Distribute this information to any relevant third-party subsidiaries that sell products or services to consumers who may be vulnerable.


On Dec. 17, CISA issued an [emergency directive](https://www.cisa.gov/uscert/ncas/current-activity/2021/12/17/cisa-issues-ed-22-02-directing-federal-agencies-mitigate-apache) mandating federal civilian departments and agencies to immediately patch their internet-facing systems for the Log4j vulnerabilities by Thursday, Dec. 23. Federal agencies were given five more days – until Dec. 28 – to report Log4Shell-affected products, including vendor and app names and versions, along with what actions have been taken – e.g. updated, mitigated, removed from agency network – to block exploitation attempts.


CISA provides a [dedicated page](https://www.cisa.gov/uscert/apache-log4j-vulnerability-guidance) for the Log4Shell flaws with patching information and has released a [Log4j scanner](https://twitter.com/cisagov/status/1473401212468932609?s=12) to hunt down potentially vulnerable web services.


The Log4j Fire Rages Unabated
-----------------------------


The initial flaw – [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) – was discovered on Dec. 9 and came under attack within hours. As of Dec. 15, more than 1.8 million attacks, against [half of all corporate networks](https://threatpost.com/log4j-attacks-state-actors-worm/177088/), using at least 70 distinct malware families, had already been launched to exploit what became a trio of bugs:


1. The Log4Shell remote-code execution (RCE) bug that spawned [even nastier mutations](https://threatpost.com/apache-log4j-log4shell-mutations/176962/) and which led to …
2. The [potential for denial-of-service](https://threatpost.com/apache-patch-log4shell-log4j-dos-attacks/177064/) (DoS) in Apache’s initial patch. Plus, there was …
3. [A third bug](https://threatpost.com/third-log4j-bug-dos-apache-patch/177159/), a DoS flaw similar to Log4Shell in that it also affected the logging library. It differed in that it concerned Context Map lookups, not the Java Naming and Directory Interface (JNDI) lookups to an LDAP server involved in CVE-2021-44228: lookups that allow attackers to execute any code that’s returned in the Log4Shell vulnerability.


At this point, the Conti ransomware gang has had a [full attack chain](https://threatpost.com/conti-ransomware-gang-has-full-log4shell-attack-chain/177173/) in place for weeks.


In a Monday update, Microsoft said that the end of December [brought no relief](https://threatpost.com/microsoft-rampant-log4j-exploits-testing/177358/): The company observed state-sponsored and cyber-criminal attackers probing systems for the Log4Shell flaw through month’s end. “Microsoft has observed attackers using many of the same inventory techniques to locate targets. Sophisticated adversaries (like nation-state actors) and commodity attackers alike have been observed taking advantage of these vulnerabilities. There is high potential for the expanded use of the vulnerabilities,” Microsoft security researchers warned.


“Exploitation attempts and testing have remained high during the last weeks of December. We have observed many existing attackers adding exploits of these vulnerabilities in their existing malware kits and tactics, from coin miners to hands-on-keyboard attacks,” the researchers said.


Hunting Down Log4j
------------------


One of the most challenging aspects of responding to the log4j vulnerability is simply identifying the devices in an organization where log4j is used. The word “ubiquitous” has applied since the get-go: “Since it is a cross-platform, widely used software library, there is incredible diversity in where and how it is deployed: it can be an application package installed by itself, bundled with another application package as just another file on disk or embedded in another application with no visible artifact,” J.J. Guy, co-founder and CEO, Sevco Security, told Threatpost on Wednesday.


“Even worse, it is used in everything from cloud-managed services to server applications and even fixed-function, embedded devices. That internet-connected toaster is very likely vulnerable to log4shell.”


We’re just in the middle of the triage phase now, Guy said, where basic tools like systems management or software management tools to check for the file on disk can provide initial triage.


One question: What’s the inventory of equipment that still needs to be triaged?


“For organizational leaders, such as the board, CEO, CIO or CISO, to have confidence in those triage results requires they report not only the machines that have been triaged but also how many are pending triage,” Guy remarked. “Reporting the ‘pending triage’ statistic requires a complete asset inventory, including which machines have been successfully triaged.”


It called this “one of the larger hidden challenges” in every organization’s response, given that so few have a comprehensive asset inventory, “despite the fact it has been a top requirement in every security compliance program for decades.”


[*Image courtesy of Quince Media.*](https://commons.wikimedia.org/wiki/File:3D_illustration_image_of_a_gavel_-_auction_hammer_-_free_to_use_in_your_projects_07.jpg) [*Licensing details*](https://creativecommons.org/licenses/by-sa/4.0/)*.*  

***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Expand]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=RTM]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.city.name=Quito]] [[victim.country.name=Ecuador]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Log4j]] [[Ftc]] [[Log4shell]] [[Cisa]] [[ThreatPost]]
#### CVE's
[[CVE-2021-44228]]

