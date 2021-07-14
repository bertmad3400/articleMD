# Microsoft links Serv-U zero-day attacks to Chinese hacking group
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/microsoft-links-serv-u-zero-day-attacks-to-chinese-hacking-group/)
+ Date: July 13, 2021
+ Author: Catalin Cimpanu


## Article:
![Microsoft links Serv-U zero-day attacks to Chinese hacking group](https://therecord.media/wp-content/uploads/2021/07/threat-actor-china.jpg)

Microsoft said today that the [recent wave of attacks](https://therecord.media/microsoft-discovers-a-solarwinds-zero-day-exploited-in-the-wild/) that have targeted SolarWinds file transfer servers are the work of a Chinese hacking group the company has been tracking under the name of **DEV-0322**.


News of the attacks first surfaced on Friday, July 9, when embattled software provider SolarWinds released a [security update](https://www.solarwinds.com/trust-center/security-advisories/cve-2021-35211) to patch a zero-day vulnerability in its Serv-U technology that was being exploited in the wild.


At the time, SolarWinds said it learned of the zero-day (CVE-2021-35211) and the ongoing attacks from Microsoft but did not release any additional details beyond the Serv-U patch (v15.2.3 HF2).


Initially, Microsoft declined to comment following the SolarWinds patch in emails sent by *The Record*.


However, following pressure from the cyber-security community on Tuesday, which kept asking the OS maker for additional details so they could deploy countermeasures to detect and block ongoing attacks, Microsoft published a [blog post](https://www.microsoft.com/security/blog/2021/07/13/microsoft-discovers-threat-actor-targeting-solarwinds-serv-u-software-with-0-day-exploit/) today with an in-depth description of the zero-day’s entire exploitation chain.


According to the report, Microsoft said it discovered the DEV-0322 attacks after its Defender antivirus began detecting malicious processes spawning from Serv-U’s main application, which eventually led its security team to investigate and discover the zero-day and the ongoing attacks.


### DEV-0322 previously targeted the US Defense Industrial Base


While Microsoft couldn’t comment on the targets of this most recent campaign, the OS maker said that past DEV-0322 attacks had targeted software companies and entities in the US Defense Industrial Base Sector.


These attacks also mark the second time that a Chinese hacking group has abused SolarWinds software to breach corporate and government networks.


[Back in December 2020](https://therecord.media/attacks-on-solarwinds-servers-also-linked-to-chinese-threat-actor/), while the Russian-orchestrated SolarWinds supply chain attack was coming to light, Chinese hacking groups were also busy abusing the CVE-2020-10148 vulnerability to install web shells on SolarWinds Orion IT monitoring platforms.


Because the CVE-2020-10148 came to light during the more broad supply chain investigation, it took security firms some time to separate the two incidents and eventually make the connection to a Chinese group tracked as [Spiral](https://www.secureworks.com/blog/supernova-web-shell-deployment-linked-to-spiral-threat-group).


All in all, companies that run SolarWinds Serv-U file transfer servers can protect themselves against DEV-022 attacks by either installing the company’s patch or by disabling SSH access to the server, which is how the group is compromising servers.


According to a [Censys search query](https://search.censys.io/search?resource=hosts&q=services.banner%3A+%22SSH-2.0-Serv-U*%22+AND+services.service_name%3A+%22SSH%22), there are more than 8,200 SolarWinds Serv-U systems exposing their SSH port online, a number that had remained steady since last week, when the patches were released.





#### Tags:
[[SolarWinds]] [[Microsoft]] [[Serv-U]] [[DEV-0322]] [[zero-day]] [[The Record]]
