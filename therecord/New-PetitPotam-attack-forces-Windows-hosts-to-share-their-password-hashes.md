# New PetitPotam attack forces Windows hosts to share their password hashes
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/new-petitpotam-attack-forces-windows-hosts-to-share-their-password-hashes/)
+ Date: July 23, 2021
+ Author: Catalin Cimpanu


## Article:
![New PetitPotam attack forces Windows hosts to share their password hashes](https://therecord.media/wp-content/uploads/2021/07/Windows-bug.jpg)

A French security researcher has discovered a security flaw in the Windows operating system that can be exploited to force remote Windows machines to authenticate and share their password hashes with an attacker.


The issue, discovered by [Gilles Lionel](https://www.linkedin.com/in/lionel-gilles-04bb10bb/), a Paris-based French security researcher, was nicknamed **PetitPotam**, and proof-of-concept (PoC) code was published earlier this week [on GitHub](https://github.com/topotam/PetitPotam).


According to Lionel, the issue takes place when an attacker abuses [MS-EFSRPC](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-efsr/08796ba8-01c8-4872-9221-1000ec2eff31), a protocol that allows Windows machines to perform operations on encrypted data stored on remote systems.


The PetitPotam attack PoC code allows an attacker to send SMB requests to a remote system’s MS-EFSRPC interface and force the victim computer to initiate an authentication procedure and share its NTLM authentication hash.


Attackers can then collect this hash and abuse it in two ways, either by using it as part of a NTLM relay attack or by saving the hash and cracking it offline to obtain a cleartext version of the victim’s account password.


### A very very dangerous issue


PetitPotam is an incredibly powerful attack. Inside large corporate networks, attackers could use it to force domain controllers to cough up their passwords, which could lead to the complete takeover of a company’s internal network.





Furthermore, tests carried out by Gilles and several security researchers have shown that disabling support for MS-EFSRPC did not stop the attack from working.


The attack has been tested against Windows 10, Windows Server 2016, and Windows Server 2019 systems, but security researchers believe PetitPotam impacts most Windows versions supported today.


There are no known mitigations that can stop this attack. The Record will update this article once this information becomes available.


A Microsoft spokesperson did not return a request for comment sent before this article’s publication.


“The problem with this type of attack is that it will take a considerable amount of time and considerations to develop appropriate countermeasures,” [Florian Roth](https://twitter.com/cyb3rops), Head of Research at Nextron Systems, told The Record.


“These are design flaws that are more difficult to fix. It’s much easier to just patch a vulnerable font driver DLL or Internet Explorer library,” Roth added.


All in all, Microsoft is going through a rough patch, security-wise. This is the third major Windows security issue disclosed over the past month after the [PrintNightmare](https://therecord.media/poc-released-for-dangerous-windows-printnightmare-bug/) and [SeriousSAM (HiveNightmare)](https://therecord.media/serioussam-bug-impacts-all-windows-10-versions-released-in-the-past-2-5-years/) vulnerabilities.





#### Tags:
[[Windows]] [[PetitPotam]] [[MS-EFSRPC]] [[The Record]]
