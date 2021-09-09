# ‘Azurescape’ Kubernetes Attack Allows Cross-Container Cloud Compromise
### A chain of exploits could allow a malicious Azure user to infiltrate other customers’ cloud instances within Microsoft’s container-as-a-service offering.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169319)
+ Date: September 9, 2021  12:39 pm
+ Author: Tara Seals


## Article:
A critical security vulnerability allowing attackers to perform cross-account container takeover in Microsoft’s public cloud, dubbed “Azurescape”, has been uncovered by researchers.


The issue exists in Azure Container Instances (ACI), which is Microsoft’s container-as-a-service (CaaS) offering (which enables users to run cloud containers without having to deal with managing the underlying infrastructure). Part of the infrastructure hosting ACI consists of multitenant Kubernetes clusters, which can be compromised to allow cyberattackers to gain full control over other users’ containers, researchers from Palo Alto Networks’ Unit 42 team explained.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“A malicious Azure user could have exploited these issues to execute code on other users’ containers, steal customer secrets and images deployed to the platform, and possibly abuse ACI’s infrastructure for cryptomining,” they said in a [Thursday posting](https://unit42.paloaltonetworks.com/azure-container-instances/).


Microsoft has rolled out a patch to ACI, but users should revoke any privileged credentials that were deployed to the platform before Aug. 31 to avoid compromise. They should also review access logs for any irregularities, Unit 42 recommended.


**ACI Multitenant Architecture – Good Fences, Good Neighbors**
--------------------------------------------------------------


In the multitenant architecture, each customer’s container is hosted in a Kubernetes pod on a dedicated, single-tenant node virtual machine (VM), according to the analysis, and the boundaries between customers are enforced by this node-per-tenant structure.


“Since practically anyone can deploy a container to the platform, ACI must ensure that malicious containers cannot disrupt, leak information, execute code or otherwise affect other customers’ containers,” explained researchers. “These are often called cross-account or cross-tenant attacks.”


The Azurescape version of such an attack has two prongs: First, malicious Azure customers/adversaries must escape their container; then, they must acquire a privileged Kubernetes service account token that can be used to take over the Kubernetes API server.


The API Server provides the frontend for a cluster’s shared state, through which all of the nodes interact, and it’s responsible for processing commands within each node by interacting with Kubelets. Each node has its own Kubelet, which is the primary “node agent” that handles all tasks for that specific node.


Thus, the end result of an API server compromise is “establishing complete control over the multitenant cluster and all customer containers running within it,” according to Unit 42.


**Kubernetes Container Escape**
-------------------------------


The first step in the attack proved easier than expected. Unit 42 researchers found that Azure uses RunC, the industry standard container runtime, to power ACI. Unfortunately, this happens to be an ancient version of the technology (RunC v1.0.0-rc2), which was released on Oct. 1, 2016.


True to legacy software form, it harbors at least two container-escape bugs. Unit 42 researchers went on to use one of these (CVE-2019-5736) to break out of a test ACI container, gaining a reverse shell running as root on the underlying Kubernetes node.


“While we escaped our container, we were still within the tenant boundary – the node VM,” researchers explained. “CaaS platforms are designed to withstand sophisticated attackers who possess kernel vulnerabilities enabling privilege escalation and container breakout. A malicious container breaking out is a somewhat expected threat, tolerated through node-level isolation.”


**Snagging a Privileged Kubernetes Account Token**
--------------------------------------------------


Escaping this underlying node VM – the boundary with other customers – means finding a way to access the API server and force it to execute commands on neighboring nodes. The best way to do this is by obtaining a privileged access token for the API server, the researchers soon discovered.


In hunting for a way to obtain such privileges, researchers observed that ACI supports executing node VM commands on uploaded containers via the “az container” exec command to a Kubelet, which is handled by a dedicated bridge pod rather than the API server itself (researchers said the implementation of the bridge pod is a fix for a previous vulnerability).


Curiously, researchers found that such exec requests arriving at the node included an authorization header carrying a Kubernetes service account token for this ‘bridge’ service account.


“Finding a token here was surprising,” according to the analysis. “Kubelets in the cluster were configured to allow anonymous access, so there was no need for requests to authenticate via a token. Perhaps this was a relic of an older implementation.”


Researchers then examined the token’s permissions, and found that it could be used to execute commands on any pod in the cluster – including the API server pod.


From there, exploitation was straightforward, they said – and they were quickly successful in using the token to open a shell on the API server container as a cluster administrator, with full control over the multitenant cluster and all customer containers within it.


“If you run Kubernetes, be careful to whom you send your service account tokens: Anyone who receives a token is free to use it and masquerade as its owner,” researchers noted. “Token thieves are likely to be very interested in the permissions of their stolen tokens.”


**Azurescape Exploit Steps**
----------------------------


In short, the Azurescape exploit worked like this, as demonstrated [in this video](https://youtu.be/YfZBwKP18CQ):


The fix was simple: Microsoft merely ensured that the bridge pod no longer sends its service account token to nodes when issuing exec requests.


**How to Prevent Cross-Container Attacks in the Cloud**
-------------------------------------------------------


Azurescape may be mitigated, but there are likely other avenues to achieving this kind of exploitation,  Unit 42 researchers warned.


“Cross-account vulnerabilities are often described as a ‘nightmare’ scenario for the public cloud,” they concluded. “Azurescape is evidence that they’re more real than we’d like to think. Cloud providers invest heavily in securing their platforms, but it’s inevitable that unknown zero-day vulnerabilities would exist and put customers at risk.”


To protect one’s Kubernetes assets, users can implement the following best practices, the firm advised:


On the latter point: “We see adversaries actively abusing the SelfSubjectReview APIs to inspect the privileges of stolen Kubernetes credentials,” according to the analysis. “[We] recently observed the Siloscape malware leveraging these APIs to retrieve the permissions of the node it compromised, and then using them to determine whether to continue its campaign against [the cluster](https://threatpost.com/kubernetes-cyberattacks-argo-workflows/167997/).”


**It’s time to evolve threat hunting into a pursuit of adversaries.**[**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**Threatpost and Cybersixgill for**[**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**and get a guided tour of the dark web and learn how to track threat actors before their next attack.**[**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with independent researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[Kubernetes]] [[API]] [[ACI]] [[multitenant]] [[Azurescape]] [[ThreatPost]]
