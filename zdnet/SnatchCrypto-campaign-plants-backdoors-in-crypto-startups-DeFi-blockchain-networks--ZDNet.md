# SnatchCrypto campaign plants backdoors in crypto startups, DeFi, blockchain networks | ZDNet
### Malware is used to find and empty cryptocurrency wallets at victim organizations.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/snatchcrypto-campaign-plants-backdoors-in-crypto-exchanges-defi-blockchain-networks/
+ Date: 2022-01-14 11:49:40
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/8b497cff5a0028d77450ec08e8318cacba872b9e/2021/08/12/880e080a-7301-4a4b-a4e7-def615879cd5/cryptocurrency-hackers.jpg?width=770&height=578&fit=crop&auto=webp)

A new campaign focused on emptying the cryptocurrency wallets of organizations in the financial and crypto spaces has been revealed by researchers. 


Dubbed SnatchCrypto, Kaspersky researchers [said on Thursday](https://securelist.com/the-bluenoroff-cryptocurrency-hunt-is-still-on/105488/) that the campaign is the work of BlueNoroff, an advanced persistent threat (APT) group suspected of being connected to the larger Lazarus APT. 

Lazarus is a North Korean hacking unit tied to cyberattacks against banks and financial services. The APT specializes in SWIFT-based intrusions in countries including Vietnam, Bangladesh, Taiwan. Alongside Cobalt and FIN7, Blueliv recently [branded the group](https://www.zdnet.com/article/fingers-point-to-lazarus-cobalt-fin7-as-key-hacking-groups-focused-on-finance-industry/) as one of the top threats faced by FinTech firms today.  

"The group [BlueNoroff] seems to work more like a unit within a larger formation of Lazarus attackers, with the ability to tap into its vast resources: be it malware implants, exploits, or infrastructure," the researchers say. 

According to Kaspersky, BlueNoroff has conducted a series of attacks against both small and medium-sized companies tied to cryptocurrency, virtual assets, the blockchain, smart contracts, decentralized finance (DeFI), and FinTech in general.  

BlueNoroff focuses on building – and abusing – trust to infiltrate company networks. Whether this is business communication and chats or wider social engineering techniques, the APT spends a lot of time and effort learning about its victims. 

As of November 2021, Kaspersky says the group has been "stalking and studying" cryptocurrency startups. BlueNoroff aims to create 'maps' of current topics of interest in the target organization and then uses this information as a springboard to launch social engineering attacks that appear to be legitimate and trustworthy.  






"BlueNoroff compromises companies through precise identification of the necessary people and the topics they are discussing at a given time," the researchers note. "A document sent from one colleague to another on a topic, which is currently being discussed, is unlikely to trigger any suspicion." 

For example, an email may be sent that pretends to be a shared document hosted on Google Drive from a 'colleague' to an employee of a startup. In a sample obtained by Kaspersky, a notification was sent at the time the trap document was opened.  

In another example, an email was pushed as a forward that appears to have been sent by a colleague – potentially increasing trust as the message looked as though it had already been checked. 

The APT also impersonates legitimate companies in phishing emails, including Coinsquad, Emurgo, Youbi Capital, and Sinovation Ventures.  

[CVE-2017-0199](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2017-0199), a remote code execution (RCE) flaw, is used to trigger a remote script linked to the malicious documents. The exploit will fetch a payload from a URL embedded in these files, and a remote template is also pulled. When they combine, base64-encoded binary objects and a VBA macro become available, then used to spawn a process for privilege escalation before the main payload is executed on a target system.  

"Interestingly, BlueNoroff shows improved opsec at this stage," Kaspersky says. "The VBA macro does a cleanup by removing the binary objects and the reference to the remote template from the original document and saving it to the same file. This essentially de-weaponizes the document leaving investigators scratching their head during analysis." 

Other infection chains observed include the use of zipped Windows shortcut files or malicious Word documents that are used to fetch secondary-stage payloads.  

At this point, a PowerShell agent is used to deploy a backdoor. The malware is able to remotely connect to its operator's command-and-control (C2) server, manipulate processes and the registry, execute commands, and steal data stored by the Chrome browser, Putty, and WinSCP. In addition, a secondary backdoor, keylogger, and screenshot taker may also be launched on the machine.  

The final payload is a custom backdoor that has only been seen in attacks conducted by BlueNoroff. This malware will collect system data and configuration related to cryptocurrency software and will attempt to interject between transactions stemming from hardware wallets.  

Of particular note is when victims use browser extensions to manage their crypto, The Metamask extension, for example, will be tampered with to monitor transactions and allow the attackers to choose the right moment to strike.  

The researchers explained how these attacks take place: 


> "When the compromised user transfers funds to another account, the transaction is signed on the hardware wallet. However, given that the action was initiated by the user at the very right moment, the user doesn't suspect anything fishy is going on and confirms the transaction on the secure device without paying attention to the transaction details.  
> 
> The user doesn't get too worried when the size of the payment he/she inputs is low and the mistake feels insignificant. However, the attackers modify not only the recipient address, but also push the amount of currency to the limit, essentially draining the account in one move." 
> 
> 

Victims have been traced to Russia, Poland, the US, Hong Kong, Singapore, China, and other countries.  

###  Previous and related coverage

* [Cryptocurrency scams pose largest threat to investors](https://www.zdnet.com/article/cryptocurrency-scams-pose-largest-threat-to-investors/)
* [Norton's cynical crypto ploy: A dark harbinger of crapware to come?](https://www.zdnet.com/article/nortons-cynical-crypto-ploy-a-dark-harbinger-of-crapware-to-come/)
* [In just a week, my Bitcoin 'investment' plummeted by almost 14%](https://www.zdnet.com/article/in-just-a-week-my-bitcoin-investment-plummeted-by-almost-14/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Threatactor:
[[threatactor.name=APT38]] [[threatactor.name=FIN7]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Finance]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Bangladesh]] [[victim.continent.name=Asia]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Singapore]] [[victim.continent.name=Asia]] [[victim.city.name=Singapore]] [[victim.country.name=Singapore]] [[victim.continent.name=Asia]] [[victim.country.name=Taiwan]] [[victim.continent.name=Asia]] [[victim.country.name=Vietnam]] [[victim.continent.name=Asia]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.country.name=Poland]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Bluenoroff]] [[Kaspersky]] [[Malware]] [[ZDNet]]
#### CVE's
[[CVE-2017-0199]]

