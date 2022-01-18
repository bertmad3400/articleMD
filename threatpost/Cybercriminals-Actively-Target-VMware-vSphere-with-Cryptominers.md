# Cybercriminals Actively Target VMware vSphere with Cryptominers
### VMware's container-based application development environment has become attractive to cyberattackers.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177722
+ Date: 2022-01-18T19:33:13+00:00
+ Author: Becky Bracken


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/17145342/cloud-e1629226435519.jpg)

Organizations running sophisticated virtual networks with VMware’s vSphere service are actively being targeted by cryptojackers, who have figured out how to inject the XMRig commercial cryptominer into the environment, undetected.


Uptycs’ Siddharth Sharma has released research showing threat actors are using malicious shell scripts to make modifications and run the [cryptominer on vSphere virtual networks](https://www.uptycs.com/blog/cryptominer-campaign-targeting-vmware-vsphere-services-for-coin-mining).


“Cryptojacking campaigns mostly target the systems having high-end resources,” Sharma pointed out. “In this campaign as we saw the attackers tried to register the XMRig miner itself as a service (daemon), which runs whenever the system gets rebooted.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


To avoid detection, the script also downloads a user-mode rootkit from the command-and-control server (C2), the report added.


“The shell script also contains commands which download the miner, the config file and the user mode rootkit from the attacker’s web server,” the report explained. “The attackers used [the] wget utility to fetch the malicious components and chmod utility to make the components executable.”


The report said the rootkit gets saved as “libload.so” and the script modifies [vSphere](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vcenter.install.doc/GUID-A71D7F56-6F47-43AB-9C4E-BAA89310F295.html) to run the XMRig cryptominer.


After the [cryptominer is dropped](https://threatpost.com/cryptomining-attack-exploits-docker-api-misconfiguration-since-2019/177299/), the script reloads the service to get the miner started, Sharma explained. The report also reported the attacker’s wallet has been paid 8.942 XMR, the report said, or about $1,790 as of press time.


**VMware Services Under Attack**
--------------------------------


VMware services have been beleaguered by recent security issues.


The new year kicked off with a high-severity [bug found in VMWare’s Cloud Foundation](https://threatpost.com/unpatched-vmware-bug-hypervisor-takeover/177428/), ESXi, Fusion and Workstation platforms, which opened the door for a hypervisor takeover of an organization’s entire virtualized environment.


And just days ago [VMWare’s Horizon servers](https://www.huntress.com/blog/cybersecurity-advisory-vmware-horizon-servers-actively-being-hit-with-cobalt-strike) with Log4Shell vulnerabilities were observed under active Cobalt Strike attack by researchers at Huntress after the U.K.’s National Health Service were targeted on Jan 5.


Sharma advises security teams running VMware services to look for unusual network activity to detect the [cryptominer](https://threatpost.com/spider-man-no-way-home-download-installs-cryptominer/177254/), as well as other attacks.


“In the past we have seen highly sophisticated groups targeting vulnerable VMware services,” Sharma said. “Hence it becomes really important to monitor the suspicious processes, events and network traffic spawned on the execution of any untrusted shell script.”


***Password******Reset:***[**On-Demand Event**](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)***:****Fortify 2022 with a password-security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the new password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken.*[**Register & stream this FREE session today**](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)*– sponsored by Specops Software.*





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Utility]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Vmware]] [[Cryptominer]] [[Sharma]] [[Vsphere]] [[Xmrig]] [[Rootkit]] [[ThreatPost]]

