# Kubernetes Cloud Clusters Face Cyberattacks via Argo Workflows
### Misconfigured permissions for Argo’s web-facing dashboard allow unauthenticated attackers to run code on Kubernetes targets, including cryptomining containers.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167997)
+ Date: July 21, 2021  11:19 am
+ Author: Tara Seals


## Article:
![AWS computing](https://media.threatpost.com/wp-content/uploads/sites/103/2020/08/21091044/podcast-news-wrap.jpg)
Kubernetes clusters are being attacked via misconfigured Argo Workflows instances, security researchers are warning.


Argo Workflows is an open-source, container-native workflow engine for orchestrating parallel jobs on Kubernetes – to speed up processing time for compute-intensive jobs like machine learning and big-data processing. It’s also used to simplify container deployments in general. Kubernetes, meanwhile, is a popular container-orchestration engine for managing cloud deployments.


Malware operators are dropping cryptominers into the cloud via Argo thanks to some instances being publicly available via dashboards that don’t require authentication for outside users, according to an analysis from Intezer. These misconfigured permissions thus can allow threat actors to run unauthorized code in the victim’s environment.



“In many instances, permissions are configured which allow any visiting user to deploy workflows,” according to the Intezer analysis, [published Tuesday](https://www.intezer.com/blog/container-security/new-attacks-on-kubernetes-via-misconfigured-argo-workflows). “In instances when permissions are misconfigured, it is possible for an attacker to access an open Argo dashboard and submit their own workflow.”


Researchers said the misconfigurations can also expose sensitive information such as code, credentials and private container-image names (which can be used to assist in other kinds of attacks).


Intezer’s scan of the web found scads of unprotected instances, operated by companies in several industries, including technology, finance and logistics.


“We have identified infected nodes and there is the potential for larger-scale attacks due to hundreds of misconfigured deployments,” according to Intezer. In one case, bad code was running on an exposed cluster in Docker Hub for nine months before being discovered and removed.


Attacks aren’t difficult to carry out: Researchers observed different popular Monero-mining malware being housed in containers located in repositories like Docker Hub, including Kannix and XMRig. Cybercriminals need only to pull one of those containers into Kubernetes via Argo or another avenue. For instance, Microsoft recently [flagged a wave of miners](https://threatpost.com/microsoft-cryptomining-kubeflow/166777/) infesting Kubernetes via the Kubeflow framework for running machine-learning workflows.


“In Docker Hub, there are still a number of options for Monero-mining that attackers can use,” researchers said. “With a simple search it shows that there are at least 45 other containers with millions of downloads.”


**How to Check for Argo Misconfigurations**
-------------------------------------------


The quickest way to see if permissions are configured correctly is to simply try accessing the Argo Workflows dashboard from an unauthenticated incognito browser outside the corporate environment, researchers noted.


A more technology-focused way to check is to query the API of an instance and check the status code, researchers added.


“Make a HTTP GET request to [your.instance:port]/api/v1/info,” according to the analysis. “A returned HTTP status code of ‘401 Unauthorized’ while being an unauthenticated user will indicate a correctly configured instance, whereas a successful status code of ‘200 Success’ could indicate that an unauthorized user is able to access the instance.”


Admins can also check for any suspicious activity in the logs and in the workflow timeline. Intezer pointed out that any workflows that have been running for an excessive amount of time could indicate cryptomining activity.


“Even if your cluster is deployed on a managed cloud Kubernetes service such as Amazon Web Service (AWS), EKS or Azure Kubernetes Service (AKS), the shared responsibility model still states that the cloud customer, not the cloud provider, is responsible for taking care of all necessary security configurations for the applications they deploy,” researchers noted.


**Cloud Misconfigurations Offer Cyberattack Vectors**
-----------------------------------------------------


Misconfigurations [continue to plague](https://threatpost.com/google-cloud-buckets-exposed-misconfiguration/159429/) the cloud sector and organizations of all sizes. An analysis last fall found that 6 percent of all Google Cloud buckets are misconfigured and left open to the public internet, for anyone to access their contents.


Sometimes those gaffes make headlines: In March it [was revealed](https://threatpost.com/hobby-lobby-customer-data-cloud-misconfiguration/164980/) that Hobby Lobby had left 138GB of sensitive information sitting in a cloud bucket open to the public internet. The trove included customer names, partial payment-card details, phone numbers, and physical and email addresses.


According to a Cloud Native Computing Foundation (CNCF) [2020 survey](https://www.cncf.io/wp-content/uploads/2020/11/CNCF_Survey_Report_2020.pdf), 91 percent of respondents were using Kubernetes, with respondents reporting that the top challenges of using and deploying containers are complexity, security and lack of training.


“Kubernetes … is one of the most popular repositories on GitHub, with over 100,000 commits and over 3,000 contributors,” Intezer researchers noted. “Each year there is a steady increase in enterprises using Kubernetes and the number of clusters they deploy. With these challenges that enterprises face using containers and Kubernetes clusters, there has never been a greater opportunity for attackers to exploit weaknesses in security…there is still always the possibility of misconfiguration or exploitation.”


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Kubernetes]] [[cloud]] [[Intezer]] [[misconfigured]] [[Workflows]] [[workflow]] [[workflows]] [[Misconfigurations]] [[Cloud]] [[ThreatPost]]
