# This chip flaw could have let malicious apps eavesdrop on Android phone users
### MediaTek fixes several flaws that attackers can exploit without user interaction.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/this-chip-flaw-could-have-let-malicious-apps-eavesdrop-on-android-phone-users/)
+ Date: November 25, 2021
+ Author: Liam Tung


## Article:
Unknown

Taiwanese chip maker MediaTek has addressed four vulnerabilities that could have allowed malicious apps to eavesdrop on Android phone users. 

Three the of vulnerabilities, tracked as CVE-2021-0661, CVE-2021-0662 and CVE-2021-0663, affected MediaTek's audio digital signal processor (DSP) firmware. It's a sensitive component that if compromised could allow attackers to spy on user conversations. 

Researchers at Check Point found and reported the flaws to MediaTek, which disclosed and fixed them in October. A fourth issue affects the MediaTek HAL (CVE-2021-0673). It was also fixed in October but will be disclosed in December. 


"A malformed inter-processor message could potentially be used by an attacker to execute and hide malicious code inside the DSP firmware. Since the DSP firmware has access to the audio data flow, an attack on the DSP could potentially be used to eavesdrop on the user," [explains Check Point researcher Slava Makkaveev](https://blog.checkpoint.com/2021/11/24/check-point-research-discover-vulnerabilities-in-smartphones-chips-embedded-in-37-of-smartphones-around-the-world/). 

**SEE:** [**Best phone 2021: The top 10 smartphones available**](https://www.zdnet.com/article/10-best-smartphones/#link=%7B%22linkText%22:%22Best%20phone%202021:%20The%20top%2010%20smartphones%20available%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/10-best-smartphones/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)

[According to market research firm Counterpoint](https://www.counterpointresearch.com/global-smartphone-ap-market-share/), MediaTek's system on chips (SoCs) accounted for 43% of the mobile SoCs shipped in Q2 2021. Its chips are found in high-end smartphones from Xiaomi, Oppo, Realme, Vivo and others. Check Point estimates MediaTek chips are present in about a third of all smartphones.

The vulnerabilities are accessible from the Android user space, meaning a malicious Android app installed on a device could be used for privilege escalation against the MediaTek DSP for eavesdropping.






MediaTek [rated](https://corp.mediatek.com/product-security-bulletin/October-2021) CVE-2021-0661, CVE-2021-0662 and CVE-2021-0663 as medium severity heap-based buffer over flaws in DSP. In all three cases, it notes that "user interaction is not needed for exploitation."

Check Point also discovered a way to use the [Android Hardware Abstraction Layer (HAL)](https://source.android.com/devices/architecture) as a way to attack MediaTek hardware. 

"While looking for a way to attack the Android HAL, we found several dangerous audio settings implemented by MediaTek for debugging purposes. A third-party Android application can abuse these settings to attack MediaTek Aurisys HAL libraries," explains Makkaveev.

**SEE:** [**Dark web crooks are now teaching courses on how to build botnets**](https://www.zdnet.com/article/college-for-cyber-criminals-dark-web-crooks-are-teaching-courses-on-how-to-build-botnets/#link=%7B%22role%22:%22standard%22,%22href%22:%22https://www.zdnet.com/article/college-for-cyber-criminals-dark-web-crooks-are-teaching-courses-on-how-to-build-botnets/%22,%22target%22:%22_blank%22,%22absolute%22:%22%22,%22linkText%22:%22Dark%20web%20crooks%20are%20now%20teaching%20courses%20on%20how%20to%20build%20botnets%22%7D)

He adds that device manufacturers don't bother validating HAL configuration files properly because they are not available to unprivileged users. 

"But in our case, we are in control of the configuration files. The HAL configuration becomes an attack vector. A malformed config file could be used to crash an Aurisys library which could lead to LPE," writes Makkaveev. 

"To mitigate the described audio configuration issues, MediaTek decided to remove the ability to use the PARAM\_FILE command via the AudioManager in the release build of Android," he adds.





#### Tags:
[[MediaTek]] [[Android]] [[ZDNet]]
