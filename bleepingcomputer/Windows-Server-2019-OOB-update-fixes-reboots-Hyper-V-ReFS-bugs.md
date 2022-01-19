# Windows Server 2019 OOB update fixes reboots, Hyper-V, ReFS bugs
### Microsoft has released an emergency out-of-band (OOB) update for Windows Server 2019 that fixes numerous critical bugs introduced during the January 2022 Patch Tuesday.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/windows-server-2019-oob-update-fixes-reboots-hyper-v-refs-bugs/
+ Date: 2022-01-18T18:14:38-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/13/windows-server-on-fire.jpg)

![Windows Server on fire](https://www.bleepstatic.com/content/hl-images/2022/01/13/windows-server-on-fire.jpg)


Microsoft has released an emergency out-of-band (OOB) update for Windows Server 2019 that fixes numerous critical bugs introduced during the January 2022 Patch Tuesday.


Soon after Windows Server admins installed the January 2022 updates, they [began reporting severe issues](https://www.bleepingcomputer.com/news/microsoft/new-windows-server-updates-cause-dc-boot-loops-break-hyper-v/), including domain controllers entering into boot loops, Hyper-V no longer starting, L2TP VPN connections failing, and ReFS volumes becoming inaccessible.


The issues were severe enough that many admins chose to uninstall the updates and forgo the included security fixes so that their servers could operate correctly again.


OOB updates for all Server versions released
--------------------------------------------


Yesterday, [Microsoft released OOB updates](https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-emergency-fixes-for-windows-server-vpn-bugs/) for Windows Server 2022, Windows Server 20H2, Windows Server 20H1, Windows Server 2016, and Windows Server 2012 R2 to fix all of these issues.


Microsoft also released security updates for Windows 10, Windows 8, and Windows 7 operating systems to resolve the LT2P connection issues.


However, the KB5010791 OOB update for Windows 2019 was not ready yesterday and was finally released this evening with the following fixes:


* Addresses a known issue that might cause IP Security (IPSEC) connections that contain a Vendor ID to fail. VPN connections using Layer 2 Tunneling Protocol (L2TP) or IP security Internet Key Exchange (IPSEC IKE) might also be affected.
* Addresses a known issue that might cause Windows Servers to restart unexpectedly after installing the January 11, 2022 update on domain controllers (DCs).
* Addresses an issue that prevents Active Directory (AD) attributes from being written properly during a Lightweight Directory Access Protocol (LDAP) modify operation when you make multiple attribute changes.
* Addresses an issue that might prevent removable media that is formatted using the Resilient File System (ReFS) from mounting or might cause the removable media to mount in the RAW file format. This issue occurs after installing the January 11, 2022 Windows update.

Microsoft states that the Windows Server 2019 KB5010791 update is available for Windows Update and the [Microsoft Catalog](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5010791). However, it is not currently available in WSUS and must be [imported manually](https://docs.microsoft.com/en-us/windows-server/administration/windows-server-update-services/manage/wsus-and-the-catalog-site#the-microsoft-update-catalog-site).


The complete list of the OOB updates released to fix the January 2022 bugs are listed below.


The following updates can only be downloaded and installed via the Microsoft Update Catalog:


* Windows 8.1, Windows Server 2012 R2: [KB5010794](https://support.microsoft.com/help/5010794)
* Windows Server 2012: [KB5010797](https://support.microsoft.com/help/5010797)

Updates for the following Windows versions are also available through Windows Update as an optional update:


* Windows 11, version 21H1 (original release): [KB5010795](https://support.microsoft.com/help/5010795)
* Windows Server 2022: [KB5010796](https://support.microsoft.com/help/5010796)
* Windows 10, version 21H2: [KB5010793](https://support.microsoft.com/help/5010793)
* Windows 10, version 21H1: [KB5010793](https://support.microsoft.com/help/5010793)
* Windows 10, version 20H2, Windows Server, version 20H2: [KB5010793](https://support.microsoft.com/help/5010793)
* Windows 10, version 20H1, Windows Server, version 20H1: [KB5010793](https://support.microsoft.com/help/5010793)
* Windows 10, version 1909, Windows Server, version 1909: [KB5010792](https://support.microsoft.com/help/5010792)
* Windows Server 2019: [KB5010791](https://support.microsoft.com/en-us/topic/january-18-2022-kb5010791-os-build-17763-2458-out-of-band-43697313-d8e0-4918-b6df-7f64d4d9a8cd)
* Windows 10, version 1607, Windows Server 2016: [KB5010790](https://support.microsoft.com/help/5010790)
* Windows 10, version 1507: [KB5010789](https://support.microsoft.com/help/5010789)
* Windows 7 SP1: [KB5010798](https://support.microsoft.com/help/5010798)
* Windows Server 2008 SP2: [KB5010799](https://support.microsoft.com/help/5010799)

Windows Server admins who installed yesterday's OOB updates report that they fixed the issues with the January updates.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[Oob]] [[Kb5010793]] [[Admins]] [[20h2]] [[20h1]] [[Kb5010791]] [[Bleeping Computer]]

