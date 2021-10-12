# New SnapMC group extorts companies after short 30-minute hacks
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/new-snapmc-group-extorts-companies-after-short-30-minute-hacks/)
+ Date: October 12, 2021
+ Author: Catalin Cimpanu


## Article:
![New SnapMC group extorts companies after short 30-minute hacks](https://therecord.media/wp-content/uploads/2021/10/hoodie-hacker.jpg)

Security researchers have discovered a new threat actor that carries out lightning-fast hacks, typically under 30 minutes, steals a company’s files, and then extorts the victim with threats to leak the data online or to media outlets unless a ransom payment is made within a few days.


Discovered by Dutch security firm Fox-IT, the company named the group **SnapMC** because of its short-lived intrusions and the use of a tool called *mc.exe* for data exfiltration.


Fox-IT researchers said the group typically breaches company networks via vulnerabilities in web-facing software, with several intrusions linked to the exploitation of [CVE-2019-18935](https://nvd.nist.gov/vuln/detail/CVE-2019-18935), a vulnerability in a UI component for the Telerik ASP.NET framework.


Once inside, the group moves fast to collect data from local systems and typically doesn’t spend more than 30 minutes on a hacked network.


Following a successful exfiltration, SnapMC operators send emails to the hacked company with a list of the stolen files as evidence.


Companies are usually given 24 hours to respond to the email and another 72 hours to negotiate a ransom payment.


To coerce companies to begin negotiations, SnapMC publishes small portions of the data, threatens to leak the files online, threatens to tell media outlets about the hack, or notify a victim’s customers about the breach.


Fox-IT said that during the time they tracked the group, they had not observed it deploying ransomware, despite having access to a victim’s internal network, with the group focusing solely on data exfiltration and the subsequent extortion.


Furthermore, Fox-IT said they also haven’t been able to link the SnapMC group to any of the current “leak markets,” which are web portals used to leak data from ongoing or failed extortion attempts.


Currently active leak and data auction sites include the likes of:


* Arvin Club
* Bonaci Group
* Dark Leak Market
* File Leaks
* Karakurt
* LockData
* Marketo
* XING


![LockData-auction](https://www-therecord.recfut.com/wp-content/uploads/2021/10/LockData-auction-1024x669.png)Image: The Record
Earlier today, Fox-IT released a [technical report](https://blog.fox-it.com/2021/10/11/snapmc-skips-ransomware-steals-data/) containing the tools and techniques commonly used by SnapMC in their intrusions — in the hopes that companies deploy proper defenses.


One of the simplest solutions to block attacks, recommended in the Fox-IT report, was to deploy a web firewall in front of Telerik-based applications since this has been proven to block SnapMC’s initial compromise attempts.





#### Tags:
[[SnapMC]] [[Fox-IT]] [[The Record]]
