# Microsoft shares guidance on securing Azure Cosmos DB accounts
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-shares-guidance-on-securing-azure-cosmos-db-accounts/)
+ Date: August 30, 2021
+ Author: Sergiu Gatlan


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/08/27/Azure-Cosmos-DB.jpg)


*Image: Microsoft*


Microsoft issued guidance on securing Azure accounts that may be impacted by a recently addressed Cosmos DB critical vulnerability, giving attackers full admin rights to users' data without authorization.


The flaw, dubbed [**ChaosDB**](https://www.bleepingcomputer.com/news/microsoft/microsoft-warns-azure-customers-of-critical-cosmos-db-vulnerability/), impacts [Microsoft Azure Cosmos DB](https://gotcosmos.com), a globally distributed NoSQL database service used by a wide assortment of high-profile customers, including Exxon-Mobil, Mercedes Benz, Symantec, Coca-Cola, and Citrix.


The security bug was found by the cloud security firm Wiz's research team in the Jupyter Notebook feature (enabled by default).


The security bug was found by the cloud security firm Wiz's research team in the Jupyter Notebook feature (enabled by default). Successful exploitation allowed any user to steal customers' primary read-write keys, letting them effectively takeover their databases remotely.


Over 30% of Cosmos DB customers notified of potential breach
------------------------------------------------------------


Microsoft says it "mitigated the vulnerability immediately" after receiving Wiz's report (the researchers' timeline shows that the bug was fixed within 48 hours after the disclosure.)


The company also alerted over 30% of Cosmos DB customers about a potential security breach on August 26, two weeks after disabling the buggy Jupyter Notebook feature server-side.


However, according to Wiz, the actual number of impacted customers is likely a lot larger since it would include most Cosmos DB customers, given that ChaosDB was present and could've been exploited for months before the disclosure.


"Our investigation indicates that no customer data was accessed because of this vulnerability by third parties or security researchers," Microsoft [said](https://msrc-blog.microsoft.com/2021/08/27/update-on-vulnerability-in-the-azure-cosmos-db-jupyter-notebook-feature/) on Friday.


"If you did not receive an email or in-portal notification, there is no evidence any other external parties had access to your primary read-write account key."


How to block the use of stolen credentials
------------------------------------------


To mitigate the risk and block attackers who might've stolen your Cosmos DB primary read-write keys before the vulnerable feature was disabled, Microsoft advises [regenerating the Cosmos DB keys](https://docs.microsoft.com/en-us/azure/cosmos-db/secure-access-to-data?tabs=using-primary-key#primary-keys).


As a best practice to further secure Azure Cosmos DB account, Microsoft also issued the following recommendations:


1. All Azure Cosmos DB customers use a combination of [firewall rules](https://docs.microsoft.com/en-us/azure/cosmos-db/how-to-configure-firewall), [vNet](https://docs.microsoft.com/en-us/azure/cosmos-db/how-to-configure-vnet-service-endpoint), and/or [Azure Private Link](https://docs.microsoft.com/en-us/azure/cosmos-db/how-to-configure-private-endpoints) on their account.  These network protection mechanisms prevent access from outside your network and unexpected locations.
2. In addition to implementing network security controls, we encourage the use of [Role Based Access Control](https://docs.microsoft.com/en-us/azure/cosmos-db/how-to-setup-rbac).  Role Based Access Control allows per user and security principal access control to Azure Cosmos DB – those identities can be audited in Azure Cosmos DB’s [diagnostic logs](https://docs.microsoft.com/en-us/azure/cosmos-db/monitor-cosmos-db-reference).
3. If you cannot use Role Based Access Control, we recommend implementing regularly scheduled [key rotations](https://docs.microsoft.com/en-us/azure/cosmos-db/secure-access-to-data?tabs=using-primary-key).
4. You can find additional security best practices in the Azure Cosmos DB [security baseline](https://docs.microsoft.com/en-us/security/benchmark/azure/baselines/cosmos-db-security-baseline) documentation.


Microsoft also added that it's including additional safeguards and monitoring to detect future attempts to gain access to its customers' Cosmos DB accounts without authorization.


Customers are also advised to toggle on Diagnostic Logging and [Azure Defender](https://docs.microsoft.com/en-us/azure/cosmos-db/cosmos-db-advanced-threat-protection?tabs=azure-portal) where available to make it easier to spot suspicious activity originating from unusual IP addresses.



The US Cybersecurity and Infrastructure Security Agency (CISA) has also urged Azure Cosmos DB customers to rotate their keys and check Microsoft's guidance on how to [Secure access to data in Azure Cosmos DB](https://docs.microsoft.com/en-us/azure/cosmos-db/secure-access-to-data?tabs=using-primary-key#primary-keys).


"Although the misconfiguration appears to have been fixed within the Azure cloud, CISA strongly encourages Azure Cosmos DB customers to roll and regenerate their certificate keys," the cybersecurity agency [said](https://us-cert.cisa.gov/ncas/current-activity/2021/08/27/microsoft-azure-cosmos-db-guidance).




#### Tags:
[[Microsoft]] [[Jupyter]] [[read-write]] [[Bleeping Computer]]
