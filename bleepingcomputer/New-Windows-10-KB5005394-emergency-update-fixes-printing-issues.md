# New Windows 10 KB5005394 emergency update fixes printing issues
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/new-windows-10-kb5005394-emergency-update-fixes-printing-issues/)
+ Date: July 27, 2021
+ Author: Sergiu Gatlan


## Article:
![New Windows 10 KB5005394 emergency update fixes printing issues](https://www.bleepstatic.com/content/hl-images/2021/01/25/Windows-10.jpg)


Microsoft has released a cumulative out-of-band update to fix a known printing issue preventing some printers and scanners from working correctly.


"Addresses an issue with devices that do not comply with section 3.2.1 of the RFC 4556 specification," Microsoft explains in the [KB5005394](https://support.microsoft.com/en-us/topic/july-27-2021-kb5005394-os-build-17763-2091-out-of-band-58863c8f-e514-47cc-b68e-14dbb883777f) support document.


"Noncompliant printers, scanners, and multifunction devices might not work when you use smart card authentication (PIV). This issue occurs after you install the July 13, 2021 update on domain controllers (DC) in your environment."


Fixed on a limited number of affected Windows versions
------------------------------------------------------


The printing issues affect both client and server Windows platforms, starting with Windows 7 SP1 / Windows Server 2008 SP2 and later:


* Client: Windows 10, version 21H1; Windows 10, version 20H2; Windows 10, version 2004; Windows 10, version 1909; Windows 10, version 1809; Windows 10 Enterprise LTSC 2019; Windows 10 Enterprise LTSC 2016; Windows 10, version 1607; Windows 10 Enterprise 2015 LTSB; Windows 8.1; Windows 7 SP1
* Server: Windows Server, version 20H2; Windows Server, version 2004; Windows Server, version 1909; Windows Server, version 1809; Windows Server 2019; Windows Server 2016; Windows Server 2012 R2; Windows Server 2012; Windows Server 2008 R2 SP1; Windows Server 2008 SP2


However, based on the support document published today, **the** **KB5005394 cumulative update released today by Microsoft only applies to** Windows 10 1809, Windows Server 1809, and Windows Server 2019.


This out-of-band update can only be installed manually as a standalone package available for download through the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5005394).


Microsoft has also released **[KB5005392](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5005392) to address the printing issues** on [Windows 7 SP1 or Windows Server 2008 R2 SP1 devices](https://support.microsoft.com/en-us/topic/kb5005392-noncompliant-devices-might-not-work-when-using-piv-after-installing-the-july-13-2021-update-for-windows-7-sp1-or-windows-server-2008-r2-sp1-2e410b99-3645-4321-a5a2-404027900fce).


When [it confirmed this known printing issue on Friday](https://www.bleepingcomputer.com/news/microsoft/windows-10-july-security-updates-break-printing-on-some-systems/), Microsoft also added that all affected smart card authenticating devices **should work as expected when using username and password authentication**.


Issue caused by security flaw hardenings
----------------------------------------


The known issue is caused by hardening changes for [CVE-2021-33764](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-33764). It only impacts smart card authenticating printers, scanners, and multifunction devices, which "don't support DH or advertise support for des-ede3-cbc ("triple DES") during the Kerberos AS request."


Affected Windows 10 users are advised to first check if they have the latest drivers and firmware installed for non-compliant and misbehaving printers or scanners.


If the devices are up-to-date, impacted users should contact the device manufacturer and ask for setting changes or updates to make the printer or scanner compliant with the CVE-2021-33764 hardenings deployed via July's Windows 10 security updates.


Microsoft is still working to mitigate the issue on all affected Windows versions to re-enable printing and scanning on impacted devices.


"This will allow time for device manufacturers to release compliant firmware and drivers for their devices," Microsoft [explains](https://support.microsoft.com/en-us/topic/kb5005408-smart-card-authentication-might-cause-print-and-scan-failures-514f0bc5-ecde-4e5e-8c5a-2a776d7fb89a). 


"Further, it should allow time to update settings, firmware, and drivers in your environment and make them compliant."




#### Tags:
[[Windows]] [[Microsoft]] [[SP1]] [[Server,]] [[Bleeping Computer]]
