# Misconfigured, old Airflow instances leak Slack, AWS credentials
### Unprotected instances are exposing secrets across industries including IT, health, and cybersecurity.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/misconfigured-airflow-instances-leak-slack-aws-credentials/)
+ Date: October 5, 2021
+ Author: Charlie Osborne


## Article:
Unknown

Apache Airflow instances that have not been properly secured are exposing everything from Slack to AWS credentials online. 


On Monday, Intezer malware analyst Nicole Fishbein and cybersecurity researcher Ryan Robinson [said the instances](https://www.intezer.com/blog/cloud-security/misconfigured-airflows-leak-credentials/), vulnerable to data theft, belong to industries including IT, cybersecurity, health, energy, finance, and manufacturing, among other sectors.   

Apache Airflow, available [on GitHub](https://github.com/apache/airflow/), is an open source platform designed for scheduling, managing, and monitoring workflows. The modular software is also used to process data in real-time, with work pipelines configured as code.  

Apache Airflow version 2.0.0 was released in [December 2020](https://airflow.apache.org/blog/airflow-two-point-oh-is-here/) and implemented a number of security enhancements including a new REST API that enforced operational authentication, as well as a shift to explicit value settings, rather than default options. 

While examining active, older versions of the workflow software, the cybersecurity firm found a number of unprotected instances that exposed credentials for business and financial services including Slack, PayPal, AWS, Stripe, Binance, MySQL, Facebook, and Klarna.  

"They [instances] are typically hosted on the cloud to provide increased accessibility and scalability," Intezer noted. "On the flip side, misconfigured instances that allow internet-wide access make these platforms ideal candidates for exploitation by attackers." 

The most common security issue causing these leaks was the use of hardcoded passwords within instances that were embedded in Python DAG code. 

![screenshot-2021-10-05-at-10-04-05.png]()![screenshot-2021-10-05-at-10-04-05.png](https://www.zdnet.com/a/img/resize/253222ce356dc9a7244979b8689db1f7804946f6/2021/10/05/4d1774ff-87bc-4580-b146-9aa9fa07e821/screenshot-2021-10-05-at-10-04-05.png?width=1200&fit=bounds&auto=webp)
 Intezer
 




In addition, the researchers discovered that the Airflow "variables" feature was a credential leak source. Variable values can be set across all DAG scripts within an instance, but if it is not configured properly, this can lead to exposed passwords. 

The team also found misconfigurations in the "[Connections](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html)" feature of Airflow which provides the link between the software and a user's environment. However, not all credentials may be input properly and they could end up in the "extra" field, the team says, rather than the secure and encrypted portion of Connections. As a result, credentials can be exposed in plaintext.  

"Many Airflow instances contain sensitive information," the researchers explained. "When these instances are exposed to the internet the information becomes accessible to everyone since the authentication is disabled. In versions prior to v1.10 of Airflow, there is a feature that lets users run Ad Hoc database queries and get results from the database. While this feature can be handy, it is also very dangerous because on top of there being no authentication, anyone with access to the server can get information from the database." 

Intezer has notified the owners of the vulnerable instances through responsible disclosure.  

It is recommended that Apache Airflow users upgrade their builds to the latest version and check user privilege settings to make sure no unauthorized users can obtain access to their instances.  

###  Previous and related coverage

* [This is how fast a password leaked on the web will be tested out by hackers](https://www.zdnet.com/article/this-is-how-fast-a-password-leaked-on-the-web-will-be-tested-out-by-hackers/)  

* [Attacker releases credentials for 87,000 FortiGate SSL VPN devices](https://www.zdnet.com/article/attacker-releases-credentials-for-87000-fortigate-ssl-vpn-devices/)  

* [Microsoft Autodiscover abused to collect web requests, credentials](https://www.zdnet.com/article/design-flaw-in-microsoft-autodiscover-abused-to-leak-windows-domain-credentials/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Intezer]] [[ZDNet]]
