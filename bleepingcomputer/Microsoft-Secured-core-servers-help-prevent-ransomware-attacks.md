# Microsoft: Secured-core servers help prevent ransomware attacks
### Microsoft says the first Secured-core certified Windows Server and Microsoft Azure Stack HCI devices are now available to protect customers' networks from security threats, including ransomware attacks.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-secured-core-servers-help-prevent-ransomware-attacks/
+ Date: 2021-12-08T14:25:26-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/09/05/Microsoft_header.jpg)

![Microsoft: Secured-core servers help prevent ransomware attacks](https://www.bleepstatic.com/content/hl-images/2021/09/05/Microsoft_header.jpg)


Microsoft says the first Secured-core certified Windows Server and Microsoft Azure Stack HCI devices are now available to protect customers' networks from security threats, including ransomware attacks.


Secured-core devices are marketed as a solution to the increasing number of firmware vulnerabilities attackers can exploit to bypass a Windows machines' Secure Boot and the lack of visibility at firmware level in today's endpoint security solutions.


All [Secured-core devices](https://www.bleepingcomputer.com/news/security/windows-10-secured-core-pcs-can-block-driver-abusing-malware/) come with built-in protection for threats that abuse firmware and driver security flaws are since [October 2019](https://www.bleepingcomputer.com/news/security/new-windows-10-secured-core-pcs-block-firmware-level-attacks/). They can help defend against malware designed to take advantage of driver security flaws to disable security solutions.


Credential theft blocking capabilities
--------------------------------------


The newly certified Secured-core servers use [Secure boot](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-secure-boot) and the [Trusted Platform Module](https://docs.microsoft.com/en-us/windows/security/information-protection/tpm/trusted-platform-module-top-node) 2.0 to ensure that only trusted will be able to load on boot.


They also leverage [Dynamic Root of Trust Measurement](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/how-hardware-based-root-of-trust-helps-protect-windows#secure-launchthe-dynamic-root-of-trust-for-measurement-drtm) (DRTM) to launch the operating system into a trusted state, blocking malware attempts to tamper with the system.


Secured-core servers also use [Hypervisor-Protected Code Integrity](https://techcommunity.microsoft.com/t5/windows-insider-program/virtualization-based-security-vbs-and-hypervisor-enforced-code/m-p/240571) (HVCI) to block all executables and drivers (such as Mimikatz) not signed by known and approved authorities from launching.


"Additionally, since [Virtualization-based security](https://techcommunity.microsoft.com/t5/windows-insider-program/virtualization-based-security-vbs-and-hypervisor-enforced-code/m-p/240571) (VBS) is enabled out of the box, IT administrators can easily enable features, such as [Credential Guard](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/comprehensive-protection-for-your-credentials-with-credential/ba-p/765314), which safeguard the credentials in an isolated environment that is invisible to attackers," Microsoft said.


By blocking credential theft attempts, Secured-core servers can help make it much harder for threat actors (including ransomware gangs such as REvil) to move laterally through the network, thus stopping their attacks before they can gain persistence and deploy their payloads.


For instance, Secured-core servers would have stopped RobbinHood Ransomware operators from [exploiting a vulnerable GIGABYTE driver](https://www.bleepingcomputer.com/news/security/ransomware-exploits-gigabyte-driver-to-kill-av-processes/) to elevate privileges and install malicious unsigned Windows drivers.


This made it possible to terminate antivirus and security software processes on compromised systems to bypass anti-ransomware defenses and deploy their payloads across the victim's network.



![REvil ransomware attack flow](https://www.bleepstatic.com/images/news/u/1109292/2021/REvil-ransomware-attack-flow.jpg)*REvil ransomware attack flow (Microsoft)*
Servers running Azure Stack HCI and Windows Server
--------------------------------------------------


Dozens of models with Secured-core server functionality are now available in the [Azure Stack HCI catalog](https://hcicatalog.azurewebsites.net/#/catalog?FeatureSupported=securedCoreServer) and the [Windows Server Catalog](https://www.windowsservercatalog.com/results.aspx?&bCatID=1333&cpID=0&avc=10&ava=0&avt=0&avq=140&OR=1&PGS=25&PG=1) lists.


You can manage the servers' configuration and status together with all Windows clients on the network through the locally deployed and browser-based Windows Admin Center app.


"The Windows Admin Center UI allows you to easily configure the six features that encompass Secured-core server: Hypervisor Enforced Code Integrity, Boot Direct Memory Access (DMA) Protection, System Guard, Secure Boot, Virtualization-based security, and Trusted Platform Module 2.0," Microsoft [added](https://www.microsoft.com/security/blog/2021/12/07/new-Secured-core-servers-are-now-available-from-the-microsoft-ecosystem-to-help-secure-your-infrastructure/).


Redmond first announced that [Windows Server 2022 will expand Secured-core](https://www.bleepingcomputer.com/news/security/microsoft-announces-windows-server-2022-with-new-security-features/) to the Windows Server platform when the new release entered preview in March.





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Expand]] [[action.malware.name=Mimikatz]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=REvil]] [[action.malware.name=RobbinHood]] [[action.malware.name=RTM]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Secured-core]] [[Windows]] [[Microsoft]] [[Hci]] [[Ransomware]] [[Bleeping Computer]]

