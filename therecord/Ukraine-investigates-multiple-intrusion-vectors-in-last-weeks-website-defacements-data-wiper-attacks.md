# Ukraine investigates multiple intrusion vectors in last week's website defacements, data wiper attacks
### The Ukrainian government said on Monday that it is investigating multiple intrusion vectors that could have been used to carry out the cyber-attacks that hit its government agencies last week.

## Information:
+ Source: The Record
+ Link: https://therecord.media/ukraine-investigates-multiple-vectors-in-website-defacements-data-wiper-attacks/
+ Date: 2022-01-18T19:33:07+00:00
+ Author: Catalin Cimpanu


## Article:
![Article Image](https://therecord.media/wp-content/uploads/2022/01/Ukraine-kyiv-soldiers-military.jpg)

The Ukrainian government said on Monday that it is investigating multiple intrusion vectors that could have been used to carry out the cyber-attacks that hit its government agencies last week.


The attacks, which took place last Friday, included an attempt to [deface more than 70 Ukrainian government websites](https://therecord.media/hackers-deface-ukrainian-government-websites/) and [the deployment of a data-wiper](https://therecord.media/microsoft-data-wiping-malware-disguised-as-ransomware-targets-ukraine-again/) on some government systems, a wiper that was designed to corrupt files and look like the affected systems were hit with a ransomware attack.


On Monday, Ukrainian officials said the website defacements were also accompanied by data destruction attacks, suggesting for the first time that the two incidents are part of the same attack chain and not separate as initially thought.


The statements echo an independent investigation from cybersecurity reporter Kim Zetter, who described in her [Zero-Day newsletter](https://zetter.substack.com/p/what-we-know-and-dont-know-about) an attack where the threat actor used different entry points into government systems and defaced or wiped data depending on the level of access they had gained.


### Log4Shell?


On Monday, the [Ukrainian Cyber Police](https://www.cyberpolice.gov.ua/news/kiberpolicziya-derzhspeczzvyazku-ta-sbu-razom-iz-mizhnarodnymy-ekspertamy-vstanovlyuyut-dzherela-poxodzhennya-kiberatak-na-derzhavni-vebsajty-897/) and the [Ukrainian Security Service](https://ssu.gov.ua/novyny/sbu-narazi-vidnovleno-robotu-95-saitiv-shcho-postrazhdaly-vid-kiberataky-na-derzhavni-resursy) said they were tracking three potential intrusion vectors that attackers could have used to pull off last week’s attacks:


* The exploitation of a vulnerability in the October CMS platform, which the Ukrainian government had used for some of the defaced websites;
* The compromise of employee accounts at a private company that provided the Ukrainian government with managed IT services;
* The use of the Log4Shell vulnerability to gain access to some of the compromised systems.


The October CMS vulnerability referenced by the Cyber Police and SSU appears to be CVE-2021-32648, which [Ukraine’s CERT team](https://www.cvedetails.com/cve/CVE-2021-32648/) said it had identified as one of the primary suspects in some of the defaced websites.


But not all of the attacked government websites ran on October CMS, and the hackers appear to have tried to gain access to some of these other sites by compromising an employee at an IT company that managed some of the government’s websites.


The name of this company appears to be Kitsoft, a Kyiv-based software developer, which [confirmed on Facebook](https://www.facebook.com/story.php?story_fbid=4922505641201033&id=147727725345539) that its infrastructure was hit by a data wiper.


Kitsoft referenced itself as the unnamed private company in a blog post published on Sunday by Microsoft, a [blog post](https://blogs.microsoft.com/on-the-issues/2022/01/15/mstic-malware-cyberattacks-ukraine-government/) in which researchers analyzed the data-wiping malware and named one of the victims as an “IT firm that manages websites for public and private sector clients, including government agencies whose websites were recently defaced.”


As Zetter also concluded in her newsletter, some details about the attack still remain shrouded in mystery, such as who was behind the attack and the number of threat actors involved in the operation.


In addition, the government’s press release also throws a new wrench in the investigation as to what role the Log4Shell exploit also played in all of this. It is unclear if government agencies are merely referencing Log4Shell due to the fact that blaming attacks on this vulnerability seems to be an easy cop-out or if they have actual evidence that this bug was exploited against their systems.


### Early attribution to Russia


While neither Ukrainian Cyber Police nor the SSU attempted to attribute the attacks to any country just yet, a statement from the Ministry of Digital Transformation did [place the blame on Russian hackers](https://thedigital.gov.ua/news/rosiya-mae-namir-zniziti-doviru-do-vladi-feykami-pro-vrazlivist-kritichnoi-informatsiynoi-infrastrukturi-ta-zliv-danikh-ukraintsiv).


While it may be a very plausible attribution, especially in regards to Russia’s recent threats to invade Ukraine, security experts have also raised theories that Russian hackers might have also gotten a helping hand from Belarussian cyber units, although no evidence has been presented so far of any tangible collaboration between the two.


Responding to the accusations, Russian officials denied any accusations in statements provided to local news outlets.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]] [[action.malware.name=Wiper]]

#### Industry:
[[victim.industry.name=Information]] [[victim.industry.name=Public]]

#### Location:
[[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Belarus]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.country.name=Ukraine]] [[victim.continent.name=Europe]] [[victim.city.name=Kyiv]] [[victim.country.name=Ukraine]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Websites]] [[Cms]] [[Log4shell]] [[The Record]]
#### CVE's
[[CVE-2021-32648]]

