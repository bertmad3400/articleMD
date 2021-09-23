# Ransomware attacks on grain coops may just be the start of ag sector security woes
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/ransomware-attacks-on-grain-coops-may-just-be-the-start-of-ag-sector-security-woes/)
+ Date: September 23, 2021
+ Author: Andrea Peterson


## Article:
![Ransomware attacks on grain coops may just be the start of ag sector security woes](https://therecord.media/wp-content/uploads/2021/09/chris-ensminger-yJDZTDeHeG8-unsplash-1.jpg)

Recent ransomware attacks against U.S. grain cooperatives and a farm data platform are raising the specter of food supply chain disruptions while highlighting the economic and physical security risks of reliance on increasingly sophisticated systems to feed the world. 


America’s farms [have led the way](https://www.washingtonpost.com/news/the-switch/wp/2015/06/22/google-didnt-lead-the-self-driving-vehicle-revolution-john-deere-did/) in real-world applications of innovations, from self-driving vehicles to satellite imagery, so much so that many farmers are already living in the future: They rely on farm platforms that can connect information from their tractors, drones, satellites, soil samples, and public sources to map out plans for planting, which herbicides or pesticides to use, and harvests. 


“Everything is connected,” explained Auburn University Professor Robert Norton, who studies food safety.


But doing this “precision agriculture” doesn’t just improve yields, it can also expose farms’ digital attack surfaces while creating a treasure trove of valuable data. And those systems and data are increasingly being targeted, including in two ransomware attacks this week, one targeting the Minnesota-based Crystal Valley Coop and another attacking NEW Cooperative in Iowa and its associated farm data service provider and platform SOILMAP.


“CISA and FBI are in close contact with NEW Cooperative and have offered assistance in supporting the company’s response and recovery,” a Cybersecurity and Infrastructure Security Agency spokesperson said in a statement to The Record. “The company is engaging proactively with CISA as the investigation progresses,” according to the statement, which described ransomware as “a longstanding global epidemic.”


The attackers may be asking for money now, but the data potentially compromised is also valuable economic and strategic intelligence. And researchers warn that the integration of insecure farm platforms with the guidance systems of farm equipment including tractors and harvesters—steel goliaths that are now high tech and extremely high-priced, with fully decked-out models easily costing hundreds of thousands of dollars—presents a physical and national security threat.


“In some ways, we are lucky that the current focus is simply extortion: at some point, a hacker is going to act maliciously to misread temperature gauges, DDoS a smart tractor fleet, or overprescribe/underprescribe fertilizers/chemicals,” Rian Wanstreet, a PhD candidate at the University of Washington and Affiliate of Harvard’s Berkman Klein Center for Internet and Society, told The Record. 


“Such disruptions would be catastrophic,” said Wanstreet, who studies agriculture and technology. 


Right now, there are usually still manual failsafes in processes that might prevent such attacks from causing major damage, according to Professor Bradley Miller, who teaches agronomy and leads the Geospatial Laboratory for Soil Informatics at Iowa State University. For example, self-driving tractors still have humans in the cab who can take over, he said. 


But there have already been attacks on the food supply chain, including the ransomware infection that affected the U.S. plants of the world’s largest meat processor JBS in May. But the disruption was minimal in that case, in part because JBS paid the [$11 million ransom](https://www.wsj.com/articles/jbs-paid-11-million-to-resolve-ransomware-attack-11623280781) almost immediately and lost less than a day of operations. 


In a June 9 [statement](https://jbsfoodsgroup.com/articles/jbs-usa-cyberattack-media-statement-june-9), the head of their U.S. operations described making the ransom payment as a “very difficult decision” for the company and himself personally, but one that “had to be made to prevent any potential risk for our customers.”


The infosec community, too, has raised the alarm—including a group of researchers led by pseudonymous hacker Sick Codes who presented [research](https://sick.codes/being-root-on-two-agriculture-companies-in-good-faith-maxing-out-the-john-deere-operations-center-worldwide-and-case-industrial-in-brazil/) at DEF CON this summer showing how vulnerabilities in connected farm equipment could be used to sow agricultural havoc, like effectively poisoning crops by tricking equipment into spraying them with the wrong mixture of chemicals.


Ransomware attacks in Iowa and Minnesota
----------------------------------------


Vulnerabilities left the agricultural sector exposed again this week as ransomware attacks hit agricultural cooperatives in Iowa and Minnesota. 


Malware samples analyzed by Recorded Future’s Insikt Group show the BlackMatter ransomware group infiltrated the systems of Iowa-based NEW Cooperative, Inc and its associated precision agriculture firm SOILMAP. The attack on the business, which has more than 60 outposts, was first publicly reported by [Bloomberg](https://www.bloomberg.com/news/articles/2021-09-20/iowa-based-grain-cooperative-hit-with-ransomware-attack).


Chat logs within the sample dated September 19 appear to show the company engaged in active negotiation with the ransomware gang for days as the gang requested a bitcoin ransom worth $5.9 million. 


The victim argues for mercy, citing itself as a major part of the U.S. food supply chain, and thus, critical infrastructure. The company also says it will be required to disclose the incident to regulators, including CISA soon:



> Your website says you do not attack critical infrastructure. We are critical infrastructure – we intertwined with the food supply chain in the US. If we are not able to recover very shortly, there is going to be very very public disruption to the grain, pork and chicken supply chain. About 40% of grain production runs on our software, and 11 million animals feed schedules rely on us. This will break the supply chain very shortly, and we will have to report this to our regulators and likely the public if this disruption continues. I assume you have thought that through? CISA is going to be demanding answers from us within the next 12 hours or so and we are going to have to tell them exactly what has happened and why the food supply chain is disrupted.
> 
> 


The BlackMatter group’s website does include a promise to avoid attacking “Critical Infrastructure,” although the list of areas they won’t attack on their dark web homepage does not specifically include agriculture. 


![](https://www-therecord.recfut.com/wp-content/uploads/2021/09/ag2.png)IMAGE: RECORDED FUTURE
Agriculture is among the [critical infrastructure areas](https://www.cisa.gov/critical-infrastructure-sectors) designated by CISA that the Biden administration has warned attackers to avoid. But the BlackMatter group representative in the chat appears to disagree with New Cooperative’s claim of the designation. 


The apparent representatives of New Cooperative tell the attackers the impacts of this hack’s real world effects “will likely be much worse” than the Colonial Pipeline attack and the situation, including regulators response, is already out of their hands “given the disruption this has already caused.” 


The BlackMatter representative later threatens to double the ransom the New Cooperative persists with its negotiation strategy. 


Chat logs from later days show an [apparent breakdown of communications](https://twitter.com/ddd1ms/status/1440766066871848966), then trolling. However, it’s not clear the “victim” in those logs actually represents NEW Cooperative. “Since the malware sample is known among researchers, it’s possible that the session was hijacked by unknown entities,” according to Recorded Future Expert Analyst Dmitry Smilyanets.


Meanwhile the clock is still ticking down towards the ransomware gang’s deadline.


![](https://www-therecord.recfut.com/wp-content/uploads/2021/09/ag1-e1632410737942.png)IMAGE: RECORDED FUTURE
A private blog post accessible through the malware sample shows that the attackers claim to have 1000GB of the company’s data, which it threatens will leak online on September 25th if the ransom goes unpaid. The gang lists sensitive business and personnel information, along with all of the SOILMAP source code and information about associated “Android & iOS apps with sources.”


According to SOILMAP’s website, the system integrates with the APIs of major agricultural systems, including [John Deere.](https://www.soilmap.com/2018/08/27/soilmap-and-my-john-deere-announce-the-completion-of-api-integration/)


In a statement to The Record, NEW Cooperative confirmed they are responding to a cybersecurity incident and had “proactively taken our systems offline to contain the threat,” which it said was “successfully contained.”


NEW Cooperative wrote that it “quickly notified law enforcement” and is working to remediate its systems. It also asked customers for patience. 


As of Thursday morning, SOILMAP services still appeared down on the company’s web site. 


The future of food security
---------------------------


A [Private Industry Notification](https://www.documentcloud.org/documents/21053957-fbi-tlp-white-pin-cyber-criminal-actors-targeting-food-agriculture-sector-ansomware-attacks-9-1-21) distributed by the FBI [at the beginning of the September](https://therecord.media/us-farm-loses-9-million-in-the-aftermath-of-a-ransomware-attack/) warned that ransomware was a threat to businesses across the food and agriculture sector “from small farms to large producers, processors and manufacturers, and markets and restaurants.” It also highlighted how ransomware attacks had already affected food supplies, including the JBS attack, plus an attack that cost a U.S. farm $9 million in lost operations as well as another incident where a U.S. bakery had to shut down operations for a week.


And just a day after the NEW Cooperative compromise was confirmed, The Free Press [reported](https://www.mankatofreepress.com/news/local_news/crystal-valley-co-op-hit-by-cyberattack/article_ee0a6786-1b24-11ec-a41a-1b3c14d1d303.html) about the compromise at Crystal Valley Co-op in Minnesota. 


![](https://www-therecord.recfut.com/wp-content/uploads/2021/09/Screen-Shot-2021-09-23-at-11.29.57-AM-1024x490.png)IMAGE: CRYSTAL VALLEY CO-OP
High-tech security concerns are on the rise among farmers—some are [even hacking into their own tractors](https://www.vice.com/en/article/xykkkd/why-american-farmers-are-hacking-their-tractors-with-ukrainian-firmware) to get around manufacturer restrictions. And there are some community resources to help those in the sector collectively respond to attacks. Although there isn’t a specific information and sharing group (ISAC) for the Food and Agriculture, several big name players in the industry are part of the broader IT-SAC, which has a subgroup focused on the sector. 


“The cyber threat in general is too complex and actors are too sophisticated for companies to go it alone,” IT-ISAC executive director Scott C. Algeier told The Record. “The food and agriculture companies we engage with are highly informed about the threats facing their enterprises and are actively engaging with each other to manage them,” he said. 


But security  across the sector is still catching up, according to Sick Codes. He’s spoken to dozens of agriculture CEOs about his research in the sector, but most don’t seem to grasp the gravity of the problem, he told The Record. 


“Many of them have gone ‘oh wow’ and then kind of moved on, but don’t really understand there are a lot of access points in their systems,” he said. 


Meanwhile some, including Norton, warn that America’s farms and food processing systems have long been on the radar of state-level cyber threat actors. Some of their activity is more classic economic espionage seeking information to boost domestic output, but other activity looks more like probing designed to map our domestic critical infrastructure systems. 


“The larger question is why? Is it going to be used sometime in the future? If so, how?” Norton asked.





#### Tags:
[[ransomware]] [[U.S.]] [[Record.]] [[“The]] [[CISA]] [[BlackMatter]] [[company’s]] [[said.]] [[JBS]] [[IMAGE:]] [[The Record]]
