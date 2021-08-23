# Botnet targets hundreds of thousands of devices using Realtek SDK
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/botnet-targets-hundreds-of-thousands-of-devices-using-realtek-sdk/)
+ Date: August 23, 2021
+ Author: Sergiu Gatlan


## Article:
![Botnet targets hundreds of thousands of devices using Realtek SDK](https://www.bleepstatic.com/content/hl-images/2021/08/23/Router.jpg)


A Mirai-based botnet now targets a critical vulnerability in the software SDK used by hundreds of thousands of Realtek-based devices, encompassing 200 models from at least 65 vendors, including Asus, Belkin, D-Link, Netgear, Tenda, ZTE, and Zyxel.


The security flaw that IoT Inspector security researchers found is now tracked as CVE-2021-35395 and was assigned a 9.8/10 severity rating.


It [impacts many Internet-exposed wireless devices](https://www.iot-inspector.com/blog/advisory-multiple-issues-realtek-sdk-iot-supply-chain/) ranging from residential gateways and travel routers to Wi-Fi repeaters, IP cameras, and smart lightning gateways or connected toys.


Attacks began only two days after public disclosure
---------------------------------------------------


Since the bug affects the management web interface, remote attackers can scan for and attempt to hack them to execute arbitrary code remotely on unpatched devices, allowing them to take over the impacted devices.


While Realtek shipped a [patched version](https://www.realtek.com/images/safe-report/Realtek_APRouter_SDK_Advisory-CVE-2021-35392_35395.pdf) of the vulnerable SDK on August 13, three days before IoT Inspector security researchers published [their advisory](https://www.iot-inspector.com/blog/advisory-multiple-issues-realtek-sdk-iot-supply-chain/), this gave very little time to vulnerable device owners to apply the patch.


As network security firm SAM Seamless Network discovered, a Mirai botnet began searching for devices unpatched against CVE-2021-35395 on August 18, only two days after IoT Inspector shared details of the bug.


"As of August 18th, we have identified attempts to exploit CVE-2021-35395 in the wild," [SAM said in a report](https://securingsam.com/realtek-vulnerabilities-weaponized/) published last week.


SAM says that the most common devices using buggy Realtek SDK targeted by this botnet are Netis E1+ extender, Edimax N150 and N300 Wi-Fi routers, and Repotec RP-WR5444 router, mainly used to enhance Wi-Fi reception.


Botnet updated to target new devices
------------------------------------


The threat actor behind this Mirai-based botnet also updated their scanners more than two weeks ago [to exploit a critical authentication bypass vulnerability](https://www.bleepingcomputer.com/news/security/actively-exploited-bug-bypasses-authentication-on-millions-of-routers/) (CVE-2021-20090) impacting millions of home routers using Arcadyan firmware.


As Juniper Threat Labs researchers revealed at the time, this threat actor has been targeting network and IoT devices since at least February.


"This chain of events shows that hackers are actively looking for command injection vulnerabilities and use them to propagate widely used malware quickly," said Omri Mallis, chief product architect at SAM Seamless Network.


"These kinds of vulnerabilities are easy to exploit and can be integrated quickly into existing hacking frameworks that attackers employ, well before devices are patched and security vendors can react."


The complete list of affected devices is too long to embed here, but it can be found [at the end of the IoT Inspector report](https://www.iot-inspector.com/blog/advisory-multiple-issues-realtek-sdk-iot-supply-chain/#:~:text=List%20of%20(known)%20affected%20manufacturers).




#### Tags:
[[IoT]] [[botnet]] [[SDK]] [[CVE-2021-35395]] [[Wi-Fi]] [[Bleeping Computer]]
