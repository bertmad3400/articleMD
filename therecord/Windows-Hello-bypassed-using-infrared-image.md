# Windows Hello bypassed using infrared image
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/windows-hello-bypassed-using-infrared-image/)
+ Date: July 18, 2021
+ Author: Catalin Cimpanu


## Article:
![Windows Hello bypassed using infrared image](https://therecord.media/wp-content/uploads/2021/07/Infrared.jpg)

Researchers from security firm CyberArk bypassed [Windows Hello](https://support.microsoft.com/en-us/windows/learn-about-windows-hello-and-set-it-up-dae28983-8242-bb2a-d3d1-87c9d265a5f0), the biometrics authentication system included with all Windows 10 versions, using just an infrared image of the device’s owner.


Discovered by CyberArk security researcher [Omer Tsarfati](https://twitter.com/OmerTsarfati), the vulnerability resided in Windows Hello’s facial recognition feature, and more specifically, in how Windows Hello processed data from USB-connected webcams.


While most users are aware that they could use a webcam to authenticate on a Windows 10 computer using their face, Tsarfati discovered that Windows Hello also supported infrared-capable webcam input.


The CybarArk researcher discovered that the video input verification process for infrared input was not sufficient or on par with the one for normal (RGB) cameras.


In tests performed earlier this year, Tsarfati found that an attacker could connect a malicious USB device designed to mimic a USB webcam to a Windows 10 computer and then use it to feed an infrared image of the device owner’s face.


While under normal circumstances, an attacker would not be able to feed a static image to Windows Hello, these same rules did not apply to the infrared input, with the CyberArk researcher successfully bypassing the authentication process and gaining access to a locked Windows 10 device.


Physical access would be required to abuse this attack vector, but Tsarfati said that Microsoft has fixed this vulnerability, tracked as [CVE-2021-34466](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-34466), earlier this week, as part of the July 2021 Patch Tuesday security updates.


Windows 10 users, especially those in enterprise devices where passwordless authentication is often enabled, are encouraged to apply the latest security updates.


A video of Tsarfati’s Windows Hello bypass is available [here](https://fast.wistia.net/embed/iframe/dfzonzhind), while a [technical write-up](https://www.cyberark.com/resources/threat-research-blog/bypassing-windows-hello-without-masks-or-plastic-surgery) is available on the CyberArk blog.





Tsarfati is also scheduled to present his findings at the [Black Hat USA 2021 security conference](https://www.blackhat.com/us-21/briefings/schedule/#bypassing-windows-hello-for-business-and-pleasure-22868) at the start of August.





#### Tags:
[[Windows]] [[Tsarfati]] [[CyberArk]] [[webcam]] [[The Record]]
