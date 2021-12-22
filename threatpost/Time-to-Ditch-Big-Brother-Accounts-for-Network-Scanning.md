# Time to Ditch Big-Brother Accounts for Network Scanning
### Yaron Kassner, CTO and co-founder of Silverfort, discusses why using all-seeing privileged accounts for monitoring is bad practice.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177194
+ Date: 2021-12-21T22:08:01+00:00
+ Author: Yaron Kassner


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/09151623/phishing-e1636488996585.jpg)

In almost every network, there is a highly privileged service account remotely connecting to all computers. These accounts are usually used by backup, security or monitoring solutions. But using such accounts to remotely login to systems on the network introduces unnecessary risk — it’s a bad practice, and an avoidable one.


An attacker can easily take advantage of these privileged accounts, as follows. 


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


First, the attacker obtains access to a computer in the network. This can be done by [exploiting vulnerabilities](https://threatpost.com/active-directory-bugs-windows-domain-takeover/177185/), phishing, a supply-chain attack and many other techniques. Then the attacker waits for the service account to connect to the compromised computer. When this happens, the attacker steals the credentials of the service account, and thus obtains domain administrator privileges. From this point forward, it becomes very hard to stop the attacker from complete domain takeover.


It’s important to note that this scenario is not theoretical. This attack vector is very common, since it is so easy to execute.


Many organizations are aware of this threat, and yet they continue to maintain these highly privileged service accounts. Even companies that have been attacked this way will continue to use these service accounts. That’s because the backup, monitoring and security vendors leave them no choice – claiming that’s the only way their solution works.


But there are alternatives. The most straightforward alternative is to have an agent on each computer contact the server for instructions, rather than allowing the server to connect to each computer. 


In addition, the instructions received from the server should be limited to the purpose of the agent. For example:


* A backup agent should be able to send encrypted files, but shouldn’t be able to perform the encryption itself;
* A monitoring agent should be able to send the CPU usage of the computer, but not install software on the computer;
* A software-update agent should be able to install software on the computer, but only software signed by the organization or a trusted vendor.


This way, an attacker that compromises a server would only be able to perform certain actions on the network rather than have complete access, and an attacker that compromises a computer in the network won’t be able to steal the server’s credentials to move laterally. 


This approach works. It’s already being used by many cloud-based solutions since they inherently don’t have access to on-premises environments. Due to this “limitation,” they were forced to come up with more secure ways to remotely manage devices.


How to Eliminate the Big-Brother Effect
---------------------------------------


So as much as we need backup, security and monitoring capabilities, it’s time to eliminate over-privileged domain service accounts. Here are several best practices to make this happen:


* When assessing a product, thoroughly review the permissions it uses, and whether they are needed;
* Also review how the permissions are being used;
* Give preference to solutions that pull configuration from a central location over solutions that remotely connect to computers to configure them;
* Restrict service accounts to the minimum access they need to perform their roles. This includes limiting their access to specific IP addresses and hosts. If they need access to all computers, restrict their access to only the relevant interfaces;
* Monitor privileged-service accounts for any deviation from their authorized behavior.


By saying no to granting domain admin privileges where they’re not needed, organizations can close a massive and dangerous security gap in their attack surfaces.


***Yaron Kassner is CTO and co-founder of [Silverfort](https://www.silverfort.com/).***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by visiting our [microsite](https://threatpost.com/microsite/infosec-insiders-community/).***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=CHOPSTICK]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[]] [[ThreatPost]]

