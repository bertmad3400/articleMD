# Microsoft releases fix for patch that broke VPNs, Hyper-V virtual machines and more | ZDNet
### Microsoft's first Patch Tuesday for 2022 was a rocky start to the year, giving admins and users numerous headaches to deal with.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/microsoft-releases-fix-for-patch-that-broke-vpns-hyper-v-virtual-machines-and-more/
+ Date: 2022-01-19 13:01:46
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/32d5e4606a71596e1ea97276ba10aea050ad4cda/2021/03/19/6c4e4301-f8e2-4321-8518-ecf035f74ec4/istock-992574526-2.jpg?width=770&height=578&fit=crop&auto=webp)

Microsoft has released several out-of-band updates to address features of Windows 11, Windows 10 and Windows Server broken by the January 2022 Patch Tuesday update. 

Microsoft [released the separate fixes on Tuesday](https://docs.microsoft.com/en-us/windows/release-health/windows-message-center#2777) via the Microsoft Update Catalog for direct download, and via Windows Update as an optional update. 


The [Windows Update on January 11](https://www.zdnet.com/article/microsoft-january-2022-patch-tuesday-six-zero-days-over-90-vulnerabilities-fixed/) was intended to address 96 security flaws but also brought a load of pain for users and admins. 

**SEE:** [**Windows 11: Here's how to get Microsoft's free operating system update**](https://www.zdnet.com/article/windows-11-heres-how-to-get-microsofts-free-operating-system-update/#link=%7B%22linkText%22:%22Windows%2011:%20Here's%20how%20to%20get%20Microsoft's%20free%20operating%20system%20update%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/windows-11-heres-how-to-get-microsofts-free-operating-system-update/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)

In release notes for the out-of-band fixes, Microsoft admits the January 2022 security updates [broke some VPN connections](https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2#2773msgdesc), [caused some Windows Servers domain control controllers to restart unexpectedly](https://docs.microsoft.com/en-us/windows/release-health/status-windows-server-2022#2775msgdesc), and [prevented virtual machines in Microsoft's Hyper-V from starting](https://docs.microsoft.com/en-us/windows/release-health/status-windows-8.1-and-windows-server-2012-r2#2776msgdesc). On top of this, users discovered a windows Resilient File System (ReFS) [issue blocked access to volumes stored on removable media](https://support.microsoft.com/en-gb/topic/kb5010691-refs-formatted-removable-media-may-fail-to-mount-or-mounts-as-raw-after-installing-the-january-11-2022-windows-updates-7a959f37-91b6-4baf-a797-829b0ee86c65), including external USB drives.

The issues affected the Windows 10 21H2 update ([KB5009566](https://support.microsoft.com/en-gb/topic/january-11-2022-kb5009543-os-builds-19042-1466-19043-1466-and-19044-1466-b763552f-73bd-435a-b220-fc3e0bc9765b)), Windows 11 update ([KB5009566](https://support.microsoft.com/en-gb/topic/january-11-2022-kb5009566-os-build-22000-434-eee797fa-5ee3-4501-aeec-db3bc73b2c7b)), and Windows Server 2022 update ([KB5009555](https://support.microsoft.com/en-gb/topic/january-11-2022-kb5009555-os-build-20348-469-e3fb2b38-3506-4dc9-8216-5d3546a6d2a4)), as well as the security updates for older versions of Windows and Windows Server. 

Microsoft has released fixes in the out-of-band updates KB5010795 for Windows 11, KB5010796 for Windows Server 2022, KB5010793 for Windows 10 21H2, 21H1 20H2 and 20H1, [as detailed in its Windows release health dashboard](https://docs.microsoft.com/en-us/windows/release-health/windows-message-center#2777). 






Updates are also available for all versions through to Windows 7 Service Pack 1 and Windows Server 2008 Service Pack 2. These are cumulative updates, meaning previous updates don't need to be installed before installing it. 

The VPN issue affected Windows 11 through to Windows 10 Enterprise 2015 LTSB and stemmed from IP Security (IPSEC) connections which contain a Vendor ID failing. VPN connections using Layer 2 Tunneling Protocol (L2TP) or IP security Internet Key Exchange (IPSEC IKE) might also be affected, according to Microsoft. 

The issue causing Windows Server domain controllers (DCs) to restart affected Windows Server 2022 through to Windows Server 2012. Windows Server 2016 and later was more likely to be affected when DCs are using Shadow Principals in Enhanced Security Admin Environment (ESAE) or environments with Privileged Identity Management (PIM), according to Microsoft. 

Hyper-V VMs were failing to start on devices with Unified Extensible Firmware Interface (UEFI) enabled on Windows 8.1, and Windows Server 2012 R2 and Windows Server 2012. 

The ReFS issue caused removable volumes formatted with ReFS to fail to mount or for it to mount as RAW. Its likely cause was that the ReFS file system isn't supported on removable media, including external USB drives, according to Microsoft. Also, the fix appears to be more complicated than just installing the out-of-band patch.  

Microsoft [recommends](https://support.microsoft.com/en-gb/topic/kb5010691-refs-formatted-removable-media-may-fail-to-mount-or-mounts-as-raw-after-installing-the-january-11-2022-windows-updates-7a959f37-91b6-4baf-a797-829b0ee86c65) uninstalling the January 11 update and following several steps to recover data from a ReFS partition before installing the out-of-band update. The recovery steps include ensuring data contained on the affected removable media is moved to a ReFS volume on a different fixed device or to a NTFS volume. 

"After data is recovered from the ReFS partition on the removable media, install the January 17, 2022 Windows out-of-band update that is applicable for your Windows operating system," Microsoft says. 

The issues that surfaced after Microsoft's first Patch Tuesday for 2022 aren't likely to inspire confidence amongst Windows admins who've long been skeptical about the quality of Microsoft's updates and whether it does sufficient testing before their release. 

[As Ask Woody's influential IT admin blogger Susan Bradley recently argued in 2020](https://www.zdnet.com/article/windows-10-patch-expert-dear-mr-panay-please-fix-microsofts-buggy-updates/), Microsoft's decision to roll up patches in a big bundle on the second Tuesday of every month requires admins to place a great deal of trust in the company. That trust is eroded if applying the updates results in a lag on productivity from buggy patches.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[Out-of-band]] [[Admins]] [[Vpn]] [[ZDNet]]

