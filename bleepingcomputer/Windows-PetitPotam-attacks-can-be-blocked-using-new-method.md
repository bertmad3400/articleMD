# Windows PetitPotam attacks can be blocked using new method
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-petitpotam-attacks-can-be-blocked-using-new-method/)
+ Date: August 2, 2021
+ Author: Lawrence Abrams


## Article:
![Securing Windows](https://www.bleepstatic.com/content/hl-images/2021/05/26/Microsoft-Defender_(1).jpg)


Security researchers have devised a way to block the recently disclosed PetitPotam attack vector that allows hackers to take control of a Windows domain controller easily.


Last month, security researcher GILLES Lionel [disclosed a new method called PetitPotam](https://www.bleepingcomputer.com/news/microsoft/new-petitpotam-attack-allows-take-over-of-windows-domains/) that forces a Windows machine, including a Windows domain controller, to authenticate against a threat actor's malicious NTLM relay server using the Microsoft Encrypting File System Remote Protocol ([EFSRPC](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-efsr/08796ba8-01c8-4872-9221-1000ec2eff31)).



Threat actors would then relay this authentication request to a targeted domain's Active Directory Certificate Services via HTTP., where the attacker would be given a Kerberos ticket-granting ticket (TGT), allowing them to assume the domain controller's identity.


After the vector was disclosed, researchers quickly began testing the method and illustrated how easy it was to dump credentials and take over a Windows domain.



Using this attack, a threat actor can take complete control over a Windows domain, including pushing out new group policies, scripts, and deploying malware on all devices, such as ransomware.


Last week, Microsoft released an advisory titled '[Mitigating NTLM Relay Attacks on Active Directory Certificate Services (AD CS)](https://support.microsoft.com/en-us/topic/kb5005413-mitigating-ntlm-relay-attacks-on-active-directory-certificate-services-ad-cs-3612b773-4043-4aa9-b23d-b87910cd3429)' that explains how to mitigate NTLM relay attacks.


"To prevent NTLM Relay Attacks on networks with NTLM enabled, domain administrators must ensure that services that permit NTLM authentication make use of protections such as [Extended Protection for Authentication (EPA)](https://docs.microsoft.com/en-us/security-updates/securityadvisories/2009/973811) or signing features such as SMB signing," explained Microsoft's advisory.


"PetitPotam takes advantage of servers where Active Directory Certificate Services (AD CS) is not configured with protections for NTLM Relay Attacks. The mitigations outlined in [KB5005413](https://support.microsoft.com/help/5005413)* instruct customers on how to protect their AD CS servers from such attacks."


While Microsoft's suggestions may prevent NTLM relay attacks, they do not provide any guidance on blocking PetitPotam, which can be used as a vector for other attacks.


"It can be used for different attacks too like NTLMv1 downgrade and relaying machine account on computers where this machine account is local admin," Lionel told BleepingComputer when he first disclosed the attack vector.


Microsoft's response to recent vulnerabilities, such as PetitPotam, [SeriousSAM](https://www.bleepingcomputer.com/news/microsoft/new-windows-10-vulnerability-allows-anyone-to-get-admin-privileges/), and [PrintNightmare](https://www.bleepingcomputer.com/tag/printnightmare/) have been very concerning for security researchers who feel that Microsoft is not doing enough to protect its customers.




> 
> I’d like to clarify my position on [#Microsoft](https://twitter.com/hashtag/Microsoft?src=hash&ref_src=twsrc%5Etfw) in general  
>   
> 
> Many things have improved over the last 10 years .. a lot .. especially with Windows 10/2016.  
> 
> Today many fellow security researchers that I highly respect work there.  
>   
> 
> I criticize Microsoft’s response to recent ..
> 
> 
> — Florian Roth  (@cyb3rops) [August 1, 2021](https://twitter.com/cyb3rops/status/1421846897262796800?ref_src=twsrc%5Etfw)


Blocking PetitPotam attacks using NETSH filters
-----------------------------------------------


The good news is that researchers have figured out a way to block the remote unauthenticated PetitPotam attack vector using NETSH filters without affecting local EFS functionality.


NETSH is a Windows command-line utility that allows administrators to configure network interfaces, add filters, and modify the Windows firewall configuration.


This weekend, [Craig Kirby](https://twitter.com/craigkirby) shared a NETSH RPC filter that blocks remote access to the MS-EFSRPC API,  effectively blocking the unauthenticated PetitPotam attack vector.


According to security researcher [Benjamin Delpy](https://twitter.com/gentilkiwi/status/1421949715986403329), you can use this filter by copying the following contents into a file called 'block\_efsr.txt' and saving it on your desktop.


Now open an elevated command prompt and type the following command to import the filter using NETSH.


You can verify that the filters have been added by running the following command:


After running the command, netsh should display two filters, one for c681d488-d850-11d0-8c52-00c04fd90f7e and another for df1941c5-fe89-4e79-bf10-463657acf44d, as shown below.



![Configured NETSH RPC filters to block PetitPotam](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/p/petitpotam/netsh-show-filter.jpg)**Configured NETSH RPC filters to block PetitPotam**
With these filters in place, the PetitPotam vector will no longer work, but EFS will continue to operate normally on the device.


If Microsoft ever fixes the API to prevent this vector, you can remove the filters using the following command:


The filterkey can be found when displaying the list of configured filters as described above.




#### Tags:
[[Windows]] [[NTLM]] [[PetitPotam]] [[Microsoft]] [[NETSH]] [[Bleeping Computer]]
