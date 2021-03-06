# New iLOBleed Rootkit Targets HP Integrated Lights-Out
### iLOBleed rootkit is active since 2020, targeting servers with sneaky and persistent attacks that evade detection, resist firmware upgrades.

## Information:
+ Source: Latest Hacking News
+ Link: https://latesthackingnews.com/2022/01/02/new-ilobleed-rootkit-targets-hp-integrated-lights-out/
+ Date: 2022-01-02
+ Author: Abeerah Hashim


## Article:
![Article Image](https://latesthackingnews.com/wp-content/uploads/2021/12/chip-processor.jpg)
 Researchers have found a new malware targeting HP Integrated Lights-Out (iLO) devices. Dubbed iLOBleed, the rootkit is already running active campaigns targeting numerous organizations.

 iLOBleed Rootkit Found Active In The Wild
-----------------------------------------

 HP’s Integrated Lights-Out (iLO) technology is a remote server management processor exhibiting separate network connectivity. The processors empower devices like HP ProLiant and Blade servers for remote management. iLO allows full access to the target servers, including powering the server on and off.

 According to security researchers from Amnpardaz, an Iranian-based security firm, a new rootkit, identified as “iLOBleed” is actively targeting HP iLO servers. As observed, this rootkit sneakily resides within the iLO and remains undetected (and unaffected) by firmware upgrades.

 Regarding how the malware reaches a device, the researchers explained in their [report](https://threats.amnpardaz.com/en/2021/12/28/implant-arm-ilobleed-a/),

 
> Accessing and infecting iLO is not only possible through the iLO network port, but also through the system administrator or root access to the main operating system. This means that if an intruder has access to a user with administrator/root privileges on the main operating system installed on the server, it can – without needing any further authentication – directly communicate with the iLO, and infect it if it is vulnerable.
> 
> 

 The researchers discovered this malware on an infected server where the attackers intended to wipe the server disks. What made iLOBleed distinct from other wiper [malware was its persistence](https://latesthackingnews.com/2020/06/14/facebook-messenger-app-vulnerability-allowed-persistent-malware-attacks/) on the server (instead of the hit-and-run model). They have shared the detailed technical analysis of the rootkit in their report.

 Preventing iLOBleed
-------------------

 Aside from its sneaky administrative and data-wiping functionalities, iLOBleed is also a potent threat since it ditches with firmware updates. Although, the latest HO iLO 5 firmware with the G10 server series resists this attack.

 However, since the earlier server series [remain vulnerable](https://latesthackingnews.com/2021/02/18/shareit-android-app-vulnerabilities-remain-unfixed-for-three-months/), an infected server might fail the firmware upgrade as the malware would resist it while displaying fake upgrade alerts.

 Nonetheless, HP has recently changed the iLO UI, thus making it easy for the users to spot any fake upgrades.

 Besides, the researchers have advised updating the iLO firmware version, disabling downgrades on the servers, and using iLO scanners to detect any bugs and malware threats.

   


## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]] [[action.malware.name=Wiper]]

#### Location:
[[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ilo]] [[Malware]] [[Ilobleed]] [[Rootkit]] [[Latest Hacking News]]

