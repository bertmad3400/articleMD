# NSA and CISA share Kubernetes security recommendations 
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/nsa-and-cisa-share-kubernetes-security-recommendations/)
+ Date: August 4, 2021
+ Author: Ionut Ilascu


## Article:
![NSA and CISA share Kubernetes security recommendations ](https://www.bleepstatic.com/content/hl-images/2020/12/08/1_0_Kubernetes.jpg)


The National Security Agency (NSA) and the Cybersecurity and Infrastructure Security Agency (CISA) have published comprehensive recommendations for strengthening the security of an organization’s Kubernetes system.


Kubernetes is a popular open-source solution for deploying, scaling, and managing containerized apps in the cloud, making it an attractive target for cyber attacks.


![Kubernetes architecture](https://www.bleepstatic.com/images/news/u/1100723/2021/Kub_Arch.jpg)


Hackers are constantly hitting Kubernetes environments, their motivation varying from stealing data, to cryptocurrency mining, to denial-of-service (DoS) that could act as a diversion for other operations.


To help companies make their Kubernetes environment more difficult to compromise, the NSA and CISA released a 52-page cybersecurity technical report that offers guidance for admins to manage Kubernetes securely.


The NSA says that the main three causes for a compromised Kubernetes environment are supply-chain attacks, malicious actors, and insider threats.


While administrators can’t prevent all three risks, they can harden the security of a Kubernetes cluster by avoiding common misconfigurations and applying mitigations to minimize security risks.


The agency notes that supply-chain attacks “are often challenging to mitigate,” adding that a malicious threat actor’s way in is typically exploiting a vulnerability or leveraging misconfigurations.



“Insider threats can be administrators, users, or cloud service providers. Insiders with special access to an organization’s Kubernetes infrastructure may be able to abuse these privileges” - the [National Security Agency](https://www.nsa.gov/News-Features/Feature-Stories/Article-View/Article/2716980/nsa-cisa-release-kubernetes-hardening-guidance/)



In broad strokes, the defensive actions against this these threats is to scan containers and Pods for bugs and misconfigurations; use the least privileges to run run Pods and containers (unless higher permissions are needed), and use network separation, strong authentication, properly configured firewalls, and audit logs.


![Kubernetes cluster components](https://www.bleepstatic.com/images/news/u/1100723/2021/Kub_Cluster.jpg)


Admins should also review all Kubernetes settings regularly and ensure that the system benefits from the latest updates, patches, and available upgrades.


Titled “Kubernetes Hardening Guidance,” the document goes through each of the following security recommendations, with examples:


**Kubernetes Pod security:**


Use containers built to run applications as non-root users 


* Where possible, run containers with immutable file systems
* Scan container images for possible vulnerabilities or misconfigurations
* Use a Pod Security Policy to enforce a minimum level of security including:


- Preventing privileged containers  

- Denying container features frequently exploited to breakout, such as hostPID, hostIPC, hostNetwork, allowedHostPath   

- Rejecting containers that execute as the root user or allow elevation to root   

- Hardening applications against exploitation using security services such as SELinux, AppArmor, and seccomp


**Network separation and hardening:**


* Lock down access to control plane nodes using a firewall and role-based access control (RBAC)
* Further limit access to the Kubernetes etcd server
* Configure control plane components to use authenticated, encrypted communications using Transport Layer Security (TLS) certificates
* Set up network policies to isolate resources. Pods and services in different namespaces can still communicate with each other unless additional separation is enforced, such as network policies
* Place all credentials and sensitive information in Kubernetes Secrets rather than in configuration files. Encrypt Secrets using a strong encryption method


**Authentication and authorization:**


* Disable anonymous login (enabled by default)
* Use strong user authentication
* Create RBAC policies to limit administrator, user, and service account activity


**Log auditing:**


* Enable audit logging (disabled by default)
* Persist logs to ensure availability in the case of node, Pod, or container level failure
* Configure a metrics logger


**Upgrading and application security practices:**


* Immediately apply security patches and updates
* Perform periodic vulnerability scans and penetration tests
* Remove components from the environment when they are no longer needed


Read the full [Kubernetes Hardening Guidance](https://media.defense.gov/2021/Aug/03/2002820425/-1/-1/1/CTR_KUBERNETES%20HARDENING%20GUIDANCE.PDF) document [PDF] from the NSA and CISA.




#### Tags:
[[Kubernetes]] [[NSA]] [[Bleeping Computer]]
