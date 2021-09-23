# 100M IoT Devices Exposed By Zero-Day Bug
### A high-severity vulnerability could cause system crashes, knocking out sensors, medical equipment and more. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=174963)
+ Date: September 23, 2021  2:35 pm
+ Author: Becky Bracken


## Article:
A flaw in a widely used internet-of-things (IoT) infrastructure code left more than 100 million devices across 10,000 enterprises vulnerable to attacks.


Researchers at Guardara used their technology to find a zero-day vulnerability in [NanoMQ](https://www.emqx.com/en/products/nanomq), an open-source platform from EMQ that monitors IoT devices in real time, then acts as a “message broker” to deliver alerts that atypical activity has been detected. EMQ’s products are used to monitor the health of patients leaving a hospital, to detect fires, monitor car systems, in smartwatches, in smart-city applications and more.


“Guardara used its technology to detect multiple issues…that caused EMQ’s NanoMQ product to crash during testing,” the company said in a press statement. “The existence of these vulnerabilities means that any NanoMQ reliant system could be brought down completely.”


Guardara CEO Mitali Rakhit told Threatpost that the vulnerability (no CVE) was assigned a CVSS score of 7.1, making it high-severity.


“How dangerous it is depends on what setting NanoMQ is used in,” Rakhit added.


Zsolt Imre from Guardara explained on [GitHub](https://github.com/nanomq/nanomq/issues/203?fbclid=IwAR0dfQrgHknG6ZsEv5WDJnpzaxyjUdQ-BtLC0ON4RkJHQm6dnB1HA4Bu1w8) that the issue was with the MQTT packet length. MQTT is a messaging protocol standard for IoT, [designed as](https://mqtt.org/) an extremely lightweight publish/subscribe messaging transport for connecting remote devices with a small code footprint, requiring minimal network bandwidth. Thus, MQTT is used in a wide variety of industries that use low-bandwidth smart sensors, such as automotive, manufacturing, telecommunications, oil and gas, and so on.


In NanoMQ’s implementation, “when the MQTT packet length is tampered with and is lower than expected, a ‘memcpy’ operation receives a size value that makes the source buffer location point to or into an unallocated memory area,” Imre wrote. “As a result, NanoMQ crashes.”


A crash


‘The problem seems to be with how the payload length is calculated,” Imre continued. “Suspected that the unusual packet length ‘msg\_len’ is a smaller value than ‘used\_pos,’ therefore the subtraction results in a negative number. However, ‘memcpy’ expects the size as ‘size\_t,’ which is unsigned. Therefore, due to the casting of a negative number to ‘size\_t’, the length becomes a very large positive number (0xfffffffc in case of this proof of concept).”


All an attacker would need to exploit the vulnerability and crash the system are basic networking and scripting skills, Rakhit added.


These kinds of denial-of-service attacks can be extremely dangerous as they affect the availability of  mission-critical equipment.


“This could potentially put millions of lives and significant property at risk,” according to the firm. “The technology within NanoMQ is used for collecting real-time data from common devices including smartwatches, car sensors and fire-detection sensors. Message brokers are used to monitor health parameters via sensors for patients leaving hospital, or motion detection sensors to prevent theft.”


The software developer has issued fixes; users of devices that incorporate NanoMQ should check with their vendors for an update to device firmware.


**Attacks on IoT Devices Spike**
--------------------------------


This disclosure comes amid a spike in the number of attacks on IoT devices, including [remote controls](https://threatpost.com/comcast-rf-attack-remotes-surveillance/169133/), [Bluetooth devices](https://threatpost.com/bluetooth-bugs-dos-code-execution/169159/), [home security systems](https://threatpost.com/fortress-home-security-remote-disarmament/169069/) and more.


Kaspersky released a report earlier this month that showed a more than 100 percent jump in [cyberattacks on IoT devices](https://threatpost.com/iot-attacks-doubling/169224/) during the first half of 2021, with a staggering 1.5 billion attacks launched so far this year.


“Since IoT devices, from smartwatches to smart-home accessories, have become an essential part of our everyday lives, cybercriminals have skillfully switched their attention to this area,” Dan Demeter, security expert at Kaspersky said. “We see that once users’ interest in smart devices rose, attacks also intensified.”


***Rule #1 of Linux Security:****No cybersecurity solution is viable if you don’t have the basics down.*[*JOIN*](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)*Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the*[*4 Golden Rules of Linux Security*](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)*. Your top takeaway will be a Linux roadmap to getting the basics right!*[*REGISTER NOW*](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)*and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.*




#### Tags:
[[NanoMQ]] [[IoT]] [[Linux]] [[MQTT]] [[Guardara]] [[Rakhit]] [[Threatpost]] [[Imre]] [[devices,]] [[ThreatPost]]
