# Windows Hello Bypass Fools Biometrics Safeguards in PCs
### A Windows security bug would allow an attacker to fool a USB camera used in the biometric facial-recognition aspect of the system.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167771)
+ Date: July 14, 2021  7:05 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/14065419/Windows-Hello-e1626260072511.jpg)
A vulnerability in Microsoft’s Windows 10 password-free authentication system has been uncovered that could allow an attacker to spoof an image of a person’s face to trick the facial-recognition system and take control of a device.


Windows Hello is [a feature](https://threatpost.com/microsoft-reveals-which-bugs-it-wont-patch/132817/) in Windows 10 that allows users to authenticate themselves without a password, using a PIN code or biometric identity—either a fingerprint or facial recognition—to access a device or machine. According to Microsoft, about 85 percent of Windows 10 users [use the system.](https://www.microsoft.com/security/blog/2020/12/17/a-breakthrough-year-for-passwordless-technology/)


The Windows Hello bypass vulnerability, tracked as [CVE-2021-34466](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-34466), requires an attacker to have physical access to a device to exploit it, according to researchers at CyberArk Labs who discovered the flaw in March.



From there, they can go on “to manipulate the authentication process by capturing or recreating a photo of the target’s face and subsequently plugging in a custom-made USB device to inject the spoofed images to the authenticating host,” Omer Tsarfati, cybersecurity researcher at CyberArk Labs, wrote [in a report](https://www.cyberark.com/resources/threat-research-blog/bypassing-windows-hello-without-masks-or-plastic-surgery) about the vulnerability published Tuesday.


Further, exploitation of the bypass can extend beyond Windows Hello systems to “any authentication system that allows a pluggable third-party USB camera to act as biometric sensor,” Tsarfati noted.


Researchers have no evidence that anyone has tried or used the attack in the wild, but someone with motive could potentially use it on a targeted victim, such as  “a researcher, scientist, journalist, activist or privileged user with sensitive IP on their device, for example,” according to the analysis.


Microsoft addressed the vulnerability — which affects both consumer and business versions of the feature — in its [July Patch Tuesday update](https://threatpost.com/microsoft-crushes-116-bugs/167764/), so users should apply the update to avoid being affected.


**Biometric Weakest Link**
--------------------------


CyberArk researchers posted a video of a proof-of-concept (PoC) for how to exploit the vulnerability, which can be used on both the consumer version, Windows Hello, and an enterprise version of the feature called Windows Hello for Business (WHfB) that businesses use with ActiveDirectory.


The bypass itself exploits a weakness in the biometric sensor of Windows Hello, which “transmits information on which the OS … makes its authentication decision,” he wrote. “Therefore, manipulating this information can lead to a potential bypass to the whole authentication system,” Tsarfati said.


For facial recognition, the biometric sensor is either a camera embedded in a device, such as a laptop, or connected to a computer via USB. Therefore, the entire process depends on this camera for proof of identity–which is where the vulnerability lies, particularly when a USB camera is used for authentication, he wrote.


“The answer lies in the input itself,” Tsarfati wrote. “Keyboard input is known only to the person who is typing before the information is entered into the system, while camera input isn’t.”


Therefore, using a camera to access “public” information—i.e., a person’s face—for authentication can easily be hijacked, he explained.


“It is similar to stealing a password, but much more accessible since the data (face) is out there,” Tsarfati wrote. “At the heart of this vulnerability lies the fact that Windows Hello allows external data sources, which can be manipulated, as a root of trust.”


**Attack Vector**
-----------------


Researchers detailed a somewhat complex way for an attacker to capture someone’s image, save the captured frames, impersonate a USB camera device, and eventually send those frames to the Windows hello system for verification.


To prove the concept, they created a custom USB device that acts as a USB camera with both infrared (IR) and Red Green Blue (RGB) sensors, using an evaluation board manufactured by NXP. They used this custom camera to transmit valid IR frames of the person they were targeting, while sending the RGB frames image of the cartoon character SpongeBob SquarePants.


“To our surprise, it worked!” Tsarfati wrote.


Based on this understanding, an attacker would only need to  implement a USB camera that supports RGB and IR cameras and then send only one genuine IR frame of a victim to bypass the login phase of the device, while the RGB frames can contain any random image, he explained.


The entire process depends on an attacker having an IR frame of a potential victim to use in an attack, which can be done either by capturing one or converting one of the person’s regular RBG frames to an IR one, Tsarfati explained.


“Our findings show that any USB device can be cloned, and any USB device can impersonate any other USB device,” he said.  “We used the IR frames of a person to ‘bypass’ the face recognition mechanism. We believe that those IR frames can be created out of regular color images.”


One spot of good news for Windows Hello users is that people who use Windows Hello Enhanced Sign-in Security—a new security feature in Windows that requires specialized and pre-installed hardware, drivers and firmware — are protected against the any attacks “which tamper with the biometrics pipeline,” Tsarfati added.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


 




#### Tags:
[[Windows]] [[USB]] [[Tsarfati]] [[RGB]] [[Microsoft]] [[CyberArk]] [[ThreatPost]]
