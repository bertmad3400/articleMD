# Threat actor ports Cobalt Strike beacon to Linux, uses it in attacks
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/threat-actor-ports-cobalt-strike-beacon-to-linux-uses-it-in-attacks/)
+ Date: September 13, 2021
+ Author: Catalin Cimpanu


## Article:
![Threat actor ports Cobalt Strike beacon to Linux, uses it in attacks](https://therecord.media/wp-content/uploads/2021/09/Cobalt-Strike.png)

A newly discovered hacking group has used a customized and enhanced version of a popular security tool to orchestrate attacks against a wide range of targets across the world over the month of August 2021.


The attacks targeted telecom companies, government agencies, IT companies, financial institutions, and advisory companies.


Codenamed **Vermilion**, the threat actor modified a version of [Cobalt Strike](https://www.cobaltstrike.com/), a penetration testing toolkit developed by security software firm HelpSystems.


While the tool was developed to help security firms emulate techniques used by threat actors as part of penetration tests, the tool’s advanced features have also made it a favorite among cybercrime groups.


Over the past few years, the Cobalt Strike toolkit has been cracked, pirated, and widely adopted by malware operations, according to research from [Intel 471](https://intel471.com/blog/cobalt-strike-cybercriminals-trickbot-qbot-hancitor), [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/cobalt-strike-favorite-tool-apt-crimeware), and a [Recorded Future report](https://www.recordedfuture.com/2020-adversary-infrastructure-report/?__hstc=156209188.d85cadfa0a6d845494553c933046377b.1631545214307.1631545214307.1631545214307.1&__hssc=156209188.1.1631545214308&__hsfp=2967514955) that found that Cobalt Strike and fellow penetration testing tool Metasploit accounted for more than a quarter of all the malware command and control (C&C) servers deployed in 2020.


Under the hood, the tool uses a server-client architecture, allowing security researchers (or malware authors) to use its server-side component to attack systems and deploy a backdoor called the [Cobalt Strike Beacon](https://www.cobaltstrike.com/help-beacon), which is typically used to deploy other additional Cobalt Strike components on infected systems.


The Beacon backdoor is [only available for Windows systems](https://blog.cobaltstrike.com/2016/03/23/linux-left-out-in-the-cold/), and because of its widespread abuse in recent years, security software often has good detection capabilities for this particular payload.


### Cobalt Strike Beacon ported to Linux


But in a [report](https://www.intezer.com/blog/malware-analysis/vermilionstrike-reimplementation-cobaltstrike) published today by cloud security firm Intezer Labs, the company said that in its quest to avoid having its malware detected, the Vermilion group developed **Vermilion Strike**, a one-of-a-kind Linux version of the Cobalt Strike Beacon backdoor.


Moreover, the group also re-wrote the original Windows version of the Beacon backdoor — for the same reason of avoiding getting its tools detected.


Intezer called the discovery significant.



> The sophistication of this threat, its intent to conduct espionage, and the fact that the code hasn’t been seen before in other attacks, together with the fact that it targets specific entities in the wild, leads us to believe that this threat was developed by a skilled threat actor.
> 
> Intezer Labs


### No connection to Secureworks’ August findings


Intezer’s discovery comes after [US security firm Secureworks found](https://www.secureworks.com/blog/detecting-cobalt-strike-government-sponsored-threat-groups) that a Vietnamese cyber-espionage group known as APT32 (Tin Woodlawn) had also created and deployed a modified version of the Cobalt Strike Beacon backdoor earlier this summer.


Asked if these are the same tools, an Intezer spokesperson told *The Record* that the two modifications are different and appear to have been developed by two different threat actors, with Vermilion putting more effort in customizing its tool and even developing a never-before-seen Linux variant.


The two discoveries might also signal the emergence of a new trend where threat actors will make slight modifications to Cobalt Strike’s code in order to avoid detection, which has been getting better in recent years as the widespread abuse has forced more and more antivirus makers to label the tool as downright malware, despite its initial innocuous role.





#### Tags:
[[malware]] [[Linux]] [[Intezer]] [[The Record]]
