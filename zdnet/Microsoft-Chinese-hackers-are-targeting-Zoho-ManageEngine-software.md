# Microsoft: Chinese hackers are targeting Zoho ManageEngine software
### Microsoft warns that hackers are targeting Zoho password management and single sign-on software to compromise Windows machines.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/microsoft-chinese-hackers-are-targeting-zoho-manageengine-software/)
+ Date: November 9, 2021
+ Author: Liam Tung


## Article:
Unknown

Microsoft has sent an alert about a sophisticated Chinese hacker group targeting an obscure bug in Zoho software to install a webshell.

Microsoft Threat Intelligence Center (MSTIC) has detected exploits targeting systems running [Zoho ManageEngine ADSelfService Plus](https://www.manageengine.com/products/self-service-password/), a self-service password management and single sign-on solution, with the remote code execution bug tracked as [CVE-2021-40539](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-40539). Zoho is best known as a popular software-as-a-service vendor, while ManageEngine is the company's enterprise IT management software division.


It's a targeted malware campaign, so most Windows users shouldn't need to worry about it, but Microsoft has [flagged the campaign](https://www.microsoft.com/security/blog/2021/11/08/threat-actor-dev-0322-exploiting-zoho-manageengine-adselfservice-plus/), which it first observed in September, because it's aimed at the US defence industrial base, higher education, consulting services, and IT sectors.

**SEE:** [**Ransomware: It's a 'golden era' for cyber criminals - and it could get worse before it gets better**](https://www.zdnet.com/article/ransomware-its-a-golden-era-for-cyber-criminals-and-it-could-get-worse-before-it-gets-better/)

MSTIC attributes the activity to a group it is tracking as DEV-0322, which also [targeted a zero-day flaw in SolarWinds Serv-U FTP software](https://www.microsoft.com/security/blog/2021/07/13/microsoft-discovers-threat-actor-targeting-solarwinds-serv-u-software-with-0-day-exploit/). The US government attributed an earlier [software supply chain attack on SolarWinds to Kremlin-backed intelligence hackers](https://www.zdnet.com/article/solarwinds-hacking-group-nobelium-is-now-targeting-the-global-it-supply-chain-microsoft-warns/).

Palo Alto Networks Unit 42 [observed the same Chinese group](https://unit42.paloaltonetworks.com/manageengine-godzilla-nglite-kdcsponge/) scanning ManageEngine ADSelfService Plus servers from mid-September to early October. 

The bug concerns a REST API authentication bypass that can lead to remote code execution in vulnerable devices. 






Microsoft fleshes out some details on the latest activity of the group's use of the Zoho bug, which relied on the Godzilla webshell payload. Webshells are generally considered a problem because they can survive a patch on the underlying OS or software. 

It notes that the group was involved in "credential dumping, installing custom binaries, and dropping malware to maintain persistence and move laterally within the network."

**SEE:** [**Ransomware: Industrial services top the hit list - but cyber criminals are diversifying**](https://www.zdnet.com/article/ransomware-industrial-services-are-still-the-most-popular-target-but-now-cyber-criminals-are-diversifying-attacks/)

The attack group also deployed a Trojan Microsoft calls Trojan:Win64/Zebracon, which uses hardcoded credentials to make connections to suspected DEV-0322-compromised Zimbra email servers.

"Godzilla is a functionality-rich webshell that parses inbound HTTP POST requests, decrypts the data with a secret key, executes decrypted content to carry out additional functionality and returns the result via a HTTP response. This allows attackers to keep code likely to be flagged as malicious off the target system until they are ready to dynamically execute it," notes Palo Alto Networks.





#### Tags:
[[Microsoft]] [[Zoho]] [[ManageEngine]] [[ZDNet]]
