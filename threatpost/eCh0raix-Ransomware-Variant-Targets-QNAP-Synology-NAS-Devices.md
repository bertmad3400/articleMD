# eCh0raix Ransomware Variant Targets QNAP, Synology NAS Devices
### Some bad actors are honing tools to go after small fry: This variant was refined to target not one, but two vendors’ devices that are common in SOHO setups.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168516)
+ Date: August 10, 2021  1:22 pm
+ Author: Lisa Vaas


## Article:
Operators of the nearly-year-old eCh0raix ransomware strain that’s been used to target QNAP and Synology network-attached storage (NAS) devices in past, separate campaigns have, gotten more efficient. According to researchers, both have put out a new variant that can target either vendors’ devices in a single campaign.


In a [report](https://unit42.paloaltonetworks.com/ech0raix-ransomware-soho/) published Tuesday, Palo Alto Network Unit 42 researchers said the new variant of eCh0raix exploits a critical bug, [CVE-2021-28799](https://nvd.nist.gov/vuln/detail/CVE-2021-28799) – an improper authorization vulnerability that gives attackers access to hard-coded credentials so as to plant a backdoor account – in the Hybrid Backup Sync (HBS 3) software on QNAP’s NAS devices.


HBS is used for backup, restoration and synchronization between local, remote and cloud storage spaces. On April 21, users of devices marketed by the Taiwanese vendor – Quality Network Appliance Provider (QNAP) – [began to report attacks](https://www.qnap.com/static/landing/2021/qlocker/response/da-dk/) that, it turned out, abused this same flaw. Hundreds of users were extorted, as BleepingComputer reported at the time.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/)


On June 21, Unit 42 spotted an attack targeting QNAP HBS3 with an exploit of CVE-2021-28799. It’s not the first time this bug was exploited to deliver Qlocker, researchers said, but it’s the first time it’s been pried open to deliver [eCh0raix](https://malpedia.caad.fkie.fraunhofer.de/details/elf.qnapcrypt), aka [QNAPCrypt ransomware](https://threatpost.com/linux-ransomware-nas-servers/146441/): an unusual Linux ransomware that was used to target QNAP NAS servers in 2019.


Researchers shared an image of the payload – shown below – which was still live at the time the report was published on Tuesday. “The attack tried to utilize a hard-coded session ID ‘jisoosocoolhbsmgnt’ to bypass authentication and execute a command on the device, aiming to fetch malware from the remote server 64[.]42[.]152[.]46 and run it on the victim device,” Unit 42 said.


The eCh0raix operators have branched out: Payload analysis shows that they’ve gone beyond their typical targeting of QNAP devices to also target Synology NAS devices, thereby enabling the ransomware to ensnare both vendors’ devices, Unit 42 researchers found.


Timeline
--------


As far as unit 42 can determine, there’s been no analysis yet of malware samples that would show eCh0raix ransomware targeting Synology devices before this. “Instances of Synology devices infected by eCh0raix have been reported from as far back as [2019,](https://www.synology-forum.nl/firmware-algemeen/ech0raix-ransomware/) but the only [previous research](https://www.anomali.com/blog/threat-actors-utilizing-ech0raix-ransomware-change-nas-targeting) connecting the Synology attacks to eCh0raix actors is based on decryptors that were found,” they elaborated.


The first time that Unit 42 researchers saw this dual-vendor variant was September 2020. Maybe the combined variant was authored at that time and the attackers had separate code bases to target the vendors’ devices in separate campaigns before that, they suggested: a hypothesis that’s confirmed by the new variant’s project name, as revealed in compilation paths in GoLang binaries: “rct\_cryptor\_universal” (/home/dev/GoglandProjects/src/rct\_cryptor\_universal).


“Prior samples of eCh0raix use the project name qnap\_crypt\_worker,” researchers pointed out. Between June and September 2020, they did see other eCh0raix samples using that rct\_cryptor\_universal project name, but September 2020 was when they first saw a full-blown sample with two separate code flows.


Nearly a Quarter-Million Vulnerable NAS Devices
-----------------------------------------------


It looks like eCh0raix is virulent: Victims have been posting their tales on forums, claiming to have paid ransoms of bitcoin valued at about $500 at the time, as recently as June 16, 2021.



> Short sad story, looking for help. I was attacked too, negotiated a bit and paid the ransom (0.0192 BTC). I received the decryptor files. There is no real paw and I don’t know how to follow the below instructions that they put on the Tor page. I uploaded the decryptor but the command doesn’t return anything
> 
> 
> — Source: post from “kapuvacante” on BleepingComputer forum
> 
> 


Unit 42 researchers estimated that there are about 240,000 internet-connected QNAP NAS devices and only about 3,500 Synology NAS devices, meaning that adding Synology to its hit list didn’t significantly boost the ransomware’s attack surface. Still, a quarter-million potential targets is nothing to sneeze at.


Why Nickel-and-Dime SOHO users?
-------------------------------


They’re going after small fry because small office/home office (SOHO) NAS devices can be used “as a stepping stone in supply chain attacks on large enterprises that can generate huge ransoms,” Unit 42 suggested.


“We’re releasing our findings about this new variant of eCh0raix to raise awareness of the ongoing threats to the SOHO and small business sectors,” the researchers explained. “Coverage of the ransomware crisis tends to focus on threats to large enterprises and government agencies, which are facing increasingly aggressive and disruptive ransomware attacks. However, the SOHO and small business sectors can contain a large attack surface for threat actors.”


Another thing that makes SOHO users tempting targets is that they don’t have the heavy-duty watchdogs that protect enterprises, Unit 42 continued: “SOHO users typically do not employ dedicated IT or security professionals, which makes them less prepared to block ransomware attacks than larger organizations.”


Alec Alvarado, Threat Intelligence Team Lead at digital risk protection provider Digital Shadows, told Threatpost on Tuesday that large organizations getting hit with ransomware gets most of the big headlines, but that “threats of ransomware at the individual and small business levels are still widely prevalent.”


Cybercriminals are “looking for the low-hanging fruit to cast as wide of a net as possible and increase their potential return on investment,” he commented. “NAS devices provide ample opportunity for attacks at the individual level and could be used for extortion or lateral movement into larger networks. The increase in work-from-home models has created a BYOD nightmare for defenders, and NAS devices are included in that. Threat actors, much like water, are trying to find the path of least resistance, and NAS devices could prove a good option for a foot in the door.”


Cover Your NAS
--------------


Unit 42 passed along these best practices for protecting home offices from ransomware attacks:


About Those Hard-Coded Credentials
----------------------------------


The big “if only”: If only there weren’t any hard-coded credential to begin with. Alvarado noted that the new variant’s exploit of a hard-coded credential is just the latest example of why hard-coding device credentials is widely seen as an unsafe practice that’s resulted in compromise on multiple occasions.


“Once these devices are distributed, it is only a matter of time for threat actors to discover the hard-coded credentials and use the information maliciously,” he said via email. “Then it is even more challenging to patch these devices, as the hard-coded credentials are integral for the device to operate. Furthermore, users of these devices aren’t likely to have the ability to disable the function or change the password, let alone they are likely unaware the hard-coded credentials are in use.”


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[eCh0raix]] [[ransomware]] [[NAS]] [[Synology]] [[hard-coded]] [[QNAP]] [[devices,]] [[that’s]] [[vendors’]] [[ThreatPost]]
