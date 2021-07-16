# Windows 10 21H2 preview released with new security features
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-10-21h2-preview-released-with-new-security-features/)
+ Date: July 16, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 10](https://www.bleepstatic.com/content/hl-images/2021/02/04/Windows_10.jpg)


Microsoft has officially announced the Windows 10 21H2 feature update (build 19044.1147) and released the first preview to Insiders for testing.


While Windows 11 is the hot topic right now, most enterprise users will likely be staying with Windows 10 until the bugs are worked out of the new operating system.


Microsoft will continue to release Windows 10 feature updates, such as Windows 10 21H2, through October 2025 to allow businesses and consumers time to switch to Windows 11.


As most of the development for new features is going into Windows 11, Microsoft will be releasing limited features for Windows 10 going forward.


"Windows 10, version 21H2 will have a scoped set of features focused on productivity and security, prioritized to meet our customers’ needs based on feedback," Microsoft's John Cable, Vice President, Program Management, Windows Servicing and Delivery, explained in a [blog post](https://blogs.windows.com/windowsexperience/2021/07/15/introducing-the-next-feature-update-to-windows-10-21h2/) tonight.


Limited release of Windows 10 21H2
----------------------------------


While many may be excited to try out the Windows 10 21H2 release, Microsoft is not making it available to everyone at this point.


For the initial test, Microsoft is only making the new Windows 10 21H2 feature update available to Windows Insiders who were moved from the 'Beta' channel to the 'Release' because their PC did not meet the system requirements for Windows 11.


Even for these users, Microsoft is only making it available to 'Seekers,' or those who manually check for updates in Windows Update.


After installing the update, Windows 10 will be upgraded to build 19044.1147.


Windows 10 21H2 will receive 18 months of support for Home and Pro editions and 30 months of support for Enterprise and Education editions.


Microsoft also states that they will be launching "the next version of the Windows 10 Long-Term Servicing Channel (LTSC) based on version 21H2 at the same time, and it will have five years of servicing as announced in February."


What's coming in Windows 10 21H2
--------------------------------


Windows 10 21H2 is not a big release compared to Windows 11 but does include some new and interesting security and business features.


With this release, Microsoft adds support for the WPA3 H2E (Hash-to-Element) protocol, which provides increased security against current and future side-channel attacks.


In 2019, researchers disclosed a new side-channel attack called "[DragonBlood](https://www.bleepingcomputer.com/news/security/wpa3-wi-fi-standard-affected-by-new-dragonblood-vulnerabilities/)" that could be used to steal a WPA3 password.


"These attacks resemble dictionary attacks and allow an adversary to recover the password by abusing timing or cache-based side-channel leaks. Our sidechannel attacks target the protocol's password encoding method" said [Mathy Vanhoef](https://twitter.com/vanhoefm) (NYUAD) and [Eyal Ronen](https://eyalro.net/) (Tel Aviv University & KU Leuven) in their research paper.


In response to the researcher, the Hash-to-Element protocol was added to WPA3's Simultaneous Authentication of Equals (SAE) authentication protocol to prevent these types of side-channel attacks.


"In 2019 the Dragonblood paper revealed that certain theoretical vulnerabilities in SAE were feasible to exploit in practice, enabling an active attacker to recover the password using side channel attacks," explained Cisco in a recent [blog post](https://blogs.cisco.com/networking/wpa3-bringing-robust-security-for-wi-fi-networks).


"In response to the Dragonblood paper, IEEE 802.11 updated SAE by defining a new “Hash-to-Element” (H2E) method, as an optional alternative to the existing “Hunting-and-Pecking” method for the secret PWE (Password Element) derivation used in SAE authentication. H2E is significantly more computationally efficient and provides robust resistance to side channel attack.


Windows 10 21H2 also brings [GPU compute](https://docs.microsoft.com/en-us/windows/wsl/tutorials/gpu-compute), the #1 most requested feature, to the Windows Subsystem for Linux and Azure IoT Edge for Linux on Windows.


This feature allows Windows users to use their graphics card to "to accelerate math-heavy workloads and uses its parallel processing to complete the required calculations faster, in many cases, than utilizing only a CPU.


To use this feature, you will need Hyper-V and WSL2 installed.


Finally, this feature update improves Windows Hello for Business by supporting passwordless deployment models for easy rollouts of new machines predefined security policies.


Microsoft states that some of these features are not currently enabled in Windows 10 21H2 and will be available in future builds.




#### Tags:
[[Windows]] [[21H2]] [[Microsoft]] [[side-channel]] [[WPA3]] [[H2E]] [[Hash-to-Element]] [[Bleeping Computer]]
