# Updates released for multiple vulnerabilities found in 42 Gears' SureMDM products | ZDNet
### 42 Gears released an initial set of updates in November and then more earlier this month.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/multiple-vulnerabilities-found-in-42-gears-suremdm-products/
+ Date: 2022-01-31 22:39:56
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/0d8afb02ad14070f3546d9d260adab2cc0b69498/2021/12/06/e458798d-bb26-421f-8bcd-10b37bc4793d/train-cyber-security.jpg?width=770&height=578&fit=crop&auto=webp)

Multiple vulnerabilities have been discovered in the SureMDM device management solution sold by 42 Gears, prompting the company to release a series of updates to address the issues. 

Immersive Labs [published](https://www.immersivelabs.com/resources/blog/suremdm-vulnerability-could-lead-to-supply-chain-compromise/) a detailed breakdown of the vulnerabilities -- one of which is critical -- that affect SureMDM's Linux agent and the web console. Kevin Breen, director of cyber threat research at Immersive Labs, told *ZDNet* that the company says it has more than 5 million successful deployments worldwide and 18,000 customers. 

It is unclear how many use the products affected by the issues they discovered, but Breen said anyone using the Linux version listed in the post was vulnerable to those vulnerabilities. Anyone who used the web console was also vulnerable until December. 

"The more concerning set of vulnerabilities were the ones affecting the web console. These vulnerabilities could have allowed an attacker to gain code execution over individual devices, desktops or servers using the SureMDM web dashboard. By chaining the vulnerabilities affecting the web console together, an attacker could disable security tools and install malware or other malicious code onto every Linux, MacOS or Android device with SureMDM installed. An attacker does not need to know customer details to achieve this or even have an account on SureMDM," Breen explained.

"Once the attacker has sent the exploit to every customer account, they would simply need to wait for the first user to log into the SureMDM web console for the payload to be executed.  Upon login, the web application would automatically start the infected jobs that would affect every managed device in the organization."

Breen added that the second set of vulnerabilities affecting hosts running the Linux Agent for SureMDM would have allowed attackers to gain remote code execution on hosts as the root user. The issue "could also be exploited with local access to the affected hosts in order to escalate privileges from standard to root user," Breen noted. 

42 Gears released updates in November and January after working with Immersive Labs on the issue since July 2021. Immersive Labs noted that the company released multiple updates throughout the summer before finally addressing the vulnerabilities they found.






Casey Bisson, head of product growth at BluBracket, said the vulnerabilities are a big deal because individually, they are all problematic, but collectively they constitute a very serious risk for users. 

"Additionally, the workflow that led to a team building and shipping an app with so many vulnerabilities is particularly worrisome, even if we do not yet know how widespread the impact of these vulnerabilities is. Vulnerabilities like these are the unfortunate byproduct of the speed with which software is developed and shipped," Bisson said. 

"It's easy to criticize each of them as obvious or easy to avoid with good engineering, but the reality is that many of these types of vulnerabilities are fairly common. Organizations have no idea what risks they have in their code because they don't scan for them. There is a systemic breakdown of processes and the application of key technologies that are allowing these vulnerabilities to get to market. 

Vulcan Cyber engineer Mike Parkin noted that the series of issues discovered highlights the fact that vulnerabilities are often found in clusters rather than as a single stand-alone problem. 

That researchers found new problems as the developer fixed the ones that had been reported is something threat actors also do, Parkin said. 

"The timeline is notable for the back and forth between the research team and the vendor, how long it took to get fixes in place, and how new vulnerabilities came to light during the process," Parkin told ZDNet. 

Bugcrowd founder Casey Ellis took a more positive view of the situation, noting the amount of cooperation and collaboration in the timeline provided by Immersive Labs. 

The timeline and associated narrative demonstrates openness from 42 Gears in responding to external security feedback as well as highly organized and professional conduct from Immersive Labs to ensure their research -- and the subsequent protection of the users of 42 Gears -- was as complete and conducted in as safe a manner as possible, Ellis explained. 

"42 Gears is used widely enough to attract the attention of Immersive Labs, which is the data point which is most relevant here. These vulnerabilities look to be fairly impactful, but the thing that is striking to me about these issues is the amount of cooperation and collaboration in the timeline," Ellis said. 

"Ideally, software would be perfect -- but we know this isn't always the case. After all, humans are responsible for writing it." 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=CHOPSTICK]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Suremdm]] [[Linux]] [[Breen]] [[Timeline]] [[Ellis]] [[ZDNet]]

