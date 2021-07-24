# New PetitPotam attack allows take over of Windows domains
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/new-petitpotam-attack-allows-take-over-of-windows-domains/)
+ Date: July 23, 2021
+ Author: Lawrence Abrams


## Article:
![Microsoft](https://www.bleepstatic.com/content/hl-images/2021/05/17/0_Windows-headpic.jpg)


A new NTLM relay attack called PetitPotam has been discovered that allows threat actors to take over a domain controller, and thus an entire Windows domain.


Many organizations utilize Microsoft Active Directory Certificate Services, which is a public key infrastructure (PKI) server that can be used to authenticate users, services, and machines on a Windows domain.


In the past, [researchers discovered a method](https://posts.specterops.io/certified-pre-owned-d95910965cd2) to force a domain controller to authenticate against a malicious NTLM relay that would then forward the request to a domain's Active Directory Certificate Services via HTTP.


Ultimately, the attacker would be granted a Kerberos ticket granting ticket (TGT) that would allow them to assume the identity of any device on the network, including a domain controller.


To force the machine to perform the authentication to a remote server, an attacker could use the *RpcRemoteFindFirstPrinterChangeNotification* function of MS-RPRN printing API.


"Microsoft’s Print Spooler is a service handling the print jobs and other various taks related to printing. An attacker controlling a domain user/computer can, with a specific RPC call, trigger the spooler service of a target running it and make it authenticate to a target of the attacker's choosing," a [blog post](https://www.thehacker.recipes/active-directory-domain-services/movement/mitm-and-coerced-authentications/ms-rprn) on Hacker.recipes explains.


"This flaw is a "won't fix" and enabled by default on all Windows environments."


If this attack is successful, the attacker could take over the domain controller and perform any command they wish, effectively taking over the Windows domain.


Since this attack was disclosed, many organizations have disabled MS-RPRN to block the attack vector.


Introducing PetitPotam
----------------------


This week, French security researcher GILLES Lionel, aka [Topotam](https://twitter.com/topotam77),  disclosed a new technique called 'PetitPotam' that performs an NTLM relay attack that does not rely on the MS-RPRN API but instead uses the EfsRpcOpenFileRaw function of the [MS-EFSRPC](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-efsr/08796ba8-01c8-4872-9221-1000ec2eff31) API.


MS-EFSRPC is Microsoft's Encrypting File System Remote Protocol that is used to perform "maintenance and management operations on encrypted data that is stored remotely and accessed over a network."




> 
> Hi all,  
> 
> MS-RPRN to coerce machine authentication is great but the service is often disabled nowadays by admins on most orgz.  
> 
> Here is one another way we use to elicit machine account auth via MS-EFSRPC. Enjoy!! :)<https://t.co/AGiS4f6yt8>
> 
> 
> — topotam (@topotam77) [July 18, 2021](https://twitter.com/topotam77/status/1416833996923809793?ref_src=twsrc%5Etfw)


Lionel has released a proof-of-concept script for the PetitPotam technique [on GitHub](https://github.com/topotam/PetitPotam) that can be used to force a domain controller to authenticate against a remote NTLM under an attacker's control using the MS-EFSRPC API.


In a conversation with BleepingComputer about the new relay attack method, Lionel stated that he does not see this as a vulnerability but rather the abuse of a legitimate function. 


"In my eyes, this is not a vulnerability but an abuse of a legitimate function. Function that shouldn't use the machine account to authenticate like in the printerbug for example," Lionel shared with BleepingComputer.


In addition to the attack relaying SMB authentication to an HTTP certificate enrollment server allowing full take over of the domain controller, Lionel said it could be used for other attacks.


These additional attacks include "NTLMv1 downgrade and relaying machine account on computers where this machine account is local admin (SCCM, exchange server, are often in this situation for example).


The researcher says the only way to mitigate this technique is to disable NTLM authentication or enable protections, such as SMB signing, LDAP signing, and channel binding.


Unfortunately, no way has been found to disable the EfsRpcOpenFileRaw from being used to relay authentication requests. 


Lionel told us that stopping the EFS service does not prevent the technique from being exploited.


BleepingComputer has contacted Microsoft about this new attack but has not heard back at this time.


PetitPotam is 'brutal'
----------------------


Since the release of PetitPotam, security researchers have been quick to test the PoC and its effectiveness.


"Finally finished testing it, it's quite brutal! Network access to full AD takeover... I really underestimated the impact of NTLM relay on PKI ESC8 The combo with PetitPotam is awesome!," [tweeted](https://twitter.com/remiescourrou/status/1418232548677804032) security researcher [Rémi Escourrou](https://twitter.com/remiescourrou).


"Actually, no way to block PetitPotam (to my current knowledge) but you can harden the HTTP service of the PKI to avoid the NTLM relay," Escourrou told BleepingComputer in a conversation last night.


Security researcher and Mimikatz creator [Benjamin Delpy](https://twitter.com/gentilkiwi) also tested the new technique, where he created a video, shown below, demonstrating how threat actors can abuse it.





#### Tags:
[[NTLM]] [[PetitPotam]] [[Windows]] [[Microsoft]] [[MS-RPRN]] [[API]] [[MS-EFSRPC]] [[BleepingComputer]] [[PKI]] [[HTTP]] [[Bleeping Computer]]
