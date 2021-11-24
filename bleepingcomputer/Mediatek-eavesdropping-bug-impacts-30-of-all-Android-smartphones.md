# Mediatek eavesdropping bug impacts 30% of all Android smartphones
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/mediatek-eavesdropping-bug-impacts-30-percent-of-all-android-smartphones/)
+ Date: November 24, 2021
+ Author: Bill Toulas


## Article:
![MediaTek](https://www.bleepstatic.com/content/hl-images/2021/11/24/Mediatek_logo.jpg)


MediaTek fixed security vulnerabilities that could have allowed attackers to eavesdrop on Android phone calls, execute commands, or elevate their privileges to a higher level.


MediaTek is one of the largest semiconductor companies in the world, with their chips present in [43% of all smartphones](https://www.counterpointresearch.com/global-smartphone-ap-market-share/) as of the second quarter of 2021


These vulnerabilities were discovered by Check Point, with three of them (CVE-2021-0661, CVE-2021-0662, CVE-2021-0663) fixed in the October 2021 MediaTek Security Bulletin, and the fourth (CVE-2021-0673) fixed by a security update coming next month.


These flaws mean that all smartphones using MediaTek chips are vulnerable to eavesdropping attacks or malware infections that require no user interaction if the security updates are not installed.


There will likely never receive a security update for a notable number of older devices that vendors no longer support.


Android API and DSP trouble
---------------------------


Modern MediaTek processors use a dedicated audio processing unit called Digital Signal Processor (DSP) to reduce CPU loads and improve audio playback quality and performance.


This unit receives audio processing requests from apps in Android user space via a driver and an IPC system. Theoretically, an unprivileged app can exploit flaws to manipulate request handlers and run code on the audio chip.


The audio driver doesn't communicate with the DSP directly but with IPI messages forwarded to the System control processor (SCP).



![Sending an IPI message with data transfer over the DMA](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/IPI%20message.jpg)**Sending an IPI message with data transfer over the DMA**  
*Source: Check Point*
By reverse-engineering the Android API responsible for audio communication, Check Point learned more about how the system works, leading to the discovery of the following vulnerabilities:


* [CVE-2021-0673](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-0673) – Details to be disclosed next month
* [CVE-2021-0661](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-0661) – Incorrect bounds check leading to out of bounds write and local privilege escalation
* [CVE-2021-0662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-0662) – Incorrect bounds check leading to out of bounds write and local privilege escalation
* [CVE-2021-0663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-0663) – Incorrect bounds check leading to out of bounds write and local privilege escalation


By chaining these flaws, an attacker could potentially perform local privilege escalation attacks, send messages to the DSP firmware, and then hide or run code on the DSP chip itself.



![Payload example causing a crash](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/crash.jpg)**Payload example causing a crash**  
*Source: Check Point*

> 
> "Since the DSP firmware has access to the audio data flow, a malformed IPI message could potentially be used by a local attacker to do privilege escalation, and theoretically eavesdrop on the mobile phone’s user." - [Check Point](https://research.checkpoint.com/2021/looking-for-vulnerabilities-in-mediatek-audio-dsp/).
> 
> 
> 


MediaTek has removed the ability to use the parameter string command via the AudioManager that’s used for exploiting CVE-2021-0673, essentially mitigating the issue.


MediaTek will release more details about the CVE-2021-0673 vulnerability in an upcoming security bulletin to be released in December 2021.


The other three flaws (CVE-2021-0661, CVE-2021-0662, CVE-2021-0663) have been addressed with Android security updates released in the [October 2021 patch level](https://www.bleepingcomputer.com/news/security/android-october-patch-fixes-three-critical-bugs-41-flaws-in-total/) or later.


We have reached out to MediaTek to ask if there are any possible mitigations for unsupported devices, and we will update this piece as soon as we have a response.


In the meantime, if you are using a MediaTek device that runs on an older patch level, make sure to install a mobile protection suite from a reputable vendor and avoid risky practices such as installing APKs from outside the Play Store.




#### Tags:
[[MediaTek]] [[Android]] [[IPI]] [[Bleeping Computer]]
