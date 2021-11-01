# Cring ransomware continues assault on industrial organizations with aging applications, VPNs
### A Sophos report attributed a recent Cring attack to hackers in Belarus and Ukraine.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/cring-ransomware-continues-assault-on-coldfusion-servers-vpns/)
+ Date: November 1, 2021
+ Author: Jonathan Greig


## Article:
Unknown

The Cring ransomware group continues to make a name for itself through attacks on aging ColdFusion servers and VPNs after emerging earlier this year. 


Experts like Digital Shadows Sean Nikkel told ZDNet that what makes Cring interesting is that so far, they appear to specialize in using older vulnerabilities in their attacks. 

"In a previous incident, Cring operators exploited a two-year-old FortiGate VPN vulnerability to target end-of-life Microsoft and Adobe applications. This should be a wake-up call for system owners everywhere who are using end-of-life or otherwise unsupported systems that are exposed to the internet at large," Nikkel said. 

"While Cring has operators that have used Mimikatz on systems to gain credentials, there's also evidence of native Windows process usage, which potentially blends in with otherwise legitimate activity. This can often make it more tricky for network hunters and defenders to see anything malicious until it's too late. This and previous attacks also showcase the continued adoption and use of Cobalt Strike beacons by various threat actors, which often make the post-exploit phase easier for attackers to manage."

Sophos [released a report](https://news.sophos.com/en-us/2021/09/21/cring-ransomware-group-exploits-ancient-coldfusion-server/?cmp=30728) in September highlighting one specific incident where Cring operators exploited a vulnerability in an 11-year-old installation of Adobe ColdFusion 9 to take control of a ColdFusion server remotely. 

Sophos was able to tie the group using the Cring ransomware to hackers in Belarus and Ukraine that used automated tools to break into the servers of an unnamed company in the services sector. 

The hackers used their automated tools to browse 9,000 pathways into the company's systems in 75 seconds. Three minutes later, they were able to exploit a vulnerability in the outdated Adobe program that allowed them to get their hands on files from servers that weren't supposed to be publicly available. They grabbed a file called "password properties," and wrote garbled code on top of their "footprints" to cover their tracks. Then, they waited two and a half days, came back into the company's network, gave themselves Admin privileges and posted a sardonic ransom note. 






The hackers were also able to get access to timesheets and accounting data for payroll before breaching the internet-facing server in minutes and executing the ransomware 79 hours later.

Andrew Brandt, principal researcher at Sophos, said the Cring ransomware isn't new, but it's uncommon. 

"In the incident we researched, the target was a services company, and all it took to break in was one internet-facing machine running old, out-of-date and unpatched software. The surprising thing is that this server was in active daily use. Often the most vulnerable devices are inactive or ghost machines, either forgotten about or overlooked when it comes to patching and upgrades," Brandt said. 

"But, regardless of what the status is -- in use or inactive -- unpatched internet-facing servers or other devices are prime targets for cyberattackers scanning a company's attack surface for vulnerable entry points. This is a stark reminder that IT administrators benefit from having an accurate inventory of all their connected assets and cannot leave out-of-date critical business systems facing the public internet. If organizations have these devices anywhere on their network, they can be sure that cyberattackers will be attracted to them. Don't make life easy for cybercriminals."

The attack identified by Sophos found that the hackers scanned the victim's website with automated tools and gained easy access once they found the unpatched ColdFusion on a server. 

Sophos researchers noted that the Cring operators "used fairly sophisticated techniques to conceal their files, inject code into memory, and cover their tracks by over-writing files with garbled data or deleting logs and other artifacts that threat hunters could use in an investigation." 

After getting around security features, the hackers left a note saying, "ready to leak in case we can not make a good deal."

Pavel Kuznetsov, deputy managing director for cybersecurity technologies for Positive Technologies, told ZDNet that Cring operators are routinely interested in conducting sufficiently deep reconnaissance inside the network before direct infection by their ransomware. 

"Among the targets are often the infrastructures of industrial organizations. Moreover, ICS segments are selected for infection by the ransomware, obviously with the aim of endangering the associated processes (production, etc.)," Kuznetsov said. 

Positive Technologies head of malware detection Alexey Vishnyakov added that the group gets its primary consolidation through the exploitation of 1-day vulnerabilities in services at the perimeter of the organization like web servers, VPN solutions and more, either through buying access from intermediaries on shadow forums or other methods. 

"The group uses Mimikatz to move inside an organization. It uses the Cobalt Strike pentesting tool to secure it within the network to the hosts. After taking over the network, it downloads and distributes the ransomware," Vishnyakov said. 

Vishnyakov echoed Kuznetsov's analysis that Cring was focused on attacking industrial companies, hoping to force suspensions of production processes and financial losses as a way to push victims into paying ransoms. 

"It is far from the first and won't be the last criminal group that acts according to the scheme of compromising an unpatched vulnerability and encrypting data," Vishnyakov said. 

"Particularly dangerous is a series of successful penetrations and production infections. Risks include not only blackmail and financial consequences -- these attacks could also possibly lead to accidents and death.





#### Tags:
[[Cring]] [[said.]] [[ransomware]] [[ColdFusion]] [[Vishnyakov]] [[Sophos]] [[network,]] [[internet-facing]] [[ZDNet]]
