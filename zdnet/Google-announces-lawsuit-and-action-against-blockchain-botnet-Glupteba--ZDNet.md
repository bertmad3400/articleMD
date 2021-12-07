# Google announces lawsuit and action against blockchain botnet Glupteba | ZDNet
### Google said the botnet currently involves approximately one million compromised Windows devices worldwide, and at times, grows at a rate of thousands of new devices per day.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/google-announces-lawsuit-and-action-against-blockchain-botnet-glupteba/
+ Date: 2021-12-07 21:15:10
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/a798533df2262a62725f5e88e831d004cbb8d691/2018/12/11/90a6a122-3561-4f9f-8bf9-56368fe81a5d/istock-675079800.jpg?width=770&height=578&fit=crop&auto=webp)

Google announced this morning that it disrupted the command and control infrastructure of Russia-based Glupteba, a blockchain-backed botnet being used to target Windows machines. 

Google vice president of security Royal Hansen and general counsel Halimah DeLaine Prado [wrote in a blog post](https://blog.google/technology/safety-security/new-action-combat-cyber-crime/) on Tuesday that the company's Threat Analysis Group [has been tracking Glupteba](https://blog.google/threat-analysis-group/disrupting-glupteba-operation/) for months and decided to take technical actions against the group as well as legal ones. 

Google [filed a lawsuit](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/1_Complaint.pdf) against the blockchain-enabled botnet -- litigation they called the first of its kind -- hoping to "create legal liability for the botnet operators, and help deter future activity."

"After a thorough investigation, we determined that the Glupteba botnet currently involves approximately one million compromised Windows devices worldwide, and at times, grows at a rate of thousands of new devices per day," the two wrote. 

"Glupteba is notorious for stealing users' credentials and data, mining cryptocurrencies on infected hosts, and setting up proxies to funnel other people's internet traffic through infected machines and routers."

Google noted that while they were able to disrupt key Glupteba command and control infrastructure, the actions may prove to be temporary considering the group's "sophisticated architecture and the recent actions that its organizers have taken to maintain the botnet, scale its operations, and conduct widespread criminal activity."

They believe the legal action will help make it harder for the group to take advantage of other devices. The lawsuit names Dmitry Starovikov and Alexander Filippov but notes that other unknown actors are involved. 






The lawsuit was filed in the Southern District of New York and the two are being sued for computer fraud and abuse, trademark infringement, and more. Google also filed for a temporary restraining order, an attempt to "create real legal liability for the operators."

But Google was also honest about the fact that the group's use of blockchain technology made the botnet resilient. They also noted that more cybercrime organizations are taking advantage of blockchain technology, which allows botnets to recover more quickly because of their decentralized nature. 

Shane Huntley and Luca Nagy, members of Google's Threat Analysis Group, explained in a blog post that Glupteba is known to steal user credentials and cookies, mine cryptocurrencies on infected hosts, deploy and operate proxy components targeting Windows systems and IoT devices. 

"TAG has observed the botnet targeting victims worldwide, including the US, India, Brazil, Vietnam, and Southeast Asia. The Glupteba malware family is primarily distributed through pay per install (PPI) networks and via traffic purchased from traffic distribution systems (TDS)," the two wrote. 

"For a period of time, we observed thousands of instances of malicious Glupteba downloads per day. The following image shows a webpage mimicking a software crack download which delivers a variant of Glupteba to users instead of the promised software."

The team and others at Google terminated around 63 million Google Docs observed to have distributed Glupteba, 1,183 Google Accounts, 908 Cloud Projects, and 870 Google Ads accounts associated with Glupteba distribution. About 3.5 million users were warned before downloading a malicious file through Google Safe Browsing warnings, according to Huntley and Nagy. 

They noted that they also worked with CloudFlare on the disruption efforts. As part of their investigation, Google used Chainalysis products and investigative services to investigate the botnet. 

Erin Plante, Chainalysis senior director of investigative services, told ZDNet that the botnet has two main cryptocurrency nexuses: Cryptojacking and a previously unknown tactic used to evade shutdown. 

Plante explained that Glupteba's operators used the machines they compromised for several criminal schemes, including utilizing their computing power to mine cryptocurrency. 

According to Plante, Glupteba also used the Bitcoin blockchain to encode updated command-and-control servers (C2) into the Op\_Returns of Bitcoin transactions, meaning that whenever one of Glupteba's C2 servers was shut down, it could simply scan the blockchain to find the new C2 server domain address, which was then hidden amongst the hundreds of thousands of daily Bitcoin transactions worldwide.

Most cybersecurity techniques involve disabling C2 server domains, making this Glupteba botnet tactic particularly difficult to contend with. Plante said this was the first known case of a botnet using this approach.

She added that the investigation revealed cryptocurrency transactions originating in [Federation Tower East](https://www.nytimes.com/2021/12/06/world/europe/ransomware-russia-bitcoin.html), a luxury office building in Moscow where many cryptocurrency businesses [known to launder criminal funds](https://www.bloomberg.com/news/articles/2021-11-03/bitcoin-money-laundering-happening-in-moscow-s-vostok-tower-experts-say) are headquartered. 

"Glupteba's blockchain-based method of avoiding the shutdown of its botnet represents a never-before-seen threat vector for cryptocurrencies. In the private sector, cryptocurrency businesses and financial institutions have thus far typically been the ones tackling cases involved in blockchain analysis, usually from an AML/CFT compliance perspective," Plante said.  

"But this case shows that cybersecurity teams at virtually any company that could be a target for cybercriminals must understand cryptocurrency and blockchain analysis in order to stay ahead of cybercriminals."





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.continent.name=Asia]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.city.name=Moscow]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Vietnam]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=Moscow]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Brazil]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Glupteba]] [[Google]] [[Botnet]] [[Blockchain]] [[Plante]] [[Windows]] [[Cryptocurrencies]] [[Bitcoin]] [[C2]] [[ZDNet]]

