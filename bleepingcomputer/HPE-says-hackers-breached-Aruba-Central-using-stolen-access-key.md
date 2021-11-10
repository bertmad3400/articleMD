# HPE says hackers breached Aruba Central using stolen access key
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/hpe-says-hackers-breached-aruba-central-using-stolen-access-key/)
+ Date: November 10, 2021
+ Author: Lawrence Abrams


## Article:
![Aruba Central](https://www.bleepstatic.com/content/hl-images/2021/11/10/aruba-central-header.jpg)


HPE has disclosed that data repositories for their Aruba Central network monitoring platform were compromised, allowing a threat actor to access collected data about monitored devices and their locations.


Aruba Central is a cloud networking solution that allows administrators to manage large networks and components from a single dashboard.


HPE disclosed today that a threat actor obtained an "access key" that allowed them to view customer data stored in the Aruba Central environment. The threat actor had access for 18 days between October 9th, 2021, and October 27th, when HPE revoked the key.


The exposed repositories contained two datasets, one for network analytics and the other for Aruba Central's '[Contract Tracing](https://www.arubanetworks.com/solutions/contact-tracing/)' feature.


"One dataset ("network analytics") contained network telemetry data for most Aruba Central customers about Wi-Fi client devices connected to customer Wi-Fi networks. A second dataset ("contact tracing") contained location-oriented data about Wi-Fi client devices including which devices were in proximity to other Wi-Fi client devices," explains an [Aruba Central FAQ](https://www.arubanetworks.com/support-services/security-bulletins/central-incident-faq/) about the security incident.


The network analytics dataset exposed in these repositories included MAC addresses, IP addresses, operating systems, hostname, and for authenticated Wi-Fi networks, a person's username.


The contract tracing dataset also included the date, time, and Wi-Fi access points users were connected to, potentially allowing the threat actor to track the general vicinity of users' location.


"The data repositories also contained records of date, time, and the physical Wi-Fi access point where a device was connected, which could allow the general vicinity of a user's location to be determined. The environment did not include any sensitive or special categories of personal data (as defined by GDPR)," reads the FAQ.


As HPE's FAQ mentioned the word 'buckets' multiple times, a threat actor likely obtained the access key for a storage bucket used by the platform.


After performing an investigation into the breach, HPE concluded that:


* No more than 30 days of data was stored within the environment at any time, as data in the network analytics and contact tracing features of the Aruba Central environment is automatically deleted every 30 days.
* The environment included personal data, but no sensitive personal data.  The personal data includes MAC addresses, IP addresses, device operating system type and hostname, and some usernames. The contact tracing data also included users’ Access Point (AP) name, proximity, and duration of time connected to that AP.
* The likelihood that your personal data was accessed is extremely low, based on extensive analysis of access and traffic patterns.
* Security-sensitive information was not compromised, and so we do not believe there is any need to change passwords, change keys, or alter your network configuration.


HPE states that they are changing how they protect and store access keys to prevent future incidents.


BleepingComputer has reached out to HPE for more information on the breach and will update the article if we receive a response.


*Thx to John for the tip!*




#### Tags:
[[HPE]] [[Aruba]] [[Wi-Fi]] [[addresses,]] [[time,]] [[Bleeping Computer]]
