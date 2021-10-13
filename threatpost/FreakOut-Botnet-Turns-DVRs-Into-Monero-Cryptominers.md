# FreakOut Botnet Turns DVRs Into Monero Cryptominers
### The new Necro Python exploit targets Visual Tool DVRs used in surveillance systems. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175467)
+ Date: October 13, 2021  4:17 pm
+ Author: Becky Bracken


## Article:
Threat group FreakOut’s Necro botnet has developed a new trick: infecting Visual Tools DVRs with a Monero miner. 


Juniper Threat Labs researchers have issued a report detailing [new activities from FreakOut](https://blogs.juniper.net/en-us/threat-research/necro-python-botnet-goes-after-vulnerable-visualtools-dvr), also known as Necro Python and Python.IRCBot. In late September, the team noticed that the botnets started to target Visual Tools DVR VX16 4.2.28.0 models with cryptomining attacks. The devices are typically deployed as part of a professional-quality surveillance system. 


A [command injection vulnerability](https://packetstormsecurity.com/files/163395/Visual-Tools-DVR-VX16-4.2.28.0-Command-Injection.html) was found in the same devices last July. Visual Tools has not yet responded to Threatpost’s request for comment. 


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“The script can run in both Windows and Linux environments,” the Juniper report said. “The script has its own polymorphic engine to morph itself every execution which can bypass signature-based defenses. This works by reading every string in its code and encrypting it using a hardcoded key.”


FreakOut has been [on the scene since](https://threatpost.com/linux-attack-freakout-malware/163137/) at least January, exploiting recently identified and unpatched vulnerabilities to launch distributed denial-of-service (DDoS) and [cryptomining attacks](https://threatpost.com/bogus-cryptomining-apps-google-play/168785/). Juniper reports that the threat actors have developed several iterations of the Necro bot, making steady improvements in its performance and persistence over the past several months. 


“We have noted a few changes on this bot from the previous version,” the report said. “First, it removed the SMB scanner which was observed in the May 2021 attack. Second, it changed the url that it injects to script files on the compromised system.”


**New DGA Functionality Helps Evade Detection**
-----------------------------------------------


The team explained that more recent versions of the Necro bot scrapped its previous reliance on a hardcoded URL for a domain generation algorithm (DGA) for added persistence. 


The new exploit has not yet been fully [evaluated for a CVE](https://nvd.nist.gov/vuln/detail/CVE-2021-42071), according to NIST, but [a proof of concept](https://www.exploit-db.com/exploits/50098) is available through the Exploit Database. 


First the Necro bot scans for the target port: [22, 80, 443, 8081, 8081, 7001]. If detected, it will launch a [XMRig](https://support.alertlogic.com/hc/en-us/articles/360001389791-XMRig-Monero-Miner#:~:text=XMRig%20is%20a%20high%20performance,(both%20x86%20and%20x86_64).&text=Execution%20of%20the%20miner%20will,power%20to%20mine%20Monero%20coins.) – that’s a high-performance Monero (XMR) miner – linked to this wallet: 


[45iHeQwQaunWXryL9YZ2egJxKvWBtWQUE4PKitu1VwYNUqkhHt6nyCTQb2dbvDRqDPXveNq94DG9uTndKcWLYNoG2uonhgH]


The team added that the bot is also still actively trying to exploit these previously identified vulnerabilities: 


Mounir Hahad, head of Juniper Threat Labs, told Threatpost that security teams need security that’s equipped to handle DGA domain attempts. 


“The very existence of this kind of botnet highlights the need for a connected security approach where DNS security capabilities on the network identify connection attempts to DGA domains behind public dynamic DNS services, as well as routers, switches, and firewalls that are capable of immediately isolating the compromised host from the rest of the network,” Hahad said.  

***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[“The]] [[said.]] [[DGA]] [[ThreatPost]]
