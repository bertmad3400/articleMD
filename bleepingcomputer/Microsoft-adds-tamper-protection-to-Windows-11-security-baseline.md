# Microsoft adds tamper protection to Windows 11 security baseline
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/microsoft-adds-tamper-protection-to-windows-11-security-baseline/)
+ Date: October 9, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft adds tamper protection to Windows 11 security baseline](https://www.bleepstatic.com/content/hl-images/2021/10/06/Windows_11.jpg)


Microsoft has released the final version of its security configuration baseline settings for Windows 11, downloadable today using the Microsoft Security Compliance Toolkit.


"Two new settings have been added for this release (which were also added to the Windows Server 2022 release), a new Microsoft Defender Antivirus setting, and a custom setting for printer driver installation restrictions," Microsoft security consultant Rick Munck said.


Human operated ransomware protection by default
-----------------------------------------------


When enabling the Microsoft Security Baseline for Windows 11, Redmond urges admins to ensure that Microsoft Defender for Endpoint's [tamper protection](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/prevent-changes-to-security-settings-with-tamper-protection?view=o365-worldwide) feature, which adds additional protection against human-operated ransomware attacks, is enabled.


It does that by blocking attempts made by malware or threat actors to disable security solutions and OS security features that would allow them to gain easier access to sensitive data and deploy malware or malicious tools.


Tamper protection sets up Microsoft Defender Antivirus using secure default values and hinders attempts to change them via the registry, PowerShell cmdlets, or group policies.


Once tamper protection is toggled on, ransomware operators would have a much more challenging task ahead of them when trying to:


* Disable virus and threat protection
* Disable real-time protection
* Turnoff behavior monitoring
* Disable antivirus (such as IOfficeAntivirus (IOAV))
* Disable cloud-delivered protection
* Remove security intelligence updates


PrintNightmare and Edge Legacy recommendations
----------------------------------------------


With the new security baseline, Microsoft also added a new setting to the MS Security Guide custom administrative template to restrict printer driver installation to administrators.


This new recommendation follows patches released since July 2021 to address the CVE-2021-34527 [PrintNightmare](https://www.bleepingcomputer.com/tag/printnightmare/) remote code execution vulnerability in the Windows Print Spooler service.


Microsoft also removed all Microsoft Edge Legacy settings after the EdgeHTML-based web browser reached the end of support in March and was removed from Windows 11.


'Going forward, please use the new Microsoft Edge (Chromium-based) baseline, which is on a separate release cadence and available as part of the Microsoft Security Compliance Toolkit," Munck [said](https://techcommunity.microsoft.com/t5/microsoft-security-baselines/windows-11-security-baseline/ba-p/2810772).


Download and implement the security baseline
--------------------------------------------


[Windows security baselines](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-security-configuration-framework/windows-security-baselines) provide admins with Microsoft-recommended security configuration baselines designed to reduce Windows systems' attack surface and boost the overall security posture of Windows enterprise endpoints.


"A security baseline is a group of Microsoft-recommended configuration settings that explains their security impact," as Microsoft [explains](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-security-configuration-framework/windows-security-baselines). "These settings are based on feedback from Microsoft security engineering teams, product groups, partners, and customers."


The Windows 11 security baseline is available for download via the [Microsoft Security Compliance Toolkit](https://www.microsoft.com/download/details.aspx?id=55319). It includes Group Policy Object (GPO) backups and reports, scripts to apply settings to the local GPO, and Policy Analyzer rules files.


"Please download the content from the Microsoft Security Compliance Toolkit, test the recommended configurations, and customize / implement as appropriate," Munck added.


Further details on the changes implemented in the Windows 11 baseline are available on the Microsoft Security Baselines [blog post](https://techcommunity.microsoft.com/t5/microsoft-security-baselines/windows-11-security-baseline/ba-p/2810772) announcing this release.




#### Tags:
[[Microsoft]] [[Windows]] [[Munck]] [[ransomware]] [[Bleeping Computer]]
