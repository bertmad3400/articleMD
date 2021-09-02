# Translated Conti ransomware playbook gives insight into attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/translated-conti-ransomware-playbook-gives-insight-into-attacks/)
+ Date: September 2, 2021
+ Author: Ionut Ilascu


## Article:
![Conti ransomware affiliate's cookbook in English](https://www.bleepstatic.com/content/posts/2021/09/02/ContiCookbook2.jpg)


Almost a month after a disgruntled [Conti affiliate leaked](https://www.bleepingcomputer.com/news/security/angry-conti-ransomware-affiliate-leaks-gangs-attack-playbook/) the gang’s attack playbook, security researchers shared a translated variant that clarifies any misinterpretation caused by automated translation.


Apart from providing information about the gang’s attack methods and the thoroughness of the instructions, which allow for less-skilled actors to become Conti ransomware affiliates and hit valuable targets.



![](https://www.bleepstatic.com/images/news/ransomware/c/conti/leaked-playbook/folder-listing.jpg)**Leaked Conti training materials**
### Little skill required


Linguists working with Cisco Talos researchers went through the leaked material to provide an intelligible English version that accurately describes the gang’s techniques and tools.


The attack scenarios described in the documents were so thorough that “even amateur adversaries [could] carry out destructive ransomware attacks,” the researchers say.



“This lower barrier to entry also may have led to the leak by a disgruntled member who was viewed as less technical (aka "a script kiddie") and less important”



Among the “tips” provided in the manuals is how to get administrator access after breaching a victim’s network by using commands and tools to list users, particularly those with Active Directory access.


Simple reconnaissance like checking LinkedIn and other social media platforms to identify employees with privileged access is also detailed, with a note that the techniques work better for companies in the U.S. and Europe.


### Tools and techniques


The top tool described in the leaked material is the Cobalt Strike red-teaming framework, accompanied by a cracked 4.3 version of the software.


Usage instructions also referred to exploiting the ZeroLogon vulnerability ([CVE-2020-1472](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-1472)). Other critical bugs mentioned in Conti ransomware’s playbook are PrintNightmare (CVE-2021-1675, CVE-2021-34527) and EternalBlue (CVE-2017-0143/0148).


Some of the tools detailed by the adversary are not what Cisco researchers typically see during incident response engagements:


* [Armitage](https://tools.kali.org/exploitation-tools/armitage) ​- Java-based GUI front-end for the Metasploit penetration testing platform
* [SharpView](https://github.com/tevora-threat/SharpView) - a .NET port of the PowerView tool from the PowerShell-based PowerSploit offensive toolkit
* [SharpChrome](https://github.com/GhostPack/SharpDPAPI%23sharpchrome) - for decrypting logins and cookies in Chrome
* [SeatBelt](https://github.com/GhostPack/Seatbelt) - collects system data like OS version, UAC policy, user folders


Among other tools and command-line utilities described in the leaked documents include the following:


* [ADFind](https://www.joeware.net/freetools/tools/adfind/) - Active Directory query tool
* PowerShell framework - to disable Windows Defender
* [GMER](http://www.gmer.net/) - an alternative for identifying security solutions and disabling them
* SMBAutoBrute - for brute–forcing accounts on current domain
* Kerberoasting - a technique for using brute force to crack the hash of a Kerberos password
* Mimikatz - for dumping passwords from memory
* RouterScan - a tool for discovering devices on the network and for extracting passwords through an exploit or brute force.
* AnyDesk - remote desktop application, for persistence
* [Atera](https://www.bleepingcomputer.com/news/security/conti-ransomware-prioritizes-revenue-and-cyberinsurance-data-theft/v) - another remote access software


Before moving to the exploitation part, the affiliates are instructed to learn about their victim’s revenue by looking for open source info.


The leak from the angry Conti affiliate also includes video tutorials, mostly in Russian, that explain how to use PowerShell for pen-testing, attacking the Active Directory, or how to use leverage SQL Server in a Windows domain.


Much of the video tutorials (Metasploit, PowerShell, WMI attacks and defense, network pen-testing) for affiliates is from various offensive security resources readily available online.


Cisco Talos researchers believe that the translated version of the leaked Conti documentation will help other researchers better understand the tactics, techniques, and procedures of this threat actor as well as others that may be inspired by documentation.



“This is an opportunity for defenders to make sure they have logic in place to detect these types of behaviors or compensating controls to help mitigate the risk. This translation should be viewed as an opportunity for defenders to get a better handle on how these groups operate and the tools they tend to leverage in these attacks” - [Cisco Talos](https://blog.talosintelligence.com/2021/09/Conti-leak-translation.html)



The researchers provide translated [individual texts in a ZIP archive](https://talosintelligence.com/resources/302) as well as a [PDF file](https://talosintelligence.com/resources/269). A [summary of the materials](https://www.fortinet.com/blog/threat-research/affiliates-cookbook-firsthand-peek-into-operations-and-tradecraft-of-conti) is also available from Fortinet.




#### Tags:
[[Conti]] [[gang’s]] [[Talos]] [[Bleeping Computer]]
