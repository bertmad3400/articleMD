# No honor among thieves: One in five targets of FIN12 hacking group is in healthcare
### The group strikes big game targets with annual revenues of over $6 billion.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/no-honor-among-thieves-one-in-five-targets-of-fin12-hacking-group-is-involved-in-healthcare/)
+ Date: October 7, 2021
+ Author: Charlie Osborne


## Article:
Unknown

You'd hope that even though ransomware is a lucrative criminal enterprise, there might be some targets that are kept off the list for ethical reasons. 


This is [not so with FIN12](https://www.mandiant.com/resources/fin12-ransomware-intrusion-actor-pursuing-healthcare-targets), a big game hunting ransomware group of which one in five of the group's victims is within the healthcare sector.  

The deployment of ransomware is popular and prolific cybercriminal activity, with potential destructive impacts outweighing other forms of crime such as straight data theft, cryptojacking, and insider threats.  

This year alone, ransomware has been used to wreak havoc in high-profile cases such as the widespread [Microsoft Exchange Server](https://www.zdnet.com/article/everything-you-need-to-know-about-microsoft-exchange-server-hack/) hacking spree, the [Colonial Pipeline attack](https://www.zdnet.com/article/colonial-pipeline-ransomware-attack-everything-you-need-to-know/) that caused fuel shortages in the US, and the disruption of supply chains due to the compromise of systems belonging to global meatpacker [JBS USA](https://www.zdnet.com/article/ransomware-meat-firm-jbs-says-it-paid-out-11m-after-attack/).  

Research conducted by KELA in August on the [initial access broker](https://www.zdnet.com/article/ransomware-operators-love-them-key-trends-in-the-initial-access-broker-space/) (IAB) space found that healthcare-related ads offering access were few and far between, and so you would hope this sector -- alongside funeral services, charities, and critical services -- might be sectioned off by ransomware groups.  

However, there was another case this year that shows this is not always the case: the fall of Ireland's [Health Service Executive](https://www.zdnet.com/article/ransomware-irelands-health-service-is-still-significantly-disrupted-weeks-after-attack/) (HSE) to ransomware, a security incident that caused disruption for weeks to critical care services.  

If a ransomware outbreak restricts access to key medical records, appointment details, treatment notes, and patient data, this can lead to delays and in the worst scenarios, death, [according to research](https://www.zdnet.com/article/ransomware-attacks-against-hospitals-are-having-some-very-grim-consequences/) conducted by The Ponemon Institute and Censinet.  






On Thursday, Mandiant said that FIN12 -- upgraded from [UNC1878](https://www.mandiant.com/resources/kegtap-and-singlemalt-with-a-ransomware-chaser) by the cybersecurity firm -- is a financially driven group that targets organizations with average annual revenue of over $6 billion. Almost all of the threat group's victims generate a revenue of at least $300 million. 

"This number could be inflated by a few extreme outliers and collection bias; however, FIN12 generally appears to target larger organizations than the average ransomware affiliate," the researchers say.

Speaking to ZDNet, Joshua Shilko, Principal Analyst at Mandiant said the group has earned itself a place in the "top tier of big game hunters" -- the operations which focus on the targets most likely to offer the biggest financial rewards in ransom payments.

"By all measures, FIN12 has been the most prolific ransomware actor that we track who is focused on high-value targets," Shilko said. "The average annual revenue for FIN12 victims was in the multi-billions. FIN12 is also our most frequently observed ransomware deployment actor."

Active since at least 2018, FIN12 used to focus on North America but over the past year has expanded its victim range to Europe and the Asia Pacific region. Mandiant says that FIN12 intrusions now make up close to 20% of incidents the firm's response team has worked on since September last year.

![screenshot-2021-10-04-at-13-49-12.png]()![screenshot-2021-10-04-at-13-49-12.png](https://www.zdnet.com/a/img/resize/a195231147ad5b0e73d975614e115e47b4a9db7d/2021/10/04/4d83150f-5863-44e6-9dd0-6d45e2ba34fc/screenshot-2021-10-04-at-13-49-12.png?width=1200&fit=bounds&auto=webp)
 Mandiant
 Threat actors will often purchase initial access to a target system to cut out the legwork of finding working credentials, VPN access, or a software vulnerability ripe for exploit. Mandiant believes with "high confidence" that the group relies on others for initial access. 

Zach Riddle, Senior Analyst at Mandiant told us: 


> "Actors providing initial access to ransomware operators typically receive payment in the form of a percentage of the ransom after a victim has paid, though actors may also purchase access to victims' networks for a set price. 
> 
> While the percentage paid for initial access can likely vary based on several factors, we have seen evidence that FIN12 has paid up to 30-35% of a ransom payment to a suspected initial access provider."
> 
> 

The cybercriminals seem to have no moral compass, either, with 20% of its victims belonging to the healthcare sector. Many ransomware-as-a-service (RaaS) outfits do not allow hospitals to be targeted, but as a result, Mandiant says that it may be cheaper for FIN12 to buy initial access due to low demand elsewhere.  

However, this might not explain FIN12's willingness to target healthcare. 

"We do not believe that others refusing to target healthcare has a direct correlation to FIN12's willingness to target this industry," commented Riddle. "FIN12 may perceive that there is a higher willingness for hospitals to quickly pay ransoms to recover critical systems rather than spend weeks negotiating with actors and/or remediating the issue. Ultimately, the criticality of the services they provide not only likely results in a higher chance that FIN12 will receive a payment from the victim, but also a quicker payment process."

FIN12 is closely linked [to Trickbot](https://www.zdnet.com/article/trickbot-is-back-again-with-fresh-phishing-and-malware-attacks/), a botnet operation that offers cybercriminals modular options including means of exploit and persistence. Despite having its infrastructure [disrupted by Microsoft](https://www.zdnet.com/article/microsoft-and-other-tech-companies-orchestrate-takedown-of-trickbot-botnet/), the threat actors have recently returned with campaigns against legal and insurance companies in North America. 

The group's main goal is to deploy [Ryuk ransomware](https://www.zdnet.com/article/this-dangerous-ransomware-is-using-a-new-trick-to-encrypt-your-network/). Ryuk is a prolific and dangerous variant of malware, containing not only the typical functions of ransomware -- the ability to encrypt systems to allow operators to demand payment in return for a decryption key  -- but also new worm-like capabilities to spread and infect additional systems. 

Mandiant suspects that FIN12 is of Russian-speaking origin, with all currently identified Ryuk ransomware operators speaking this language. In addition, other malware used by FIN12, dubbed Grimagent -- and, so far, remaining unconnected to any other threat group -- contains files and components in Russian.

FIN12's average time-to-ransom is just under four days, with its speed increasing year-over-year. In some cases, a successful ransomware campaign was managed in just two-and-a-half days.  

"While it is possible that they will test out other backdoors or even sponsor the development of private tools in the future, they seemingly have settled into a pattern of disguising their beacon activity using malleable C2 profiles and obfuscating their common payloads with a range of in-memory loaders," Shilko said. "Notably, actors also sometimes make changes based on public reporting and it would not be surprising if the group made changes based on our reporting; however, we anticipate that these changes would largely focus on limiting detection rather than rethinking their larger playbook."

###  Previous and related coverage

* [AI will have a huge impact on your healthcare. But there are still big obstacles to overcome](https://www.zdnet.com/article/ai-will-have-a-huge-impact-on-your-healthcare-but-there-are-still-big-obstacles-to-overcome/)  

* [Microsoft has big plans for healthcare, and it's taking a different path to the rest of big tech](https://www.zdnet.com/article/microsoft-has-big-plans-for-healthcare-and-its-taking-a-different-path-to-the-rest-of-big-tech/)  

* [What is digital health? Everything you need to know about the future of healthcare](https://www.zdnet.com/article/what-is-digital-health/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[ransomware]] [[FIN12]] [[Mandiant]] [[Ryuk]] [[ZDNet]]
