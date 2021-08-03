# NSA, CISA publish Kubernetes hardening guide
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/nsa-cisa-publish-kubernetes-hardening-guide/)
+ Date: August 3, 2021
+ Author: Catalin Cimpanu


## Article:
![NSA, CISA publish Kubernetes hardening guide](https://therecord.media/wp-content/uploads/2021/08/kubernetes.png)

The National Security Agency (NSA) and the Cybersecurity and Infrastructure Security Agency (CISA) have published today a 59-page technical report containing guidance for hardening Kubernetes clusters.


Initially developed by Google engineers and later open-sourced under the Cloud Native Computing Foundation, [Kubernetes](https://kubernetes.io/) is one of today’s most popular container orchestration software.


Used primarily inside cloud-based infrastructure, Kubernetes allows system administrators to easily deploy new IT resources using software containers.


However, because the Kubernetes and Docker model is so different compared to traditional, monolithic software platforms, many system administrators have problems configuring Kubernetes to work in a secure way.


Over the past few years, several crypto-mining botnets have targeted these misconfigurations. Threat actors scanned the internet for [Kubernetes management features](https://azure.microsoft.com/en-us/blog/detect-largescale-cryptocurrency-mining-attack-against-kubernetes-clusters/) left exposed online without authentication or for applications running on large Kubernetes clusters (such as [Argo Workflow](https://www.intezer.com/blog/container-security/new-attacks-on-kubernetes-via-misconfigured-argo-workflows/) or [Kubeflow](https://www.microsoft.com/security/blog/2020/06/10/misconfigured-kubeflow-workloads-are-a-security-risk/)), gained access to a Kubernetes backend, and then used this access to deploy crypto-mining apps inside a victim’s cloud infrastructure.


These attacks started taking place at a timid pace in early 2017 but have now reached a state where multiple gangs are fighting each other on the same misconfigured cluster.


Through the guidance published today, CISA and NSA officials hope to provide system administrators with a secure baseline for future Kubernetes configurations that will avoid these types of intrusions.


Furthermore, besides a basic configuration guideline, the joint CISA & NSA report also details basic mitigations that companies and government agencies can implement to prevent or limit the severity of a Kubernetes breach. These include:


* Scan containers and Pods for vulnerabilities or misconfigurations.
* Run containers and Pods with the least privileges possible.
* Use network separation to control the amount of damage a compromise can cause.
* Use firewalls to limit unneeded network connectivity and encryption to protect confidentiality.
* Use strong authentication and authorization to limit user and administrator access as well as to limit the attack surface.
* Use log auditing so that administrators can monitor activity and be alerted to potential malicious activity.
* Periodically review all Kubernetes settings and use vulnerability scans to help ensure risks are appropriately accounted for and security patches are applied.


The full joint CISA & NSA advisory is available as a PDF download [**here**](https://media.defense.gov/2021/Aug/03/2002820425/-1/-1/1/CTR_KUBERNETES%20HARDENING%20GUIDANCE.PDF).





#### Tags:
[[Kubernetes]] [[CISA]] [[NSA]] [[The Record]]
