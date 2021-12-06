# Apache Kafka Cloud Clusters Expose Sensitive Data for Large Companies
### The culprit is misconfigured Kafdrop interfaces, used for centralized management of the open-source platform.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176778
+ Date: 2021-12-06T16:14:54+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2020/03/09191149/insecure-cloud.jpg)

Some of the world’s largest companies have exposed reams of sensitive information from the cloud, researchers said – thanks to misconfigured Kafdrop instances.


Kafdrop is a management interface for Apache Kafka, which is an open-source, cloud-native platform for collecting, analyzing, storing and managing data streams. Kafka has several common use cases; for instance, in the finance sector it’s often used for real-time data processing in order to catch and block fraudulent transactions as they occur. It the internet of things world, it can support “just-in-time” resource allocation for smart-grid applications and the like. Other uses include tracking application activity (user clicks, registrations, time spent on certain pages or features, orders, etc.); and event logging or real-time monitoring.



> **We want to know what your biggest cloud security concerns and challenges are, and how your company is dealing with them. Weigh in with our exclusive, anonymous [Threatpost Poll](https://threatpost.com/cloud-security-challenges-poll/176702/)!**
> 
> 


Kafka is tailored for large companies, and is in use by 60 percent of the Fortune 100, [it says](https://kafka.apache.org/powered-by), including Box, Cisco, Goldman Sachs, Intuit, Target and others, plus eight of 10 of the world’s largest banks, the 10 largest global insurance companies and eight of the 10 key world telecom providers, among thousands of others.


As such, a vulnerable or exposed management tool for the platform makes for “a perfect target for attackers who can infiltrate and exfiltrate data and take over cluster management,” according to researchers at Spectral.


**Kafdrop: A Central Hub and Target**
-------------------------------------


One such “perfect target” is Kafdrop, a popular open-source user interface that can be deployed as a Docker container.


It connects and maps existing Kafka clusters automatically, Spectral researchers explained, allowing users to manage topic creation and removal, as well as “understand the topology and layout of a cluster, drilling into hosts, topics, partitions, and consumers. It also allows you to sample and download live data from all topics and partitions, acting as a legitimate Kafka consumer.”


Unfortunately, Spectral researchers also discovered multiple instances of misconfigured Kafdrop interfaces exposing complete Kafka clusters to the public internet.


“These clusters expose customer data, transactions, medical records and internal system traffic: providing an inside look into the complete nervous system, all public,” according to the firm’s analysis, [released Monday](https://spectralops.io/blog/misconfigured-kafdrop-puts-companies-apache-kafka-completely-exposed/). “We found exposed clusters from companies across a multitude of industries, including insurance, healthcare, IoT, media and social networks.”


Researchers added, “Also exposed was real-time traffic revealing secrets, authentication tokens, and other access details that allow hackers to infiltrate the companies’ cloud activities on AWS, IBM, Oracle and others.”


They warned that the impact on affected companies could be significant, with several attack outcomes possible, including:


* Sensitive information compromise/data theft
* Deletion of Kafka topics and data sources, wreaking havoc in internal systems and leading to potential denial-of-service (DoS)
* Exposure of log and transactional data – everything from sensitive traffic records to financial transactions, and internal database records to sensitive app payloads
* Additional access to other parts of the corporate cloud/network by injecting specially crafted messages into Kafka; Kafka can connect to external systems for data import/export
* Regulatory non-compliance


“Since Kafka serves as a data hub and central processing system for mission-critical data, an exposed cluster risks every facet of the organization,” researcher noted. “By understanding the topology of a cluster, a hacker can efficiently connect and impersonate a legitimate consumer, injecting or pulling data at will.”


In one of the exposed clusters, Spectral observed live traffic at “one of the largest news outlets in the world,” containing service tokens, secrets, cookies and more. In another case, researchers were able to see email traffic, containing message content, tokens and private cookies carried as parameters within email URLs.


One of the large medical organizations had “complete topology for handling requests, processing, and inventory of medication as well as customer prescription transactions,” researchers added, while another exposed cluster held insurance claims, transactions and interactions between agents and customers.


Affected companies were notified, researchers said.


**Preventing Cloud Misconfigurations**
--------------------------------------


Cloud misconfigurations are increasingly common, with data leaks [nearly endemic](https://threatpost.com/hobby-lobby-customer-data-cloud-misconfiguration/164980/) among public cloud storage buckets. But Spectral’s research shows that there are other common cloud misconfigurations to worry about.


To avoid exposing the corporate crown jewels, Kafdrop should be redeployed behind an app server, with an active and configured authentication module, researchers noted.


“With only one connected access point, you can now add an authentication module to [something like] Nginx and use it as an authentication layer,” they explained.


Also, Spectral contributed authentication code into the open-source code base in the wake of its findings.


“Kafdrop is based on the Spring-Boot framework, which supports security as a first-class citizen and includes a wide range of built-in authentication mechanisms,” according to the writeup. “As such, we at Spectral have contributed an authentication code addition back into Kafdrop using a simple username-password authentication. Though this is pretty basic methodology, it is better than not having any authentication at all.”


Other remediation and mitigation strategies include encrypting data at rest in Kafka, and configuring applications to always encrypt when reading or writing data to and from Kafka; and, employing advanced misconfiguration scanners to help detect broken authentication, input sanitation problems and encryption errors.


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** ***[REGISTER TODAY](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)*** ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This [LIVE, interactive Threatpost Town Hall](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article), sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***for the LIVE event!***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Finance]] [[victim.industry.name=Healthcare]] [[victim.industry.name=Healthcare]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Kafdrop]] [[Cloud]] [[Open-source]] [[Real-time]] [[Threatpost]] [[ThreatPost]]

