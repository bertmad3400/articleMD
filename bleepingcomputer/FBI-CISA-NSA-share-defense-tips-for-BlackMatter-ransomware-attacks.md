# FBI, CISA, NSA share defense tips for BlackMatter ransomware attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/fbi-cisa-nsa-share-defense-tips-for-blackmatter-ransomware-attacks/)
+ Date: October 18, 2021
+ Author: Ionut Ilascu


## Article:
![FBI, CISA, and NSA share tips to prevent BlackMatter ransomware attacks](https://www.bleepstatic.com/content/hl-images/2021/08/05/BlackMatter-ransomware.jpg)


The Cybersecurity and Infrastructure Security Agency (CISA), the Federal Bureau of Investigation (FBI), and the National Security Agency (NSA) published today an advisory with details about how the BlackMatter ransomware gang operates.


The three agencies also provide information that can help organizations defend the activity of this adversary on the network and defend against it


BlackMatter ransomware-as-a-service activity started in July with the clear goal of breaching corporate networks belonging to businesses in the U.S., Canada, Australia, and the U.K. with a revenue of at least $100 million.


An announcement from the gang showed that they were looking to [buy access](https://www.bleepingcomputer.com/news/security/blackmatter-ransomware-gang-rises-from-the-ashes-of-darkside-revil/) to such networks for as much as $100,000 as long as it was not for hospitals, critical infrastructure, non-profit, defense industry, and government organizations.


### Compromised credentials


BlackMatter is responsible for encrypting systems at multiple organizations in the U.S. and asking ransoms that go as high as $15 million in cryptocurrency.


The joint cybersecurity advisory from CISA, the FBI, and the NSA shares the tactics, techniques, and procedures associated with BlackMatter activity that could help organizations protect against the BlackMatter ransomware gang.


One variant of the malware analzed in an isolated environment shows that the threat actor used compromised administrator credentials to discover all the hosts in the victim's Active Directory.


It also used Microsoft Remote Procedure Call (MSRPC) function (srvsvc.NetShareEnumAll) that allowed listing all accessible network shares for each host.



"Notably, this variant of BlackMatter leverages the embedded credentials and SMB protocol to remotely encrypt, from the original compromised host" - [joint advisory](https://us-cert.cisa.gov/ncas/alerts/aa21-291a) from CISA, FBI, and NSA



The BlackMatter file-encrypting malware also has a version for Linux-based systems that can [encrypt VMware ESXi virtual servers](https://www.bleepingcomputer.com/news/security/linux-version-of-blackmatter-ransomware-targets-vmware-esxi-servers/), which are common in enterprise environments for resource management purposes.


The advisory today warns that, unlike other ransomware actors that encrypt backup data stores and appliances, the BlackMatter gang wipes or reformats them.


### Detecting and defending


Based on identified TTPs associated with BlackMatter ransomware, the three agencies created signatures for the open-source Snort network intrusion detection and prevention system that can alert when a remote encryption process initiates.


**Intrusion Detection System Rule:**


**Inline Intrusion Prevention System Rule:**


To counter BlackMatter ransomware attacks, CISA, the FBI, and the NSA shares a set of cybersecurity measures that start from the basic password hygiene and go to mitigations designed to minimize the Active Directory attack surface.


![CISA, FBI, NSA mitigations for BlackMatter ransomware attacks](https://www.bleepstatic.com/images/news/u/1100723/Ransomware/BlackMatter/BlackMatterRnsmMitigs.jpg)



Apart from using the Snort signatures above, the agencies recommend using strong, unique passwords for various accounts, such as admin, service, and domain administrators.


Multi-factor authentication should be active for all services that support the feature. This requirement is important particularly for webmail, virtual private networks, and accounts that access critical systems.


Installing security patches on time remains "one of the most efficient and cost-effective steps an organization can take to minimize its exposure to cybersecurity threats."


Additional mitigation advice in the advisory refers to the following:


* limit access to resources over the network to necessary services and user accounts
* network segmentation and traversal monitoring to hinder network visibility and mapping, and to learn of unusual activity indicative of lateral movement
* time-based access for accounts with admin privileges and above for a limited timeframe necessary for completing a task
* disable command-line and scripting activities and permissions to prevent privilege escalation and lateral movement
* keep regularly maintained offline backups that are encrypted and immutable - it cannot be altered, the so-called write-once-read-many (WORM) storage device


For critical infrastructure organizations, CISA, the FBI, and NSA released a special set of supplementary mitigations that should be prioritized:


* Disable the storage of clear-text passwords in LSASS memory.
* Consider disabling or limiting New Technology Local Area Network Manager (NTLM) and WDigest Authentication
* Implement Credential Guard for Windows 10 and Server 2016. For Windows Server 2012R2, enable Protected Process Light for Local Security Authority (LSA)
* Minimize the AD attack surface to reduce malicious ticket-granting activity. Malicious activity such as “Kerberoasting” takes advantage of Kerberos’ Ticket Granting service and can be used to obtain hashed credentials that attackers attempt to crack


BlackMatter is among the top ransomware threats today. It emerged from the DarkSide ransomware gang, which shut down after the infamous [attack on Colonial Pipeline](https://www.bleepingcomputer.com/news/security/colonial-pipeline-restores-operations-5-million-ransom-demanded/) in May.


The threat actor steals data from its victims before the encryption stage and publishes the files on their leak site unless they get the ransom.


At the moment, their site lists victims from various industry sectors (clothing, beverage, software, investment, technology) that did not pay the ransom, many of them based in the U.S.


Recently, the gang breached business software solutions provider [Marketron](https://www.bleepingcomputer.com/news/security/marketron-marketing-services-hit-by-blackmatter-ransomware/), the U.S. farmers cooperative [NEW Cooperative](https://www.bleepingcomputer.com/news/security/us-farmer-cooperative-hit-by-59m-blackmatter-ransomware-attack/), and technology giant [Olympus](https://www.bleepingcomputer.com/news/security/blackmatter-ransomware-hits-medical-technology-giant-olympus/).




#### Tags:
[[BlackMatter]] [[ransomware]] [[CISA,]] [[FBI,]] [[NSA]] [[U.S.]] [[cybersecurity]] [[Bleeping Computer]]
