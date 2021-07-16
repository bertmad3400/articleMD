# Microsoft Defender for Identity now detects PrintNightmare attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/microsoft-defender-for-identity-now-detects-printnightmare-attacks/)
+ Date: July 16, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft Defender for Identity now detects PrintNightmare attacks](https://www.bleepstatic.com/content/hl-images/2021/05/26/Microsoft-Defender.jpg)


Microsoft has added support for PrintNightmare exploitation detection to Microsoft Defender for Identity to help Security Operations teams detect attackers' attempts to abuse this critical vulnerability.


As revealed by Microsoft program manager [Daniel Naim](https://twitter.com/danielmy1Daniel/status/1415695946164449288), Defender for Identity [now identifies](https://docs.microsoft.com/en-us/defender-for-identity/lateral-movement-alerts#suspected-exploitation-attempt-on-windows-print-spooler-service-external-id-2415) Windows Print Spooler service exploitation (including the actively exploited CVE-2021-34527 [PrintNightmare](https://www.bleepingcomputer.com/tag/printnightmare/) bug) and helps block lateral movement attempts within an org's network.


If successfully exploited, this critical flaw enables [attackers to take over affected servers](https://www.bleepingcomputer.com/news/security/public-windows-printnightmare-0-day-exploit-allows-domain-takeover/) by elevating privileges to Domain Administrator, stealing domain credentials, and distribute malware as a Domain Admin via remote code execution (RCE) with SYSTEM privileges.


[Microsoft Defender for Identity](https://www.microsoft.com/en-us/microsoft-365/security/identity-defender) (previously known as Azure Advanced Threat Protection or Azure ATP) is a cloud-based security solution that leverages on-premises Active Directory signals.


This allows SecOps teams to detect and investigate compromised identities, advanced threats, and malicious insider activity targeting enrolled orgs.


Defender for Identity is bundled with Microsoft 365 E5 but, if you don't have a subscription already, you can get a [Security E5 trial](https://go.microsoft.com/fwlink/p/?LinkID=2077047&clcid=0x409&culture=en-us&country=US) right now to give this new feature a spin.



![Microsoft Defender for Identity detecting PrintNightmare exploitation attempt](https://www.bleepstatic.com/images/news/u/1109292/2021/Microsoft%20Defender%20for%20Identity%20detecting%20PrintNightmare%20exploitation%20attempt.png)*Microsoft Defender for Identity detecting PrintNightmare exploitation attempt (Daniel Naim)*
Last week, Microsoft [clarified the PrintNightmare patch guidance](https://www.bleepingcomputer.com/news/security/microsoft-printnightmare-security-updates-work-start-patching/) and shared the steps needed to correctly patch the critical vulnerability after several security researchers [tagged the patches issued to address the bug were incomplete](https://www.bleepingcomputer.com/news/microsoft/microsofts-incomplete-printnightmare-patch-fails-to-fix-vulnerability/).


CISA also issued an emergency directive on Tuesday, [ordering federal agencies](https://www.bleepingcomputer.com/news/security/cisa-orders-federal-agencies-to-patch-windows-printnightmare-bug/) to mitigate the actively exploited [PrintNightmare](https://www.bleepingcomputer.com/news/security/microsoft-printnightmare-security-updates-work-start-patching/) vulnerability on their networks.


In related news, Defender for Identity was updated in November to [detect Zerologon exploitation](https://www.bleepingcomputer.com/news/security/microsoft-defender-for-identity-now-detects-zerologon-attacks/) as part of on-premises attacks attempting to this critical vulnerability.


Microsoft will roll out a another update later this month which will enable security operations (SecOps) teams to block attack attempts by [locking compromised users' Active Directory accounts](https://www.bleepingcomputer.com/news/security/microsoft-365-to-let-secops-lock-hacked-active-directory-accounts/).


New Windows Print Spooler vulnerability
---------------------------------------


On Thursday evening, Microsoft shared mitigation guidance on a [new Windows Print Spooler elevation of privilege vulnerability](https://www.bleepingcomputer.com/news/microsoft/microsoft-shares-guidance-on-new-windows-print-spooler-vulnerability/) tracked as CVE-2021-34481 and discovered by Dragos security researcher Jacob Baines.


Unlike PrintNightmare, this security bug can only be exploited by attackers with local access to vulnerable systems to gain elevated privileges.


"The attack is not really related to PrintNightmare. As you know, PN can be executed remotely and this is a local only vulnerability," Baines told BleepingComputer.


While Microsoft shared very little info regarding this bug (including what versions of Windows are vulnerable), Baines said that the security flaw is printer driver-related.


Redmond is still investigating this vulnerability and working on security updates to address the underlying Windows Print Spooler service weaknesses.


Until a CVE-2021-34481 patch is available, Microsoft advises admins to [disable the Print Spooler service](https://www.bleepingcomputer.com/news/microsoft/microsoft-shares-guidance-on-new-windows-print-spooler-vulnerability/) on Windows devices exposed to attacks.




#### Tags:
[[Microsoft]] [[PrintNightmare]] [[Windows]] [[teams]] [[Baines]] [[Bleeping Computer]]
