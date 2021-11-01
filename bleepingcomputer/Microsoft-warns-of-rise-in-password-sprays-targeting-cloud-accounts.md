# Microsoft warns of rise in password sprays targeting cloud accounts
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-warns-of-rise-in-password-sprays-targeting-cloud-accounts/)
+ Date: October 31, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft warns of rise in password sprays targeting cloud accounts](https://www.bleepstatic.com/content/hl-images/2021/09/05/Microsoft.jpg)


The Microsoft Detection and Response Team (DART) says it detected an increase in password spray attacks targeting privileged cloud accounts and high-profile identities such as C-level executives.


[Password spraying](https://attack.mitre.org/versions/v8/techniques/T1110/003/) is a type of brute force attack where the attackers attempt to gain access to large lists of accounts using a small number of commonly used passwords.






These attacks often use the same password while switching from one account to another to find easy to breach accounts and avoid triggering defenses like password lockout and malicious IP blocking (when using a botnet).


This tactic makes it less likely to trigger an account lock as it happens when they're targeted in classic brute-forcing attacks that quickly try to log into a small number of accounts by going through an extensive password list, one account at a time.


"Over the past year, the Microsoft Detection and Response Team (DART), along with Microsoft's threat intelligence teams, have observed an uptick in the use of password sprays as an attack vector," DART said.


"Recently, DART has seen an uptick in cloud administrator accounts being targeted in password spray attacks, so understanding the targets is a good place to start."


DART recommends enabling and enforcing multi-factor authentication (MFA) across all accounts whenever possible and adopting passwordless technology to drastically lower the risk of account compromise when targeted by such attacks.


Admins and high profile accounts increasingly targeted
------------------------------------------------------


As Microsoft revealed one year ago, password spray attacks are among the most popular authentication attacks amounting to [over a third of enterprise account compromises](https://techcommunity.microsoft.com/t5/azure-active-directory-identity/advancing-password-spray-attack-detection/ba-p/1276936), according to Alex Weinert, Director of Identity Security at Microsoft.


DART has seen a wide array of administrator accounts with various permissions being targeted in recent password spray attacks.


The list of most popular targets includes accounts ranging from security, Exchange service, global, and Conditional Access administrators to SharePoint, helpdesk, billing, user, authentication, and company admins.


Besides this type of privileged accounts, threat actors have also attempted to compromise identities with a high profile (including C-level executives) or access to sensitive data.


"It is easy to make exceptions to policy for staff who are in executive positions, but in reality, these are the most targeted accounts. Be sure to apply protection in a democratic way to avoid creating weak spots in configuration," DART [added](https://www.microsoft.com/security/blog/2021/10/26/protect-your-business-from-password-sprays-with-microsoft-dart-recommendations/).


In July, the [NSA revealed](https://www.bleepingcomputer.com/news/security/nsa-russian-gru-hackers-use-kubernetes-to-run-brute-force-attacks/) that the Russian state-backed Fancy Bear hacking group launched password spray attacks against U.S. and foreign organizations, including the U.S. government and Department of Defense agencies, from Kubernetes clusters.


Microsoft also said earlier this month that it spotted both [Iran-linked DEV-0343](https://www.bleepingcomputer.com/news/security/microsoft-iran-linked-hackers-target-us-defense-tech-companies/) and the [Russian-sponsored Nobelium](https://www.bleepingcomputer.com/news/microsoft/microsoft-russian-svr-hacked-at-least-14-it-supply-chain-firms-since-may/) groups using password sprays in attacks targeting defense tech companies and managed service providers (MSPs) or cloud service providers, respectively.




#### Tags:
[[Microsoft]] [[cloud]] [[Bleeping Computer]]
