# Log4j: Mirai botnet found targeting ZyXEL networking devices | ZDNet
### A report explained that the Log4j vulnerability is being used to infect and assist in the proliferation of malware used by the Mirai botnet.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/log4j-mirai-ddos-botnet-targeting-zyxel-networking-devices/
+ Date: 2022-01-24 18:26:00
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/ae87ac070a5b3d088fcafae17c131be3067edb71/2022/01/10/d0db5c59-423a-428b-a098-a043e397f51b/shutterstock-2090832775.jpg?width=770&height=578&fit=crop&auto=webp)

An Akamai researcher has discovered an attempt to use Log4j vulnerabilities in ZyXEL networking devices to "infect and assist in the proliferation of malware used by the Mirai botnet."

Larry Cashdollar, a member of the Security Incident Response Team at Akamai Technologies, [explained](https://www.akamai.com/blog/security/mirai-botnet-abusing-log4j-vulnerability) that Zyxel may have been specifically targeted because they [published a blog](https://www.zyxel.com/us/en/support/Zyxel_security_advisory_for_Apache_Log4j_RCE_vulnerability.shtml) noting they were impacted by the Log4j vulnerability. 


"The first sample I examined contained functions to scan for other vulnerable devices," Cashdollar wrote in an [Akamai blog post](https://www.akamai.com/blog/security/mirai-botnet-abusing-log4j-vulnerability).

"The second sample... did contain the standard Mirai attack functions," he added. "It appears the... attack vectors had been removed in favor of Log4j exploitation. Based on the attack function names and their instructions, I believe this sample is part of the Mirai malware family."

Cashdollar concluded his blog post by writing that "if you have automated string extraction utilities for malware samples that log to a vulnerable Log4j instance, this payload could execute." 

Zyxel [released](https://www.zyxel.com/us/en/support/Zyxel_security_advisory_for_Apache_Log4j_RCE_vulnerability.shtml) a security advisory about the issue, noting that it is aware of the vulnerability and that it only affects the NetAtlas Element Management System line of products. 

"After a thorough investigation, we've identified only one vulnerable product that is within its warranty and support period, and we will release a hotfix and a patch to address the issue, as shown in the table below," they wrote.






Zyxel said a hotfix was released on December 20 and urged those in need to contact them for the file. A patch will be available by the end of February. 

Vulcan Cyber co-founder Tal Morgenstern said that by design, the Zyxel NetAtlas Element Management System provides extensive control of Zyxel enterprise network infrastructure and the services that run on it. 

In the right hands, the task automation provided by systems management tools allows IT and network operators to keep things running uninterrupted at massive scale, Morgenstern explained. In the wrong hands, threat actors can do extensive damage quickly to the vulnerable networks they get access to. 

"Unfortunately, vulnerabilities in systems and network management software tools are trending. SolarWinds, Open Management Infrastructure (OMI), Salt, VMware, and Zoho ManageEngine are just a few we've seen in the last few months. Considering the amount of access and control these tools have, it is critical IT security teams take immediate steps to fully mitigate the notable risk these vulnerable tools present to the companies that use them," Morgenstern said. 

Bugcrowd founder Casey Ellis told ZDNet that this is one of the many vendors which include Log4j as an open-source library and that the attack "is a demonstration of the ubiquity of the Log4j library and the attack surface created as a result."

"It's one of the reasons the security community went a bit bananas about this issue when it first dropped, and I'd expect to see similar advisories from other vendors for some time to come," Ellis said. 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Zyxel]] [[Malware]] [[Mirai]] [[Blog]] [[ZDNet]]

