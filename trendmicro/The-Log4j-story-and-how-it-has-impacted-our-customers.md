# The Log4j story, and how it has impacted our customers
### Read about the Log4j story, an analysis of the impact and what to do next.

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/21/l/the-log4j-story-and-how-it-has-impacted-our-customers.html
+ Date: 2021-12-22
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/the-log4j-story-and-how-it-has-impacted-our-customers/microsoftteams-image.png)





The security research community had been expecting something like this to come along for a while. So it was with a sense of dread that we read news of a newly discovered CVSS 10.0 vulnerability in early December. The impact is already being felt around the globe as threat actors scramble to exploit the bug before defenders can apply their patches. It is a story that could take months [or even years to play out](https://www.infosecurity-magazine.com/news/experts-log4j-bug-could-be/).


The latest Trend Micro customer data reveals just how significant the global and vertical reach of Log4Shell is, and the huge range of applications it impacts. That’s why we continue to research potential new vectors and Log4j vulnerabilities, and to help organizations better understand where they may be exposed.


What happened?


Log4j is a popular Java-based logging tool used in platforms as diverse as Minecraft and Elasticsearch. A [high severity vulnerability](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228) dubbed “Log4Shell” was patched by the open source Apache community in early December. However, exploits subsequently created for it have already been used by threat actors to launch ransomware, mine illegally for virtual currency, steal data and much more. Why is it so dangerous?


1. Log4j is near-ubiquitous in modern enterprises, in both third-party and home-grown applications
2. Due to Java dependencies, it is not always easy to find instances of Log4j running, in order to patch them
3. There are multiple attack vectors depending on the application in question. In the case of Minecraft, exploitation was [reportedly as simple](https://twitter.com/MalwareTechBlog/status/1469289471463944198) as copying a string into a chat box
4. The vulnerability can lead to remote code execution, allowing attackers to install malicious code on an affected machine to launch a range of attacks


Charting the spread of Log4j


New Trend Micro data highlights exactly how widespread the threat is. Although just 7% of our customers were impacted, they were dispersed across Europe (26%), the Americas (33%), Japan (16%) and AMEA (25%). The US dominated country-by-country (5,069) followed by Japan (4,223). The threat is also presence across verticals. The top three for Trend Micro customers were government (1,950), retail (1,537) and manufacturing (1,507).


As mentioned, Log4j is an incredibly popular utility for Java-based logging. In our breakdown we found it most common on the desktop in StandAlone Doc Browser, 724Access, VMware, and Minecraft. On the server side, it was Tableau, PowerChute Business Edition, spectrumcontrol and Tomcat.


However, that’s still not the whole story. We also observed some apps more frequently impacted in specific regions. SIOS.QuickAgent2 topped the list in Japan, for example. When it came to verticals, Tableau and VMware were most commonly affected in government, retail and manufacturing. But third place went to ArcGIS in government, SASEnvironmentManager in retail and Informatica Cloud Security Agent in manufacturing. Knowing where to find Log4j is crucial to mitigating the risk of exploitation.


  

A new DoS threat


The story has since taken yet another turn, thanks in part to the work of Trend Micro researcher Guy Lederfein and Trend Micro’s Zero Day Initiative (ZDI). He helped discover [a new Denial of Service (DoS)](https://www.zerodayinitiative.com/blog/2021/12/17/cve-2021-45105-denial-of-service-via-uncontrolled-recursion-in-log4j-strsubstitutor) vulnerability in Log4j which has subsequently been patched.


As the world’s largest vendor agnostic bug bounty program, the ZDI’s mission has never been more important. Incentivizing researchers from across the globe to find new vulnerabilities before the bad guys do is of critical importance in a world where exploits of popular programs like Log4j can result in such widespread damage so quickly.


In the meantime, Trend Micro stands ready to help customers [with a free assessment tool](https://resources.trendmicro.com/Log4Shell-Vulnerability-Assessment.html?_ga=2.107316933.670848857.1640086353-1896003459.1562355749) designed to root out instances of unpatched Log4j across your IT environment. Check out all the latest info on the [threat here](/en_us/apache-log4j-vulnerability.html).









## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Manufacturing]] [[victim.industry.name=Retail]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Japan]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.city.name=Quito]] [[victim.country.name=Ecuador]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Log4j]] [[Minecraft]] [[Trend Micro]]

