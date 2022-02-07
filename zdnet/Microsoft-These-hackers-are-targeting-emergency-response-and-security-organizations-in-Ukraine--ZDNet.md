# Microsoft: These hackers are targeting emergency response and security organizations in Ukraine | ZDNet
### Actinium, a hacking group linked to Russia's Federal Security Service (FSB), uses phishing emails as a way to infiltrate government, defense and security agencies.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/microsoft-these-hackers-are-targeting-emergency-response-and-security-organizations-in-ukraine/
+ Date: 2022-02-07 12:52:18
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/a5bd7529b863d8da105f131de3576f24fd53ae5c/2022/01/04/5979e293-db40-4196-86c8-4d6632cbb0dc/ransomware-cyberattack-security-encrypted.jpg?width=770&height=578&fit=crop&auto=webp)

Microsoft has detailed recent hacking activity of cyber actors, most likely aligned with the Russian Federal Security Service (FSB), who have targeted Ukraine government, security agencies and aid organizations. 

Microsoft says the hacking group, which it calls Actinium, has "targeted or compromised accounts" at Ukraine emergency response organizations since October. Actinium hackers also targeted organizations that would coordinate international and humanitarian aid to Ukraine, [it says in a new report](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/). 


"Since October 2021, Actinium has targeted or compromised accounts at organizations critical to emergency response and ensuring the security of Ukrainian territory, as well as organizations that would be involved in coordinating the distribution of international and humanitarian aid to Ukraine in a crisis," Microsoft said.

**SEE:** [**Cybersecurity: Let's get tactical**](https://www.zdnet.com/topic/cybersecurity-lets-get-tactical/#link=%7B%22linkText%22:%22Cybersecurity:%20Let's%20get%20tactical%20(ZDNet%20special%20report)%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/topic/cybersecurity-lets-get-tactical/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D%23link=%7B%22role%22:%22standard%22,%22href%22:%22https://www.zdnet.com/topic/cybersecurity-lets-get-tactical/%23link=%7B%22linkText%22:%22Cybersecurity:%20Let's%20get%20tactical%20(ZDNet%20special%20report)%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/topic/cybersecurity-lets-get-tactical/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D%22,%22target%22:%22%22,%22absolute%22:%22%22,%22linkText%22:%22%3Cstrong%3ECybersecurity:%20Let's%20get%20tactical%20(ZDNet%20special%20report%3C/strong%3E%22%7D) **(ZDNet special report)**

The Security Service of Ukraine (SSU), which heads up Ukraine's counter-intelligence efforts, calls the group Armageddon. SSU has traced the group's earliest activity to at least 2014 and says it focuses on intelligence gathering in Crimea, largely through phishing and malware. 

Armageddon is known for crude but brazen cyberattacks aimed at gathering intel from Ukraine security, defense and law enforcement agencies. 

Microsoft prioritized its report on Actinium's recent activity as concerns mount over Russia's apparent preparations to invade Ukraine. 






While perhaps not that sophisticated or stealthy, the group's tactics are constantly evolving and do prioritize anti-malware evasion, according to Microsoft. It uses a range of targeted "spear-phishing" emails that employ remote document templates and remote macro scripts to infect only selected targets while minimizing the chance of detection through attachment scanning anti-malware systems. 

"Delivery using remote template injection ensures that malicious content is only loaded when required (for example, when the user opens the document)," says Microsoft's Threat Intelligence Center (MSTIC). 

"This helps attackers to evade static detections, for example, by systems that scan attachments for malicious content. Having the malicious macro hosted remotely also allows an attacker to control when and how the malicious component is delivered, further evading detection by preventing automated systems from obtaining and analyzing the malicious component."

The group also employs 'web bugs' that allow the sender to track when a message has been opened and rendered. Lure documents include ones impersonating the World Health Organization containing updates about COVID-19. 

The phishing attachments contain a payload that executes secondary payloads on a compromised device. It uses a range of 'staging' scripts such as heavily obfuscated VBScripts, obfuscated PowerShell commands, self-extracting archives, and LNK files, backed up by curiously named scheduled tasks in scripts to maintain persistence. 

Over a month period, Microsoft saw Actinium using over 25 unique domains and over 80 unique IP addresses to support payload staging and its command and control (C2) infrastructure, indicating they often modify their infrastructure to frustrate investigations. Most of its DNS records for the domains also change once a day, with the domains registered through the legitimate company registrar REG.RU.

Microsoft confirmed it has observed the group using Pterodo malware to gain interactive access to target networks. In some cases, it also used the legitimate UltraVNC program for interactive connections to a target. Actinium's other key piece of malware is QuietSieve, used for exfiltration of data from the compromised host, and to receive and execute a remote payload from the operator. 

Microsoft notes that Actinium rapidly develops a range of payloads with lightweight capabilities via obfuscated scripts that are used to deploy more advanced malware at a later stage. Agile development of these scripts, which Microsoft describes as "fast-moving targets with a high degree of variance", help evade antivirus detection. Examples of these downloaders include DinoTrain, DilongTrash, Obfuberry, PowerPunch, DessertDown, and Obfumerry.

US, European and [UK cybersecurity officials](https://www.zdnet.com/article/uk-security-centre-urges-companies-to-boost-their-defences-after-cyberattacks-on-ukraine/) urged all organizations to shore up defenses [following Microsoft's warning in January that it had discovered destructive wiper malware on several Ukraine systems](https://www.zdnet.com/article/microsoft-says-destructive-malware-being-used-against-ukrainian-organizations/).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tor]] [[action.malware.name=Wiper]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.country.name=Ukraine]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Malware]] [[ZDNet]]

