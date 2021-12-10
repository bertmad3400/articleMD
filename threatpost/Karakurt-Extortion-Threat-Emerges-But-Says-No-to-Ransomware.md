# 'Karakurt' Extortion Threat Emerges, But Says No to Ransomware
### The threat group, first identified in June, focuses solely on data exfiltration and subsequent extortion, and has already targeted 40 victims since September.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176911
+ Date: 2021-12-10T13:16:43+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/10081343/Karakurt-e1639142036611.jpeg)

There is a new financially motivated threat group on the rise and for a change, it doesn’t appear to be interested [in deploying](https://threatpost.com/emotets-behavior-spread-are-omens-of-ransomware-attacks/176845/) ransomware or taking out [high-profile targets](https://threatpost.com/pipeline-crippled-ransomware/165963/).


Researchers from Accenture Security have been tracking a group that calls itself “Karakurt,” which means “black wolf” in Turkish and is the name of a venomous spider found in eastern Europe and Siberia.


Karakurt focuses on data exfiltration and subsequent extortion, allowing it to move quickly. In fact, since September, it has already hit more than 40 victims, 95 percent of which were in North America with the rest in Europe, researchers [revealed in a report](https://www.accenture.com/us-en/blogs/cyber-defense/karakurt-threat-mitigation) published Friday.


“The threat group is financially motivated, opportunistic in nature, and so far, appears to target smaller companies or corporate subsidiaries versus the alternative big-game hunting approach,” they wrote in the report.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Researchers said they expect that Karakurt will turn out to be a bit of a trendsetter and that in the future, other groups will move away from targeting massive corporations or [critical-infrastructure providers](https://threatpost.com/fbi-claws-back-millions-darksides-ransom/166705/) with ransomware to adopt a similar exfiltration/extortion approach.


This is because it “enables faster attack execution and steers clear of intentionally disrupting business operations, yet still yields leverage in terms of data extortion,” Accenture’s Cyber Investigations, Forensics & Response (CIFR) team told Threatpost in an email.


**Timeline and Initial Intrusion**
----------------------------------


Researchers outside of Accenture Security first identified Karakurt in June as it began setting up its infrastructure and data-leak sites, Accenture CIFR researchers told Threatpost. That month, the group registered the sites karakurt.group and karakurt.tech; and created the Twitter handle [@karakurtlair](https://twitter.com/KarakurtLair) in August. Not long after, the group’s first successful attack followed.


Accenture Security’s collection sources and intrusion analysis identified the first victim of the group in September; two months later, the group revealed its victim on the karakurt.group website, researchers said.


Karakurt’s tactics, techniques and procedures (TTPs) for infiltrating victim networks, achieving persistence, moving laterally and stealing data are similar to many threat actors, and the group often takes a “living off the land” approach depending on the attack surface, researchers said — i.e., using tools or features that already exist in the target environment.


The group establishes initial access using legitimate VPN credentials, though researchers said it’s unclear how they obtain those credentials. “One possibility is exploitation of vulnerable VPN devices, but all cases included inconsistent or absent enforcement of multi-factor authentication (MFA) for user accounts,” they wrote in the report.


**Switching Up Tactics**
------------------------


To maintain persistence once accessing a network, Karakurt predominantly uses service creation, remote-management software and distribution of command-and-control (C2) beacons across victim environments using Cobalt Strike.


However, recently the group seems to have switched tactics in its deployment of backup persistence, researchers observed. Instead of deploying Cobalt Strike, Karakurt “persisted within the victim’s network via the VPN IP pool or installed AnyDesk to allow external remote access to compromised devices,” they wrote. This allows the group to leverage previously obtained user, service and administrator credentials to move laterally.


The group also will use other remote-management tools, remote desktop protocol (RDP), Cobalt Strike and PowerShell commands to move laterally and discover pertinent data to steal and use for extortion purposes as needed, researchers said.


If Karakurt can’t elevate privileges using credentials, they turn to either Mimikatz or PowerShell to do so, but only if necessary, researchers observed.


Overall, the group’s attack vector so far shows it is nimble enough to modify its tactics depending on the victim’s environment, researchers told Threatpost. And because Karakurt often uses valid credentials to access networks, it can manage to evade detection in many cases.


Finally, to steal data, Karakurt uses 7zip and WinZip for compression, as well as Rclone or FileZilla (SFTP) for staging and final exfiltration to Mega.io cloud storage. Staging directories used to exfiltrate data in attacks were C:\Perflogs and C:\Recovery, according to Accenture Security.


**Mitigation Advice**
---------------------


Researchers provided typical mitigation advice to organizations to avoid being compromised and extorted by Karakurt, which will contact companies multiple times to put pressure on them to pay once their data has been taken.


Organizations should maintain best practices like patching across all systems, particular those that face the internet; updating anti-virus software; implementing strict network egress policies; and using application whitelisting where feasible to protect themselves, researchers advised.


Given the group’s tendency to use valid credentials, organizations also should make passwords as complex as they can, as well as use MFA whenever possible.


Moreover, they should only use admin accounts for valid administrative purposes and never to connect to the network or browse the internet, and should also enforce them with cross-platform MFA, researchers recommended.


Hunting for attacker TTPs — including common living-off-the-land techniques that Karakurt has used — to proactively detect, respond to and mitigate attacks also is advised.


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** ***[REGISTER TODAY](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)*** ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This [LIVE, interactive Threatpost Town Hall](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article), sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***for the LIVE event!***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=FTP]] [[action.malware.name=Mimikatz]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=Tunis]] [[victim.country.name=Tunisia]] [[victim.continent.name=Africa]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Accenture]] [[Threatpost]] [[Vpn]] [[ThreatPost]]

