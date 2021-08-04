# Hacker target Kubernetes to steal data and processing power. Now the NSA has tips to protect yourself
### Top causes of compromises include supply chain risks, malicious attacks, and insider threats.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/hacker-target-kubernetes-to-steal-data-and-processing-power-now-the-nsa-has-tips-to-protect-yourself/)
+ Date: August 4, 2021 -- 10:36 GMT (11:36 BST)
+ Author: Liam Tung


## Article:
Unknown

The National Security Agency (NSA) has released its first Kubernetes hardening guidance to help organizations deploy the open-source platform for managing containerized applications.

The guidance was also authored by the DHS's Cybersecurity and Infrastructure Security Agency (CISA) to make users aware of key threats and configurations to minimize risk. 


"Kubernetes is commonly targeted for three reasons: data theft, computational power theft, or denial of service," [the agencies note in a joint announcement](https://www.nsa.gov/News-Features/Feature-Stories/Article-View/Article/2716980/nsa-cisa-release-kubernetes-hardening-guidance/). 

**SEE:**[**One third of cybersecurity workers have faced harassment at work or online - this initiative aims to stamp it out**](https://www.zdnet.com/article/one-third-of-cybersecurity-workers-have-faced-harassment-at-work-or-online-this-initiative-aims-to-stamp-it-out/)

"Data theft is traditionally the primary motivation; however, cyber actors may attempt to use Kubernetes to harness a network's underlying infrastructure for computational power for purposes such as cryptocurrency mining."

Researchers recently [warned that attackers were using misconfigured Kubernetes](https://www.zdnet.com/article/researchers-find-new-attack-vector-against-kubernetes-clusters-via-misconfigured-argo-workflows-instances/) deployments to drop crypto-miners on enterprise hardware.     

The key hardening guidance isn't unusual, but the report also offers an in-depth look at applying standard security mitigations in the context of complex environments that are often deployed in the cloud. At a high-level the guidance includes: scanning containers and pods for vulnerabilities or misconfigurations, running containers and pods with the least privileges possible, and using network separation, firewalls, strong authentication, and log auditing.






Of course, standard cyber hygiene is key too, including applying patches, updates, and upgrades to minimize risk. They also recommend vulnerability scans to check patches are applied. 

The advice covers Kubernetes clusters, the control plane, worker nodes (for running containerized apps for the cluster), and pods for containers that are hosted upon these nodes.  

The NSA and CISA make a special point about supply chain risks, including software and hardware dependencies that could be compromised at any point in the supply chain before deployment.

"The security of applications running in Kubernetes and their third-party dependencies relies on the trustworthiness of the developers and the defense of the development infrastructure. A malicious container or application from a third party could provide cyber actors with a foothold in the cluster," the agencies note. 

**SEE:**[**Ransomware: Only half of organisations can effectively defend against attacks, warns report**](https://www.zdnet.com/article/ransomware-only-half-of-organisations-can-effectively-defend-against-attacks-warns-report/)

The report also warns that remote attackers do target control plane components lacking appropriate access controls, as well as worker nodes that live outside of the locked down control plane. 

Insider threats include admins with high privileges and physical access to systems or hypervisors. 

Pods in particular need to be hardened against exploitation because they're often an attacker's initial execution environment after exploiting a container. 

It also recommends running non-root containers and rootless container engines to prevent root execution as many container services, by default, run as the privileged root user. 





#### Tags:
[[Kubernetes]] [[ZDNet]]
