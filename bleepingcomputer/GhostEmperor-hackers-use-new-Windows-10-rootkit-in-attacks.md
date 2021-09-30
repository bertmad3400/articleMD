# GhostEmperor hackers use new Windows 10 rootkit in attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/ghostemperor-hackers-use-new-windows-10-rootkit-in-attacks/)
+ Date: September 30, 2021
+ Author: Sergiu Gatlan


## Article:
![GhostEmperor hackers use new Windows 10 rootkit in attacks](https://www.bleepstatic.com/images/news/u/1109292/2021/China-fingerprint.jpg)


Chinese-speaking cyberspies have targeted Southeast Asian governmental entities and telecommunication companies for more than a year, backdooring systems running the latest Windows 10 versions with a newly discovered rootkit.


The hacking group, dubbed **GhostEmperor** by Kaspersky researchers who spotted it, use the **Demodex** rootkit, which acts as a backdoor to maintain persistence on compromised servers.


This rootkit's primary goal is to hide malware artifacts (including files, registry keys, and network traffic) to evade detection by both forensic investigators and security products.


"To bypass the Windows Driver Signature Enforcement mechanism, GhostEmperor uses a loading scheme involving a component of an open-source project named 'Cheat Engine', "Kaspersky [said in July](https://usa.kaspersky.com/about/press-releases/2021_ghostemperor-apt-targets-high-profile-victims-using-unknown-rootkit) when it released the first details regarding this threat actor.


"This advanced toolset is unique and Kaspersky researchers see no similarity to already known threat actors. Kaspersky experts have surmised that the toolset has been in use since at least July 2020."



![GhostEmperor infection chain](https://www.bleepstatic.com/images/news/u/1109292/2021/GhostEmperor%20infection%20chain.png)*GhostEmperor infection chain (Kaspersky)*
To breach their victims' servers, the threat actors exploited known vulnerabilities in Internet-facing server software, including Apache, Window IIS, Oracle, and Microsoft Exchange (the latter hit two days after the [ProxyLogon bugs](https://www.bleepingcomputer.com/tag/proxylogon/) were publicly disclosed).


GhostEmperor also uses a "sophisticated multi-stage malware framework" that allows the attackers with remote control capabilities over breached devices to provide remote control over the attacked servers.




> 
> [8/n] We assess that the common infection vectors were exploitation of public facing web servers and ProxyLogon, which we saw being used as early as March 4, two days after the CVE was released. [pic.twitter.com/rtMk6WPPAt](https://t.co/rtMk6WPPAt)
> 
> 
> — Mark Lechtik (@\_marklech\_) [September 30, 2021](https://twitter.com/_marklech_/status/1443536509378957314?ref_src=twsrc%5Etfw)


Skilled hacking group with a focus on high-profile targets
----------------------------------------------------------


GhostEmperor operators showed that they are "accomplished in their craft" and with a significant set of skills highlighted through the use of both sophisticated and uncommon anti-analysis and anti-forensic techniques.


While the vast majority of their attacks were focused on telecom firms and government organizations from South East Asia (e.g., Malaysia, Thailand, Vietnam, Indonesia), the researchers also observed targeting of other geopolitical areas, including countries like Egypt, Ethiopia, and Afghanistan.


"We observed that the underlying actor managed to remain under the radar for months, all the while demonstrating a finesse when it came to developing the malicious toolkit, a profound understanding of an investigator's mindset and the ability to counter forensic analysis in various ways," Kaspersky [concluded](https://securelist.com/ghostemperor-from-proxylogon-to-kernel-mode/104407/).


"The attackers conducted the required level of research to make the Demodex rootkit fully functional on Windows 10, allowing it to load through documented features of a third-party signed and benign driver.


"This suggests that rootkits still need to be taken into account as a TTP during investigations and that advanced threat actors, such as the one behind GhostEmperor, are willing to continue making use of them in future campaigns."


Further technical details regarding GhostEmperor's tactics and the Demodex rootkit can be found in Kaspersky's [deep dive](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2021/09/30094337/GhostEmperor_technical-details_PDF_eng.pdf) and [report](https://securelist.com/ghostemperor-from-proxylogon-to-kernel-mode/104407/).




#### Tags:
[[GhostEmperor]] [[Kaspersky]] [[Windows]] [[rootkit]] [[Bleeping Computer]]
