# Argo CD Security Bug Opens Kubernetes Cloud Apps to Attackers
### The popular continuous-delivery platform has a path-traversal bug (CVE-2022-24348) that could allow cyberattackers to hop from one application ecosystem to another.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178239
+ Date: 2022-02-04T18:26:07+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2019/03/02162457/Containers.jpg)

A high-severity security vulnerability in Argo CD can enable attackers to access targets’ application-development environments, paving the way for stealing passwords, API keys, tokens and other sensitive information.


Argo CD is a continuous-delivery platform deployed as a Kubernetes controller in the cloud, and it’s used to deploy applications, then continuously monitor them in real time as they run.


The bug is a path-traversal issue, according to Apiiro’s security-research team, which occurs when adversaries are able to access files and directories that are stored outside their permissioned purview. It carries a score of 7.7 out of 10 o the CVSS vulnerability-severity scale.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Attackers can exploit the bug (CVE-2022-24348) by loading a malicious Kubernetes Helm Chart YAML file into the Argo CD system, then using it to “hop” from their own application ecosystem to access other applications’ data, researchers said.


**Breaking Down the Argo Attack Vector**
----------------------------------------


The vulnerability exists in the way Argo CD handles the control for its anti-path-traversal security mechanism, according to Apiiro.


In terms of how the bug can be specifically exploited, it’s important to understand how users can leverage Argo CD to build an application-deployment pipeline, Apiiro noted. They can do this in two ways: By defining a Git repository; or by building a Kubernetes Helm Chart file. The issue lies in the latter approach.


“A Helm Chart is a YAML file that embeds different fields to form a declaration of resources and configurations needed in order for deploying an application,” according to an Apiiro [analysis on Thursday](https://apiiro.com/blog/malicious-kubernetes-helm-charts-can-be-used-to-steal-sensitive-information-from-argo-cd-deployments/). The file includes “the metadata and information needed to deploy the appropriate Kubernetes configuration, and the ability to dynamically update the cloud configuration as the manifest is being modified.”


The application being built may have certain building blocks, which could be housed in other files that function as self-contained application parts kept in a repository.


“Repositories are saved on a dedicated server or pod named argocd-reposerver,” according to Apiiro. “There is no strong segmentation apart from file hierarchy, so the anti-path-traversal mechanism is a critical linchpin of file security.”


**A Problematic Anti-Path-Traversal Mechanism**
-----------------------------------------------


Argo CD’s anti-path-traversal mechanism is handled by single file in the source code, according to the analysis. The file performs the procedural cleanup of source path input – and it checks that the resulting cleaned-up version of the path matches the subdirectory of the current operating directory. It does this by evaluating listed elements under the Helm Chart’s valueFiles field.


The valueFiles fields are parsed by the application starting with a preliminary check for input value content: “The code searches for a patterned string that will fit into the mold of a URI by utilizing a function called ParseRequestURI,” explained researchers.


ParseRequestURI parses a raw URL into a URL structure, and it assumes that the raw URL was received in an HTTP request, they noted. This in turn makes it possible to confuse the parser, to make it think that a local file-path name is a valid URL – which would cause it to skip the cleanup and anti-path-traversal mechanism check, they said.


“If the valueFiles listed are going to look like a URI, it will be treated as one, skipping all other checks and treating it as a legitimate URL,” explained the researchers. “Because the default behavior of the function is to take for granted that it receives an HTTP request, it can be an absolute path of a URL like /directory/values.yaml. When looking at it as a URL, it passes the sanity test but is an absolute file-path.”


Thus, attackers can use a specially crafted Helm Chart, boobytrapped with requests for application file paths that lead to portions of application environments outside their purview, according to Apiiro – which tend to be guessable.


“Because the reposerver uses a monolithic and deterministic file-structure, all the other out-of-bound applications have a definite and predictable format and path,” the researchers said. “An attacker can assemble a concatenated, direct call to a specified values.yaml file, which is used by many applications as a vassal for secret and sensitive values.”


**Exploitation Impact**
-----------------------


If cyberattackers successfully exploit the bug, they can read the contents of other files present on the reposerver, which can contain sensitive information, according to the analysis. While that’s concerning enough, researchers also noted that an exploit could offer a foothold for moving laterally through an organization’s cloud.


“Because application files usually contain an assortment of transitive values of secrets, tokens and environmental sensitive settings – this can effectively be used by the attacker to further expand their campaign by moving laterally through different services and escalating their privileges to gain more ground on the system and target organization’s resources,” they explained.


Administrators should update with Argo CD’s patch as soon as possible, especially in light of the fact that cyberattackers are following the increasing number of organizations moving workloads to cloud resources and Kubernetes.


It’s also worth noting that Argo itself has been used in the past to carry out attacks. Last July [it came to light](https://threatpost.com/kubernetes-cyberattacks-argo-workflows/167997/) that misconfigured permissions for Argo Workflows’ web-facing dashboard were being exploited by unauthenticated attackers to run code on Kubernetes targets, including cryptomining containers.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=RTM]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Bern]] [[victim.country.name=Switzerland]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Kubernetes]] [[Apiiro]] [[Url]] [[Cloud]] [[Anti-path-traversal]] [[Valuefiles]] [[“because]] [[ThreatPost]]
#### CVE's
[[CVE-2022-24348]]

