# New Windows KB5009543, KB5009566 updates break L2TP VPN connections
### Windows 10 users and administrators report problems making L2TP VPN connections after installing the recent Windows 10 KB5009543 and Windows 11 KB5009566 cumulative updates.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/new-windows-kb5009543-kb5009566-updates-break-l2tp-vpn-connections/
+ Date: 2022-01-12T10:40:38-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/01/13/windows-10-glass-broken.jpg)

![Windows bug](https://www.bleepstatic.com/content/hl-images/2021/01/13/windows-10-glass-broken.jpg)


Windows 10 users and administrators report problems making L2TP VPN connections after installing the recent Windows 10 KB5009543 and Windows 11 KB5009566 cumulative updates.


Yesterday, Microsoft released Windows updates to fix security vulnerabilities and bugs as part of the [January 2022 Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/microsoft-january-2022-patch-tuesday-fixes-6-zero-days-97-flaws/).


These updates include [KB5009566](https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5009566-update-released-with-security-fixes/) for Windows 11 and [KB5009543](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5009543-and-kb5009545-updates-released/) for Windows 10 2004, 20H1, and 21H1.


Updates break L2TP connections
------------------------------


After installing yesterday's updates, Windows users find their L2TP VPN connections broken when attempting to connect using the Windows VPN client.


When attempting to connect to a VPN device, they are shown an error stating, "Can't connect to VPN. The L2TP connection attempt failed because the security layer encountered a processing error during initial negotiations with the remote computer," as shown below.



![Windows error when connecting to an LT2P VPN](https://www.bleepstatic.com/images/news/Microsoft/windows/l/l2tp-vpns-broken/connection-error.jpg)**Windows error when connecting to an LT2P VPN**
The Event Log will also log entries with error code 789, stating that the connection to the VPN failed.



![Windows event log for failed L2TP VPN connection](https://www.bleepstatic.com/images/news/Microsoft/windows/l/l2tp-vpns-broken/event-log.jpg)**Windows event log for failed L2TP VPN connection**
The bug is not affecting all VPN devices and seems only to be affecting users using the built-in Windows VPN client to make the connection.


A security researcher known as [Ronny](https://twitter.com/RonnyTNL) on Twitter told BleepingComputer that the bug affects their Ubiquiti Site-to-Site VPN connections for those using the Windows VPN client.


Many Windows admins also [report](https://www.reddit.com/r/sysadmin/comments/s1oqv8/kb5009543_january_11_2022_breaks_l2tp_vpn/) on Reddit that the bug also affects connections to SonicWall, Cisco Meraki, and WatchGuard Firewalls, with the latter's client also affected by the bug.


With many users still working remotely, admins have been forced to remove the KB5009566 and KB5009543 updates, which immediately fixes the L2TP VPN connections on reboot.


Windows users can remove the KB5009566 and KB5009543 updates using the following commands from an [Elevated Command Prompt](https://www.bleepingcomputer.com/tutorials/how-to-open-a-windows-10-elevated-command-prompt/).



```
Windows 10: wusa /uninstall /kb:5009543
Windows 11: wusa /uninstall /kb:5009566

```

However, as Microsoft bundles all security updates in a single Windows cumulative update, removing the update will remove all fixes for vulnerabilities patched during the January Patch Tuesday. 


Therefore, Windows admins need to weigh the risks of unpatched vulnerabilities versus the disruption caused by the inability to connect to VPN connections.


It is not clear what caused the bug, but Microsoft's January Patch Tuesday fixed numerous vulnerabilities in the Windows Internet Key Exchange (IKE) protocol ([CVE-2022-21843](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21843), [CVE-2022-21890](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21890), [CVE-2022-21883](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21883), [CVE-2022-21889](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21889), [CVE-2022-21848](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21848), and [CVE-2022-21849](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21849)) and in the Windows Remote Access Connection Manager ([CVE-2022-21914](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21914) and [CVE-2022-21885](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2022-21885)) that could be causing the problems.


Unfortunately, there is no known fix or workaround for the L2TP VPN connection issues at this time.


BleepingComputer has reached out to Microsoft about the bug but has not received a reply yet.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Vpn]] [[L2tp]] [[Kb5009543]] [[Kb5009566]] [[Microsoft]] [[Admins]] [[Bleeping Computer]]
#### CVE's
[[CVE-2022-21843]] [[CVE-2022-21890]] [[CVE-2022-21883]] [[CVE-2022-21889]] [[CVE-2022-21848]] [[CVE-2022-21849]] [[CVE-2022-21914]] [[CVE-2022-21885]]

