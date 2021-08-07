# Apple fixed AWDL bug that could be used to escape air-gapped networks
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/apple-fixed-awdl-bug-that-could-be-used-to-escape-air-gapped-networks/)
+ Date: August 7, 2021
+ Author: Catalin Cimpanu


## Article:
![Apple fixed AWDL bug that could be used to escape air-gapped networks](https://therecord.media/wp-content/uploads/2021/08/AWDL-bug.png)

Apple has fixed a vulnerability in its Apple Wireless Direct Link (AWDL) technology that could have been abused by threat actors to escape and steal data from air-gapped networks.


Silently patched earlier this spring, in April — *with the release of iOS 14.5, iPadOS 14.5, watchOS 7.4, and Big Sur 11.3* — the vulnerability was publicly disclosed for the first time earlier this week in a [blog post](https://medium.com/sensorfu/escaping-from-a-truly-air-gapped-network-via-apple-awdl-6cf6f9ea3499) by Mikko Kenttälä, a Finish security researcher and the founder and CEO of SensorFu.


### Bug lets attackers bounce connections on Apple devices


Kenttälä discovered the issue in [AWDL](https://owlink.org/wiki/), a protocol that Apple rolled out in 2014 that allows Apple devices to talk to each other via a Bluetooth or WiFi connection.


While most Apple users might not be aware of the protocol’s existence, AWDL is the base of Apple services like AirPlay and AirDrop, and Apple has included AWDL by default on all devices the company has sold in recent years, such as Macs, iPhones, iPads, Apple watches, Apple TVs, and HomePods.


As part of its default functionality, the AWDL protocol automatically scans for other nearby Apple devices that come into its range, and it might need to connect in the future. This behavior takes place silently, in the phone’s background, and at any time as long as an Apple device’s WiFi or Bluetooth connection is enabled.


The technical background of this bug is a bit complicated and explained much better in Kenttälä’s blog post, but to summarize, the researcher effectively found a method to use ICMPv6 and IPv6 packets to take data from an infected system, bounce the packets on a nearby AWDL-capable Apple device, and send the stolen files to another device with an IPv6 address.


### The threat to air-gapped networks


While there are better ways to steal data from a device, Kenttälä said that this particular bug was an issue for the operators of air-gapped networks.


Designed to operate without an internet connection and physically separate from an organization’s main office network, air-gapped networks are typically used by government, military, or corporate entities to store sensitive data, such as classified files or intellectual property.


Kenttälä says that if a threat actor manages to infect a device in any of these super-secure networks, the bug he discovered could have been abused to steal data any time an employee with an iPhone or other Apple device passed through the vicinity of the air-gapped network.


If the passer-by’s device had a mobile data connection enabled, the attacker would bounce small amounts of data to a remote system, as can be seen in a proof-of-concept video Kenttälä published on YouTube, embedded below:





These types of attacks are often derided by the cybersecurity community due to the amount of if and buts required to be successful.


However, those who operate these types of networks always take them very seriously, as they know that the threat actors they’re protecting against would go to extreme lengths to compromise such systems and have the ability to infect these systems with malware if they’d wished to.





#### Tags:
[[air-gapped]] [[Kenttälä]] [[AWDL]] [[The Record]]
