# Patch Tuesday gets off to a busy start for January
### For the first Patch Tuesday of 2022, Microsoft offered up fixes for 97 security issues, with six of them rated as critical. 

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3647150/patch-tuesday-gets-off-to-a-busy-start-for-january.html
+ Date: 2022-01-14T12:10-05:00
+ Author: Greg Lambert


## Article:
![Article Image](https://images.idgesg.net/images/article/2020/07/microsoft_windows_updates_cycle_arrows_laptop_mobile_phone_3x2_1200x800-100851684-large.jpg?auto=webp&quality=85,70)

For this week's Patch Tuesday, the first of the year, Microsoft addressed 97 security issues, six of them rated critical. Though six vulnerabilities have been publicly reported, I do not classify them as zero-days. Microsoft has fixed a lot of security related issues and is aware of several known issues that may have inadvertently caused significant server issues including:

* Hyper-V, which no longer starts with the message, "Virtual machine xxx could not be started because the hypervisor is not running."
* ReFS (Resilient) file systems that are no longer accessible (which is kind of ironic).
* And Windows [domain controller boot loops](https://borncity.com/win/2022/01/12/windows-server-januar-2022-sicherheitsupdates-verursachen-boot-schleife/).

There are a variety of known issues this month, and I'm not sure whether we'll see more issues reported with the January server patches. You can find more information on the risk of deploying these latest updates with our [helpful infographic](https://applicationreadiness.com/assurance-security-dashboard-january-2022/).

**Key testing scenarios**

There are no reported high-risk changes to the Windows platform this month. However, there is one reported functional change, and an additional feature added.

* Test local and remote printing and test printing over RDP.
* Test site-to-site VPN, including new and existing connections.
* Test reading or processing ETL files.
* Check starting and stopping Hyper-V on your servers.
* Run Transactional NTFS (TxF) and CLFS test scenarios while including tests for [ReFS](https://docs.microsoft.com/en-us/windows-server/storage/refs/refs-overview) file I/O transfers.

**Known issues**

Each month, Microsoft includes a list of known issues that relate to the operating system and platforms included in this update cycle. I've referenced a few key issues that relate to the company's latest builds, including:

* SharePoint Server: Most users cannot access Web.config files in SharePoint Server. The affected group of users does not include farm administrators, local administrators, or members who are managed by the system. For more information, see [Users cannot access Web.config files in SharePoint Server (KB5010126)](https://support.microsoft.com/en-us/topic/users-cannot-access-web-config-files-in-sharepoint-server-kb5010126-d741e0a6-5cdb-4fa5-8aa1-45806cac30d2).
* After installing the June 21, 2021 ([KB5003690](https://support.microsoft.com/en-us/topic/june-21-2021-kb5003690-os-builds-19041-1081-19042-1081-and-19043-1081-preview-expired-11a7581f-2a01-47d5-ba12-431709ee2248)) update, some devices cannot install new ones, such as the July 6, 2021 ([KB5004945](https://support.microsoft.com/en-us/topic/july-6-2021-kb5004945-os-builds-19041-1083-19042-1083-and-19043-1083-out-of-band-44b34928-0a71-4473-aa22-ecf3b83eed0e)) or later updates. You will receive the error message, "PSFX\_E\_MATCHING\_BINARY\_MISSING." For more information and a workaround, see [KB5005322.](https://support.microsoft.com/en-us/topic/kb5005322-some-devices-cannot-install-new-updates-after-installing-kb5003214-may-25-2021-and-kb5003690-june-21-2021-66edf7cf-5d3c-401f-bd32-49865343144f)
* After installing updates released April 22, 2021 or later, an issue occurs that affects versions of Windows Server being used as a Key Management Services (KMS) host. Client devices running Windows 10 Enterprise LTSC 2019 and Windows 10 Enterprise LTSC 2016 might fail to activate. This issue only occurs when using a new Customer Support Volume Licence Key (CSVLK). Microsoft is working on a resolution and will provide an update in an upcoming release.
* After installing this Windows update, when connecting to devices in an untrusted domain using Remote Desktop, connections might fail to authenticate when using smart card authentication. You might receive the prompt, "Your credentials did not work. The credentials that were used to connect to [device name] did not work. Please enter new credentials" and "The login attempt failed" in red. This issue is resolved using [Known Issue Rollback (KIR)](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/known-issue-rollback-helping-you-keep-windows-devices-protected/ba-p/2176831). For general information on using Group Policies, see [Group Policy Overview](https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831791(v=ws.11)); we have listed the following group policy installation files in the event that a KIR procedure is required: [Windows Server 2022](https://download.microsoft.com/download/1/e/3/1e36d9a4-e8de-4b35-8566-efdb6aab08fe/Windows%20Server%202022%20Known%20Issue%20Rollback%20101521%2001.msi); [Windows 10, version 2004; Windows 10, version 20H2; and Windows 10, version 21H1](https://download.microsoft.com/download/1/e/3/1e36d9a4-e8de-4b35-8566-efdb6aab08fe/Windows%2010%20(2004,%2020H2%20&%2021H1)%20Known%20Issue%20Rollback%20101521%2001.msi).
* After installing [KB4493509](https://support.microsoft.com/en-us/topic/april-9-2019-kb4493509-os-build-17763-437-3009e91f-261d-7cdc-4f7e-b00a3fde5991), devices with some Asian language packs installed may see the error, "0x800f0982 - PSFX\_E\_MATCHING\_COMPONENT\_NOT\_FOUND.
* After installing Windows 11, some image editing programs might not render colors correctly on certain high dynamic range (HDR) displays.

Microsoft is working on the Windows 11 issues, but has yet to respond to the Hyper-V, ReFS, or Domain Controller problems. One of the best ways to see whether known issues might affect your target platform is to check out the many configuration options for downloading patch data at the [Microsoft Security Update guidance site](https://msrc.microsoft.com/update-guide/en-us) or the [summary page for this month's security update](https://support.microsoft.com/es-es/topic/security-update-deployment-information-january-11-2022-kb5010029-df340fef-e896-407e-92bf-5e96baf4af23).

**Major revisions**
-------------------

Microsoft has not released any major revisions (or minor documentation changes) for the January Patch release.

**Mitigations and workarounds**
-------------------------------

Although there are no published mitigations or workarounds relating to the January patches, we expect a response from Microsoft to the Server 2022 patch-related issues within the next few days.

Each month, we break down the update cycle into product families (as defined by Microsoft) with the following basic groupings:

* Browsers (Microsoft IE and Edge);
* Microsoft Windows (both desktop and server);
* Microsoft Office;
* Microsoft Exchange;
* Microsoft Development platforms ( ASP.NET Core, .NET Core and Chakra Core);
* Adobe (retired???, maybe next year).

**Browsers**
------------

This month sees a mixed bag of updates for Microsoft browsers. Though we don't get any patches for the legacy browsers, Microsoft has released five updates that are specific to the Chromium version of Edge. In addition to these changes, the Chromium project has released a further 24 updates to the Chromium browser core. You can find more information about the Microsoft updates [here](https://docs.microsoft.com/en-us/DeployEdge/microsoft-edge-relnotes-security), with the release notes for the Chromium project updates found [here](https://chromereleases.googleblog.com/2022/01/stable-channel-update-for-desktop.html). Microsoft has published detailed information on the Microsoft Edge-specific issues (found in the [Security Update Guide](https://msrc.microsoft.com/update-guide/en-us)) while Google refrains from publishing detailed security and vulnerability information until all patches are released. 

Add these Chrome (Edge and Chromium) updates to your regular scheduled update release schedule.

**Windows**
-----------

This is a significant update to the Windows platform with seven updates rated critical, and a hefty 80 patches rated as important. There are now several reported issues with this month's server patches affecting (probably all) Windows domain controllers. If you are seeing the following error message post update — "*The system process 'C:\Windows\system32\lsass.exe' terminated unexpectedly with status code -1073741819. The system will now shut down and restart*." — you are not alone. There are also significant numbers of reports that [virtual machines on recently updated Hyper-V do not start](https://www.borncity.com/blog/2022/01/12/patchday-windows-8-1-server-2012-r2-updates-11-januar-2022-mgliche-boot-probleme/#comment-120077).

Normally, we would recommend a significant testing cycle before a production release of Windows updates. However this month's update addresses [CVE-2022-21907](https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fmsrc.microsoft.com%2Fupdate-guide%2Fvulnerability%2FCVE-2022-21907&data=04%7C01%7Ckburke%40virsec.com%7C4574195dd7714054084008d9d53482c1%7Cb9db4e90e1e046c8ac7725cc6454e1d9%7C0%7C0%7C637775243771475117%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=1HgtdMhfXTm2HiPPmMSq2qQ%2FwfCS7ajNA6CZYQ6H6Vs%3D&reserved=0) "which is a particularly dangerous CVE because of its ability to allow for an attacker to affect an entire intranet once the attack succeeds", said Danny Kim, principal architect at [Virsec](http://www.virsec.com/). The CVE is the latest example of how software capabilities can be warped and weaponized; it  targets the HTTP trailer support feature, which allows a sender to include additional fields in a message to supply metadata by providing a specially crafted message that can lead to remote code execution.

 Microsoft says this vulnerability is “wormable” so we recommend that you add this month's Windows update to your "Patch Now" schedule.

Windows Testing Guidelines

* Test your IME with both English and Asian language packs.
* Remote Desktop: A client should be able to connect to the RDP host and be able to redirect drives, audio, clipboard and to printers.
* Test CLFS Logs: (“[CRUD](https://docs.microsoft.com/en-us/iis-administration/api/crud)”) Create a log, read from a log, and update a log.
* Networking: Send and receive large size files to other nodes using IPv4 and IPv6.
* Test NTFS using short name related scenarios.

This month's Windows patches included a major update to NTFS (with no functional changes); for more information and suggested testing scenarios, refer to the Microsoft document [Transactional NTFS (TxF)](https://docs.microsoft.com/en-us/windows/win32/fileio/transactional-ntfs-portal).

**Microsoft Office**
--------------------

Microsoft has released four updates for the venerable Office productivity suite (one rated critical, the remaining three, important). The critical patch ([CVE-2022-21840](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-21840)) addresses a remote code execution vulnerability in the Microsoft Core libraries that (thankfully) requires user interaction such as the following scenario by Microsoft: "In an email attack scenario, an attacker could exploit the vulnerability by sending the specially crafted file to the user and convincing the user to open the file." So, it's 2022 and by clicking on an email, we can just give it all away. 

Microsoft has confirmed that these four patches fully address the issue, so please add this update to your standard Office patch release schedule.

**Microsoft Exchange Server**
-----------------------------

There are three updates to the Microsoft Exchange Server platform this month. With two rated as important ([CVE-2022-21969](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-21969) and [CVE-2022-21855](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-21855)), the focus should be on the critical patch [CVE-2022-21846](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-21846). This vulnerability has a very high [CVSS](https://nvd.nist.gov/vuln-metrics/cvss) rating of 9.0. However, the risk of exploitation is much reduced due to the propagation nature of this vulnerabilities' attack vector. To be successful, an attacker must be present on the network or able to access an adjacent component on the target system (such as Bluetooth). 

Microsoft offered the following testing guidelines for these three patches, which include:

* Test [OWA](https://outlook.live.com/OWA/) scenarios with http and (secure) https URLs.
* Test new Exchange “site mailbox” creation(s).

Fortunately, we are not expecting the challenging configuration issues this month that we've seen in past updates. So, "test before deploy" and add these Exchange updates to your standard server update schedule.

**Microsoft development platforms**

For this cycle, Microsoft released a single update ([CVE-2022-21911](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-21911)) rated as important for its development platforms. This denial-of-service attack does not require user interaction or admin privileges to succeed in compromising a target system. Microsoft has published an official fix for the issue, which may affect .NET COM servers and REGEX expressions. These components will need some testing before deployment of the singular .NET update. You may also have to download these and future updates in a separate file for .NET 4.8 patches. 

Microsoft has published a blog on [.NET 4.8 release cadences and methodologies](https://devblogs.microsoft.com/dotnet/upcoming-updates-for-net-framework-4-8/). Add this update to your regular patch release schedule.

**Adobe (really just Reader)**

It's back with a vengeance! Adobe has published so many vulnerabilities for its Adobe Reader (and Acrobat) products, I initially thought that the long list of memory related issues addressed the entire Adobe suite. 

Nope. 

Adobe Reader has seen no less than 26 updates, with 15 rated critical, three as important, and another seven as moderate. All versions are affected, and all currently supported platforms will require an update. You can read more about this (very) long list of updates [here](https://helpx.adobe.com/security/products/acrobat/apsb22-01.html). Add these Adobe updates to your "Patch Now" schedule.





## Tags:

#### Action:
[[action.malware.name=Arp]] [[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Agriculture]]

#### Location:
[[victim.continent.name=Asia]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Windows]] [[Hyper-v]] [[Ntfs]] [[Sharepoint]] [[Computerworld]]
#### CVE's
[[CVE-2022-21907]] [[CVE-2022-21840]] [[CVE-2022-21969]] [[CVE-2022-21855]] [[CVE-2022-21846]] [[CVE-2022-21911]]

