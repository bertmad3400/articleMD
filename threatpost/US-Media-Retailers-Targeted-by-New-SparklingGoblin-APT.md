# US Media, Retailers Targeted by New SparklingGoblin APT
### The new APT uses an undocumented backdoor to infiltrate the education, retail and government sectors. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168928)
+ Date: August 25, 2021  11:10 am
+ Author: Tom Spring


## Article:
An emerging international cybergang is broadening its targets to include North American media firms, universities and one computer retailer. The advanced persistent threat (APT) group is new, according to researchers who dubbed it SparklingGoblin. Also new is a novel backdoor technique, called SideWalk, used by the APT to penetrate cybersecurity defenses.


SparklingGoblin, according to ESET researchers who named and discovered the crime group and backdoor, is an offshoot of another APT Winnti Group, first identified in 2013 by Kaspersky. [ESET also said in a Tuesday report](https://www.welivesecurity.com/2021/08/24/sidewalk-may-be-as-dangerous-as-crosswalk/) that the SideWalk backdoor is similar to one used by Winnti called Crosswalk.


Crosswalk and SideWalk, according the ESET, are both “modular backdoors used to exfiltrate system information and that can run shellcode sent by the C&C server.”  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The group, which previously focused attacks on sectors in Macao, Hong Kong and Taiwan in 2020, is still active targeting victims via spearphishing campaigns that include a range of malicious payloads including PDFs (with LNK files), decoy Adobe Flash Players and booby-trapped JavaScript files. Researchers also theorize that initial compromises of victims may also include waterholes.


**Birth of an APT**
-------------------


ESET said it first became aware of SparklingGoblin in May 2020 when tracking the Winnti APT. Researchers said that’s when they stumbled upon an unusual malware packer used to deliver malicious payloads to victims. An analysis of the malware inside the packer revealed “samples containing artifacts from both the Equation Group and Winnti Group,” researchers wrote in an analysis.


The Equation Group, linked to the U.S. National Security Agency, had many of its secrets leaked online by a group called ShadowBrokers in 2017.


“The payload in these samples is an implant attributed to Equation. It is known as PeddleCheap (A.K.A. DanderSpritz) according to the project names seen in the Shadow Brokers leaks,” ESET researchers wrote.


ESET researchers said further analysis revealed the malware cocktail to be related to Winnti, but distinctly different in other ways. “Even though that campaign exhibited links to Winnti Group, the modus operandi was quite different, and we started tracking it as a separate threat actor (SparklingGoblin),” wrote ESET.


Those unique indicators included a version of Crosswalk that for the first time leveraged a PlugX variant called Korplug in conjunction with using Google Docs as a place to store malicious payloads – called a dead drop resolver.


“Following the Hong Kong university compromise, we observed multiple compromises against organizations around the world using similar toolsets and TTPs. Considering those particular [tactics, techniques and procedures, or TTP] and to avoid adding to the general confusion around the ‘Winnti Group’ label, we decided to document this cluster of activity as a new group, which we have named SparklingGoblin, and that we believe is connected to Winnti Group while exhibiting some differences,” ESET wrote.


**A New Modular Backdoor: SideWalk**
------------------------------------


Similar to modular backdoor Crosswalk and Winnti, SideWalk is ESET’s name for SparklingGoblin’s backdoor.


“SideWalk is a modular backdoor that can dynamically load additional modules sent from its C&C server, makes use of Google Docs as a dead drop resolver, and Cloudflare workers as a C&C server. It can also properly handle communication behind a proxy,” researchers said.


The SideWalk backdoor is ChaCha20-encrypted shellcode that is loaded from disk by SparklingGoblin’s InstallUtil-based .NET loaders, notes researchers. An InstallUtil (or Installuti.exe) [is a Windows system tool](https://docs.microsoft.com/en-us/dotnet/framework/tools/installutil-exe-installer-tool) that detects and executes installer components.


“The loader is responsible for reading the encrypted shellcode from disk, decrypting it and injecting it into a legitimate process using the [process hollowing technique](https://attack.mitre.org/techniques/T1055/012/),” researchers wrote.


Process hollowing is a method of executing arbitrary code in the address space of a separate live process, according to a MITRE description of the technique. The attack allows the adversary to run malicious code in the context of a legitimate process.


ESET’s technical analysis covers the data and string pool decryption of the payload via a deobfuscated version of the RunShellcode method called by the Windows InstallUtil.exe utility.


**Fresh Horizons for a New APT**
--------------------------------


In its initial campaigns, SparklingGoblin is believed to be after usernames and IP addresses from a US computer retailer and Canadian schools. The group has mostly targeted the academic sectors in East and Southeast Asia.


Data targeted by SparklingGoblin includes:


Researchers are also unclear where the APT is based. ESET noted that there are clues  that point to SparklingGoblin possibly operating out of eastern Asia, based on Chinese language used by the threat actors.


“SparklingGoblin is a group with some level of connection to Winnti Group. It was very active in 2020 and the first half of 2021, compromising multiple organizations over a wide range of verticals around the world,” researchers wrote.


ESET has documented an extensive list of indicators of compromise and samples on [its GitHub repository](https://github.com/eset/malware-ioc/tree/master/sparklinggoblin).




#### Tags:
[[ESET]] [[Winnti]] [[SparklingGoblin]] [[wrote.]] [[Group,]] [[shellcode]] [[C&C]] [[malware]] [[ThreatPost]]
