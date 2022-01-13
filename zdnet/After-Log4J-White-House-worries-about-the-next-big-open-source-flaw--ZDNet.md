# After Log4J, White House worries about the next big open source flaw | ZDNet
### The White House is holding a meeting today with tech leaders to discuss Log4J and other potential flaws.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/after-log4j-white-house-worries-about-the-next-big-open-source-flaw/
+ Date: 2022-01-13 17:32:51
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/3251b64805aeed4353455ef0824fba6825101b64/2021/11/01/fd27d12f-c8be-4fb5-ba0f-d339b783c136/gettyimages-1236202461.jpg?width=770&height=578&fit=crop&auto=webp)

The White House is holding a meeting today with Apache, Google, Apple, Amazon and other major tech organizations to discuss software security and open source tools in the wake of the [Log4J vulnerability](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/) that has caused shockwaves throughout the world since it was discovered in December. 

White House National Security Advisor Jake Sullivan [asked](https://www.reuters.com/technology/white-house-national-security-adviser-asks-software-companies-discuss-2021-12-23/?fbclid=IwAR2UU-d4YIxQKHRH9BOSOAG64n67PoFUQbvZgScb1uba12_FdnwaNyXGNmU) for the meeting in December, noting in a letter to the companies that it was a "national security concern" for foundational open source software to be maintained by volunteers. 

The meeting, led by White House cybersecurity leader Anne Neuberger, will include officials from companies like IBM, Microsoft Corp, Meta, Linux and Oracle as well as government agencies like CISA, the Commerce Department and the Defense Department. 

Chris Inglis, National Cyber Director, [said](https://twitter.com/ncdinglis/status/1481649740563447808) on Thursday that the situation around Log4J "has highlighted the need to improve our software security and the transparency of our software supply chain." 

"Enjoying the discussion with White House National Security Council and leading open source project managers about how to bring coherence to federal efforts to increase software resilience," Inglis said. 

The Apache Software Foundation, which manages Log4J and is run by volunteers, [released](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=199530455) a [bevy of documents](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=199530004) ahead of the meeting explaining their stance and their efforts to shore up the vulnerability. Some of the documents offer a tacit defense of the organization's response to the crisis, calling Log4J "an unfortunate combination of independently designed features within the Java platform."

Apache noted that they have several hundred open source projects and oversee 227 million lines of code. 






During [a press conference this week](https://www.zdnet.com/article/cisa-director-we-have-not-seen-significant-intrusions-from-log4j/), CISA director Jen Easterly and CISA executive assistant director for cybersecurity Eric Goldstein told reporters that they have not seen any "high-profile breaches or attacks" related to the Log4J vulnerability outside of the [attack on the Belgian Defense Ministry](https://www.zdnet.com/article/belgian-defense-ministry-confirms-cyberattack-through-log4j-exploitation/).

"At this time, we have not seen the use of Log4Shell resulting in significant intrusions. This may be the case because sophisticated adversaries have already used this vulnerability to exploit targets and are just waiting to leverage their new access until network defenders are on a lower alert. Everybody remembers [the Equifax breach](https://www.zdnet.com/article/how-the-equifax-breach-breaks-down-by-the-numbers/) that was revealed in September of 2017 was a result of an open-source software vulnerability discovered in March of that year," Easterly said. 

"It may also be due in part to the urgent actions taken by defenders and many organizations to rapidly mitigate the most easily exploitable devices, such as those accessible directly from the internet," Easterly added. "We do expect Log4Shell to be used in intrusions well into the future." 

Later in the conversation, both Easterly and Goldstein spoke at length about larger concerns for what other open source projects may have vulnerabilities with dire knock-on effects like Log4J. 

Easterly said that as a result of Log4J, CISA is accelerating its efforts to create a "software bill of materials" (SBOM) and noted that they recently hired Allan Friedman, who previously led cybersecurity and SBOM efforts at the Commerce Department. Friedman is now working on coordinating SBOM efforts inside and outside the US government. 

Easterly and Goldstein also cited the White House meeting today as part of their effort to address open source security issues. 

"I think this vulnerability reflects the work that we have yet to do and I think that work will focus both on ensuring that organizations have visibility into libraries and components in their environment and in their software stacks as well as ensuring that we have the community understanding of the most prevalent and critical open source products and libraries that are used across critical infrastructure and across the government," Goldstein said. 

"We are prioritizing support assistance and transparency to the developers and maintainers of those specific libraries and components. We are taking a prioritized approach, recognizing the ubiquity of these components and that they are now so broadly utilized across technology environments. This vulnerability will catalyze further attention, focus and investment, which will manifest in better security."

Goldstein noted that even though they have not seen any significant attacks, there has been widespread scanning and exploitation of Log4Shell by cybercriminals who use it to install cryptomining software on victim computers or to capture victim computers for use in botnets.

Steve Povolny, head of advanced threat research for McAfee Enterprise, told ZDNet that there has [already been three](https://www.zdnet.com/article/second-log4j-vulnerability-found-apache-log4j-2-16-0-released/) [different iteration](https://www.zdnet.com/article/apache-releases-new-2-17-0-patch-for-log4j-to-solve-denial-of-service-vulnerability/) of the Log4J vulnerability, prompting concern about the wider issues with similar tools. While he does not expect any more iterations of the Log4J vulnerability, he referenced [recent research about JNDI issues](https://www.zdnet.com/article/jfrog-researchers-find-jndi-vulnerability-in-h2-database-consoles-similar-to-log4shell/) as an example of how widespread concern about Log4J led to other issues being discovered. 

"What you see here is a pattern going back 20 years which I call ambulance chasing and it's actually a very effective way to weed out similar vulnerabilities. It often happens with the major critical vulnerabilities, where somebody publishes exploit code and all of a sudden, the research industry finds the new target of interest because it's sexy and it's topical," he said. 

"But it turns out to be a great way to flush out similar types of vulnerabilities in either the same or tangentially similar project and products. You've got a lot of eyes on components like JNDI and the Apache framework that does logging."





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=RTM]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Mining]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Cisa]] [[Goldstein]] [[Cybersecurity]] [[Log4shell]] [[ZDNet]]

