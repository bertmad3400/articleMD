# Cloud computing: Microsoft fixes Azure container flaw that could have leaked data
### Microsoft has plugged a container escape flaw affecting Azure Container Instances.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/cloud-computing-microsoft-fixes-azure-container-flaw-that-could-have-leaked-data/)
+ Date: September 9, 2021 -- 09:18 GMT (10:18 BST)
+ Author: Liam Tung


## Article:
Unknown

Microsoft has revealed that it has fixed a bug in its Azure Container Instances (ACI) service that may have allowed a user to access other customers' information in the ACI.    

[ACI lets customers run applications in containers on Azure](https://www.zdnet.com/article/microsoft-previews-new-azure-container-instance-service-on-linux/) using virtual machines that are managed by Microsoft rather than managing their own.   


Researchers from Palo Alto Networks reported the security bug to Microsoft, which recently addressed the issue.  

**SEE:**[**The CIO's new challenge: Making the case for the next big thing**](https://www.zdnet.com/article/the-cios-new-challenge-making-the-case-for-the-next-big-thing/#link=%7B%22linkText%22:%22The%20CIO's%20new%20challenge:%20Making%20the%20case%20for%20the%20next%20big%20thing%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/the-cios-new-challenge-making-the-case-for-the-next-big-thing/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)

Microsoft [said in a blogpost](https://msrc-blog.microsoft.com/2021/09/08/coordinated-disclosure-of-vulnerability-in-azure-container-instances-service/) there was no indication any customer information was accessed due to the vulnerability — both in the cluster the researchers were using or in other clusters. 

"Microsoft recently mitigated a vulnerability reported by a security researcher in the Azure Container Instances (ACI) that could potentially allow a user to access other customers' information in the ACI service. Our investigation surfaced no unauthorized access to customer data," it said.

Nonetheless, it has told customers who received a notification from it via the Azure Portal to revoke any privileged credentials that were deployed to the platform before August 31, 2021. 






Ariel Zelivansky, researcher at Palo Alto, told Reuters his team used a known vulnerability to escape Azure's system for containers. Since it was not yet patched in Azure, this allowed them to gain full control of a cluster. Palo Alto reported the container escape to Microsoft in July.  

Even without vulnerabilities, containerized applications, which are often hosted on cloud infrastructure, can be difficult to shield from attackers. The NSA and CISA recently [issued guidance for organizations to harden containerized applications because their underlying infrastructure can be incredibly complex](https://www.zdnet.com/article/hacker-target-kubernetes-to-steal-data-and-processing-power-now-the-nsa-has-tips-to-protect-yourself/). 

**SEE:** [**Open source matters, and it's about more than just free software**](https://www.zdnet.com/article/open-source-software-is-it-about-free-or-is-it-about-freedom/)

Microsoft noted that among other things admins should revoke privileged credentials on a regular basis.

Microsoft [disclosed a separate Azure vulnerability two weeks ago](https://www.zdnet.com/article/azure-cosmos-db-alert-critical-vulnerability-puts-users-at-risk/) affecting customers running NoSQL databases on Azure, which provides the Cosmos DB managed NoSQL DB service. A critical flaw, dubbed ChaosDB, allowed an attacker to read, modify or delete databases.  





#### Tags:
[[Microsoft]] [[Palo]] [[ZDNet]]
