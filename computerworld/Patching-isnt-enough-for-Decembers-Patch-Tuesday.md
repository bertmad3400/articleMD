# Patching isn't enough for December's Patch Tuesday
### With 67 flaws addressed, six publicly-reported issues and one vulnerability already exploited, this month's updates pale in comparison to the challenges addressing the Log4j issue. 

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3645134/patching-isnt-enough-for-decembers-patch-tuesday.html
+ Date: 2021-12-18T10:51-05:00
+ Author: Greg Lambert


## Article:
![Article Image](https://images.idgesg.net/images/article/2020/08/hand_reaches_to_activate_controls_with_gear_icons_process_development_update_fix_automate_by_putilich_gettyimages-1220461550_2400x1600-100854509-large.jpg?auto=webp&quality=85,70)

This month's Patch Tuesday update is important for several reasons. With 67 unique vulnerabilities addressed, six publicly-reported issues and one already exploited, this month's updates still pale in comparison to [dealing with the Log4j issue](https://www.csoonline.com/article/3645348/how-to-properly-mitigate-the-log4j-vulnerabilities.html). (Fortunately, there are no browser or Microsoft Exchange updates and minimal changes to Microsoft Office.)

We have added the Windows updates and Visual Studio updates to our "Patch Now" release cycle recommendations, while Office updates are relegated to a normal release cadence. You can find more information on the risk of deploying these Patch Tuesday updates [in this infographic](https://applicationreadiness.com/assurance-security-dashboard-december-2021/).

**Key testing scenarios**
-------------------------

There are no reported high-risk changes to the Windows platform this month. However, there is one reported functional change, and an additional feature. Here are our high-level testing recommendations:

* Test local printing. Test remote printing and test printing over RDP.
* Test reading or processing ETL files and large WMF files.
* Test new and existing VPN connections. Include a test of site-to-site VPN.
* Test NTFS short name scenarios and large file transfers.

**Known issues**
----------------

Each month, Microsoft includes a list of known issues that relate to the operating system and platforms included in this update cycle. I've referenced a few key issues that relate to the latest builds, including:

* After installing updates released April 22, 2021 or later, an issue occurs that affects versions of Windows Server used as a Key Management Services (KMS) host. Client devices running Windows 10 Enterprise LTSC 2019 and Windows 10 Enterprise LTSC 2016 might fail to activate. These issues will not affect Windows activation. Microsoft is currently investigating the problem.
* After installing this update, when connecting to devices in an untrusted domain using Remote Desktop, connections might fail to authenticate when using smart card authentication. This issue is resolved using Known Issue Rollback (KIR), which can be implemented with the following Group Policy installation files:
+ [Windows Server 2022](https://download.microsoft.com/download/1/e/3/1e36d9a4-e8de-4b35-8566-efdb6aab08fe/Windows%20Server%202022%20Known%20Issue%20Rollback%20101521%2001.msi)
+ [Windows 10, version 2004, Windows 10, version 20H2 and Windows 10, version 21H1](https://download.microsoft.com/download/1/e/3/1e36d9a4-e8de-4b35-8566-efdb6aab08fe/Windows%2010%20(2004,%2020H2%20&%2021H1)%20Known%20Issue%20Rollback%20101521%2001.msi)

One of the best ways to see if there are known issues that could affect your target platform is to check out the many configuration options for downloading patch data at the [Microsoft Security Update guidance](https://msrc.microsoft.com/update-guide/en-us) or the [summary page for this month's security update](https://support.microsoft.com/en-us/topic/security-update-deployment-information-december-14-2021-kb5008541-fe85e678-5400-49bb-9725-3be4707f5381).

**Major revisions**

Microsoft released four updates for informational reasons (documentation and FAQ updates) including: [CVE-2021-43236](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-43236), [CVE-2021-43883](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-43883), [CVE-2021-43893](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-43893), [CVE-2021-43905](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-43905). In addition, Microsoft released several major updates to previous patches,  including:

* [CVE-2019-0887](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2019-0887), [CVE-2020-0655](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2020-0655) and [CVE-2021-1669](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2020-0655): These remote desktop service RCE updates received a major revision notice due to an updated affected system table. Windows 11 is affected by these security issues and this patch applies accordingly.
* [CVE-2021-24084](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-24084): The scope of affected systems has been updated to all supported Windows systems.

Due to the larger scope of these patches, you may not have downloaded and applied them in November. This month, all four updates will be included in the patch cycle (though their dates may reflect a November release date).

**Mitigations and workarounds**
-------------------------------

This month, there is a single reported vulnerability that includes both mitigation and documented workarounds:

* [CVE-2021-43890](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-43890): Microsoft has published an extensive set of workarounds for this AppX spoofing vulnerability. Using the GPO policies BlockNonAdminUserInstall and AllowAllTrustedAppToInstall, it is possible to reduce the surface area for side-loading attacks on the AppX installer. Microsoft has published a [detailed how-to document](https://docs.microsoft.com/en-us/windows/msix/group-policy-msix) on setting GPO policies for AppX (and now MSIX).

Each month, we break down the update cycle into product families (as defined by Microsoft) with the following basic groupings:

* Browsers (Microsoft IE and Edge);
* Microsoft Windows (both desktop and server);
* Microsoft Office;
* Microsoft Exchange;
* Microsoft Development platforms ( [ASP.NET](http://asp.net/) Core, .NET Core and Chakra Core);
* And Adobe. (Retired? Maybe next year.)

**Browsers**
------------

This month, the [Chromium project](https://www.chromium.org/) released 16 updates for the Microsoft Edge browser. We are really seeing a trend here, with no updates to Microsoft's legacy browsers. These updates are very likely part of an auto-update process for your desktop environment, as these updates will not be deployed via Microsoft Update. 

You can find out more in the [Chrome Release blog](https://chromereleases.googleblog.com/2021) and security details on the [Chrome Security Page](https://sites.google.com/a/chromium.org/dev/Home/chromium-security). Given the nature of Edge (not completely integrated into the OS), there are very few expected compatibility or integration errors expected with this release. Add these Chrome updates to your regular update release schedule.

**Windows**
-----------

December brings a moderate update to Windows with 36 updates; three are rated critical by Microsoft and the remaining 33 as important. Normally, we would focus on the critical patches. But this month it's more appropriate to focus on publicly disclosed and exploited vulnerabilities, including:

* [CVE-2021-43240](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-43240): NTFS File System Elevation of Privilege
* [CVE-2021-41333](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41333): Windows Print Spooler RCE
* [CVE-2021-43880](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-43880): Windows Mobile Device Management Elevation of Privilege
* [CVE-2021-43883](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-43883): Windows Installer Elevation of Privilege
* [CVE-2021-43893](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-43893): Windows EFS Elevation of Privilege

This month we have "only" one vulnerability reported as exploited in the wild, with a side-loading spoof attack on the Microsoft AppX installer component ([CVE-2021-43890](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-43890)). Fortunately, this is a complex attack that requires user intervention and Microsoft has confirmed an official fix for this issue. Given the focus on updates to core system components (NTFS, Installer, and printing) we have included some testing recommendations:

* Perform tests on server and desktop send/receive heavy traffic. Focus on singular, very large files.
* Test your .WMF files (due to the codec update) and any graphically intensive D3D applications.
* Test various network traffic conditions, particularly with large data transfers — especially SMB, encrypted file systems, and remote shares.
* Install, update, and uninstall your core applications in a test environment. Ensure that all uninstalls are clean.
* Test your printing, especially remote printing, and printing over RDP.
* All applications that utilise TLS/SSL should undergo a basic "smoke test."

And about that Log4j issue? Patching the OS is not enough to protect your environment. We highly recommend an immediate scan of your application portfolio for JAVA dependencies and references to Log4j components. This week's news of Log4j issues is just the beginning. Expect large scale, industrialized attacks over the Christmas period and into the New Year. It's going to be bad. It’s going to be messy. 

Add these Windows updates to your "Patch Now" schedule and get to work on reducing your application attack surface.

**Microsoft Office**
--------------------

Microsoft released nine patches for Office, all rated important. All versions of SharePoint and Access are affected, as are versions 2016 and 2019 of Word. There are no preview pane attack vectors this month, and all of the reported vulnerabilities require user interaction. Add these Microsoft Office updates to your regular patch release schedule.

**Microsoft Exchange Server**
-----------------------------

The Log4j issue may be the coal in your stocking, but Microsoft has gifted us a reprieve from any Microsoft Exchange updates this month. So you can pay more attention to other things, like Christmas. Or Log4j. You choose.

**Microsoft Development Platforms**
-----------------------------------

Microsoft published seven updates to its development platforms this month (one critical and the remaining rated as important) that affect Visual Studio, PowerShell, and the [ASP.NET/.NET](http://asp.net/.NET) framework. The single critical rated patch ([CVE-2021-43907](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-43907)) relates to the popular WSL extension; if unpatched, it could lead to a remote-code execution scenario. It’s a pretty serious issue that will affect all WSL users. Unfortunately, the testing profile will be quite large with testing requirements for the .NET COM server and REGEX expressions. 

We suggest that you add this Visual Studio update to your "Patch Now" schedule and also reference the additional (and separate) .NET related updates [published on the Microsoft Dev blog](https://devblogs.microsoft.com/dotnet/december-2021-updates/).

**Adobe (really just Reader)**
------------------------------

This month, Microsoft did no release any update to Adobe Reader. I keep thinking that I can retire this section, but we keep getting periodic updates from Adobe or critical printing updates for PDF files. Let's see what happens in 2022.

**And, if you got this far...**
-------------------------------

Because of minimal operations during the holidays and the upcoming new year break, Microsoft will not release a preview release (known as a “C” release) for December. Normal monthly servicing for both Microsoft B and C releases will resume in January. Windows 10, version 2004 has reached end of servicing as of this release. Next month we are likely to see an update to the TLS protocol for Windows Server 2008 with support for TLS 1.2.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=Paris]] [[victim.country.name=France]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Microsoft]] [[Windows]] [[Log4j]] [[Appx]] [[Computerworld]]
#### CVE's
[[CVE-2021-43236]] [[CVE-2021-43883]] [[CVE-2021-43893]] [[CVE-2021-43905]] [[CVE-2019-0887]] [[CVE-2020-0655]] [[CVE-2021-1669]] [[CVE-2021-24084]] [[CVE-2021-43890]] [[CVE-2021-43240]] [[CVE-2021-41333]] [[CVE-2021-43880]] [[CVE-2021-43907]]

