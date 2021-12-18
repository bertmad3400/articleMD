# Convergence Ahoy: Get Ready for Cloud-Based Ransomware
### Oliver Tavakoli, CTO at Vectra AI, takes us inside the coming nexus of ransomware, supply-chain attacks and cloud deployments.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177112
+ Date: 2021-12-17T15:45:36+00:00
+ Author: Oliver Tavakoli


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/17145342/cloud-e1629226435519.jpg)

The two types of cyberattacks that have dominated the news over the past year have been ransomware, and software and service supply-chain attacks. The former have mainly been perpetrated by criminal enterprises looking to turn a quick profit. In contrast, the latter attacks have primarily been the domain of nation-states looking to expand their information-gathering capabilities.


There’s a good chance these two approaches will start converging — and it’s going to happen in the cloud.


One example of this already happening is the ransomware attack that leveraged [Kaseya software](https://threatpost.com/kaseya-patches-zero-day-exploits/167548/) – but that was a different kind of supply-chain attack in that the supply chain consisted of the managed security service providers (MSSPs) who were hosting Kaseya software on behalf of their customers. Kaseya itself (unlike SolarWinds) was not hacked, and all the action happened downstream.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Why are ransomware and the supply chain coming together? Historically, what started out as nation-state techniques make their way into pen-testing and red teaming tools and eventually become commoditized in attacks undertaken by hackers seeking profit. There’s no reason to think the same won’t happen in this case; thus, it is useful to consider tools and techniques employed in supply-chain attacks as a harbinger of what is to come to ransomware attacks.


**Cloud Leverage in Supply-Chain Attacks**
------------------------------------------


Nation-states have plenty of time and human capital to expend in supply-chain efforts, so the complexity or relatively unknown nature of the environment does not present a significant barrier. In fact, many nation-state attacks involve cloud components — they often mix and match traditional on-prem steps in an attack with steps taken in the cloud.


The SolarWinds hack was a case in point. After [hacking into SolarWinds](https://threatpost.com/solarwinds-attackers-dhs-emails/165110/) and laboriously crafting and inserting a payload into the Orion software, Cozy Bear (aka the Russian SVR) waited for software updates to go out and the infected Orion servers to call home. What followed from there was a careful selection of high-value targets to pursue. One of the common approaches, which was observed across multiple targets, was that the attackers went on to steal the [SAML certificate-signing key](https://www.varonis.com/blog/what-is-saml/). The end goal was to be able impersonate an authenticated user accessing data in Office 365 or other software-as-a-service (SaaS)-delivered applications.


More recently, that same threat actor (referred to by Microsoft as Nobelium) was [reported](https://threatpost.com/solarwinds-attackers-new-tactics-malware/176818/) to be hacking  MSSPs, expressly to gain access to administrative account credentials. These were used to create accounts in Azure Active Directory (AD), and then onward to victim’s on-premise AD — the cloud was used again.


This all comes against the backdrop of security monitoring having a particular scope (data center, cloud, federated identity, endpoints, etc.) — overall, security monitoring implemented by most organizations doesn’t do a good job of stitching these scopes together, and that presents another advantage to advanced attackers. As they hopscotch through these areas, they can generally count on any slightly suspicious behavior in one scope not leading to elevated concern in the next.


**The Traditional Nature of Ransomware Attacks**
------------------------------------------------


In contrast, most ransomware attacks that have made the news have been relatively pedestrian. They have used well-known tool chains that are also used by pen-testers and red teams (think Mimikatz, Cobalt Strike, BloodHound, etc.) to perpetrate attacks on relatively traditional IT environments.


There is generally very little reliance on zero-day vulnerabilities (Kaseya being an exception in that the attackers burned a couple of Kaseya VSA server zero-days). When software vulnerabilities *are* exploited as part of the attack, it’s typically via well-known vulnerabilities for which patches are already available but have not yet been applied by the target. The poster child for this was the [EternalBlue exploit](https://threatpost.com/scanner-shows-eternalblue-vulnerability-unpatched-on-thousands-of-machines/126818/) in the internal propagation of WannaCry in 2017 – Microsoft released the patch in March, while the large-scale outbreak of WannaCry happened in May.


**Why Ransomware Will Come to the Cloud**
-----------------------------------------


There is also Willie Sutton’s famous quote when asked why he robbed banks: “Because that’s where the money is.” The migration of data and applications to the cloud which was already well underway at the end of 2019 has been supercharged by the pandemic. And as almost every piece of data of value moves to the cloud, either into SaaS applications or into public-cloud stacks, attackers will undoubtedly follow to the cloud as the pickings for on-premise attacks become slim.


And thanks to the supply-chain attacks, detailed information on how clouds operate and how to attack them is becoming commoditized. So once the money moves to the cloud, the ability to attack there will not be limited to nation states.


**What Ransomware Will Look Like in the Cloud**
-----------------------------------------------


With most attacks, there is a question of what the initial point of entry will be and how that initial foothold will be expanded to gain access to valuable data.


We have already seen multiple points of entry to attacks involving the cloud:


* **Account takeover** – compromising an endpoint belonging to the organization by coaxing users to provide account credentials in seemingly legitimate exchanges.
* **Identity system takeover** – stealing an organization’s SAML-signing key allows the attacker to authenticate as any account in the system.
* **Sprawling DMZ** – workloads (often created by development teams) in the public cloud which are unpatched or unsecured, and are accessible to the internet without the organization’s security team being aware of them.


Lateral movement (from point of entry to targeted data) in the cloud almost always involves stolen or impersonated credentials, or the leverage of available APIs. Cloud systems come with incredibly powerful APIs – particularly for privileged credentials – which enable attackers to rapidly progress to their ultimate goal.


**Takeaways**
-------------


There are things organizations can do to prepare for these attacks:


* Ensure you keep your SAML-signing key under incredibly strict control and monitor any access to the system which uses the key.
* Review your multifactor authentication (MFA) policies – I know, everyone claims to have MFA enabled for all accounts, but most Azure AD customers do this via [conditional-access](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview) policies, which often contain a mess of contradictory logic which may or may not accomplish what you believe your policy to be.
* Review permissions granted to your cloud-accessible identities and practice principles of least privilege.
* Carefully monitor the creation of new privileged accounts as well as any use of privileged accounts.
* Know thy internet-accessible footprint – where possible, implement overarching policies which prevent a developer from accidentally exposing your cloud footprint to the internet and constantly scan for such accidents on the assumption that such policies can fail.
* Shift a substantial portion of your pen testing and red teaming efforts to your public cloud and SaaS applications – find out how hard a target you really are.


And obviously, put strict controls over the data you most care about and practice restoring the data from isolated backups.


***Oliver Tavakoli is CTO at [Vectra AI](http://www.vectra.ai).***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by visiting our [microsite](https://threatpost.com/microsite/infosec-insiders-community/).***





## Tags:

#### Threatactor:
[[threatactor.name=APT29]] [[threatactor.name=APT29]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=BloodHound]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Expand]] [[action.malware.name=Mimikatz]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]] [[action.malware.name=WannaCry]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Cloud]] [[Ransomware]] [[Supply-chain]] [[Kaseya]] [[Cloud]] [[Ransomware]] [[ThreatPost]]

