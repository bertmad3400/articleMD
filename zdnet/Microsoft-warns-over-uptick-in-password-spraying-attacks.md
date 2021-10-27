# Microsoft warns over uptick in password spraying attacks
### State-sponsored hackers and cyber criminals are going after identities with password spraying, a low-effort and high-value method for the attacker, says Microsoft's Detection and Response Team (DART).

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/microsoft-warns-over-uptick-in-password-spraying-attacks/)
+ Date: October 27, 2021
+ Author: Liam Tung


## Article:
Unknown

Cyber attackers aren't just looking for software flaws, supply chain weakness, and open RDP connections. The other key asset hackers are after is identities, especially account details that will give them access to other internal systems.

CISA earlier [this year warned that the suspected Kremlin-backed hackers behind the SolarWinds attacks](https://www.zdnet.com/article/cisa-solarwinds-hackers-also-used-password-guessing-to-breach-targets/) were not just trojanising software updates, but also password guessing and password spraying administrative accounts for initial access.


More recently, Microsoft observed an [emerging Iranian hacking group using password spraying](https://www.zdnet.com/article/microsoft-warns-over-password-attacks-against-250-office-365-customers/) against Israeli and US critical infrastructure targets operating in the Persian Gulf. 

**SEE:** [**Ransomware: Industrial services top the hit list - but cyber criminals are diversifying**](https://www.zdnet.com/article/ransomware-industrial-services-are-still-the-most-popular-target-but-now-cyber-criminals-are-diversifying-attacks/)

Microsoft estimates that more than a third of account compromises are password spraying attacks, even though such attacks have a 1% success rate for accounts, unless organisations use Microsoft's '[password protection' to avoid bad passwords](https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-password-ban-bad). 

"Instead of trying *many passwords against one user*, they try to defeat lockout and detection by trying *many users against one password*," [Microsoft explained last year](https://techcommunity.microsoft.com/t5/azure-active-directory-identity/advancing-password-spray-attack-detection/ba-p/1276936). That approach helps avoid rate limiting, where too many failed password attempt results in a lockout. 

[Microsoft's Detection and Response Team (DART) has outlined](https://www.microsoft.com/security/blog/2021/10/26/protect-your-business-from-password-sprays-with-microsoft-dart-recommendations/) two main password spray techniques, the first of which it calls 'low and slow'. Here, a determined attacker deploys a sophisticated password spray using "several individual IP address to attack multiple accounts at the same time with a limited number of curated password guesses."






The other technique, 'availability and reuse', exploits previously compromised credentials that are posted and sold on the dark web. "Attackers can utilize this tactic, also called 'credential stuffing,' to easily gain entry because it relies on people reusing passwords and usernames across sites," Microsoft explains.

Legacy and unsecured authentication protocols are a problem because they can't enforce multi-factor authentication. Attackers are also focussing on the REST API, says DART. Top applications targeted include Exchange ActiveSync, IMAP, POP3, SMTP Auth, and Exchange Autodiscover.

"Recently, DART has seen an uptick in cloud administrator accounts being targeted in password spray attacks," Microsoft notes.   

Extra care should also be taken when configuring security controls for roles such as security admins, Exchange service admins, Global admins, Conditional Access admins, SharePoint admins, Helpdesk admins, Billing admins, User admins, Authentication admins, and Company admins. High-profile identities such as C-level execs or specific roles with access to sensitive data are also popular targets, says Microsoft.

Microsoft this [week warned that the SolarWinds hackers, a.k.a. Nobelium](https://www.zdnet.com/article/solarwinds-hacking-group-nobelium-is-now-targeting-the-global-it-supply-chain-microsoft-warns/), were employing [password spray attacks on new targets](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks/), primarily against managed service providers that have been delegated admin access by upstream customers.

**SEE:** [**Ransomware: Looking for weaknesses in your own network is key to stopping attacks**](https://www.zdnet.com/article/ransomware-looking-for-weaknesses-in-your-own-network-is-key-to-stopping-attacks/)

Microsoft found that Nobelium was "targeting privileged accounts of service providers to move laterally in cloud environments, leveraging the trusted relationships to gain access to downstream customers and enable further attacks or access targeted systems."

[The attacks are not the result of a product security vulnerability](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks/), Microsoft stressed, "but rather a continuation of Nobelium's… dynamic toolkit that includes sophisticated malware, password sprays, supply chain attacks, token theft, API abuse, and spear phishing to compromise user accounts and leverage the access of those accounts."

DART offers some handy tips to help shape the course of an investigation, such as determining whether the spray attack was successful on at least one account, determining which users were affected, and whether admin accounts were compromised.





#### Tags:
[[admins,]] [[Microsoft]] [[ZDNet]]
