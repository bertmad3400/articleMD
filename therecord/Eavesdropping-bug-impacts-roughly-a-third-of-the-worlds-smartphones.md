# Eavesdropping bug impacts roughly a third of the world’s smartphones
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/eavesdropping-bug-impacts-roughly-a-third-of-the-worlds-smartphones/)
+ Date: November 24, 2021
+ Author: Catalin Cimpanu


## Article:
![Eavesdropping bug impacts roughly a third of the world’s smartphones](https://therecord.media/wp-content/uploads/2021/11/smartphone-mobile.png)

MediaTek, a Taiwanese company that manufactures a wide array of chips for smartphones and other smart devices, has released security updates last month to address severe vulnerabilities that could allow malicious Android apps to record audio and spy on phone owners.


Three issues were patched in October (CVE-2021-0661, CVE-2021-0662, CVE-2021-0663), and a fourth (CVE-2021-0673) will be fixed next month, in December, according to security firm Check Point, whose researchers found the issues earlier this year.


“MediaTek chips contain a special AI processing unit (APU) and audio Digital signal processor (DSP) to improve media performance and reduce CPU usage,” a Check Point spokesperson said in an email this week.


“Both the APU and the audio DSP have custom microprocessor architectures, making MediaTek DSP a unique and challenging target for security research. Check Point grew curious around the degree to which MediaTek DSP could be used as an attack vector for threat actors,” the company added.


“For the first time, CPR was able to reverse engineer the MediaTek audio processor, revealing several security flaws,” it added.


### Malicious apps can abuse MediaTek bugs to spy on users


According to a [technical report](https://research.checkpoint.com/2021/looking-for-vulnerabilities-in-mediatek-audio-dsp/) published earlier today, malicious apps installed on a device can interact with the MediaTek audio driver. These apps could send maliciously-crafted messages to the MediaTek firmware to gain control over this driver and then abuse it to steal any audio flow going through the device.


The vulnerability can’t allow attackers to tap into microphones, but once audio data passes through the MediaTek driver, it can be recorded, such as audio from phone calls, WhatsApp calls, browser videos, and video players.


Currently, MediaTek chips are installed on roughly 37% of all the world’s smartphones, meaning the vulnerability presents a huge attack surface for any malicious app and malware creator.


Devices from Xiaomi, Oppo, Realme, and Vivo are known to use MediaTek chipsets.


The MediaTek firmware updates are normally delivered to smartphone vendors, who then deploy them to users as Android OS security updates in monthly cycles.


To protect their devices against these four MediaTek vulnerabilities, users are advised to apply the October and the upcoming December 2021 Android security bulletins.


“We have no evidence it is currently being exploited,” said Tiger Hsu, Product Security Officer at MediaTek. The MediaTek exec also thanked Check Point for their research into this novel area of their chip and their bug reports.





#### Tags:
[[MediaTek]] [[apps]] [[Android]] [[The Record]]
