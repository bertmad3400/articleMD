# Vice Society ransomware joins ongoing PrintNightmare attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/vice-society-ransomware-joins-ongoing-printnightmare-attacks/)
+ Date: August 13, 2021
+ Author: Sergiu Gatlan


## Article:
![Vice Society ransomware joins ongoing PrintNightmare attacks](https://www.bleepstatic.com/content/hl-images/2020/11/06/Ransomware-headpic.jpg)


The Vice Society ransomware gang is now also actively exploiting Windows print spooler PrintNightmare vulnerability for lateral movement through their victims' networks.


[PrintNightmare](https://www.bleepingcomputer.com/tag/printnightmare/) is a set of recently disclosed security flaws (tracked as [CVE-2021-1675](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-1675), [CVE-2021-34527](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527), and [CVE-2021-36958](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-another-windows-print-spooler-zero-day-bug/)) found to affect the Windows Print Spooler service, Windows print drivers, and the Windows Point and Print feature.



Microsoft has released security updates to address the CVE-2021-1675 and CVE-2021-34527 bugs in [June](https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2021-patch-tuesday-fixes-6-exploited-zero-days-50-flaws/), [July](https://www.bleepingcomputer.com/news/security/microsoft-pushes-emergency-update-for-windows-printnightmare-zero-day/), and [August](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-print-spooler-printnightmare-vulnerability/), and has also published a security advisory this week with a [workaround for CVE-2021-36958](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-another-windows-print-spooler-zero-day-bug/) (a zero-day bug allowing privilege escalation).


Attackers can abuse this set of security flaws for local privilege escalation (LPE) or distributing malware as Windows domain admins via remote code execution (RCE) with SYSTEM privileges.


PrintNightmare added to Vice Society's arsenal
----------------------------------------------


Recently, [Cisco Talos researchers observed](https://blog.talosintelligence.com/2021/08/vice-society-ransomware-printnightmare.html) Vice Society ransomware operators deploying a malicious Dynamic-link library (DLL) to exploit two PrintNightmare flaws (CVE-2021-1675 and CVE-2021-34527).


Vice Society ransomware (likely a HelloKitty spin-off) encrypts both Windows and Linux systems using OpenSSL (AES256 + secp256k1 + ECDSA), as ransomware expert Michael Gillespie [found in mid-June](https://twitter.com/demonslay335/status/1403109032014061568) when the first samples surfaced.


The Vice Society gang mainly targets small or midsize victims in human-operated double-extortion attacks, with a notable focus on public school districts and other educational institutions.


Cisco Talos also made a list of Vice Society's favorite tactics, techniques, and procedures (TTPs), including backup deletion to prevent victims from restoring encrypted systems and bypassing Windows protections for credential theft and privilege escalation.


"They are quick to leverage new vulnerabilities for lateral movement and persistence on a victim's network," Cisco Talos said.


"They also attempt to be innovative on end-point detection response bypasses" and "operate a data leak site, which they use to publish data exfiltrated from victims who do not choose to pay their extortion demands."




> 
> Vice Society is actively exploiting PrintNightmare (CVE-2021-1675 / CVE-2021-34527) to spread laterally across victim networks. They are a new player in the ransomware space. They have been observed launching big-game hunting and double-extortion attacks <https://t.co/hQqRXEMFYc>
> 
> 
> — Craig Williams (@security\_craig) [August 12, 2021](https://twitter.com/security_craig/status/1425949130019545091?ref_src=twsrc%5Etfw)


PrintNightmare actively exploited by multiple threat actors
-----------------------------------------------------------


The [Conti](https://twitter.com/John_Fokker/status/1425749521569624065) and [Magniber ransomware](https://www.bleepingcomputer.com/news/security/ransomware-gang-uses-printnightmare-to-breach-windows-servers/) gangs are also using PrintNightmare exploits to compromise unpatched Windows servers.


Magniber's attempts to exploit the Windows print spooler vulnerabilities in attacks against South Korean victims were detected by Crowdstrike in mid-June.


In-the-wild PrintNightmare exploitation reports [[1](https://twitter.com/BushidoToken/status/1422492498241392647), [2](https://twitter.com/securitydoggo/status/1422241229392203777), [3](https://twitter.com/CR_Nocturnus/status/1420402020259926016)] have been [slowly trickling in](https://twitter.com/BushidoToken/status/1426099976850001920) since the vulnerability was first reported and [proof-of-concept exploits were leaked](https://www.bleepingcomputer.com/news/security/public-windows-printnightmare-0-day-exploit-allows-domain-takeover/).


"Multiple distinct threat actors are now taking advantage of PrintNightmare, and this adoption will likely continue to increase as long as it is effective," Cisco Talos added.


"The use of the vulnerability known as PrintNightmare shows that adversaries are paying close attention and will quickly incorporate new tools that they find useful for various purposes during their attacks."


To defend against these ongoing attacks, you should apply any available PrintNightmare patches as soon as possible and implement the workarounds provided by Microsoft for the CVE-2021-36958 zero-day to remove the attack vector.




#### Tags:
[[PrintNightmare]] [[Windows]] [[ransomware]] [[Talos]] [[Bleeping Computer]]
