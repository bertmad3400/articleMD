# Cisco says it will not release software update for critical 0-day in EOL VPN routers
### Cisco said there are no workarounds for the vulnerability.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/cisco-not-planning-to-fix-critical-0-day-rce-vulnerability-in-eol-vpn-routers/)
+ Date: August 27, 2021 -- 20:22 GMT (21:22 BST)
+ Author: Jonathan Greig


## Article:
Unknown

Cisco [announced recently](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cisco-sb-rv-overflow-htpymMB5) that it will not be releasing software updates for a vulnerability with its Universal Plug-and-Play (UPnP) service in Cisco Small Business RV110W, RV130, RV130W, and RV215W Routers.

The vulnerability allows unauthenticated, remote attacker to execute arbitrary code or cause an affected device to restart unexpectedly, resulting in a denial of service (DoS) condition.

"This vulnerability is due to improper validation of incoming UPnP traffic. An attacker could exploit this vulnerability by sending a crafted UPnP request to an affected device. A successful exploit could allow the attacker to execute arbitrary code as the root user on the underlying operating system or cause the device to reload, resulting in a DoS condition," Cisco said in a statement. 

"Cisco has not released software updates that address this vulnerability. There are no workarounds that address this vulnerability."

The vulnerability only affects the RV Series Routers if they have UPnP configured but the UPnP service is enabled by default on LAN interfaces and disabled by default on WAN interfaces.

The company explained that to figure out if the UPnP feature is enabled on the LAN interface of a device, users should open the web-based management interface and navigate to Basic Settings > UPnP. If the Disable check box is unchecked, UPnP is enabled on the device.

Cisco said that while disabling the affected feature has been proven successful in some test environments, customers should "determine the applicability and effectiveness in their own environment and under their own use conditions." 






They also warned that any workaround or mitigation might harm how their network functions or performs. Cisco urged customers to migrate to the Cisco Small Business RV132W, RV160, or RV160W Routers.

The vulnerability and Cisco's notice caused a minor stir among IT leaders, some of whom said exploiting it requires the threat actor to have access to an internal network, which can be gained easily through a phishing email or other methods. 

Jake Williams, CTO at BreachQuest, added that once inside, a threat actor could use this vulnerability to easily take control of the device using an exploit. 

"The vulnerable devices are widely deployed in smaller business environments. Some larger organizations also use the devices for remote offices. The vulnerability lies in uPnP, which is intended to allow dynamic reconfiguration of firewalls for external services that need to pass traffic inbound from the Internet," Williams told ZDNet. 

"While uPnP is an extremely useful feature for home users, it has no place in business environments. Cisco likely leaves the uPnP feature enabled on its small business product line because those environments are less likely to have dedicated support staff who can reconfigure a firewall as needed for a product. Staff in these environments need everything to 'just work.' In the security space, we must remember that every feature is also additional attack surface waiting to be exploited." 

Williams added that even without the vulnerability, if uPnP is enabled, threat actors inside the environment can use it to open ports on the firewall, allowing in dangerous traffic from the Internet. 

"Because the vulnerable devices are almost exclusively used in small business environments, with few dedicated technical support staff, they are almost never updated," he noted.

Vulcan Cyber CEO Yaniv Bar-Dayan said UPnP is a much-maligned service used in the majority of internet connected devices, estimating that more than 75% of routers have UPnP enabled. 

While Cisco's Product Security Incident Response Team said it was not aware of any malicious use of this vulnerability so far, Bar-Dayan said UPnP has been used by hackers to take control of everything from IP cameras to enterprise network infrastructure. 

Other experts, like nVisium senior application security consultant Zach Varnell, added that it's extremely common for the devices to rarely -- or never -- receive updates. 

"Users tend to want to leave well enough alone and not touch a device that's been working well -- including when it needs important updates. Many times, users also take advantage of plug-and-play functionality, so they do very little or zero configuration changes, leaving the device at its default status and ultimately, vulnerable," Varnell said. 

New Net Technologies global vice president of security research Dirk Schrader added that while UPnP is one of the least known utilities to average consumers, it is used broadly in SOHO networking devices such as DSL or cable router, WLAN devices, even in printers. 

"UPnP is present in almost all home networking devices and is used by device to find other networked devices. It has been targeted before, and one of the big botnets, Mirai, relied heavily on UPnP. Given that the named Cisco devices are placed in the SOHO and SMB segment, the owners are most likely not aware of UPnP and what it does," Schrader said. 

"That and the fact that no workaround or patch are available yet is a quite dangerous combination, as the installed base is certainly not small. Hope can be placed on the fact the -- by default -- UPnP is not enabled on the WAN interfaces of the affected Cisco device, only on the LAN side. As consumers are not likely to change that, for this vulnerability to be exploited, attackers seem to need a different, already established footprint within the LAN. But attackers will check the vulnerability and see what else can be done with it."





#### Tags:
[[UPnP]] [[uPnP]] [[ZDNet]]
