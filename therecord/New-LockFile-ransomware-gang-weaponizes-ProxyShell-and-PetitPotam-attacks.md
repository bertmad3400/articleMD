# New LockFile ransomware gang weaponizes ProxyShell and PetitPotam attacks
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/new-lockfile-ransomware-gang-weaponizes-proxyshell-and-petitpotam-attacks/)
+ Date: August 22, 2021
+ Author: Catalin Cimpanu


## Article:
![New LockFile ransomware gang weaponizes ProxyShell and PetitPotam attacks](https://therecord.media/wp-content/uploads/2021/08/ransomware.png)

A new ransomware group has weaponized two recently disclosed vulnerabilities in order to improve their chances at breaching, taking over, and encrypting corporate networks.


Named **LockFile**, this new ransomware gang has been seen exploiting a vulnerability known as ProxyShell to gain access to Microsoft Exchange email servers, from where it pivots to companies’ internal networks, according to reports from security firm [TG Soft](https://twitter.com/VirITeXplorer/status/1428750497872232459) and security researcher [Kevin Beaumont](https://doublepulsar.com/multiple-threat-actors-including-a-ransomware-gang-exploiting-exchange-proxyshell-vulnerabilities-c457b1655e9c).


Once inside, LockFile operators abuse an attack method known as PetitPotam to take over a company’s Windows domain controller and then deploy their file-encrypting payloads to connected workstations, according to a [report](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/lockfile-ransomware-new-petitpotam-windows) published on Friday by security firm Symantec.


Details about the PetitPotam attack and the ProxyShell vulnerability have been disclosed at the [end of July](https://github.com/topotam/PetitPotam) and [early](https://peterjson.medium.com/reproducing-the-proxyshell-pwn2own-exploit-49743a4ea9a1) [August](https://www.zerodayinitiative.com/blog/2021/8/17/from-pwn2own-2021-a-new-attack-surface-on-microsoft-exchange-proxyshell), respectively, showing once again that cybercrime gangs are quite quick to weaponize exploits when they enter the public domain.





Symantec said the group has already hit at least ten organizations, with most of its victims based in the US and Asia.


“The LockFile ransomware was first observed on the network of a US financial organization on July 20, 2021, with its latest activity seen as recently as August 20,” the company said last week.


Currently, details about this ransomware operation are still scarce. What is known is that LockFile is trying to mimic the visual style of the ransom notes used by [LockBit](https://therecord.media/australian-cybersecurity-agency-warns-of-spike-in-lockbit-ransomware-attacks/), a more well-known ransomware gang that recently has seen a spike in use in the criminal underworld.


![LockFile-ransom](https://www-therecord.recfut.com/wp-content/uploads/2021/08/LockFile-ransom-1024x409.jpg)Image: Symantec
To prevent the LockFile gang from gaining access to their systems, companies are advised to apply patches for the PetitPotam and ProxyShell vulnerabilities.


PetitPotam patches and mitigations are detailed [here](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36942).  
  
ProxyShell security patches have shipped with May and July Windows security updates ([CVE-2021-31207](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31207), [CVE-2021-34473](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34473), and [CVE-2021-34523](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34523)).





#### Tags:
[[ransomware]] [[LockFile]] [[PetitPotam]] [[ProxyShell]] [[The Record]]
