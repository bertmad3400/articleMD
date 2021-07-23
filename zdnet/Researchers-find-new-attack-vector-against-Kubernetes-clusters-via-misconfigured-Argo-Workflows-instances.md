# Researchers find new attack vector against Kubernetes clusters via misconfigured Argo Workflows instances
### The report notes that other security teams have discovered large-scale cryptocurrency mining attack against Kubernetes clusters.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/researchers-find-new-attack-vector-against-kubernetes-clusters-via-misconfigured-argo-workflows-instances/)
+ Date: July 23, 2021 -- 14:00 GMT (15:00 BST)
+ Author: Jonathan Greig


## Article:
Unknown

Analysts with cybersecurity company Intezer have found that cybercriminals are now going after a new attack vector against Kubernetes clusters via misconfigured Argo Workflows instances.

Intezer security researchers Ryan Robinson and Nicole Fishbein [wrote a report](https://www.intezer.com/blog/container-security/new-attacks-on-kubernetes-via-misconfigured-argo-workflows/) detailing the attack, noting that they have already found infected nodes. The two said the attacks were concerning because there are hundreds of misconfigured deployments and attackers have been detected dropping cryptominers like the kannix/monero-miner through this attack vector.

"We have detected exposed instances of Argo Workflows that belong to companies from different sectors including technology, finance and logistics. Argo Workflows is an open-source, container-native workflow engine designed to run on K8s clusters. Argo Workflows instances with misconfigured permissions allow threat actors to run unauthorized code on the victim's environment," Robinson and Fishbein said. 

"Exposed instances can contain sensitive information such as code, credentials and private container image names. We also discovered that in many instances, permissions are configured which allow any visiting user to deploy workflows. We also detected that some misconfigured nodes are being targeted by threat actors."

Some cyberattackers have been able to take advantage of misconfigured permissions that give them access to an open Argo dashboard where they can submit their own workflow.

The "kannix/monero-miner," according to the researchers, requires little skill to use and the report notes that other security teams have discovered large-scale cryptocurrency mining attack against Kubernetes clusters.

"In Docker Hub there are still a number of options for Monero mining that attackers can use. With a simple search it shows that there are at least 45 other containers with millions of downloads," the study said. 






Fishbein and Robinson urge users to access the Argo Workflows dashboard from an unauthenticated incognito browser outside of corporate environments as a way to check if instances are misconfigured. 

Administrators can also query the API of an instance and check the status code. 


Yaniv Bar-Dayan, CEO of Vulcan Cyber, explained that the complexity and scale inherent to enterprise cloud deployments means that there will be breaches due to human error. 

"Misconfiguration is just one type of risk-inducing vulnerability, and cloud is just one attack vector that needs to be tracked and mitigated. If security teams can understand and prioritize risk created by cloud misconfigurations alongside IT infrastructure and application vulnerabilities they have a shot at reducing risk and improving the security posture of business," Bar-Dayan added. 

"Cloud security can no longer be someone else's problem, and it is not enough to ask if cloud infrastructure by itself is secure. We must ask the same about our applications, traditional infrastructure and networks."

Coalfire managing principal Andrew Barratt noted that orchestration platforms are an interesting attack surface due to what they can be leveraged to perform. 

Barratt said they could allow an adversary to perform very sophisticated lateral attacks entirely leveraging the scale of native cloud services. While he is not against using them, he said it is now important for them to be seen as a sophisticated attack platform with many capabilities and typically elevated privileges as well as the ability to build and deploy resources with an immediate cost associated. 

"These vulnerabilities have been around for a long time and security teams are already aware of them to some degree, regardless of platform -- be it virtualization, physical data centers or the public cloud and the many different service offerings," said Michael Cade, senior global technologist with Kasten.

"This is not going to be the only vulnerability that is found within Kubernetes environments or wider operating systems."





#### Tags:
[[misconfigured]] [[cloud]] [[Workflows]] [[Kubernetes]] [[Fishbein]] [[teams]] [[ZDNet]]
