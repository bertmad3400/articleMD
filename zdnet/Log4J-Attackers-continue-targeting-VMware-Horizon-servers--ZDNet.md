# Log4J: Attackers continue targeting VMware Horizon servers | ZDNet
### VMware has urged customers to apply the latest guidance as a way to resolve vulnerabilities CVE-2021-44228 and CVE-2021-4504.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/log4j-attackers-continue-targeting-vmware-horizon-servers/
+ Date: 2022-01-21 16:58:00
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/648d544e04767b8c71653463ec50b9f8977ed6bd/2022/01/11/6005ba87-2a82-4d5d-a352-f25e33a510c0/vmware.jpg?width=770&height=578&fit=crop&auto=webp)

Attackers are still targeting VMware Horizon servers through [Log4J vulnerabilities](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/), according to several cybersecurity companies monitoring the situation. 

Two weeks ago, the UK's National Health Service (NHS) [issued](https://www.zdnet.com/article/log4j-flaw-attackers-are-targeting-log4shell-vulnerabilities-in-vmware-horizon-servers-says-nhs/) a warning that an 'unknown threat group' is attempting to exploit a [Log4j vulnerability](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/) ([CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228)) in VMware Horizon servers to establish web shells that could be used to distribute malware and ransomware, steal sensitive information, and complete other malicious attacks. 

Since then, several cybersecurity companies have confirmed that hackers are continuing to target VMware Horizon servers. In a statement to *ZDNet*, VMware said they are continuing to urge customers to apply the latest guidance found in their security advisory, [VMSA-2021-0028](https://www.vmware.com/security/advisories/VMSA-2021-0028.html), in order to resolve vulnerabilities CVE-2021-44228 and CVE-2021-4504. 

"We also recommend that customers visit our corresponding [Questions & Answers document](https://via.vmw.com/vmsa-2021-0028-faq) for the latest information and join the VMware [Security-Announce mailing list](https://lists.vmware.com/cgi-bin/mailman/listinfo/security-announce) for all future advisories. Any service connected to the internet and not yet patched for Log4j vulnerabilities CVE-2021-44228 and CVE-2021-4504 is vulnerable to hackers, and VMware strongly recommends patching," a VMware spokesperson said. 

Rapid7 [said](https://www.rapid7.com/blog/post/2022/01/18/active-exploitation-of-vmware-horizon-servers/) it began monitoring a sudden increase in VMware Horizon exploitation on January 14 and identified five unique avenues that attackers have taken post-exploitation, signaling that multiple actors are involved in this mass exploitation activity.

"The most common activity sees the attacker executing PowerShell and using the built-in System.Net.WebClient object to download cryptocurrency mining software to the system," Rapid7 explained.

Huntress [released](https://www.huntress.com/blog/cybersecurity-advisory-vmware-horizon-servers-actively-being-hit-with-cobalt-strike) its own blog about the issue, noting that according to Shodan, about 25,000 Horizon servers are currently internet accessible worldwide.






Roger Koehler, vice president of threat operations at Huntress, told ZDNet the NHS article didn't give an idea of the scope of the problem. 

"Based on how many Horizon servers in our data set are unpatched (only 18% were patched as of last Friday night), there is a high risk of this seriously impacting hundreds-if not in the low thousands-of businesses. This weekend also marks the first time we've seen proof of widespread escalation, going from gaining initial access to starting to take hostile actions on Horizon servers," Koehler said. 

"Since we're seeing multiple likely unrelated campaigns (cryptominers, web shells, Cobalt Strike), it's likely that this will continue to escalate. Attackers are going to make businesses pay for not fully patching when VMware gave their initial guidance. Although the initial web shell campaign appears to focus on long-term access, it's likely that future activity will focus on targeting or impacting the systems accessible via VMware Horizon. And it makes sense-attackers can use this access to impact all the virtualized hosts and servers." 

Koehler added that these are high-value targets and people are not patching despite multiple widespread campaigns targeting them, noting that they recently witnessed this happen with ProxyShell and ProxyLogon. While these are not quite as significant and far-reaching as this latest cyberattack, these vulnerabilities serve as evidence that attackers will likely be back to target those systems that haven't yet been patched, Koehler explained. 

He said ProxyShell surfaced months after ProxyLogon was disclosed, and it was made possible only because many had failed to properly patch. 

"The timing is also significant. If we think back to the big [Kaseya incident](https://www.zdnet.com/article/updated-kaseya-ransomware-attack-faq-what-we-know-now/), they picked the July 4 holiday weekend. The original widespread intrusion with web shells took place over the Christmas holiday (they were dropped between December 25 and December 29) and things are escalating now that it's another three-day weekend in the US. Is damage control going to become a holiday tradition for those in cybersecurity?" Koehler said.

"The web shell attack between December 25 and 29 was more sophisticated compared to something like the Exchange attack. It seems like the majority of antivirus tools failed to identify that anything was wrong and still haven't caught up. The moral of this story? It's the same old song: patch, patch, patch."





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Conti]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]] [[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Vmware]] [[Koehler]] [[ZDNet]]
#### CVE's
[[CVE-2021-44228]] [[CVE-2021-4504]]

