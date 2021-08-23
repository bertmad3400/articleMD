# Hundreds of thousands of Realtek-based devices under attack from IoT botnet
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/hundreds-of-thousands-of-realtek-based-devices-under-attack-from-iot-botnet/)
+ Date: August 23, 2021
+ Author: Catalin Cimpanu


## Article:
![Hundreds of thousands of Realtek-based devices under attack from IoT botnet](https://therecord.media/wp-content/uploads/2021/08/router-1.png)

A dangerous vulnerability in Realtek chipsets used in **hundreds of thousands of smart devices from at least 65 vendors** is currently under attack from a notorious DDoS botnet gang.


The attacks started last week, according to a [report](https://securingsam.com/realtek-vulnerabilities-weaponized/) from IoT security firm SAM, and began just three days after fellow security firm IoT Inspector published [details](https://www.iot-inspector.com/blog/advisory-multiple-issues-realtek-sdk-iot-supply-chain/) about the vulnerability on its blog.


#### Vulnerability impacts little know but very popular Realtek SoC


Tracked as [CVE-2021-35395](https://nvd.nist.gov/vuln/detail/CVE-2021-35395), the vulnerability is part of four issues IoT Inspector researchers found in the software development kit (SDK) that ships with multiple Realtek chipsets (SoCs).


These chips are manufactured by Realtek but are shipped to other companies, which then use them as the basic System-on-Chip (SoC) board for their own devices, with the Realtek SDK serving as a configurator and starting point for their own firmware.


IoT Inspector said they found more than 200 different device models from at least 65 different vendors that had been built around these chips and were using the vulnerable SDK.


Estimated in the realm of hundreds of thousands of internet-connected devices, the list of vulnerable items includes routers, network gateways, Wi-Fi repeaters, IP cameras, smart lighting, and even internet-connected toys.


Of the four issues discovered by the IoT Inspector research team, the CVE-2021-35395 vulnerability received the highest severity rating, of 9.8 out of 10 on the CVSSv3 severity scale.


According to the research team, the vulnerability, which resided in a web panel used to configure the SDK/device, allowed a remote attacker to connect to these devices via malformed URL web panel parameters, bypass authentication, and run malicious code with the highest privileges, effectively taking over the device.


While Realtek released patches [[PDF](https://www.realtek.com/images/safe-report/Realtek_APRouter_SDK_Advisory-CVE-2021-35392_35395.pdf)] a day before IoT Inspector published its findings last week, this was far too small of a time window for device vendors to deploy the security updates down the line to their own set of customers.


This means that today, the vast majority of these devices are still running outdated firmware (and an outdated Realtek SDK), being exposed to attacks.


#### A very busy botnet


Per SAM, exploitation started shortly after and came from [the same Mirai-based botnet](https://unit42.paloaltonetworks.com/mirai-variant-iot-vulnerabilities/) that a week before [rushed to exploit a similar mega-bug](https://therecord.media/routers-and-modems-running-arcadyan-firmware-are-under-attack/) in millions of routers running Arcadyan-based firmware.


The SAM research team said that based on their own scans, the most common device models currently running the vulnerable Realtek SDK include the likes of:


* Netis E1+ extender
* Edimax N150 and N300 Wi-Fi router
* Repotec RP-WR5444 router


Owners of such devices should look or inquire their sellers for new firmware patches.





#### Tags:
[[Realtek]] [[IoT]] [[botnet]] [[The Record]]
