# Stealthy ‘WIRTE’ Gang Targets Middle Eastern Governments
### Kaspersky researchers suspect that the cyberattackers may be a subgroup of the politically motivated, Palestine-focused Gaza Cybergang.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176688
+ Date: 2021-12-01 17:11:04+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/01115115/middle-east-map.jpeg)

A threat actor tracked as WIRTE has been assaulting Middle East governments since at least 2019 using “living-off-the-land” techniques and malicious Excel 4.0 macros.


On Monday, Kaspersky [reported](http://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044/) that it observed the group in February using Microsoft Excel droppers, which planted hidden spreadsheets and VBA macros to launch intrusions, fingerprint systems and execute code on infected machines.


Researchers said that the first-stage implants look similar to the first-stage VBS implant used by the [MuddyWater](https://threatpost.com/microsoft-zerologon-attack-iranian-actors/159874/) advanced persistent threat (APT) actor for reconnaissance and profiling (aka Mercury, Static Kitten or Seedworm). Whatever its name, MuddyWater has historically [targeted government victims](https://threatpost.com/muddywater-apt-custom-tools/144193/) in the Middle East to exfiltrate data.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


In April 2019, Kaspersky Lab reported that it had observed [MuddyWater exfiltrating data](https://threatpost.com/muddywater-apt-custom-tools/144193/) such as credentials from governmental and telco targets in the Middle East, using a relatively simple, expendable set of tools that revealed a moderately sophisticated threat actor at work – with the potential to get even more dangerous over time.


Slightly Different TTPs Than MuddyWater’s
-----------------------------------------


But although the most recent intrusion sets look similar to a new MuddyWater first-stage VBS implant used for reconnaissance and profiling, they use slightly different tactics, techniques and procedures (TTPs), Kaspersky said.


Specifically, the threat actor has expanded on MuddyWater’s targeting: Most victims are still Middle Eastern government and diplomatic entities, but the attacks are now also being launched against what researchers called the “unusual” victims of law firms and financial institutions.


“To date, most of the known victims are located in the Middle East, but there are also targets in other regions,” according to the report. “Various industries are affected by this campaign. The main focus is on government and diplomatic entities, though we also noticed an unusual targeting of law firms and financial institutions.”


The targeted entities are located in Armenia, Cyprus, Egypt, Jordan, Lebanon, Palestine, Syria and Turkey.


WIRTE Possibly Tied to Gaza Cybergang
-------------------------------------


The APT is, in fact, a lesser-known actor named WIRTE, first [publicly referenced](https://lab52.io/blog/wirte-group-attacking-the-middle-east/) by Lab52 in 2019, Kaspersky said: a group that it suspects, with low confidence, might be related to the [Gaza Cybergang](https://threatpost.com/molerats-apt-espionage-facebook-dropbox/162162/) threat actor.


Gaza Cybergang is an Arabic-speaking, politically motivated collective of interrelated threat groups that was actively targeting the Middle East and North Africa as of a year ago. According to Kaspersky’s [previous research](https://threatpost.com/sas-2019-gaza-cybergang-blends-sophistication-levels-in-highly-effective-spy-effort/143546/), Gaza Cybergang had a particular focus on the Palestinian Territories.


.EXE Disguised as ‘Kaspersky Update Agent’
------------------------------------------


The infection chains started with spear-phishing emails carrying a malicious Microsoft Excel/Word document as the initial attack vector. The documents carry embedded VBA macros designed to deploy a malicious payload.


In order to entice targets to trigger the Excel dropper, WIRTE festooned its phishing emails with logos and branding of the targeted entity, or topics that were trending in their region. In one case, the gang mimicked the Palestinian Authority, Kaspersky said.


The group also stole Kaspersky’s name, slapping a fake “Kaspersky Update Agent” label onto what’s actually an executable that drops the VBS implant, as shown below.


Researchers couldn’t confirm whether the executable was also distributed through email or whether the threat actor downloaded it further along in the infection chain after initial penetration, but it has the same execution flow as the Excel 4.0 macros, they said.


After a target opens the Excel dropper and disables the protected mode, it executes a series of formulas placed in a hidden column. The main spreadsheet, which requested the target to “enable editing,” is hidden. Then, the dropper unhides a secondary spreadsheet with a decoy.


Then the dropper runs formulas from a third spreadsheet with hidden columns, which runs these three anti-sandbox checks:


1. Get the name of the environment in which Excel is running, along with version number.
2. Check if a mouse is present.
3. Check if the host computer can play sounds.


The process will halt if any of those checks fail. Otherwise, the macro opens a temporary %ProgramData%\winrm.txt file, saves a VBS stager to %ProgramData%\winrm.vbs and adds a pair of registry keys, shown below, for persistence via [Component Object Model (COM) hijacking.](https://attack.mitre.org/techniques/T1546/015/) 


After that, the macro writes a snippet of PowerShell wrapped in VB code into %ProgramData%. Kaspersky is calling this snippet the “LitePower” stager: A stager that downloads payloads and receives marching orders from the command-and-control (C2) servers.


These are the commands Kaspersky observed during the intrusions:


1. List local disk drives
2. Get list of antivirus software installed
3. Check if current user has admin privileges
4. Get OS architecture
5. Check for backdoor services
6. Check for the registry keys added for COM hijacking
7. List all hotfixes installed
8. Take screenshots and save to %AppData% before sending them to the C2 via a POST request


Slippery C2 Servers
-------------------


Researchers identified C2 domains dating to at least December 2019, some of which were tucked behind CloudFlare to obscure their real C2 IP addresses.


With help from partners, Kaspersky managed to gather some original C2 IP addresses, which revealed that the servers are hosted in Ukraine and Estonia, as shown below.


Newly observed intrusions performed by the threat actor show the use of different communication methods compared with older attacks, but the same ports and similar PowerShell IEX command execution and sleep functions were employed in all attacks, Kaspersky says.


WIRTE’s newly observed intrusions use different communication methods than the older attacks, but the same ports, as well as similar PowerShell IEX command execution and sleep functions – as shown below – were employed in all attacks, Kaspersky said.


In past assaults, the adversary has used regsvr32.exe as a [living-off-the-land (LotL)](https://encyclopedia.kaspersky.com/glossary/lotl-living-off-the-land/?utm_source=securelist&utm_medium=blog&utm_campaign=termin-explanation) technique. In more recent incidents, however, the actor switched to another LotL technique, including COM hijacking.


But in either case, the working directory is %ProgramData%, researchers noted – just another similarity that suggests that WIRTE is behind recent intrusions. “All in all, we believe that all these similarities are a strong indication that the attacks described in this report were conducted by the WIRTE threat actor,” Kaspersky said.


“We assess with low confidence that WIRTE is a subgroup under the Gaza Cybergang umbrella,” according to the report. “Although the three subgroups we are tracking use entirely different TTPs, they all occasionally use decoys associated with Palestinian matters, which we haven’t seen commonly used by other threat actors, especially those operating in the Middle East region such as MuddyWater and Oilrig.”


A modified toolset enabled WIRTE to hide away for years, researchers added. The LotL techniques are “an interesting new addition to their TTPs, while the use of interpreted language malware such as VBS and PowerShell scripts distinguishes this suspected Gaza Cybergang from other subgroups, given that it gives them flexibility to “update their toolset and avoid static detection controls,” Kaspersky said .


“Whether WIRTE is a new subgroup or an evolution of existing Gaza Cybergang subgroups, we see them expanding their presence further in cyberspace by using updated and stealthier TTPs,” the firm predicted.


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** [***REGISTER TODAY***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article) ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This*** [***LIVE, interactive Threatpost Town Hall***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***, sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article) ***for the LIVE event!***





## Tags:

#### Threatactor:
[[threatactor.name=Molerats]] [[threatactor.name=MuddyWater]] [[threatactor.name=MuddyWater]] [[threatactor.name=MuddyWater]] [[threatactor.name=MuddyWater]] [[threatactor.name=OilRig]] [[threatactor.name=WIRTE]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.continent.name=Africa]] [[victim.country.name=Egypt]] [[victim.continent.name=Africa]] [[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Armenia]] [[victim.continent.name=Asia]] [[victim.country.name=Jordan]] [[victim.continent.name=Asia]] [[victim.country.name=Lebanon]] [[victim.continent.name=Asia]] [[victim.country.name=Palestine]] [[victim.continent.name=Asia]] [[victim.country.name=Syria]] [[victim.continent.name=Asia]] [[victim.country.name=Turkey]] [[victim.continent.name=Asia]] [[victim.country.name=Cyprus]] [[victim.continent.name=Europe]] [[victim.country.name=Estonia]] [[victim.continent.name=Europe]] [[victim.country.name=Turkey]] [[victim.continent.name=Europe]] [[victim.country.name=Ukraine]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Kaspersky]] [[Wirte]] [[Muddywater]] [[Gaza]] [[Cybergang]] [[Vbs]] [[C2]] [[Powershell]] [[First-stage]] [[Ttps]] [[ThreatPost]]

