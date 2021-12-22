# Honeypot experiment reveals what hackers want from IoT devices
### ​A three-year-long honeypot experiment featuring simulated low-interaction IoT devices of various types and locations gives a clear idea of why actors target specific devices.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/honeypot-experiment-reveals-what-hackers-want-from-iot-devices/
+ Date: 2021-12-22T16:46:05-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/22/bees.jpg)

![bees](https://www.bleepstatic.com/content/hl-images/2021/12/22/bees.jpg?rand=1902165521)


​A three-year-long honeypot experiment featuring simulated low-interaction IoT devices of various types and locations gives a clear idea of why actors target specific devices.


More specifically, the honeypot was meant to create a sufficiently diverse ecosystem and cluster the generated data in a way that determines the goals of adversaries.


IoT (Internet of Things) devices are a booming market that includes small internet-connected devices such as cameras, lights, doorbells, smart TVs, motion sensors, speakers, thermostats, and many more.


It is estimated that by 2025, over 40 billion of these devices will be connected to the Internet, providing network entry points or computational resources that can be used in unauthorized crypto mining or as part of DDoS swarms.


Setting the stage
-----------------


The three components of the honeypot ecosystem set up by researchers at the NIST and the University of Florida included server farms, a vetting system, and the data capturing and analysis infrastructure.


To create a diverse ecosystem, the researchers installed Cowrie, Dionaea, KFSensor, and HoneyCamera, which are off-the-shelf IoT honeypot emulators.


The researchers configured their instances to appear as real devices on Censys and Shodan, two specialized search engines that find internet-connected services.


The three main types of honeypots were the following:


* **HoneyShell** – Emulating Busybox
* **HoneyWindowsBox** – Emulating IoT devices running Windows
* **HoneyCamera** – Emulating various IP cameras from Hikvision, D-Link, and other devices.


![Experiment layout](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/honeypot_setting.jpg)**Experiment layout**  
*Source: Arxiv.org*
A novel element in this experiment is that the honeypots were adjusted to respond to attacker traffic and attack methods. 


The researchers used the collected data to change the IoT configuration and defenses and then gather new data that reflected the actor's response to these changes.


The findings
------------


The experiment produced data from massive 22.6 million hits, with the vast majority targeting the HoneyShell honeypot.



![Number of hits for each honeypot type](https://www.bleepstatic.com/images/news/u/1220909/Tables/hits.jpg)**Number of hits for each honeypot type**  
*Source: Arxiv.org*
The various actors exhibited similar attack patterns, likely because their objectives and the means to achieve them were common.


For example, most actors run commands such as "masscan" to scan for open ports and "/etc/init.d/iptables stop" to disable firewalls.


Additionally, many actors run "free -m", "lspci grep VGA", and "cat /proc/cpuinfo", all three aiming to collect hardware information about the target device.


Interestingly, almost a million hits tested "admin / 1234" username-password combination, reflecting an overuse of the credentials in IoT devices.


As for end goals, the researchers found that the HoneyShell and the HoneyCamera honeypots were targeted mainly for DDoS recruitment and were often also infected with a Mirai variant or a coin miner.


Coin miner infections were the most common observation on the Windows honeypot, followed by viruses, droppers, and trojans.



![Attack types targeting HoneyShell](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Attack types targeting HoneyWindowsBox**  
*Source: Arxiv.org*
In the case of the HoneyCamera, the researchers intentionally crafted a vulnerability to reveal credentials and noticed that 29 actors engaged in exploiting the flaw manually.



![HoneyCamera layout](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**HoneyCamera layout**  
*Source: Arxiv.org*
"Only 314 112 (13 %) unique sessions were detected with at least one successful command execution inside the honeypots," explains the [research paper](https://arxiv.org/pdf/2112.10974.pdf).


"This result indicates that only a small portion of the attacks executed their next step, and the rest (87 %) solely tried to find the correct username/password combination."


How to secure your devices
--------------------------


To prevent hackers from taking over your IoT devices, follow these basic measures:


* Change the default account to something unique and strong (long).
* Set up a separate network for IoT devices and keep it isolated from critical assets.
* Make sure to apply any available firmware or other security updates as soon as possible.
* Actively monitor your IoT devices and look for signs of exploitation.

Most importantly, if a device does not need to be exposed to the Internet, ensure it is located behind a firewalls or VPN to prevent unauthorized remote access.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Agriculture]] [[victim.industry.name=Education]] [[victim.industry.name=Mining]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Iot]] [[Honeycamera]] [[Honeypots]] [[Arxiv.org]] [[Honeyshell]] [[Bleeping Computer]]

