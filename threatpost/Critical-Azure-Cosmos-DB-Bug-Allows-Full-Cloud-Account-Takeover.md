# Critical Azure Cosmos DB Bug Allows Full Cloud Account Takeover
### It’s unclear if Microsoft customers were breached during the months-long period where the #ChaosDB bug in Jupyter Notebooks was exploitable.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168986)
+ Date: August 27, 2021  12:49 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/27123642/Jupiter-e1630082270279.jpg)
A critical security vulnerability in Microsoft’s Azure cloud database platform – Cosmos DB – could have allowed full remote takeover of accounts, with admin rights to read, write and delete any information to a database instance.


According to researchers at Wiz, any Azure customer could access another customer’s account, without authentication. The bug, dubbed #ChaosDB, could be trivially exploited, and “impacts thousands of organizations, including numerous Fortune 500 companies,” according to researchers.


Microsoft disabled the buggy component after being alerted to it by Wiz and notified more than 30 percent of Cosmos DB customers about the issue, but “we believe the actual number of customers affected by #ChaosDB is higher,” according to a [Wiz writeup](https://chaosdb.wiz.io/), published on Thursday.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The firm added that any prior exploitation is unknown, and that “the vulnerability has been exploitable for months and every Cosmos DB customer should assume they’ve been exposed.”


Incidentally, the issue has no CVE because [cloud bugs](https://threatpost.com/azure-functions-privilege-escalation/165307/) aren’t designated within that system, researchers added.


**Scant Bug Details for #ChaosDB**
----------------------------------


The issue exists in the Jupyter Notebook feature of Cosmos DB, according to the analysis. Jupyter Notebook is an open-source web application that allows users to create and share documents that contain live code, equations, visualizations and narrative text.


“Azure Cosmos DB built-in Jupyter Notebooks are directly integrated into the Azure portal and your Azure Cosmos DB accounts, making them convenient and easy to use,” according to Microsoft’s [documentation](https://docs.microsoft.com/en-us/azure/cosmos-db/cosmosdb-jupyter-notebooks). “Developers, data scientists, engineers and analysts can use the familiar Jupyter Notebooks experience to do data exploration, data cleaning, data transformations, numerical simulations, statistical modeling, data visualization and machine learning.”


However, Wiz researchers found that by querying information about a target Cosmos DB Jupyter Notebook, it’s possible to snag credentials for not just the Jupyter Notebook compute instance and the Jupyter Notebook Storage account of another user, but also the Cosmos DB account itself including the account’s primary read-write key used to encrypt it.


“Using these credentials, it is possible to view, modify and delete data in the target Cosmos DB account via multiple channels,” according to Wiz.


The company isn’t providing further technical details beyond the fact that #ChaosDB is actually made up of a string of vulnerabilities that can be chained together; but it did provide an attack diagram:


![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/27121310/diagram.gif)


It also released a video demonstrating a proof-of-concept exploit:


**How to Protect Against #ChaosDB Cyberattacks**
------------------------------------------------


To mitigate the risk, Microsoft has advised customers to regenerate the Cosmos DB primary keys “out of an abundance of caution.” The steps for doing so [can be found here](https://docs.microsoft.com/en-us/azure/cosmos-db/secure-access-to-data?tabs=using-primary-key#primary-keys).


The computing giant also noted that Azure Cosmos DB accounts with a vNET or that are firewall-enabled are protected by additional security mechanisms that prevent risk of unauthorized access.


Wiz researchers, who earned a $40,000 bug bounty for finding the issue, added that all users should review all past activity in their Cosmos DB accounts.


No in-the-wild exploitation has been noticed as of yet.


“We have no indication that external entities outside the researcher had access to the primary read-write key associated with your Azure Cosmos DB account(s),” Microsoft said. “In addition, we are not aware of any data access because of this vulnerability.”


 




#### Tags:
[[Jupyter]] [[#ChaosDB]] [[Microsoft]] [[ThreatPost]]
