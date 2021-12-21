# Windows 10 21H2 adds ransomware protection to security baseline
### Microsoft has released the final version of security configuration baseline settings for Windows 10, version 21H2, available today from the Microsoft Security Compliance Toolkit.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/windows-10-21h2-adds-ransomware-protection-to-security-baseline/
+ Date: 2021-12-21T08:06:10-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/04/17/windows-10-sapphire.jpg)

![Windows 10 21H2 adds ransomware protection to security baseline](https://www.bleepstatic.com/content/hl-images/2021/04/17/windows-10-sapphire.jpg)


Microsoft has released the final version of security configuration baseline settings for Windows 10, version 21H2, available today from the Microsoft Security Compliance Toolkit.


"This Windows 10 feature update brings very few new policy settings," Microsoft security consultant Rick Munck said.


"One setting has been added for this release for printer driver installation restrictions (which was also added to the Windows 11 release). Additionally, all Microsoft Edge Legacy settings have been removed,"


Protection from human-operated ransomware
-----------------------------------------


However, the highlight of the new Windows 10 security baseline is the addition of [tamper protection](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/prevent-changes-to-security-settings-with-tamper-protection?view=o365-worldwide) as a setting to enable by default (this was also made a [default setting in the Windows 11 security baseline](https://www.bleepingcomputer.com/news/security/microsoft-adds-tamper-protection-to-windows-11-security-baseline/) two months ago).


When toggling on the Microsoft Security Baseline for Windows 10 21H2, Redmond urges admins to toggle on Defender for Endpoint's [tamper protection](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/prevent-changes-to-security-settings-with-tamper-protection?view=o365-worldwide) feature to protect against human-operated ransomware attacks.


This feature does that by blocking attempts by ransomware operators or malware to disable OS security features and security solutions to gain easier access to sensitive data and deploy further malware or malicious tools.


Tamper protection automatically locks Microsoft Defender Antivirus using the default secure values, thwarting attempts to change them using the registry, PowerShell cmdlets, or group policies.


After enabling it, ransomware operators would have a considerably more challenging task when trying to:


* Disable virus and threat protection
* Disable real-time protection
* Turnoff behavior monitoring
* Disable antivirus (such as IOfficeAntivirus (IOAV))
* Disable cloud-delivered protection
* Remove security intelligence updates
* Disable automatic actions on detected threats

PrintNightmare and Edge Legacy
------------------------------


With the new Windows 10 21H2 security baseline, Redmond removed all Microsoft Edge Legacy settings after its EdgeHTML-based web browser reached end of support in March.


"Going forward, please use the new Microsoft Edge (Chromium-based) baseline, which is on a separate release cadence and available as part of the Microsoft Security Compliance Toolkit," Munck added.


Microsoft also added a new setting to the MS Security Guide custom administrative template designed to restrict printer driver installation to users with Administrator privileges.


The new recommendation follows security updates released starting with July 2021 to address the CVE-2021-34527 [PrintNightmare](https://www.bleepingcomputer.com/tag/printnightmare/) remote code execution flaw impacting the Windows Print Spooler service.


Now available for download
--------------------------


[Windows security baselines](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-security-configuration-framework/windows-security-baselines) provide Microsoft-recommended security configurations which reduce Windows systems' attack surface and increase the overall security posture of enterprise endpoints.


"A security baseline is a group of Microsoft-recommended configuration settings that explains their security impact," as Microsoft [explains](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-security-configuration-framework/windows-security-baselines). "These settings are based on feedback from Microsoft security engineering teams, product groups, partners, and customers."


The Windows 10 21H2 security baseline is now available for download via the [Microsoft Security Compliance Toolkit](https://www.microsoft.com/download/details.aspx?id=55319), and it includes Group Policy Object (GPO) backups and reports, the scripts needed to apply settings to the local GPO, as well as Policy Analyzer rules.


"Please download the content from the Microsoft Security Compliance Toolkit, test the recommended configurations, and customize / implement as appropriate," Munck added.


More info on the changes that the new Windows 10 21H2 security baseline comes with is available in this [Microsoft Security Baselines blog post](https://techcommunity.microsoft.com/t5/microsoft-security-baselines/security-baseline-for-windows-10-version-21h2/ba-p/3042703).





## Tags:

#### Threatactor:
[[threatactor.name=APT3]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=cmd]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Windows]] [[21h2]] [[Ransomware]] [[Munck]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-34527]]

