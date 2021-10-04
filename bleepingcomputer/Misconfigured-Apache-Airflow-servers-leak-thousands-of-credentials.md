# Misconfigured Apache Airflow servers leak thousands of credentials
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/misconfigured-apache-airflow-servers-leak-thousands-of-credentials/)
+ Date: October 4, 2021
+ Author: Ax Sharma


## Article:
![apache airflow](https://www.bleepstatic.com/content/hl-images/2021/10/04/header.png)


While investigating a misconfiguration flaw in Apache Airflow, researchers discovered many exposed instances over the web leaking sensitive information, including credentials, from well-known tech companies.


Apache Airflow is a popular open-source workflow management platform for organizing and managing tasks.


Cloud hosting providers, payment processors leaked credentials
--------------------------------------------------------------


This week, researchers Nicole Fishbein and Ryan Robinson from security firm Intezer have disclosed details on how they identified misconfiguration errors across Apache Airflow servers run by major tech companies.


The misconfiguration flaws resulted in sensitive data leakage including thousands of credentials from popular platforms and services such as Slack, PayPal, and Amazon Web Services (AWS), among others, claim the researchers:



![services and platforms leaking creds](https://www.bleepstatic.com/images/news/u/1164866/2021/Oct-2021/apache-airflow-misconfig/image1.jpg)**Researchers saw commonly used services and platforms leaking credentials**(Intezer)
"These unsecured instances expose sensitive information of companies across the media, finance, manufacturing, information technology (IT), biotech, e-commerce, health, energy, cybersecurity, and transportation industries," says Intezer's researchers.


In various scenarios that researchers have analyzed, the most common reason for credential leak seen on Airflow servers was insecure coding practices.


For example, Intezer's team discovered various production instances with hard-coded passwords inside the [Python DAG](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html) code:



![production environment credentials leak](https://www.bleepstatic.com/images/news/u/1164866/2021/Oct-2021/apache-airflow-misconfig/image2.jpg)**Examples of hardcoded password for a production PostgreSQL database** (Intezer)
"Passwords should not be hardcoded and the long names of images and dependencies should be utilized. You will not be protected when using poor coding practices even if you believe the application is firewalled off to the internet," warn Fishbein and Robinson. 


In another case of misconfiguration, researchers saw Airflow servers with a publicly accessible configuration file: 


"The configuration file (airflow.cfg) is created when Airflow is first started. It contains Airflow's configuration and it is able to be changed," state the researchers. The file contains secrets such as passwords and keys.


But, if the `expose\_config` option in the file is mistakenly set to 'True,' the configuration becomes accessible to anyone via the web server, who can now view these secrets.



![publicly visible Airflow config file](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Publicly visible Airflow config file 'airflow.cfg'**(Intezer)
Other examples caught in the wild included sensitive data stored in Airflow "Variables" that could be edited by an unauthorized user to inject malicious code, and the improper use of "Connections" feature—credentials stored in the unencrypted "Extra" field as JSON blobs visible to everyone.


Research demonstrates risks of delayed patching
-----------------------------------------------


In addition to identifying improperly configured Airflow assets, the focus of this research was to draw attention to risks that come from delaying software updates.


Intezer states the vast majority of these flaws were identified in servers running [Airflow v1.x](https://github.com/apache/airflow/releases/tag/1.0.0) from 2015, still in use by organizations from different sections.


In version 2 of Airflow, many new security features were introduced including a REST API that requires authentication for all operations. The newer version also doesn't store sensitive information in logs and forces the administrator to explicitly confirm configuration options, rather than go with default ones.


Exposing customer records and sensitive data due to security flaws resulting from procrastinated patching could be in violation of data protection laws like the [GDPR](https://www.bleepingcomputer.com/news/technology/amazon-gets-888-million-gdpr-fine-for-behavioral-advertising/).


"Disruption of clients' operations through poor cybersecurity practices can also result in legal action such as class action lawsuits," advises the security firm.


This discovery comes just months after a misconfiguration in Argo Workflows, also discovered by Intezer, was abused by attackers to [deploy cryptominers on Kubernetes clusters](https://www.bleepingcomputer.com/news/security/attackers-deploy-cryptominers-on-kubernetes-clusters-via-argo-workflows/).


In August this year, BleepingComputer reported on cases of misconfigured buckets exposing millions of sensitive records from a [secret terrorist watchlist](https://www.bleepingcomputer.com/news/security/secret-terrorist-watchlist-with-2-million-records-exposed-online/).


Intezer states that prior to making its findings public it has notified the identified organizations and entities leaking sensitive data via vulnerable Airflow instances.


"In light of the major changes made in version 2, it is strongly recommended to update the version of all Airflow instances to the latest version. Make sure that only authorized users can connect," advise Intezer's researchers in their [report](https://www.intezer.com/blog/cloud-security/misconfigured-airflows-leak-credentials).




#### Tags:
[[Intezer]] [[(Intezer)]] [[Bleeping Computer]]
