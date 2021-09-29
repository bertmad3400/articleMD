# Tomiris backdoor discovery linked to Sunshuttle, DarkHalo hackers
### Another backdoor has been tentatively linked to the hackers behind SolarWinds.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/the-tomiris-backdoor-has-now-been-linked-to-sunshuttle-darkhalo-hackers/)
+ Date: September 29, 2021
+ Author: Charlie Osborne


## Article:
Unknown

Researchers have uncovered a new connection between Tomiris and the APT behind the SolarWinds breach, DarkHalo. 


On Wednesday at the Kaspersky Security Analyst Summit (SAS), researchers said that [a new campaign](https://securelist.com/darkhalo-after-solarwinds-the-tomiris-connection/104311/) revealed similarities between DarkHalo's Sunshuttle, as well as "target overlaps" with Kazuar.  

The [SolarWinds incident](https://www.zdnet.com/article/microsoft-solarwinds-attack-took-more-than-1000-engineers-to-create/) took place in 2020. FireEye and Microsoft revealed the breach, in which SolarWinds's Orion network management software was compromised to impact as many as 18,000 customers in a software update-based supply-chain attack.  

While many thousands of clients may have received a malicious update, the threat actors appeared to cherry-pick the targets worthy of further compromise -- including Microsoft, FireEye, and government agencies.  

Microsoft president Brad Smith dubbed the incident as "the largest and most sophisticated attack the world has ever seen." 

![screenshot-2021-09-27-at-15-51-57.png]()![screenshot-2021-09-27-at-15-51-57.png](https://www.zdnet.com/a/img/resize/b6936bc4734a0040c603dfb2f31bc41ac8c98edb/2021/09/27/cb475f99-6830-48ba-976d-1ccaeaf8a8e0/screenshot-2021-09-27-at-15-51-57.png?width=1200&fit=bounds&auto=webp)
 Kaspersky
 Eventually, the finger was pointed at the advanced persistence threat (APT) group DarkHalo/Nobelium as the party responsible, which [managed to deploy](https://www.zdnet.com/article/third-malware-strain-discovered-in-solarwinds-supply-chain-attack/) the Sunburst/Solorigate backdoor, Sunspot build server monitoring software, and Teardrop/Raindrop dropper, designed to deploy a Cobalt Strike beacon, on target systems.   

The Russian, state-backed group's campaign was tracked as [UNC2452](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html), which has also been linked to the [Sunshuttle/GoldMax](https://www.fireeye.com/blog/threat-research/2021/03/sunshuttle-second-stage-backdoor-targeting-us-based-entity.html) backdoor.  






In June, after roughly six months of inactivity from DarkHalo, Kaspersky uncovered a DNS hijacking campaign against multiple government agencies in an unnamed CIS member state. 

"These hijacks were for the most part relatively brief and appear to have primarily targeted the mail servers of the affected organizations," Kaspersky commented. "We do not know how the threat actor was able to achieve this, but we assume they somehow obtained credentials to the control panel of the registrar used by the victims."

The researchers say that the campaign operators redirected victims attempting to access an email service to a fake domain which then prompted them into downloading a malicious software update, made possible by switching legitimate DNS servers for compromised zones to attacker-controlled resolvers. This update contained the Tomiris backdoor.  

"Further analysis showed that the main purpose of the backdoor was to establish a foothold in the attacked system and to download other malicious components," Kaspersky added. "The latter, unfortunately, were not identified during the investigation." 

Tomiris, however, did prove to be an interesting discovery. The backdoor is described as "suspiciously similar" to Sunshuttle. 

Both backdoors are written in the Golang (Go) programming language, the same english language spelling mistakes were in the payloads' code, and each uses similar encryption and obfuscation setups for configuration and network traffic management purposes.  

In addition, both Tomiris and Sunshuttle use scheduled tasks for persistence as well as sleep-based delay mechanisms. The team believes the "general workflow of the two programs" hints at the same development practices.  

However, the backdoor has little function beyond the capability to download additional malware, which suggests Tomiris is likely part of a wider operator toolkit.

It should also be noted that Tomiris has been found in environments also infected with the Kazuar backdoor, malware that Kaspersky has tentatively [linked to Sunburst](https://securelist.com/sunburst-backdoor-kazuar/99981/) -- while Palo Alto has also connected Kazuar and the Turla APT. Cisco Talos has also [recently uncovered](https://blog.talosintelligence.com/2021/09/tinyturla.html) a new, simple backdoor now deployed by the Turla APT on victim systems.  

Kaspersky also acknowledges this may be a case of a 'false flag' designed to mislead researchers and send them down the wrong analysis or attribution paths. Pierre Delcher, security researcher at Kaspersky commented: 


> "None of these items, taken individually, is enough to link Tomiris and Sunshuttle with sufficient confidence. We freely admit that a number of these data points could be accidental, but still feel that taken together they at least suggest the possibility of common authorship or shared development practices." 
> 
> 

###  Previous and related coverage

* [SolarWinds: The more we learn, the worse it looks](https://www.zdnet.com/article/solarwinds-the-more-we-learn-the-worse-it-looks/)  

* [SolarWinds hack analysis reveals 56% boost in command server footprint](https://www.zdnet.com/article/solarwinds-hack-analysis-reveals-56-boost-in-command-server-footprint/)  

* [Microsoft: SolarWinds attack took more than 1,000 engineers to create](https://www.zdnet.com/article/microsoft-solarwinds-attack-took-more-than-1000-engineers-to-create/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Kaspersky]] [[Tomiris]] [[SolarWinds]] [[ZDNet]]
