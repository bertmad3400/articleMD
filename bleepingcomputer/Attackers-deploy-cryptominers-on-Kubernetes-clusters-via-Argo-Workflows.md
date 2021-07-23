# Attackers deploy cryptominers on Kubernetes clusters via Argo Workflows
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/attackers-deploy-cryptominers-on-kubernetes-clusters-via-argo-workflows/)
+ Date: July 23, 2021
+ Author: Sergiu Gatlan


## Article:
![Attackers deploy cryptominers on Kubernetes clusters via Argo Workflows](https://www.bleepstatic.com/content/hl-images/2020/12/08/1_0_Kubernetes.jpg)


Threat actors are abusing misconfigured Argo Workflows instances to deploy cryptocurrency miners on Kubernetes (K8s) clusters.


[Kubernetes](https://kubernetes.io/) is an open-source system that helps to automate the deployment, scaling, and management of containerized workloads, services, and apps over clusters of hosts.


[Argo Workflows](https://github.com/argoproj/argo-workflows) is the most popular workflow execution engine for Kubernetes, designed to orchestrate parallel jobs for speeding up machine learning or data processing computing-intensive jobs on Kubernetes clusters.


New attack vector already used in the wild
------------------------------------------


"Attackers are already taking advantage of this vector as we detected operators dropping cryptominers using this method in the wild," Intezer security researchers Ryan Robinson and Nicole Fishbein [revealed in a report](https://www.intezer.com/blog/container-security/new-attacks-on-kubernetes-via-misconfigured-argo-workflows/) published earlier this week.


Threat actors gain access to such clusters via Internet-exposed Argo dashboards and deploy their own malicious workflows using various Monero miner containers, including kannix/monero-miner, a defunct container that mines for Monero using the XMRig CPU/GPU miner.


While kannix/monero-miner is no longer available on Docker Hub, attackers can pick from a few dozens of other containers that do the same job: mining Monero cryptocurrency using the CPU or the GPU.


The researchers added that broader-scale attacks should be expected, given that hundreds of Argo Workflows deployments with the wrong permissions are exposed to Internet access.


The two security researchers were able to find exposed Argo Workflows instances belonging to organizations from multiple industry sectors, including technology, finance, and logistics.


Admins are advised to always enable authentication on Argo Workflows dashboards if they can't avoid exposing on the Internet, and to monitor their environments (containers, images, and the processes they run) for malicious activity.



![Cryptominer running on Argo instancer](https://www.bleepstatic.com/images/news/u/1109292/2021/Cryptominer%20running%20on%20Argo%20instancer.png)*Cryptominer running on Argo instance for 9 months (Intezer)*
More Kubernetes attack vectors
------------------------------


Misconfigured Argo Workflows instances are the latest observed attack vector, with threat actors previously scanning for and abusing other security holes to breach Kubernetes clusters.


For instance, last month, Microsoft warned that [cryptomining gangs were targeting machine learning (ML) infrastructure](https://www.bleepingcomputer.com/news/security/microsoft-warns-of-cryptomining-attacks-on-kubernetes-clusters/) running on Kubernetes clusters via Internet-exposed Kubeflow dashboards.


The attackers used Kubeflow Pipelines to deploy ML pipelines running XMRig and Ethminer cryptocurrency miners for CPU and GPU cryptomining.


One year before, in April 2020, Microsoft discovered another large-scale cryptomining campaign attempting to breach [Kubernetes clusters used for resource-hungry machine learning computing tasks](https://azure.microsoft.com/en-us/blog/detect-largescale-cryptocurrency-mining-attack-against-kubernetes-clusters/) by abusing Jupyter notebooks.


In June, Unit 42 researchers also discovered Siloscape, the [first malware to target Windows containers](https://www.bleepingcomputer.com/news/security/new-kubernetes-malware-backdoors-clusters-via-windows-containers/) with the end goal of backdooring Kubernetes clusters.


Unlike other malware that targets cloud environments and mainly focuses on cryptojacking, Siloscape exposes the compromised servers to a broader range of malicious pursuits, including ransomware attacks, credential theft, data exfil, and even supply chain attacks.




#### Tags:
[[Kubernetes]] [[Workflows]] [[Monero]] [[GPU]] [[cryptomining]] [[Bleeping Computer]]
