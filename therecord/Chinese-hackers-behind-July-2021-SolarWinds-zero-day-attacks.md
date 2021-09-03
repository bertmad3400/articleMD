# Chinese hackers behind July 2021 SolarWinds zero-day attacks
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/chinese-hackers-behind-july-2021-solarwinds-zero-day-attacks/)
+ Date: September 3, 2021
+ Author: Catalin Cimpanu


## Article:
![Chinese hackers behind July 2021 SolarWinds zero-day attacks](https://therecord.media/wp-content/uploads/2021/09/exploit-vulnerability-abstract.png)

[In mid-July this year](https://therecord.media/microsoft-discovers-a-solarwinds-zero-day-exploited-in-the-wild/), Texas-based software provider SolarWinds released an emergency security update to patch a zero-day in its Serv-U file transferring technology that was being exploited in the wild.


At the time, SolarWinds did not share any details about the attacks and only said that it learned of the bug from Microsoft’s security team.


In a [blog post on Thursday](https://www.microsoft.com/security/blog/2021/09/02/a-deep-dive-into-the-solarwinds-serv-u-ssh-vulnerability/), Microsoft revealed more details about the July attacks.


The company said the zero-day was the work of a new threat actor the company was tracking as **DEV-0322**, which Microsoft described as “**a group operating out of China, based on observed victimology, tactics, and procedures**.”


Microsoft said the group targeted SolarWinds Serv-U servers “by connecting to the open SSH port and sending a malformed pre-auth connection request,” which allowed DEV-0322 operators to run malicious code on the targeted system and take over vulnerable devices.


The OS maker did not go into details about what the intruders did once they breached a target. It is unclear if the hackers were interested in cyber-espionage and intelligence collection or if DEV-0322 was a run-of-the-mill crypto-mining gang.


### Zero-day root cause: No ASLR


On the other hand, Microsoft delved into the technical aspects of the zero-day itself, tracked as CVE-2021-35211.


Microsoft said that one of the reasons the attacks succeeded was because some of the Serv-U binaries had not been protected by [ASLR (Address Space Layout Randomization)](https://en.wikipedia.org/wiki/Address_space_layout_randomization), a feature that randomizes the memory location of an application in order to prevent attackers from targeting specific memory sections and corrupt an app’s memory.


As ASLR protection was missing, Microsoft said that exploiting the Serv-U zero-day was “not so complicated.”


“Enabling ASLR is a simple compile-time flag which is enabled by default and has been available since Windows Vista,” Microsoft engineers said.


### Chinese hackers exploited SolarWinds products before


After news of the major SolarWinds supply-chain attack broke last year, an attack carried out by Russian cyber-espionage teams [linked to the SVR intelligence service](https://therecord.media/white-house-formally-blames-russian-intelligence-service-svr-for-solarwinds-hack/), the subsequent investigation found unrelated SolarWinds vulnerabilities that [were also exploited by Chinese hackers](https://therecord.media/attacks-on-solarwinds-servers-also-linked-to-chinese-threat-actor/).


US security firm Secureworks, which discovered these attacks, codenamed the Chinese group as [Spiral](https://www.secureworks.com/blog/supernova-web-shell-deployment-linked-to-spiral-threat-group).


Per Secureworks, in the attacks detected at the end of 2020 and start of 2021, Spiral exploited a SolarWinds zero-day in the Orion IT monitoring platform tracked as [CVE-2020-10148](https://www.kb.cert.org/vuls/id/843464).





#### Tags:
[[SolarWinds]] [[Microsoft]] [[zero-day]] [[Serv-U]] [[ASLR]] [[The Record]]
