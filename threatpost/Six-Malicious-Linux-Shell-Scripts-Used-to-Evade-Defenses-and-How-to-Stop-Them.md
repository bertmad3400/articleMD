# Six Malicious Linux Shell Scripts Used to Evade Defenses and How to Stop Them
### Uptycs Threat Research outline how malicious Linux shell scripts are used to cloak attacks and how defenders can detect and mitigate against them.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168127)
+ Date: July 29, 2021  9:00 am
+ Author: Unknown


## Article:
![Six Malicious Linux Shell Scripts Used to Evade Defenses and How to Stop Them](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26105054/Six-Malicious-Linux-Shell-Scripts-Used-to-Evade-Defenses-and-How-to-Stop-Them-.jpg)
*Siddartha Sharma and Adhokshaj Mishra*


Evasive techniques used by attackers, date back to the earlier days, when base64 and other common encoding schemes were used. Today, attackers are adopting new Linux shell script tactics and techniques to disable firewalls, monitoring agents and modifying access control lists (ACLs).


In previous [Uptycs Threat Research posts](https://www.uptycs.com/blog/tag/threat-research/?utm_source=threatpost&utm_medium=sponsorship&utm_campaign=threat_research), we discussed the common utilities in Linux, which are generally used by threat actors in the attack chain. In this report, we highlight those common defense evasion techniques, which are common in malicious Linux shell scripts. And then, we outline how Uptycs spots and mitigates against them.


In this post, we cover common evasive shell-script techniques as:


*The hash 39ac019520a278e350065d12ebc0c24201584390724f3d8e0dc828664fee6cae will be used to demonstrate and explain these techniques.*


**Technique 1: Uninstalling monitoring Agents**
-----------------------------------------------


Monitoring agents are the software components that regularly monitor the activities going on in the system related to process and network. Various logs are also created by the monitoring agents, which helps as an aid during any incident investigation.


The malicious script, we found in our in-house osquery based sandbox tries to:


Uninstall BCM client management agent which is generally installed on Endpoints for risk mitigation.


[![figure 1- Script Uninstalling monitoring agents](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26102529/igure-1-Script-Uninstalling-monitoring-agents.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26102529/igure-1-Script-Uninstalling-monitoring-agents.png)


**Technique 2: Disabling Firewalls and Interrupts**
---------------------------------------------------


Most of the systems and servers deploy firewalls as a defense mechanism.In the malicious script, attackers try to disable the firewall i.e., uninterrupted firewall (**ufw**) as a defense evasive tactic. Along with that, attackers also remove iptables rules (**iptables -F**) because it is widely used for managing the firewall rules on Linux systems and servers. (see figure 2)


[![Figure 2- Script Disabling Firewall](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26102701/Figure-2-Script-Disabling-Firewall-.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26102701/Figure-2-Script-Disabling-Firewall-.png)


Attackers also used the commands to disable **non-maskable Interrupt(nmi)**. Watchdog is basically a configurable timer mechanism which generates interrupt at a particular given condition and time. In case of the system freeze, the nmi watchdog interrupt handler would kill the task which is responsible for the system freeze. To evade this defense mechanism, attackers disable watchdog feature using sysctl command or temporarily disabling it by setting the value to ‘0’. (see figure 3)


[![Figure 3- Script Disabling kernel watchdog](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26102756/Figure-3-Script-Disabling-kernel-watchdog-.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26102756/Figure-3-Script-Disabling-kernel-watchdog-.png)


**Technique 3: Disabling Linux Security Modules (LSMs)**
--------------------------------------------------------


The malicious shell script also disables Linux security modules like SElinux, Apparmor. These modules are designed to implement mandatory access control(MAC) policies. A server administrator could simply configure these modules to provide the users restricted access to the installed or running applications in the system.


***AppArmour***


AppArmour is a security feature in Linux which is used to lock down applications like Firefox for increased security. A user can restrict an application in Ubuntu’s default configuration by giving limited permission to a certain application.


[![Figure 4- Commands disabling AppArmour](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26102900/Figure-4-Commands-disabling-AppArmour-.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26102900/Figure-4-Commands-disabling-AppArmour-.png)


***SElinux***


SElinux is another security feature in Linux systems by which a security administrator could apply security context on certain applications and utilities. On some web servers, the shell is disabled or restricted so for RCE (Remote Code Execution) adversaries usually bypass/disable this:


[![Figure 5- Commands disabling SElinux](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26102944/Figure-5-Commands-disabling-SElinux-.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26102944/Figure-5-Commands-disabling-SElinux-.png)


**Technique 4: Modifying ACLs**
-------------------------------


ACLs, or Access Control Lists, contain the rules by which permissions on files and utilities are granted. Filesystem ACLs tell operating systems which users can access the system, and what privileges the users are allowed. **Setfacl** utility in Linux is used to modify, remove the ACL, in the script we can see the usage of setfacl which sets permissions of chmod for the user:


[![Figure 6- ACL modification](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26103042/Figure-6-ACL-modification-.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26103042/Figure-6-ACL-modification-.png)


**Technique 5: Changing Attributes**
------------------------------------


**Chattr** in Linux is used to set/unset certain attributes of a file, more on [chattr utility here](https://man7.org/linux/man-pages/man1/chattr.1.html). Adversaries use this for their own dropped files or to make their files immutable so that a user cannot delete it:


[![Figure 7.1- Chattr usage for dropped malicious file](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26103124/Figure-7.1-Chattr-usage-for-dropped-malicious-file--300x77.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26103124/Figure-7.1-Chattr-usage-for-dropped-malicious-file-.png)


Another scenario:


[![Figure 7.2- Making the keys file immutable](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26103202/Figure-7.2-Making-the-keys-file-immutable-.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26103202/Figure-7.2-Making-the-keys-file-immutable-.png)


**Technique 6: Renaming common Utilities**
------------------------------------------


One of the malicious scripts (**d7c4693f4c36d8c06a52d8981827245b9ab4f63283907ef8c3947499a37eedc8**) also contained common utilities like wget,curl used with different names. These utilities are generally used to download files from the remote IP. Attackers use these utilities to download malicious files from C2.Some of the security solutions whose detection rules monitor the exact names of the utilities might not trigger the download event if **wget,curl** are used under different names.


[![Figure 8- Utilities getting renamed in the script](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26103438/Figure-8-Utilities-getting-renamed-in-the-script-.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26103438/Figure-8-Utilities-getting-renamed-in-the-script-.png)


[![Figure 9- Usage of renamed common utilities](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26103522/Figure-9-Usage-of-renamed-common-utilities-.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26103522/Figure-9-Usage-of-renamed-common-utilities-.png)


**Uptycs EDR Detections**


[Uptycs EDR armed with YARA](https://www.uptycs.com/webinar-registration-yara-osquery-malware-hunting/?utm_source=threatpost&utm_medium=sponsorship&utm_campaign=threat_research) process scanning detected these malicious scripts with a threat score of 10/10.


[![Figure 10- chattr and setfacl usage](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26103625/Figure-10-chattr-and-setfacl-usage-.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26103625/Figure-10-chattr-and-setfacl-usage-.png)


[![Figure 11-Toolkit data showing attribution](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26103711/Figure-11-Toolkit-data-showing-attribution-.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26103711/Figure-11-Toolkit-data-showing-attribution-.png)


Uptycs EDR Queries


Alongside the detections, Uptycs EDR also records all the events we mentioned above in the **process\_events table**. Using the queries below, incident response analysts can easily identify such malicious events:


***Firewall disabling***


select * from process\_events where exe\_name = ‘ufw’;


***ACL modification***


select * from process\_events where exe\_name = ‘setfacl’;


***Chattr utility usage***


select * from process\_events where exe\_name = ‘chattr’ and cmdline = ‘chattr +ia /home/hilde/.ssh/authorized\_keys2’;


***Checking renamed common utilities (wget,curl)***


select * from process\_events where exe\_name = ‘mv’;


**Conclusion**
--------------


As attackers are using more sophisticated and novel methods for evasion, it becomes increasingly important to monitor and record the activities happening in the system. Uptycs EDR offers the added benefit of taking a deep dive into the events logged, providing more insights of an attack. The reactive nature of Uptycs’ EDR helps to log everything whatever goes on in the system.


We recommend the following measures:


**Hashes**


**Want to Learn More About How Uptycs Can Help Secure Your Linux Environments?** [**Watch A 15-Minute Demo!**](https://www.uptycs.com/-thankyou-uptycs-15-minute-linux-demo/?utm_source=threatpost&utm_medium=sponsorship&utm_campaign=threat_research)




#### Tags:
[[Linux]] [[Uptycs]] [[EDR]] [[process_events]] [[exe_name]] [[system.]] [[ThreatPost]]
