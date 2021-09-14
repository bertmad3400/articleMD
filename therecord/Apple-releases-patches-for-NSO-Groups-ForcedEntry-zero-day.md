# Apple releases patches for NSO Group’s ForcedEntry zero-day
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/apple-releases-patches-for-nso-groups-forcedentry-zero-day/)
+ Date: September 13, 2021
+ Author: Catalin Cimpanu


## Article:
![Apple releases patches for NSO Group’s ForcedEntry zero-day](https://therecord.media/wp-content/uploads/2021/05/iphone-ios-e1626716322336.jpg)

Apple has released security updates today to patch ForcedEntry, a professional exploit developed by Israeli spyware maker NSO Group, and which has been abused to hack into the phones of multiple activists since February this year.


Patches are available today for [macOS](https://support.apple.com/kb/HT212805), [iOS, iPadOS](https://support.apple.com/en-us/HT212807), and [watchOS](https://support.apple.com/kb/HT212806).


Tracked as **CVE-2021-30860**, the ForcedEntry zero-day exploits a bug in [CoreGraphics](https://developer.apple.com/documentation/coregraphics), an Apple component for drawing 2D graphics.


When weaponized, ForcedEntry allows NSO customers to send maliciously crafted PDF files to a victim’s Apple device and run malicious code that takes over their systems.


Citizen Lab, a political, human rights, and cybersecurity research center at the University of Toronto, was credited with discovering this zero-day.


In reports published in [August](https://citizenlab.ca/2021/08/bahrain-hacks-activists-with-nso-group-zero-click-iphone-exploits/) and earlier [today](https://citizenlab.ca/2021/09/forcedentry-nso-group-imessage-zero-click-exploit-captured-in-the-wild/), Citizen Lab researchers said they found ForcedEntry deployed on the iPhones of activists in [Bahrain](https://therecord.media/bahraini-activists-targeted-with-new-ios-zero-click-exploit/) and Saudi Arabia.




| **Target** | **Description** | **Date(s) of Hacking** |
| --- | --- | --- |
| Moosa Abd-Ali * | Activist | (Sometime before September 2020) |
| --- | --- | --- |
| Yusuf Al-Jamri | Blogger | (Sometime before September 2019) |
| **Activist A** | Member of Waad | September 16, 2020 |
| **Activist B *** | Member of Waad, Labor Law Researcher | June 3, 2020 July 12, 2020 July 19, 2020 July 24, 2020 August 6, 2020 September 15, 2020 |
| **Activist C** | Member of Waad | September 14, 2020 |
| **Activist D *** | Member of BCHR | September 14, 2020 |
| **Activist E** | Member of BCHR | February 10, 2021 |
| **Activist F** * | Member of BCHR | July 11, 2020 July 15, 2020 July 22, 2020 October 13, 2020 |
| **Activist G** * | Member of Al Wefaq | (Sometime before October 2019) |
| **Activist H** | **Based in Saudi Arabia** | **March 2021** |


The researchers said they believe the exploit has been used in attacks since at least February this year.


In its August report, Citizen Lab said that NSO Group appears to have specifically developed ForcedEntry as a way to bypass a new security feature called [BlastDoor](https://googleprojectzero.blogspot.com/2021/01/a-look-at-imessage-in-ios-14.html) that Apple added in iOS 14 in the fall of 2020.


### Safari zero-day also patched


In addition, Apple’s security updates today also include a patch for a second zero-day, tracked as CVE-2021-30858.


Reported by an anonymous researcher, this bug impacts Safari’s WebKit browser engine and was also abused in the wild, but details about its exploitation have not been revealed.


Patches for this zero-day were released for [macOS](https://support.apple.com/en-us/HT212804), [iOS, and iPadOS](https://support.apple.com/en-us/HT212807).


These two zero-days represent the 14th and 15th zero-days Apple has patched this year.


Reached out for comment, Apple provided the following statement after several news publications blew the zero-day’s severity out of proportion.



> After identifying the vulnerability used by this exploit for iMessage, Apple rapidly developed and deployed a fix in iOS 14.8 to protect our users. We’d like to commend Citizen Lab for successfully completing the very difficult work of obtaining a sample of this exploit so we could develop this fix quickly. Attacks like the ones described are highly sophisticated, cost millions of dollars to develop, often have a short shelf life, and are used to target specific individuals. While that means they are not a threat to the overwhelming majority of our users, we continue to work tirelessly to defend all our customers, and we are constantly adding new protections for their devices and data.
> 
> Ivan Krstić, head of Apple Security Engineering and Architecture





#### Tags:
[[2020Activist]] [[ForcedEntry]] [[*Member]] [[NSO]] [[year.]] [[zero-day]] [[The Record]]
