# Microsoft Rushes Fix for ‘PetitPotam’ Attack PoC
### Microsoft releases mitigations for a Windows NT LAN Manager exploit that forces remote Windows systems to reveal password hashes that can be easily cracked. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168163)
+ Date: July 26, 2021  3:33 pm
+ Author: Tom Spring


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26141726/Windows-Abstract.jpg)
Microsoft was quick to respond with a fix to an attack dubbed “PetitPotam” that could force remote Windows systems to reveal password hashes that could then be easily cracked. To thwart an attack, Microsoft recommends system administrators stop using the now deprecated Windows NT LAN Manager (NTLM).


Security researcher Gilles Lionel first identified the bug on Thursday and also [published](https://github.com/topotam/PetitPotam) proof-of-concept (PoC) exploit code to demonstrate the attack. The following day, [Microsoft issued an advisory](https://msrc.microsoft.com/update-guide/vulnerability/ADV210003) that included workaround mitigations to protect systems.


The PetitPotam bug is tied to the Windows operating system and the abuse of a remote access protocol called Encrypting File System Remote Protocol (MS-EFSRPC). The protocol is designed to allow Windows systems to access remote encrypted data stores, allowing for management of the data while enforcing access control policies.



The PetitPotam PoC is a form of manipulator-in-the-middle (MitM) attack against Microsoft’s NTLM authentication system. Next, an attacker uses the file-sharing protocol Server Message Block (SMB) to request access to a remote system’s MS-EFSRPC interface. According to Lionel, this forces the targeted computer to initiate an authentication procedure and share its authentication details via NTLM.


**NTLM: Persona Non Grata Protocol**
------------------------------------


Because the NTLM protocol is an insufficient authentication protocol that’s nonetheless used to relay authentication details, hashed passwords can be scooped up by an attacker and later cracked offline with minimal effort. NTLM has a long list of criticisms that [date back to 2010](https://threatpost.com/ntlm-authentication-still-security-risk-081310/74330/), when even then it was seen as an insufficient authentication protocol.


“NTLM is susceptible to relay attacks, which allows actors to capture an authentication and relay it to another server, granting them the ability to perform operations on the remote server using the authenticated user’s privileges,” wrote researchers at Preempt in [a 2019 report](https://threatpost.com/critical-microsoft-rce-bugs-windows/145572/).


**Attack Scenario**
-------------------


According to Lionel, this similar scenario can be played out with a PetitPotam attack. He demonstrated how a PetitPotam attack can be chained to an exploit targeting Windows Active Directory Certificate Services (AD CS), which provides public key infrastructure (PKI) functionality.


Researchers at Truesec break it down further in a blog [post published Sunday](https://blog.truesec.com/2021/07/25/mitigating-ntlm-relay-attacks-on-active-directory-certificate-services-ad-cs-adv210003-kb5005413-petitpotam/).


“An attacker can target a Domain Controller to send its credentials by using the MS-EFSRPC protocol and then relaying the DC [domain controller] NTLM credentials to the Active Directory Certificate Services AD CS Web Enrollment pages to enroll a DC certificate. … This will effectively give the attacker an authentication certificate that can be used to access domain services as a DC and compromise the entire domain.”


**PetitPotam Mitigation Options**
---------------------------------


In response to the public availability of the PoC, Microsoft was quick to respond, outlining several mitigation options. For starters, Microsoft recommends disabling NTLM authentication on Windows domain controllers. It also suggests enabling the Extended Protection for Authentication (EPA) feature on AD CS services.


“To prevent NTLM Relay Attacks on networks with NTLM enabled, domain administrators must ensure that services that permit NTLM authentication make use of protections such as [Extended Protection for Authentication (EPA)](https://docs.microsoft.com/en-us/security-updates/securityadvisories/2009/973811) or signing features such as SMB signing,” wrote Microsoft. “PetitPotam takes advantage of servers where Active Directory Certificate Services (AD CS) is not configured with protections for NTLM Relay Attacks. The mitigations outlined in [KB5005413](https://support.microsoft.com/help/5005413) instruct customers on how to protect their AD CS servers from such attacks.”


Microsoft also added that companies are vulnerable to a PetitPotam attack if NTLM authentication is enabled in their domains and/or they’re using AD CS with the services “Certificate Authority Web Enrollment” and “Certificate Enrollment Web Service.”


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[NTLM]] [[Microsoft]] [[PetitPotam]] [[Windows]] [[PoC]] [[MS-EFSRPC]] [[ThreatPost]]
