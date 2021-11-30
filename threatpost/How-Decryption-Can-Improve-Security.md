# How Decryption Can Improve Security
### 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176613)
+ Date: November 30, 2021  3:58 pm
+ Author: Jeff Costlow


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/30145114/Tech-resized.jpg)
Strong encryption is critical to protecting sensitive business and personal data. Google estimates that 95 percent of its internet traffic uses the encrypted HTTPS protocol, and most industry analyst firms conclude that between 80-90 percent of network traffic is encrypted today. This is a significant step forward for data integrity and consumer privacy.


However, organizations with a commitment to data privacy aren’t the only ones who see value in obscuring their digital footprint in encrypted traffic. Cybercriminals have been quick to weaponize encryption as a means to hide their malicious activity in otherwise benign traffic.


Gartner shared that [70 percent of malware campaigns](https://www.gartner.com/imagesrv/media-products/pdf/radware/Radware-1-2Y7FR0I.pdf) in 2020 used some type of encryption. And Zscaler is blocking 733 million encrypted attacks per month this year, an increase of 260 percent over 2019.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


According to a [Joint Cybersecurity Advisory](https://us-cert.cisa.gov/sites/default/files/publications/AA21-209A_Joint_CSA%20Top%20Routinely%20Exploited%20Vulnerabilities.pdf) issued by the FBI, CISA, the U.K. National Cyber Security Centre and the Australian Cyber Security Centre, encrypted protocols are used to mask lateral movement and other advanced tactics in 60 percent of attacks using the 30 most exploited network vulnerabilities. Put another way, organizations are blind to 60 percent of CISA’s [most exploited vulnerabilities.](https://us-cert.cisa.gov/ncas/alerts/aa20-133a)


Security researchers have also found sophisticated emerging attack techniques with line-rate decryption of the most commonly abused Microsoft protocols, such as SMBv3, Active Directory Kerberos, Microsoft Remote Procedure Call (MS-RPC), NTLM, LDAP, WINRM, in addition to TLS 1.3.


All of this has catalyzed the need for a new approach when it comes to detecting threats within encrypted traffic: namely, decryption. Decryption can detect post-compromise activity that encrypted traffic analysis (ETA) misses, including ransomware campaigns that exploit the PrintNightmare vulnerability.


Today, it’s nearly impossible to tell the good from the bad without the ability to decrypt traffic securely. The ability to remain invisible has given cyberattackers the upper hand. Encrypted traffic has been exploited in some of the biggest cyberattacks and exploit techniques of the past year, from Sunburst and Kaseya to PrintNightmare and ProxyLogon. Attack techniques such as living-off-the-land and Active Directory Golden Ticket are only successful because attackers can exploit organizations’ encrypted traffic. Ransomware is also top of mind for enterprises right now, yet many are crippled by the fact that they cannot see what is happening laterally within the east-west traffic corridor.


Organizations have been wary to embrace decryption due to concerns around compliance, privacy and security, as well as performance impacts and high compute costs. But there are ways to decrypt traffic without compromising compliance, security, privacy or performance. Let’s debunk some of the common myths and misconceptions.


**Myth 1:** Decryption Weakens Security
---------------------------------------


**Truth:** There are two main kinds of decryption: Out-of-band and in-line. Out-of-band decryption sends de-identified and tokenized data to the cloud for machine learning. This means it never sends any cleartext data across the network, so there are no additional security concerns.


Inline decryption, also known as SSL interception or man-in-the-middle (MitM), is an older approach that can result in organizations experiencing additional complications with certificate management, and attackers may perform downgrade attacks where messages are re-encrypted using weaker cipher suites.


**Myth 2:** Decryption Violates Privacy Laws & Compliance Standards
-------------------------------------------------------------------


**Truth:** Decryption of enterprise network traffic does not violate privacy regulations or laws. However, some decryption capabilities cannot be configured on sensitive subnets to avoid violation of compliance frameworks such as GDPR, PCI DSS and HIPAA. Organizations must proactively avoid recording data relevant to compliance frameworks, and have user access controls to ensure that only authorized users have access to packet-level data.


**Myth 3**: Encrypted Traffic Cannot Be Accessed by Attackers
-------------------------------------------------------------


**Truth**: Deprecated encryption protocols such as SSL and TLS 1.0 and 1.1 may leave traffic vulnerable to sniffing and decryption by sophisticated attackers.


**Myth 4**: Encrypted Traffic Provides No Benefit to Attackers
--------------------------------------------------------------


**Truth**: While most companies use encryption to ensure the privacy of their data, cybercriminals have also become adept at using the same technology to cover up their tracks.


The benefits of decrypting network traffic are many. First, decryption enables the detection of attacks earlier in an attack campaign because malicious payloads are no longer hidden. Second, decryption improves mean time to response because it provides valuable context to ensure rapid detection, scoping, investigation and remediation of threats. And finally, decryption allows a full forensic record for post-compromise investigations.


***Jeff Costlow is the CISO at [ExtraHop](https://www.extrahop.com/)***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by [visiting our microsite](https://threatpost.com/microsite/infosec-insiders-community/)***




#### Tags:
[[Truth:]] [[traffic.]] [[ThreatPost]]
