# TA551 Shifts Tactics to Install Sliver Red-Teaming Tool
### A new email campaign from the threat group uses the attack-simulation framework in a likely leadup to ransomware deployment.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175651)
+ Date: October 21, 2021  3:31 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/21151334/red-team-e1634843629348.jpg)
The criminal threat group known as TA551 has added the Sliver red-teaming tool to its bag of tracks – a move that may signal ramped up ransomware attacks ahead, researchers said.


According to Proofpoint researchers, TA551 (aka Shathak) has been mounting cyberattacks that start with email thread hijacking – an [increasingly popular tactic](https://threatpost.com/emotet-returns-100k-mailboxes/162584/) in which adversaries insert themselves into existing email conversations. In one offensive seen just this week, the messages contained password-protected zipped Word documents. If opened and macros enabled, the attachments ultimately lead to the download of Sliver, an open-source, cross-platform adversary simulation and red-team platform.


The activity demonstrates a “significant departure” from previous tactics, techniques and procedures (TTPs) from TA551, according to Proofpoint. Typically, the end goal for TA551 has been to drop an initial-access/banking trojan such as IcedID, Qbot or Ursnif (and [Emotet in the past](https://threatpost.com/trickbot-takes-over-emotet/164710/)), which eventually led to ransomware attacks. For instance, [IcedID implants](https://threatpost.com/spam-icedid-banking-trojan-variant/167250/) were associated with Maze and [Egregor ransomware](https://threatpost.com/fbi-egregor-attacks-businesses-worldwide/162885/) events in 2020, the firm determined.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“Typically, TA551 use more commodity malware like banking trojans,” Sherrod DeGrippo, vice president of threat research and detection at Proofpoint, told Threatpost. “They would compromise a victim and potentially broker access to enable the deployment of Cobalt Strike and eventually ransomware. Now with Sliver, they don’t need to rely on other groups for access. The threat actor is able to break in on their own with much more flexibility to pushing ransomware, stealing data or doing any lateral movements through the target organization.”


**Red Teams Tools on the Rise for Cybercrime**
----------------------------------------------


The move to installing Sliver speaks to the snowballing use of legitimate threat-hunting and defense tools by cybercriminals, said DeGrippo. Proofpoint observed a 161 percent increase in threat actor use of [the red-teaming tool Cobalt Strike](https://threatpost.com/cobalt-strike-cybercrooks/167368/) between 2019 and 2020 for instance.


It’s a phenomenon that other researchers have flagged as well.


“Attackers have never had it better in terms of freely available tooling, such as Metasploit and Mimikatz, or pirated copies of Cobalt Strike,” Nate Warfield, CTO at Prevailion, wrote in a [Threatpost column](https://threatpost.com/cybersecurity-failing-ransomware/175637/) this week. “Whether they need phishing toolsets, obfuscation frameworks, initial access tools, command-and-control (C2) infrastructure, credential-abuse tools or even open-source ransomware payloads, nearly all of this can be found for free on GitHub. Most people assume malicious actors are hiding on the Dark Web, selling tools for Bitcoin to only the shadiest of black hats, but this simply isn’t true.”


He added, “The industry has given offensive security professionals its blessing to develop and release attack frameworks under the rationale that ‘defenders need to understand these tactics.’ But this glosses over the fact that attack frameworks also help the attackers and make it harder for defenders to keep up.”


Sliver is available for free online, and capabilities include information-gathering, command-and-control (C2) functionality, token manipulation, process injection and other features. Additional offensive frameworks that appear as first-stage payloads used by cybercrime actors include Lemon Tree and Veil, according to Proofpoint.


“Threat actors are using as many legitimate tools as possible, including executing Windows processes like PowerShell and WMI; injecting malicious code into legitimate binaries; and frequently using allowable services like Dropbox, Google Drive, SendGrid, and Constant Contact to host and distribute malware,” DeGrippo told Threatpost. “They are flexible and easy to access and use.”


**Defending Against Email Attacks**
-----------------------------------


Proofpoint said that it’s not releasing any campaign data, including victimology, geographic distribution of attacks or the volume of the activity – so it’s hard to say which businesses should be concerned. However, TA551 [is known for](https://www.itpro.com/security/cyber-crime/360248/ta551shathak-threat-research) widescale, global attacks that cast a big net. And, DeGrippo did offer the following tips for protection:


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


 


 




#### Tags:
[[TA551]] [[ransomware]] [[Proofpoint]] [[ThreatPost]]
