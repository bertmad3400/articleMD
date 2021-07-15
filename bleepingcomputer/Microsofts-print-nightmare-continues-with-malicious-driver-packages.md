# Microsoft's print nightmare continues with malicious driver packages
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsofts-print-nightmare-continues-with-malicious-driver-packages/)
+ Date: July 15, 2021
+ Author: Lawrence Abrams


## Article:
![Microsoft](https://www.bleepstatic.com/content/hl-images/2021/03/18/microsoft-fire.jpg)


Microsoft's print nightmare continues with another example of how a threat actor can achieve SYSTEM privileges by abusing malicious printer drivers.


Last month, security researchers accidentally disclosed a proof-of-concept exploit for the [Windows PrintNightmare zero-day](https://www.bleepingcomputer.com/news/security/public-windows-printnightmare-0-day-exploit-allows-domain-takeover/).


This vulnerability is tracked as CVE-2021-34527 and is a missing permission check in the Windows Print Spooler that allows for installing malicious print drivers to achieve remote code execution or local privilege escalation on vulnerable systems.



Microsoft [released an out-of-band KB5004945 security update](https://www.bleepingcomputer.com/news/security/microsoft-pushes-emergency-update-for-windows-printnightmare-zero-day/) that was supposed to fix the vulnerability, but security researchers quickly determined that the patch could be bypassed [under certain conditions](https://www.bleepingcomputer.com/news/microsoft/microsofts-incomplete-printnightmare-patch-fails-to-fix-vulnerability/).


However, Microsoft stated that their patches worked as intended, and as the vulnerability was being actively exploited, advised all Windows users to install the update.


The print nightmare continues
-----------------------------


Yesterday, security researcher and Mimikatz creator [Benjamin Delpy](https://twitter.com/gentilkiwi) said he found a way to abuse Windows' normal method of installing printer drivers to gain local SYSTEM privileges through malicious printer drivers.


This technique can be used even if admins applied [Microsoft's recommended mitigations](http://msrc-blog.microsoft.com/2021/07/08/clarified-guidance-for-cve-2021-34527-windows-print-spooler-vulnerability/) of restricting printer driver installation to admins and disabling Point and Print.




> 
> [#printnightmare](https://twitter.com/hashtag/printnightmare?src=hash&ref_src=twsrc%5Etfw) - Episode 3  
>   
> 
> You know that even patched, with default config (or security enforced with [#Microsoft](https://twitter.com/hashtag/Microsoft?src=hash&ref_src=twsrc%5Etfw) settings), a standard user can load drivers as SYSTEM?  
>   
> 
> - Local Privilege Escalation - [#feature](https://twitter.com/hashtag/feature?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/Zdge0okzKi](https://t.co/Zdge0okzKi)
> 
> 
> —  Benjamin Delpy (@gentilkiwi) [July 15, 2021](https://twitter.com/gentilkiwi/status/1415520478693888004?ref_src=twsrc%5Etfw)


While this new local privilege escalation method is not the same as the one commonly referred to PrintNightmare, Delpy told BleepingComputer that he considers similar printer driver installation bugs to be classified under the same name.


In a conversation with BleepingComputer, Delpy explained that even with mitigations applied, a threat actor could create a signed malicious print driver package and use it to achieve SYSTEM privileges on other systems.


To do this, the threat actor would create a malicious print driver and sign it using a trusted Authenticode certificate [using these steps](https://docs.microsoft.com/en-us/windows-hardware/drivers/develop/signing-a-driver-for-public-release)


However, some threat actors go for the "Rolls Royce" method of signing drivers, which is to buy or steal an EV certificate and then [submit it for Microsoft WHQL validation](https://docs.microsoft.com/en-us/windows-hardware/drivers/dashboard/get-a-code-signing-certificate) as a fake company.


Once they have a signed printer driver package, a threat actor can install the driver on any other networked device where they have administrative privileges.


Threat actors can then use this "pivot" device to gain SYSTEM privileges on other devices where they do not have elevated privileges simply by installing the malicious driver, as shown by the video below.



Delpy said that this technique could be used to help threat actors spread laterally in an already compromised network.


When asked how Microsoft could prevent this type of attack, Delpy stated that they attempted to prevent it in the past by deprecating version 3 printer drivers. Ultimately, this caused problems, and [Microsoft ended the v3 deprecation policy](https://docs.microsoft.com/en-us/previous-versions/windows/hardware/design/dn705223(v=vs.85)) in June 2017.


Unfortunately, this method will likely not be fixed as Windows is designed to allow an administrator to install a printer driver, even ones that may be unknowningly malicious. Furthermore, Windows is designed to allow non-admin users to install signed drivers on their devices for ease of use. 


Instead, security software will likely be the primary defense against attacks like this by detecting the malicious driver or behavior.


BleepingComputer has contacted Microsoft regarding the issue but has not heard back.




#### Tags:
[[Microsoft]] [[Windows]] [[Delpy]] [[-]] [[BleepingComputer]] [[Bleeping Computer]]
