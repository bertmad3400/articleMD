# Threat actor uses HP iLO rootkit to wipe servers
### An Iranian cyber-security firm said it discovered a first-of-its-kind rootkit that hides inside the firmware of HP iLO devices and which has been used in real-world attacks to wipe servers of Iranian organizations.

## Information:
+ Source: The Record
+ Link: https://therecord.media/threat-actor-uses-hp-ilo-rootkit-to-wipe-servers/
+ Date: 2021-12-29T12:01:11+00:00
+ Author: Catalin Cimpanu


## Article:
![Article Image](https://therecord.media/wp-content/uploads/2021/12/HP-iLO.png)

An Iranian cyber-security firm said it discovered a first-of-its-kind rootkit that hides inside the firmware of HP iLO devices and which has been used in real-world attacks to wipe servers of Iranian organizations.


Named **iLOBleed**, the rootkit was discovered by Tehran-based security firm Amnpardaz and detailed in a [report](https://threats.amnpardaz.com/en/2021/12/28/implant-arm-ilobleed-a/) released on Tuesday.


According to the company, iLOBleed targets [HP iLO](https://www.hpe.com/us/en/servers/integrated-lights-out-ilo.html) (Integrated Lights-Out), a hardware device that can be added to servers or workstations as an add-on board.


iLO devices come with their own processor unit, storage space, RAM, and network card and run separately from any local operating system.


Their primary role is to provide a way for system administrators to connect to remote systems, even when these systems are turned off, and perform maintenance operations, such as updating firmware, installing security updates, or reinstalling faulty systems.


These features have made iLO cards one of the most successful enterprise products used for the management of remote computer fleets and for automating the deployment of OS images in many modern data centers.


#### First iLOBleed attacks spotted in 2020


But Amnpardaz said that since 2020, it investigated several incidents where a mysterious threat actor compromised targets and hid inside iLO as a way to survive OS reinstalls and maintain persistence inside the victim’s network.


To avoid detection, researchers said the attacker disguised the iLOBleed rootkit as a module for the iLO firmware itself, and the attacker also crafted a fake update UI to show to system administrators when they tried to update the iLO firmware.


“The malware tries hard at simulating the upgrade process and goes to difficulties of displaying fake ‘upgraded’ versions in the web UI of the iLO and other places, but there is a catch: HP has changed the UI of the iLO considerably,” the Amnpardaz team said today.


![HP-iLO-fake-update](https://therecord.media/wp-content/uploads/2021/12/HP-iLO-fake-update.png)Image: Amnpardaz
But even if the rootkit provided full control over infected hosts, the attackers appear to have only used it to wipe infected systems as part of some sort of data wiping operation.


“When our security analysis team discovered the malware, the attackers had decided to wipe the server’s disks and completely hide their tracks,” the Amnpardaz team explained.


“Interestingly, the attackers were not satisfied with one-time destruction and set the malware to repeatedly perform the data destruction at intervals. Maybe they thought that this way if the system administrator reinstalls the operating system, the entire hard drive will be destroyed again after a while. Clearly, they didn’t think their malware will be found.”


#### Threat actor behind attacks remains unnamed


Both Amnpardaz and members of the cybersecurity community have described the iLO rootkit as state-of-the-art and likely the work of a very advanced threat actor. The actor itself was not identified in the Amnpardaz report nor in any online conversations.


“Naturally, the cost of performing such an attack puts it in the category of APTs,” the Iranian security firm said on Tuesday.


“But using such powerful and costly malware for something like data destruction, a task that increases the likelihood of malware being detected, seems to be a blatant mistake on the part of these crooks.”


While Amnpardaz’s report exposed the existence of this malware, questions still remain about how it was initially deployed. Current standing theories include scenarios where the attacker entered a victim’s network through other channels and then deployed iLOBleed as a backdoor (persistence mechanism), either by exploiting vulnerabilities in old iLO firmware or by expanding access from an infected host to its iLO card, if present.


As Amnpardaz also pointed out in their report, the discovery of iLOBleed is a breakthrough and an achievement, primarily because there are very few security tools and products capable of detecting malware activity at iLO’s level—a component that operates deeper than the OS itself, let alone security products.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.city.name=Tehran]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ilo]] [[Amnpardaz]] [[Malware]] [[Ilobleed]] [[Rootkit]] [[The Record]]

