# CISA says BlackMatter ransomware group behind recent attacks on agriculture companies
### New Cooperative and Crystal Valley were both hit with ransomware over the last two months.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/cisa-says-blackmatter-ransomware-group-behind-recent-attacks-on-agriculture-companies/)
+ Date: October 19, 2021
+ Author: Jonathan Greig


## Article:
Unknown

CISA, the FBI and NSA officially [implicated](https://us-cert.cisa.gov/ncas/alerts/aa21-291a) the BlackMatter ransomware group in the recent attacks on two agriculture companies, confirming the assessments of some security researchers who said the gang was behind incidents involving New Cooperative and Crystal Valley in September.

New Cooperative -- an Iowa-based farm service provider -- [was hit with a ransomware attack](https://www.zdnet.com/article/iowa-farm-services-provider-hit-with-blackmatter-ransomware-and-5-9-million-ransom/) on September 20 and BlackMatter demanded a $5.9 million ransom. Crystal Valley, based in Minnesota, [was attacked two days later](https://www.zdnet.com/article/crystal-valley-cooperative-becomes-latest-agriculture-business-hit-with-ransomware/). Both attacks came as harvests began to ramp up for farmers.

In the advisory, CISA, the FBI and NSA said BlackMatter has targeted multiple US critical infrastructure entities since July. The advisory provides a detailed examination of BlackMatter's tactics and outlines how the group typically attacks organizations. 

"Using embedded, previously compromised credentials, BlackMatter leverages the Lightweight Directory Access Protocol (LDAP) and Server Message Block (SMB) protocol to access the Active Directory (AD) to discover all hosts on the network," CISA said in the advisory. 

"BlackMatter then remotely encrypts the hosts and shared drives as they are found. Ransomware attacks against critical infrastructure entities could directly affect consumer access to critical infrastructure services; therefore, CISA, the FBI, and NSA urge all organizations, including critical infrastructure organizations, to implement the recommendations listed in the Mitigations section of this joint advisory."

The law enforcement organizations noted that BlackMatter operates as ransomware-as-a-service and may possibly be a rebrand of [DarkSide](https://www.zdnet.com/article/darkside-the-ransomware-group-responsible-for-colonial-pipeline-cyberattack-explained/), a ransomware group that [allegedly closed shop](https://www.zdnet.com/article/russian-language-cybercriminal-forum-xss-bans-darkside-and-other-ransomware-groups/) in May after attacking [Colonial Pipeline](https://www.zdnet.com/article/colonial-pipeline-ransomware-attack-everything-you-need-to-know/). 

They added that BlackMatter has demanded ransom payments ranging from $80,000 to $15,000,000 in Bitcoin and Monero.






"Notably, this variant of BlackMatter leverages the embedded credentials and SMB protocol to remotely encrypt, from the original compromised host, all discovered shares' contents, including ADMIN$, C$, SYSVOL, and NETLOGON. BlackMatter actors use a separate encryption binary for Linux-based machines and routinely encrypt ESXi virtual machines. Rather than encrypting backup systems, BlackMatter actors wipe or reformat backup data stores and appliances," the advisory explained.

"BlackMatter leverages legitimate remote monitoring and management software and remote desktop software, often by setting up trial accounts, to maintain persistence on victim networks. BlackMatter attempts to exfiltrate data for extortion. BlackMatter remotely encrypts shares via SMB protocol and drops a ransomware note in each directory. BlackMatter may wipe backup systems."

The notice lists dozens of measures organizations should take to protect themselves from BlackMatter, including the implementation of detection signatures, strong passwords, MFA, routine patching, network segmentation and access limitations.

Due to the increase in ransomware attacks [on weekends and holidays](https://www.zdnet.com/article/fbi-cisa-warns-of-potential-cyberattacks-over-labor-day-weekend/), CISA suggested organizations implement time-based access for accounts set at the admin-level and higher.

In September, the [FBI released its own notice](https://www.zdnet.com/article/fbi-warns-of-ransomware-attacks-targeting-food-and-agriculture-sector-as-white-house-pushes-for-proactive-measures/) warning companies in the food and agriculture sector to watch out for ransomware attacks aiming to disrupt supply chains. The FBI note said ransomware groups are seeking to "disrupt operations, cause financial loss, and negatively impact the food supply chain." 

"Ransomware may impact businesses across the sector, from small farms to large producers, processors and manufacturers, and markets and restaurants. Cybercriminal threat actors exploit network vulnerabilities to exfiltrate data and encrypt systems in a sector that is increasingly reliant on smart technologies, industrial control systems, and internet-based automation systems," the FBI said. 

"Food and agriculture businesses victimized by ransomware suffer significant financial loss resulting from ransom payments, loss of productivity, and remediation costs. Companies may also experience the loss of proprietary information and personally identifiable information and may suffer reputational damage resulting from a ransomware attack."

The notice listed multiple attacks on the food and agriculture sector since November, including a Sodinokibi/REvil ransomware attack on a US bakery company, the attack on [global meat processor JBS](https://www.zdnet.com/article/jbs-usa-cyber-attack-affecting-north-american-and-australian-systems/) in May, a March 2021 attack on a US beverage company and a January attack on a US farm that caused losses of approximately $9 million. 

In November 2020, the FBI also cited an attack on a US-based international food and agriculture business that was hit with a $40 million ransom demand from the OnePercent Group. The company was able to recover from backups and did not pay the ransom.





#### Tags:
[[BlackMatter]] [[ransomware]] [[CISA,]] [[NSA]] [[ZDNet]]
