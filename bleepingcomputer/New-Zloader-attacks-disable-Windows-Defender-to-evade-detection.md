# New Zloader attacks disable Windows Defender to evade detection
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-zloader-attacks-disable-windows-defender-to-evade-detection/)
+ Date: September 14, 2021
+ Author: Sergiu Gatlan


## Article:
![New Zloader attacks disable Windows Defender to evade detection](https://www.bleepstatic.com/content/hl-images/2021/07/09/Windows.jpg)


An ongoing Zloader campaign uses a new infection chain to disable Microsoft Defender Antivirus (formerly Windows Defender) on victims' computers to evade detection.


According to Microsoft's stats, [Microsoft Defender Antivirus](https://www.microsoft.com/en-us/windows/comprehensive-security) is the anti-malware solution pre-installed on [more than 1 billion systems](https://news.microsoft.com/bythenumbers/en/windowsdevices) running Windows 10.


The attackers have also changed the malware delivery vector from spam or phishing emails to TeamViewer Google ads published through Google Adwords, redirecting the targets to fake download sites.


From there, they are tricked into downloading signed and malicious MSI installers designed to install Zloader malware payloads on their computers.


"The attack chain analyzed in this research shows how the complexity of the attack has grown in order to reach a higher level of stealthiness," said SentinelLabs security researchers Antonio Pirozzi and Antonio Cocomazzi [in a report published today](https://www.sentinelone.com/labs/hide-and-seek-new-zloader-infection-chain-comes-with-improved-stealth-and-evasion-mechanisms/).


"The first stage dropper has been changed from the classic malicious document to a stealthy, signed MSI payload. It uses backdoored binaries and a series of LOLBAS to impair defenses and proxy the execution of their payloads.



![Zloader attack chain](https://www.bleepstatic.com/images/news/u/1109292/2021/Zloader%20attack%20chain.jpg)*Zloader attack chain (SentinelLabs)*
Attacks focused on Australian and German banking customers
----------------------------------------------------------


[Zloader](https://www.bleepingcomputer.com/tag/zloader/) (also known as Terdot and DELoader) is a banking trojan initially spotted back in August 2015 when it was used to attack several British financial targets' customers.


Like [Zeus Panda](https://www.bleepingcomputer.com/tag/zeus-panda/) and [Floki Bot](https://securityintelligence.com/news/floki-bot-funny-name-financial-nightmare/), this malware is almost entirely based on the Zeus v2 Trojan's source code [leaked online](http://web.archive.org/web/20110719121544/http://www.csis.dk/en/csis/blog/3229/) more than a decade ago.


The banking trojan [targeted banks](https://securityintelligence.com/around-the-world-with-zeus-sphinx-from-canada-to-australia-and-back/) worldwide, from Australia and Brazil to North America, attempting to harvest financial data via web injections that use social engineering to convince infected customers to hand out auth codes and credentials.


More recently, it has also been used to deliver ransomware payloads such as [Ryuk](https://www.sentinelone.com/labs/an-inside-look-at-how-ryuk-evolved-its-encryption-and-evasion-techniques/) and [Egregor](https://www.sentinelone.com/labs/egregor-raas-continues-the-chaos-with-cobalt-strike-and-rclone/). Zloader also comes with backdoor and remote access capabilities, and it can also be used as a malware loader to drop further payloads on infected devices.


According to SentinelLabs' research, this latest campaign is primarily focused on targeting customers of German and Australian banking institutions.


"This is the first time we have observed this attack chain in a ZLoader campaign," [SentinelLabs' researchers concluded](https://assets.sentinelone.com/sentinellabs/SentinelLabs-Zloader).


"At the time of writing, we have no evidence that the delivery chain has been implemented by a specific affiliate or if it was provided by the main operator."


MalwareBytes, who tracks this [malvertising campaign they named Malsmoke](https://www.bleepingcomputer.com/news/security/adult-site-users-targeted-with-zloader-malware-via-fake-java-update/) since the start of 2020, saw the threat actors infecting their targets with the Smoke Loader malware dropper using the Fallout exploit kit via adult-themed malicious sites.


They've switched to sites imitating Discord, TeamViewer, Zoom, and QuickBooks starting with the end of August 2021, and are likely targeting businesses rather than individuals according to [security researcher nao\_sec](https://twitter.com/nao_sec/status/1437800037468160006).




#### Tags:
[[Zloader]] [[malware]] [[Microsoft]] [[SentinelLabs]] [[Bleeping Computer]]
