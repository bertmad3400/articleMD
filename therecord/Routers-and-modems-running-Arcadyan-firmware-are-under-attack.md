# Routers and modems running Arcadyan firmware are under attack
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/routers-and-modems-running-arcadyan-firmware-are-under-attack/)
+ Date: August 8, 2021
+ Author: Catalin Cimpanu


## Article:
![Routers and modems running Arcadyan firmware are under attack](https://therecord.media/wp-content/uploads/2021/08/router.png)

Routers and modems running a version of the Arcadyan firmware, including devices from ASUS, Orange, Vodafone, and Verizon, are currently under attack from a threat actor attempting to ensnare the devices into their DDoS botnet.


[First spotted](https://twitter.com/bad_packets/status/1423206304168898561) by security firm *Bad Packets* earlier this week and [confirmed](https://blogs.juniper.net/en-us/security/freshly-disclosed-vulnerability-cve-2021-20090-exploited-in-the-wild) by *Juniper Labs* on Friday, the attacks are exploiting a vulnerability tracked as [CVE-2021-20090](https://kb.cert.org/vuls/id/914124).


Discovered by Tenable security researcher Evan Grant [earlier this year](https://www.tenable.com/security/research/tra-2021-13), the vulnerability resides in the firmware code produced by Taiwanese tech firm Arcadyan.


Grant says the vulnerability has existed in the code for at least ten years and has made its way into the firmware of at least 20 router and modem models sold by 17 different vendors, which based their products on a white-label version of old Arcadyan devices.


The list of affected devices includes some of today’s biggest router vendors and internet service providers, such as ASUS, Orange, Vodafone, Telstra, Verizon, Deutsche Telekom, British Telecom, and many others.




| **`Vendor`** | **`Device`** | **`Found on version`** |
| `ADB` | `ADSL wireless IAD router` | `1.26S-R-3P` |
| `Arcadyan` | `ARV7519` | `00.96.00.96.617ES` |
| `Arcadyan` | `VRV9517` | `6.00.17 build04` |
| `Arcadyan` | `VGV7519` | `3.01.116` |
| `Arcadyan` | `VRV9518` | `1.01.00 build44` |
| `ASMAX` | `BBR-4MG / SMC7908 ADSL` | `0.08` |
| `ASUS` | `DSL-AC88U (Arc VRV9517)` | `1.10.05 build502` |
| `ASUS` | `DSL-AC87VG (Arc VRV9510)` | `1.05.18 build305` |
| `ASUS` | `DSL-AC3100` | `1.10.05 build503` |
| `ASUS` | `DSL-AC68VG` | `5.00.08 build272` |
| `Beeline` | `Smart Box Flash` | `1.00.13\_beta4` |
| `British Telecom` | `WE410443-SA` | `1.02.12 build02` |
| `Buffalo` | `WSR-2533DHPL2` | `1.02` |
| `Buffalo` | `WSR-2533DHP3` | `1.24` |
| `Buffalo` | `BBR-4HG` |  |
| `Buffalo` | `BBR-4MG` | `2.08 Release 0002` |
| `Buffalo` | `WSR-3200AX4S` | `1.1` |
| `Buffalo` | `WSR-1166DHP2` | `1.15` |
| `Buffalo` | `WXR-5700AX7S` | `1.11` |
| `Deutsche Telekom` | `Speedport Smart 3` | `010137.4.8.001.0` |
| `HughesNet` | `HT2000W` | `0.10.10` |
| `KPN` | `ExperiaBox V10A (Arcadyan VRV9517)` | `5.00.48 build453` |
| `KPN` | `VGV7519` | `3.01.116` |
| `O2` | `HomeBox 6441` | `1.01.36` |
| `Orange` | `LiveBox Fibra (PRV3399)` | `00.96.00.96.617ES` |
| `Skinny` | `Smart Modem (Arcadyan VRV9517)` | `6.00.16 build01` |
| `SparkNZ` | `Smart Modem (Arcadyan VRV9517)` | `6.00.17 build04` |
| `Telecom (Argentina)` | `Arcadyan VRV9518VAC23-A-OS-AM` | `1.01.00 build44` |
| `TelMex` | `PRV33AC` | `1.31.005.0012` |
| `TelMex` | `VRV7006` |  |
| `Telstra` | `Smart Modem Gen 2 (LH1000)` | `0.13.01r` |
| `Telus` | `WiFi Hub (PRV65B444A-S-TS)` | `v3.00.20` |
| `Telus` | `NH20A` | `1.00.10debug build06` |
| `Verizon` | `Fios G3100` | `1.5.0.10` |
| `Vodafone` | `EasyBox 904` | `4.16` |
| `Vodafone` | `EasyBox 903` | `30.05.714` |
| `Vodafone` | `EasyBox 802` | `20.02.226` |


Besides the wide impact, the bug wasn’t initially a big deal. Found earlier this year and [patched in April](https://www.buffalo.jp/news/detail/20210727-01.html), the vulnerability never came under attack until this week.


Exploitation only started Thursday this week, two days after Grant published an [in-depth technical write-up](https://medium.com/tenable-techblog/bypassing-authentication-on-arcadyan-routers-with-cve-2021-20090-and-rooting-some-buffalo-ea1dd30980c2), which also included proof-of-concept code.


Bad Packets co-founder and CTO Troy Mursch told *The Record* the attacks are leveraging the proof-of-concept code shared in Grant’s blog post, which is tailored to attack Buffalo routers.





Per Grant, once exploited, the vulnerability can be used to bypass authentication procedures on affected routers and modems to enable the Telnet service and allow threat actors to connect to devices remotely.


While Grant has not tested his proof-of-concept exploit for other devices, and the exploit might not work out of the box for all, the chances are that it does.


While still unconfirmed, owners of any of the affected devices listed in the table above are advised to inquire their router vendor for security patches.


Juniper said it identified the threat actor behind these attacks as a [notorious botnet herder](https://unit42.paloaltonetworks.com/mirai-variant-iot-vulnerabilities/) operating a version of the Mirai malware.





#### Tags:
[[(Arcadyan]] [[proof-of-concept]] [[The Record]]
