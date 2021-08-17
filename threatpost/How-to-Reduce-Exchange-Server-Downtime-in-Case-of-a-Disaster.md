# How to Reduce Exchange Server Downtime in Case of a Disaster?
### Exchange downtime can have serious implications on businesses. Thus, it’s important to maintain backups and implement best practices for Exchange servers that can help restore the Exchange server when a disaster strikes with minimal impact and downtime.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168344)
+ Date: August 17, 2021  9:00 am
+ Author: Unknown


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/04065749/How-to-Reduce-Exchange-Server-downtime-in-Case-of-a-Disaster.jpg)
Exchange Server downtime may occur at any point in time due to several reasons, such as malware attack, server crash, database corruption, and hardware or software-related issues/incompatibility. However, downtime can impact productivity and lead to data loss that can have severe implications on your business. According to [Gartner](http://blogs.gartner.com/andrew-lerner/2014/07/16/the-cost-of-downtime/) Research, one minute downtime can cost around $5600 on average, depending on the size of the business.


Exchange Server downtime is inevitable, especially when your organization relies on a standalone on-premises Exchange server. However, you can reduce the downtime in the event of a disaster if you maintain a regular verified backups or use an Exchange recovery software.


In this guide, we’ll discuss some quick tips to minimize the Exchange Server downtime and restore the services without impacting the users.


Maintain VSS Backup
-------------------


To avoid downtime and data loss due to database corruption, administrators can create Volume Snapshot Service or Volume Shadow Copy Service-based (VSS-based) backups in Microsoft Exchange Server using the Windows Server backup plug-in. You may also use other backup applications which are application-aware and compatible with the installed Exchange Server and Service pack level.


[![VSS Backup](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/04065345/VSS-Backup.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/04065345/VSS-Backup.png)


A regular backup can help restore the mailbox database and mailbox connectivity after a malicious attack, database corruption, or server crash, with minimum and acceptable downtime depending on the resources and performance. A VSS-based backup is more critical for standalone on-premises Exchange Servers. To know more, refer to [Microsoft Guide on Windows Server Backup](https://docs.microsoft.com/en-us/exchange/high-availability/disaster-recovery/backup-with-windows-server-backup?view=exchserver-2019).


Update Exchange and Windows
---------------------------


To prevent malicious attacks, such as Hafnium, you must install the Exchange Server and Windows Server updates as they arrive. Microsoft regularly releases security updates to patch vulnerabilities that the hackers could exploit to attack your Exchange server, leading to data loss and database corruption.


You can refer to [this guide](https://www.stellarinfo.com/blog/microsoft-exchange-remote-code-execution-vulnerability-flaws-and-fixes/) to learn more about recent attacks, vulnerability flaws, and their fixes.


***TIP:*** *Although patches are released periodically, it’s always suggested to keep an eye on vulnerabilities announcements and also to lock down and harden your Exchange Server setup.*


Database Availability Group (DAG)
---------------------------------


Database Availability Group (DAG) is a group of Exchange mailbox servers that host a set of databases and provides automatic recovery when a disaster strikes. DAG requires at least two Exchange servers with a file witness server. It replicates the database copies across all Exchange Servers and thus, ensures high availability even when one of the servers crashes or the database is damaged and dismounted from the active server.


[![Database Availability Group (DAG)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/04065451/Database-Availability-Group-DAG.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/04065451/Database-Availability-Group-DAG.png)


However, DAG does not protect from malicious attacks as the infected copies of the database might get replicated across all passive Exchange servers. Thus, it’s critical to maintain backups.


Remember, DAG is not an alternative to backup! DAG will give you a peace of mind if one server fails in your infrastructure. It is also ideal to test the patches in DAG environment. You can redirect the users to the other server and turn off the main server for hardware and software maintenance without causing any downtime.


Uninterrupted Power Supply
--------------------------


Unexpected power failure or power outages can not only lead to downtime but can also damage the transaction logs and databases as the databases do not get the necessary time to shutdown properly. Sudden power loss can also lead to hardware failure, inconsistencies, and [Dirty Shutdown state](https://www.stellarinfo.com/article/resolve-exchange-dirty-shutdown-error.php) (database dismount).


Thus, it’s crucial to ensure an uninterrupted power supply to the Exchange Server and network devices. To avoid such situations, install an Uninterrupted Power Supply (UPS) unit which will ensure that the server doesn’t power off if there is a few minutes of power loss. Also, set up DAG with one server located in another office or branch and keep the spare hardware components in case the server hardware gets damaged.


***TIP:*** *It is always suggested to have the server with dual power supply just in case one fails.*


Ensure Sufficient Storage Space
-------------------------------


Low storage can also cause database corruption. Thus, it’s critical to ensure the drive storing database and transaction logs have sufficient storage space to store data.


Database size may grow over time. Transaction logs are generated in large numbers, which can quickly eat up the entire free space on the disk. Thus, it’s recommended to store database and transaction logs on two separate volumes or drives, especially when running a standalone Exchange server. This will help you conserve the storage space and recover the database if it gets damaged due to inconsistency issues or uncommitted transaction logs.


Also, you can create VSS backups regularly to automatically and safely truncate the transaction logs to free up the storage space.


Disaster Recovery
-----------------


Be prepared for disasters, such as server crash, database or mailbox corruption, etc. Disaster may strike unexpectedly, which can lead to downtime and data loss.


Based on the level of disaster, you can perform the disaster recovery steps to recover the server, database, or mailbox.


You may also use an Exchange Recovery software, such as [Stellar Repair for Exchange](https://www.stellarinfo.com/edb-exchange-server-recovery.htm), to recover mailboxes from a crashed server or corrupt database. It’s a GUI-based software that helps you quickly restore mailbox connectivity by restoring the mailboxes from a damaged database directly to a new or existing database on an Exchange server or Office 365. The software automates the recovery tasks, which helps reduce downtime in the event of a disaster and saves you from manual efforts.


Conclusion
----------


Regular VSS-based backups are the easiest and convenient way to avoid Exchange server downtime and data loss due to issues, such as database corruption.


However, if the backups aren’t available or do not work, you can use the EseUtil in Exchange server to soft repair or hard repair (when soft repair fails) the database. The utility mostly works when the damage is low. However, you should avoid the hard repair as it purges any irrecoverable data from the database. This can lead to data loss.


Another process which should be included in a business yearly routine is to do a disaster recovery test where the services and data are restored to a remote site and tested. This process should be documented. So, in case of a disaster, there is a plan. Also, it is highly suggested to make a restore test to ensure that the backups are working fine and the data is verified. As a precaution and pre-disaster situation, it is highly suggested to setup monitoring and E-Mail/SMS notifications on storage, compute, services, power, and temperature to ensure optimal performance of the servers.


Nonetheless, even though you try to prevent any disaster as much as possible, it can still happen. A better way to ensure fast and reliable recovery of services with no data loss is to use an [Exchange recovery software](https://www.stellarinfo.com/edb-exchange-server-recovery.htm), such as Stellar Repair for Exchange. The tool helps you recover all the mailboxes from a damaged or corrupt database and saves them as PST. You can also export the recovered mailboxes directly to the live Exchange Server or Office 365 tenants.




#### Tags:
[[However,]] [[it’s]] [[corruption,]] [[server.]] [[Windows]] [[Thus,]] [[crash,]] [[standalone]] [[Microsoft]] [[corruption.]] [[ThreatPost]]
