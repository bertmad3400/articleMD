# Microsoft touts first PCs to ship natively with secure Pluton chip
### Along with thwarting malware, the Pluton chip handles BitLocker, Windows Hello, and System Guard and might help prevent physical insider attacks. The technology is also being used in Azure Sphere in the cloud.

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3646749/microsoft-touts-first-pcs-to-ship-natively-with-secure-pluton-chip.html
+ Date: 2022-01-12T03:00-05:00
+ Author: Lucas Mearian


## Article:
![Article Image](https://images.idgesg.net/images/article/2017/10/thinkstockphotos-499123970-100738770-large.jpg?auto=webp&quality=85,70)

As organizations continue to wrestle with how to manage a hybrid workforce, security outside the corporate firewall continues to play a huge role in day-to-day IT operations.

Following the October release of Windows 11, which boasted features aimed at enabling hybrid work, Microsoft last week announced the first PCs with its Pluton chip-to-cloud security technology. The technology is aimed at securing the computers of remote workers and others.

At [CES](https://www.ces.tech), Microsoft announced that Lenovo and chipmaker AMD have launched the first laptops — the ThinkPad Z13 and ThankPad Z16 — that come natively with the Pluton security chips. Pricing for the ThinkPad Z13 starts at $1,549, pricing for the ThinkPad Z16 starts at $2,099. Both laptops will be available in May and Lenovo said there is no additional cost associated with the Pluton chip inside.

Pluton will be disabled by default on 2022 Lenovo ThinkPad platforms (specifically, the Z13, Z16, T14, T16, T14s, P16s, and X13 using AMD 6000-series processors). Customers will have the ability to enable Pluton themselves, a Lenovo spokesperson said.

Asked why the chip is initially disabled, the spokesperson said enterprise customers "have told us they extensively test and evaluate any new security-related software or feature that will be introduced into their network and can choose to enable Pluton on their devices as they see fit. As Pluton rolls out into market and we have time to assess the customer demand for factory enablement, we will review enabling [it]."

The Pluton processor is aimed at delivering greater protection than the existing Trusted Platform Module (TPM) as it’s a dedicated security chip that handles security features such as BitLocker, Windows Hello, and System Guard.

Windows 11 came with [a plethora of security updates](https://www.computerworld.com/article/3637054/just-who-is-windows-11-for-anyway.html), not the least of which was the inability to disable existing features such as UEFI, Secure book, and the cryptographic TPM. Windows 11 is a Zero Trust-ready operating system designed to be secure from the chip to the cloud, with verifiable security verifications built in and turned on by default.

TPM 2.0 is used to generate and protect encryption keys, user credentials, and other sensitive data so malware and attackers can’t access or tamper with data.

The Pluton chip is [a purpose-built security processor](https://blogs.windows.com/windowsexperience/2022/01/04/ces-2022-chip-to-cloud-security-pluton-powered-windows-11-pcs-are-coming/) developed through a joint effort between Microsoft and top silicon makers, including AMD and Qualcomm. It’s aimed at protecting PCs against some of the most sophisticated malware attacks by more securely storing user credentials (including fingerprint information), identities, personal data, and encryption keys. The embedded security processor brings together the functionality of TPM 2.0 with the ability to update and dynamically add new security features seamlessly through [Windows Update](https://support.microsoft.com/en-us/windows/update-windows-3c5ae7fc-9fb6-9af1-1984-b5e0412c556a), the Microsoft service that installs the latest software/firmware on a computer.

The “tightly integrated hardware and software” helps protect against security vulnerabilities by adding additional visibility and control, and is more adaptable to changes in the threat landscape, according to Microsoft.

The Pluton chip is integrated into the die of a device’s CPU and is therefore more difficult for attackers to access. Sensitive information stored in it can’t be removed — even if an attacker has installed malware or has physical possession of the PC — because the chip is isolated from the rest of the system. The discrete chip also helps prevent emerging attack techniques, such as speculative execution (a side channel attack) that exploits CPU behavior and functionality.

Pluton can act as a TPM or provide additional security to a device in conjunction with a third-party discrete TPM, according to Matt Wo, a spokesperson for Microsoft Cybersecurity.

“Our partners have the choice and flexibility in offering Pluton with or without a third-party TPM,” Wo said in an email response to Computerworld. “When Pluton is configured as a TPM, it protects the BitLocker keys used to help encrypt and protect customer data stored on the system.”

Patrick Hevesi, a vice president analyst at Gartner, said the biggest benefit of the Pluton chip is the possible elimination of the physical side channel attacks against standalone TPM-to-CPU communication channels.

[Side-channel attacks](https://www.csoonline.com/article/3388647/what-is-a-side-channel-attack-how-these-end-runs-around-encryption-put-everyone-at-risk.html) don’t target weaknesses in the crypto-systems themselves; instead, the malware looks for information leaks that may indicate something about the cryptographic system’s operation. For example, acoustic attacks can record the sound of a user's key strokes to steal their passphrase or the electromagnetic field (EMF) radiation emitted by a computer screen can be used to view information before it's encrypted.

"Since the Pluton security process will be built right into the System on a Chip (SoC) chips, there should be no way to get to the channel without destroying the chip,"  Hevesi said via email. "Also, according to Microsoft’s specifications, the keys will never leave the Pluton Security boundary, which will help prevent attacks like speculative execution and other key material types of attacks."

Another benefit of the Pluton architecture is that Microsoft will control the firmware updates to the security processor and allow for direct updates from Windows Update; that allows the company to control and secure the firmware code and continue to add new security features as new versions of Windows roll out, according to Hevesi.

Microsoft will also be able to advance the hardware and software security features such as secure boot, measured boot, and virtualization-based security right on a single SoC processor.

"This will help prevent even remote attacks that try to change the kernel or OS boot process. The Pluton chip will help secure remote devices because of both the physical layer and software based security feature integrations," Hevesi said. "This technology also can apply to devices on-premises to possibly prevent physical insider attacks and they have also added this technology to [Azure Sphere](https://azure.microsoft.com/en-us/services/azure-sphere/) in the cloud."

Not everyone believes the new Pluton chip is the security be-all-to-end-all. 

Michael Suby, research vice president for IDC's Security and Trust research service, said the SoC platform is a useful advance that in the short term won't radically change corporate PC-purchasing decisions.

"A potential exploit sequence of threat actors could clandestinely take physical possession of the executive’s laptop, crack open the device and infect it at the hardware level, and then leave the device, seemingly undisturbed to the executive and potential IT security teams as well," Suby said.

Lenovo’s new laptops are powered by AMD Ryzen 6000 Series processors, which integrate the Pluton Security chip on new Windows 11 PCs. The Pluton chip is built on technology used for years in Microsoft Xbox and Microsoft Azure Sphere.

“As we move into this new era of hybrid work, you need modern security solutions that deliver end-to-end protection from wherever you are,” Wo said. “Windows 11 was designed to raise the bar on security, out of the box, to enable protections like Windows Hello, Device Encryption, virtualization-based security (VBS), hypervisor-protected code integrity (HVCI), and Secure Boot — a combination that has been shown to reduce malware by 60%.”

Microsoft said many of the upgrades in Windows 11 and the collaborative chip design were inspired by hybrid work themes.

“It is clear the past few years have fostered great learnings that our partners have integrated into the design of these devices. These learnings — and the new ways of working — also influenced many of the innovations in the design of Windows 11,” Nicole Dezen, vice president of Microsoft Device Partner Sales, said in [a blog post](https://blogs.windows.com/windowsexperience/2022/01/05/windows-11-devices-at-ces-showcase-industry-leading-sustainability-powerful-hybrid-work-and-robust-security/).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Manufacturing]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[Malware]] [[Lenovo]] [[Amd]] [[Thinkpad]] [[Pcs]] [[Laptops]] [[Z13]] [[Z16]] [[Computerworld]]

