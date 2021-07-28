# Windows 10: Microsoft's latest update fixes printer smart card bug
### Microsoft issues more fixes a widespread printer bug caused by updates in the July 2021 Patch Tuesday.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/windows-10-microsofts-latest-update-fixes-printer-smart-card-bug/)
+ Date: July 28, 2021 -- 09:16 GMT (10:16 BST)
+ Author: Liam Tung


## Article:
Unknown

Microsoft has released an out of band non-security update to fix a bug in some business printers and scanners that use a smart card for authentication. 

The update, [KB5005394](https://support.microsoft.com/en-us/topic/july-27-2021-kb5005394-os-build-17763-2091-out-of-band-58863c8f-e514-47cc-b68e-14dbb883777f), addresses an issue in Windows 10 version 1809 — Windows 10 Enterprise 2019 LTSC — that caused printers, scanners and multifunctional devices (MFDs) to not function. The update bumps up the OS build number to 17763.2091. 


The issue stems from a July 13 update to harden the Windows 10 against the security vulnerability [tagged as CVE-2021-33764](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-33764). 

Printers and MFDs that were affected were not compliant with the [authentication specification RFC 4556](https://www.ietf.org/rfc/rfc4556.txt). Microsoft advised admins to verify that the latest firmware and drivers for these devices were installed and promised a mitigation, which it's been delivering to different versions of Windows 10 over the past week.

This was a separate issue to the so-called [PrintNightmare bugs that Microsoft patched](https://www.zdnet.com/article/microsofts-printnightmare-patch-is-now-causing-problems-for-some-printers/) ahead of the July 2021 Patch Tuesday security update, and the [Windows Print Spooler bug it fixed this month](https://www.zdnet.com/article/windows-print-spooler-hit-with-local-privilege-escalation-vulnerability/).  

Microsoft released fixes for the same smart card authentication issue for newer versions of Windows 10 last week. 

"After installing updates released July 13, 2021 on domain controllers (DCs) in your environment, printers, scanners, and multifunction devices that are not compliant with section 3.2.1 of [RFC 4556 spec](https://www.ietf.org/rfc/rfc4556.txt) might fail to print when using smart card (PIV) authentication," [it noted](https://support.microsoft.com/en-gb/topic/july-13-2021-kb5004237-os-builds-19041-1110-19042-1110-and-19043-1110-ae798d3c-3de3-4c1f-b9d9-7391b71da889) in advisories [for Windows 10 20H1](https://support.microsoft.com/en-gb/topic/july-13-2021-kb5004237-os-builds-19041-1110-19042-1110-and-19043-1110-ae798d3c-3de3-4c1f-b9d9-7391b71da889) and [Windows 10 2004](https://support.microsoft.com/en-gb/topic/july-13-2021-kb5004237-os-builds-19041-1110-19042-1110-and-19043-1110-ae798d3c-3de3-4c1f-b9d9-7391b71da889). 






In a [separate support note](https://support.microsoft.com/en-us/topic/kb5005408-smart-card-authentication-might-cause-print-and-scan-failures-514f0bc5-ecde-4e5e-8c5a-2a776d7fb89a), Microsoft explains printers and MFDs were affected if they don't support Diffie-Hellman for key-exchange or or advertise support for des-ede3-cbc ("triple DES") during PKINIT Kerberos authentication. 

The issue [affected all versions of Windows](https://docs.microsoft.com/en-us/windows/release-health/status-windows-10-21h1#issue-details), including: 

* Client: Windows 10, version 21H1; Windows 10, version 20H2; Windows 10, version 2004; Windows 10, version 1909; Windows 10, version 1809; Windows 10 Enterprise LTSC 2019; Windows 10 Enterprise LTSC 2016; Windows 10, version 1607; Windows 10 Enterprise 2015 LTSB; Windows 8.1; Windows 7 SP1
* Server: Windows Server, version 20H2; Windows Server, version 2004; Windows Server, version 1909; Windows Server, version 1809; Windows Server 2019; Windows Server 2016; Windows Server 2012 R2; Windows Server 2012; Windows Server 2008 R2 SP1; Windows Server 2008 SP2





#### Tags:
[[Windows]] [[Microsoft]] [[Server,]] [[LTSC]] [[ZDNet]]
