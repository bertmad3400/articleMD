# Windows 10 security: Here's how researchers managed to fool Windows Hello
### Tricking Window's facial recognition security takes quite a bit of work. Here's how they did it.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/windows-10-security-heres-how-researchers-managed-to-fool-windows-hello/)
+ Date: July 19, 2021 -- 09:57 GMT (10:57 BST)
+ Author: Liam Tung


## Article:
Unknown

Security researchers have shown how they were able to bypass Windows 10's Windows Hello biometric authentication with just a single infrared frame of the target. 

Researchers at security firm Cyber Ark have detailed the Windows Hello authentication bypass and how an attacker could exploit it. 


The attack is quite elaborate and would require planning, including being able to acquire an infrared (IR) image of the target's face and building a custom USB device, such as a USB web camera, that will work with Windows Hello. The attack exploits how Windows 10 treats these USB devices and would require the attacker to have gained physical access to the target PC.

**SEE:** [**Windows 10 Start menu hacks**](https://www.techrepublic.com/resource-library/whitepapers/windows-10-start-menu-hacks/?ftag=CMG-01-10aaa1b) **(TechRepublic Premium)**

But with those pieces in place, an attacker could gain access to sensitive information on the target's Windows 10 PC – and potentially information stored in Microsoft 365 cloud services.

"With only one valid IR frame of the target, the adversary can bypass the facial recognition mechanism of Windows Hello, resulting in a complete authentication bypass and potential access to all the victim's sensitive assets," [Cyber Ark researcher Omer Tsarfati explained in a blogpost](https://www.cyberark.com/resources/threat-research-blog/bypassing-windows-hello-without-masks-or-plastic-surgery). 

The attacker could capture an IR frame of the target or convert a regular RGB frame into an IR frame. 






The apparent weakness lies in how Windows Hello processes "public" data, such as the image of the person's face, from a USB device, so long as the device meets Windows Hello requirements that the camera has both IR and RGB sensors. 

The researchers discovered that only the IR camera frames are processed during authentication, so an attacker just needs a valid IR frame to bypass Windows Hello authentication. The RGB frames can contain anything. During tests, Tsarfati used an RGB frame of SpongeBob and the bypass still worked. 

Tsarfati argued it would be fairly simple to get an IR frame of the target. For example, walking by the person with an IR camera or placing it where the target will likely walk through, such as an elevator. The image could even be snapped at a distance with higher-end infrared sensors.

Tsarfati noted that Microsoft addressed the vulnerability last week and [has tagged it as CVE-2021-34466](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-34466).    

**SEE:**[**Ransomware: Paying up won't stop you from getting hit again, says cybersecurity chief**](https://www.zdnet.com/article/ransomware-paying-up-wont-stop-you-from-getting-hit-again-says-cybersecurity-chief/#link=%7B%22linkText%22:%22Ransomware:%20Paying%20up%20won't%20stop%20you%20from%20getting%20hit%20again,%20says%20cybersecurity%20chief%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/ransomware-paying-up-wont-stop-you-from-getting-hit-again-says-cybersecurity-chief/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)

Microsoft said that the attacker would need physical access and that it is a complex attack to pull off. Microsoft noted it is an important patch to apply, but its description suggests it's nothing an admin should lose sleep over. 

"A successful attack depends on conditions beyond the attacker's control. That is, a successful attack cannot be accomplished at will, but requires the attacker to invest in some measurable amount of effort in preparation or execution against the vulnerable component before a successful attack can be expected," Microsoft noted. 

"For example, a successful attack may require an attacker to: gather knowledge about the environment in which the vulnerable target/component exists; prepare the target environment to improve exploit reliability; or inject themselves into the logical network path between the target and the resource requested by the victim in order to read and/or modify network communications (e.g., a man in the middle attack)."





#### Tags:
[[Windows]] [[USB]] [[Microsoft]] [[Tsarfati]] [[RGB]] [[ZDNet]]
