# Chinese espionage group deploys new rootkit compatible with Windows 10 systems
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/chinese-espionage-group-deploys-new-rootkit-compatible-with-windows-10-systems/)
+ Date: September 30, 2021
+ Author: Catalin Cimpanu


## Article:
![Chinese espionage group deploys new rootkit compatible with Windows 10 systems](https://therecord.media/wp-content/uploads/2021/09/China.jpg)

At the SAS 2021 security conference today, analysts from security firm Kaspersky Lab have published details about a new Chinese cyber-espionage group that has been targeting high-profile entities across South East Asia since at least July 2020.


Named **GhostEmperor**, Kaspersky said the group uses highly sophisticated tools and is often focused on gaining and keeping long-term access to its victims through the use of a powerful rootkit that can even work on the latest versions of Windows 10 operating systems.


“We observed that the underlying actor managed to remain under the radar for months,” Kaspersky researchers explained today.


The entry point for GhostEmperor’s hacks were public-facing servers. Kaspersky believes the group used exploits for Apache, Oracle, and Microsoft Exchange servers to breach a target’s perimeter network and then pivoted to more sensitive systems inside the victim’s network.


According to a technical report [[PDF](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2021/09/30094337/GhostEmperor_technical-details_PDF_eng.pdf)] released during the conference today, GhostEmperor used an assortment of different scripts and tools to deploy backdoors inside a victim’s network.


![GhostEmperor](https://www-therecord.recfut.com/wp-content/uploads/2021/09/Ghost_Emperor_04.png)Image: Kaspersky
This backdoor (an in-memory implant) was then used to download and run [Cheat Engine](https://www.cheatengine.org/), a tool used by online gamers to introduce cheats in their favorite video games.


Kaspersky said GhostEmperor used Cheat Engine’s powerful drivers to bypass the Windows PatchGuard security feature and install a rootkit inside the victim’s Windows OS.


Called **Demodex**, researchers said the rootkit was extremely advanced and allowed the group to maintain access to the victim’s device even after OS reinstalls and even on systems running recent versions of the Windows 10 OS.


![GhostEmperor Demodex](https://www-therecord.recfut.com/wp-content/uploads/2021/09/Ghost_Emperor_06.png)Image: Kaspersky
But this wasn’t GhostEmperor’s only trick. Kaspersky also noted that the group’s malware was full of “a broad set of unusual and sophisticated anti-forensic and anti-analysis techniques” that tried to prevent or hinder security researchers trying to analyze their malware.


In addition, GhostEmperor used another clever trick that consisted in modifying the communications between infected hosts to its command and control servers by re-packaging data as fake multimedia formats.


Security apps that spotted traffic from GhostEmperor’s malware would have normally classified it as RIFF, JPEG, or PNG files hosted on an Amazon server, researchers explained.


While Kaspersky did not reveal the name of the group’s targets, they said GhostEmperor went after governmental entities and telecommunication companies across South East Asia (Malaysia, Thailand, Vietnam, and Indonesia), with outliers in Egypt, Afghanistan, and Ethiopia.





#### Tags:
[[Kaspersky]] [[Windows]] [[victim’s]] [[GhostEmperor]] [[rootkit]] [[GhostEmperor’s]] [[The Record]]
