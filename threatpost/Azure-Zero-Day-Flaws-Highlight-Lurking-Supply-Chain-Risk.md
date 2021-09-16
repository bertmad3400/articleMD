# Azure Zero-Day Flaws Highlight Lurking Supply-Chain Risk
### Dubbed OMIGOD, a series of vulnerabilities in the Open Management Infrastructure used in Azure on Linux demonstrate hidden security threats, researchers said.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169508)
+ Date: September 16, 2021  7:37 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/17145342/cloud-e1629226435519.jpg)
Four Microsoft zero-day vulnerabilities in the Azure cloud platform’s Open Management Infrastructure (OMI) — a software that many don’t know is embedded in a host of services — show that OMI represents a significant security blind spot, researchers said.


Collectively dubbed “OMIGOD” because of the name and the reaction of the researchers who discovered them, the flaws — which were zero-day when found — affect thousands of Azure customers and millions of endpoints, according to a [blog post](https://www.wiz.io/blog/secret-agent-exposes-azure-customers-to-unauthorized-code-execution) published this week by cloud infrastructure security firm Wiz.


Though Microsoft patched them this week in its [monthly Patch Tuesday](https://threatpost.com/microsoft-patch-tuesday-exploited-windows-zero-day/169459/) raft of updates, their presence in OMI highlights the risk for the supply chain when companies unknowingly run code — particularly open-source code — on their systems that allows for exploitation, researchers said.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Indeed, recent high-profile supply-chain attacks such as [SolarWinds](https://threatpost.com/solarwinds-attackers-dhs-emails/165110/) and [Kaseya](https://threatpost.com/kaseya-patches-zero-days-revil-attacks/167670/) demonstrate how much damage can be done when undetected flaws in third-party software that organizations use in larger systems are exploited.


“One of the biggest challenges in preventing them is that our digital supply chain is not transparent,” senior security researcher Nir Ohfeld wrote in the Wiz post. “If you don’t know what’s hidden in the services and products you use every day, how can you manage the risk?


Indeed, the OMIGOD  vulnerabilities discovered by Ohfeld and his colleagues present a security danger to potentially millions of unsuspecting customers of cloud computing services, he said.


“In a small sample of Azure tenants we analyzed, over 65 percent [of Azure customers] were unknowingly at risk,” Ohfeld wrote.


The vulnerabilities that Wiz researchers discovered include one that allows for remote code execution (RCE), [CVE-2021-38647](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38647). The other three are privilege-escalation vulnerabilities ([CVE-2021-38648](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38648), [CVE-2021-38645](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38645) and [CVE-2021-38649)](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38649) of lower risk but which are critical for a full attack chain.


“Unless a patch is applied, attackers can easily exploit these four vulnerabilities to escalate to root privileges and remotely execute malicious code (for instance, encrypting files for ransom),” Ohfeld said.


**Hidden Cloud Security Danger in OMI**
---------------------------------------


One reason for the significant alarm over the flaws is that they are found in OMI, an agent automatically deployed when customers set up a Linux virtual machine (VM) in their cloud and enable certain Azure services, researchers explained.


“This happens without customers’ explicit consent or knowledge,” Ohfeld wrote. “Users simply click ‘agree’ to log collection during setup, and they have unknowingly opted in.”


OMI is a perilous attack surface because Azure provides “virtually no public documentation” about it, he said. That means most customers have never heard of it and are unaware that it even exists as an exploitable entity in their deployment.


Moreover, the OMI agent runs as root with the highest privileges, so any user can communicate with it using a UNIX socket or via an HTTP API when configured to allow external access, Ohfeld explained.


“As a result, the vulnerabilities we found would allow external users or low-privileged users to remotely execute code on target machines or escalate privileges,” he wrote.


**‘Textbook RCE Vulnerability”**
--------------------------------


[CVE-2021-38647](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38647), with a 9.8 severity rating, is the most serious of the flaws, allowing for RCE. However, for it to be exploited, the Azure product using OMI would have to be one, such as Configuration Management, that exposes an HTTPS port, or port 5986, for interacting with OMI.


“That’s what makes RCE possible,” Ohfeld explained. “Note that most Azure services that use OMI deploy it without exposing the HTTPS port.”


Calling the bug “a textbook RCE vulnerability that you would expect to see in the 90s” not in 2021, the flaw can expose millions of endpoints because “an attacker could use a single packet to become root on a remote machine by simply removing the authentication header,” Ohfeld wrote.


“Thanks to the combination of a simple conditional statement coding mistake and an uninitialized auth struct, any request without an Authorization header has its privileges default to uid=0, gid=0, which is root,” he explained.


In situations where the OMI ports are accessible to the internet to allow for remote management, threat actors can use the vulnerability co-obtain initial access to a target Azure environment and then move laterally within it, Ohfeld added.


“An exposed HTTPS port is the holy grail for malicious actors,” he observed. “With one simple exploit they can get access to new targets, execute commands at the highest privileges and possibly spread to new target machines.”


The other three flaws—with severity ratings that range from 7.1 to 7.8—can be used as part of attack chains once attackers gain initial low-privileged access to their targets, Ohfeld added.


**Threat Discovery and Mitigations**
------------------------------------


Wiz researchers reported the four vulnerabilities to Microsoft through the responsible disclosure process; the company patched them as of Tuesday, researchers said.


Upgrading OMI and thus patch installation happens through the parent Azure service that installed it, they added. “However, we urge customers to verify that their environment is indeed patched and they are running the latest version of OMI (Version 1.6.8.1),” Ohfeld wrote.


Different Azure services have different port numbers, Microsoft noted in its advisory for CVE-2021-38647. However, for customers who want to check that their Azure Linux Node does not have an exposed port, they should look for the command ‘*netstat -an | grep <port-number>*‘ on most Linux distributions, which will indicate if any processes are listening on an open port, the company said.


**Rule #1 of Linux Security:**No cybersecurity solution is viable if you don’t have the basics down. **[JOIN](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)** Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the **[4 Golden Rules of Linux Security](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)**. Your top takeaway will be a Linux roadmap to getting the basics right! **[REGISTER NOW](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar)**and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.




#### Tags:
[[Ohfeld]] [[OMI]] [[Linux]] [[said.]] [[wrote.]] [[Microsoft]] [[cloud]] [[explained.]] [[don’t]] [[it,]] [[ThreatPost]]
