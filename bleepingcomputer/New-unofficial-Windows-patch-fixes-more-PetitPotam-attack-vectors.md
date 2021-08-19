# New unofficial Windows patch fixes more PetitPotam attack vectors
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-unofficial-windows-patch-fixes-more-petitpotam-attack-vectors/)
+ Date: August 19, 2021
+ Author: Lawrence Abrams


## Article:
![Windows security](https://www.bleepstatic.com/content/hl-images/2021/05/26/Microsoft--Defender.jpg)


A second unofficial patch for the Windows PetitPotam NTLM relay attack has been released to fix further issues not addressed by Microsoft's official security update.


An NTLM relay attack is when a threat actor can force a server or domain controller to authenticate against an NTLM relay server under a threat actor's control.


This NTLM relay would then forward the request to a targeted victim's Active Directory Certificate Services via HTTP to receive a Kerberos ticket-granting ticket (TGT), which allows the attacker to assume the identity of the domain controller and take over the Windows domain.


In the past, there have been numerous ways to force a domain controller to authenticate against a threat actor's relay server, such as the MS-RPRN printing API, which Microsoft has fixed.


In July, security researcher GILLES Lionel, aka [Topotam](https://twitter.com/topotam77), disclosed a new technique called '[PetitPotam](https://www.bleepingcomputer.com/news/microsoft/new-petitpotam-attack-allows-take-over-of-windows-domains/)' that performs unauthenticated forced authentication on domain controllers using various functions in the [MS-EFSRPC](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-efsr/08796ba8-01c8-4872-9221-1000ec2eff31) (Microsoft Encrypted File System) API.


Microsoft's security update is not complete
-------------------------------------------


Due to the critical nature of this attack, [Microsoft released a security update](https://www.bleepingcomputer.com/news/microsoft/windows-security-update-blocks-petitpotam-ntlm-relay-attacks/) as part of the [August 2021 Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/microsoft-august-2021-patch-tuesday-fixes-3-zero-days-44-flaws/) that attempted to fix the PetitPotam vulnerability, tracked as CVE-2021-36942.


"An unauthenticated attacker could call a method on the LSARPC interface and coerce the domain controller to authenticate against another server using NTLM," explains Microsoft in the [CVE-2021-36942 advisory](http://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-36942).


Unfortunately, Microsoft's update is incomplete, and it is still possible to abuse PetitPotam.


As part of this patch, Microsoft fixed the unauthenticated vector for all EFSRPC functions and only completely blocks the forced negotiation for the [OpenEncryptedFileRawA](https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-openencryptedfilerawa) and [OpenEncryptedFileRawW](https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-openencryptedfileraww) API functions when called via an LSARPC named pipe.


A named pipe is an Windows interface that allows processes on the same or different systems to communicate with each other. These named pipes expose API functions that can be called by other processes to perform various tasks.


However, Microsoft's update did not block the OpenEncryptedFileRawA/OpenEncryptedFileRawWs function via the MS-EFSRPC named pipe, and threat actors can still abuse other functions via both LSARPC and EFSRPC.


"At least three other function can be abused that they didn't block/patch. Some on twitter already pointed out them and can be "easily" found if people look for," Lionel told BleepingComputer last week.


Since then, Lionel has updated PetitPotam to support the following other EFSRPC functions that were not blocked by Microsoft's security update:


Furthermore, even though Microsoft fixed the unauthenticated issue, it is common for threat actors to gain access to network credentials that could still be used to trigger this attack.


Unofficial patch fixes these unresolved issues
----------------------------------------------


To provide a more complete patch, the [0patch micropatching service](https://0patch.com/) has released an updated unofficial patch that can be used to block all known PetitPotam NTLM relay attacks on the following Windows versions:


1. **Windows Server 2019** (updated with July 2021 Updates)
2. **Windows Server 2016** (updated with July 2021 Updates)
3. **Windows Server 2012 R2** (updated with July 2021 Updates)
4. **Windows Server 2008 R2** (updated with January 2020 Updates, no Extended Security Updates)


With this micropatch, the functions are blocked in both the LSARPC and EFSRPC named pipes and can no longer be exploited as part of an NTLM relay attack.


"What we did was patch just one function that is called from all these and is responsible for sending System's credentials to attacker's endpoint," 0patch cofounder [Mitja Kolsek](https://twitter.com/mkolsek) told BleepingComputer.


"As with our previous patch, we enclosed this function in an impersonation block, resulting in attacker only getting their own credentials back instead of System's."


For those who wish to wait for a possible official patch from Microsoft, you can also defend against PetitPotam attacks [using NETSH RPC filters](https://www.bleepingcomputer.com/news/microsoft/windows-petitpotam-attacks-can-be-blocked-using-new-method/) that block remote access to the MS-EFSRPC API.




#### Tags:
[[Microsoft]] [[Windows]] [[NTLM]] [[PetitPotam]] [[LSARPC]] [[(updated]] [[Updates)]] [[MS-EFSRPC]] [[patch,]] [[EFSRPC]] [[Bleeping Computer]]
